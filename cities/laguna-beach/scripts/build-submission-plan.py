#!/usr/bin/env python3
"""Compile confirmed records and packets into exact EnerGov transactions."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

from _lib import confirmed_fact_value, fact_index, load_json, sha256_file, utc_now, write_json


ROLE_FACTS = {
    "Applicant": "applicant.name",
    "Owner": "owner.name",
    "Contractor": "contractor.name",
    "Architect": "designer.architect.name",
    "Designer": "designer.name",
    "Engineer": "designer.engineer.name",
}


def usable_fact(facts: dict[str, dict[str, Any]], fact_id: str, blocked: list[str]) -> Any:
    fact = facts.get(fact_id)
    if fact is None:
        blocked.append(f"missing fact: {fact_id}")
        return None
    usable, value, reason = confirmed_fact_value(fact)
    if not usable:
        blocked.append(f"unusable fact {fact_id}: {reason}")
        return None
    return value


def deep_link(route: dict[str, Any]) -> str:
    base = route["applyUrl"].rstrip("/")
    return base if base.endswith("/0/0") else base + "/0/0"


def custom_field_facts(facts: dict[str, dict[str, Any]], route: dict[str, Any], blocked: list[str]) -> list[dict[str, Any]]:
    question_by_name = {
        question["fieldName"]: question
        for group in route.get("questionGroups") or []
        for question in group.get("questions") or []
    }
    mapped: dict[str, dict[str, Any]] = {}
    prefix = f"portal:{route['menuId']}:"
    for fact_id, fact in facts.items():
        for consumer in fact.get("consumers") or []:
            target = consumer.get("target")
            if consumer.get("kind") != "portal_field" or not isinstance(target, str) or not target.startswith(prefix):
                continue
            field_name = target[len(prefix):]
            if field_name not in question_by_name:
                blocked.append(f"portal field drift: {field_name} is not in type {route['menuId']}")
                continue
            usable, value, reason = confirmed_fact_value(fact)
            if not usable:
                blocked.append(f"unusable portal fact {fact_id}: {reason}")
                continue
            if field_name in mapped:
                blocked.append(f"multiple facts target portal field: {field_name}")
                continue
            mapped[field_name] = {"field_name": field_name, "fact_id": fact_id, "value": value}
    for name, question in question_by_name.items():
        if question.get("required") and name not in mapped:
            blocked.append(f"required portal field has no sourced fact: {name}")
    return [mapped[name] for name in sorted(mapped)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts", required=True)
    parser.add_argument("--application-set", required=True)
    parser.add_argument("--portal-map", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    facts_document = load_json(args.facts)
    facts = fact_index(facts_document)
    application_set = load_json(args.application_set)
    portal_map = load_json(args.portal_map)
    routes = {route["menuId"]: route for route in portal_map["routes"]}
    if application_set.get("status") != "confirmed" or not application_set.get("confirmed_at"):
        raise SystemExit("application set is not user-confirmed")
    if application_set["run_id"] != facts_document["run_id"]:
        raise SystemExit("run_id mismatch between project facts and application set")

    transactions = []
    for record in application_set["records"]:
        if record["channel"] != "online":
            continue
        blocked = list(record.get("blocked_reasons") or [])
        if record.get("status") != "confirmed":
            blocked.append(f"record is not confirmed: {record.get('status')}")
        for prerequisite_id in record["prerequisites"]:
            if usable_fact(facts, prerequisite_id, blocked) is not True:
                blocked.append(f"prerequisite is not satisfied: {prerequisite_id}")
        portal = record.get("portal")
        if not portal:
            raise SystemExit(f"online record {record['id']} has no portal configuration")
        route = routes.get(portal["type_id"])
        if route is None:
            raise SystemExit(f"record {record['id']}: portal type {portal['type_id']} is not supported")
        if route["module"] != portal["module"] or route["label"].strip() != portal["label"].strip():
            blocked.append("application-set portal label/module differs from pinned map")

        address = usable_fact(facts, application_set["address_fact_id"], blocked)
        description = usable_fact(facts, record["scope_description_fact_id"], blocked)
        basic_info = []
        if description is not None:
            basic_info.append({"fact_id": record["scope_description_fact_id"], "value": description})
        if record["lane"] == "building":
            valuation_id = record.get("valuation_fact_id")
            if not valuation_id:
                blocked.append("Building record has no separate valuation fact")
            else:
                valuation = usable_fact(facts, valuation_id, blocked)
                if valuation is not None:
                    basic_info.append({"fact_id": valuation_id, "value": valuation})

        contacts = []
        for contact in route.get("contactTypes") or []:
            if not contact.get("required"):
                continue
            role = contact["name"]
            fact_id = ROLE_FACTS.get(role)
            if fact_id is None:
                blocked.append(f"no canonical identity mapping for required contact role: {role}")
                continue
            if usable_fact(facts, fact_id, blocked) is not None:
                contacts.append({"role": role, "identity_fact_id": fact_id})

        permitted_categories = {item["name"]: item for item in route.get("attachments") or []}
        uploads = []
        present_categories = set()
        for attachment in record.get("attachments") or []:
            category = attachment["category"]
            path = Path(attachment["path"])
            present_categories.add(category)
            if category not in permitted_categories:
                blocked.append(f"attachment category is not available on type {route['menuId']}: {category}")
                continue
            if not path.is_file():
                blocked.append(f"attachment file is missing: {path}")
                continue
            uploads.append({"category": category, "files": [{"path": str(path.resolve()), "sha256": sha256_file(path)}]})
        for category in route.get("requiredAttachments") or []:
            if category not in present_categories:
                blocked.append(f"required attachment category is missing: {category}")

        normalized = "|".join([str(address or ""), str(route["menuId"]), str(description or ""), application_set["run_id"]])
        idempotency_key = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        transactions.append(
            {
                "record_id": record["id"],
                "portal_type_id": route["menuId"],
                "module": route["module"],
                "label": route["label"].strip(),
                "deep_link": deep_link(route),
                "idempotency_key": idempotency_key,
                "address": {"fact_id": application_set["address_fact_id"], "value": address},
                "basic_info": basic_info,
                "contacts": contacts,
                "custom_fields": custom_field_facts(facts, route, blocked),
                "uploads": uploads,
                "checkpoints": {
                    "signature": "user_personal_entry_required",
                    "final_submit": "fresh_explicit_approval_required",
                    "payment": "separate_explicit_approval_required",
                },
                "expected_confirmation": route["submitSuccessMessage"],
                "post_submit_next_action": "City completeness screen; staff generally contacts the applicant in 2-3 business days for payment. Building permit issuance is later in person where applicable.",
                "status": "blocked" if blocked else "portal_ready",
                "blocked_reasons": sorted(set(blocked)),
            }
        )

    if not transactions:
        raise SystemExit("application set contains no online records")
    output = {
        "schema_version": "1.1.0",
        "run_id": application_set["run_id"],
        "generated_at": utc_now(),
        "records": transactions,
    }
    write_json(args.output, output)
    blocked_count = sum(item["status"] == "blocked" for item in transactions)
    print(f"Built {len(transactions)} transactions ({blocked_count} blocked) -> {args.output}")
    return 2 if blocked_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
