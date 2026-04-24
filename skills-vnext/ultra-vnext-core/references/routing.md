# Routing Reference

`ultra-vnext-core` is a compatibility alias for the mainline
`ultra-orchestrator` strict protocol.

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

## Run Mode Priority

Use the strictest appropriate mode:

1. `STRICT_OPENSPEC`
2. `STRICT`
3. `STANDARD`
4. `LIGHT`

Development work defaults to `STRICT_OPENSPEC`. Downgrade only when the user
explicitly asks for lightweight execution or the environment makes OpenSpec
impossible. Record the downgrade reason.

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
