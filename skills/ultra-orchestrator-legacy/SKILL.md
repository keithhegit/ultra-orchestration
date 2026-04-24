---
name: ultra-orchestrator-legacy
description: Legacy compatibility entry point for the original Ultra Orchestrator flow. Use only when you need the older lightweight stage-based orchestration behavior without the new strict OpenSpec-first control plane.
---

# Ultra Orchestrator Legacy

This is the legacy compatibility entry point. New runs should use
`$ultra-orchestrator`, which now points to the strict mainline protocol.

Drive the run as a control plane, not as a generic helper.

## Run the workflow

Execute stages in this exact order:

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

Treat this as a state machine, not a one-way waterfall.

Use these feedback loops when needed:

- `Review -> Execute` when the result fails spec or engineering review
- `QA -> Execute` when implementation is locally wrong but the plan still stands
- `QA -> Plan` when QA reveals an architecture or requirement mistake

Do not skip a stage unless the task is trivially small. If you skip, state why in the orchestration log.

## Produce mandatory artifacts

Every run must produce these top-level outputs:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`

Use the canonical field shapes in [`references/contracts.md`](references/contracts.md).

## Use supporting skills

Invoke these sibling skills by phase:

- `$clarify-and-intake` for intake normalization
- `$decision-complete-planner` for task graph creation
- `$dispatch-and-track` for work package assignment and ledger updates
- `$spec-review` before implementation when scope or interfaces are non-trivial
- `$code-review` after implementation and before integration
- `$qa-verify` when behavior changed or user flows matter
- `$deliver-and-retro` to assemble final outputs
- `$risk-vetter` before new tools, skills, or high-impact actions
- `$safety-guard` when commands or write scope look risky
- `$autoplan` when the user wants a fast planning pipeline without manual phase handoffs

## Enforce role boundaries

Keep one active role per phase:

- Intake Lead
- Planner
- Architect/Eng Reviewer
- Worker
- Reviewer
- QA
- Integrator

Do not let the Planner perform broad implementation. Do not let the Integrator silently redo delegated work. Do not accept Reviewer approval when acceptance checks were undefined.

## Dispatch rules

- Parallelize only independent work packages.
- Only dispatch in parallel when dependencies are satisfied and `owned_paths` are disjoint.
- Treat overlapping `owned_paths` as write-lock conflicts and serialize them.
- Allow one constrained retry for transient failures.
- Escalate hard blockers with summary, evidence, and suggested next step.

When in doubt, prefer serial execution over unsafe parallelism.

## Review rules

Run two gates:

1. Specification consistency
2. Engineering quality

Use the compact multi-lens checklist in [`references/review-lenses.md`](references/review-lenses.md).

Do not integrate conclusions that lack evidence.

## Ledger ownership

Treat `ExecutionLedger` as a control-plane artifact owned by the host orchestration layer.

- Let LLMs produce structured artifacts and status intent.
- Let scripts or the outer state machine update ledger fields precisely.
- Do not ask an LLM to rewrite a large ledger JSON blob from scratch in a long conversation.

## Context firewall

Default to artifact-driven handoff.

- Pass `TaskManifest`, `WorkPackage`, `AgentResult`, and narrow file pointers.
- Do not pass full upstream chat history to downstream roles unless it is truly necessary.
- Keep context on a need-to-know basis to reduce token pollution and inherited mistakes.

## Safety rules

Before using external tools, unknown skills, destructive commands, or broad write scopes:

1. Run `$risk-vetter`
2. Apply `$safety-guard` if needed
3. Record the decision in `vetter_report`

Use these policy thresholds:

- `LOW`: allow
- `MEDIUM`: allow with guardrails
- `HIGH`: require explicit approval
- `EXTREME`: block unless the user clearly approves

## Use scripts when helpful

- Run `scripts/new_run.py` to scaffold a run ledger and output shell.
- Run `scripts/validate_run.py` to validate a completed run artifact.

## Keep context compact

Load detailed references only when needed:

- [`references/contracts.md`](references/contracts.md) for canonical shapes
- [`references/workflow.md`](references/workflow.md) for stage-by-stage guidance
- [`references/review-lenses.md`](references/review-lenses.md) for review criteria
- [`references/examples.md`](references/examples.md) for example run artifacts

## Slice-driven execution

When the repository uses OpenSpec changes, treat `change` and `slice` as different layers:

- `change` is the specification and progress ledger unit
- `slice` is the implementation, verification, and commit unit

Default execution stack:

1. `Program`
2. `Milestone`
3. `Change`
4. `Slice`

Do not report day-to-day engineering progress only at milestone granularity when a slice-level view is available.

## Required slice status discipline

Use this canonical slice status vocabulary:

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

For every active change, Ultra should know:

- current slice status
- next intended slice
- owned paths for the current slice
- required verification gate before advancing slice status

## Ledger synchronization rule

After each completed implementation slice:

1. update the OpenSpec-side change status intent
2. update roadmap or current-status tally if counts changed
3. record the verification result that justifies the new slice status

Do not leave slice status advanced in code or conversation only. The ledger must match the implementation state.

## Single-change trial mode

When validating workflow speed or skill quality, prefer a `single-change trial`:

1. open or select one change
2. set `slice_0_spec_ready`
3. implement exactly one bounded slice
4. run the minimum meaningful verification
5. record friction, speed, and repeatability notes

Use this mode to calibrate whether a change is too broad, whether owned paths are too wide, or whether orchestration overhead is too high.

## Batch-opening guidance

When many changes remain unopened, Ultra should prefer:

- opening only the next highest-value changes needed for the current execution wave
- assigning slice status at creation time
- avoiding a backlog of ambiguous change folders with no slice state

Open many changes in one pass only when the user explicitly wants backlog initialization or ledger normalization.
