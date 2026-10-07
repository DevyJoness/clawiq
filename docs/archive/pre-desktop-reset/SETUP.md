# SETUP

_Last updated: 2026-09-15_

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

## Lucy Telegram group mode (MVP)

Static commands require a running bot process even when Ollama is disabled.
For availability while the PC is off, use an always-on host. Deployment and
Moscow-time schedules are described in [LUCY_HOSTING.md](LUCY_HOSTING.md).

Private messages require `owner_telegram_id` in ignored local JSON. Without it,
all private messages are silently ignored. This is an access check, not a model
instruction. Only !лагеря, !бр, !гайды, !состав, !id and !люська are dispatched; chat
messages cannot add commands or change configuration. Owner identity and Telegram
tags are never supplied to Ollama. Public game nicknames and string-valued game
IDs are loaded from `automation/lucy_group_bot/roster.json` via `roster_file`.
This single file feeds the compact !состав reply (no LLM required) and model context.
`!id nickname` looks up the game ID in that same file without inference. Matching
ignores case and the RV prefix; exact matches take priority over partial matches.
Ambiguous partial matches ask for a full nickname rather than guessing an ID.
Bare `!люська` shows a short command guide without invoking Ollama.
Update it and restart Lucy after a roster change. Membership announcements remind
the brigade to update the list; Telegram membership is not a game-roster mapping.
Topic/privacy filters supplement the system prompt;
they are not a mathematical guarantee against arbitrary model hallucinations.
The supplied game knowledge is a user-provided snapshot, not live game data.
Ollama requests explicitly use a 16384-token context, temperature 0 and thinking
disabled. The previous default context truncated the full Russian knowledge base.
Keep the prompt plus output within that budget when extending the knowledge file.
Replies use short plain-text paragraphs; Markdown markers are normalized before
HTML escaping. These measures reduce, but cannot eliminate, model factual errors.
The raid announcement is fixed text and needs a manual update after 11.10.
Standard command scopes are cleared on startup (default, ru, en); chat-specific
group scopes are cleared on the first message. Other language/member-specific
scopes cannot be enumerated by Telegram and may require targeted cleanup.
Do not run OpenClaw's Telegram integration on this token: it can re-register
menus and has different access rules.

Lucy is a local deterministic Telegram group adapter for the Turyaga community.
Static commands do not invoke an LLM; only explicit Lucy questions do. It does not share group
messages with ClawIQ's personal assistant sessions. This keeps the first group
feature inexpensive, predictable, and isolated from the local-first core.

### What it handles

- `!лагеря` responds with the administrator-configured camp-attack schedule.
- `!люська <вопрос>` sends a group question to the local Ollama model.
- Member joins receive the configured welcome message.
- Member departures receive the configured farewell message.
- Commands and messages are scoped to explicitly configured Telegram chat IDs.

### Configure it locally

1. Copy `automation/lucy_group_bot/lucy-group-bot.example.json` to
   `automation/lucy_group_bot/lucy-group-bot.json`.
2. Stop the existing Gateway and run
   `./scripts/Start-LucyGroupBot.ps1 -UseExistingOpenClawToken -DiscoverChatId`.
   Send any message in the target group; the command prints its numeric group
   ID without logging message text or the token. Use that ID in place of
   `REPLACE_WITH_GROUP_CHAT_ID`.
3. Replace the camp response with its actual schedule in Moscow time. The local
   configuration is ignored by Git.
4. In BotFather, rename the bot with `/setname` to `Люська`. Telegram bot names
   cannot be changed by the Bot API or this repository.
5. Disable the bot's privacy mode with BotFather `/setprivacy`, then make it a
   group administrator. Privacy mode would hide `!лагеря`; administrator access
   plus the `chat_member` update is required for reliable join/leave events.

### Start and test

Use a dedicated Telegram bot token for Lucy if the personal OpenClaw Gateway is
running. Set it only in the local shell, never in a project file or chat:

```powershell
$env:CLAWIQ_LUCY_TELEGRAM_BOT_TOKEN = "<local BotFather token>"
./scripts/Start-LucyGroupBot.ps1
```

The existing OpenClaw token can be used temporarily without copying it out of
`~/.openclaw/openclaw.json`:

```powershell
./scripts/Stop-ClawIQ.ps1
./scripts/Start-LucyGroupBot.ps1 -UseExistingOpenClawToken
```

Do not run both consumers with the same bot token: Telegram permits a single
long-polling consumer. Invite the bot to the configured group, send
`!лагеря`, then add and remove a test account to verify the welcome and
farewell replies. On a first launch with old events waiting, append
`-SkipPending` to avoid replying to historical membership updates.

The included local starter configuration sets `!лагеря` to `Лагеря каждый день в 00:05 МСК`
and maps `!люська <вопрос>` to local `qwen3:14b` through Ollama. It
uses a temporary `"*"` group rule to make an immediate first test possible;
replace it with the discovered numeric group ID after the test.

Ollama is optional: static commands and membership replies work with Ollama
stopped, omitted, or configured with `enabled: false`. The launcher no longer
starts or requires Ollama. Start Ollama separately for AI answers.
At most two AI answers run concurrently; slow inference does not block static
commands. In-flight AI requests are not persisted: after a process crash the
participant may need to repeat the question.
The system prompt describes Lucy as the helper of a brigade of about 70 Turyaga
players, includes the confirmed camp schedule, and forbids inventing game or
member facts. It receives the current question only, without shared chat history.

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
