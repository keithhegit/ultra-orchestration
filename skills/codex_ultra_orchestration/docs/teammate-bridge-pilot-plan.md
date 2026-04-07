# /teammate Bridge Pilot Plan

This note records how `/teammate` should be used to validate the OpenSpec and Ultra-Orchestrator bridge.

## Goal

Use `/teammate` as a real-world acceptance project for the bridge.

## Why `/teammate` is a reasonable pilot

- It is a non-trivial codebase.
- It gives enough surface area for feature work and bug fixing.
- It is large enough to test spec-first decomposition and review/QA loopbacks.

## Pilot rules

- Start with one OpenSpec change per run.
- Prefer one worktree per change when parallel work begins.
- Use OpenSpec to define proposal, design, and tasks.
- Use Ultra to control dispatch, review, QA, and final delivery.

## Initial acceptance threshold

The bridge is acceptable for broader use only if:

- one feature task succeeds
- one bug-fix task succeeds
- one task demonstrates loopback and recovery
- archive remains gated by review and QA outcome

## What success looks like

- Better planning input quality than raw natural-language requests
- Cleaner `TaskManifest` and `WorkPackage` generation
- More reliable review and QA feedback loops
- No loss of control in Ultra's state machine
