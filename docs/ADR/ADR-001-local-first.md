# ADR-001 — Local-first

Status: Accepted, 2026-10-07.

Decision: desktop/core предпочитают локальную Ollama. Cloud providers в 0.4.0 отключены. Отсутствие local модели вызывает явную ошибку. В будущих versions cloud fallback требует capability/privacy/budget policy и выбранных credentials.

Consequence: offline private inference, потребность в local resources; качество оценивается отдельно. Existing cloud-first OpenClaw config не применяется desktop автоматически.
