#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def first_heading(text: str, default: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return default


def bullet_lines(text: str) -> list[str]:
    return [
        line[2:].strip()
        for line in text.splitlines()
        if line.startswith("- ") and line[2:].strip()
    ]


def fenced_blocks(text: str) -> list[str]:
    return re.findall(r"```(?:yaml|yml|json)?\n(.*?)```", text, flags=re.S)


def build_fallback_manifest(change_id: str, proposal: str, tasks_md: str) -> dict:
    success = bullet_lines(tasks_md)[:6]
    constraints = bullet_lines(proposal)[:6]
    return {
        "id": change_id,
        "goal": first_heading(proposal, change_id),
        "context": "Generated from OpenSpec artifacts by bridge_change.py",
        "success_criteria": success or ["Fill from proposal/design/tasks manually."],
        "constraints": constraints or ["Review proposal and design for explicit constraints."],
        "owned_paths": [],
        "dependencies": [],
        "expected_outputs": ["TaskManifest", "WorkPackages"],
        "risk_level": "MEDIUM",
        "non_goals": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bridge an OpenSpec change directory into Ultra vNext artifacts."
    )
    parser.add_argument("change_dir", help="Path to openspec/changes/<change-id>")
    parser.add_argument("output_dir", help="Directory to write bridge artifacts into")
    args = parser.parse_args()

    change_dir = Path(args.change_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    change_id = change_dir.name
    proposal = read(change_dir / "proposal.md")
    design = read(change_dir / "design.md")
    tasks_md = read(change_dir / "tasks.md")
    bridge_md = read(change_dir / "ultra-bridge.md")

    manifest = None
    work_packages = []
    raw_manifest_block = None
    raw_work_package_blocks: list[str] = []

    if bridge_md:
        blocks = fenced_blocks(bridge_md)
        if blocks:
            raw_manifest_block = blocks[0].strip() + "\n"
            manifest = {"source": "ultra-bridge.md", "raw_manifest_block": blocks[0]}
            if len(blocks) > 1:
                raw_work_package_blocks = [block.strip() + "\n" for block in blocks[1:]]
                work_packages = [
                    {"source": "ultra-bridge.md", "raw_work_package_block": block}
                    for block in blocks[1:]
                ]

    if manifest is None:
        manifest = build_fallback_manifest(change_id, proposal + "\n" + design, tasks_md)

    summary = {
        "change_id": change_id,
        "change_dir": str(change_dir),
        "inputs": {
            "proposal": bool(proposal),
            "design": bool(design),
            "tasks": bool(tasks_md),
            "ultra_bridge": bool(bridge_md),
        },
        "manifest_kind": "raw-bridge-block" if "raw_manifest_block" in manifest else "fallback-json",
        "work_package_count": len(work_packages),
    }

    (output_dir / "bridge-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "task-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "work-packages.json").write_text(
        json.dumps(work_packages, indent=2) + "\n", encoding="utf-8"
    )
    if raw_manifest_block:
        (output_dir / "task-manifest.yaml").write_text(
            raw_manifest_block, encoding="utf-8"
        )
    if raw_work_package_blocks:
        yaml_blob = "\n---\n".join(raw_work_package_blocks)
        (output_dir / "work-packages.yaml").write_text(
            yaml_blob, encoding="utf-8"
        )

    print(str(output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
