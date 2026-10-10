#!/usr/bin/env python3
"""Evals for the permit-drawings hand-off (references/plan-sheets.md).

Every name, address and number in the fixtures is fictional. The PDFs are made in a
temporary folder, so the plugin ships no PDF.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from _schema import validate_instance  # noqa: E402


SCHEMA_PATH = ROOT / "schemas" / "permit-drawings-handoff.schema.json"
# The schema is a byte-identical copy of the one permit-drawings ships
# (skills/shared/permit-drawings/schemas/city-plugin-handoff.schema.json).
# Change this pin only when that schema changes in the same release.
SCHEMA_SHA256 = "0a426a57962a4187188f568e5ac20c62137edff86668ea65bb109758ad98ad80"
SCHEMA_ID = "crossbeam.permit-drawings-handoff/1"
PROVENANCE = "permit-drawings project.json"
ARCH_D = (2592, 1728)  # 36 x 24 in, in points
LETTER = (612, 792)


def load(path: Path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def errors(document) -> list[str]:
    return validate_instance(document, load(SCHEMA_PATH))


def make_pdf(path: Path, pages: int, size: tuple[int, int]) -> None:
    from pypdf import PdfWriter

    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=size[0], height=size[1])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as stream:
        writer.write(stream)


def check_schema_copy() -> None:
    schema = load(SCHEMA_PATH)
    if sha256(SCHEMA_PATH) != SCHEMA_SHA256:
        raise AssertionError(
            "schemas/permit-drawings-handoff.schema.json differs from the pinned permit-drawings schema; "
            "copy it unchanged from permit-drawings and update the pin in the same release"
        )
    if schema.get("$id") != SCHEMA_ID:
        raise AssertionError(f"schema id is {schema.get('$id')!r}, expected {SCHEMA_ID!r}")


def check_fixtures_valid() -> None:
    for name in ("drawn-set.json", "city-documents.json"):
        found = errors(load(HERE / name))
        if found:
            raise AssertionError(f"{name} should be valid: {found}")


def resubmittal(drawn: dict) -> dict:
    doc = copy.deepcopy(drawn)
    doc["city_round"] = 1
    doc["files"][0]["replaces"] = {"city_round": 0, "path": "test-set.pdf", "category": "Plans"}
    doc["files"][1]["upload"] = False
    doc["corrections_answered"] = {
        "answers_city_round": 0,
        "city_documents": "input/city/after-round-0/city-documents.json",
        "response_sheet": "response-sheet.pdf",
    }
    doc["comments_for_plugin"] = [
        {"number": "3", "text": "Provide the valuation on the application.",
         "planned_change": "Ask the applicant to confirm the valuation and enter it on the application."}
    ]
    return doc


def check_resubmittal_valid() -> None:
    found = errors(resubmittal(load(HERE / "drawn-set.json")))
    if found:
        raise AssertionError(f"resubmittal bundle should be valid: {found}")


def check_broken_refused() -> None:
    drawn = load(HERE / "drawn-set.json")
    city = load(HERE / "city-documents.json")
    cases = []

    def case(name, base, change):
        doc = copy.deepcopy(base)
        change(doc)
        cases.append((name, doc))

    case("wrong gate", drawn, lambda d: d.__setitem__("gate", "CONSTRUCTION"))
    case("wrong kind", drawn, lambda d: d.__setitem__("kind", "plans"))
    case("unknown schema id", drawn, lambda d: d.__setitem__("schema", "crossbeam.permit-drawings-handoff/2"))
    case("path leaves the bundle", drawn, lambda d: d["files"][0].__setitem__("path", "../outside.pdf"))
    case("bad hash", drawn, lambda d: d["files"][0].__setitem__("sha256", "XYZ"))
    case("upload flag missing", drawn, lambda d: d["files"][0].pop("upload"))
    case("locked plan set", drawn, lambda d: d["plan_set"].__setitem__("unlocked", False))
    case("plan set failed kit QA", drawn, lambda d: d["plan_set"].__setitem__("kit_qa_pass", False))
    case("assumed value without FV tag", drawn, lambda d: d["facts"][5].__setitem__("fv", None))
    case("unknown fact given a value", drawn, lambda d: d["facts"][6].__setitem__("value", "000-000-00"))
    case("unknown fact without a reason", drawn, lambda d: d["facts"][6].__setitem__("null_reason", None))
    case("verified fact with a null value", drawn, lambda d: d["facts"][0].__setitem__("value", None))
    case(
        "sheet item not decided in stage 7",
        drawn,
        lambda d: d["open_items"][0].__setitem__("owner_decision", {"status": "pending", "words": None, "log": None}),
    )
    case("approval this skill does not own", drawn,
         lambda d: d["approvals_done"].append({"approval": "final_submit", "log": "x", "date": "2026-10-01"}))
    case("unknown plugin task", drawn, lambda d: d.__setitem__("left_to_plugin", ["stamp_drawings"]))
    case("no city documents", city, lambda d: d.__setitem__("documents", []))
    case("unknown outcome", city, lambda d: d.__setitem__("outcome", "maybe"))

    for name, doc in cases:
        if not errors(doc):
            raise AssertionError(f"schema accepted a broken bundle: {name}")


def build_bundle(work: Path) -> Path:
    """Write the fixture bundle with real files, as permit-drawings stage 8 would."""
    folder = work / "package" / "round-0" / "handoff"
    make_pdf(folder / "test-set.pdf", 3, ARCH_D)
    make_pdf(folder / "energy-report.pdf", 2, LETTER)
    dump(folder / "project.json", {"note": "fictional project file for the hand-off eval"})
    handoff = load(HERE / "drawn-set.json")
    for item in handoff["files"]:
        path = folder / item["path"]
        item["sha256"] = sha256(path)
        item["bytes"] = path.stat().st_size
    plan = folder / handoff["plan_set"]["path"]
    handoff["plan_set"]["sha256"] = sha256(plan)
    handoff["project_file"]["sha256"] = sha256(folder / "project.json")
    dump(folder / "handoff.json", handoff)
    return folder / "handoff.json"


def take_bundle(handoff_path: Path, work: Path) -> dict:
    """Run the mechanical checks in plan-sheets.md section 3, steps 1 to 3."""
    from pypdf import PdfReader

    handoff = load(handoff_path)
    found = errors(handoff)
    if found:
        raise AssertionError(f"bundle invalid: {found}")
    if handoff["city"]["jurisdiction_id"] != "laguna-beach-ca":
        raise AssertionError("bundle is for another jurisdiction")
    folder = handoff_path.parent
    hashes = set()
    for item in handoff["files"]:
        path = folder / item["path"]
        if not path.is_file():
            raise AssertionError(f"bundle file missing: {item['path']}")
        if sha256(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            raise AssertionError(f"bundle file changed: {item['path']}")
        hashes.add(item["sha256"])
    plan = handoff["plan_set"]
    if plan["sha256"] not in hashes:
        raise AssertionError("plan_set is not one of the bundle files")
    reader = PdfReader(str(folder / plan["path"]))
    if reader.is_encrypted or len(reader.pages) != plan["pages"]:
        raise AssertionError("plan set is locked or has the wrong page count")
    if sha256(folder / handoff["project_file"]["path"]) != handoff["project_file"]["sha256"]:
        raise AssertionError("project.json changed")

    target = work / "input" / "plans" / "permit-drawings" / f"round-{handoff['city_round']}"
    target.mkdir(parents=True, exist_ok=True)
    for name in [item["path"] for item in handoff["files"]] + [handoff["project_file"]["path"], "handoff.json"]:
        shutil.copy2(folder / name, target / name)
        if sha256(target / name) != sha256(folder / name):
            raise AssertionError(f"copy changed {name}")
    return {"handoff": handoff, "copied_to": target, "handoff_sha256": sha256(handoff_path)}


def record_facts(taken: dict, fact_map: dict[str, str], work: Path) -> dict:
    """Write state/project-facts.json from the bundle, with the provenance plan-sheets.md asks for.

    The id mapping is the agent's judgment, given here as a fixture.
    """
    handoff = taken["handoff"]
    copied_project = (taken["copied_to"] / handoff["project_file"]["path"]).relative_to(work)
    facts = []
    for item in handoff["facts"]:
        plugin_id = fact_map.get(item["id"])
        if plugin_id is None:
            continue
        notes = []
        if item["value"] is None:
            notes.append(f"null in the drawn set: {item['null_reason']}")
        if item["status"] == "ASSUMED":
            notes.append(f"assumed, field verify {item['fv']}")
        source = None
        if item["source"] is not None:
            source = {
                "kind": "plan",
                "receipt": {
                    "kind": "file",
                    "captured_at": now(),
                    "file": str(copied_project),
                    "page": None,
                    "sheet": item["on_sheets"][0] if item["on_sheets"] else None,
                    "field": item["source"]["pointer"],
                    "record_id": None,
                    "note": f"{PROVENANCE}, status {item['status']}, handoff sha256 {taken['handoff_sha256']}",
                },
            }
        controlled = item["applicant_controlled"]
        facts.append({
            "id": plugin_id,
            "value": item["value"],
            "source": source,
            "confidence": 0 if item["value"] is None else (0.6 if item["status"] == "ASSUMED" else 1),
            "confirmation": {
                "required": controlled,
                "status": "pending" if controlled else "not_required",
                "confirmed_at": None,
                "note": "confirm the drawn-set value with the applicant" if controlled else None,
            },
            "consumers": [],
            "conflicts": [],
            "notes": notes,
        })
    document = {
        "schema_version": "1.0.0",
        "run_id": "handoff-eval-001",
        "jurisdiction": "laguna-beach-ca",
        "created_at": now(),
        "updated_at": now(),
        "facts": facts,
    }
    dump(work / "state" / "project-facts.json", document)
    return document


def check_round_trip() -> None:
    fact_map = load(HERE / "fact-map.json")["map"]
    with tempfile.TemporaryDirectory(prefix="laguna-handoff-evals-") as directory:
        work = Path(directory) / "permit-work"
        handoff_path = build_bundle(work)
        taken = take_bundle(handoff_path, work)

        # A file changed after its hash went in the bundle is refused.
        tampered = Path(directory) / "tampered"
        shutil.copytree(handoff_path.parent, tampered)
        (tampered / "energy-report.pdf").write_bytes(b"%PDF-1.4\n% changed\n")
        try:
            take_bundle(tampered / "handoff.json", Path(directory) / "other-work")
        except AssertionError:
            pass
        else:
            raise AssertionError("a changed bundle file was accepted")

        facts = record_facts(taken, fact_map, work)
        found = validate_instance(facts, load(ROOT / "schemas" / "project-facts.schema.json"))
        if found:
            raise AssertionError(f"project facts invalid: {found}")
        by_id = {item["id"]: item for item in facts["facts"]}
        address = by_id["site.address"]
        if PROVENANCE not in address["source"]["receipt"]["note"] or address["source"]["kind"] != "plan":
            raise AssertionError("drawn-set fact lost its provenance")
        if by_id["site.apn"]["value"] is not None or by_id["site.apn"]["source"] is not None:
            raise AssertionError("an unknown fact was filled in")
        valuation = by_id["project.valuation.residential"]
        if valuation["value"] is not None or valuation["confirmation"]["status"] != "pending":
            raise AssertionError("a valuation was invented or not left for the applicant")
        owner = by_id["owner.name"]
        if not owner["confirmation"]["required"] or owner["confirmation"]["status"] != "pending":
            raise AssertionError("an applicant-controlled fact was not left pending")
        if any(item["id"] == "area.wall_t" for item in facts["facts"]):
            raise AssertionError("an unmapped drawing value was written as a City fact")

        # City corrections go back as a valid city_documents bundle with real hashes.
        after = work / "input" / "city" / "after-round-0"
        make_pdf(after / "corrections-letter.pdf", 1, LETTER)
        city = load(HERE / "city-documents.json")
        city["documents"][0]["sha256"] = sha256(after / "corrections-letter.pdf")
        city["documents"][0]["bytes"] = (after / "corrections-letter.pdf").stat().st_size
        city["original_submittal"]["uploaded_files"][0]["sha256"] = taken["handoff"]["plan_set"]["sha256"]
        dump(after / "city-documents.json", city)
        found = errors(load(after / "city-documents.json"))
        if found:
            raise AssertionError(f"city documents bundle invalid: {found}")
        if not (work / city["original_submittal"]["drawn_set"]).is_file():
            raise AssertionError("original_submittal.drawn_set does not name the filed bundle")

        # The resubmittal uploads only what changed, into the original slot.
        resubmit = resubmittal(taken["handoff"])
        found = errors(resubmit)
        if found:
            raise AssertionError(f"resubmittal invalid: {found}")
        uploads = [item for item in resubmit["files"] if item["upload"]]
        if [item["path"] for item in uploads] != ["test-set.pdf"] or uploads[0]["replaces"]["category"] != "Plans":
            raise AssertionError("resubmittal upload plan is wrong")


def check_reference() -> None:
    text = (ROOT / "references" / "plan-sheets.md").read_text(encoding="utf-8")
    needed = [
        "requirements/plan-sheet-matrix",
        "crossbeam_get_skill",
        "connect CrossBeam and use permit drawings from the CrossBeam app",
        "schemas/permit-drawings-handoff.schema.json",
        "permit-drawings project.json",
        "A `null` value stays `null`",
        "Business and Professions",
        "Ask each approval once, on one side.",
        "Upload the plan PDF byte for byte.",
        "city-documents.json",
    ]
    missing = [item for item in needed if item not in text]
    if missing:
        raise AssertionError(f"references/plan-sheets.md is missing: {missing}")
    if text.count("licensed architect or engineer") > 2:
        raise AssertionError("say the licensed-professional rule once")


def main() -> int:
    checks = [
        ("hand-off schema is the pinned permit-drawings copy", check_schema_copy),
        ("fictional drawn-set and city-documents bundles validate", check_fixtures_valid),
        ("fictional resubmittal bundle validates", check_resubmittal_valid),
        ("broken bundles are refused", check_broken_refused),
        ("bundle files, facts provenance and corrections round trip", check_round_trip),
        ("plan-sheets reference names the contract", check_reference),
    ]
    for name, check in checks:
        check()
        print(f"PASS {name}")
    print("All permit-drawings hand-off evals passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
