# PROJECT_CONTEXT

_Last updated: 2026-09-15_

# Project

**ClawIQ** is a local-first personal AI platform built on OpenClaw.

## Latest Release

**v0.3.0 — Local Jira QA Automation**

Released: 2026-09-15

- Adds an isolated, local Jira QA adapter using Jira REST API and local Ollama.
- Produces an evidence-based QA Checklist and Regression/Smoke Test as separate Jira comments.
- Does not use Rovo and does not alter issue statuses or other fields.
- Requires a secure outbound tunnel before event-driven Jira Automation is enabled.

### Current operating mode

The event-driven webhook is released but intentionally not enabled because the current network blocks Cloudflare Tunnel connectivity. Until that is resolved, Jira QA is performed manually on request using an issue key or Jira link. Existing hourly automation remains unchanged.

## Current Sprint
**Sprint 3 — Intelligence**

Jira Epic: **KAN-7**

### Objectives
- Personality
- Identity
- Prompt Architecture
- Memory Foundation
- Router
- Vision
- Documentation
- Testing & QA

## Active Epics

| Epic | Description |
|------|-------------|
| KAN-7 | Sprint 3 – Intelligence |
| KAN-8 | Infrastructure |
| KAN-9 | Desktop Application |
| KAN-10 | Memory |
| KAN-11 | Vision |
| KAN-12 | Productivity Integrations |
| KAN-13 | Testing & QA |
| KAN-14 | Technical Debt |

## Architecture Status

### Stable
- Gateway
- OpenClaw
- Ollama
- Telegram interface
- Local Jira QA adapter (released; deployment pending)

### In Progress
- Router
- Memory
- Personality
- Vision
- Desktop foundation

### Planned
- Native Desktop
- Native Mobile
- Skills Platform
- Semantic Memory
- Multi-Agent

## Source of Truth

- Jira — active work
- ROADMAP.md — long-term strategy
- ARCHITECTURE.md — architecture
- CHANGELOG.md — history
- BUGS.md — known issues

## Rules

1. Roadmap defines direction.
2. Jira defines execution.
3. GitHub stores code.
4. Documentation is updated with architecture.
5. Prefer local-first.
6. Prefer production-ready solutions.

## Current Priorities

P0:
- Router
- Memory
- Personality
- Prompt Architecture
- Documentation

P1:
- Desktop
- Vision
- Infrastructure

P2:
- Productivity
- Semantic Search
- Cost Optimization

## Goal

Build a production-ready cross-platform personal AI platform.
