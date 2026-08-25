#!/usr/bin/env python3
"""Fill exact mapped AcroForm fields from provenance-bearing project facts."""

from __future__ import annotations

import argparse
import textwrap
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from _lib import (
    confirmed_fact_value,
    fact_index,
    full_field_name,
    load_json,
    require_pypdf,
    sha256_file,
    utc_now,
    write_json,
)


def rect_key(rect: list[float]) -> tuple[float, ...]:
    return tuple(round(float(item), 3) for item in rect)


def source_widget_key(page: int, field_name: str, rect: list[float]) -> tuple[Any, ...]:
    return (int(page), str(field_name), rect_key(rect))


def mapping_targets(mapping: dict[str, Any]) -> list[dict[str, Any]]:
    fields = mapping.get("pdf_fields") or []
    widgets = mapping.get("pdf_widgets") or []
    if fields and widgets:
        raise ValueError(f"mapping {mapping['fact_id']} mixes pdf_fields and pdf_widgets")
    if not fields and not widgets:
        raise ValueError(f"mapping {mapping['fact_id']} has no PDF targets")
    if fields:
        return [{"kind": "field", "name": name} for name in fields]
    return [
        {
            "kind": "widget",
            "page": int(widget["page"]),
            "field_name": str(widget["field_name"]),
            "rect": [float(item) for item in widget["rect"]],
        }
        for widget in widgets
    ]


def writer_widget_records(writer: Any) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for page_number, page in enumerate(writer.pages, start=1):
        for widget_index, reference in enumerate(page.get("/Annots") or []):
            widget = reference.get_object()
            if str(widget.get("/Subtype")) != "/Widget":
                continue
            rect = widget.get("/Rect")
            name = full_field_name(widget)
            if rect is None or name is None:
                continue
            records.append(
                {
                    "page": page_number,
                    "widget_index": widget_index,
                    "reference": reference,
                    "widget": widget,
                    "field_name": name,
                    "rect": [float(item) for item in rect],
                    "parent": widget.get("/Parent"),
                }
            )
    return records


def split_duplicate_widget_fields(
    pypdf: Any,
    writer: Any,
    exact_target_keys: set[tuple[Any, ...]],
) -> dict[tuple[Any, ...], str]:
    """Give each widget in a targeted multi-widget field a stable output field name."""

    records = writer_widget_records(writer)
    records_by_key: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for record in records:
        key = source_widget_key(record["page"], record["field_name"], record["rect"])
        records_by_key.setdefault(key, []).append(record)
    for key in exact_target_keys:
        matches = records_by_key.get(key, [])
        if len(matches) != 1:
            raise SystemExit(f"field-map widget drift; expected one exact target for {key}, got {len(matches)}")

    parent_ids: set[tuple[int, int]] = set()
    output_names: dict[tuple[Any, ...], str] = {}
    for key in exact_target_keys:
        record = records_by_key[key][0]
        parent = record["parent"]
        if parent is None:
            output_name = (
                f"crossbeam_p{record['page']:03d}_w{record['widget_index']:03d}_"
                f"terminal_{record['reference'].idnum}"
            )
            record["widget"][pypdf.generic.NameObject("/T")] = (
                pypdf.generic.TextStringObject(output_name)
            )
            output_names[key] = output_name
            continue
        parent_ids.add((parent.idnum, parent.generation))

    if not parent_ids:
        return output_names

    grouped: dict[tuple[int, int], list[dict[str, Any]]] = {}
    for record in records:
        parent = record["parent"]
        if parent is None:
            continue
        parent_id = (parent.idnum, parent.generation)
        if parent_id in parent_ids:
            grouped.setdefault(parent_id, []).append(record)

    acroform = writer._root_object["/AcroForm"].get_object()
    top_fields = acroform["/Fields"]
    top_field_ids = {
        (reference.idnum, reference.generation): index
        for index, reference in enumerate(top_fields)
    }
    missing_top_level = parent_ids - set(top_field_ids)
    if missing_top_level:
        raise SystemExit(
            "exact widget normalization currently requires top-level terminal fields; "
            f"nested parents found: {sorted(missing_top_level)}"
        )

    replacements: dict[tuple[int, int], list[Any]] = {}
    for parent_id, siblings in grouped.items():
        parent_reference = siblings[0]["parent"]
        parent = parent_reference.get_object()
        new_references: list[Any] = []
        for ordinal, record in enumerate(
            sorted(siblings, key=lambda item: (item["page"], item["widget_index"])),
            start=1,
        ):
            output_name = (
                f"crossbeam_p{record['page']:03d}_w{record['widget_index']:03d}_"
                f"{parent_id[0]}_{ordinal:03d}"
            )
            new_parent = pypdf.generic.DictionaryObject()
            for key, value in parent.items():
                if str(key) not in {"/Kids", "/T", "/V", "/DV"}:
                    new_parent[key] = value
            new_parent[pypdf.generic.NameObject("/T")] = pypdf.generic.TextStringObject(output_name)
            new_parent[pypdf.generic.NameObject("/Kids")] = pypdf.generic.ArrayObject(
                [record["reference"]]
            )
            new_reference = writer._add_object(new_parent)
            record["widget"][pypdf.generic.NameObject("/Parent")] = new_reference
            new_references.append(new_reference)
            original_key = source_widget_key(
                record["page"], record["field_name"], record["rect"]
            )
            output_names[original_key] = output_name
        replacements[parent_id] = new_references

    rebuilt = pypdf.generic.ArrayObject()
    for reference in top_fields:
        parent_id = (reference.idnum, reference.generation)
        if parent_id in replacements:
            rebuilt.extend(replacements[parent_id])
        else:
            rebuilt.append(reference)
    acroform[pypdf.generic.NameObject("/Fields")] = rebuilt
    return output_names


