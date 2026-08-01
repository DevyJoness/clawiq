# ClawIQ Core Skill Proposal

## Goal

Create the first project-specific OpenClaw Skill for ClawIQ.

The skill should contain only conventions and engineering practices specific to the ClawIQ project.

It should not duplicate general programming knowledge already present in the language model.

---

## Description

Project conventions, engineering workflow, documentation awareness and development principles for ClawIQ.

---

## Proposed SKILL.md

---
name: clawiq-core
description: "Project conventions, engineering workflow, documentation awareness and development principles for ClawIQ."
---

# ClawIQ Core

Use this skill whenever working on the ClawIQ project.

## Project Documentation

Repository documentation:

- README.md
- ROADMAP.md
- ARCHITECTURE.md
- SETUP.md
- BUGS.md
- MAINTENANCE.md

Prompt documentation:

- docs/prompts/system-v1.md
- docs/prompts/coding-v1.md
- docs/prompts/router-v1.md
- docs/prompts/vision-v1.md

## Engineering Workflow

Always follow this order:

1. Understand the problem.
2. Diagnose using evidence.
3. Prefer built-in OpenClaw mechanisms.
4. Implement the solution.
5. Validate the result.
6. Update documentation if necessary.

## Development Principles

- Do not guess when verification is possible.
- Prefer built-in OpenClaw functionality over custom implementations.
- Distinguish temporary workarounds from permanent fixes.
- Keep project documentation synchronized with implementation.
- Prefer maintainable and well-documented solutions.

## Scope

This skill contains only project-specific conventions.

General software engineering knowledge should come from the language model itself.
