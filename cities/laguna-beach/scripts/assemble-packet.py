#!/usr/bin/env python3
"""Assemble deterministic portal PDFs from an explicit category manifest."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from _lib import load_json, require_pypdf, sha256_file, utc_now, write_json


def flattened_reader(pypdf, source: Path):
    reader = pypdf.PdfReader(str(source))
    writer = pypdf.PdfWriter()
    writer.clone_document_from_reader(reader)
    fields = writer.get_fields() or {}
    values = {
        name: field.get("/V", "/Off" if str(field.get("/FT")) == "/Btn" else "")
        for name, field in fields.items()
    }
    if values:
        writer.update_page_form_field_values(None, values, auto_regenerate=False, flatten=True)
    writer.remove_annotations(subtypes="/Widget")
    writer.root_object.pop(pypdf.generic.NameObject("/AcroForm"), None)
    buffer = BytesIO()
    writer.write(buffer)
    buffer.seek(0)
    return pypdf.PdfReader(buffer), buffer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    pypdf = require_pypdf()
    manifest = load_json(args.manifest)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    receipts = []

    for packet in manifest.get("outputs", []):
        filename = packet["filename"]
        if Path(filename).name != filename or not filename.lower().endswith(".pdf"):
            raise SystemExit(f"unsafe or non-PDF output filename: {filename}")
        inputs = [Path(item) for item in packet["inputs"]]
        if not inputs:
            raise SystemExit(f"{filename}: no inputs")
        for source in inputs:
            if not source.is_file():
                raise SystemExit(f"{filename}: missing input {source}")

        writer = pypdf.PdfWriter()
        buffers: list[BytesIO] = []
        input_receipts = []
        for source in inputs:
            if packet.get("flatten_for_upload", False):
                reader, buffer = flattened_reader(pypdf, source)
                buffers.append(buffer)
            else:
                reader = pypdf.PdfReader(str(source))
            writer.append(reader)
            input_receipts.append({"path": str(source.resolve()), "sha256": sha256_file(source), "pages": len(reader.pages)})

        destination = output_dir / filename
        with destination.open("wb") as stream:
            writer.write(stream)
        reopened = pypdf.PdfReader(str(destination))
        expected_pages = sum(item["pages"] for item in input_receipts)
        if len(reopened.pages) != expected_pages:
            raise SystemExit(f"{filename}: page count changed during assembly")
        if packet.get("flatten_for_upload", False):
            widget_count = sum(
                1
                for page in reopened.pages
                for annotation in (page.get("/Annots") or [])
                if str(annotation.get_object().get("/Subtype")) == "/Widget"
            )
            if widget_count or reopened.get_fields():
                raise SystemExit(f"{filename}: flattened output still has form fields/widgets")
        receipts.append(
            {
                "filename": filename,
                "category": packet["category"],
                "path": str(destination.resolve()),
                "sha256": sha256_file(destination),
                "pages": len(reopened.pages),
                "flattened_for_upload": bool(packet.get("flatten_for_upload", False)),
                "inputs": input_receipts,
            }
        )

    receipt_path = output_dir / "packet-receipt.json"
    write_json(receipt_path, {"schema_version": "1.0.0", "assembled_at": utc_now(), "packets": receipts})
    print(f"Assembled {len(receipts)} portal packets -> {receipt_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
