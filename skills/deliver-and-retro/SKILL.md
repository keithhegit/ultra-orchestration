---
name: deliver-and-retro
description: Assemble the final deliverable, orchestration log, vetter report, and concise retrospective for a completed orchestrated run. Use when implementation and review are complete and results need to be packaged clearly.
---

# Deliver And Retro

Package the run for the user and for future runs.

## Produce

- `final_deliverable`
- `orchestration_log`
- `vetter_report`
- `control_surface_used`
- short retro notes

## Rules

- Summarize what changed, what was verified, and what risks remain.
- Include approval or guardrail decisions in `vetter_report`.
- Keep retro brief and action-oriented.
- Do not bury blockers or unverified claims.
- For `STRICT` and `STRICT_OPENSPEC`, do not deliver unless run ledger,
  contract validation, review, and QA status are explicit.
- If any control surface was skipped, name it and explain why.

## control_surface_used

Include:

- `run_mode`
- `used_openspec_change`
- `used_openspec_bridge`
- `used_run_ledger`
- `used_contract_validation`
- `used_slice_dag`
- `used_dynamic_qa`
- skipped control surfaces and reasons
