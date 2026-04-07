---
name: openspec-ultra-bridge
description: Bridge OpenSpec change artifacts into Ultra-Orchestrator execution artifacts. Use when a repo follows OpenSpec for proposal, design, tasks, and archive, but execution should remain controlled by Ultra-Orchestrator through TaskManifest, WorkPackage, review, QA, risk gates, and ledger-based orchestration.
---

# OpenSpec Ultra Bridge

Treat OpenSpec as the spec source-of-truth and Ultra-Orchestrator as the execution control plane.

## Priority

Absorb OpenSpec advantages without weakening the existing Ultra-Orchestrator architecture.

Prioritize these four advantages first:

1. Persistent spec assets
2. Change-based workflow
3. Archive discipline
4. Spec-first task decomposition input

Do not let this bridge replace Ultra's state machine, review, QA, risk vetter, safety guard, or execution ledger ownership.

## Purpose

Use this skill to translate between:

- OpenSpec change artifacts
- Ultra-Orchestrator execution artifacts

The bridge must not replace OpenSpec. It must map OpenSpec artifacts into Ultra execution objects and map Ultra review and QA feedback back into OpenSpec update suggestions.

## Inputs

Expect one or more of these OpenSpec artifacts:

- `proposal.md`
- `design.md`
- `tasks.md`
- spec delta artifacts
- change metadata such as `change-id`

Optionally consume these Ultra-side artifacts:

- `TaskManifest`
- `WorkPackage`
- `AgentResult`
- `RunOutput`
- `ExecutionLedger` summary

## Produce

Generate these Ultra-side artifacts when possible:

- `TaskManifest`
- `WorkPackage`
- `change-id <-> task-id` mapping notes
- archive gate readiness notes

Generate these OpenSpec-side feedback outputs when possible:

- task refinement suggestions
- design update suggestions
- failure-context updates
- archive blocking reasons

## Mapping rules

- Map `change-id` to `TaskManifest.id`.
- Map proposal summary to `goal`.
- Map design constraints to `constraints`.
- Map OpenSpec task dependencies to `dependencies`.
- Map task acceptance criteria or spec delta checks to `success_criteria` and `acceptance_checks`.
- Map affected components or files to `owned_paths`.

## Orchestration rules

- Preserve OpenSpec as the spec source-of-truth.
- Preserve Ultra-Orchestrator as the orchestration source-of-truth.
- Do not rewrite OpenSpec artifacts into Ultra-native storage unless the user explicitly asks for that migration.
- Prefer artifact-driven handoff over conversation-history handoff.
- Treat archive as gated by Ultra review, QA, and risk decisions.
- Use OpenSpec as a higher-quality frontend for planning, not as a replacement for dispatch, review, or QA.

## Worktree guidance

When Git Worktree is used:

- Prefer one OpenSpec change per worktree.
- Record worktree path in run metadata.
- Use owned-path rules and active write locks before parallel execution.

## Pilot guidance

When validating this bridge on a real project such as `/teammate`:

- Start with one change at a time.
- Prefer one feature task, one bug-fix task, and one task that forces a review or QA loopback.
- Judge success by bridge stability, not by feature count.

## Change and slice contract

This bridge must preserve a strict division:

- OpenSpec `change` = specification source-of-truth and long-lived progress node
- Ultra `slice` = execution source-of-truth for implementation progress inside a change

Do not collapse them into one concept.

When bridging, always make the current slice explicit for the selected change.

## Required change scaffold

For every newly opened change, initialize at minimum:

- `proposal.md`
- `tasks.md`
- `ultra-bridge.md`

The initial bridge status should default to:

- `slice_0_spec_ready` if the change is opened and ready for implementation
- `slice_0_not_opened` only for program-level ledgers or unopened planned changes

## Required ultra-bridge fields

Each `ultra-bridge.md` should include or imply:

- `change_id`
- `milestone`
- `status`
- `task_manifest_focus`
- `work_package_scope`
- `next_slice`

If a field is not known yet, write the narrowest truthful placeholder rather than omitting slice status.

## Status synchronization

After each completed slice, the bridge should push status intent back into OpenSpec-facing artifacts:

- update `ultra-bridge.md` status
- update `tasks.md` task checks when implementation actually landed
- suggest roadmap or current-status tally changes when opened/unopened counts changed

Do not treat conversation text as an acceptable substitute for status synchronization.

## Batch initialization mode

When a program has many unopened planned changes, the bridge may be used to:

1. enumerate all planned changes
2. classify them as `opened` or `unopened`
3. create missing change skeletons in batches
4. stamp each opened change with an initial slice status

This is the preferred way to normalize a long-running program before large implementation waves.

## Efficiency feedback loop

When a single change is used as a trial run, the bridge should also emit:

- whether the change size was appropriate
- whether the owned-path scope was narrow enough
- what friction came from spec mapping versus implementation
- what should be added back into the bridge workflow template

Use this to improve bridge stability over time rather than treating every change as isolated.

## Read references on demand

- `references/mapping.md` for detailed field mapping
- `references/workflow.md` for end-to-end fused workflow
- `references/archive-gate.md` for archive readiness conditions
- `references/adoption-priorities.md` for what to absorb first from OpenSpec
- `references/teammate-pilot.md` for pilot acceptance on `/teammate`
