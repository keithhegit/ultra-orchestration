---
name: autoplan
description: Automatically chain intake, planning, spec review, and plan refinement into one orchestrated planning pass, surfacing only decisions that need explicit user approval. Use when the user wants a fast but disciplined planning workflow.
---

# Autoplan

Run the planning pipeline end to end.

## Sequence

1. `$clarify-and-intake`
2. `$decision-complete-planner`
3. `$spec-review`
4. plan refinement

## Rules

- Surface only unresolved decisions that materially affect scope, architecture, or user-facing behavior.
- If the spec review returns `rework_required`, revise the plan before presenting it.
- Keep the final plan concise but decision complete.
