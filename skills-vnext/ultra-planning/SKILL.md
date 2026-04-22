---
name: ultra-planning
description: Decision-complete planning for Codex Ultra vNext. Use after intake or brainstorming when work spans multiple files, roles, phases, or risk boundaries and needs an explicit task graph, path ownership, acceptance checks, retry assumptions, and parallel versus serial execution rules.
---

# Ultra Planning

Turn an approved problem statement into a plan that is complete enough for
controlled dispatch.

## Planning Standard

Produce a `TaskManifest` plus one or more `WorkPackage` items.

The plan is not complete until it defines:

- goal
- context
- success criteria
- constraints
- non-goals
- dependencies
- `owned_paths`
- expected outputs
- risk level
- acceptance checks
- retry budget or retry assumptions

## DAG And Lock Rules

For each work package, identify:

- upstream dependencies
- whether the task is parallel-safe
- which paths are read-only context
- which paths are write-owned

Only mark work as parallel-safe when both conditions hold:

1. all upstream dependencies are satisfiable without new design work
2. `owned_paths` do not intersect with another active write package

## Role Discipline

- planner defines work, but does not silently become the implementer
- reviewer tasks must not be mixed into implementation packages
- integrator tasks should package accepted outputs, not redo worker code

## Output Shape

Return:

- one `TaskManifest`
- an ordered list of `WorkPackage` items
- parallel groups or serial sequence notes
- explicit assumptions that may force a re-plan

Read [planning-checklist](references/planning-checklist.md) and the shared
contracts in `ultra-vnext-core`.
