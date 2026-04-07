# Teammate Pilot Acceptance

Use this reference when validating the bridge on `/teammate`.

## Objective

Prove that OpenSpec can improve upstream spec quality without weakening Ultra-Orchestrator's execution control.

## Recommended pilot set

Run at least these three tasks:

1. One multi-file feature task
2. One bug-fix task
3. One task that triggers a real review or QA loopback

## Acceptance criteria

### A. Boundary stability

- OpenSpec remains the spec source-of-truth.
- Ultra remains the orchestration source-of-truth.
- The bridge does not become a third orchestration system.

### B. Mapping stability

- The same change maps to similar `TaskManifest` and `WorkPackage` structure across repeated runs.
- `change-id <-> task-id` remains traceable.
- Acceptance checks stay attached to the correct work package.

### C. Feedback stability

- Review findings can be translated back into OpenSpec task or design refinement suggestions.
- QA findings can be translated back into failure-context or archive-blocking reasons.
- Feedback is specific enough to act on.

### D. Loopback stability

At least one pilot should demonstrate a successful loopback:

- review -> apply
or
- QA -> apply
or
- QA -> ff/new

### E. Archive discipline

- Archive is blocked when review or QA is incomplete.
- Archive is allowed only when the change intent and execution outcome still match.

## Signs the bridge is not stable yet

- Mapping needs manual reinterpretation every run.
- Review and QA results cannot be fed back into spec assets cleanly.
- Archive decisions depend on chat memory instead of artifacts.
- The bridge starts redefining Ultra core stages or ownership.

## Exit condition

Treat the bridge as stable enough for wider use only after three real pilot tasks complete without redefining the mapping rules each time.
