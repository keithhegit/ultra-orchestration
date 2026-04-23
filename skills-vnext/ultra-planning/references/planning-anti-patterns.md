# Planning Anti-Patterns

## Bad Plan Signals

- the plan says "implement as needed" without file ownership
- acceptance checks are vague, such as "works correctly"
- several packages can write to the same path without a lock decision
- review is expected to infer intent from chat history
- QA has no scenario list
- a worker must make architecture decisions during implementation

## Example: Too-Broad Owned Paths

Bad:

- `owned_paths: src/`

Better:

- `owned_paths: src/runtime/summary.ts`
- `owned_paths: src/renderer/panels/runtime-panel.tsx`

## Example: Weak Acceptance Checks

Bad:

- "state should work"

Better:

- "bootstrap response includes runtime summary"
- "renderer can show current phase without parsing chat prose"

## Example: Unsafe Parallelism

Bad:

- two packages both write `src/runtime/summary.ts`

Better:

- either merge them into one package
- or serialize them with an explicit dependency
