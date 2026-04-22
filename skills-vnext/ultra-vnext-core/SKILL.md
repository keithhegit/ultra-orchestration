---
name: ultra-vnext-core
description: Shared orchestration contracts, state-machine rules, context-firewall handoff, and host-driven ledger guidance for Codex Ultra vNext. Use when building, reviewing, or running a multi-stage Codex workflow that needs consistent manifests, work packages, agent results, safe parallelism, retry limits, and auditable delivery artifacts.
---

# Ultra VNext Core

Use this skill as the shared operating contract for the rest of the vNext
suite. Load it first when the work spans multiple stages, roles, or artifacts.

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

This rule absorbs the best OpenSpec and Superpowers discipline while keeping
token growth under control.

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
- Read [source-synthesis](references/source-synthesis.md) for how this vNext
  suite combines Superpowers, OpenSpec, gstack, karpathy-guidelines, and OMX.
