---
name: ultra-qa
description: Scenario-based QA for Codex Ultra vNext. Use after implementation or review whenever behavior changed, a bug was fixed, a user flow was introduced, or delivery quality depends on proving happy path, error path, regression, and user-visible outcomes through static reasoning or dynamic execution when available.
---

# Ultra QA

QA validates behavior, not just code shape.

## Two Modes

- static mode: inspect code, diffs, tests, and artifacts when execution is not
  possible
- dynamic mode: run commands or tests when the environment allows it

Do not pretend dynamic evidence exists when it does not.

## Scenario Set

Cover at least:

- happy path
- error path
- regression risk
- user-visible behavior
- missing tests that should exist later

## Failure Routing

- send failures to `Execute` when the plan remains valid
- send failures to `Plan` when QA exposes a deeper requirement or architecture
  flaw

## Output

Return:

- scenarios exercised
- static evidence
- dynamic evidence, if any
- pass or fail
- residual risks
- reroute recommendation when failed

Read [qa-modes](references/qa-modes.md) before running verification.
