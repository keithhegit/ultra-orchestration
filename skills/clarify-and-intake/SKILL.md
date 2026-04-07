---
name: clarify-and-intake
description: Normalize ambiguous user requests into a structured intake artifact with task description, context, success criteria, constraints, and task type. Use before planning or implementation whenever requirements are incomplete, mixed, or implicit.
---

# Clarify And Intake

Convert the raw request into an intake artifact before planning starts.

## Produce

Return a compact JSON-like structure with:

- `task_description`
- `context`
- `success_criteria`
- `constraints`
- `task_type`
- `open_questions`

## Rules

- Resolve discoverable facts from the repo or environment before asking questions.
- Prefer concrete, testable success criteria.
- Separate constraints from preferences.
- Produce artifacts that downstream roles can consume without inheriting the full chat history.
- If information is missing but low risk, choose a reasonable default and record it.
- If missing information would change architecture or public behavior, escalate clearly.

## Hand off

Pass the intake artifact to `$decision-complete-planner`.
If external tools or unfamiliar skills may be needed, flag `$risk-vetter`.
