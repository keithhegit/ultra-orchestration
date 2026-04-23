# Work Package Examples

## Example 1: Multi-File Feature

Task:

- add workspace-level model defaults to settings UI

Good plan shape:

- `TaskManifest`
  - goal: add editable workspace defaults
  - success criteria: value persists, UI shows current value, validation is explicit
  - owned paths: settings UI, config store, shared types
- `WorkPackage 1`
  - role: planner or worker
  - scope: shared type and config store changes
  - owned paths: `src/config/*`, `src/types/*`
- `WorkPackage 2`
  - role: worker
  - scope: settings UI
  - owned paths: `src/ui/settings/*`
- serial note
  - UI package depends on shared type package

## Example 2: OpenSpec Change

Task:

- implement the first slice of `workspace-model-defaults`

Good route:

1. `openspec-ultra-bridge-v2` reads proposal, design, tasks, and bridge assets
2. `ultra-planning` turns that into `TaskManifest` and `WorkPackage` items
3. planning marks:
   - current slice
   - owned paths for the slice
   - review target
   - QA scenario target

Good output:

- one execution-ready `TaskManifest`
- one or more `WorkPackage` items for the current slice only
- explicit note if later slices depend on this one
