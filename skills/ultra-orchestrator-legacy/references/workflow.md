# Workflow

## Intake

- Normalize `task_description`, `context`, `success_criteria`, and `constraints`.
- Classify the task: question, plan, small edit, multi-file implementation, debugging, review, or release prep.
- Decide whether external tools or skills are needed.

## Plan

- Create a decision-complete plan.
- Convert work into explicit work packages.
- Mark dependencies and identify any shared write scope.

## Dispatch

- Assign work by role.
- Include owned paths and acceptance checks.
- Update the ledger before execution starts.
- Only parallelize when dependencies are satisfied and write locks do not conflict.

## Execute

- Run independent packages in parallel.
- Keep dependent or overlapping packages serialized.
- Retry only transient failures, and only once.
- When execution fails review, loop back with concrete failure context.

## Review

- Verify the result against the plan first.
- Then review for bugs, regressions, evidence quality, and missing tests.
- Reject work back to Execute when the implementation is wrong.

## QA

- Validate user-visible flows or changed behavior.
- For fixes, require regression thinking even when full tests are not possible.
- Use static analysis by default and dynamic execution when the host environment allows it.
- Return work to Execute or Plan when QA reveals real failures.

## Deliver

- Produce `final_deliverable`, `orchestration_log`, and `vetter_report`.
- Summarize remaining risks and next actions.

## Retro

- Capture which orchestration choices helped.
- Capture one or two improvements for the next run.
