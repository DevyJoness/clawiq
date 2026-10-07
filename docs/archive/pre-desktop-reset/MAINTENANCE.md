# MAINTENANCE

_Last updated: 2026-09-15_

# Purpose

This document describes routine maintenance procedures for the ClawIQ development environment.

---

# Maintenance Schedule

## Daily

- Pull latest Git changes.
- Verify Gateway starts correctly.
- Check Ollama status.
- Review application logs.

---

## Weekly

- Update local models if required.
- Review Jira sprint progress.
- Remove obsolete branches.
- Verify documentation consistency.

## Jira QA adapter

The local Jira QA adapter was released in v0.3.0 but is not currently deployed through a public tunnel. Do not start or expose it as part of normal maintenance until secure outbound tunnel connectivity has been verified.

Current supported workflow: create QA Checklist and Regression/Smoke Test artifacts on demand from a Jira issue key or link. Existing hourly automation remains unchanged.

When deployment resumes:

1. Verify `cloudflared` can reach Cloudflare over TCP or UDP port 7844.
2. Use only a loopback-bound webhook with a protected secret.
3. Test with a dedicated non-production Jira issue before enabling the Jira Automation rule.
4. Keep the hourly automation enabled until the event-driven flow is proven stable.

---

## Monthly

- Update Python dependencies.
- Review OpenClaw updates.
- Archive completed sprint notes.
- Clean local cache and temporary files.

---

# Health Checklist

Gateway

- Starts without errors
- Accepts requests
- Routes correctly

Router

- Chooses local models first
- Falls back to cloud providers
- Produces expected routing decisions

Memory

- Stores conversations
- Restores context
- No corruption detected

Telegram

- Bot online
- Receives messages
- Sends responses

---

# Logs

Monitor for:

- Startup failures
- Provider errors
- Timeout exceptions
- Memory errors
- Router failures
- Jira QA webhook authentication, Jira REST, or Ollama errors when the adapter is explicitly deployed

---

# Backup

Recommended backups:

- Repository
- Configuration
- Environment variables
- Prompt library
- Documentation

---

# Updating

Before updating:

1. Commit current changes.
2. Pull latest repository.
3. Update dependencies.
4. Verify startup.
5. Execute smoke tests.

---

# Incident Response

If ClawIQ becomes unstable:

1. Check logs.
2. Verify Gateway.
3. Verify Ollama.
4. Verify local models.
5. Verify API keys.
6. Restart services.
7. Record issue in BUGS.md if reproducible.

---

# Related Documents

- SETUP.md
- BUGS.md
- CHANGELOG.md
- PROJECT_CONTEXT.md
