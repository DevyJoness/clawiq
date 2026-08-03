# MAINTENANCE

_Last updated: 2026-08-03_

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
