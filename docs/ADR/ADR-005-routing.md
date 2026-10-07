# ADR-005 — Router foundation

Status: Accepted, 2026-10-07.

Decision: classify text/image intent детерминированными правилами, выбрать только установленную local модель из allowlist, вернуть route explanation. Coding prefers coder then Qwen3; vision requires Qwen2.5-VL. Research intent сообщает отсутствие live search.

Consequence: reproducible MVP, но не semantic classifier и не universal optimal selection. Corpus/evals, timeout/failure policies и tool capability planning — следующие increments. Нет скрытого provider fallback.
