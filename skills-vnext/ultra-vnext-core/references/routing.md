# Routing Reference

`ultra-vnext-core` is the only required startup skill for vNext. It should load
other vNext skills only when the task needs them.

## Minimal Startup Forms

```text
$ultra-vnext-core Build a settings page for workspace-level model defaults.
```

```text
$ultra-vnext-core OpenSpec change workspace-model-defaults: implement the first slice.
```

```text
$ultra-vnext-core bugfix: command execution hangs after approval is granted.
```

## Route Examples

### New Feature

Use:

1. `ultra-brainstorming`
2. `ultra-planning`
3. `ultra-risk-vetting`
4. `ultra-execution-control`
5. `ultra-review`
6. `ultra-qa`
7. `ultra-delivery`

Skip `ultra-brainstorming` only when success criteria and constraints are
already explicit.

Planning is still mandatory before controlled dispatch.

### OpenSpec Change

Use:

1. `openspec-ultra-bridge-v2`
2. `ultra-planning`
3. `ultra-risk-vetting`
4. `ultra-execution-control`
5. `ultra-review`
6. `ultra-qa`
7. `ultra-delivery`

OpenSpec owns the durable spec. Ultra owns execution control.

Bridge output must still pass through `ultra-planning` before dispatch.

### Bug Fix

Use:

1. `ultra-planning`
2. `ultra-risk-vetting`
3. `ultra-execution-control`
4. `ultra-review`
5. `ultra-qa`
6. `ultra-delivery`

The plan must include regression surface and verification intent before edits.

## Planning Gate

`ultra-planning` is the second hard gate after task classification.

Do not move from routing into controlled execution until planning has produced:

- one `TaskManifest`
- one or more `WorkPackage` items
- owned paths
- acceptance checks
- risk and retry assumptions
- serial or parallel execution notes

If planning cannot produce those outputs, route back to brainstorming or bridge
preparation instead of improvising during implementation.

## Routing Principles

- Prefer the shortest safe route.
- Do not ask the user to enumerate subskills.
- Do not load every sibling skill by default.
- Add risk vetting before execution whenever scope or impact is uncertain.
- End with delivery when the user needs a durable result.
