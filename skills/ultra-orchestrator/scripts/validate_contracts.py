#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = {
    "taskmanifest": [
        "id",
        "goal",
        "context",
        "success_criteria",
        "constraints",
        "owned_paths",
        "dependencies",
        "expected_outputs",
        "risk_level",
        "non_goals",
    ],
    "workpackage": [
        "task_id",
        "role",
        "scope",
        "owned_paths",
        "input_artifacts",
        "acceptance_checks",
        "report_format",
    ],
    "agentresult": [
        "task_id",
        "status",
        "summary",
        "changed_paths",
        "artifacts",
        "evidence",
        "risks",
        "followups",
    ],
    "executionledger": [
        "run_id",
        "run_mode",
        "phase",
        "status",
        "created_at",
        "updated_at",
        "tasks",
        "blockers",
        "review_queue",
        "qa_queue",
        "integration",
    ],
    "runoutput": [
        "final_deliverable",
        "orchestration_log",
        "vetter_report",
        "control_surface_used",
    ],
    "controlsurfaceused": [
        "run_mode",
        "used_openspec_change",
        "used_openspec_bridge",
        "used_run_ledger",
        "used_contract_validation",
        "used_slice_dag",
        "used_dynamic_qa",
        "skipped_control_surfaces",
    ],
}


def infer_kind(path: Path) -> str | None:
    name = path.stem.lower().replace("-", "").replace("_", "")
    for kind in REQUIRED_FIELDS:
        if kind in name:
            return kind
    if name == "ledger":
        return "executionledger"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Ultra vNext JSON artifacts.")
    parser.add_argument("artifact", help="Path to a JSON artifact")
    parser.add_argument(
        "--kind",
        choices=sorted(REQUIRED_FIELDS),
        help="Explicit artifact kind if it cannot be inferred",
    )
    args = parser.parse_args()

    artifact = Path(args.artifact).expanduser().resolve()
    kind = args.kind or infer_kind(artifact)
    if not kind:
        raise SystemExit("Could not infer artifact kind; pass --kind explicitly.")

    payload = json.loads(artifact.read_text(encoding="utf-8"))
    missing = [field for field in REQUIRED_FIELDS[kind] if field not in payload]

    if missing:
        raise SystemExit(
            f"{artifact.name} failed {kind} validation. Missing fields: {', '.join(missing)}"
        )

    print(f"{artifact.name}: OK ({kind})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
