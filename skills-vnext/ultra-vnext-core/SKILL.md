---
name: ultra-vnext-core
description: Compatibility and preview alias for the main Ultra Orchestrator strict protocol. Use this single skill to start vNext-style orchestrated runs when users still invoke ultra-vnext-core; it should follow the same run-mode decision, strict OpenSpec preference, ledger, JSON artifact, contract validation, slice DAG, review, QA, delivery, and retro behavior as ultra-orchestrator.
---

# Ultra VNext Core

Use this skill as a compatibility alias for the mainline `$ultra-orchestrator`
protocol. The user should not need to list every subskill.

Prefer the same behavior as the new main entry point:

```text
$ultra-orchestrator <task description>
```

`$ultra-vnext-core <task description>` remains valid for existing users and
pilot runs.

## Run Mode Decision

Classify the run before planning or execution:

- `LIGHT`
  review-only, QA-only, explanation-only, or user-explicit lightweight work
- `STANDARD`
  user-explicit fast orchestration with bounded risk and no full control plane
- `STRICT`
  development work where OpenSpec is unavailable but ledger and JSON contracts
  are still required
- `STRICT_OPENSPEC`
  default for development work, bug fixes, multi-file implementation, pilots,
  full orchestration tests, OpenSpec work, slice DAG work, and control-plane
  validation

Development tasks must prefer `STRICT_OPENSPEC`. If that mode is impossible,
explain why and downgrade explicitly. Markdown-only artifacts are not enough
for `STRICT` or `STRICT_OPENSPEC`.

## Router Duties

When invoked:

1. classify the task and choose `run_mode`
2. create or require OpenSpec change scaffolding when `STRICT_OPENSPEC` applies
3. initialize the run ledger for `STRICT` and `STRICT_OPENSPEC`
4. route through the minimal required sibling skills
5. validate machine-checkable artifacts before delivery
6. produce delivery artifacts or a clear blocker

Do not ask the user to manually name every subskill.

## Strict Control Plane

For `STRICT` and `STRICT_OPENSPEC`, the run must use:

- `scripts/new_run.py` to initialize a run directory
- `ledger.json` as the execution state record
- JSON `TaskManifest`
- JSON `WorkPackage`
- JSON or structured `AgentResult`
- `scripts/validate_contracts.py` for core artifact validation
- explicit review and QA gates
- final `control_surface_used`

If a required script or artifact cannot be used, stop with a blocker instead
of silently downgrading to markdown-only orchestration.

## OpenSpec Bootstrap

When `STRICT_OPENSPEC` applies and no existing change is available, create or
request this scaffold:

```text
openspec/changes/<change-id>/proposal.md
openspec/changes/<change-id>/design.md
openspec/changes/<change-id>/tasks.md
openspec/changes/<change-id>/ultra-bridge.md
```

## Slice-Driven Execution

Keep `change` and `slice` separate:

- OpenSpec `change` is the specification and progress ledger unit
- Ultra `slice` is the implementation, verification, and commit unit

Use this slice status vocabulary:

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

## State Machine

Default phases:

`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`

Required loopbacks:

- `Review -> Execute` when the plan is valid but the work is wrong
- `QA -> Execute` when behavior is wrong but architecture is still valid
- `QA -> Plan` when the failure exposes a planning or requirement flaw

## Delivery Requirement

Every delivery must include:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`
- `control_surface_used`

`control_surface_used` must state `run_mode`, OpenSpec use, bridge use, ledger
use, contract validation use, slice DAG use, dynamic QA use, and skipped control
surfaces with reasons.

## Read Next

- Read [routing](references/routing.md) for strict routing examples.
- Read [contracts](references/contracts.md) for machine-checkable artifacts.
- Read [state-machine](references/state-machine.md) for phase and loopback rules.
- Read [design-tenets](references/design-tenets.md) for governing principles.
