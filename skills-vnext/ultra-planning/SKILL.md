---
name: ultra-planning
description: Rigid decision-complete planning for Codex Ultra vNext. Use after intake, brainstorming, or OpenSpec bridge whenever work spans multiple files, roles, phases, or risk boundaries and must be turned into review-ready TaskManifest and WorkPackage artifacts with explicit dependencies, owned paths, acceptance checks, retry assumptions, and serial versus parallel execution rules.
---

# Ultra Planning

Use this skill as a rigid workflow gate before controlled dispatch. This skill
must remove planning ambiguity rather than summarize it.

## Hard Gate

Do not allow controlled dispatch until the plan includes:

- success criteria
- constraints
- non-goals
- owned paths
- acceptance checks
- dependency order
- risk level
- retry assumptions

If any of those are missing or still depend on chat interpretation, the plan is
not complete.

## When To Use

Planning is required when:

- the work spans multiple files or directories
- multiple phases or roles are involved
- OpenSpec change assets are being turned into execution packages
- review, QA, or risk gates need explicit targets
- parallel execution is being considered
- the implementer would otherwise need to make design or boundary decisions

Planning may be compressed only when:

- the task is truly tiny
- the write scope is narrow and obvious
- no risky command or external mutation is involved
- review and QA targets remain explicit

If you compress planning, record the reason in the orchestration log.

## Planning Workflow

1. Read the intake, brainstormed design, or OpenSpec bridge artifacts.
2. Check whether success criteria, constraints, and scope are already stable.
3. If not stable, route back to `ultra-brainstorming` or the intake step.
4. Define the top-level `TaskManifest`.
5. Split the work into one or more `WorkPackage` items.
6. Mark dependencies, owned paths, parallel groups, and serial boundaries.
7. Attach acceptance checks, risk level, and retry assumptions.
8. Record assumptions, blockers, and re-plan triggers.
9. Run the planning self-review before declaring the plan complete.

## Planning Standard

Produce one `TaskManifest` plus one or more `WorkPackage` items.

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

## Completion Standard

Planning is complete only when:

- a new implementer could start from the plan without inventing key decisions
- review knows what to inspect
- QA knows what behavior must be verified
- write ownership is explicit
- serial versus parallel execution is explicit
- blockers and re-plan triggers are named

If the plan still requires the implementer to decide boundaries, acceptance, or
parallelism, the plan is incomplete.

## Planning Self-Review

Before returning the plan, check:

- do any `owned_paths` overlap unexpectedly
- are acceptance checks concrete and verifiable
- do reviewer and QA receive explicit inspection targets
- is any work package write scope too broad
- do dependencies still rely on chat memory rather than artifacts
- does any package mix planning, implementation, and review responsibility
- would a failure in one package force a re-plan that is not yet documented

## Failure Handling

- If success criteria, scope, or constraints are still unstable, route back to
  `ultra-brainstorming`.
- If OpenSpec assets are incomplete or contradictory, route back to
  `openspec-ultra-bridge-v2` or spec preparation.
- If planning reveals that one request actually contains several independent
  initiatives, decompose the work and plan only the first bounded unit.

## Role Discipline

- planner defines work, but does not silently become the implementer
- reviewer tasks must not be mixed into implementation packages
- integrator tasks should package accepted outputs, not redo worker code

## Output Template

Return in this order:

1. one `TaskManifest`
2. ordered `WorkPackage` items
3. parallel groups or serial sequence notes
4. assumptions
5. blockers
6. re-plan triggers

## Examples

- Read [planning-workflow](references/planning-workflow.md) for the rigid flow.
- Read [planning-anti-patterns](references/planning-anti-patterns.md) for what
  makes a plan unsafe or incomplete.
- Read [work-package-examples](references/work-package-examples.md) for one
  normal multi-file feature and one OpenSpec change route.
- Read [planning-checklist](references/planning-checklist.md) before finalizing.
