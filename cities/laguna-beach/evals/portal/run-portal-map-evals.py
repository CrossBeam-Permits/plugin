#!/usr/bin/env python3
"""Offline evals for the v2 portal map, its freshness check, and the plan builder.

Everything here runs from the pinned snapshot in assets/portal-maps/. Nothing
touches the network. Drift cases mutate a copy of the pinned snapshot and check
that check-portal-freshness.py sorts each change correctly.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from _lib import sha256_file  # noqa: E402
from _portal import compile_map, layout_questions, record_type  # noqa: E402
from _schema import validate_instance  # noqa: E402

MAP_PATH = ROOT / "assets/portal-maps/v2-portal-map.json"
SNAPSHOT_PATH = ROOT / "assets/portal-maps/portal-snapshot.json"
CASES = ROOT / "evals/portal/v2-map-cases.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run(*arguments: str, expected: int = 0) -> str:
    result = subprocess.run([sys.executable, *arguments], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    if result.returncode != expected:
        raise AssertionError(f"{' '.join(arguments)} returned {result.returncode}, expected {expected}\n{result.stdout}")
    return result.stdout


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def klass(portal_map: dict, menu_id: int, label: str) -> dict:
    record = record_type(portal_map, menu_id)
    assert record is not None, menu_id
    found = [item for item in record["workClasses"] if item["label"] == label]
    assert len(found) == 1, (menu_id, label, [item["label"] for item in record["workClasses"]])
    return found[0]


# ------------------------------------------------------------------ map

def check_map_reproduces_from_snapshot() -> None:
    pinned = load(MAP_PATH)
    assert pinned["schema_version"] == "2.0.0"
    assert pinned["source"]["snapshot"] == "assets/portal-maps/portal-snapshot.json"
    assert pinned["source"]["snapshot_sha256"] == sha256_file(SNAPSHOT_PATH), "map was not built from the pinned snapshot"
    rebuilt = compile_map(load(SNAPSHOT_PATH), pinned["source"]["snapshot"], sha256_file(SNAPSHOT_PATH))
    assert json.dumps(rebuilt, sort_keys=True) == json.dumps(pinned, sort_keys=True), "pinned map differs from a rebuild; do not hand-edit it"
    assert pinned["missing_mapped_menu_ids"] == []
    snapshot = load(SNAPSHOT_PATH)
    assert all(item["status"] == 200 for item in snapshot["requests"]), "snapshot contains a failed request"
    assert {item["menuId"] for item in pinned["record_types"]} == {114, 182, 183, 186, 187, 188, 214}


def check_map_integrity() -> None:
    portal_map = load(MAP_PATH)
    for record in portal_map["record_types"]:
        assert record["applyUrl"].startswith("https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/"), record["menuId"]
        assert record["applyUrl"].endswith(f"/apply/{record['menuId']}/0/0"), record["applyUrl"]
        assert any(item["id"] == record["catalogWorkClassId"] for item in record["workClasses"]), record["menuId"]
        for item in record["workClasses"]:
            assert item["online"] is True and item["filingBehavior"] in {"review_first", "pay_first", "simple"}, item
            assert item["attachmentSetId"] in portal_map["attachment_sets"], item["label"]
            assert item["contactSetId"] in portal_map["contact_sets"], item["label"]
            if item["layoutId"]:
                assert layout_questions(portal_map, item["layoutId"]) is not None, (record["menuId"], item["label"])
                assert portal_map["layouts"][item["layoutId"]]["questionCount"] == item["questionCount"]
            assert item["instructions"] is not None, (record["menuId"], item["label"])


def check_audit_facts() -> None:
    portal_map = load(MAP_PATH)
    cases = load(CASES)
    assert cases["pinned_pulled_at"] == portal_map["source"]["pulled_at"], "update v2-map-cases.json after reviewing the rebuilt map"
    for menu_id, minimum in cases["min_online_work_classes"].items():
        assert len(record_type(portal_map, int(menu_id))["workClasses"]) >= minimum, menu_id
    for menu_id, label in cases["catalog_default_work_class"].items():
        record = record_type(portal_map, int(menu_id))
        assert klass(portal_map, int(menu_id), label)["id"] == record["catalogWorkClassId"], menu_id
    for case in cases["work_classes"]:
        item = klass(portal_map, case["type"], case["label"])
        assert item["filingBehavior"] == case["filing_behavior"], case
        if "layout_question_count" in case:
            assert item["questionCount"] == case["layout_question_count"], (case, item["questionCount"])
        if "same_layout_as" in case:
            assert item["layoutId"] == klass(portal_map, case["type"], case["same_layout_as"])["layoutId"], case
        if "own_catalog_entry" in case:
            assert case["own_catalog_entry"] in item["deepLinkedByMenuIds"], case
        if "required_question" in case:
            assert layout_questions(portal_map, item["layoutId"])[case["required_question"]]["required"] is True, case
    # One merged PDF per Application/Plans card: the City allows one PDF file there.
    for record in portal_map["record_types"]:
        for item in record["workClasses"]:
            for rule in portal_map["attachment_sets"][item["attachmentSetId"]]:
                if rule["name"] in cases["one_pdf_cards"]:
                    assert rule["maxFiles"] == 1 and rule["allowedFileTypes"] == ".pdf", (record["menuId"], item["label"], rule)


# ------------------------------------------------------------------ freshness

def freshness(snapshot: dict, temp: Path, name: str, expected: int) -> str:
    path = temp / f"{name}.json"
    dump(path, snapshot)
    return run(str(SCRIPTS / "check-portal-freshness.py"), "--portal-map", str(MAP_PATH), "--snapshot", str(path), expected=expected)


def snapshot_class(snapshot: dict, type_name: str, label: str) -> dict:
    for record in snapshot["types"].values():
        if record["name"] == type_name:
            for item in record["workClasses"]:
                if item["name"] == label:
                    return item
    raise AssertionError((type_name, label))


def check_freshness_classification(temp: Path) -> None:
    base = load(SNAPSHOT_PATH)
    out = freshness(base, temp, "same", 0)
    assert "Blocking changes: 0" in out and "Warnings: 0" in out

    cosmetic = copy.deepcopy(base)
    reroof = snapshot_class(cosmetic, "Residential", "Reroof")
    reroof["templateName"] = reroof["templateName"].replace("-**", "-*")
    out = freshness(cosmetic, temp, "template-marker", 0)
    assert "templateName marker changed (cosmetic)" in out and "Blocking changes: 0" in out

    renamed = copy.deepcopy(base)
    snapshot_class(renamed, "Residential", "Reroof")["templateName"] = "Building Permit (R) - Roofing -**"
    assert "templateName changed" in freshness(renamed, temp, "template-renamed", 1)

    added = copy.deepcopy(base)
    residential = next(record for record in added["types"].values() if record["name"] == "Residential")
    extra = copy.deepcopy(snapshot_class(added, "Residential", "Alteration"))
    extra.update(id="00000000-0000-0000-0000-000000000001", name="Kitchen Remodel")
    residential["workClasses"].append(extra)
    assert "online work class added: Kitchen Remodel" in freshness(added, temp, "class-added", 1)

    went_offline = copy.deepcopy(base)
    snapshot_class(went_offline, "Residential", "Demolition")["internetApplyType"] = None
    assert "online work class removed: Demolition" in freshness(went_offline, temp, "class-offline", 1)

    question = copy.deepcopy(base)
    reroof_layout = question["layouts"][snapshot_class(question, "Residential", "Reroof")["onlineLayoutId"]]
    target = next(q for group in reroof_layout["groups"] for q in group["questions"] if q["fieldName"] == "NUM_WaterHeater")
    target["required"] = True
    out = freshness(question, temp, "question-required", 1)
    assert "question changed: NUM_WaterHeater" in out and "layout 3dfb1688" in out

    instructions = copy.deepcopy(base)
    key = next(key for key in instructions["instructions"] if key.endswith(snapshot_class(instructions, "Residential", "Revision")["id"]))
    instructions["instructions"][key]["steps"]["AttachmentInstructions"] += " Upload a new fictional form."
    out = freshness(instructions, temp, "instructions", 1)
    assert "City instruction text changed" in out and "Upload a new fictional form." in out

    limit = copy.deepcopy(base)
    plans = next(rule for rule in snapshot_class(limit, "Residential", "Pool")["fileCategories"] if rule["name"] == "Plans")
    plans["maxFiles"] = None
    assert "attachment rule changed: Plans" in freshness(limit, temp, "plans-limit", 1)

    removed = copy.deepcopy(base)
    removed["catalog"] = [item for item in removed["catalog"] if item["menuId"] != 188]
    assert "catalog entry removed" in freshness(removed, temp, "mapped-removed", 1)

    new_entry = copy.deepcopy(base)
    entry = copy.deepcopy(next(item for item in new_entry["catalog"] if item["menuId"] == 197))
    entry.update(menuId=999, label="Fictional New Permit")
    new_entry["catalog"].append(entry)
    out = freshness(new_entry, temp, "unmapped-added", 0)
    assert "catalog entry added (not mapped by this plugin)" in out

    broken = copy.deepcopy(base)
    broken["schema_version"] = "0.0.1"
    freshness(broken, temp, "bad-schema", 2)


# ------------------------------------------------------------------ plan builder

def fact(fact_id: str, value, consumers: list | None = None) -> dict:
    receipt = {"kind": "user_answer", "captured_at": now(), "file": None, "page": None, "sheet": None, "field": None, "record_id": None, "note": "fictional eval"}
    return {
        "id": fact_id, "value": value, "source": {"kind": "user_confirmed", "receipt": receipt}, "confidence": 1,
        "confirmation": {"required": True, "status": "confirmed", "confirmed_at": now(), "note": None},
        "consumers": consumers or [], "conflicts": [], "notes": [],
    }


def plan_case(temp: Path, name: str, *, label: str, files: dict[str, list[str]], extra_facts: list | None = None,
              selection: dict | None = None, portal_map: Path = MAP_PATH, expected: int = 0, use_selection: bool = True,
              menu_id: int = 183) -> dict:
    directory = temp / name
    directory.mkdir(parents=True, exist_ok=True)
    attachments = []
    for category, names in files.items():
        for filename in names:
            path = directory / filename
            path.write_bytes(b"%PDF-1.4\n% fictional eval attachment\n%%EOF\n")
            attachments.append({"category": category, "path": str(path), "required": True})
    facts = {
        "schema_version": "1.0.0", "run_id": "portal-eval", "jurisdiction": "laguna-beach-ca", "created_at": now(), "updated_at": now(),
        "facts": [
            fact("site.address", "100 Fictional Way, Laguna Beach, CA 92651"),
            fact("project.description.r1", "Fictional eval scope"),
            fact("project.valuation.r1", 1000),
            fact("applicant.name", "Fictional Applicant"),
            fact("owner.name", "Fictional Owner"),
            *(extra_facts or []),
        ],
    }
    route = record_type(load(MAP_PATH), menu_id)
    application_set = {
        "schema_version": "1.0.0", "run_id": "portal-eval", "status": "confirmed", "address_fact_id": "site.address",
        "current_stage": "building_preparation", "confirmed_at": now(), "notes": [],
        "records": [{
            "id": "r1", "lane": "building", "scope_label": "Fictional", "scope_description_fact_id": "project.description.r1",
            "rationale": [{"source": "fictional eval", "locator": "n/a", "note": None}], "forms": [], "prerequisites": [],
            "channel": "online", "portal": {"type_id": menu_id, "label": route["label"], "module": route["module"], "deep_link": route["applyUrl"]},
            "valuation_fact_id": "project.valuation.r1", "attachments": attachments, "status": "confirmed", "blocked_reasons": [],
        }],
    }
    chosen = klass(load(MAP_PATH), menu_id, label) if selection is None else None
    selection_document = {
        "schema_version": "1.0.0", "run_id": "portal-eval", "portal_map_pulled_at": load(MAP_PATH)["source"]["pulled_at"],
        "selections": [selection or {
            "record_id": "r1", "portal_type_id": menu_id, "work_class_id": chosen["id"], "work_class_label": chosen["label"],
            "reasoning": "Fictional eval: chosen by the eval author to exercise this work class.",
            "evidence_fact_ids": ["project.description.r1"], "alternatives_considered": [], "status": "confirmed", "confirmed_at": now(),
        }],
    }
    dump(directory / "facts.json", facts)
    dump(directory / "set.json", application_set)
    dump(directory / "selection.json", selection_document)
    arguments = [
        str(SCRIPTS / "build-submission-plan.py"), "--facts", str(directory / "facts.json"),
        "--application-set", str(directory / "set.json"), "--portal-map", str(portal_map), "--output", str(directory / "plan.json"),
    ]
    if use_selection:
        arguments += ["--work-class-selection", str(directory / "selection.json")]
    run(*arguments, expected=expected)
    if expected == 1:
        return {}
    plan = load(directory / "plan.json")
    errors = validate_instance(plan, load(ROOT / "schemas/submission-plan.schema.json"))
    assert not errors, errors
    return plan["records"][0]


def reasons(record: dict) -> str:
    return "\n".join(record["blocked_reasons"])


def check_plan_builder(temp: Path) -> None:
    two_cards = {"Permit Application": ["application.pdf"], "Plans": ["plans.pdf"]}

    demolition = plan_case(temp, "demolition", label="Demolition - Single Family Residence", files=two_cards)
    assert demolition["status"] == "portal_ready", reasons(demolition)
    assert demolition["work_class"]["label"] == "Demolition - Single Family Residence"
    assert demolition["work_class"]["filing_behavior"] == "review_first"
    assert demolition["deep_link"].endswith("#/permit/apply/183/0/0")

    missing = plan_case(temp, "no-selection", label="Reroof", files=two_cards, use_selection=False, expected=2)
    assert "no work class selected" in reasons(missing)

    unknown = plan_case(temp, "unknown-class", label="Reroof", files=two_cards, expected=2, selection={
        "record_id": "r1", "portal_type_id": 183, "work_class_id": "00000000-0000-0000-0000-00000000beef", "work_class_label": "Kitchen Remodel",
        "reasoning": "Fictional eval: a class the map does not know.", "evidence_fact_ids": ["project.description.r1"],
        "alternatives_considered": [], "status": "confirmed", "confirmed_at": now()})
    assert "HARD STOP: work class Kitchen Remodel" in reasons(unknown)

    proposed = plan_case(temp, "proposed", label="Reroof", files=two_cards, expected=2, selection={
        "record_id": "r1", "portal_type_id": 183, "work_class_id": klass(load(MAP_PATH), 183, "Reroof")["id"], "work_class_label": "Reroof",
        "reasoning": "Fictional eval: not yet confirmed by the user.", "evidence_fact_ids": ["project.description.r1"],
        "alternatives_considered": [], "status": "proposed", "confirmed_at": None})
    assert "not confirmed by the user" in reasons(proposed)

    no_layout_map = copy.deepcopy(load(MAP_PATH))
    reroof_layout = klass(no_layout_map, 183, "Reroof")["layoutId"]
    del no_layout_map["layouts"][reroof_layout]
    trimmed = temp / "map-without-reroof-layout.json"
    dump(trimmed, no_layout_map)
    no_layout = plan_case(temp, "no-layout", label="Reroof", files=two_cards, portal_map=trimmed, expected=2)
    assert f"HARD STOP: layout {reroof_layout}" in reasons(no_layout)

    solar = plan_case(temp, "solarapp", label="SolarAPP+", files={"SolarAPP Approval Document": ["a.pdf"], "SolarAPP Specification Sheets": ["b.pdf"]}, expected=2)
    assert "has its own catalog entry [124]" in reasons(solar)

    split_plans = plan_case(temp, "split-plans", label="Pool", files={"Permit Application": ["application.pdf"], "Plans": ["sheet-1.pdf", "sheet-2.pdf"]}, expected=2)
    assert "merge them into one PDF" in reasons(split_plans)

    not_pdf = plan_case(temp, "not-pdf", label="Pool", files={"Permit Application": ["application.pdf"], "Plans": ["plans.dwg"]}, expected=2)
    assert "Plans accepts .pdf only" in reasons(not_pdf)

    revision_files = {"Original Plans Approved/Stamped by City": ["approved.pdf"], "Revised Plans": ["revised.pdf"]}
    revision = plan_case(temp, "revision-missing-number", label="Revision", files=revision_files, expected=2)
    assert "required portal field has no sourced fact: RevisionNumber" in reasons(revision)
    revision = plan_case(temp, "revision", label="Revision", files=revision_files,
                         extra_facts=[fact("revision.number", 1, [{"kind": "portal_field", "target": "portal:183:RevisionNumber"}])])
    assert revision["status"] == "portal_ready", reasons(revision)
    assert revision["work_class"]["filing_behavior"] == "pay_first"
    assert "Pay First" in revision["post_submit_next_action"]

    stale_field = plan_case(temp, "field-not-in-class", label="Demolition", files=two_cards, expected=2,
                            extra_facts=[fact("mep.water_heater.count", 1, [{"kind": "portal_field", "target": "portal:183:NUM_WaterHeater"}])])
    assert "NUM_WaterHeater is not in the selected work class layout" in reasons(stale_field)

    v1 = ROOT / "assets/portal-maps/v1-portal-map.json"
    if v1.is_file():
        plan_case(temp, "v1-map", label="Reroof", files=two_cards, portal_map=v1, expected=1)


def check_receipt_schema() -> None:
    receipt = {
        "schema_version": "1.1.0", "run_id": "portal-eval", "record_id": "r1", "status": "submitted", "portal_type_id": 183,
        "work_class": {"id": "fictional", "label": "Pool", "filing_behavior": "review_first"},
        "scope": "Fictional pool", "timestamp": now(), "user_identity_label": "Fictional Applicant", "portal_record_number": "DEMO-0001",
        "uploaded_files": [{"filename": "plans.pdf", "category": "Plans", "sha256": "0" * 64}], "confirmation_text": "Fictional confirmation",
        "page_state_receipts": [], "payment_state": "pending_invoice", "expected_city_response": "Completeness screen", "next_action": "Wait for staff",
        "in_person_follow_up": None, "recovery_note": None,
        "invoices": [{"observed_at": now(), "source": "portal", "invoice_number": None, "total": None, "fee_lines": [], "due_date": None, "note": None}],
        "payments": [], "status_checks": [{"checked_at": now(), "portal_status": "In Review", "workflow_step": None, "note": None}],
        "city_documents": [{"received_at": now(), "kind": "corrections_letter", "filename": "letter.pdf", "sha256": "1" * 64, "note": None}],
        "resubmittals": [], "issuance": {"status": "not_ready", "observed_at": now(), "permit_number": None, "note": None},
    }
    errors = validate_instance(receipt, load(ROOT / "schemas/submission-receipt.schema.json"))
    assert not errors, errors
    receipt["payments"] = [{"approved_at": now(), "paid_at": now(), "amount": 10, "invoice_number": None, "portal_receipt_number": None, "card_number": "x"}]
    assert validate_instance(receipt, load(ROOT / "schemas/submission-receipt.schema.json")), "payment card data must be rejected"


def check_reference_contract() -> None:
    text = {name: (ROOT / "references" / name).read_text(encoding="utf-8") for name in (
        "online-submission.md", "portal-checkpoints.md", "portal-account.md", "after-filing.md", "building-routing.md", "process-stage.md")}
    assert "v2-portal-map.json" in text["online-submission.md"] and "v2-portal-map.json" in text["portal-checkpoints.md"]
    assert "work-class-selection.json" in text["building-routing.md"]
    assert "one merged PDF" in text["online-submission.md"]
    assert "pick the file" in text["online-submission.md"]
    assert "will not link" in text["portal-account.md"]
    assert "contact on the record" in text["portal-account.md"]
    assert "separate, explicit approval" in text["after-filing.md"]
    assert "Pay First" in text["building-routing.md"] and "Demolition" in text["building-routing.md"]
    assert "no V1 online type" not in text["building-routing.md"]
    assert "status `blocked`" not in text["process-stage.md"]


def main() -> int:
    check_map_reproduces_from_snapshot()
    print("PASS portal v2: map reproduces from the pinned snapshot")
    check_map_integrity()
    check_audit_facts()
    print("PASS portal v2: work classes, layouts, attachment and contact sets")
    with tempfile.TemporaryDirectory(prefix="laguna-portal-evals-") as directory:
        check_freshness_classification(Path(directory))
        print("PASS portal v2: freshness drift classification")
        check_plan_builder(Path(directory))
        print("PASS portal v2: work class selection and plan builder hard stops")
    check_receipt_schema()
    check_reference_contract()
    print("PASS portal v2: receipt schema and reference contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
