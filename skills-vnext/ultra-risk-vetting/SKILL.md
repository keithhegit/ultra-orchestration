---
name: ultra-risk-vetting
description: Risk classification and approval gating for Codex Ultra vNext. Use before external tools, unfamiliar skills, destructive commands, broad write scopes, credential access, network operations, repository publishing, or any action where safety, reversibility, user approval, or audit evidence matters.
---

# Ultra Risk Vetting

Classify risk before execution. This skill is the vNext replacement for the
stable `risk-vetter` skill and absorbs the approval-facing part of
`safety-guard`.

## Risk Levels

Use four levels:

- `LOW`
  safe, local, reversible, narrow-scope work
- `MEDIUM`
  normal engineering work with bounded writes or commands
- `HIGH`
  broad writes, destructive operations, publishing, credentials, or external
  systems
- `EXTREME`
  irreversible, secret-exposing, production-impacting, legal, financial, or
  security-sensitive actions

## Gate Rules

- `LOW`: proceed and log briefly
- `MEDIUM`: proceed with guardrails and evidence capture
- `HIGH`: stop for explicit user approval unless the user already gave concrete
  approval for the exact action
- `EXTREME`: block by default and ask for explicit approval plus scope
  confirmation

## Vetting Checklist

Before execution, inspect:

- reversibility
- write scope
- command destructiveness
- external network or system effects
- credential or secret exposure
- production or user data impact
- whether the action changes published state
- whether the action can be safely retried

## Output

Return a `VetterDecision`:

- `risk_level`
- `decision`
- `required_guardrails`
- `approval_required`
- `evidence_to_capture`
- `reasoning_summary`
- `residual_risk`

Record the decision in `vetter_report` and hand required guardrails to
`ultra-execution-control`.

Read [risk-policy](references/risk-policy.md) for examples and thresholds.
