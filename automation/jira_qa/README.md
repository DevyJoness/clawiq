# Jira local QA webhook

This package is the isolated Jira Automation entry point. It uses only Python's standard library, talks to Jira Cloud REST API v3, and sends the QA prompt to local Ollama. It has no dependency on Rovo and does not call or modify the OpenClaw Gateway.

Run it from the repository root:

```powershell
python -m automation.jira_qa.main
```

Configuration and the Cloudflare/Jira setup are documented in [docs/JIRA_QA_WEBHOOK.md](../../docs/JIRA_QA_WEBHOOK.md).
