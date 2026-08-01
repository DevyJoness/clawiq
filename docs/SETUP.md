# ClawIQ Setup Guide

This document describes the complete installation and configuration process for ClawIQ.

---

# Requirements

- Windows 11
- Node.js (latest LTS recommended)
- Git
- Ollama
- Telegram Bot Token
- GitHub account

---

# Repository

Clone the repository.

```bash
git clone https://github.com/DevyJoness/clawiq.git
```

---

# Install OpenClaw

Install globally using npm.

```powershell
npm install -g openclaw
```

Verify installation.

```powershell
openclaw --version
```

---

# Install Ollama

Download and install Ollama.

Verify:

```powershell
ollama --version
```

---

# Download Models

Main model:

```powershell
ollama pull qwen3:14b
```

Vision model:

```powershell
ollama pull qwen2.5vl:7b
```

Verify:

```powershell
ollama list
```

---

# Configure OpenClaw

Run:

```powershell
openclaw configure
```

Configure:

- Workspace
- Gateway
- Telegram
- Ollama

---

# Configure Telegram

Create a bot using BotFather.

Add the token inside OpenClaw configuration.

---

# Configure Gateway

Gateway should be configured as:

- Mode: Local
- Bind: Loopback
- Port: 18789

Verify:

```powershell
openclaw gateway status
```

Dashboard:

```
http://127.0.0.1:18789
```

---

# Configure Models

Run:

```powershell
openclaw configure --section model
```

Select:

Primary model

```
ollama/qwen3:14b
```

Vision model

```
ollama/qwen2.5vl:7b
```

Verify:

```powershell
openclaw agents list
```

Expected:

```
Model:
ollama/qwen3:14b
```

---

# Gateway Autostart

OpenClaw creates:

```
~/.openclaw/gateway.cmd

~/.openclaw/gateway.vbs
```

If automatic startup fails after installation or update:

Run

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair-gateway.ps1
```

This repairs:

- gateway.cmd
- gateway.vbs

---

# Known Windows Issue

OpenClaw currently generates launcher files using absolute paths.

Windows usernames containing non-ASCII characters (for example Cyrillic usernames) may break:

- gateway.cmd
- gateway.vbs

ClawIQ includes a repair script:

```
scripts/repair-gateway.ps1
```

---

# Verify Gateway

Run:

```powershell
openclaw gateway status
```

Expected:

```
Runtime: running

Connectivity probe: ok
```

---

# Verify Telegram

Send a message to the bot.

Expected:

- reply received
- no Model Fallback
- provider = Ollama

---

# Identity

Workspace contains:

```
IDENTITY.md
```

OpenClaw reads identity from plain fields.

Correct:

```
- Name: ClawIQ
- Theme: Personal AI Operating System
- Emoji: 🧠
```

Incorrect:

```
- **Name:** ClawIQ
```

Update identity:

```powershell
openclaw agents set-identity --agent main --workspace "$env:USERPROFILE\.openclaw\workspace" --from-identity
```

---

# GitHub Documentation

Project documentation is stored in:

```
docs/

README.md
ARCHITECTURE.md
ROADMAP.md
SETUP.md
BUGS.md
MAINTENANCE.md
```

Prompt library:

```
docs/prompts/

system-v1.md
coding-v1.md
vision-v1.md
router-v1.md
```

---

# Maintenance

Repair gateway:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair-gateway.ps1
```

Stop Ollama:

```powershell
taskkill /IM ollama.exe /F
```

Start Ollama:

```powershell
ollama serve
```

Loaded models:

```powershell
ollama ps
```

Installed models:

```powershell
ollama list
```

---

# Current Architecture

```
Telegram

↓

OpenClaw Gateway

↓

Agent (main / ClawIQ)

↓

Ollama

↓

Qwen3:14b

↓

Future Router

↓

Future Skills

↓

Future Memory
```

---

# Current Status

Completed

- GitHub repository
- Documentation
- Gateway
- Telegram
- Ollama
- Qwen3
- Vision model
- Prompt library
- Gateway repair script

In Progress

- Vision integration
- Gemini integration
- Agent identity
- Router
- Memory

Planned

- Web UI
- Mobile application
- Multi-agent system
- ClawIQ Router
- Cloud deployment


## Default Routing
Primary: ollama/qwen3:14b
Fallbacks:
1. google/gemini-3.1-pro-preview
2. openai/gpt-5.5
3. ollama/qwen2.5vl:7b
Vision: ollama/qwen2.5vl:7b
