#!/usr/bin/env python3
"""Tests for host packaging: installed-copy validation, root resolution, connector config.

Run from anywhere:
    python3 -m unittest discover -s cities/laguna-beach/evals -p "test_*.py" -v
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import _lib  # noqa: E402


def installed_copy(destination: Path) -> Path:
    """Copy the plugin the way a host cache holds it: a version folder, no repository."""
    target = destination / "plugins/cache/crossbeam-permits/laguna-beach/0.5.0"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns("__pycache__", "results"))
    return target


def run(script: Path, *args: str, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(script), *args], cwd=cwd,
                          capture_output=True, text=True)


class PluginRootTests(unittest.TestCase):
    def test_root_is_the_plugin_folder(self):
        self.assertEqual(_lib.plugin_root(), ROOT)
        self.assertEqual(_lib.plugin_path("schemas/project-facts.schema.json"),
                         ROOT / "schemas/project-facts.schema.json")

    def test_plugin_path_refuses_escape_and_absolute(self):
        with self.assertRaises(ValueError):
            _lib.plugin_path("../outside.json")
        with self.assertRaises(ValueError):
            _lib.plugin_path("/etc/hosts")

    def test_resolver_works_from_a_task_directory(self):
        with tempfile.TemporaryDirectory() as task:
            result = run(ROOT / "scripts/plugin_root.py", "--json",
                         "--path", "schemas/project-facts.schema.json", cwd=Path(task))
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["plugin_root"], str(ROOT))
            self.assertTrue(Path(payload["paths"]["schemas/project-facts.schema.json"]).is_file())
            missing = run(ROOT / "scripts/plugin_root.py", "--path", "schemas/nope.json", cwd=Path(task))
            self.assertNotEqual(missing.returncode, 0)


class InstalledCopyValidationTests(unittest.TestCase):
    def test_validator_runs_in_an_installed_copy(self):
        with tempfile.TemporaryDirectory() as home:
            copy = installed_copy(Path(home))
            result = run(copy / "scripts/validate-plugin.py", "--skip-evals",
                         "--skip-claude-validation", cwd=Path(home))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("marketplace checks skipped", result.stdout)
            strict = run(copy / "scripts/validate-plugin.py", "--skip-evals",
                         "--skip-claude-validation", "--require-marketplace", cwd=Path(home))
            self.assertNotEqual(strict.returncode, 0)

    def test_validator_rejects_a_host_version_mismatch(self):
        with tempfile.TemporaryDirectory() as home:
            copy = installed_copy(Path(home))
            manifest = copy / "gemini-extension.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            data["version"] = "0.0.1"
            manifest.write_text(json.dumps(data), encoding="utf-8")
            result = run(copy / "scripts/validate-plugin.py", "--skip-evals",
                         "--skip-claude-validation", cwd=Path(home))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("versions must agree", result.stdout + result.stderr)

    def test_validator_rejects_a_connector_credential(self):
        with tempfile.TemporaryDirectory() as home:
            copy = installed_copy(Path(home))
            config = copy / ".mcp.json"
            data = json.loads(config.read_text(encoding="utf-8"))
            data["mcpServers"]["crossbeam"]["headers"] = {"Authorization": "Bearer example"}
            config.write_text(json.dumps(data), encoding="utf-8")
            result = run(copy / "scripts/validate-plugin.py", "--skip-evals",
                         "--skip-claude-validation", cwd=Path(home))
            self.assertNotEqual(result.returncode, 0)


class ConnectorConfigTests(unittest.TestCase):
    def test_every_host_points_at_the_same_oauth_server(self):
        claude = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]["crossbeam"]
        gemini = json.loads((ROOT / "gemini-extension.json").read_text())["mcpServers"]["crossbeam"]
        cursor = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())["mcpServers"]["crossbeam"]
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(claude["type"], "http")
        self.assertTrue(claude["url"].startswith("https://"))
        self.assertEqual(gemini["httpUrl"], claude["url"])
        self.assertEqual(cursor["url"], claude["url"])
        self.assertEqual(codex["mcpServers"], "./.mcp.json")
        for server in (claude, gemini, cursor):
            self.assertNotIn("headers", server)

    def test_preparer_says_the_connector_is_optional(self):
        wrapper = (ROOT / "skills/laguna-permit-preparer/SKILL.md").read_text()
        self.assertIn("Everything in this plugin works without it", wrapper)
        self.assertIn("continue without them", wrapper)


if __name__ == "__main__":
    unittest.main()
