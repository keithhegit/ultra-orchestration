# Mapping Reference

## Core model

Use OpenSpec for long-lived spec assets and Ultra-Orchestrator for execution control.

## Change to TaskManifest

- `change-id` -> `TaskManifest.id`
- proposal summary -> `goal`
- design constraints -> `constraints`
- tasks dependencies -> `dependencies`
- affected areas -> `owned_paths`
- acceptance criteria / spec delta checks -> `success_criteria`

## Task to WorkPackage

- task item -> `scope`
- role hint -> `role`
- affected files -> `owned_paths`
- validation checklist -> `acceptance_checks`

## AgentResult back to OpenSpec

- `evidence` -> completion proof
- `risks` -> follow-up design/task notes
- `failure_context` -> task/design corrections
- `followups` -> future changes or archive caveats
