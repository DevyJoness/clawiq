# Jira → local QA webhook

_Added: 2026-09-15_

## Purpose and boundaries

This integration adds an isolated local automation entry point for a Jira issue that enters **«В процессе проверки»**. It creates two separate Jira comments: **QA Checklist** and **Regression/Smoke Test**.

It is deliberately separate from the OpenClaw Gateway and Telegram interface. The service reads the current Jira issue, its configured acceptance-criteria field, linked Jira issues, and the ClawIQ documentation/source context before asking the local Ollama model to produce evidence-based test artifacts. The prompt prohibits invented requirements; missing evidence is explicitly identified as missing.

It never changes issue status, assignee, fields, or workflow. It does not use Rovo. Existing scheduled/hourly automation is not changed or disabled by this feature and should remain enabled until this flow has been verified with a test issue.

## Security model

- The service binds to `127.0.0.1` only. It is not directly reachable on the LAN.
- Cloudflare Tunnel exposes only this one HTTPS endpoint to Jira Cloud.
- Every webhook request must contain the configured `X-ClawIQ-Webhook-Secret`; validation is constant-time.
- Jira credentials and the tunnel credential stay outside Git. `.env` is ignored.
- The service accepts only `POST /webhooks/jira/qa-review`, a bounded JSON body, event `qa_review`, and the configured review status.
- A successful request returns `202` quickly; one local worker processes tasks serially. It prevents duplicate queued jobs and rechecks Jira comments immediately before writing.

## 1. Configure the local service

1. Copy `automation/jira_qa/.env.example` to `automation/jira_qa/.env`.
2. In Atlassian, create an API token for the account that is permitted to view issues and add comments in the intended project. Put its e-mail and token in the `.env` file.
3. Set `CLAWIQ_JIRA_BASE_URL` to the exact site URL, for example `https://example.atlassian.net`.
4. Generate a high-entropy webhook secret locally and put it in `CLAWIQ_JIRA_WEBHOOK_SECRET`. For PowerShell:

   ```powershell
   [Convert]::ToBase64String((1..48 | ForEach-Object { Get-Random -Maximum 256 }))
   ```

5. If acceptance criteria use a Jira custom field, set `CLAWIQ_JIRA_ACCEPTANCE_CRITERIA_FIELD` to its REST field ID, such as `customfield_12345`. Leave it unset only when criteria are part of the description.
6. Start Ollama with the configured local model (`qwen3:14b` by default), then start the webhook:

   ```powershell
   .\scripts\Start-JiraQaWebhook.ps1
   ```

7. In a second terminal, verify local health:

   ```powershell
   Invoke-RestMethod http://127.0.0.1:8787/healthz
   ```

The `.env` file is intentionally not a deployment mechanism. For a longer-running Windows installation, place equivalent values in a protected service environment or user environment; never log, commit, or paste them into Jira Automation.

## 2. Publish only the endpoint with Cloudflare Tunnel

Install `cloudflared`, authenticate with the Cloudflare account that owns the chosen hostname, and create a named tunnel. Do not use a Quick Tunnel for production.

```powershell
cloudflared tunnel login
cloudflared tunnel create clawiq-jira-qa
cloudflared tunnel route dns clawiq-jira-qa jira-qa.example.com
```

Create the Cloudflare configuration in Cloudflare's protected configuration directory (not in this repository). Replace the tunnel ID and credential-file path created by Cloudflare:

```yaml
tunnel: <tunnel-id>
credentials-file: C:\Users\<you>\.cloudflared\<tunnel-id>.json
ingress:
  - hostname: jira-qa.example.com
    service: http://127.0.0.1:8787
  - service: http_status:404
```

Run it with:

```powershell
cloudflared tunnel --config C:\Users\<you>\.cloudflared\config.yml run clawiq-jira-qa
```

The resulting public target is `https://jira-qa.example.com/webhooks/jira/qa-review`. Cloudflare must forward only to the loopback service. Do not expose port 8787 via a router or bind the service to `0.0.0.0`.

## 3. Create the Jira Automation rule

Create the rule in the intended Jira project:

1. **Trigger:** *Issue transitioned*.
2. **Condition:** destination status equals **В процессе проверки** (use the actual localized status name used by the project).
3. **Action:** *Send web request*:
   - URL: `https://jira-qa.example.com/webhooks/jira/qa-review`
   - Method: `POST`
   - Headers: `Content-Type: application/json` and `X-ClawIQ-Webhook-Secret: <the generated secret>`
   - Custom data:

     ```json
     {
       "issueKey": "{{issue.key}}",
       "event": "qa_review",
       "toStatus": "В процессе проверки"
     }
     ```

4. Restrict the rule actor to the minimum project permissions needed to trigger its web request. The Jira API token account needs only Browse Projects and Add Comments for the target project.
5. Keep the rule disabled until a test run is ready. Do **not** disable the existing hourly automation.

The static secret is necessarily configured in both the local protected environment and the Jira rule. Rotate it by replacing both values and restarting the local service. The service never accepts a secret from the JSON payload.

## 4. Safe verification and operations

Before enabling the rule broadly, use a dedicated test issue with non-production content:

1. Start the local service and Cloudflare Tunnel.
2. Transition only the test issue into the review status.
3. Confirm the Automation audit log reports HTTP `202`.
4. Check that exactly two comments were added and that they cite only issue/repository evidence or identify missing evidence.
5. Repeat the transition or replay the event. The marker-based duplicate check must avoid adding a second pair.
6. Only after that succeeds, enable the rule for normal use; leave the hourly automation in place until the team explicitly retires it.

Logs are written to the service console. Authentication failures are logged without the supplied secret. A Jira/Ollama failure creates no partial status update; it is visible in logs and can be retried by replaying the Jira event. If one comment was written before a later failure, the next retry detects it and creates only the missing comment.

Run the local automated checks:

```powershell
python -m unittest discover -s tests -v
```
