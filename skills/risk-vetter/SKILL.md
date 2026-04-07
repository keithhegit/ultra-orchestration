---
name: risk-vetter
description: Classify tools, skills, commands, and external actions by risk level and define required approvals or guardrails before execution. Use whenever a run may invoke unfamiliar tooling, destructive actions, broad write scope, or external systems.
---

# Risk Vetter

Classify execution risk before the orchestrator crosses a safety boundary.

## Risk levels

- `LOW`
- `MEDIUM`
- `HIGH`
- `EXTREME`

## Evaluate

- Destructiveness
- Breadth of write scope
- External system impact
- Reversibility
- Availability of verification

## Output

Return:

- `risk_level`
- `checked_items`
- `decisions`
- `required_guardrails`
- `approval_needed`
