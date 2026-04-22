---
name: ultra-execution-control
description: Dispatch and execution control for Codex Ultra vNext. Use after planning when work packages must be assigned, retries bounded, blockers surfaced, and write-lock safety enforced through DAG readiness, owned-path checks, careful or freeze guardrails, and host-driven ledger updates.
---

# Ultra Execution Control

Move work packages through execution without losing safety, ownership, or
auditability.

## Dispatch Rules

Dispatch a work package only when:

- dependencies are satisfied
- acceptance checks are concrete
- write ownership is explicit
- the task is not blocked by another active writer

If a task shares `owned_paths` with another in-flight task, serialize it.

## Ledger Rules

The ledger is the system of record. Keep it lightweight and host-driven.

- the model may propose state updates
- the host should apply the actual ledger change
- every blocker should include a short summary, evidence, and next-step ask
- every retry should increment a bounded counter

## Guardrails

Use:

- `careful` for risky or destructive commands
- `freeze` to limit writes to the declared path boundary
- `guard` when both are needed together

## Result Contract

Require every child execution unit to return:

- `task_id`
- `status`
- `summary`
- `changed_paths`
- `artifacts`
- `evidence`
- `risks`
- `followups`

If evidence is missing, do not mark the package review-ready.

Read [execution-rules](references/execution-rules.md) before dispatching.
