# ADR-004 — Desktop-first

Status: Accepted, 2026-10-07.

Decision: standalone Windows Electron first, далее macOS/Linux и mobile через общий application contract. Renderer sandboxed, без Node/network/file APIs. Core operations идут по validated narrow IPC.

Consequence: UI/runtime отдельно от routing/storage; unsigned portable preview сейчас, signing/update delivery later. Electron wrapper не считается native mobile foundation; shared service contract должен пережить замену интерфейса.
