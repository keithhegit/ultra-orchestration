# Core Contracts

## TaskManifest

Required fields:

- `id`
- `goal`
- `context`
- `success_criteria`
- `constraints`
- `owned_paths`
- `dependencies`
- `expected_outputs`
- `risk_level`
- `non_goals`

Optional but recommended:

- `run_mode`
- `change_id`
- `slice_status`
- `next_slice`
- `parallel_groups`
- `assumptions`
- `review_targets`

## WorkPackage

Required fields:

- `task_id`
- `role`
- `scope`
- `owned_paths`
- `input_artifacts`
- `acceptance_checks`
- `report_format`

Recommended:

- `dependencies`
- `retry_budget`
- `risk_level`
- `freeze_paths`
- `slice`

## AgentResult

Required fields:

- `task_id`
- `status`
- `summary`
- `changed_paths`
- `artifacts`
- `evidence`
- `risks`
- `followups`

## ExecutionLedger

Suggested top-level structure:

- `run_id`
- `run_mode`
- `phase`
- `status`
- `created_at`
- `updated_at`
- `tasks`
- `blockers`
- `review_queue`
- `qa_queue`
- `integration`

## RunOutput

Required top-level fields:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`
- `control_surface_used`

## ControlSurfaceUsed

Required fields:

- `run_mode`
- `used_openspec_change`
- `used_openspec_bridge`
- `used_run_ledger`
- `used_contract_validation`
- `used_slice_dag`
- `used_dynamic_qa`
- `skipped_control_surfaces`
