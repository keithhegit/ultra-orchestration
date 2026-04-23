---
name: ultra-vnext-core
description: Primary entry point and router for Codex Ultra vNext. Use this single skill to start an orchestrated run for new features, bug fixes, OpenSpec changes, multi-file work, review/QA-heavy work, or any task that needs planning, dispatch, risk gates, execution control, review, QA, delivery evidence, and retro. The core skill decides which vNext subskills to load and in what order.
---

# Ultra VNext Core

Use this skill as the main entry point for the vNext suite. The user should not
need to list every subskill. Route the request, load only the needed sibling
skills, and keep the run moving through the control plane.

## Startup Contract

Recommended user invocation:

```text
$ultra-vnext-core <task description>
```

OpenSpec invocation:

```text
$ultra-vnext-core OpenSpec change <change-id or path>: <task description>
```

Bug fix invocation:

```text
$ultra-vnext-core bugfix: <symptom, failing behavior, or suspected area>
```

If the client exposes slash aliases, `/ultra-vnext-core` can be used the same
way.

## Router Duties

When invoked:

1. Classify the task.
2. Decide the minimal subskill sequence.
3. Load only the needed sibling skills.
4. Execute the fixed state machine.
5. Produce delivery artifacts or a clear blocker.

Do not ask the user to manually name every subskill.

## Routing Table

| Task signal | Route |
|---|---|
| vague idea, new feature, UX/API design, architecture-sensitive work | `ultra-brainstorming -> ultra-planning -> ultra-risk-vetting -> ultra-execution-control -> ultra-review -> ultra-qa -> ultra-delivery` |
| clear multi-file implementation | `ultra-planning -> ultra-risk-vetting -> ultra-execution-control -> ultra-review -> ultra-qa -> ultra-delivery` |
| OpenSpec change path, `openspec/changes`, proposal/design/tasks, archive workflow | `openspec-ultra-bridge-v2 -> ultra-planning -> ultra-risk-vetting -> ultra-execution-control -> ultra-review -> ultra-qa -> ultra-delivery` |
| bug, regression, failing test, broken behavior | `ultra-planning -> ultra-risk-vetting -> ultra-execution-control -> ultra-review -> ultra-qa -> ultra-delivery` |
| review-only request | `ultra-review -> ultra-delivery` |
| QA-only request | `ultra-qa -> ultra-delivery` |
| high-risk command, publishing, destructive write, credentials, external mutation | `ultra-risk-vetting` before any execution |

If a task is trivially small, you may compress phases, but record the skipped
phase and reason in the orchestration log.

## Core Rules

1. Treat orchestration as a finite-state machine, not a one-way waterfall.
2. Hand off artifacts, not raw chat history.
3. Let the host update the ledger; the model proposes state changes but should
   not freehand large ledger rewrites.
4. Allow parallelism only when the DAG is ready and write scopes do not overlap.
5. Require evidence before promotion into review, QA, or final delivery.

## Standard State Machine

Default phases:

`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`

Required loopbacks:

- `Review -> Execute` when the plan is valid but the work is wrong
- `QA -> Execute` when behavior is wrong but architecture is still valid
- `QA -> Plan` when the failure exposes a planning or requirement flaw

Default retry policy:

- transient failures: at most 1 bounded retry per work package
- repeated or hard blockers: escalate with summary, evidence, and next-step ask

## Context Firewall

Do not pass the entire upstream conversation to downstream workers by default.
Pass only:

- the relevant `TaskManifest`
- the assigned `WorkPackage`
- file pointers or artifact paths the worker needs
- failure context if the task is a retry or reroute

This rule keeps OpenSpec-style durable artifacts and design-first discipline
available without letting token growth or inherited mistakes take over the run.

## Safe Parallelism

Dispatch a task in parallel only when all of the following are true:

- its dependencies are satisfied in the task DAG
- its `owned_paths` do not intersect with another active write package
- its inputs are stable enough that the worker will not need speculative design
- its acceptance checks are concrete enough for independent verification

If any condition is false, serialize.

## Shared Outputs

Every orchestrated run should converge on these top-level artifacts:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`

Every child task should converge on:

- `TaskManifest`
- `WorkPackage`
- `AgentResult`

See [contracts](references/contracts.md) and
[state-machine](references/state-machine.md).

## Scripts

- `scripts/new_run.py`
  initialize a run directory with a starter ledger and artifact folders
- `scripts/validate_contracts.py`
  validate required top-level fields for the core JSON artifacts

## Read Next

- Read [design-tenets](references/design-tenets.md) for the governing rules.
- Read [routing](references/routing.md) for detailed routing examples.
- Read [source-synthesis](references/source-synthesis.md) for how this vNext
  suite combines Superpowers, OpenSpec, gstack, karpathy-guidelines, and OMX.
