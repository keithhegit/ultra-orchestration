#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_LEDGER = {
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
}

REQUIRED_OUTPUT = {
    "final_deliverable",
    "orchestration_log",
    "vetter_report",
    "control_surface_used",
}

REQUIRED_CONTROL = {
    "run_mode",
    "used_openspec_change",
    "used_openspec_bridge",
    "used_run_ledger",
    "used_contract_validation",
    "used_slice_dag",
    "used_dynamic_qa",
    "skipped_control_surfaces",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def missing(required: set[str], payload: dict) -> list[str]:
    return sorted(required - set(payload))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Ultra run directory.")
    parser.add_argument("run_dir", help="Directory containing ledger.json and run-output.json")
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    ledger = read_json(run_dir / "ledger.json")
    output = read_json(run_dir / "run-output.json")
    control = output.get("control_surface_used", {})

    problems = []
    for label, required, payload in [
        ("ledger", REQUIRED_LEDGER, ledger),
        ("run-output", REQUIRED_OUTPUT, output),
        ("control_surface_used", REQUIRED_CONTROL, control),
    ]:
        fields = missing(required, payload)
        if fields:
            problems.append(f"{label} missing: {', '.join(fields)}")

    if ledger.get("run_mode") not in {"LIGHT", "STANDARD", "STRICT", "STRICT_OPENSPEC"}:
        problems.append("ledger run_mode is invalid")

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("Run artifacts are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
