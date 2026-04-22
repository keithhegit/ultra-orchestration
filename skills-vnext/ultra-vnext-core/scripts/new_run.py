#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_PHASES = [
    "Intake",
    "Plan",
    "Dispatch",
    "Execute",
    "Review",
    "QA",
    "Deliver",
    "Retro",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def build_ledger(run_id: str) -> dict:
    now = utc_now()
    return {
        "run_id": run_id,
        "phase": "Intake",
        "status": "initialized",
        "created_at": now,
        "updated_at": now,
        "phases": DEFAULT_PHASES,
        "tasks": [],
        "blockers": [],
        "review_queue": [],
        "qa_queue": [],
        "integration": {
            "status": "pending",
            "accepted_results": [],
            "rejected_results": [],
        },
    }


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize a Codex Ultra vNext run directory."
    )
    parser.add_argument("run_root", help="Directory that should contain run folders")
    parser.add_argument(
        "--run-id",
        help="Explicit run id. Defaults to a UTC timestamp-based id.",
    )
    args = parser.parse_args()

    run_root = Path(args.run_root).expanduser().resolve()
    run_root.mkdir(parents=True, exist_ok=True)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("run-%Y%m%d-%H%M%S")
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    for name in ("artifacts", "manifests", "results", "logs"):
        (run_dir / name).mkdir(exist_ok=True)

    write_json(run_dir / "ledger.json", build_ledger(run_id))
    write_json(
        run_dir / "run-output.json",
        {
            "final_deliverable": None,
            "orchestration_log": [],
            "vetter_report": [],
        },
    )

    print(str(run_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
