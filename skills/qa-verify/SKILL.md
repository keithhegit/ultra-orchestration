---
name: qa-verify
description: Run scenario-based verification and regression checks for changed behavior, user flows, and bug fixes before delivery. Use after implementation or review whenever behavior changed or user-visible quality matters.
---

# QA Verify

Validate behavior, not just code shape.

Treat QA as two-mode verification:

- Static baseline: reason over code, diffs, existing tests, and available evidence
- Dynamic verification: run tests or commands when the host environment allows it

Do not assume browser automation exists unless the environment explicitly provides it.

## Check

- Happy path
- Error path
- Regression risk
- User-visible behavior
- Follow-up tests that should exist even if they are not added now

## Failure handling

- If behavior is wrong but the plan is still valid, send the work back to `Execute`.
- If QA reveals a deeper architecture or requirement flaw, send the work back to `Plan`.

## Output

Return:

- scenarios exercised
- evidence collected
- pass or fail status
- residual risks