def fact_id_for(template: str, record_id: str | None) -> str:
    if "{record_id}" not in template:
        return template
    if not record_id:
        raise ValueError(f"--record-id is required by fact mapping {template}")
    return template.replace("{record_id}", record_id)


def transform(value: Any, mapping: dict[str, Any], field_count: int) -> list[str]:
    mode = mapping["transform"]
    if mode == "currency":
        try:
            amount = Decimal(str(value).replace("$", "").replace(",", ""))
        except InvalidOperation as exc:
            raise ValueError(f"not a currency value: {value!r}") from exc
        return ["$" + format(amount, ",.2f")]
    if mode == "lines":
        lines = textwrap.wrap(str(value), width=45, break_long_words=False, break_on_hyphens=False)
        if len(lines) > field_count:
            raise ValueError(f"description needs {len(lines)} lines but the map provides {field_count}")
        return lines
    if mode == "checkbox":
        if isinstance(value, bool):
            checked = value
        elif isinstance(value, (int, float)) and value in (0, 1):
            checked = bool(value)
        elif isinstance(value, str) and value.strip().lower() in {"true", "yes", "on", "1"}:
            checked = True
        elif isinstance(value, str) and value.strip().lower() in {"false", "no", "off", "0"}:
            checked = False
        else:
            raise ValueError(f"not a checkbox value: {value!r}")
        return [mapping.get("on_value", "/Yes") if checked else "/Off"]
    if mode == "yes_no":
        if isinstance(value, bool):
            return ["Yes" if value else "No"]
        if isinstance(value, str) and value.strip().lower() in {"yes", "no"}:
            return [value.strip().capitalize()]
        raise ValueError(f"not a yes/no value: {value!r}")
    return [str(value)]


