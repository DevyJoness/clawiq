# ClawIQ Setup Guide

This guide describes how to set up ClawIQ from scratch.

---

# Requirements

## Software

- Windows 11 (recommended)
- Node.js
- Git
- Ollama
- OpenClaw
- Telegram
- GitHub account

Optional:

- Gemini CLI
- Notion
- Docker

---

# Installation

## 1. Install Node.js

Download:

https://nodejs.org/

Verify:

```bash
node -v
npm -v
```

---

## 2. Install Git

Download:

https://git-scm.com/

Verify:

```bash
git --version
```

---

## 3. Install Ollama

Download:

https://ollama.com/

Verify:

```bash
ollama --version
```

---

## 4. Download Models

Current models:

```bash
ollama pull qwen3:14b
```

```bash
ollama pull qwen2.5vl:7b
```

---

## 5. Install OpenClaw

```bash
npm install -g openclaw
```

Verify:

```bash
openclaw --version
```

---

## 6. Configure OpenClaw

Run:

```bash
openclaw configure
```

Configure:

- Gateway
- OpenAI
- Telegram
- Ollama

---

## 7. Configure Gateway

Install service:

```bash
openclaw gateway install
```

Check:

```bash
openclaw gateway status --deep
```

---

## 8. Configure Telegram

Create Telegram Bot

Save token

Connect channel

Verify communication

---

## 9. Verify Installation

Gateway

```bash
openclaw gateway status
```

Models

```bash
openclaw models status
```

Ollama

```bash
ollama ps
```

---

# Current Models

Primary

- GPT-5.5

Fallback

- Qwen3 14B

Vision

- Qwen2.5VL

---

# Known Issues

## BUG-003

Windows Companion authentication.

---

## BUG-004

Vision crashes on AMD GPU.

---

## BUG-005

Gemini OAuth migration.

---

# Future Setup

Planned

- Docker
- VPS
- Raspberry Pi
- Home Server
