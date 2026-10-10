#!/usr/bin/env python3
"""Round-trip evals for the pinned form maps and the sign-before-upload step.

The Building Permit Application runs the full fill -> verify -> render -> sign cases.
Every other Planning map in PLANNING_ROUND_TRIP runs fill -> verify with a value for
every mapped fact. A form with no fillable fields must refuse to fill.

Default mode needs no City PDF. It builds a replica of the pinned form from the map's
own field tree (same names, types, pages, and rectangles), so CI exercises the exact map.
With --forms-dir it runs the same cases against the official PDFs the user downloaded.

Every fact here is fictional.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
FORM_ID = "building-application"
# Planning maps pinned 2026-10-10 that round-trip on every run. sign-permit-application
# is pinned too, but the City form has no fields, so it must refuse to fill instead.
PLANNING_ROUND_TRIP = (
    "adu-application",
    "lot-line-adjustment-application",
    "revocable-encroachment-permit-application",
    "sb-9-application",
    "temporary-use-permit-application",
)
FLAT_FORMS = ("sign-permit-application",)
sys.path.insert(0, str(SCRIPTS))

from _schema import validate_instance  # noqa: E402


def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def run(*arguments: str, expected: int | None = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [sys.executable, *arguments],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if expected is not None and result.returncode != expected:
        raise AssertionError(
            f"returned {result.returncode}, expected {expected}: {' '.join(arguments)}\n{result.stdout}"
        )
    return result


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


FICTIONAL = {
    "application.date": "10/09/2026",
    "site.address": "123 Test Avenue, Laguna Beach, CA 92651",
    "project.description.residential": "Fictional eval: replace kitchen cabinets and add one window in an existing single-family dwelling.",
    "applicant.name": "Alex Applicant",
    "applicant.phone": "949-555-0100",
    "applicant.email": "alex@example.invalid",
    "owner.name": "Olivia Owner",
    "owner.phone": "949-555-0101",
    "owner.email": "owner@example.invalid",
    "owner.mailing_address": "123 Test Avenue, Laguna Beach, CA 92651",
    "contractor.license_name": "Example Builders Inc",
    "contractor.dba": "Example Builders",
    "contractor.license_number": "0000000",
    "contractor.license_class": "B",
    "contractor.phone": "949-555-0102",
    "contractor.email": "builder@example.invalid",
    "contractor.mailing_address": "1 Example Way, Irvine, CA 92618",
    "building.residential.alteration_or_repair": "Alteration",
    "building.commercial.alteration_or_repair": "Repair",
    "stormwater_certification.certifier_name": "Alex Applicant",
    "stormwater_certification.certifier_address": "123 Test Avenue, Laguna Beach, CA 92651",
    "stormwater_certification.certifier_phone": "949-555-0100",
    "stormwater_certification.certifier_email": "alex@example.invalid",
}


def fact(fact_id: str, value, *, controlled: bool, source_kind: str | None = None) -> dict:
    kind = source_kind or ("user_confirmed" if controlled else "plan")
    return {
        "id": fact_id,
        "value": value,
        "source": {
            "kind": kind,
            "receipt": {
                "kind": "user_answer" if kind == "user_confirmed" else "file",
                "captured_at": now(),
                "file": None if kind == "user_confirmed" else "fictional-plans.pdf",
                "page": None,
                "sheet": None,
                "field": None,
                "record_id": "residential",
                "note": "fictional form eval",
            },
        },
        "confidence": 1,
        "confirmation": {
            "required": controlled or kind == "user_confirmed",
            "status": "confirmed" if (controlled or kind == "user_confirmed") else "not_required",
            "confirmed_at": now() if (controlled or kind == "user_confirmed") else None,
            "note": "fictional form eval",
        },
        "consumers": [],
        "conflicts": [],
        "notes": ["Fictional; not for submission"],
    }


def value_for(mapping: dict, fact_id: str):
    if fact_id in FICTIONAL:
        return FICTIONAL[fact_id]
    if mapping["transform"] == "checkbox":
        return True
    if mapping["transform"] == "currency":
        return 25000
    if mapping["transform"] == "lines":
        return "Fictional eval description."
    return "12"


def facts_for(field_map: dict, case: dict) -> dict:
    facts: list[dict] = []
    seen: set[str] = set()
    for mapping in field_map["canonical_mappings"]:
        fact_id = mapping["fact_id"].replace("{record_id}", "residential")
        if fact_id in seen:
            continue
        seen.add(fact_id)
        facts.append(fact(fact_id, value_for(mapping, fact_id), controlled=bool(mapping.get("applicant_controlled"))))
    if case.get("permittee_type") is not None:
        facts.append(
            fact(
                "permittee.type",
                case["permittee_type"],
                controlled=True,
                source_kind=case.get("declaration_source"),
            )
        )
    return {
        "schema_version": "1.0.0",
        "run_id": f"form-eval-{case['id']}",
        "jurisdiction": "laguna-beach-ca",
        "created_at": now(),
        "updated_at": now(),
        "facts": facts,
    }


def build_replica(field_map: dict, destination: Path) -> None:
    """Recreate the pinned form's field tree so CI can fill the exact map without the City PDF."""

    from reportlab.lib.colors import transparent
    from reportlab.pdfgen import canvas

    page_count = max(widget["page"] for widget in field_map["widgets"])
    pdf = canvas.Canvas(str(destination), pagesize=(612, 792))
    form = pdf.acroForm
    for page in range(1, page_count + 1):
        pdf.setFont("Helvetica", 8)
        pdf.drawString(36, 770, f"Replica of {field_map['form_id']} for evals, page {page}")
        for block in field_map.get("signature_blocks") or []:
            if block["page"] == page:
                x0, y0, x1, _ = block["rect"]
                pdf.line(x0, y0, x1, y0)
                pdf.drawString(x0, y0 - 9, block["label"])
        for widget in field_map["widgets"]:
            if widget["page"] != page:
                continue
            x0, y0, x1, y1 = widget["rect"]
            if widget["field_type"] == "/Btn":
                form.checkbox(name=widget["field_name"], x=x0, y=y0, size=min(x1 - x0, y1 - y0), buttonStyle="check")
            else:
                form.textfield(
                    name=widget["field_name"], x=x0, y=y0, width=x1 - x0, height=y1 - y0,
                    borderWidth=0, fontSize=7, fillColor=transparent,
                )
        pdf.showPage()
    pdf.save()


