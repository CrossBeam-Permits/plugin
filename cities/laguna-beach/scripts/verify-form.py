#!/usr/bin/env python3
"""Reopen a filled PDF and verify canonical values, widgets, and appearances."""

from __future__ import annotations

import argparse
from pathlib import Path

from _lib import inherited_value, load_json, require_pypdf, sha256_file, utc_now, widget_inventory, write_json


def normal_appearance_present(widget: object) -> bool:
    resolved = widget.get_object() if hasattr(widget, "get_object") else widget
    appearance = resolved.get("/AP")
    if appearance is None:
        return False
    appearance = appearance.get_object()
    normal = appearance.get("/N")
    if normal is None:
        return False
    normal = normal.get_object() if hasattr(normal, "get_object") else normal
    if hasattr(normal, "keys"):
        return len(list(normal.keys())) > 0 or normal.get("/Length") is not None
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--answers", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    pypdf = require_pypdf()
    pdf = Path(args.pdf)
    answer_document = load_json(args.answers)
    reader = pypdf.PdfReader(str(pdf))
    fields = reader.get_fields() or {}

    widgets_by_name: dict[str, list[object]] = {}
    for page in reader.pages:
        for reference in page.get("/Annots") or []:
            widget = reference.get_object()
            if str(widget.get("/Subtype")) != "/Widget":
                continue
            current = widget
            parts: list[str] = []
            visited: set[int] = set()
            while current is not None:
                current = current.get_object() if hasattr(current, "get_object") else current
                if id(current) in visited:
                    break
                visited.add(id(current))
                if current.get("/T") is not None:
                    parts.append(str(current.get("/T")))
                current = current.get("/Parent")
            name = ".".join(reversed(parts)) if parts else None
            if name:
                widgets_by_name.setdefault(name, []).append(widget)

    errors: list[str] = []
    verified: list[dict] = []
    for answer in answer_document["answers"]:
        name = answer["pdf_field"]
        expected = str(answer["expected_value"])
        field = fields.get(name)
        if field is None:
            errors.append(f"canonical field missing: {name}")
            continue
        canonical_value = inherited_value(field, "/V")
        if str(canonical_value or "") != expected:
            errors.append(f"canonical value mismatch for {name}: expected {expected!r}, got {str(canonical_value or '')!r}")
        widgets = widgets_by_name.get(name, [])
        if not widgets:
            errors.append(f"widget missing for updated field: {name}")
            continue
        for index, widget in enumerate(widgets):
            effective = inherited_value(widget, "/V")
            if str(effective or "") != expected:
                errors.append(f"widget value mismatch for {name}[{index}]: expected {expected!r}, got {str(effective or '')!r}")
            if not normal_appearance_present(widget):
                errors.append(f"normal appearance missing for {name}[{index}]")
        verified.append({"pdf_field": name, "expected_value": expected, "widget_count": len(widgets)})

    report = {
        "schema_version": "1.0.0",
        "verified_at": utc_now(),
        "pdf": str(pdf.resolve()),
        "sha256": sha256_file(pdf),
        "canonical_field_count": len(fields),
        "widget_count": len(widget_inventory(reader)),
        "answers_verified": verified,
        "errors": errors,
        "logical_status": "pass" if not errors else "fail",
        "visual_status": "manual_render_review_required",
    }
    destination = Path(args.output) if args.output else pdf.with_name(pdf.stem + ".verification.json")
    write_json(destination, report)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Verified {len(verified)} field values and appearances -> {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
