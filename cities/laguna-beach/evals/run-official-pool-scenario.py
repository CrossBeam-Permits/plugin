#!/usr/bin/env python3
"""Exercise every semantic DR page-2/page-25 target against the pinned City PDF."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def scenario_value(mapping: dict) -> object:
    overrides = {
        "site.address": "123 Test Avenue, Laguna Beach, CA 92651",
        "site.apn": "644-123-45",
        "site.use": "Single-family residential",
        "site.zone": "R-1",
        "site.lot_slope_percent": "12%",
        "applicant.company_name": "Test Pool Company",
        "applicant.contact_name": "Alex Applicant",
        "applicant.mailing_address": "123 Test Avenue",
        "applicant.city_state_zip": "Laguna Beach, CA 92651",
        "applicant.phone": "949-555-0100",
        "applicant.email": "applicant@example.invalid",
        "applicant_representative.company_name": "Test Design Studio",
        "applicant_representative.contact_name": "Riley Representative",
        "applicant_representative.mailing_address": "456 Test Street",
        "applicant_representative.city_state_zip": "Laguna Beach, CA 92651",
        "applicant_representative.phone": "949-555-0101",
        "applicant_representative.email": "representative@example.invalid",
        "owner.company_name": "",
        "owner.contact_name": "Olivia Owner",
        "owner.mailing_address": "123 Test Avenue",
        "owner.city_state_zip": "Laguna Beach, CA 92651",
        "owner.phone": "949-555-0102",
        "owner.email": "owner@example.invalid",
        "project.description": "New in-ground swimming pool and spa with associated equipment and site work.",
        "project.pool.length_by_width": "30 ft x 15 ft",
        "project.pool.depth": "3.5-8 ft",
        "project.pool.volume_gallons": "18,000",
        "project.spa.length_by_width": "8 ft x 8 ft",
        "project.spa.depth": "3.5 ft",
        "project.spa.volume_gallons": "900",
        "project.pool_spa.total_volume_gallons": "18,900",
        "project.grading.cut.pool_spa_cubic_yards": "85",
        "project.grading.fill.pool_spa_cubic_yards": "12",
        "project.grading.net_export.pool_spa_cubic_yards": "73",
    }
    fact_id = mapping["fact_id"]
    if fact_id in overrides:
        return overrides[fact_id]
    if mapping["transform"] in {"checkbox", "yes_no"}:
        return True
    if "quantity" in fact_id or "count" in fact_id:
        return 1
    if "comments" in fact_id:
        return "Test"
    return "1"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forms-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    forms_dir = Path(args.forms_dir)
    output_dir = Path(args.output_dir)
    field_map = load(ROOT / "assets/field-maps/design-review-application.json")
    manifest = load(ROOT / "assets/form-manifest.json")
    form = next(item for item in manifest["forms"] if item["id"] == "design-review-application")
    source = forms_dir / form["cache_name"]
    if not source.is_file():
        source = forms_dir / form["download_name"]
    if not source.is_file():
        raise SystemExit(f"official Design Review PDF is missing from {forms_dir}")

    now = timestamp()
    facts = []
    seen: set[str] = set()
    for mapping in field_map["canonical_mappings"]:
        fact_id = mapping["fact_id"]
        if fact_id in seen:
            continue
        seen.add(fact_id)
        controlled = bool(mapping.get("applicant_controlled"))
        facts.append(
            {
                "id": fact_id,
                "value": scenario_value(mapping),
                "source": {
                    "kind": "user_confirmed" if controlled else "plan",
                    "receipt": {
                        "kind": "user_answer" if controlled else "file",
                        "captured_at": now,
                        "file": "synthetic-pool-scenario",
                        "page": None,
                        "sheet": "release-eval",
                        "field": fact_id,
                        "record_id": None,
                        "note": "Synthetic release scenario; not a real parcel or filing",
                    },
                },
                "confidence": 1,
                "confirmation": {
                    "required": controlled,
                    "status": "confirmed" if controlled else "not_required",
                    "confirmed_at": now if controlled else None,
                    "note": "Synthetic release scenario",
                },
                "consumers": [],
                "conflicts": [],
                "notes": ["Synthetic release scenario; not for submission"],
            }
        )
    facts_document = {
        "schema_version": "1.0.0",
        "run_id": "official-pool-map-release-eval",
        "jurisdiction": "laguna-beach-ca",
        "created_at": now,
        "updated_at": now,
        "facts": facts,
    }
    facts_path = output_dir / "project-facts.json"
    filled = output_dir / "design-review-pool-filled.pdf"
    dump(facts_path, facts_document)

    subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "validate-json.py"),
            "--schema",
            str(ROOT / "schemas/project-facts.schema.json"),
            str(facts_path),
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "fill-form.py"),
            "--input",
            str(source),
            "--facts",
            str(facts_path),
            "--field-map",
            str(ROOT / "assets/field-maps/design-review-application.json"),
            "--output",
            str(filled),
        ],
        check=True,
    )
    answers_path = filled.with_name(filled.stem + ".answers-used.json")
    subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "verify-form.py"),
            "--pdf",
            str(filled),
            "--answers",
            str(answers_path),
        ],
        check=True,
    )

    answers = load(answers_path)["answers"]
    if len(answers) != 205:
        raise AssertionError(f"expected 205 semantic target answers, got {len(answers)}")
    unresolved = load(filled.with_name(filled.stem + ".unresolved-fields.json"))["unresolved"]
    if unresolved:
        raise AssertionError(f"fully sourced release scenario has unresolved mappings: {unresolved}")

    preview_dir = output_dir / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    if shutil.which("pdftoppm"):
        for page in (2, 25):
            subprocess.run(
                [
                    "pdftoppm",
                    "-f",
                    str(page),
                    "-l",
                    str(page),
                    "-png",
                    "-r",
                    "144",
                    "-singlefile",
                    str(filled),
                    str(preview_dir / f"page-{page}"),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

    report = {
        "schema_version": "1.0.0",
        "scenario": "synthetic new in-ground pool and spa",
        "not_for_submission": True,
        "source_sha256": form["sha256"],
        "field_map_version": field_map["field_map_version"],
        "page_2_semantic_targets_filled": 21,
        "page_25_semantic_targets_filled": 184,
        "total_semantic_targets_filled": len(answers),
        "review_only_page_2_duplicate": "Text25 (overlaps owner mailing address Text24)",
        "logical_verification": "pass",
        "visual_review": "required",
    }
    dump(output_dir / "pool-scenario-report.json", report)
    print(f"PASS official pool scenario: 21 page-2 + 184 page-25 targets -> {filled}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
