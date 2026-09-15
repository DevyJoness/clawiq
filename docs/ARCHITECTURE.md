# ARCHITECTURE

_Last updated: 2026-09-15_

# Overview

ClawIQ is a modular, local-first AI platform.

The system is designed so that interfaces, AI providers and tools are replaceable while the assistant's identity, memory and behaviour remain consistent.

---

# Core Architecture

```text
                    User
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Telegram │ Desktop │ Mobile │ API │ Web
        │
        ▼
+-------------------------------+
|         ClawIQ Gateway        |
+-------------------------------+
               │
               ▼
+-------------------------------+
|        Intelligent Router     |
+-------------------------------+
        │        │         │
        ▼        ▼         ▼
   Memory     Skills   AI Providers
        │        │         │
        ▼        ▼         ▼
 Knowledge    Tools    Local / Cloud
```

---

# Components

## Gateway

Responsibilities

- Entry point
- Authentication
- Session management
- Request normalization
- Interface abstraction

---

## Router

Responsibilities

- Model selection
- Cost optimisation
- Local-first execution
- Provider fallback
- Context preparation

---

## Memory

Responsibilities

- Conversation history
- User preferences
- Long-term knowledge
- Semantic retrieval
- Shared context

Memory must be independent from any AI provider.

---

## Skills

Skills perform domain-specific work.

Examples:

- Coding
- Vision
- Research
- GitHub
- Jira
- Notion
- Calendar
- Local Files

Skills should remain modular.

### Jira QA webhook

The Jira QA webhook is a local automation adapter, not a Gateway replacement. Jira Automation reaches it through a narrowly scoped HTTPS tunnel; the adapter validates a shared secret, fetches current Jira evidence, invokes the local QA model, and writes only two idempotent QA comments. It remains isolated from Telegram, Gateway sessions, and scheduled automation. See [JIRA_QA_WEBHOOK.md](JIRA_QA_WEBHOOK.md).

---

## AI Providers

### Local

- Ollama
- Qwen3
- Qwen2.5-VL

### Cloud

- OpenAI
- Gemini
- Kimi

Providers must be interchangeable.

---

## Interfaces

Current

- Telegram

Planned

- Windows
- macOS
- Linux
- iPhone
- Android
- API
- Web

Interfaces must never contain business logic.

---

# Principles

1. Local-first.
2. Shared memory.
3. Provider independence.
4. Modular skills.
5. Stable personality.
6. Production-ready solutions.
7. Documentation accompanies architecture.

---

# Current Architecture Status

Implemented

- Gateway
- OpenClaw integration
- Ollama
- Telegram
- Basic routing

In Progress

- Router v2
- Memory foundation
- Prompt architecture
- Personality
- Vision

Planned

- Desktop runtime
- Mobile runtime
- Skills platform
- Semantic memory
- Multi-agent orchestration

---

# Documentation

Architecture decisions should remain synchronized with:

- ROADMAP.md
- PROJECT_CONTEXT.md
- Jira (KAN)