def replica_map(field_map: dict, replica: Path) -> dict:
    from pypdf import PdfReader

    reader = PdfReader(str(replica))
    states = {}
    for page in reader.pages:
        for reference in page.get("/Annots") or []:
            widget = reference.get_object()
            appearance = widget.get("/AP")
            if appearance is not None and "/N" in appearance:
                names = [str(name) for name in appearance["/N"].keys() if str(name) != "/Off"]
                if names:
                    states[str(widget.get("/T"))] = names[0]
    copied = copy.deepcopy(field_map)
    copied["source_sha256"] = hashlib.sha256(replica.read_bytes()).hexdigest()
    for mapping in copied["canonical_mappings"]:
        if mapping["transform"] == "checkbox":
            mapping["on_value"] = states[mapping["pdf_fields"][0]]
    return copied


def contractor_targets(field_map: dict) -> set[str]:
    return {
        name
        for mapping in field_map["canonical_mappings"]
        if mapping.get("only_when")
        for name in mapping.get("pdf_fields") or []
    }


def check_map_contract(field_map: dict, manifest: dict) -> None:
    form = next(item for item in manifest["forms"] if item["id"] == FORM_ID)
    assert form["status"] == "pinned" and form["pages"] == 2
    assert form["url"].startswith("https://gis.lagunabeachcity.net/"), form["url"]
    assert form["source_receipt"]["linked_from"], "Building form needs its portal link receipt"
    assert field_map["field_map_version"] == form["field_map_version"]
    assert field_map["required_declarations"] == ["permittee.type"]

    names = {item["name"] for item in field_map["fields"]}
    targeted = {name for mapping in field_map["canonical_mappings"] for name in mapping.get("pdf_fields") or []}
    blocks = field_map["signature_blocks"]
    assert {block["kind"] for block in blocks} >= {"signature"}
    assert sum(block["kind"] == "signature" for block in blocks) == 2, "page 1 and stormwater signatures"
    for block in blocks:
        if block["pdf_field"]:
            assert block["pdf_field"] in names and block["pdf_field"] in field_map["review_fields"]
            assert block["pdf_field"] not in targeted, f"signature field is mapped: {block['pdf_field']}"
    stormwater = {"I", "at", "Text35", "Address", "Text36", "Text33"}
    assert stormwater <= targeted, sorted(stormwater - targeted)
    contractor = [m for m in field_map["canonical_mappings"] if m["fact_id"].startswith("contractor.")]
    assert len(contractor) == 7
    assert all(m.get("only_when") == {"fact_id": "permittee.type", "equals": "licensed_contractor"} for m in contractor)
    assert all(m["applicant_controlled"] for m in contractor)

    retired = {item["sha256"] for item in manifest.get("retired_forms") or []}
    assert form["sha256"] not in retired
    pinned_ids = {item["id"] for item in manifest["forms"]}
    for pending in manifest.get("pending_sources") or []:
        assert pending["status"] == "needs_source" and pending["url"].startswith("https://")
        assert pending["id"] not in pinned_ids
    for item in manifest["forms"]:
        item_map = load(ROOT / "assets/field-maps" / f"{item['id']}.json")
        assert item_map.get("status", "pinned") == item["status"], item["id"]
        if item["status"] != "pinned":
            assert item["current_source"]["url"].startswith("https://"), item["id"]


