# CHANGELOG

## Unreleased — 2026-10-07

- Lucy Windows desktop MVP: welcome illustration, five separate native windows,
  shared local roster/guides UI, isolated Electron renderer and loopback service.
- Added Windows build/launcher and real Electron window smoke test; removed the
  Telegram WebApp runtime dependency from the shared Lucy UI. Bot remains unchanged.

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

### Lucy brigade policy

- Added local Mini App MVP «Штаб РВ» with dashboard, roster search, guides and command help.
- Redesigned the mini app for desktop/mobile; fixed navigation during API failures, added game ID/command copying and expandable knowledge sections.
- Mini app uses bot announcement data and serves only explicitly public routes.

- Model-independent one-off and daily Moscow-time messages with persistent delivery state and bounded retry.
- Portable Node container and explicit uptime/deployment instructions for the brigade adapter.

- Unavailable or failed local inference returns a friendly vacation notice with the available deterministic commands.

- Owner-only private messages (numeric sender and chat ID checks; fail closed).
- Approved commands only: !лагеря, !бр, !гайды, !состав, !id, !люська.
- Bare !люська displays a compact command guide; !id nickname resolves game IDs from the shared roster without LLM calls, with ambiguity handling.
- RV brigade context and supplied Turyaga knowledge base; public game nicknames/IDs are permitted, Telegram tags and owner data excluded.
- Compact deterministic !состав command sourced from a shared 67-member roster; game IDs retained as strings.
- Join/leave messages remind responsible members to update the roster and command.
- Cleared standard Telegram command menus for default/Russian/English scopes; group scopes cleared on activity.
- Local-only personality, privacy/topic guards, welcome/farewell messages.

## Fixed

- Explicit 16384-token Ollama context prevents observed truncation of the supplied knowledge base; disabled thinking and reduced sampling variability.
- Plain-text normalization of AI replies; removed blanket blocking of long game IDs and damage values.
- Lucy launcher variable collision with the shared PowerShell script.
- Static group commands remain available without Ollama and during inference.
- Camp response updated to «Лагеря каждый день в 00:05 МСК».
- Added brigade context for roughly 70 Turyaga players and bounded AI concurrency.

## Added

- Local, deterministic Telegram group adapter for the Lucy (`Люська`) MVP.
- Per-group extensible `!` command registry with a configurable `!лагеря`
  response.
- Configurable welcome and farewell handling for Telegram membership events,
  durable update offsets, and duplicate-event suppression.
- Safe launcher and setup instructions for either a dedicated Lucy bot token
  or a controlled temporary hand-off from the existing OpenClaw Telegram bot.

## Compatibility

- The personal OpenClaw Gateway, its local-first routing, and existing Telegram
  configuration are unchanged. Lucy must use a separate bot token while the
  Gateway polls Telegram, or the Gateway must be stopped for a temporary
  hand-off.

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

Latest Release:
0.3.0

Current Development:
0.3.x

Current Sprint:
Sprint 3 — Intelligence

---

# Related Documents

- PROJECT_CONTEXT.md
- ROADMAP.md
- ARCHITECTURE.md
- BUGS.md
