---
name: openspec-ultra-bridge-v2
description: Bridge OpenSpec change artifacts into Codex Ultra vNext execution contracts. Use when a repo stores long-lived specs in `openspec/changes` or `openspec/specs`, but execution should still flow through Ultra manifests, work packages, review, QA, ledger tracking, and final delivery rather than replacing Ultra with a separate control plane.
---

# OpenSpec Ultra Bridge V2

OpenSpec is the specification layer. Ultra remains the control plane.

This skill is a compatibility bridge for vNext users. The default public entry
point is now `$ultra-orchestrator`, which invokes this bridge as needed.

## What This Skill Does

Translate:

- `proposal.md`
- `design.md`
- `tasks.md`
- optional `ultra-bridge.md`

into:

- `TaskManifest`
- `WorkPackage` set
- bridge notes for review and QA

## Bridge Rules

1. Do not let OpenSpec replace Ultra's execution ledger or review gates.
2. Prefer one bounded `change` as the default execution unit.
3. Use OpenSpec for durable spec memory and archive history.
4. Use Ultra for dispatch, retries, review, QA, and delivery.
5. In `STRICT_OPENSPEC`, do not continue without change scaffold, slice status,
   JSON-ready planning artifacts, and ledger handoff.

## How To Use

1. Point the bridge at an OpenSpec change directory.
2. Read the proposal, design, and task assets.
3. If `ultra-bridge.md` exists, treat it as the preferred mapping hint.
4. Normalize the change into a reviewable `TaskManifest` and `WorkPackage`
   set.
5. Hand off those outputs to `ultra-planning` or `ultra-execution-control`.

## Required Change Scaffold

For newly opened strict changes, initialize at minimum:

- `proposal.md`
- `design.md`
- `tasks.md`
- `ultra-bridge.md`

Default status:

- `slice_0_spec_ready` when the change is ready for implementation
- `slice_0_not_opened` only for unopened planned changes

## Slice Contract

Keep `change` and `slice` separate:

- OpenSpec `change` is the durable spec and progress node
- Ultra `slice` is the implementation and verification unit

Every bridge output should name:

- `change_id`
- current slice status
- next slice
- owned paths
- review targets
- QA targets
- blockers for status sync or archive

## Script

Use `scripts/bridge_change.py` to extract and materialize bridge artifacts from
a real OpenSpec change directory.

## Read Next

- [bridge-pattern](references/bridge-pattern.md)
- [teammate-pilot](references/teammate-pilot.md)
- the shared contracts in `../ultra-vnext-core/references/contracts.md`
