# Архитектура ClawIQ

Обновлено: 2026-10-07. Current и target разделены намеренно.

## Current v0.4.0

```text
Electron renderer (file assets, no network/Node)
          ↓ narrow validated IPC
Electron main (native image picker, lifecycle)
          ↓
core/assistant.mjs
  ├─ router.mjs → task + local model + explanation
  ├─ store.mjs → isolated conversation JSON
  └─ loopback Ollama HTTP → qwen3 / coder / qwen2.5vl
```

Renderer не содержит токенов, не читает файлы и не выбирает backend URL. Main проверяет sender и mainFrame, лимитирует изображение 10 МБ и проверяет PNG/JPEG signature. Routing не вызывает LLM для классификации: это проверяемые эвристики MVP. Reason и selected model возвращаются вместе с ответом.

History: OS userData/sessions, атомарная запись JSON через rename, random conversation ID. До 20 завершённых предыдущих messages передаются модели. Незавершённые/ошибочные запросы видны, но исключаются из следующего контекста. Никаких файлов/данных Люськи.

## Target

```text
Windows / macOS / Linux / future mobile
               ↓ shared application contract
identity + scoped sessions + permissions + routing
               ↓
OpenClaw personal agent / provider adapters / skills
               ↓
local models + explicitly enabled cloud + approved tools
```

Существующий OpenClaw сохраняется как выбранный tool/agent runtime. Его HTTP agent endpoint — operator credential boundary; он не должен быть доступен renderer или public network. Перед подключением нужен dedicated personal agent, local-first policy, action approvals и тесты permissions. Текущий user config может иметь cloud-first default и fallback; v0.4.0 его не использует и не переписывает.

## Отдельные системы

- Люська в отдельном репозитории/runtime; personal memory не передаётся в группы.
- automation/jira_qa — legacy isolated service, не часть desktop process. Webhook deployment отключён; очередь только in-memory, до production нужны durable jobs и evidence-version idempotency.
- scripts/Start-ClawIQ.ps1 управляет legacy OpenClaw инфраструктурой, не запускает новый UI. Для UI — Start-ClawIQDesktop.ps1.

## Extension rules

Интерфейсы используют contract, не бизнес-логику. Cloud fallback требует явной policy и выбора credentials. Tool action не считается выполненным до подтверждённого результата. Новые providers/skills должны иметь capability, timeout, cancellation, observability и test coverage. Shared memory означает общую модель данных с access scopes, не один публичный общий transcript.
