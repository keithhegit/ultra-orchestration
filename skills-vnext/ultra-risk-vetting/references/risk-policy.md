# Risk Policy

## LOW Examples

- reading local files
- inspecting git status
- running non-mutating search commands
- writing a small documented file in an approved workspace

## MEDIUM Examples

- editing several files inside approved owned paths
- running tests or build commands
- creating local run artifacts
- using scripts that only touch a declared output directory

## HIGH Examples

- deleting files
- force-pushing or publishing
- broad recursive moves
- editing outside declared ownership
- invoking external services that mutate state

## EXTREME Examples

- secret exfiltration risk
- production data mutation
- financial, legal, medical, or security-sensitive actions
- irreversible account or permission changes

## Guardrail Mapping

- `careful`: warn and confirm before dangerous commands
- `freeze`: restrict writes to approved paths
- `guard`: combine careful and freeze

When in doubt, escalate one level instead of silently accepting risk.
