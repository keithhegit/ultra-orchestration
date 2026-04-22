# Bridge Pattern

## Principle

OpenSpec is the specification memory.
Ultra is the execution memory and control plane.

## Recommended Flow

1. create or refine an OpenSpec change
2. ensure `proposal.md`, `design.md`, and `tasks.md` agree
3. optionally add `ultra-bridge.md` for explicit execution mapping
4. materialize `TaskManifest` and `WorkPackage` outputs
5. run Ultra planning, review, QA, and delivery
6. archive the change only after the execution loop is complete

## Why This Split Works

- long-lived specs stop living only in chat history
- execution remains disciplined and auditable
- review and QA do not disappear behind spec generation
