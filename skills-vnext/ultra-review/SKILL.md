---
name: ultra-review
description: Spec and engineering review for Codex Ultra vNext. Use after planning or implementation to check specification fidelity, evidence quality, constraints compliance, regression risk, and whether work should be accepted, rejected back to execution, or escalated back to planning.
---

# Ultra Review

Review is the gate between execution and trust.

## Review Order

1. Review against the spec and acceptance checks.
2. Review for engineering quality, risk, and regressions.
3. Decide whether the result is:
   - accepted
   - rejected to `Execute`
   - rerouted to `Plan`

## Review Lenses

Always inspect through these lenses:

- falsification: what would prove this wrong
- evidence quality: what concrete evidence supports the claim
- constraints compliance: what requirements were violated or skipped
- downside risk: what could break if this lands
- blind spots: what the worker may have missed

## Output

Return:

- decision
- findings
- evidence reviewed
- missing evidence
- reroute target if rejected
- residual risks if accepted

Do not let unsupported conclusions pass into integration.

Read [review-lenses](references/review-lenses.md) for the full checklist.
