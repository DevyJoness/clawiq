# Legacy Jira QA adapter

Обновлено: 2026-10-07. automation/jira_qa — отдельный adapter из 0.3.0, не часть desktop process. По умолчанию dormant; текущая `.env` может содержать placeholders. Не объявляем tunnel/hourly automations работающими без отдельной проверки.

Workflow: secret-validated POST /webhooks/jira/qa-review → issue evidence → local Ollama → два Jira comments. Не меняет statuses/assignees. Сервис слушает loopback 127.0.0.1:8787 при стандартной конфигурации. Auth secret comparison constant-time.

```powershell
python -m unittest discover -s tests -p test_jira_qa.py
.\scripts\Start-JiraQaWebhook.ps1
```

Запуск требует действующего ignored .env, Jira read/comment permissions и Ollama. Tunnel не нужен для локальных tests. Перед public webhook закрыть in-memory queue, ограничение нагрузки, issue revision idempotency, актуальный source context и secret-safe logging. До этого production exposure не рекомендуется.

Историческая инструкция tunnel сохранена в archive/pre-desktop-reset/JIRA_QA_WEBHOOK.md как справка, не текущий deployment state. Backlog management проекта через подключённый Jira connector не является этим workflow и не включает его автоматически.
