# ROADMAP

_Last updated: 2026-09-15_

# Vision

ClawIQ is a local-first personal AI platform designed to evolve into a standalone cross-platform AI operating system.

The assistant should preserve a single personality, shared memory and consistent behavior regardless of interface or AI provider.

---

# Guiding Principles

- Local-first by default
- Model-agnostic architecture
- Shared memory
- Modular skills
- Production-ready engineering
- Documentation-first development

---

# Phase 1 — Foundation ✅

Status: Completed

## Goals

- OpenClaw integration
- Ollama integration
- Telegram interface
- Basic gateway
- Project documentation
- Local development environment

---

# Phase 2 — Intelligence 🚧

Status: In Progress

Primary Jira Epic: **KAN-7**

## Deliverables

- Personality system
- Identity rules
- Prompt Architecture v2
- Intelligent Router
- Memory foundation
- Vision workflow
- Documentation alignment
- Testing & QA

Success criteria:

- Stable assistant behaviour
- Predictable routing
- Shared conversational context
- Reliable prompt architecture

---

# Phase 3 — Platform

## Objectives

- Native Desktop Application
- Plugin/Skills framework
- Local semantic search
- Knowledge management
- Background services

Related Epics

- KAN-9 Desktop
- KAN-10 Memory
- KAN-12 Productivity

---

# Phase 4 — Productivity

## Integrations

- GitHub
- Jira — local QA adapter released in v0.3.0; event-driven deployment pending secure tunnel connectivity
- Notion
- Calendar
- Gmail
- Local Files

Goals

- Daily workflow automation
- Project awareness
- Long-term memory

### Shipped increment: Jira QA automation

v0.3.0 provides a local-first Jira QA adapter that reads current issue evidence and produces separate QA Checklist and Regression/Smoke Test comments via local Ollama. It is intentionally dormant until a reliable tunnel is available. In the interim, the supported workflow is on-demand QA by Jira issue key or link.

---

# Phase 5 — AI OS

## Long-Term Vision

ClawIQ becomes a complete AI operating system featuring:

- Native Windows application
- Native macOS application
- Native Linux application
- Native iPhone application
- Native Android application
- Unified memory
- Multi-provider orchestration
- Skills ecosystem
- Multi-agent workflows

---

# Success Metrics

Technical

- Stable local-first routing
- Shared memory
- Cross-platform architecture
- Production deployment

Product

- One assistant across all devices
- Consistent personality
- Replaceable models
- Extensible skills

---

# Source of Truth

Current implementation:
- PROJECT_CONTEXT.md

Architecture:
- ARCHITECTURE.md

Execution:
- Jira (KAN)

History:
- CHANGELOG.md
