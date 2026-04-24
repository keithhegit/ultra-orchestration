---
name: dispatch-and-track
description: Assign work packages by role, enforce owned-path boundaries, manage execution state, track retries, blockers, review readiness, and host-driven ledger updates. Use when work is being handed off across phases or subagents.
---

# Dispatch And Track

Use the plan to route work safely and keep the run ledger current.

In `STRICT` and `STRICT_OPENSPEC`, the ledger is mandatory. If `ledger.json`
cannot be initialized or updated by the host/script layer, stop with a blocker
instead of replacing it with a prose-only log.

## Update

- `current_stage`
- `task_status`
- `dependencies_satisfied`
- `retry_counts`
- `max_retries`
- `active_write_locks`
- `blockers`
- `pending_review`
- `integration_status`
- current `run_mode`
- current OpenSpec change and slice status when present
- `control_surface_used` intent for delivery

## Rules

- Only treat a work package as runnable when its dependencies are satisfied.
- Parallelize only work packages with disjoint owned paths.
- If packages overlap, serialize them and record why.
- Record active write locks before execution starts.
- Allow one retry only for transient failures.
- Convert blockers into clear summaries with evidence and recommended next actions.
- Prefer host-script ledger updates over asking the model to rewrite the full ledger object.
- Require JSON or structured `AgentResult` before marking work review-ready.
- For `STRICT_OPENSPEC`, update or propose OpenSpec-side slice status after
  each completed implementation slice.

Use the ledger shape in [`../ultra-orchestrator/references/contracts.md`](../ultra-orchestrator/references/contracts.md).
