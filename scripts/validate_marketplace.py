#!/usr/bin/env python3
"""Validate .claude-plugin/marketplace.json against the per-city plugin directories.

Catches drift between the top-level marketplace registry and the 484 per-city
plugin manifests:

- marketplace.json must be valid JSON with required fields
- every plugin entry's `source` must resolve to a real directory
- each plugin directory must contain .claude-plugin/plugin.json (with matching name),
  meta.json, and a skills/ directory
- plugin names must be unique

Handles both source formats:
- `metadata.pluginRoot` + plain-string `source` (e.g. "huntington-beach")
- inline `source: "./cities/huntington-beach"` (no pluginRoot needed)

Exit code 0 on success, 1 on any validation failure.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def resolve_source(src: str, plugin_root: str) -> Path:
    if src.startswith("/"):
        return Path(src)
    if src.startswith("./"):
        return REPO_ROOT / src[2:]
    if plugin_root:
        return REPO_ROOT / plugin_root / src
    return REPO_ROOT / src


def main() -> int:
    try:
        md = json.loads(MARKETPLACE.read_text())
    except FileNotFoundError:
        print(f"FAIL: {MARKETPLACE.relative_to(REPO_ROOT)} not found")
        return 1
    except json.JSONDecodeError as e:
        print(f"FAIL: {MARKETPLACE.relative_to(REPO_ROOT)} is not valid JSON: {e}")
        return 1

    for required in ("name", "owner", "plugins"):
        if required not in md:
            err(f"marketplace.json missing required field: {required!r}")

    plugin_root = (
        md.get("metadata", {}).get("pluginRoot", "").lstrip("./").rstrip("/")
    )

    seen_names: set[str] = set()
    for i, p in enumerate(md.get("plugins", [])):
        name = p.get("name")
        src = p.get("source")

        if not name:
            err(f"plugin[{i}]: missing 'name'")
            continue
        if name in seen_names:
            err(f"plugin[{name}]: duplicate name")
        seen_names.add(name)

        if not isinstance(src, str):
            err(f"plugin[{name}]: 'source' must be a string (got {type(src).__name__})")
            continue

        plugin_dir = resolve_source(src, plugin_root)
        if not plugin_dir.is_dir():
            rel = plugin_dir.relative_to(REPO_ROOT) if REPO_ROOT in plugin_dir.parents else plugin_dir
            err(f"plugin[{name}]: source path does not exist: {rel}")
            continue

        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        meta_json = plugin_dir / "meta.json"
        skills_dir = plugin_dir / "skills"

        if not plugin_json.is_file():
            err(f"plugin[{name}]: missing {plugin_json.relative_to(REPO_ROOT)}")
        else:
            try:
                pj = json.loads(plugin_json.read_text())
                if pj.get("name") != name:
                    err(
                        f"plugin[{name}]: plugin.json name {pj.get('name')!r} "
                        f"does not match marketplace name {name!r}"
                    )
            except json.JSONDecodeError as e:
                err(f"plugin[{name}]: invalid JSON in plugin.json: {e}")

        if not meta_json.is_file():
            err(f"plugin[{name}]: missing {meta_json.relative_to(REPO_ROOT)}")
        if not skills_dir.is_dir():
            err(f"plugin[{name}]: missing skills/ directory")

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
