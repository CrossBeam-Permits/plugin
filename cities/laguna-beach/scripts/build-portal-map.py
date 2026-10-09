#!/usr/bin/env python3
"""Compile a portal snapshot into the v2 portal map (offline, deterministic).

    python3 scripts/build-portal-map.py \
      --snapshot assets/portal-maps/portal-snapshot.json \
      --output assets/portal-maps/v2-portal-map.json
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _lib import load_json, sha256_file, write_json  # noqa: E402
from _portal import compile_map  # noqa: E402

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def relative_label(path: Path) -> str:
    try:
        return path.resolve().relative_to(PLUGIN_ROOT).as_posix()
    except ValueError:
        return path.name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    snapshot_path = Path(args.snapshot)
    portal_map = compile_map(load_json(snapshot_path), relative_label(snapshot_path), sha256_file(snapshot_path))
    write_json(args.output, portal_map)
    classes = sum(len(item["workClasses"]) for item in portal_map["record_types"])
    print(
        f"Built v2 portal map: {len(portal_map['record_types'])} record types, {classes} online work classes, "
        f"{len(portal_map['layouts'])} layouts -> {args.output}"
    )
    if portal_map["missing_mapped_menu_ids"]:
        print(f"WARNING mapped menu ids missing from the live catalog: {portal_map['missing_mapped_menu_ids']}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
