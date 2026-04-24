---
name: ultra-orchestrator
description: Primary Ultra Orchestration entry point for strict Codex-controlled engineering runs. Use this single skill for development, bug fixes, OpenSpec work, multi-file implementation, review/QA-heavy tasks, risk-gated work, or any run that needs automatic mode selection, OpenSpec bootstrap, machine-checkable TaskManifest and WorkPackage artifacts, ledger tracking, slice DAG execution, review, QA, delivery evidence, and retro.
---

# Ultra Orchestrator

Use this skill as the default public entry point for Ultra Orchestration.
The user should only need to invoke `$ultra-orchestrator <task description>`.

This is the mainline successor to the vNext protocol. The old stable workflow
is preserved as `ultra-orchestrator-legacy`.

## Startup Contract

Recommended invocation:

```text
$ultra-orchestrator <task description>
```

OpenSpec invocation:

```text
$ultra-orchestrator OpenSpec change <change-id or path>: <task description>
```

Compatibility invocation:

```text
$ultra-vnext-core <task description>
```

If the client exposes slash aliases, `/ultra-orchestrator` can be used the same
way.

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

## Routing Table

| Task signal | Default mode | Route |
|---|---|---|
| development, feature, bugfix, multi-file implementation, pilot, full orchestration test | `STRICT_OPENSPEC` | OpenSpec bootstrap or bridge -> planning -> risk -> dispatch -> review -> QA -> delivery |
| existing OpenSpec change path, `openspec/changes`, proposal/design/tasks, archive workflow | `STRICT_OPENSPEC` | bridge -> planning -> risk -> dispatch -> review -> QA -> delivery |
| development task where OpenSpec cannot be used | `STRICT` | planning -> risk -> dispatch -> review -> QA -> delivery |
| review-only request | `LIGHT` | review -> delivery |
| QA-only request | `LIGHT` | QA -> delivery |
| high-risk command, publishing, destructive write, credentials, external mutation | current mode plus risk gate | risk before execution |

If a task is tiny but still a development task, keep `STRICT_OPENSPEC` unless
the user explicitly asks for lightweight execution.

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

Default to a single bounded change and one current implementation slice.
OpenSpec owns durable specification state. Ultra owns execution control.

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

Every active change must name current slice status, next slice, owned paths,
and the verification gate required before advancing.

## State Machine

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

Pass artifacts, not full chat history:

- relevant `TaskManifest`
- assigned `WorkPackage`
- file pointers or artifact paths
- failure context for retries or reroutes

## Safe Parallelism

Dispatch work in parallel only when:

- dependencies are satisfied in the DAG
- `owned_paths` do not intersect with another active write package
- inputs are stable enough to avoid speculative design
- acceptance checks are concrete enough for independent verification

If any condition is false, serialize.

## Delivery Requirement

Every delivery must include:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`
- `control_surface_used`

`control_surface_used` must state:

- `run_mode`
- `used_openspec_change`
- `used_openspec_bridge`
- `used_run_ledger`
- `used_contract_validation`
- `used_slice_dag`
- `used_dynamic_qa`
- skipped control surfaces and reasons

## Supporting Skills

Route through these siblings as needed:

- `$openspec-ultra-bridge` for OpenSpec change mapping
- `$decision-complete-planner` for JSON-ready task graphs
- `$dispatch-and-track` for ledger and write-lock tracking
- `$risk-vetter` and `$safety-guard` for risk gates and guardrails
- `$spec-review` and `$code-review` for review gates
- `$qa-verify` for verification
- `$deliver-and-retro` for final packaging

## Read Next

- Read [routing](references/routing.md) for strict routing examples.
- Read [contracts](references/contracts.md) for machine-checkable artifacts.
- Read [state-machine](references/state-machine.md) for phase and loopback rules.
- Read [design-tenets](references/design-tenets.md) for governing principles.