def sidecar(pdf: Path, suffix: str) -> Path:
    return pdf.with_name(pdf.stem + suffix)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--facts", required=True)
    parser.add_argument("--field-map", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--record-id")
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args()

    pypdf = require_pypdf()
    source = Path(args.input)
    output = Path(args.output)
    facts_document = load_json(args.facts)
    facts = fact_index(facts_document)
    field_map = load_json(args.field_map)

    source_digest = sha256_file(source)
    if source_digest != field_map["source_sha256"]:
        raise SystemExit(
            f"source checksum drift: field map expects {field_map['source_sha256']}, got {source_digest}"
        )

    reader = pypdf.PdfReader(str(source))
    available = reader.get_fields() or {}
    exact_target_keys: set[tuple[Any, ...]] = set()
    for mapping in field_map["canonical_mappings"]:
        for target in mapping_targets(mapping):
            if target["kind"] == "widget":
                key = source_widget_key(target["page"], target["field_name"], target["rect"])
                if key in exact_target_keys:
                    raise SystemExit(f"field-map reuses an exact widget target: {key}")
                exact_target_keys.add(key)

    writer = pypdf.PdfWriter()
    writer.clone_document_from_reader(reader)
    output_names = split_duplicate_widget_fields(pypdf, writer, exact_target_keys)

    values: dict[str, str] = {}
    font_sizes: dict[str, float] = {}
    output_y_offsets: dict[str, float] = {}
    answers: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []

    for mapping in field_map["canonical_mappings"]:
        targets = mapping_targets(mapping)
        target_labels = [
            target["name"]
            if target["kind"] == "field"
            else {
                "page": target["page"],
                "field_name": target["field_name"],
                "rect": target["rect"],
            }
            for target in targets
        ]
        fact_id = fact_id_for(mapping["fact_id"], args.record_id)
        fact = facts.get(fact_id)
        if fact is None:
            unresolved.append({"fact_id": fact_id, "required": mapping["required"], "reason": "fact is absent", "pdf_targets": target_labels})
            continue
        usable, raw_value, reason = confirmed_fact_value(fact)
        if not usable:
            unresolved.append({"fact_id": fact_id, "required": mapping["required"], "reason": reason, "pdf_targets": target_labels})
            continue
        if mapping.get("applicant_controlled") and (fact.get("confirmation") or {}).get("status") != "confirmed":
            unresolved.append({"fact_id": fact_id, "required": mapping["required"], "reason": "applicant-controlled fact is not confirmed", "pdf_targets": target_labels})
            continue
        missing_fields = [
            target["name"]
            for target in targets
            if target["kind"] == "field" and target["name"] not in available
        ]
        if missing_fields:
            raise SystemExit(f"field-map drift; PDF fields are absent: {missing_fields}")
        rendered = transform(raw_value, mapping, len(targets))
        for target, rendered_value in zip(targets, rendered):
            if target["kind"] == "field":
                pdf_field = target["name"]
                source_widget = None
            else:
                widget_key = source_widget_key(
                    target["page"], target["field_name"], target["rect"]
                )
                pdf_field = output_names[widget_key]
                source_widget = {
                    "page": target["page"],
                    "field_name": target["field_name"],
                    "rect": target["rect"],
                }
            values[pdf_field] = rendered_value
            font_sizes[pdf_field] = float(mapping.get("font_size", 0))
            output_y_offsets[pdf_field] = float(mapping.get("output_y_offset", 0))
            answers.append(
                {
                    "fact_id": fact_id,
                    "pdf_field": pdf_field,
                    "expected_value": rendered_value,
                    "source": fact["source"],
                    "applicant_controlled": mapping.get("applicant_controlled", False),
                    "source_widget": source_widget,
                }
            )

    required_unresolved = [item for item in unresolved if item["required"]]
    if required_unresolved and not args.allow_partial:
        write_json(sidecar(output, ".unresolved-fields.json"), {"schema_version": "1.0.0", "form_id": field_map["form_id"], "unresolved": unresolved})
        print(f"Blocked: {len(required_unresolved)} required facts are unresolved")
        return 2

    for record in writer_widget_records(writer):
        name = full_field_name(record["widget"])
        offset = output_y_offsets.get(name, 0)
        if not offset:
            continue
        rect = record["widget"]["/Rect"]
        record["widget"][pypdf.generic.NameObject("/Rect")] = pypdf.generic.ArrayObject(
            [
                pypdf.generic.FloatObject(float(rect[0])),
                pypdf.generic.FloatObject(float(rect[1]) + offset),
                pypdf.generic.FloatObject(float(rect[2])),
                pypdf.generic.FloatObject(float(rect[3]) + offset),
            ]
        )

    writer_fields = writer.get_fields() or {}
    missing_after_clone = sorted(set(values) - set(writer_fields))
    if missing_after_clone:
        raise SystemExit(f"fields missing after clone: {missing_after_clone}")
    if values:
        appearance_values: dict[str, Any] = {}
        for name, value in values.items():
            field = writer_fields[name]
            if str(field.get("/FT")) == "/Tx":
                field[pypdf.generic.NameObject("/V")] = pypdf.generic.TextStringObject(value)
                appearance_values[name] = (value, "/Helv", font_sizes.get(name, 0))
            else:
                appearance_values[name] = value
        for record in writer_widget_records(writer):
            name = full_field_name(record["widget"])
            if name not in values:
                continue
            parent = record["widget"].get("/Parent")
            if parent is not None and str(parent.get_object().get("/FT")) == "/Tx":
                parent.get_object()[pypdf.generic.NameObject("/V")] = (
                    pypdf.generic.TextStringObject(values[name])
                )
        writer.update_page_form_field_values(
            None,
            appearance_values,
            auto_regenerate=False,
            flatten=False,
        )
        for record in writer_widget_records(writer):
            name = full_field_name(record["widget"])
            if name not in values:
                continue
            parent = record["widget"].get("/Parent")
            if parent is not None and str(parent.get_object().get("/FT")) == "/Tx":
                parent.get_object()[pypdf.generic.NameObject("/V")] = (
                    pypdf.generic.TextStringObject(values[name])
                )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as stream:
        writer.write(stream)

    common = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "form_id": field_map["form_id"],
        "field_map_version": field_map["field_map_version"],
        "source_pdf": str(source.resolve()),
        "source_sha256": source_digest,
        "output_pdf": str(output.resolve()),
        "output_sha256": sha256_file(output),
    }
    write_json(sidecar(output, ".answers-used.json"), {**common, "answers": answers})
    write_json(sidecar(output, ".unresolved-fields.json"), {**common, "unresolved": unresolved})
    write_json(
        sidecar(output, ".review-and-sign.json"),
        {
            **common,
            "review_fields": field_map["review_fields"],
            "instruction": "User must review the final rendered form and personally complete signatures/attestations.",
        },
    )
    print(f"Filled {len(answers)} exact fields -> {output}")
    if required_unresolved:
        print(f"WARNING: {len(required_unresolved)} required facts remain unresolved")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
