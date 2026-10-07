# Maintenance

Обновлено: 2026-10-07.

Перед feature работой: git status, Jira backlog, доступность модели. Не обновляйте providers/models автоматически вместе с запуском приложения.

Периодически: npm audit полного toolchain, node tests, Python legacy tests, desktop smoke и packaged smoke. Не используйте audit --omit=dev как единственное доказательство безопасности Electron сборки: её toolchain объявлен dev dependency.

History backup: закройте ClawIQ, скопируйте userData/sessions в защищённое место. Там личные сообщения в plaintext. Не загружайте их в GitHub/Jira. Restore выполняется только при закрытом приложении. Автоматический export/retention/recovery planned.

Legacy Gateway/Ollama health: исправленный Test-Port возвращает TCP Boolean. Это не проверка качества модели. Для desktop смотрите UI readiness и реальный local smoke. Stop-ClawIQ.ps1 останавливает всю найденную Ollama и может повлиять на Люську; не используйте его без понимания общей зависимости.

Люська: отдельный repo/runtime. Не меняйте её token, offset state и schedules через обслуживание personal assistant. Старые local paths сохранены при extraction; перенос процесса на новую папку — отдельное действие, нельзя запускать дубликат polling.

Jira QA остаётся dormant. Перед tunnel нужно закрыть durable queue, idempotency per evidence revision и test-issue rollout. Утверждение старых документов об hourly automation не считается текущим подтверждённым состоянием.
