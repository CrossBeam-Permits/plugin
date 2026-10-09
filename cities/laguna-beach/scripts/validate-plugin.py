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
    ".cursor-plugin/plugin.json",
    ".mcp.json",
    "gemini-extension.json",
    "CHANGELOG.md",
    "SKILL.md",
    "requirements.txt",
    "skills/laguna-permit-preparer/SKILL.md",
    "skills/laguna-permit-preparer/agents/openai.yaml",
    "assets/form-manifest.json",
    "assets/portal-maps/v2-portal-map.json",
    "assets/portal-maps/portal-snapshot.json",
    "schemas/work-class-selection.schema.json",
    "schemas/project-facts.schema.json",
    "schemas/application-set.schema.json",
    "schemas/submission-plan.schema.json",
    "schemas/submission-receipt.schema.json",
    "evals/run-evals.py",
    "scripts/plugin_root.py",
]

PLUGIN_NAME = "laguna-beach"
WRAPPER_NAME = "laguna-permit-preparer"
CROSSBEAM_MCP_URL = "https://crossbeam-mcp.old-cherry-b095.workers.dev/mcp"
MARKETPLACE_SOURCE = {
    "source": "git-subdir",
    "url": "https://github.com/CrossBeam-Permits/plugin.git",
    "path": "cities/laguna-beach",
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def frontmatter_name(text: str) -> str | None:
    """Read the top-level name: value from YAML frontmatter (mechanical parse)."""
    if not text.startswith("---\n"):
        return None
    for line in text.split("---", 2)[1].splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def find_marketplace(root: Path) -> Path | None:
    """Return the repository marketplace file when this is the source checkout.

    An installed copy (a Claude Code or Codex plugin cache, a Gemini extension
    folder, or an uploaded skill) has no repository around it.
    """
    candidate = root.parent.parent / ".claude-plugin/marketplace.json"
    if root.parent.name == "cities" and candidate.is_file():
        return candidate
    return None


def check_connector(root: Path, codex_manifest: dict) -> None:
    """The CrossBeam connector is declared for every host, optional, and credential-free."""
    servers = load(root / ".mcp.json").get("mcpServers")
    if not isinstance(servers, dict) or set(servers) != {"crossbeam"}:
        raise SystemExit(".mcp.json must declare exactly the crossbeam server")
    crossbeam = servers["crossbeam"]
    if crossbeam != {"type": "http", "url": CROSSBEAM_MCP_URL}:
        raise SystemExit(".mcp.json crossbeam entry must be the plain OAuth HTTP server, with no headers or tokens")
    if codex_manifest.get("mcpServers") != "./.mcp.json":
        raise SystemExit("Codex must load the connector from ./.mcp.json")
    gemini = load(root / "gemini-extension.json").get("mcpServers")
    if gemini != {"crossbeam": {"httpUrl": CROSSBEAM_MCP_URL}}:
        raise SystemExit("gemini-extension.json must declare only the crossbeam httpUrl server")
    cursor = load(root / ".cursor-plugin/plugin.json").get("mcpServers")
    if cursor != {"crossbeam": {"url": CROSSBEAM_MCP_URL}}:
        raise SystemExit(".cursor-plugin/plugin.json must declare only the crossbeam url server")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-evals", action="store_true")
    parser.add_argument(
        "--skip-claude-validation",
        action="store_true",
        help="Skip only the external Claude CLI validation; local checks still run.",
    )
    parser.add_argument(
        "--require-marketplace",
        action="store_true",
        help="Fail when the repository marketplace.json is absent (use in the source repository CI).",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    missing = [item for item in REQUIRED if not (root / item).is_file()]
    if missing:
        raise SystemExit(f"plugin is incomplete: {missing}")

    notes: list[str] = []
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    root_name = frontmatter_name(skill)
    if root_name not in (PLUGIN_NAME, WRAPPER_NAME):
        raise SystemExit(f"root SKILL.md frontmatter name is invalid: {root_name!r}")
    if root_name != PLUGIN_NAME:
        # Claude Code and Codex never load the root SKILL.md while skills/ exists,
        # so the preparer still loads once. The Agent Skills spec wants the name to
        # match the folder, which matters when the folder is uploaded as one skill.
        notes.append(
            f"root SKILL.md is named {root_name!r}; the Agent Skills spec expects "
            f"{PLUGIN_NAME!r} (its folder name)"
        )
    wrapper = (root / "skills/laguna-permit-preparer/SKILL.md").read_text(encoding="utf-8")
    if frontmatter_name(wrapper) != WRAPPER_NAME:
        raise SystemExit("the preparer wrapper must be named laguna-permit-preparer")
    for phrase in ("../../SKILL.md", "${CLAUDE_PLUGIN_ROOT}", "scripts/plugin_root.py"):
        if phrase not in wrapper:
            raise SystemExit(f"the preparer wrapper must resolve the plugin root ({phrase} missing)")

    claude_manifest = load(root / ".claude-plugin/plugin.json")
    codex_manifest = load(root / ".codex-plugin/plugin.json")
    gemini_manifest = load(root / "gemini-extension.json")
    cursor_manifest = load(root / ".cursor-plugin/plugin.json")
    manifests = {
        "Claude": claude_manifest,
        "Codex": codex_manifest,
        "Gemini": gemini_manifest,
        "Cursor": cursor_manifest,
    }
    for host, manifest in manifests.items():
        if manifest.get("name") != PLUGIN_NAME:
            raise SystemExit(f"{host} plugin name must be {PLUGIN_NAME}")
    if root.name != PLUGIN_NAME and find_marketplace(root) is not None:
        raise SystemExit(f"the plugin folder must be named {PLUGIN_NAME}")
    if cursor_manifest.get("skills") != "./skills/":
        raise SystemExit("Cursor must load skills from ./skills/")
    check_connector(root, codex_manifest)
    if codex_manifest.get("skills") != "./skills/":
        raise SystemExit("Codex must load the thin wrapper from ./skills/")
    # The city guidance and the submittal layer are ONE plugin. There is no
    # dependency to resolve; instead assert the per-scope skills actually ship
    # beside the preparer, because building-routing.md now points at them.
    if claude_manifest.get("dependencies"):
        raise SystemExit(
            "laguna-beach is a single self-contained plugin; it must not declare dependencies"
        )
    scope_skills = {path.name for path in (root / "skills").iterdir() if path.is_dir()}
    required_scopes = {"swimming-pool", "reroof", "panel-upgrade", "laguna-permit-preparer"}
    missing_scopes = sorted(required_scopes - scope_skills)
    if missing_scopes:
        raise SystemExit(f"city scope skills missing from the plugin: {missing_scopes}")
    for scope in sorted(scope_skills):
        skill_text = (root / "skills" / scope / "SKILL.md").read_text(encoding="utf-8")
        if not skill_text.startswith("---\n"):
            raise SystemExit(f"skill {scope} has no YAML frontmatter")
        frontmatter = skill_text.split("---", 2)[1].splitlines()
        allowed_keys = {"name", "description", "license", "metadata", "allowed-tools"}
        top_keys = {line.split(":", 1)[0] for line in frontmatter
                    if line and not line[0].isspace() and not line.startswith("#")}
        unexpected = sorted(top_keys - allowed_keys)
        if unexpected:
            raise SystemExit(f"skill {scope} has unsupported top-level metadata: {unexpected}; nest it under metadata")
        if frontmatter_name(skill_text) != scope:
            raise SystemExit(f"skill {scope} needs its canonical name for Codex discovery")

    if len(scope_skills) < 23:
        raise SystemExit(f"expected 22 city skills plus the preparer, found {len(scope_skills)}")

    versions = {host: manifest.get("version") for host, manifest in manifests.items()}
    marketplace_path = find_marketplace(root)
    if marketplace_path is None:
        if args.require_marketplace:
            raise SystemExit("repository marketplace.json not found; run from the source checkout")
        notes.append(
            "marketplace checks skipped: no repository .claude-plugin/marketplace.json "
            "(normal for an installed copy)"
        )
    else:
        marketplace = load(marketplace_path)
        entries = {item["name"]: item for item in marketplace["plugins"]}
        if PLUGIN_NAME not in entries:
            raise SystemExit(f"marketplace entry is missing: {PLUGIN_NAME}")
        versions["marketplace"] = entries[PLUGIN_NAME].get("version")
        city_source = dict(entries[PLUGIN_NAME]["source"])
        # A release may pin the entry with ref and/or sha; the rest must not change.
        pins = {key: city_source.pop(key) for key in ("ref", "sha") if key in city_source}
        if city_source != MARKETPLACE_SOURCE:
            raise SystemExit("the city plugin must use the sparse git-subdir marketplace source")
        if "sha" in pins and not (len(pins["sha"]) == 40 and all(c in "0123456789abcdef" for c in pins["sha"])):
            raise SystemExit("a marketplace sha pin must be a full 40-character lowercase commit SHA")
    if len(set(versions.values())) != 1:
        raise SystemExit(f"Laguna manifest versions must agree: {versions}")
    version = claude_manifest["version"]
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {version}" not in changelog:
        raise SystemExit(f"CHANGELOG.md has no section for {version}")

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

    for note in notes:
        print(f"NOTE: {note}")
    print(f"PASS Laguna Beach plugin {version} validation (no ZIP or bundled City PDFs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
