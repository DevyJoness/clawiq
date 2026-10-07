# ClawIQ — актуальный контекст

Обновлено: 2026-10-07. Владелец: Артём. Репозиторий: DevyJoness/clawiq. Планирование: Jira KAN. Версия desktop/core: 0.4.0, local preview.

## Решение о направлении

ClawIQ — личная AI-платформа с desktop как первым интерфейсом. Люська стала самостоятельным продуктом в DevyJoness/lucy. Её Telegram-бот сохраняет своё поведение; он не является интерфейсом personal assistant.

## Реализовано

- Изолированный Electron UI для личного чата и отдельных разговоров.
- Local-first маршруты conversation, coding, analysis, research (без live search), vision.
- Ollama Qwen3 и Qwen2.5-VL; выбор coder при установленной локальной модели.
- Persistent session history, восстановление после перезапуска, удаление разговора.
- Выбор PNG/JPEG через native dialog; изображения не сохраняются в session files.
- Readiness моделей, честные ошибки timeout/unavailable; исправлена TCP-проверка legacy launch scripts.
- Node/Python tests, Windows CI workflow, desktop smoke и portable build.

## Ограничения

История не равна semantic memory. Передаётся до 20 предыдущих завершённых сообщений; разговор ограничен 200 сообщениями. История хранится plaintext в локальном userData, не шифруется приложением. Изображения не доступны повторно после перезапуска.

Нет облачных provider calls, веб-поиска, произвольного file access, tool execution, мобильных приложений, installer signing и гарантированного recovery in-flight jobs. Старый Jira QA — изолированный dormant adapter с отдельным lifecycle; его deployment не считается завершённым.

## Приоритеты

1. Общий contract OpenClaw personal agent + permissions/approval, без public/shared Lucy memory.
2. Надёжность запросов и качественная проверка routing.
3. Memory lifecycle: retention, export, recovery, backup и privacy.
4. Desktop streaming/cancel, settings и signed distribution.
5. Skills и последующие macOS/Linux/mobile interfaces.

Старые обозначения Sprint 3 и KAN-7…KAN-14 относятся к предшествующему плану. Новые задачи и ссылки — в BACKLOG.md. Этот документ не объявляет planned функции работающими.
