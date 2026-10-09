#!/usr/bin/env python3
"""Pull the City's public EnerGov catalog into a portal snapshot (read-only).

Every request is an unauthenticated GET to the City's public SelfService API.
Nothing here signs in, creates a draft, uploads, or submits. The snapshot keeps
only the fields the portal map uses, in sorted-key JSON, so two pulls diff
cleanly. Build the map from it with build-portal-map.py.

    python3 scripts/pull-portal-catalog.py --output /tmp/portal-snapshot.json
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _lib import write_json  # noqa: E402
from _portal import MAPPED_MENU_IDS, PortalClient, pull_snapshot  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", required=True, help="Where to write the snapshot JSON")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests (default 1.0)")
    parser.add_argument(
        "--menu-ids",
        default=",".join(str(item) for item in MAPPED_MENU_IDS),
        help="Comma-separated catalog menu ids to map (default: the plugin's record types)",
    )
    args = parser.parse_args()
    menu_ids = tuple(int(item) for item in args.menu_ids.split(",") if item.strip())
    client = PortalClient(delay_seconds=args.delay)
    snapshot = pull_snapshot(client, menu_ids, progress=lambda message: print(message, file=sys.stderr))
    write_json(args.output, snapshot)
    print(f"{len(client.log)} GET requests -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
