# Границы ClawIQ и Люськи

Обновлено: 2026-10-07.

| | ClawIQ | Люська |
|---|---|---|
| Назначение | Личный AI-ассистент и платформа | Помощница игровой бригады |
| Основной интерфейс | Windows desktop | Telegram group bot |
| Репозиторий | DevyJoness/clawiq | DevyJoness/lucy |
| Данные | Личные session files | Публичный игровой roster/knowledge, offsets/schedules |
| Личность | Универсальный ClawIQ | Игровая Люська |
| Runtime | Electron + core + Ollama; OpenClaw adapter planned | Отдельный Node bot + optional local Ollama |
| Lifecycle | Собственные запуск и релизы | Собственные запуск и развитие |

Люська — первое детище ClawIQ, самостоятельный продукт, не встроенный skill текущего personal assistant. В будущем она может пользоваться общими библиотеками через версионированный contract, но это не требует объединять память и токены.

При отделении исходная игровая логика не изменена. Старые локальные директории automation/lucy_*, apps/lucy_desktop и launch scripts сохранены для совместимости текущего deployment и исключены из ClawIQ Git. Канонический код находится в независимом Lucy repo. Clean clone ClawIQ не содержит Lucy adapter.

OpenClaw Telegram polling нельзя одновременно запускать с Люськой на том же bot token. ClawIQ desktop не запускает Telegram и не изменяет bot credentials/configuration.
