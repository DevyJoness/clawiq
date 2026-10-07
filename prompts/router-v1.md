# ClawIQ Router v1 — intent reference

Executable truth: core/router.mjs. Этот Markdown не исполняется как model-selection engine.

- Image attached → vision → installed qwen2.5vl:7b.
- Code/debug intent → installed qwen2.5-coder:14b, otherwise qwen3:14b.
- Analysis/planning/conversation → installed qwen3:14b.
- Research intent → local analysis with explicit no-live-search limitation.

Unavailable local model: explain installation requirement; no implicit cloud fallback. Tool permissions и budget/privacy policies должны применяться вне LLM. Объяснять route, не гарантировать optimal model choice без eval evidence.
