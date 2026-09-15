# SETUP

_Last updated: 2026-08-03_

# Purpose

This document describes the recommended development environment for ClawIQ.

The goal is to provide a reproducible local-first setup for contributors.

---

# Requirements

## Operating System

Recommended:

- Windows 11

Supported:

- Windows 10
- Linux (planned)
- macOS (planned)

---

# Required Software

- Git
- Python 3.11+
- Ollama
- OpenClaw
- VS Code
- PowerShell 7 (recommended)

---

# Local Models

Required:

- Qwen3
- Qwen2.5-VL

Optional:

- Additional Ollama-compatible models

---

# Environment

Configure:

- OpenAI API Key
- Gemini API Key (optional)
- Kimi API Key (optional)

Local models should be preferred whenever possible.

---

# Installation

1. Clone repository.
2. Install Python dependencies.
3. Install Ollama.
4. Download required models.
5. Configure environment variables.
6. Start OpenClaw.
7. Start ClawIQ Gateway.
8. Verify Telegram interface.

---

# Verification Checklist

- Gateway starts successfully.
- Ollama responds.
- Local model is available.
- Telegram bot connects.
- Router selects providers correctly.
- Logs contain no startup errors.

## Jira QA automation (optional)

The local Jira QA webhook is an isolated automation service. It receives a signed Jira Automation event through a Cloudflare Tunnel, reads the current issue through Jira REST API, and posts an evidence-based QA Checklist and Regression/Smoke Test through the local Ollama model. It does not use Rovo or alter Jira issue fields/statuses.

Follow [JIRA_QA_WEBHOOK.md](JIRA_QA_WEBHOOK.md) for protected environment variables, tunnel configuration, Jira Automation setup, and safe test verification. Keep any existing hourly QA automation enabled until the event-driven flow has been verified.

---

# Troubleshooting

Common issues:

- Missing API keys.
- Ollama not running.
- Missing local model.
- Incorrect environment variables.
- Port already in use.

Refer to:

- BUGS.md
- MAINTENANCE.md

---

# Development Workflow

1. Pull latest changes.
2. Create feature branch.
3. Implement changes.
4. Test locally.
5. Update documentation if architecture changed.
6. Commit.
7. Push.
8. Create Pull Request.

---

# Source of Truth

Architecture:
- ARCHITECTURE.md

Current sprint:
- PROJECT_CONTEXT.md

Long-term direction:
- ROADMAP.md
