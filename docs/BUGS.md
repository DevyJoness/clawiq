# Bugs и ограничения

Обновлено: 2026-10-07. Planned функции ведутся в Jira/BACKLOG, а не выдаются за подтверждённые bugs.

## Исправлено в 0.4.0

Legacy Test-Port выбрасывал Boolean Test-NetConnection и возвращал $?; closed port мог показывать OK. Теперь возвращается фактический результат probe.

## Открытые риски

- Desktop in-flight generation не переживает kill/restart; user request сохранён pending/failed, auto-resume отсутствует. Создать durable job lifecycle.
- История plaintext; encryption/retention/export не реализованы.
- Legacy Jira queue in-memory и без предела; duplicate marker не зависит от изменения acceptance criteria.
- npm audit: 8 moderate package findings в транзитивном build toolchain, 0 high/critical на 07.10.2026. Это не восемь независимых exploits. Нужен проверенный совместимый dependency upgrade.
- Unsigned portable Windows preview, без installer/auto-update.

Vision quality, router accuracy и performance требуют eval corpus; smoke не доказывает production readiness. Отсутствующие mobile/web/tool/cloud capabilities — известные ограничения версии, не скрытые поломки.

Bug report: version, route/model, steps, expected/actual, sanitized logs, severity, Jira key. Не прикладывайте tokens, private transcript и private images без явного решения владельца.
