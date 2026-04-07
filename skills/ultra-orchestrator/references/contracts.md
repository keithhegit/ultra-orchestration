# Contracts

Use these canonical shapes across all sibling skills.

## TaskManifest

```json
{
  "id": "task-001",
  "goal": "Ship a user-visible feature or fix",
  "context": ["Relevant repo facts or prior artifacts"],
  "success_criteria": ["Observable outcomes"],
  "constraints": ["Deadlines, policies, environment limits"],
  "owned_paths": ["src/features/payments"],
  "dependencies": ["task-000"],
  "expected_outputs": ["code changes", "tests", "notes"],
  "risk_level": "MEDIUM",
  "max_retries": 1,
  "non_goals": ["Out-of-scope changes"]
}
```

## WorkPackage

```json
{
  "task_id": "task-001",
  "role": "Worker",
  "scope": "Implement invoice retry UI state",
  "owned_paths": ["src/features/invoices"],
  "input_artifacts": ["plan.md", "task-manifest.json"],
  "acceptance_checks": ["Loading, success, error states render"],
  "context_bundle": ["task-manifest.json", "relevant-file-pointers.txt"],
  "report_format": "AgentResult"
}
```

## AgentResult

```json
{
  "task_id": "task-001",
  "status": "done",
  "summary": "Implemented retry button state handling",
  "changed_paths": ["src/features/invoices/RetryButton.tsx"],
  "artifacts": ["test-results.txt"],
  "evidence": ["unit tests pass", "manual state walkthrough"],
  "risks": ["No browser verification yet"],
  "failure_context": [],
  "followups": ["Add visual regression coverage"]
}
```

## ExecutionLedger

```json
{
  "run_id": "run-20260325-001",
  "current_stage": "review",
  "task_status": {
    "task-001": "review"
  },
  "dependencies_satisfied": {
    "task-001": true
  },
  "retry_counts": {
    "task-001": 0
  },
  "max_retries": {
    "task-001": 1
  },
  "active_write_locks": {
    "src/features/invoices": "task-001"
  },
  "blockers": [],
  "pending_review": ["task-001"],
  "integration_status": "waiting"
}
```

## RunOutput

```json
{
  "final_deliverable": {
    "summary": "Short user-facing summary",
    "artifacts": []
  },
  "orchestration_log": [
    {
      "stage": "plan",
      "task": "task-001",
      "owner": "Planner",
      "status": "done",
      "notes": "Task graph prepared"
    }
  ],
  "vetter_report": {
    "checked_items": [],
    "risk_level": "LOW",
    "decisions": []
  }
}
```
