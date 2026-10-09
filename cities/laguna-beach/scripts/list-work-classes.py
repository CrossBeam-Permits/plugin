#!/usr/bin/env python3
"""Show the City's online work classes for one portal record type.

This prints evidence for the agent to reason over: each class's label, filing
behavior, More Info question groups, required uploads and contacts, and the
City's own instruction text. It does not choose a class. The agent decides
from the project facts, writes work-class-selection.json with its reasons,
and confirms the choice with the user.

    python3 scripts/list-work-classes.py --type 183
    python3 scripts/list-work-classes.py --type 183 --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _lib import load_json  # noqa: E402
from _portal import attachments_for, contacts_for, record_type  # noqa: E402

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--type", type=int, required=True, help="Catalog menu id, e.g. 183")
    parser.add_argument("--portal-map", default=str(PLUGIN_ROOT / "assets/portal-maps/v2-portal-map.json"))
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text")
    args = parser.parse_args()

    portal_map = load_json(args.portal_map)
    route = record_type(portal_map, args.type)
    if route is None:
        raise SystemExit(f"type {args.type} is not in the portal map")
    snapshot_path = PLUGIN_ROOT / portal_map["source"]["snapshot"]
    snapshot = load_json(snapshot_path) if snapshot_path.is_file() else {}
    instructions = snapshot.get("instructions") or {}

    rows = []
    for klass in route["workClasses"]:
        layout = (portal_map["layouts"] or {}).get(klass.get("layoutId") or "", {"groups": []})
        rows.append(
            {
                "id": klass["id"],
                "label": klass["label"],
                "filing_behavior": klass["filingBehavior"],
                "own_catalog_entry": [item for item in klass["deepLinkedByMenuIds"] if item != args.type],
                "more_info_groups": [f"{group['group'] or '(untitled)'} ({len(group['questions'])})" for group in layout["groups"]],
                "required_more_info": [q["fieldName"] for g in layout["groups"] for q in g["questions"] if q["required"] and q["fieldName"]],
                "required_uploads": klass["requiredAttachments"],
                "one_file_uploads": [a["name"] for a in attachments_for(portal_map, klass) or [] if a.get("maxFiles") == 1],
                "required_contacts": [c["name"] for c in contacts_for(portal_map, klass) or [] if c["required"]],
                "city_instructions": (instructions.get(f"{route['typeId']}/{klass['id']}") or {}).get("steps") or {},
            }
        )
    if args.json:
        print(json.dumps({"type": args.type, "label": route["label"], "pulled_at": portal_map["source"]["pulled_at"], "work_classes": rows}, indent=2, ensure_ascii=False))
        return 0
    print(f"Type {args.type} {route['label']} - {len(rows)} online work classes (portal read {portal_map['source']['pulled_at']})")
    print(f"Catalog entry opens work class: {route['catalogWorkClassId']}")
    for row in rows:
        print(f"\n## {row['label']}  [{row['filing_behavior']}]  id={row['id']}")
        if row["own_catalog_entry"]:
            print(f"   Has its own catalog entry: {row['own_catalog_entry']} (file it there)")
        print(f"   More Info: {', '.join(row['more_info_groups']) or 'no questions'}")
        if row["required_more_info"]:
            print(f"   Required More Info: {', '.join(row['required_more_info'])}")
        print(f"   Required uploads: {', '.join(row['required_uploads']) or 'none'}; one file only: {', '.join(row['one_file_uploads']) or 'none'}")
        print(f"   Required contacts: {', '.join(row['required_contacts']) or 'none marked required'}")
        for step, text in row["city_instructions"].items():
            print(f"   City {step}: {' '.join(text.split())}")
        if not row["city_instructions"]:
            print("   City instructions: none configured for this class")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
