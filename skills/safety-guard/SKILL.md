---
name: safety-guard
description: Apply careful, freeze, and guard behaviors to dangerous commands, broad edit scope, and high-impact operations. Use when execution needs command warnings, path restrictions, or combined safety guardrails.
---

# Safety Guard

Apply practical safety controls around execution.

## Modes

- `careful`: warn on destructive or high-impact commands
- `freeze`: restrict edits to explicit paths or directories
- `guard`: combine both

## Rules

- Prefer the narrowest workable edit scope.
- If a command is hard to reverse, treat it as at least `MEDIUM`.
- If the run crosses both broad write scope and destructive potential, use `guard`.
- Record active guardrails in `vetter_report`.
