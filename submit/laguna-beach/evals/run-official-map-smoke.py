#!/usr/bin/env python3
"""Fill and verify each semantic form map against user-acquired official PDFs."""

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
SEMANTIC_FORM_IDS = (
    "building-application",
    "coastal-development-permit-application",
    "design-review-application",
    "floodplain-development-residential",
    "zone-clearance-application",
)
PREVIEW_PAGES = {
    "building-application": (1,),
    "coastal-development-permit-application": (2,),
    "design-review-application": (2, 25),
    "floodplain-development-residential": (1,),
    "zone-clearance-application": (1, 2),
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def value_for(mapping: dict) -> object:
    fact_id = mapping["fact_id"]
    if mapping["transform"] == "lines":
        target_count = len(mapping.get("pdf_fields") or mapping.get("pdf_widgets") or [])
        return ("Map test " * (target_count * 5)).strip()
    known = {
        "site.address": "123 Test Avenue, Laguna Beach, CA 92651",
        "site.apn": "644-123-45",
        "project.description": "Synthetic permit form map verification.",
        "project.description.smoke": "Synthetic permit form map verification.",
        "owner.name": "Olivia Owner",
        "owner.contact_name": "Olivia Owner",
        "applicant.name": "Alex Applicant",
        "applicant.contact_name": "Alex Applicant",
        "applicant.phone": "949-555-0100",
        "applicant.email": "applicant@example.invalid",
    }
    if fact_id in known:
        return known[fact_id]
    if mapping["transform"] in {"checkbox", "yes_no"}:
        return True
    if mapping["transform"] == "currency":
        return 1000
    return "1"


def facts_for(field_map: dict, timestamp: str) -> dict:
    facts = []
    seen: set[str] = set()
    for mapping in field_map["canonical_mappings"]:
        fact_id = mapping["fact_id"].replace("{record_id}", "smoke")
        effective_mapping = {**mapping, "fact_id": fact_id}
        if fact_id in seen:
            continue
        seen.add(fact_id)
        controlled = bool(mapping.get("applicant_controlled"))
        facts.append(
            {
                "id": fact_id,
                "value": value_for(effective_mapping),
                "source": {
                    "kind": "user_confirmed" if controlled else "plan",
                    "receipt": {
                        "kind": "user_answer" if controlled else "file",
                        "captured_at": timestamp,
                        "file": "synthetic-map-smoke",
                        "page": None,
                        "sheet": "release-eval",
                        "field": fact_id,
                        "record_id": "smoke",
                        "note": "Synthetic release verification; not a real filing",
                    },
                },
                "confidence": 1,
                "confirmation": {
                    "required": controlled,
                    "status": "confirmed" if controlled else "not_required",
                    "confirmed_at": timestamp if controlled else None,
                    "note": "Synthetic release verification",
                },
                "consumers": [],
                "conflicts": [],
                "notes": ["Synthetic release verification; not for submission"],
            }
        )
    return {
        "schema_version": "1.0.0",
        "run_id": "official-map-smoke",
        "jurisdiction": "laguna-beach-ca",
        "created_at": timestamp,
        "updated_at": timestamp,
        "facts": facts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forms-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--only", action="append", choices=SEMANTIC_FORM_IDS)
    args = parser.parse_args()
    selected = tuple(args.only or SEMANTIC_FORM_IDS)
    forms_dir = Path(args.forms_dir)
    output_root = Path(args.output_dir)
    manifest = load(ROOT / "assets/form-manifest.json")
    manifest_by_id = {item["id"]: item for item in manifest["forms"]}
    reports = []

    for form_id in selected:
        form = manifest_by_id[form_id]
        source = forms_dir / form["cache_name"]
        if not source.is_file():
            source = forms_dir / form["download_name"]
        if not source.is_file():
            raise SystemExit(f"{form_id}: official PDF is missing from {forms_dir}")
        field_map = load(ROOT / "assets/field-maps" / f"{form_id}.json")
        form_output = output_root / form_id
        facts_path = form_output / "project-facts.json"
        filled = form_output / f"{form_id}-filled.pdf"
        dump(facts_path, facts_for(field_map, now()))
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
        command = [
            sys.executable,
            str(SCRIPTS / "fill-form.py"),
            "--input",
            str(source),
            "--facts",
            str(facts_path),
            "--field-map",
            str(ROOT / "assets/field-maps" / f"{form_id}.json"),
            "--output",
            str(filled),
        ]
        if any("{record_id}" in item["fact_id"] for item in field_map["canonical_mappings"]):
            command.extend(["--record-id", "smoke"])
        subprocess.run(command, check=True)
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
        answer_count = len(load(answers_path)["answers"])
        expected = sum(
            len(item.get("pdf_fields") or item.get("pdf_widgets") or [])
            for item in field_map["canonical_mappings"]
        )
        if answer_count != expected:
            raise AssertionError(f"{form_id}: expected {expected} answers, got {answer_count}")

        if shutil.which("pdftoppm"):
            preview_dir = form_output / "previews"
            preview_dir.mkdir(parents=True, exist_ok=True)
            for page in PREVIEW_PAGES[form_id]:
                subprocess.run(
                    [
                        "pdftoppm", "-f", str(page), "-l", str(page), "-png", "-r", "144",
                        "-singlefile", str(filled), str(preview_dir / f"page-{page}"),
                    ],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
        reports.append(
            {
                "form_id": form_id,
                "source_sha256": form["sha256"],
                "field_map_version": field_map["field_map_version"],
                "semantic_targets_filled": answer_count,
                "logical_verification": "pass",
                "visual_review": "required",
            }
        )
        print(f"PASS {form_id}: {answer_count} semantic targets")

    dump(
        output_root / "official-map-smoke-report.json",
        {"schema_version": "1.0.0", "not_for_submission": True, "forms": reports},
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
