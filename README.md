# ClawIQ

> **One AI. Many Brains.**

ClawIQ is a local-first personal AI platform built on OpenClaw. Its long-term goal is to become a cross-platform AI operating system that provides a consistent personality, shared memory, and intelligent routing across local and cloud models.

---

## Vision

ClawIQ is **not** a Telegram bot.

Telegram is currently the primary interface, but the product is designed to evolve into native applications for:

- Windows
- macOS
- Linux
- iPhone
- Android

The assistant should remain the same regardless of interface or model.

---

## Current Status

**Development Stage:** Sprint 3 – Intelligence

Current focus:

- Personality & Identity
- Prompt Architecture
- Model Router
- Memory Foundation
- Vision Pipeline
- Documentation Alignment
- Testing & QA

Jira is the source of truth for active work.
ROADMAP.md defines long-term direction.

---

## Core Principles

- Local-first
- Model-agnostic
- Production-ready
- Shared memory
- Modular architecture
- Replace models, not the assistant

---

## High-Level Architecture

```text
User
 │
 ▼
Interfaces
 │
 ▼
Gateway
 │
 ▼
Router
 ├── Local Models
 ├── Cloud Models
 ├── Skills
 ├── Memory
 └── Tools
```

---

## Current AI Stack

### Local

- Ollama
- Qwen3
- Qwen2.5-VL

### Cloud

- OpenAI
- Gemini
- Kimi

---

## Repository Structure

```text
docs/
prompts/
scripts/
workspace/
```

---

## Development Workflow

Idea

↓

ROADMAP

↓

Jira Epic

↓

Story

↓

Task

↓

GitHub

↓

Release

↓

Documentation

---

## Documentation

- PROJECT_CONTEXT.md
- ROADMAP.md
- ARCHITECTURE.md
- SETUP.md
- MAINTENANCE.md
- BUGS.md
- CHANGELOG.md

---

## License

Private project.
