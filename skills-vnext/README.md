# Codex Ultra Orchestration vNext Skill Tree

This directory is an isolated vNext workspace for evolving Ultra-Orchestrator
without modifying the stable workspace-level skills under
`D:\Codex_workspace\.agents\skills`.

## Goals

- keep the current global skills stable
- prototype a stronger prompt and contract system for Codex App on Windows
- absorb the best ideas from Superpowers, OpenSpec, gstack, karpathy-style
  guidelines, and OMX without replacing Ultra as the control plane

## Skills

- `ultra-vnext-core`
  shared contracts, state-machine rules, host-driven ledger, and helper scripts
- `ultra-brainstorming`
  design-first discovery and approval gates before planning or coding
- `ultra-planning`
  decision-complete task graphs with path ownership and retry assumptions
- `ultra-execution-control`
  dispatch, lock enforcement, execution tracking, and blocker routing
- `ultra-review`
  spec and engineering review with explicit reject or reroute decisions
- `ultra-qa`
  scenario-based static and dynamic QA with pass or fail outcomes
- `ultra-risk-vetting`
  risk classification, approval thresholds, and guardrail selection
- `ultra-delivery`
  final deliverable, orchestration log, vetter report, and retro packaging
- `openspec-ultra-bridge-v2`
  map OpenSpec change assets into Ultra execution artifacts

## Stable To vNext Mapping

| vNext skill | Stable relationship | Replacement type |
|---|---|---|
| `ultra-vnext-core` | `ultra-orchestrator` | partial replacement plus shared kernel |
| `ultra-brainstorming` | `clarify-and-intake` + early `autoplan` | enhanced replacement |
| `ultra-planning` | `decision-complete-planner` | direct replacement |
| `ultra-execution-control` | `dispatch-and-track` + part of `safety-guard` | enhanced integration |
| `ultra-review` | `spec-review` + `code-review` | merged replacement |
| `ultra-qa` | `qa-verify` | direct replacement |
| `ultra-risk-vetting` | `risk-vetter` + approval part of `safety-guard` | direct replacement |
| `ultra-delivery` | `deliver-and-retro` | direct replacement |
| `openspec-ultra-bridge-v2` | `openspec-ultra-bridge` | enhanced replacement |

## Current Scope

This tree is intended to be copied into a future repo or merged into the remote
`ultra-orchestration` repository after pilot validation.