def check_needs_source_refusal(temp: Path, source: Path) -> None:
    """A map marked needs_source refuses to fill and names the City link it is waiting on.

    No shipped map is needs_source today, so the case marks a copy of a pinned map.
    """

    facts = temp / "empty-facts.json"
    dump(facts, {"schema_version": "1.0.0", "run_id": "x", "jurisdiction": "laguna-beach-ca", "created_at": now(), "updated_at": now(), "facts": []})
    stale = load(ROOT / "assets/field-maps/adu-application.json")
    stale["status"] = "needs_source"
    stale["status_note"] = "The City links document 99999; download, pin, and remap it before filling."
    stale_path = temp / "needs-source-map.json"
    dump(stale_path, stale)
    result = run(
        str(SCRIPTS / "fill-form.py"), "--input", str(source), "--facts", str(facts),
        "--field-map", str(stale_path),
        "--output", str(temp / "needs-source-must-not-exist.pdf"), expected=1,
    )
    assert "needs_source" in result.stdout and "99999" in result.stdout, result.stdout
    assert not (temp / "needs-source-must-not-exist.pdf").exists()


def planning_value(mapping: dict, fact_id: str):
    if mapping["transform"] in {"checkbox", "yes_no"}:
        return True
    if mapping["transform"] == "lines":
        return "Fictional eval description for a form map round trip."
    if mapping["transform"] == "currency":
        return 1000
    return f"Eval {fact_id.rsplit('.', 1)[-1]}"


def planning_facts(field_map: dict) -> dict:
    facts: list[dict] = []
    seen: set[str] = set()
    for mapping in field_map["canonical_mappings"]:
        fact_id = mapping["fact_id"]
        if fact_id in seen:
            continue
        seen.add(fact_id)
        facts.append(fact(fact_id, planning_value(mapping, fact_id), controlled=bool(mapping.get("applicant_controlled"))))
    return {
        "schema_version": "1.0.0",
        "run_id": f"form-eval-{field_map['form_id']}",
        "jurisdiction": "laguna-beach-ca",
        "created_at": now(),
        "updated_at": now(),
        "facts": facts,
    }


def check_planning_map_contract(form_id: str, field_map: dict, form: dict) -> None:
    assert form["status"] == "pinned" and form["redistribution"] == "fetch_only", form_id
    assert form["url"].startswith("https://www.lagunabeachcity.net/home/showpublisheddocument/"), form_id
    assert form["url"].endswith(f"/{form['document_id']}/{form['ticks']}"), form_id
    receipt = form["source_receipt"]
    assert receipt["http_status"] == 200 and receipt["linked_from"], form_id
    assert all(item["url"].startswith("https://www.lagunabeachcity.net/") for item in receipt["linked_from"])
    assert field_map["source_sha256"] == form["sha256"] and field_map["field_map_version"] == form["field_map_version"]
    signature_fields = {item["name"] for item in field_map["fields"] if item["type"] == "/Sig"}
    targeted = {name for mapping in field_map["canonical_mappings"] for name in mapping.get("pdf_fields") or []}
    targeted |= {widget["field_name"] for mapping in field_map["canonical_mappings"] for widget in mapping.get("pdf_widgets") or []}
    assert not signature_fields & targeted, (form_id, sorted(signature_fields & targeted))
    assert signature_fields <= set(field_map["review_fields"]), form_id
    assert not any(mapping["fact_id"].startswith(f"form.{form_id}.field.") for mapping in field_map["canonical_mappings"]), form_id
    for section in field_map.get("manual_sections") or []:
        assert section["title"] and all(1 <= page <= form["pages"] for page in section["pages"]), form_id


