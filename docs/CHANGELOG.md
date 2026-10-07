# Changelog

## 0.4.0 — 2026-10-07 — Desktop Foundation (local preview)

- ClawIQ возвращён к personal assistant: собственный Windows desktop, локальный чат, routing reason и model selection.
- Persistent conversations, recovery after restart, deletion, failed-request visibility.
- Text/code/analysis routes через Qwen3; optional local coder; image route через Qwen2.5-VL.
- Люська выделена в самостоятельный DevyJoness/lucy без изменения игровых правил/runtime. Legacy local deployment сохранён.
- Product boundaries, roadmap, architecture, setup, testing, ADR и backlog обновлены.
- Исправлен false-positive Test-Port; добавлен Windows CI и desktop smoke.

Known limits: эвристическая маршрутизация; нет cloud/web/tool actions, semantic memory, signed installer и auto-resume jobs. Desktop не использует cloud-first config существующего OpenClaw.

## История до reset

0.3.0, 15.09.2026: isolated local Jira QA adapter, dormant deployment.
0.2.x: infrastructure/prompts/doc revisions; Intelligence не считается полностью выполненным.
0.1.0/0.1.1: OpenClaw/Ollama/Telegram foundation и первые documents/scripts.

Подробный предшествующий CHANGELOG сохранён в archive/pre-desktop-reset/CHANGELOG.md. Номера версий прошлого roadmap не являются свидетельством реализации Memory или Desktop в соответствующем историческом релизе.
