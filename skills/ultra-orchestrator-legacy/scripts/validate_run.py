#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {"final_deliverable", "orchestration_log", "vetter_report"}
REQUIRED_LEDGER = {
    "run_id",
    "current_stage",
    "task_status",
    "dependencies_satisfied",
    "retry_counts",
    "max_retries",
    "active_write_locks",
    "blockers",
    "pending_review",
    "integration_status",
}


def validate_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Ultra-Orchestrator run artifacts.")
    parser.add_argument("run_dir", help="Directory containing ledger.json and run-output.json")
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    ledger = validate_json(run_dir / "ledger.json")
    output = validate_json(run_dir / "run-output.json")

    missing_ledger = sorted(REQUIRED_LEDGER - set(ledger))
    missing_output = sorted(REQUIRED_TOP_LEVEL - set(output))

    if missing_ledger or missing_output:
        if missing_ledger:
            print("Missing ledger keys:", ", ".join(missing_ledger))
        if missing_output:
            print("Missing run-output keys:", ", ".join(missing_output))
        return 1

    if output["vetter_report"].get("risk_level") not in {"LOW", "MEDIUM", "HIGH", "EXTREME"}:
        print("Invalid risk level in vetter_report")
        return 1

    print("Run artifacts are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
