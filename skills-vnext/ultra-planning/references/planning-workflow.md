# Planning Workflow

## Rigid Sequence

1. read the intake, design, or bridge artifact
2. confirm that success criteria and constraints exist
3. return to brainstorming if the request is still under-specified
4. define the `TaskManifest`
5. split work into `WorkPackage` items
6. assign dependencies and owned paths
7. mark parallel-safe versus serial work
8. attach acceptance checks, risk, and retry assumptions
9. run planning self-review
10. return the decision-complete package set

## Why This Gate Exists

Planning protects execution from:

- hidden scope expansion
- overlapping writes
- vague acceptance checks
- reviewer and QA ambiguity
- implementers inventing missing decisions

## Output Order

Return:

1. `TaskManifest`
2. `WorkPackage` list
3. serial or parallel notes
4. assumptions
5. blockers
6. re-plan triggers
