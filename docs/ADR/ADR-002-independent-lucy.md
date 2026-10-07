# ADR-002 — Independent Lucy

Status: Accepted, 2026-10-07.

Decision: Люська — отдельный продукт, repository и runtime. Telegram group bot не является интерфейсом personal ClawIQ. Игровые data/persona и personal memory не смешиваются.

Consequence: сохранить игровые handlers, конфигурацию и polling lifecycle; shared Ollama возможна, shared private transcript — нет. Legacy local paths остаются для совместимости, канонический код находится в DevyJoness/lucy.
