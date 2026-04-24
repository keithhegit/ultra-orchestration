# Ultra Orchestration vNext Skill Tree

This directory contains vNext compatibility aliases and preview internals for
Ultra Orchestration. The main public entry point now lives in
`../skills/ultra-orchestrator`.

## Goals

- preserve vNext invocation compatibility while the strict protocol moves into
  the mainline `ultra-orchestrator`
- keep specification, execution, review, QA, risk, and delivery roles explicit
- support artifact-driven handoff instead of full chat-history inheritance
- make risk decisions, QA evidence, and final delivery logs auditable

## Skill Levels

### Rigid workflow skills

- `ultra-vnext-core`
- `ultra-brainstorming`
- `ultra-planning`
- `ultra-risk-vetting`
- `ultra-delivery`

These skills define protocol gates and should be followed strictly.

### Controlled execution skills

- `ultra-execution-control`
- `ultra-review`
- `ultra-qa`
- `openspec-ultra-bridge-v2`

These skills may adapt to context, but must not cross contracts, safety gates,
or role boundaries.

## Skills

- `ultra-vnext-core`
  compatibility alias for the mainline `ultra-orchestrator` strict protocol
- `ultra-brainstorming`
  design-first discovery and approval gates before planning or coding
- `ultra-planning`
  decision-complete task graphs with path ownership and retry assumptions
- `ultra-execution-control`
  dispatch, lock enforcement, execution tracking, and blocker routing
- `ultra-review`
  spec and engineering review with explicit accept, reject, or reroute decisions
- `ultra-qa`
  scenario-based static and dynamic QA with pass or fail outcomes
- `ultra-risk-vetting`
  risk classification, approval thresholds, and guardrail selection
- `ultra-delivery`
  final deliverable, orchestration log, vetter report, and retro packaging
- `openspec-ultra-bridge-v2`
  map OpenSpec change assets into Ultra execution artifacts

## Mainline Relationship

| vNext skill | Mainline relationship | Migration type |
|---|---|---|
| `ultra-vnext-core` | `ultra-orchestrator` | compatibility alias |
| `ultra-brainstorming` | `clarify-and-intake` + early `autoplan` | enhanced version |
| `ultra-planning` | `decision-complete-planner` | direct counterpart |
| `ultra-execution-control` | `dispatch-and-track` + part of `safety-guard` | integrated version |
| `ultra-review` | `spec-review` + `code-review` | merged version |
| `ultra-qa` | `qa-verify` | direct counterpart |
| `ultra-risk-vetting` | `risk-vetter` + approval part of `safety-guard` | direct counterpart |
| `ultra-delivery` | `deliver-and-retro` | direct counterpart |
| `openspec-ultra-bridge-v2` | `openspec-ultra-bridge` | enhanced version |

## Usage

Install these folders into your target agent's documented skills directory.
Start new work with the mainline entry skill:

```text
$ultra-orchestrator <task description>
```

Existing vNext prompts still work:

```text
$ultra-vnext-core OpenSpec change <change-id or path>: <task description>
```

`ultra-vnext-core` should follow the same run-mode decision rules as
`ultra-orchestrator`, including `STRICT_OPENSPEC` preference for development
work.

`ultra-planning` is the hard gate before controlled dispatch. If the resulting
plan still leaves key decisions to the implementer, the run is not ready.

For full installation and startup prompts, see the root
[`README.md`](../README.md).
