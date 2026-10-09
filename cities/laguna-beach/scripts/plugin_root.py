#!/usr/bin/env python3
"""Print the Laguna plugin root so commands can use absolute paths.

Run it by its absolute path from any directory, for example from the user's
task directory:

    python3 /path/to/laguna-beach/scripts/plugin_root.py
    python3 /path/to/laguna-beach/scripts/plugin_root.py --path schemas/project-facts.schema.json

It exits non-zero when the folder does not look like the Laguna plugin.
"""

from __future__ import annotations

import argparse
import json
import sys

from _lib import plugin_path, plugin_root

LAYOUT = [
    "SKILL.md",
    "scripts/_lib.py",
    "schemas",
    "assets",
    "references",
    "skills/laguna-permit-preparer/SKILL.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--path", action="append", default=[],
                        help="plugin-relative path to resolve; repeatable")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args()

    root = plugin_root()
    missing = [item for item in LAYOUT if not (root / item).exists()]
    if missing:
        print(f"not a complete Laguna plugin at {root}; missing {missing}", file=sys.stderr)
        return 1

    resolved = {}
    for item in args.path:
        try:
            target = plugin_path(item)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        if not target.exists():
            print(f"not found in the plugin: {item}", file=sys.stderr)
            return 1
        resolved[item] = str(target)

    if args.json:
        version = None
        manifest = root / ".claude-plugin/plugin.json"
        if manifest.is_file():
            version = json.loads(manifest.read_text(encoding="utf-8")).get("version")
        print(json.dumps({"plugin_root": str(root), "version": version, "paths": resolved}, indent=2))
    elif resolved:
        for value in resolved.values():
            print(value)
    else:
        print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
