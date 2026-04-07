---
name: decision-complete-planner
description: Turn a structured intake artifact into a decision-complete plan, task graph, dependency map, owned paths, acceptance checks, expected outputs, and retry assumptions. Use when work spans multiple steps, files, or roles and needs explicit orchestration.
---

# Decision Complete Planner

Produce a plan another agent can execute without filling in key decisions.

## Produce

- Short summary
- Ordered implementation phases
- `TaskManifest` entries
- `WorkPackage` entries
- Parallel vs serial execution boundaries
- Acceptance checks per package
- Retry budget assumptions for each non-trivial work package

Use canonical field names from [`../ultra-orchestrator/references/contracts.md`](../ultra-orchestrator/references/contracts.md).

## Rules

- Prefer behavior-level decomposition over file-by-file decomposition.
- Mark shared write scope explicitly.
- Treat shared write scope as a write-lock conflict, not a soft warning.
- Keep non-goals visible.
- If a design choice is still unresolved, surface it instead of hiding it in prose.

## Hand off

Send the plan to `$spec-review` for completeness, then to `$dispatch-and-track`.
