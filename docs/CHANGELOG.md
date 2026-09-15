# CHANGELOG

All notable changes to ClawIQ are documented in this file.

The format follows the Keep a Changelog convention.

---

# [0.3.0] - 2026-09-15

## Added

- Local, loopback-only Jira QA webhook with constant-time secret validation.
- Jira Cloud REST integration for current issue details, acceptance criteria, linked issues, and duplicate-comment detection.
- Local Ollama QA workflow that creates separate evidence-based QA Checklist and Regression/Smoke Test comments.
- Idempotent queued processing, structured error logging, and automated webhook/workflow tests.
- Cloudflare Tunnel and Jira Automation setup documentation without Rovo.

## Security

- Jira and webhook secrets are loaded from an ignored local environment file and are never committed.
- The service does not modify issue status or other Jira fields.

## Compatibility

- Existing Gateway, Telegram, and hourly automation are unchanged.

---

# [Unreleased]

## Planned

### Intelligence

- Personality system improvements
- Identity refinement
- Prompt Architecture v2
- Intelligent Router
- Memory Foundation
- Vision workflow improvements

### Platform

- Desktop application foundation
- Skills architecture
- Semantic memory
- Productivity integrations

### Infrastructure

- Improved logging
- Better error handling
- Startup validation
- Health monitoring

---

# [0.2.0] - In Development

## Added

- Sprint 3 project structure
- Updated architecture documentation
- Unified project documentation
- Jira-aligned roadmap
- Current project context

## Changed

- Documentation reorganized
- Architecture updated to Gateway → Router → Memory → Skills
- Telegram positioned as one interface rather than the product

---

# [0.1.1]

## Added

- Initial documentation
- Maintenance guide
- Setup guide
- Bug tracking

## Improved

- Gateway stability
- OpenClaw integration
- Local development workflow

---

# [0.1.0]

## Initial Release

### Implemented

- OpenClaw integration
- Ollama support
- Telegram interface
- Local-first development
- Initial prompt library
- Repository structure

---

# Versioning

Current Development:
0.2.0

Current Sprint:
Sprint 3 — Intelligence

---

# Related Documents

- PROJECT_CONTEXT.md
- ROADMAP.md
- ARCHITECTURE.md
- BUGS.md
