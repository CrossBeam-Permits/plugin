#!/usr/bin/env python3
"""Check an applicant-signed form against the unsigned fill before upload.

The applicant signs the filled PDF themselves: wet-sign and scan, or their own
e-signature tool. This script never applies a signature. It proves three things
mechanically and leaves the final look to a person:

1. The signed file is a different file with the same page count.
2. The filled values did not change (re-runs verify-form.py when fields survive;
   otherwise looks for each value in the text layer and lists the rest for
   visual comparison).
3. Each signature block has new ink compared with the unsigned fill.

It writes the signed file's SHA-256 so the packet uploads exactly this file.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from _lib import load_json, require_pypdf, sha256_file, utc_now, write_json
from _signature import page_sizes, signature_crops


SCRIPTS = Path(__file__).resolve().parent


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def text_layer_check(reader: Any, answers: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    text = normalized(" ".join(page.extract_text() or "" for page in reader.pages))
    found, missing = [], []
    for answer in answers:
        value = str(answer["expected_value"])
        if value.startswith("/"):
            # Checkbox states have no text; the rendered page is the only evidence.
            missing.append(answer["pdf_field"])
            continue
        (found if normalized(value) in text else missing).append(answer["pdf_field"])
    return found, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--signed", required=True, help="PDF the applicant signed")
    parser.add_argument("--filled", required=True, help="unsigned output of fill-form.py")
    parser.add_argument("--answers", required=True, help="answers-used.json from fill-form.py")
    parser.add_argument("--field-map", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--min-ink", type=float, default=0.01, help="minimum added dark-pixel fraction")
    parser.add_argument(
        "--visually-confirmed",
        action="append",
        default=[],
        metavar="BLOCK_ID",
        help="signature block the applicant and agent confirmed by eye after the ink check missed it",
    )
    args = parser.parse_args()

    pypdf = require_pypdf()
    signed = Path(args.signed)
    filled = Path(args.filled)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    answers_document = load_json(args.answers)
    field_map = load_json(args.field_map)
    errors: list[str] = []
    missing_signatures: list[str] = []

    signed_sha = sha256_file(signed)
    filled_sha = sha256_file(filled)
    if answers_document.get("output_sha256") not in (None, filled_sha):
        errors.append("the unsigned fill does not match answers-used.json; re-run fill-form.py")
    if answers_document.get("form_id") != field_map.get("form_id"):
        errors.append("answers-used.json and the field map name different forms")
    if signed_sha == filled_sha:
        print("ERROR: the signed file is identical to the unsigned fill; nothing was signed")
        return 2

    filled_reader = pypdf.PdfReader(str(filled))
    signed_reader = pypdf.PdfReader(str(signed))
    filled_sizes = page_sizes(filled_reader)
    signed_sizes = page_sizes(signed_reader)
    if len(signed_sizes) != len(filled_sizes):
        errors.append(f"page count changed: unsigned {len(filled_sizes)}, signed {len(signed_sizes)}")

    answers = answers_document["answers"]
    signed_fields = signed_reader.get_fields() or {}
    value_check: dict[str, Any]
    if signed_fields:
        verification = output_dir / "verify-form.json"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "verify-form.py"),
                "--pdf",
                str(signed),
                "--answers",
                str(Path(args.answers)),
                "--output",
                str(verification),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        value_check = {"mode": "form_fields", "verify_form_report": str(verification.resolve())}
        if result.returncode != 0:
            errors.append("filled values changed after signing:\n" + result.stdout.strip())
    else:
        found, missing = text_layer_check(signed_reader, answers)
        value_check = {
            "mode": "flattened_or_scanned",
            "found_in_text_layer": found,
            "compare_visually": missing,
            "note": "Fields are gone (flattened or scanned). Compare every listed value on the rendered signed pages with the unsigned preview.",
        }

    blocks = field_map.get("signature_blocks") or []
    block_results: list[dict[str, Any]] = []
    if blocks and len(signed_sizes) == len(filled_sizes):
        with tempfile.TemporaryDirectory(prefix="unsigned-crops-") as scratch:
            before = {
                item["id"]: item
                for item in signature_crops(filled, blocks, filled_sizes, None, Path(scratch))
            }
            after = signature_crops(
                signed, blocks, signed_sizes, filled_sizes, output_dir / "signature-crops"
            )
        for item in after:
            if "error" in item:
                errors.append(f"{item['id']}: {item['error']}")
                continue
            added = item["dark_fraction"] - before[item["id"]]["dark_fraction"]
            item["unsigned_dark_fraction"] = before[item["id"]]["dark_fraction"]
            item["added_ink"] = round(added, 5)
            item["ink_detected"] = added >= args.min_ink
            item["visually_confirmed"] = item["id"] in args.visually_confirmed
            if item["kind"] == "signature" and not (item["ink_detected"] or item["visually_confirmed"]):
                missing_signatures.append(item["id"])
            block_results.append(item)
    elif not blocks:
        errors.append("field map has no signature_blocks; locate the signature lines before using this check")

    preview_dir = output_dir / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, str(SCRIPTS / "render-preview.py"), "--pdf", str(signed), "--output-dir", str(preview_dir)],
        check=True,
        stdout=subprocess.DEVNULL,
    )

    if errors:
        status = "fail"
    elif missing_signatures:
        status = "signature_missing"
    else:
        status = "signed_verified"
    report = {
        "schema_version": "1.0.0",
        "checked_at": utc_now(),
        "form_id": field_map.get("form_id"),
        "field_map_version": field_map.get("field_map_version"),
        "unsigned_pdf": str(filled.resolve()),
        "unsigned_sha256": filled_sha,
        "signed_pdf": str(signed.resolve()),
        "signed_sha256": signed_sha,
        "signed_bytes": signed.stat().st_size,
        "pages": len(signed_sizes),
        "signed_by": "applicant; the agent never applies a signature",
        "value_check": value_check,
        "signature_blocks": block_results,
        "missing_signatures": missing_signatures,
        "previews": str(preview_dir.resolve()),
        "errors": errors,
        "status": status,
        "visual_status": "manual_review_required",
        "packet_instruction": "Upload only the file with signed_sha256. Re-run this check if the file changes.",
    }
    write_json(output_dir / "signed-verification.json", report)
    for error in errors:
        print(f"ERROR: {error}")
    if missing_signatures:
        print(f"MISSING SIGNATURE: {', '.join(missing_signatures)}")
    print(f"{status}: {signed_sha} -> {output_dir / 'signed-verification.json'}")
    if errors:
        return 1
    if missing_signatures:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
