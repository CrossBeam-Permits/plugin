#!/usr/bin/env python3
"""Compare a fresh public portal snapshot to the pinned V1 route map."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from _lib import load_json


ROUTE_KEYS = [
    "menuId", "typeId", "typeName", "label", "module", "category", "applyUrl",
    "allowsInternetSubmission", "eReviewsEnabled", "feeEstimateAvailable",
    "internetApplyType", "workClassId", "workClassName", "templateName", "requires",
    "requiredAttachments", "attachments", "contactTypes", "questionCount",
    "questionGroups", "submitSuccessMessage",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def projection(snapshot: list[dict], ids: set[int]) -> list[dict]:
    result = []
    for route in snapshot:
        if route.get("menuId") not in ids:
            continue
        result.append({key: route.get(key) for key in ROUTE_KEYS})
    return sorted(result, key=lambda item: item["menuId"])


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--portal-map", required=True)
    parser.add_argument("--snapshot", required=True)
    args = parser.parse_args()

    portal_map = load_json(args.portal_map)
    snapshot_path = Path(args.snapshot)
    snapshot = load_json(snapshot_path)
    if not isinstance(snapshot, list):
        raise SystemExit("snapshot must be the public online-intake-summary JSON array")
    ids = {item["menuId"] for item in portal_map["routes"]}
    fresh = projection(snapshot, ids)
    pinned = sorted(portal_map["routes"], key=lambda item: item["menuId"])
    missing = sorted(ids - {item["menuId"] for item in fresh})
    changed = canonical(fresh) != canonical(pinned)
    source_digest = digest(snapshot_path)
    if missing or changed:
        if missing:
            print(f"ERROR missing V1 portal types: {missing}")
        if changed:
            print("ERROR portal route/configuration drift; rebuild and review v1-portal-map.json")
        print(f"Fresh snapshot SHA-256: {source_digest}")
        return 1
    print(f"Portal map current for {len(ids)} V1 types; snapshot SHA-256 {source_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
