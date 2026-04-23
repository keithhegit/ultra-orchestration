---
name: ultra-delivery
description: Final delivery packaging for Codex Ultra vNext. Use after review and QA to assemble the final deliverable, orchestration log, vetter report, validation evidence, residual risks, and retro notes so the user can understand what changed, why it changed, how it was verified, and what remains.
---

# Ultra Delivery

Package the run into an auditable user-facing result. This skill is the vNext
replacement for the stable `deliver-and-retro` skill.

## Delivery Gate

Do not deliver until:

- accepted work packages are reviewed
- QA status is explicit
- risk decisions are recorded
- evidence exists for every major claim
- unresolved risks are named

If evidence is missing, route back to `ultra-review` or `ultra-qa`.

## Required Run Output

Every delivery must include:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`

Recommended additions:

- `qa_summary`
- `changed_paths`
- `verification_evidence`
- `residual_risks`
- `followups`
- `retro`

## Final Response Standard

Keep the user-facing final response concise, but do not hide risk.

Mention:

- what was completed
- where the important artifacts live
- what verification passed
- what was not verified
- what remains as follow-up

## Retro

Retro improves the next run and should not block delivery unless it reveals a
missing review, QA, or risk gate.

Capture:

- which decomposition worked
- which guardrails helped
- which handoff was noisy or oversized
- which contract field should be tightened
- whether the vNext skill sequence should change next time

Read [delivery-checklist](references/delivery-checklist.md) for the final gate.
