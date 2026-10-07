# Legacy Jira QA

Изолированный Python adapter, сохранён для совместимости. Не запускается ClawIQ desktop. Current deployment dormant; `.env.example` — placeholders. Документы: ../../docs/JIRA_QA_WEBHOOK.md. Перед production нужны durable queue и idempotency по evidence revision. Unit tests: python -m unittest discover -s tests -p test_jira_qa.py.
