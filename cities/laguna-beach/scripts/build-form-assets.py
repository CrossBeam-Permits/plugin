#!/usr/bin/env python3
"""Build exact-revision field maps from locally verified official PDFs."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _lib import (
    field_tree,
    field_tree_sha256,
    load_json,
    require_pypdf,
    sha256_file,
    utc_now,
    widget_inventory,
    write_json,
)


PLANNING_MAPPINGS = [
    {"fact_id": "site.address", "pdf_fields": ["Site Address"], "required": True, "applicant_controlled": False, "transform": "string"},
    {"fact_id": "owner.name", "pdf_fields": ["Owner Name"], "required": True, "applicant_controlled": True, "transform": "string"},
]

BUILDING_MAPPINGS = [
    {"fact_id": "site.address", "pdf_fields": ["PROJECT ADDRESS"], "required": True, "applicant_controlled": False, "transform": "string"},
    {"fact_id": "project.is_residential.{record_id}", "pdf_fields": ["Residential"], "required": True, "applicant_controlled": False, "transform": "checkbox", "on_value": "/On"},
    {"fact_id": "project.description.{record_id}", "pdf_fields": ["Description of Work 1", "Description of Work 2", "Description of Work 3", "Description of Work 4", "Description of Work 5", "Description of Work 6"], "required": True, "applicant_controlled": False, "transform": "lines"},
    {"fact_id": "project.valuation.{record_id}", "pdf_fields": ["Valuation of Work"], "required": True, "applicant_controlled": True, "transform": "currency"},
    {"fact_id": "applicant.name", "pdf_fields": ["APPLICANT NAME If none of the below"], "required": True, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "applicant.phone", "pdf_fields": ["Phone"], "required": True, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "applicant.email", "pdf_fields": ["Email Address"], "required": True, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "owner.name", "pdf_fields": ["LEGAL PROPERTY OWNER NAME"], "required": True, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "owner.phone", "pdf_fields": ["Phone_2"], "required": False, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "owner.email", "pdf_fields": ["Email Address_2"], "required": False, "applicant_controlled": True, "transform": "string"},
    {"fact_id": "owner.mailing_address", "pdf_fields": ["Mailing Address City State Zip"], "required": False, "applicant_controlled": True, "transform": "string"},
]

MEP_MAPPINGS = [
    dict(item)
    for item in BUILDING_MAPPINGS
    if item["fact_id"] != "project.is_residential.{record_id}"
]
for index, mapping in enumerate(MEP_MAPPINGS):
    if mapping["fact_id"] == "project.description.{record_id}":
        MEP_MAPPINGS[index] = {**mapping, "pdf_fields": mapping["pdf_fields"][:5]}


def locate_form(directory: Path, form: dict[str, Any]) -> Path:
    for name in (form["cache_name"], form["download_name"]):
        candidate = directory / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        f"{form['id']}: expected {form['cache_name']} or {form['download_name']} in {directory}"
    )


def mappings_for(form_id: str) -> tuple[list[dict[str, Any]], list[str]]:
    if form_id == "building-application":
        return BUILDING_MAPPINGS, ["Signature3", "Date"]
    if form_id == "mep-application":
        return MEP_MAPPINGS, ["Date56_af_date"]
    return PLANNING_MAPPINGS, ["Owner Signature", "Date Signed by Owner"]


def complete_mappings(
    form_id: str,
    explicit: list[dict[str, Any]],
    fields: list[dict[str, Any]],
    widgets: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    mappings = [dict(item) for item in explicit]
    mapped = {name for item in mappings for name in item["pdf_fields"]}
    review = []
    widget_states = {
        item["field_name"]: item.get("normal_appearance_states") or []
        for item in widgets
        if item.get("field_name")
    }
    for index, field in enumerate(fields):
        name = field["name"]
        field_type = field["type"]
        if field_type == "/Sig":
            review.append(name)
            continue
        if name in mapped or field_type not in {"/Tx", "/Btn", "/Ch"}:
            continue
        mapping = {
            "fact_id": f"form.{form_id}.field.{index:03d}",
            "pdf_fields": [name],
            "pdf_label": field.get("tooltip") or name,
            "required": False,
            "applicant_controlled": False,
            "transform": "checkbox" if field_type == "/Btn" else "string",
        }
        if field_type == "/Btn":
            states = [item for item in widget_states.get(name, []) if item != "/Off"]
            if states:
                mapping["on_value"] = states[0]
            else:
                review.append(name)
                continue
        mappings.append(mapping)
        mapped.add(name)
    return mappings, review


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--forms-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    pypdf = require_pypdf()
    manifest = load_json(args.manifest)
    forms_dir = Path(args.forms_dir)
    output_dir = Path(args.output_dir)
    failures: list[str] = []

    for form in manifest["forms"]:
        try:
            path = locate_form(forms_dir, form)
            reader = pypdf.PdfReader(str(path))
            fields = field_tree(reader)
            widgets = widget_inventory(reader)
            actual = {
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
                "pages": len(reader.pages),
                "canonical_fields": len(fields),
                "widgets": len(widgets),
                "field_tree_sha256": field_tree_sha256(reader),
            }
            for key, value in actual.items():
                if value != form[key]:
                    failures.append(f"{form['id']}: {key} expected {form[key]!r}, got {value!r}")
            explicit_mappings, review_fields = mappings_for(form["id"])
            mappings, signature_fields = complete_mappings(form["id"], explicit_mappings, fields, widgets)
            review_fields = sorted(set(review_fields + signature_fields))
            available = {item["name"] for item in fields}
            for mapping in mappings:
                for pdf_field in mapping["pdf_fields"]:
                    if pdf_field not in available:
                        failures.append(f"{form['id']}: mapped PDF field is absent: {pdf_field}")
            write_json(
                output_dir / f"{form['id']}.json",
                {
                    "schema_version": "1.0.0",
                    "form_id": form["id"],
                    "field_map_version": form["field_map_version"],
                    "generated_at": utc_now(),
                    "source_sha256": form["sha256"],
                    "field_tree_sha256": form["field_tree_sha256"],
                    "canonical_mappings": mappings,
                    "review_fields": review_fields,
                    "fields": fields,
                    "widgets": widgets,
                },
            )
        except Exception as exc:  # report every affected form in one run
            failures.append(f"{form['id']}: {exc}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1
    print(f"Built {len(manifest['forms'])} field maps -> {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
