# ClawIQ backlog — reset 2026-10-07

Jira KAN — источник текущего состояния. Ниже snapshot планирования, не замена Jira. Люська живёт отдельно в DevyJoness/lucy.

## Epics

- [KAN-15 — ClawIQ — Reliable Intelligence](https://clawiq.atlassian.net/browse/KAN-15)
- [KAN-16 — ClawIQ — Memory & Privacy](https://clawiq.atlassian.net/browse/KAN-16)
- [KAN-17 — ClawIQ — Desktop Product](https://clawiq.atlassian.net/browse/KAN-17)
- [KAN-18 — ClawIQ — OpenClaw & Skills](https://clawiq.atlassian.net/browse/KAN-18)
- [KAN-19 — ClawIQ — Quality & Releases](https://clawiq.atlassian.net/browse/KAN-19)
- [KAN-20 — ClawIQ — Cross-platform](https://clawiq.atlassian.net/browse/KAN-20)

## Tasks

| Jira | Результат | Milestone | Статус на reset |
|---|---|---|---|
| [KAN-21](https://clawiq.atlassian.net/browse/KAN-21) | Локальный router foundation: текст, код, анализ и vision | m0 | Done — verified 0.4.0 |
| [KAN-22](https://clawiq.atlassian.net/browse/KAN-22) | Проверить точность классификации и выбора моделей на корпусе запросов | m1 | To Do |
| [KAN-23](https://clawiq.atlassian.net/browse/KAN-23) | Durable lifecycle запросов: restart, retry, cancel | m1 | To Do |
| [KAN-24](https://clawiq.atlassian.net/browse/KAN-24) | Явная privacy/budget policy для будущего cloud fallback | m1 | To Do |
| [KAN-25](https://clawiq.atlassian.net/browse/KAN-25) | История отдельных разговоров с восстановлением после restart | m0 | Done — verified 0.4.0 |
| [KAN-26](https://clawiq.atlassian.net/browse/KAN-26) | Export, retention, backup и privacy локальной памяти | m2 | To Do |
| [KAN-27](https://clawiq.atlassian.net/browse/KAN-27) | Preferences и project memory с access scopes | m2 | To Do |
| [KAN-28](https://clawiq.atlassian.net/browse/KAN-28) | Оценить OpenClaw storage и semantic retrieval на реальных сценариях | m2 | To Do |
| [KAN-29](https://clawiq.atlassian.net/browse/KAN-29) | Windows personal assistant local preview | m0 | Done — verified 0.4.0 |
| [KAN-30](https://clawiq.atlassian.net/browse/KAN-30) | Streaming, cancel и восстановление состояния интерфейса | m3 | To Do |
| [KAN-31](https://clawiq.atlassian.net/browse/KAN-31) | Настройки моделей и прозрачные capabilities | m3 | To Do |
| [KAN-32](https://clawiq.atlassian.net/browse/KAN-32) | Signed Windows installer и безопасный update flow | m3 | To Do |
| [KAN-33](https://clawiq.atlassian.net/browse/KAN-33) | Подключить dedicated OpenClaw personal-agent contract | m1 | To Do |
| [KAN-34](https://clawiq.atlassian.net/browse/KAN-34) | Read-only web research с источниками и provenance | m4 | To Do |
| [KAN-35](https://clawiq.atlassian.net/browse/KAN-35) | Local files и действия с reviewable approval | m4 | To Do |
| [KAN-36](https://clawiq.atlassian.net/browse/KAN-36) | Пересмотреть legacy Jira QA перед event-driven deployment | m4 | To Do |
| [KAN-37](https://clawiq.atlassian.net/browse/KAN-37) | Отделить Люську и обновить продуктовую документацию | m0 | Done — verified 0.4.0 |
| [KAN-38](https://clawiq.atlassian.net/browse/KAN-38) | Стабилизировать CI и clean-clone release gate | m1 | To Do |
| [KAN-39](https://clawiq.atlassian.net/browse/KAN-39) | Устранить moderate findings build toolchain | m1 | To Do |
| [KAN-40](https://clawiq.atlassian.net/browse/KAN-40) | LLM quality и vision eval с privacy-safe corpus | m1 | To Do |
| [KAN-41](https://clawiq.atlassian.net/browse/KAN-41) | macOS/Linux runtime и distribution spike | m3 | To Do |
| [KAN-42](https://clawiq.atlassian.net/browse/KAN-42) | iPhone/Android клиент и secure sync contract | m5 | To Do |
| [KAN-43](https://clawiq.atlassian.net/browse/KAN-43) | Voice и multi-agent readiness после стабильного core | m5 | To Do |

## Очередность

M1: OpenClaw contract (KAN-33), durable lifecycle (KAN-23), routing corpus (KAN-22), clean-clone/CI (KAN-38), dependencies (KAN-39). Cloud policy (KAN-24) проектируется до cloud; текущий release local-only.

Потом M2 memory/privacy, M3 desktop distribution, M4 scoped skills, M5 mobile/voice. Старые KAN-1…KAN-14 принадлежат предыдущему плану; snapshot сохранён локально перед reset.
