#!/usr/bin/env python3
"""Compare the pinned v2 portal map with a fresh pull of the City's portal.

Two ways to get the fresh side:

    # Live: read the City's public catalog now (GET only, about 65 requests)
    python3 scripts/check-portal-freshness.py --live

    # Offline: compile a saved snapshot (for evals and re-checks)
    python3 scripts/check-portal-freshness.py --snapshot path/to/portal-snapshot.json

Exit codes: 0 current (warnings may be printed), 1 blocking drift, 2 the
fresh side could not be read or compiled. A blocking change means the pinned
map no longer matches what an applicant would see: rebuild the map, review the
diff, and update the references before anyone files with it.

Cosmetic changes, such as Tyler's template-name marker moving from ``-*`` to
``-**``, are warnings. They are printed but do not fail the check.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _lib import load_json, sha256_file, write_json  # noqa: E402
from _portal import (  # noqa: E402
    MAP_SCHEMA_VERSION,
    PortalClient,
    compile_map,
    diff_maps,
    pull_snapshot,
)

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAP = PLUGIN_ROOT / "assets/portal-maps/v2-portal-map.json"


def short(value: object, limit: int = 220) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def text_change(before: str | None, after: str | None, context: int = 80) -> str:
    """Show only the changed span of an instruction, with a little context."""
    if before is None and after is None:
        return "text not available in the snapshots"
    a = " ".join((before or "").split())
    b = " ".join((after or "").split())
    start = 0
    while start < min(len(a), len(b)) and a[start] == b[start]:
        start += 1
    end = 0
    while end < min(len(a), len(b)) - start and a[len(a) - 1 - end] == b[len(b) - 1 - end]:
        end += 1
    lead = a[max(0, start - context):start]
    old_part = a[start:len(a) - end]
    new_part = b[start:len(b) - end]
    tail = a[len(a) - end:len(a) - end + context]
    return f"...{lead}[-{old_part}-]{{+{new_part}+}}{tail}..."


def instruction_text(snapshot: dict | None, type_id: str, class_id: str, step: str) -> str | None:
    if not snapshot:
        return None
    return ((snapshot.get("instructions") or {}).get(f"{type_id}/{class_id}") or {}).get("steps", {}).get(step)


def render_report(pinned: dict, fresh: dict, findings: list[dict], fresh_label: str, snapshots: tuple[dict | None, dict | None]) -> str:
    blocking = [item for item in findings if item["severity"] == "blocking"]
    warnings = [item for item in findings if item["severity"] == "warning"]
    lines = [
        "# Laguna portal map drift report",
        "",
        f"- Pinned map: pulled {pinned['source']['pulled_at']} (snapshot {pinned['source']['snapshot_sha256'][:12]})",
        f"- Fresh side: {fresh_label}, pulled {fresh['source']['pulled_at']}",
        f"- Blocking changes: {len(blocking)}",
        f"- Warnings: {len(warnings)}",
        "",
    ]
    if not findings:
        lines.append("The pinned map matches the portal. Nothing to do.")
        return "\n".join(lines) + "\n"
    old_snapshot, new_snapshot = snapshots
    for title, items in (("Blocking drift (rebuild and review the map)", blocking), ("Warnings (no action needed to keep filing)", warnings)):
        if not items:
            continue
        lines += [f"## {title}", ""]
        current_scope = None
        for item in items:
            if item["scope"] != current_scope:
                current_scope = item["scope"]
                lines.append(f"### {current_scope}")
            lines.append(f"- {item['change']}")
            if item["before"] is not None:
                lines.append(f"  - before: {short(item['before'])}")
            if item["after"] is not None:
                lines.append(f"  - after: {short(item['after'])}")
            if item["change"] == "City instruction text changed":
                record = next((r for r in fresh["record_types"] if item["scope"].startswith(f"type {r['menuId']} ")), None)
                klass = None
                if record:
                    label = item["scope"].split(" / ", 1)[-1]
                    klass = next((w for w in record["workClasses"] if w["label"] == label), None)
                if record and klass:
                    for step in item["after"] or []:
                        before = instruction_text(old_snapshot, record["typeId"], klass["id"], step)
                        after = instruction_text(new_snapshot, record["typeId"], klass["id"], step)
                        lines.append(f"  - {step}: {text_change(before, after)}")
        lines.append("")
    if blocking:
        lines += [
            "## What to do",
            "",
            "1. Save the fresh pull: `python3 scripts/pull-portal-catalog.py --output assets/portal-maps/portal-snapshot.json`.",
            "2. Rebuild: `python3 scripts/build-portal-map.py --snapshot assets/portal-maps/portal-snapshot.json --output assets/portal-maps/v2-portal-map.json`.",
            "3. Review every blocking item above against `references/building-routing.md`, `planning-routing.md`, and `online-submission.md`; update them where an applicant would now be told something wrong.",
            "4. Run `python3 evals/run-evals.py`. Until this is done, the agent stops any affected record at the visible drift check.",
            "",
        ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--portal-map", default=str(DEFAULT_MAP), help="Pinned v2 map (default: the bundled one)")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--live", action="store_true", help="Pull the City's public catalog now (GET only)")
    source.add_argument("--snapshot", help="Compile this saved snapshot instead of pulling live")
    parser.add_argument("--save-snapshot", help="With --live, also save the fresh snapshot here")
    parser.add_argument("--report", help="Write the Markdown drift report to this file too")
    parser.add_argument("--json", dest="json_report", help="Write the findings as JSON to this file")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between live requests")
    args = parser.parse_args()

    pinned_path = Path(args.portal_map)
    pinned = load_json(pinned_path)
    if pinned.get("schema_version") != MAP_SCHEMA_VERSION:
        print(f"ERROR {pinned_path} is not a v{MAP_SCHEMA_VERSION} portal map; v1 maps have no work classes")
        return 2

    old_snapshot = None
    pinned_snapshot_path = PLUGIN_ROOT / pinned["source"]["snapshot"]
    if pinned_snapshot_path.is_file():
        old_snapshot = load_json(pinned_snapshot_path)

    try:
        if args.live:
            client = PortalClient(delay_seconds=args.delay)
            snapshot = pull_snapshot(client, tuple(pinned_snapshot_mapped_ids(pinned)), progress=lambda m: print(m, file=sys.stderr))
            with tempfile.TemporaryDirectory(prefix="laguna-portal-") as directory:
                temporary = Path(args.save_snapshot) if args.save_snapshot else Path(directory) / "portal-snapshot.json"
                write_json(temporary, snapshot)
                fresh = compile_map(snapshot, temporary.name, sha256_file(temporary))
            fresh_label = f"live pull ({len(client.log)} GET requests)"
        else:
            snapshot_path = Path(args.snapshot)
            snapshot = load_json(snapshot_path)
            fresh = compile_map(snapshot, snapshot_path.name, sha256_file(snapshot_path))
            fresh_label = f"snapshot {snapshot_path.name}"
    except Exception as error:  # network, HTTP, or shape failure: report it, never pass silently
        print(f"ERROR could not read the fresh portal configuration: {error}")
        return 2

    findings = diff_maps(pinned, fresh)
    report = render_report(pinned, fresh, findings, fresh_label, (old_snapshot, snapshot))
    print(report, end="")
    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
    if args.json_report:
        write_json(args.json_report, {"pinned_pulled_at": pinned["source"]["pulled_at"], "fresh_pulled_at": fresh["source"]["pulled_at"], "findings": findings})
    blocking = sum(item["severity"] == "blocking" for item in findings)
    if blocking:
        print(f"ERROR portal drift: {blocking} blocking change(s); rebuild and review v2-portal-map.json")
        return 1
    print(f"Portal map current for {len(pinned['record_types'])} record types ({len(findings)} warning(s))")
    return 0


def pinned_snapshot_mapped_ids(pinned: dict) -> list[int]:
    return [item["menuId"] for item in pinned["catalog"] if item.get("mapped")] or [item["menuId"] for item in pinned["record_types"]]


if __name__ == "__main__":
    raise SystemExit(main())
