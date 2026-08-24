#!/usr/bin/env python3
"""Validate the Laguna plugin in place without creating a distributable archive."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


REQUIRED = [
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "SKILL.md",
    "requirements.txt",
    "skills/laguna-permit-preparer/SKILL.md",
    "skills/laguna-permit-preparer/agents/openai.yaml",
    "assets/form-manifest.json",
    "assets/portal-maps/v1-portal-map.json",
    "schemas/project-facts.schema.json",
    "schemas/application-set.schema.json",
    "schemas/submission-plan.schema.json",
    "schemas/submission-receipt.schema.json",
    "evals/run-evals.py",
]


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-evals", action="store_true")
    parser.add_argument(
        "--skip-claude-validation",
        action="store_true",
        help="Skip only the external Claude CLI validation; local checks still run.",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    repository_root = root.parent.parent
    missing = [item for item in REQUIRED if not (root / item).is_file()]
    if missing:
        raise SystemExit(f"plugin is incomplete: {missing}")

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    if "name: laguna-permit-preparer" not in skill:
        raise SystemExit("SKILL.md frontmatter name is invalid")
    wrapper = (root / "skills/laguna-permit-preparer/SKILL.md").read_text(encoding="utf-8")
    if "../../SKILL.md" not in wrapper:
        raise SystemExit("the cross-runtime skill wrapper must load the canonical root SKILL.md")

    claude_manifest = load(root / ".claude-plugin/plugin.json")
    codex_manifest = load(root / ".codex-plugin/plugin.json")
    if claude_manifest["name"] != "laguna-beach-submit":
        raise SystemExit("Claude plugin name must be laguna-beach-submit")
    if codex_manifest["name"] != claude_manifest["name"]:
        raise SystemExit("Claude and Codex plugin names differ")
    if codex_manifest.get("skills") != "./skills/":
        raise SystemExit("Codex must load the thin wrapper from ./skills/")
    dependencies = {
        item if isinstance(item, str) else item["name"]
        for item in claude_manifest.get("dependencies", [])
    }
    if "laguna-beach" not in dependencies:
        raise SystemExit("the Laguna city plugin dependency is missing")

    marketplace = load(repository_root / ".claude-plugin/marketplace.json")
    entries = {item["name"]: item for item in marketplace["plugins"]}
    for name in ("laguna-beach", "laguna-beach-submit"):
        if name not in entries:
            raise SystemExit(f"marketplace entry is missing: {name}")
    submit_source = entries["laguna-beach-submit"]["source"]
    if submit_source != {
        "source": "git-subdir",
        "url": "https://github.com/CrossBeam-Permits/plugin.git",
        "path": "submit/laguna-beach",
    }:
        raise SystemExit("submit plugin must use the sparse git-subdir marketplace source")

    binary_pdfs = sorted(root.rglob("*.pdf")) + sorted(root.rglob("*.PDF"))
    archives = sorted(root.rglob("*.zip"))
    if binary_pdfs or archives:
        raise SystemExit(f"fetch-only plugin contains binary forms/archives: {binary_pdfs + archives}")
    unsafe_names = [
        path
        for path in root.rglob("*")
        if path.is_file()
        and any(
            word in path.name.lower()
            for word in ("password", "cookie", "session-token", "payment-card")
        )
    ]
    if unsafe_names:
        raise SystemExit(f"unsafe files in plugin: {unsafe_names}")

    if not args.skip_evals:
        subprocess.run(
            [sys.executable, str(root / "evals/run-evals.py")],
            cwd=root,
            check=True,
        )

    if not args.skip_claude_validation:
        executable = shutil.which("claude")
        if executable is None:
            raise SystemExit("Claude CLI is unavailable; use --skip-claude-validation only in a constrained host")
        subprocess.run([executable, "plugin", "validate", str(root), "--strict"], check=True)

    print("PASS Laguna submit plugin validation (no ZIP or bundled City PDFs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
