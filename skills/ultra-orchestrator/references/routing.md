# Routing Reference

`ultra-orchestrator` is the default public entry point. `ultra-vnext-core`
remains a compatibility alias for the same strict protocol.

## Minimal Startup Forms

```text
$ultra-orchestrator Build a settings page for workspace-level model defaults.
```

```text
$ultra-orchestrator OpenSpec change workspace-model-defaults: implement the first slice.
```

```text
$ultra-orchestrator bugfix: command execution hangs after approval is granted.
```

## Run Mode Priority

Use the strictest appropriate mode:

1. `STRICT_OPENSPEC`
2. `STRICT`
3. `STANDARD`
4. `LIGHT`

Development work defaults to `STRICT_OPENSPEC`. Downgrade only when the user
explicitly asks for lightweight execution or the environment makes OpenSpec
impossible. Record the downgrade reason.

## Route Examples

### Development Or Bugfix

Default:

1. choose `STRICT_OPENSPEC`
2. create or select one OpenSpec change
3. bridge the change into Ultra artifacts
4. plan one bounded slice
5. risk vet
6. dispatch with ledger and write locks
7. review
8. QA
9. deliver with `control_surface_used`

### Existing OpenSpec Change

Use:

1. `openspec-ultra-bridge`
2. `decision-complete-planner`
3. `risk-vetter`
4. `dispatch-and-track`
5. `spec-review` and `code-review`
6. `qa-verify`
7. `deliver-and-retro`

Bridge output must still pass through planning before dispatch.

### Review Or QA Only

Use `LIGHT`:

1. review or QA skill
2. delivery
3. record skipped control surfaces and reasons

## Strict Gate

Do not move into controlled execution in `STRICT` or `STRICT_OPENSPEC` until
the run has:

- initialized run directory and `ledger.json`
- one JSON `TaskManifest`
- one or more JSON `WorkPackage` items
- owned paths
- acceptance checks
- risk and retry assumptions
- serial or parallel execution notes
- contract validation plan

If those outputs cannot be produced, stop with a blocker rather than
improvising during implementation.
