# ADR-001 — Local First

## Status

Accepted

## Context

ClawIQ is designed as a personal AI platform.

Cloud providers may become unavailable, expensive or rate-limited.

A local model should always be preferred whenever it can complete the task with sufficient quality.

---

## Decision

Use Ollama as the primary inference provider.

Cloud providers are used only as fallbacks.

---

## Consequences

Advantages

- Offline capability
- Lower cost
- Better privacy
- Predictable behavior

Disadvantages

- Lower quality for some complex reasoning tasks
- Higher local hardware requirements
