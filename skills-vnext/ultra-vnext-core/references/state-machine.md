# Ultra vNext State Machine

## Primary Flow

`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`

## Allowed Loopbacks

- `Review -> Execute`
  use when implementation quality is wrong but the plan is still valid
- `QA -> Execute`
  use when behavior is wrong but the architecture still stands
- `QA -> Plan`
  use when the failure indicates a requirement or planning flaw

## Retry Policy

- default retry budget: `1`
- use a higher budget only when the task is highly deterministic
- once the retry budget is exhausted, escalate

## Escalation Packet

When blocked, surface:

- blocker summary
- evidence
- impacted package
- recommended next step