def official_source(forms_dir: str, form: dict) -> Path:
    run(
        str(SCRIPTS / "check-source-freshness.py"), "--manifest", str(ROOT / "assets/form-manifest.json"),
        "--forms-dir", forms_dir, "--only", form["id"],
    )
    source = Path(forms_dir) / form["cache_name"]
    return source if source.is_file() else Path(forms_dir) / form["download_name"]


def run_planning_round_trips(manifest: dict, temp: Path, forms_dir: str | None) -> list[str]:
    forms = {item["id"]: item for item in manifest["forms"]}
    passed: list[str] = []
    for form_id in PLANNING_ROUND_TRIP:
        form = forms[form_id]
        field_map = load(ROOT / "assets/field-maps" / f"{form_id}.json")
        check_planning_map_contract(form_id, field_map, form)
        work = temp / form_id
        work.mkdir(parents=True, exist_ok=True)
        if forms_dir:
            source, map_path, active_map = official_source(forms_dir, form), ROOT / "assets/field-maps" / f"{form_id}.json", field_map
        else:
            source = work / f"replica-{form_id}.pdf"
            build_replica(field_map, source)
            active_map = replica_map(field_map, source)
            map_path = work / "replica-field-map.json"
            dump(map_path, active_map)
        facts_document = planning_facts(active_map)
        assert not validate_instance(facts_document, load(ROOT / "schemas/project-facts.schema.json"))
        facts_path = work / "project-facts.json"
        dump(facts_path, facts_document)
        output = work / f"{form_id}-filled.pdf"
        run(
            str(SCRIPTS / "fill-form.py"), "--input", str(source), "--facts", str(facts_path),
            "--field-map", str(map_path), "--output", str(output),
        )
        answers = output.with_name(output.stem + ".answers-used.json")
        run(str(SCRIPTS / "verify-form.py"), "--pdf", str(output), "--answers", str(answers))
        expected_targets = sum(
            len(mapping.get("pdf_fields") or mapping.get("pdf_widgets") or [])
            for mapping in active_map["canonical_mappings"]
            if mapping["transform"] != "lines"
        )
        filled = [item for item in load(answers)["answers"]]
        single = [item for item in filled if not any(
            m["transform"] == "lines" and m["fact_id"] == item["fact_id"] for m in active_map["canonical_mappings"]
        )]
        assert len(single) == expected_targets, (form_id, len(single), expected_targets)
        unresolved = load(output.with_name(output.stem + ".unresolved-fields.json"))["unresolved"]
        assert not unresolved, (form_id, unresolved)
        sign_sheet = load(output.with_name(output.stem + ".review-and-sign.json"))
        assert sign_sheet["manual_sections"] == (field_map.get("manual_sections") or []), form_id
        passed.append(form_id)

    for form_id in FLAT_FORMS:
        form = forms[form_id]
        field_map = load(ROOT / "assets/field-maps" / f"{form_id}.json")
        assert form["status"] == "pinned" and form["canonical_fields"] == 0 and form["widgets"] == 0, form_id
        assert not field_map["canonical_mappings"] and field_map["manual_sections"], form_id
        # The refusal comes before any checksum check, so any PDF stands in for the replica.
        source = official_source(forms_dir, form) if forms_dir else temp / "adu-application" / "replica-adu-application.pdf"
        facts = temp / "empty-facts.json"
        dump(facts, {"schema_version": "1.0.0", "run_id": "x", "jurisdiction": "laguna-beach-ca", "created_at": now(), "updated_at": now(), "facts": []})
        result = run(
            str(SCRIPTS / "fill-form.py"), "--input", str(source), "--facts", str(facts),
            "--field-map", str(ROOT / "assets/field-maps" / f"{form_id}.json"),
            "--output", str(temp / f"{form_id}-must-not-exist.pdf"), expected=1,
        )
        assert "no fillable fields" in result.stdout and "pages [3]" in result.stdout, result.stdout
        assert not (temp / f"{form_id}-must-not-exist.pdf").exists()
        passed.append(f"{form_id} (flat: refuses to fill)")
    return passed


