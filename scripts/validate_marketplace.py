#!/usr/bin/env python3
"""Validate .claude-plugin/marketplace.json against the per-city plugin directories.

Catches drift between the top-level marketplace registry and the per-city
plugin manifests:

- marketplace.json must be valid JSON with required fields
- every plugin entry's `source` must resolve to a real directory in this repo
- each plugin directory must contain .claude-plugin/plugin.json (with matching name),
  meta.json, and a skills/ directory
- plugin names must be unique
- every folder under cities/ must be listed (no orphan city that nobody can install)

Every source must be `{"source": "git-subdir", "url": <this repo>, "path": "cities/<slug>"}`,
the format all entries use.

Exit code 0 on success, 1 on any validation failure.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
CITIES = REPO_ROOT / "cities"
REPO_URLS = {
    "https://github.com/CrossBeam-Permits/plugin.git",
    "https://github.com/CrossBeam-Permits/plugin",
}

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def resolve_source(name: str, src: object) -> Path | None:
    """Return the plugin folder a git-subdir `source` points at, or None after recording why."""
    if not isinstance(src, dict) or src.get("source") != "git-subdir":
        err(f"plugin[{name}]: 'source' must be a git-subdir object (got {src!r})")
        return None
    if src.get("url") not in REPO_URLS:
        err(f"plugin[{name}]: git-subdir url {src.get('url')!r} is not this repository")
        return None
    path = src.get("path")
    if not isinstance(path, str) or not path:
        err(f"plugin[{name}]: git-subdir source has no 'path'")
        return None
    parts = Path(path).parts
    if Path(path).is_absolute() or ".." in parts or (parts and parts[0].startswith(".")):
        err(f"plugin[{name}]: git-subdir path {path!r} must be a plain path inside this repository")
        return None
    return REPO_ROOT / path


def main() -> int:
    try:
        md = json.loads(MARKETPLACE.read_text())
    except FileNotFoundError:
        print(f"FAIL: {rel(MARKETPLACE)} not found")
        return 1
    except json.JSONDecodeError as e:
        print(f"FAIL: {rel(MARKETPLACE)} is not valid JSON: {e}")
        return 1

    if not isinstance(md, dict):
        print(f"FAIL: {rel(MARKETPLACE)} must be a JSON object")
        return 1

    for required in ("name", "owner", "plugins"):
        if required not in md:
            err(f"marketplace.json missing required field: {required!r}")

    seen_names: set[str] = set()
    listed_dirs: set[Path] = set()
    plugins = md.get("plugins")
    if not isinstance(plugins, list):
        err("marketplace.json 'plugins' must be a list")
        plugins = []
    for i, p in enumerate(plugins):
        if not isinstance(p, dict):
            err(f"plugin[{i}]: entry must be an object")
            continue
        name = p.get("name")
        if not name:
            err(f"plugin[{i}]: missing 'name'")
            continue
        if name in seen_names:
            err(f"plugin[{name}]: duplicate name")
        seen_names.add(name)

        plugin_dir = resolve_source(name, p.get("source"))
        if plugin_dir is None:
            continue
        if not plugin_dir.is_dir():
            err(f"plugin[{name}]: source path does not exist: {rel(plugin_dir)}")
            continue
        listed_dirs.add(plugin_dir.resolve())

        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.is_file():
            err(f"plugin[{name}]: missing {rel(plugin_json)}")
        else:
            try:
                pj = json.loads(plugin_json.read_text())
                if not isinstance(pj, dict) or pj.get("name") != name:
                    err(
                        f"plugin[{name}]: plugin.json name "
                        f"{pj.get('name') if isinstance(pj, dict) else pj!r} "
                        f"does not match marketplace name {name!r}"
                    )
            except json.JSONDecodeError as e:
                err(f"plugin[{name}]: invalid JSON in plugin.json: {e}")

        if not (plugin_dir / "meta.json").is_file():
            err(f"plugin[{name}]: missing {rel(plugin_dir / 'meta.json')}")
        if not (plugin_dir / "skills").is_dir():
            err(f"plugin[{name}]: missing skills/ directory")

    if CITIES.is_dir():
        for city in sorted(d for d in CITIES.iterdir() if d.is_dir()):
            if city.resolve() not in listed_dirs:
                err(f"{rel(city)}: not listed in marketplace.json, so it cannot be installed")

    if errors:
        print(f"FAIL: {len(errors)} validation error(s):")
        for e in errors[:50]:
            print(f"  - {e}")
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more")
        return 1

    print(f"OK: marketplace.json + {len(seen_names)} plugin manifests validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
