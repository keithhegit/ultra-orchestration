---
name: decision-complete-planner
description: Turn a structured intake artifact into a decision-complete plan, task graph, dependency map, owned paths, acceptance checks, expected outputs, and retry assumptions. Use when work spans multiple steps, files, or roles and needs explicit orchestration.
---

# Decision Complete Planner

Produce a plan another agent can execute without filling in key decisions.

In mainline `STRICT` or `STRICT_OPENSPEC` runs, planning must produce
JSON-ready artifacts. Markdown summaries may explain the plan, but they do not
replace the machine-checkable `TaskManifest` and `WorkPackage` objects.

## Produce

- Short summary
- Ordered implementation phases
- JSON `TaskManifest` entries
- JSON `WorkPackage` entries
- Parallel vs serial execution boundaries
- Acceptance checks per package
- Retry budget assumptions for each non-trivial work package
- Current OpenSpec change and slice status when `STRICT_OPENSPEC` applies

Use canonical field names from [`../ultra-orchestrator/references/contracts.md`](../ultra-orchestrator/references/contracts.md).

## Rules

- Prefer behavior-level decomposition over file-by-file decomposition.
- Mark shared write scope explicitly.
- Treat shared write scope as a write-lock conflict, not a soft warning.
- Keep non-goals visible.
- If a design choice is still unresolved, surface it instead of hiding it in prose.
- For development tasks, prefer one bounded OpenSpec change and one current
  slice before dispatch.
- Do not send work to dispatch if artifact validation cannot be planned.

## Hand off

Send the plan to `$spec-review` for completeness, then to `$dispatch-and-track`.
