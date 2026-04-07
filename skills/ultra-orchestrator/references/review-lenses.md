# Review Lenses

Use only the lenses needed to reduce real risk. Avoid ceremony.

## Specification consistency

- Does the result satisfy the stated goal?
- Are acceptance checks actually met?
- Did the worker stay inside owned paths and non-goals?
- Are any hidden assumptions unresolved?

## Engineering quality

- Falsification: What would make this result wrong?
- Evidence quality: What concrete evidence supports the claim?
- Constraints compliance: Did we honor environment, policy, and deadline limits?
- Downside risk: What can fail in production?
- Bias or blind spots: What did we not test or inspect?

## Review outcome

Choose one:

- `approved`
- `approved_with_followups`
- `rework_required`
