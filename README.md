# ClawIQ

Личный local-first AI-ассистент Артёма. Один ассистент, сохраняемый контекст и выбор подходящего маршрута под запрос. Основной интерфейс — самостоятельное desktop-приложение; Telegram больше не является интерфейсом текущего ClawIQ.

## Текущий релиз

**v0.4.0 — Desktop Foundation**, Windows local preview. Реализованы чат с локальной Ollama, маршрутизация текста/кода/анализа/изображений, история отдельных разговоров и безопасный Electron renderer. Это начальная платформа, не законченная AI OS.

Текст: qwen3:14b. Изображения PNG/JPEG: qwen2.5vl:7b. При наличии qwen2.5-coder:14b код направляется туда, иначе в Qwen3. Облачные запросы, веб-поиск и действия через инструменты в этом релизе отключены. Отсутствие модели сообщает ошибку, а не запускает облачный fallback.

## Быстрый запуск

Windows, Node.js 24, Ollama. Python 3.11+ нужен для старого Jira QA adapter и его тестов, не для desktop-чата.

```powershell
ollama pull qwen3:14b
ollama pull qwen2.5vl:7b
npm.cmd ci
npm.cmd start
```

Собранный portable preview: dist/clawiq/win-unpacked/ClawIQ.exe. Переносите всю папку win-unpacked. Модели и Ollama устанавливаются отдельно.

## Люська

[Люська](https://github.com/DevyJoness/lucy) — самостоятельный первый продукт, выросший из ClawIQ. У неё собственный Telegram-бот, игровая база, расписания и репозиторий. ClawIQ не читает игровые данные, не запускает её bot process и не использует её личность. Подробности: [границы продуктов](docs/PRODUCTS.md).

## Архитектура и следующий шаг

Desktop → узкий IPC → core (routing + sessions) → local Ollama. OpenClaw остаётся выбранным runtime для будущих skills/actions. Его старый Gateway не запускается desktop-приложением; подключение выделенного personal agent с permissions — следующий milestone. Не подменяйте отсутствующий tool API прямым доступом renderer к файлам.

## Документация

- [Состояние проекта](docs/PROJECT_CONTEXT.md)
- [Roadmap](docs/ROADMAP.md)
- [Архитектура](docs/ARCHITECTURE.md)
- [Desktop](docs/DESKTOP.md)
- [Установка](docs/SETUP.md)
- [Тестирование](docs/TESTING.md)
- [Планирование](docs/BACKLOG.md)
- [Изменения](docs/CHANGELOG.md)
- [ADR](docs/ADR/README.md)

Jira KAN — источник актуальных задач, GitHub — кода и релизов. Старые документы сохранены в docs/archive/pre-desktop-reset только для истории. Проект private.
