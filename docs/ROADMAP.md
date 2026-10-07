# Roadmap ClawIQ

Обновлено: 2026-10-07. Миссия: личный local-first AI-ассистент, который сохраняет контекст, выбирает модели и инструменты под запрос, работает через собственные приложения.

## M0 — Desktop Foundation (0.4.0 local preview)

- Люська отделена в самостоятельный продукт/repo.
- Windows personal chat, локальная text/vision маршрутизация, persistent conversation history.
- Актуальные architecture/product docs и reset backlog.
- Проверяемые tests/CI и release с честными ограничениями.

DoD: local chat получает реальный Ollama ответ, история восстанавливается, Windows package стартует без Node, public Lucy данные не входят в personal package.

## M1 — Reliable Intelligence

Routing quality corpus, model availability/capability checks, durable accepted requests, retries/cancel, явная local/cloud policy. Dedicated OpenClaw personal-agent adapter с permissions и observable execution. DoD: restart не теряет принятые jobs, private data не уходит в cloud без policy, failed tool не выдаётся за успех.

## M2 — Memory Foundation

Retention, export/delete, backup/recovery, per-scope ownership, preferences и project context. Semantic retrieval вводится после оценки доступного OpenClaw storage и конкретных retrieval scenarios. DoD: изоляция personal/project/third-party контекстов и проверяемый lifecycle данных.

## M3 — Desktop Product

Streaming, cancel, provider settings, file/image UX, packaging/signing/update flow, accessibility и macOS/Linux smoke. DoD: reproducible signed distribution и usable offline history; отсутствие модели объяснено.

## M4 — Skills & Productivity

Web research, local files, GitHub/Jira/calendar как scoped adapters с approval, evidence/provenance и безопасным failure handling. Legacy Jira QA пересмотреть; его public deployment не является P0 desktop.

## M5 — Cross-platform Personal Assistant

Mobile contract, iPhone/Android clients, optional secure sync, voice. Desktop/core не должны зависеть от Telegram. Multi-agent вводится после стабильных sessions, tools и permissions.

Релизные номера прошлого плана не означают завершение старых phases: историческая 0.3.0 была Jira QA, а не Memory. Следующий номер определяется реальным shipped increment. Текущая версия — local preview, production-ready остаётся целью.