def draw_ink_overlay(field_map: dict, destination: Path) -> None:
    from reportlab.pdfgen import canvas

    pages = max(widget["page"] for widget in field_map["widgets"])
    pdf = canvas.Canvas(str(destination), pagesize=(612, 792))
    for page in range(1, pages + 1):
        for block in field_map["signature_blocks"]:
            if block["page"] != page:
                continue
            x0, y0, x1, y1 = block["rect"]
            pdf.setStrokeColorRGB(0.05, 0.05, 0.35)
            if block["kind"] == "signature":
                pdf.setLineWidth(2.2)
                for offset in (0.25, 0.45, 0.65):
                    path = pdf.beginPath()
                    path.moveTo(x0 + 8, y0 + (y1 - y0) * offset)
                    path.curveTo(x0 + 60, y1 - 1, x0 + 110, y0 + 1, (x0 + x1) / 2 + 40, y0 + (y1 - y0) * (1 - offset))
                    pdf.drawPath(path)
            else:
                pdf.setFont("Helvetica", 10)
                pdf.drawString(x0 + 4, y0 + 5, "10/09/2026")
        pdf.showPage()
    pdf.save()


def make_signed_variant(variant: str, filled: Path, field_map: dict, temp: Path) -> Path:
    from pypdf import PdfReader, PdfWriter

    destination = temp / f"signed-{variant}.pdf"
    if variant == "identical":
        shutil.copyfile(filled, destination)
        return destination
    writer = PdfWriter()
    writer.clone_document_from_reader(PdfReader(str(filled)))
    if variant in {"ink_overlay", "tampered", "scanned"}:
        overlay = temp / "ink-overlay.pdf"
        draw_ink_overlay(field_map, overlay)
        for page, ink in zip(writer.pages, PdfReader(str(overlay)).pages):
            page.merge_page(ink)
    if variant == "tampered":
        writer.update_page_form_field_values(None, {"Valuation of Work": "$99,999.00"}, auto_regenerate=False)
    writer.add_metadata({"/Producer": f"form-eval {variant}"})
    with destination.open("wb") as stream:
        writer.write(stream)
    if variant != "scanned":
        return destination

    # A wet-signed scan: raster pages only, no fields and no text layer.
    from reportlab.pdfgen import canvas

    raster_dir = temp / "scan"
    raster_dir.mkdir(exist_ok=True)
    subprocess.run(["pdftoppm", "-png", "-r", "110", str(destination), str(raster_dir / "page")], check=True)
    scanned = temp / "signed-scanned-image.pdf"
    pdf = canvas.Canvas(str(scanned), pagesize=(612, 792))
    for image in sorted(raster_dir.glob("page-*.png")):
        pdf.drawImage(str(image), 0, 0, width=612, height=792)
        pdf.showPage()
    pdf.save()
    return scanned


