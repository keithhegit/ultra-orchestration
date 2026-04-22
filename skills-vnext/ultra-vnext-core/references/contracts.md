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
