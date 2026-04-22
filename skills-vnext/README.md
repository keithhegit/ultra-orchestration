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
- `openspec-ultra-bridge-v2`
  map OpenSpec change assets into Ultra execution artifacts

## Current Scope

This tree is intended to be copied into a future repo or merged into the remote
`ultra-orchestration` repository after pilot validation.