def run_cases(field_map: dict, source: Path, map_path: Path, temp: Path, cases: dict) -> list[str]:
    schema = load(ROOT / "schemas/project-facts.schema.json")
    contractor_fields = contractor_targets(field_map)
    single_line_targets = {
        name
        for mapping in field_map["canonical_mappings"]
        if mapping["transform"] != "lines"
        for name in mapping.get("pdf_fields") or []
    }
    passed: list[str] = []
    filled_for_signing: Path | None = None
    answers_for_signing: Path | None = None

    for case in cases["fill_cases"]:
        work = temp / case["id"]
        facts_document = facts_for(field_map, case)
        errors = validate_instance(facts_document, schema)
        if case.get("declaration_source") not in (None, "user_confirmed"):
            assert errors, "schema must reject an inferred owner-builder/contractor declaration"
        else:
            assert not errors, errors
        facts_path = work / "project-facts.json"
        dump(facts_path, facts_document)
        output = work / "building-application-filled.pdf"
        run(
            str(SCRIPTS / "fill-form.py"), "--input", str(source), "--facts", str(facts_path),
            "--field-map", str(map_path), "--record-id", "residential", "--output", str(output),
            expected=case["expect_exit"],
        )
        if case["expect_exit"] != 0:
            assert not output.exists()
            unresolved = load(output.with_name(output.stem + ".unresolved-fields.json"))["unresolved"]
            assert any(item["fact_id"] == "permittee.type" and item["required"] for item in unresolved)
            passed.append(case["id"])
            continue
        answers = output.with_name(output.stem + ".answers-used.json")
        run(str(SCRIPTS / "verify-form.py"), "--pdf", str(output), "--answers", str(answers))
        preview = work / "preview"
        run(str(SCRIPTS / "render-preview.py"), "--pdf", str(output), "--output-dir", str(preview), "--dpi", "72", "--field-map", str(map_path))
        manifest = load(preview / "render-manifest.json")
        assert len(manifest["pages"]) == 2 and len(manifest["signature_crops"]) == len(field_map["signature_blocks"])
        filled_fields = {item["pdf_field"] for item in load(answers)["answers"]}
        if case["expect_contractor_filled"]:
            assert contractor_fields <= filled_fields
            assert single_line_targets <= filled_fields, sorted(single_line_targets - filled_fields)
            filled_for_signing, answers_for_signing = output, answers
        else:
            assert not contractor_fields & filled_fields
            skipped = load(output.with_name(output.stem + ".unresolved-fields.json"))["not_applicable"]
            assert {name for item in skipped for name in item["pdf_targets"]} == contractor_fields
        sign_sheet = load(output.with_name(output.stem + ".review-and-sign.json"))
        assert sign_sheet["signature_blocks"] == field_map["signature_blocks"]
        assert sign_sheet["declarations"]["permittee.type"] == case["permittee_type"]
        passed.append(case["id"])

    assert filled_for_signing is not None and answers_for_signing is not None
    for case in cases["sign_cases"]:
        work = temp / case["id"]
        work.mkdir(parents=True, exist_ok=True)
        signed = make_signed_variant(case["variant"], filled_for_signing, field_map, work)
        result = run(
            str(SCRIPTS / "verify-signed-form.py"), "--signed", str(signed), "--filled", str(filled_for_signing),
            "--answers", str(answers_for_signing), "--field-map", str(map_path), "--output-dir", str(work / "check"),
            expected=case["expect_exit"],
        )
        if case["variant"] == "identical":
            assert "identical" in result.stdout
            passed.append(case["id"])
            continue
        report = load(work / "check/signed-verification.json")
        assert report["status"] == case["expect_status"], report
        assert report["signed_sha256"] == hashlib.sha256(signed.read_bytes()).hexdigest()
        if case["expect_status"] == "signed_verified":
            assert not report["missing_signatures"]
            assert all(Path(item["crop_png"]).is_file() for item in report["signature_blocks"])
            assert list((work / "check/previews").glob("page-*.png"))
            if case["variant"] == "scanned":
                assert report["value_check"]["mode"] == "flattened_or_scanned"
                assert report["value_check"]["compare_visually"]
            else:
                assert report["value_check"]["mode"] == "form_fields"
        passed.append(case["id"])
    return passed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forms-dir", help="run against the official PDF in this directory instead of the replica")
    parser.add_argument("--output-dir", help="keep outputs here (default: a temporary directory)")
    args = parser.parse_args()
    if not shutil.which("pdftoppm"):
        raise SystemExit("pdftoppm is required for the form round-trip evals")

    manifest = load(ROOT / "assets/form-manifest.json")
    field_map = load(ROOT / "assets/field-maps" / f"{FORM_ID}.json")
    cases = load(Path(__file__).with_name("cases.json"))
    check_map_contract(field_map, manifest)
    print("PASS building map contract, statuses, and pending sources")

    with tempfile.TemporaryDirectory(prefix="laguna-form-evals-") as scratch:
        temp = Path(args.output_dir) if args.output_dir else Path(scratch)
        temp.mkdir(parents=True, exist_ok=True)
        if args.forms_dir:
            run(
                str(SCRIPTS / "check-source-freshness.py"), "--manifest", str(ROOT / "assets/form-manifest.json"),
                "--forms-dir", args.forms_dir, "--only", FORM_ID,
            )
            form = next(item for item in manifest["forms"] if item["id"] == FORM_ID)
            source = Path(args.forms_dir) / form["cache_name"]
            if not source.is_file():
                source = Path(args.forms_dir) / form["download_name"]
            map_path = ROOT / "assets/field-maps" / f"{FORM_ID}.json"
            active_map = field_map
            label = "official PDF"
        else:
            source = temp / "replica-building-application.pdf"
            build_replica(field_map, source)
            active_map = replica_map(field_map, source)
            map_path = temp / "replica-field-map.json"
            dump(map_path, active_map)
            label = "replica"
        check_needs_source_refusal(temp, source)
        print("PASS needs_source map refuses to fill")
        passed = run_cases(active_map, source, map_path, temp, cases)
        print(f"PASS building round trip on {label}: {', '.join(passed)}")
        planning = run_planning_round_trips(manifest, temp / "planning", args.forms_dir)
        print(f"PASS planning round trips on {label}: {', '.join(planning)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
