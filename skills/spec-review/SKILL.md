---
name: spec-review
description: Review plans and work packages for specification completeness, hidden assumptions, dependency gaps, interface risks, and acceptance-check quality. Use after planning and before substantial implementation.
---

# Spec Review

Audit the plan before implementation begins.

## Check

- Goal clarity
- Scope and non-goals
- Dependency correctness
- Acceptance-check quality
- Hidden assumptions
- Failure modes and interface gaps

## Output

Return one of:

- `approved`
- `approved_with_followups`
- `rework_required`

Use concise findings with evidence. If the plan is blocked by unresolved decisions, say so directly.
