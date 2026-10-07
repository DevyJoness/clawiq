# ADR-006 — OpenClaw integration contract

Status: Accepted, 2026-10-07. Integration implementation planned.

Decision: сохранить OpenClaw для skills/tools и operator workflows, не создавать второй универсальный Gateway. 0.4.0 direct Ollama adapter закрывает local conversational MVP; не выдаётся за OpenClaw tool execution.

Before integration: dedicated personal agent, loopback endpoint, main-process-only credentials, explicit local/cloud model policy, scoped context, action approval и idempotent results. Operator bearer credentials не передаются renderer/public clients. Использовать существующий OpenClaw HTTP/agent/session APIs после contract tests.
