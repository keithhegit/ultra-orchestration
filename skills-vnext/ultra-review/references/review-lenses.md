# Review Lenses

## Specification Fidelity

- does the result match the acceptance checks
- did the worker solve the right problem

## Evidence Quality

- are claims backed by code, tests, logs, or concrete diffs
- is any important conclusion unsupported

## Risk

- what can regress
- what remains untested
- what hidden assumptions are still in play

## Reroute Decision

- reject to `Execute` for implementation faults
- reroute to `Plan` for requirement or architecture faults
