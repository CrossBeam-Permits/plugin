#!/usr/bin/env python3
"""Shared, deterministic helpers for the Laguna EnerGov portal map (v2).

Three jobs live here, so the pull, the map builder and the freshness checker
cannot disagree:

1. ``pull_snapshot`` reads the City's public Tyler EnerGov catalog with GET
   requests only. It keeps a small projection of each response (the fields the
   map uses), not the raw bytes.
2. ``compile_map`` turns a snapshot into the v2 portal map.
3. ``diff_maps`` compares two maps and sorts each change into blocking drift or
   a non-blocking warning.

Regex is used here only for mechanical text processing (HTML to text, link
extraction, template-name normalisation). It never decides a route.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any, Callable

PORTAL_BASE_URL = "https://lagunabeachca-energovweb.tylerhost.net"
PORTAL_DOMAIN = "lagunabeachca-energovweb.tylerhost.net"
API_ROOT = f"{PORTAL_BASE_URL}/apps/selfservice/api"
# Request headers the portal's own front end sends. They name the public tenant;
# they are not credentials.
TENANT_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "tenantId": "2",
    "tenantName": "City of Laguna Beach, CA",
    "Tyler-TenantUrl": "City of Laguna Beach, CA",
    "Tyler-Tenant-Culture": "en-US",
    "User-Agent": "crossbeam-laguna-plugin-portal-map/2 (read-only catalog check)",
}
# The catalog menu entries this plugin maps. Other entries are listed in the
# map's catalog only, so a new or removed entry is still reported.
MAPPED_MENU_IDS = (114, 182, 183, 186, 187, 188, 214)
INSTRUCTION_STEPS = (
    "LocationInstructions",
    "BasicInfoInstructions",
    "ContactInstructions",
    "MoreInfoInstructions",
    "AttachmentInstructions",
    "SignatureInstructions",
    "ReviewInstructions",
)
UNLIMITED_FILES = 2147483647
SNAPSHOT_SCHEMA_VERSION = "1.0.0"
MAP_SCHEMA_VERSION = "2.0.0"


# ---------------------------------------------------------------- utilities

def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(canonical(value))


def html_to_text(markup: Any) -> str | None:
    """Mechanically strip Tyler's inline-styled HTML to readable text."""
    if not isinstance(markup, str) or not markup.strip():
        return None
    # Source line breaks inside the HTML are layout only; block tags carry the structure.
    text = re.sub(r"\s+", " ", markup)
    text = re.sub(r"<\s*(br|/p|/li|/div|/h[1-6])\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text).replace(" ", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n[ \n]*", "\n", text)
    return text.strip() or None


def extract_links(markup: Any) -> list[dict[str, str]]:
    if not isinstance(markup, str):
        return []
    links = []
    for match in re.finditer(r"<a\b[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", markup, flags=re.I | re.S):
        links.append({"href": html.unescape(match.group(1)).strip(), "text": html_to_text(match.group(2)) or ""})
    return links


def template_stem(name: Any) -> str | None:
    """Template name without Tyler's trailing ``-*``/``-**`` marker and spaces.

    Mechanical normalisation only: the marker is cosmetic, so a change that
    survives this function is still reported.
    """
    if not isinstance(name, str):
        return None
    return re.sub(r"\s*-\s*\*+\s*$", "", name.strip()).strip()


def filing_behavior(internet_apply_type: Any) -> str | None:
    """Map Tyler's InternetApplyType label to a stable token. Empty means not online."""
    value = (internet_apply_type or "").strip()
    if not value:
        return None
    return value.lower().replace(" ", "_")


# ---------------------------------------------------------------- live pull

class PortalClient:
    """Rate-limited, GET-only client for the City's public portal API."""

    def __init__(self, delay_seconds: float = 1.0, timeout: float = 60.0, opener: Callable | None = None):
        self.delay_seconds = delay_seconds
        self.timeout = timeout
        self.opener = opener or urllib.request.urlopen
        self.last_at = 0.0
        self.log: list[dict[str, Any]] = []

    def get(self, path: str) -> Any:
        wait = self.delay_seconds - (time.monotonic() - self.last_at)
        if wait > 0:
            time.sleep(wait)
        self.last_at = time.monotonic()
        request = urllib.request.Request(f"{API_ROOT}/{path}", headers=TENANT_HEADERS, method="GET")
        try:
            with self.opener(request, timeout=self.timeout) as response:
                body = response.read()
                status = response.status
        except urllib.error.HTTPError as error:
            self.log.append({"path": path, "status": error.code, "bytes": 0, "sha256": None})
            raise RuntimeError(f"GET {path} -> HTTP {error.code}") from error
        self.log.append({"path": path, "status": status, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
        document = json.loads(body.decode("utf-8"))
        if isinstance(document, dict) and document.get("Success") is False:
            raise RuntimeError(f"GET {path} -> Success:false {document.get('ErrorMessage')}")
        return document


def _catalog_entries(menu_document: dict[str, Any]) -> list[dict[str, Any]]:
    menus = (menu_document.get("Result") or {}).get("Menus") or []
    apply_menu = next((item for item in menus if item.get("Details") == "Apply" and not item.get("IsCustom")), None)
    if apply_menu is None:
        raise RuntimeError("no Apply menu in Home/Menu; the catalog shape changed")
    entries = []
    for module_menu in apply_menu.get("SubMenus") or []:
        for item in module_menu.get("SubMenus") or []:
            info = item.get("CaseTypeInfo") or {}
            route = json.loads(item["Route"]).get("NavigationUrl", "") if item.get("Route") else ""
            route = route.replace(":menuId", str(item.get("MenuID"))).replace("/:draftId/:actionTypeId", "/0/0")
            class_id = info.get("PackageCaseClassId")
            entries.append(
                {
                    "module": module_menu.get("Details"),
                    "menuId": item.get("MenuID"),
                    "label": item.get("Label"),
                    "category": item.get("CategoryName"),
                    "description": item.get("Description"),
                    "typeId": info.get("PackageCaseTypeId"),
                    "workClassId": None if class_id in (None, "", "N/A") else class_id,
                    "caseTypeUse": info.get("CaseTypeUse"),
                    "eReviewsEnabled": info.get("EReviewsEnabled"),
                    "descriptionRequired": info.get("DescriptionRequired"),
                    "squareFootageRequired": info.get("SquareFootageRequired"),
                    "valuationRequired": info.get("ValuationRequired"),
                    "signatureRequired": info.get("SignatureRequired"),
                    "successMessage": info.get("SuccessMessage"),
                    "applyUrl": f"{PORTAL_BASE_URL}/apps/SelfService#/{route}" if route else None,
                }
            )
    return sorted(entries, key=lambda entry: (str(entry["module"]), entry["menuId"]))


def _work_class(raw: dict[str, Any]) -> dict[str, Any]:
    file_set = raw.get("FileSet") or {}
    categories = []
    for category in file_set.get("FileSetFileCategories") or []:
        allowed = category.get("NumberOfFilesAllowed")
        categories.append(
            {
                "name": category.get("FileCategoryName"),
                "description": category.get("FileCategoryDescription"),
                "required": bool(category.get("IsRequired")),
                "allowedFileTypes": category.get("AllowedFileTypes"),
                "maxFiles": None if allowed in (None, UNLIMITED_FILES) else allowed,
            }
        )
    categories.sort(key=lambda item: (not item["required"], str(item["name"])))
    contacts = [
        {"name": item.get("Name"), "required": bool(item.get("IsRequired")), "validatesLicense": bool(item.get("IsValidateLic"))}
        for item in raw.get("ContactTypeList") or []
    ]
    contacts.sort(key=lambda item: (not item["required"], str(item["name"])))
    certifications = sorted(
        str(item.get("Name") or item.get("CertificationTypeName") or item.get("Description") or "unnamed")
        for item in raw.get("CertificationTypeList") or []
    )
    return {
        "id": raw.get("PermitWorkClassID") or raw.get("PlanWorkClassID"),
        "name": raw.get("WorkClassName") or raw.get("PlanWorkClassName"),
        "templateName": raw.get("TemplateName"),
        "internetApplyType": (raw.get("InternetApplyType") or "").strip() or None,
        "onlineLayoutId": raw.get("OnlineCustomFieldLayoutID") or None,
        "offlineLayoutId": raw.get("CustomFieldLayoutID") or None,
        "addressRequired": raw.get("IsCAPAddressRequired"),
        "certificationTypes": certifications,
        "contactTypes": contacts,
        "fileCategories": categories,
    }


def _layout(document: dict[str, Any]) -> dict[str, Any]:
    result = document.get("Result") or {}
    groups = []
    for group in sorted(result.get("CustomGroups") or [], key=lambda item: (item.get("SortOrder") or 0, item.get("Id") or 0)):
        fields = []
        for field in sorted(group.get("CustomFields") or [], key=lambda item: (item.get("SortOrder") or 0, item.get("Id") or 0)):
            pick_list = None
            if field.get("IsPickList"):
                pick_list = [
                    str(item.get("Label") if isinstance(item, dict) and item.get("Label") is not None else (item.get("Value") if isinstance(item, dict) else item))
                    for item in field.get("CustomPickListItems") or []
                ]
            fields.append(
                {
                    "fieldName": field.get("FieldName"),
                    "label": (field.get("Label") or "").strip(),
                    "required": bool(field.get("IsRequired")),
                    "readOnly": bool(field.get("IsReadOnly")),
                    "fieldTypeId": field.get("FieldTypeId"),
                    "controlTypeId": field.get("CustomFieldLayoutControlType"),
                    "isTable": bool(field.get("IsTable")),
                    "pickList": pick_list,
                    "tip": (field.get("FieldTip") or "").strip() or None,
                }
            )
        groups.append({"group": (group.get("Label") or "").strip(), "questions": fields})
    return {"name": (result.get("Name") or "").strip() or None, "groups": groups}


def _instructions(document: dict[str, Any]) -> dict[str, Any]:
    raw = document.get("Result") or {}
    steps: dict[str, str] = {}
    links: dict[str, dict[str, str]] = {}
    for step in INSTRUCTION_STEPS:
        text = html_to_text(raw.get(step))
        if text:
            steps[step] = text
        for link in extract_links(raw.get(step)):
            links.setdefault(link["href"], link)
    return {"steps": steps, "links": [links[key] for key in sorted(links)]}


def pull_snapshot(
    client: PortalClient,
    menu_ids: tuple[int, ...] = MAPPED_MENU_IDS,
    progress: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    """Read the public catalog for the mapped menu entries. GET requests only."""
    say = progress or (lambda message: None)
    catalog = _catalog_entries(client.get("Home/Menu"))
    by_menu = {entry["menuId"]: entry for entry in catalog}
    missing = [menu_id for menu_id in menu_ids if menu_id not in by_menu]
    mapped = [by_menu[menu_id] for menu_id in menu_ids if menu_id in by_menu]
    say(f"catalog: {len(catalog)} entries; mapped present: {len(mapped)}; missing: {missing}")

    types: dict[str, Any] = {}
    for entry in mapped:
        key = f"{entry['module']}:{entry['typeId']}"
        if key in types:
            continue
        module_path = "permits" if entry["module"] == "PERMITS" else "plans"
        setup = client.get(f"energov/{module_path}/setup/{entry['typeId']}")
        list_key = "PermitTypes" if entry["module"] == "PERMITS" else "PlanTypes"
        raw_types = (setup.get("Result") or {}).get(list_key) or []
        raw_type = next(
            (item for item in raw_types if str(item.get("PermitTypeID") or item.get("PlanTypeID")).lower() == str(entry["typeId"]).lower()),
            raw_types[0] if raw_types else {},
        )
        work_classes = sorted((_work_class(item) for item in raw_type.get("WorkClassTemplates") or []), key=lambda item: str(item["name"]))
        types[key] = {
            "module": entry["module"],
            "typeId": entry["typeId"],
            "name": raw_type.get("PermitName") or raw_type.get("PlanName"),
            "allowsInternetSubmission": raw_type.get("AllowInternetSubmission"),
            "workClasses": work_classes,
        }
        say(f"setup {key}: {len(work_classes)} work classes")

    layout_pairs: dict[str, str] = {}
    instruction_keys: list[tuple[str, str]] = []
    for record in types.values():
        for work_class in record["workClasses"]:
            if not work_class["internetApplyType"]:
                continue
            online = work_class["onlineLayoutId"] or work_class["offlineLayoutId"]
            offline = work_class["offlineLayoutId"] or work_class["onlineLayoutId"]
            if online:
                layout_pairs.setdefault(online, offline)
            instruction_keys.append((record["typeId"], work_class["id"]))

    layouts = {}
    for online in sorted(layout_pairs):
        layouts[online] = _layout(client.get(f"energov/customfields/template/{online}/{layout_pairs[online]}"))
    say(f"layouts: {len(layouts)}")

    instructions = {}
    for type_id, class_id in sorted(set(instruction_keys)):
        instructions[f"{type_id}/{class_id}"] = _instructions(client.get(f"casetype/instructions/{type_id}/{class_id}/"))
    say(f"instruction sets: {len(instructions)}")

    return {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "portal": {"base_url": PORTAL_BASE_URL, "api_root": API_ROOT},
        "pulled_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "method": "Unauthenticated GET requests to the City's public EnerGov SelfService API; no account, draft or submission.",
        "mapped_menu_ids": list(menu_ids),
        "missing_menu_ids": missing,
        "catalog": catalog,
        "types": dict(sorted(types.items())),
        "layouts": layouts,
        "instructions": instructions,
        "requests": client.log,
    }


# ---------------------------------------------------------------- compile

def _question_count(layout: dict[str, Any] | None) -> int:
    if not layout:
        return 0
    return sum(len(group["questions"]) for group in layout["groups"])


def compile_map(snapshot: dict[str, Any], snapshot_path: str, snapshot_sha256: str) -> dict[str, Any]:
    if snapshot.get("schema_version") != SNAPSHOT_SCHEMA_VERSION:
        raise ValueError(f"unsupported portal snapshot schema: {snapshot.get('schema_version')}")
    catalog = snapshot["catalog"]
    by_menu = {entry["menuId"]: entry for entry in catalog}
    deep_links: dict[tuple[str, str], list[int]] = {}
    for entry in catalog:
        if entry["typeId"] and entry["workClassId"]:
            deep_links.setdefault((str(entry["typeId"]).lower(), str(entry["workClassId"]).lower()), []).append(entry["menuId"])

    used_layouts: set[str] = set()
    attachment_sets: dict[str, list[dict[str, Any]]] = {}
    contact_sets: dict[str, list[dict[str, Any]]] = {}

    def set_id(prefix: str, value: list[dict[str, Any]], bucket: dict[str, list[dict[str, Any]]]) -> str:
        identifier = f"{prefix}-{sha256_json(value)[:12]}"
        bucket.setdefault(identifier, value)
        return identifier

    record_types = []
    for menu_id in snapshot["mapped_menu_ids"]:
        entry = by_menu.get(menu_id)
        if entry is None:
            continue
        type_record = snapshot["types"][f"{entry['module']}:{entry['typeId']}"]
        work_classes = []
        not_online = []
        for raw in type_record["workClasses"]:
            if not raw["internetApplyType"]:
                not_online.append({"id": raw["id"], "label": raw["name"]})
                continue
            layout_id = raw["onlineLayoutId"] or raw["offlineLayoutId"]
            if layout_id:
                used_layouts.add(layout_id)
            instructions = snapshot["instructions"].get(f"{type_record['typeId']}/{raw['id']}")
            attachments = raw["fileCategories"]
            work_classes.append(
                {
                    "id": raw["id"],
                    "label": raw["name"],
                    "online": True,
                    "internetApplyType": raw["internetApplyType"],
                    "filingBehavior": filing_behavior(raw["internetApplyType"]),
                    "templateName": raw["templateName"],
                    "layoutId": layout_id,
                    "questionCount": _question_count(snapshot["layouts"].get(layout_id)) if layout_id else 0,
                    "deepLinkedByMenuIds": sorted(deep_links.get((str(type_record["typeId"]).lower(), str(raw["id"]).lower()), [])),
                    "addressRequired": raw["addressRequired"],
                    "licenseCertificationTypes": raw["certificationTypes"],
                    "contactSetId": set_id("contacts", raw["contactTypes"], contact_sets),
                    "requiredContacts": [item["name"] for item in raw["contactTypes"] if item["required"]],
                    "attachmentSetId": set_id("files", attachments, attachment_sets),
                    "requiredAttachments": [item["name"] for item in attachments if item["required"]],
                    "instructions": None
                    if instructions is None
                    else {
                        "sha256": sha256_json(instructions["steps"]),
                        "steps": {step: sha256_text(text) for step, text in sorted(instructions["steps"].items())},
                        "links": instructions["links"],
                    },
                }
            )
        work_classes.sort(key=lambda item: str(item["label"]).lower())
        not_online.sort(key=lambda item: str(item["label"]).lower())
        record_types.append(
            {
                "menuId": menu_id,
                "module": entry["module"],
                "label": (entry["label"] or "").strip(),
                "category": entry["category"],
                "catalogDescriptionSha256": sha256_text(entry["description"] or ""),
                "catalogDescription": entry["description"],
                "typeId": entry["typeId"],
                "typeName": type_record["name"],
                "applyUrl": entry["applyUrl"],
                "catalogWorkClassId": entry["workClassId"],
                "allowsInternetSubmission": type_record["allowsInternetSubmission"],
                "eReviewsEnabled": entry["eReviewsEnabled"],
                "feeEstimateAvailable": entry["caseTypeUse"] == 0,
                "requires": {
                    "description": entry["descriptionRequired"],
                    "squareFootage": entry["squareFootageRequired"],
                    "valuation": entry["valuationRequired"],
                    "signature": entry["signatureRequired"],
                },
                "submitSuccessMessage": entry["successMessage"],
                "workClasses": work_classes,
                "workClassesNotOnline": not_online,
            }
        )

    layouts = {}
    for layout_id in sorted(used_layouts):
        layout = snapshot["layouts"].get(layout_id)
        if layout is None:
            continue
        layouts[layout_id] = {"name": layout["name"], "questionCount": _question_count(layout), "groups": layout["groups"]}

    return {
        "schema_version": MAP_SCHEMA_VERSION,
        "portal": {"base_url": PORTAL_BASE_URL, "domain": PORTAL_DOMAIN},
        "source": {
            "snapshot": snapshot_path,
            "snapshot_sha256": snapshot_sha256,
            "pulled_at": snapshot["pulled_at"],
            "method": snapshot["method"],
            "built_by": "scripts/build-portal-map.py",
        },
        "catalog": [
            {
                "menuId": entry["menuId"],
                "module": entry["module"],
                "label": (entry["label"] or "").strip(),
                "category": entry["category"],
                "typeId": entry["typeId"],
                "workClassId": entry["workClassId"],
                "mapped": entry["menuId"] in snapshot["mapped_menu_ids"],
            }
            for entry in catalog
        ],
        "missing_mapped_menu_ids": snapshot.get("missing_menu_ids") or [],
        "record_types": record_types,
        "attachment_sets": dict(sorted(attachment_sets.items())),
        "contact_sets": dict(sorted(contact_sets.items())),
        "layouts": layouts,
    }


# ---------------------------------------------------------------- lookups

def record_type(portal_map: dict[str, Any], menu_id: int) -> dict[str, Any] | None:
    return next((item for item in portal_map.get("record_types") or [] if item["menuId"] == menu_id), None)


def work_class(record: dict[str, Any], class_id: str) -> dict[str, Any] | None:
    wanted = str(class_id).lower()
    return next((item for item in record["workClasses"] if str(item["id"]).lower() == wanted), None)


def attachments_for(portal_map: dict[str, Any], klass: dict[str, Any]) -> list[dict[str, Any]] | None:
    return (portal_map.get("attachment_sets") or {}).get(klass.get("attachmentSetId"))


def contacts_for(portal_map: dict[str, Any], klass: dict[str, Any]) -> list[dict[str, Any]] | None:
    return (portal_map.get("contact_sets") or {}).get(klass.get("contactSetId"))


def layout_questions(portal_map: dict[str, Any], layout_id: str | None) -> dict[str, dict[str, Any]] | None:
    """Questions by field name, or None when the layout is not pinned."""
    if not layout_id:
        return {}
    layout = (portal_map.get("layouts") or {}).get(layout_id)
    if layout is None:
        return None
    return {
        question["fieldName"]: question
        for group in layout["groups"]
        for question in group["questions"]
        if question.get("fieldName")
    }


# ---------------------------------------------------------------- diff

def _finding(severity: str, scope: str, what: str, before: Any = None, after: Any = None) -> dict[str, Any]:
    return {"severity": severity, "scope": scope, "change": what, "before": before, "after": after}


WORK_CLASS_BLOCKING_KEYS = (
    "label", "online", "internetApplyType", "filingBehavior", "layoutId", "deepLinkedByMenuIds",
    "addressRequired", "licenseCertificationTypes", "contacts", "attachments",
)
RECORD_BLOCKING_KEYS = (
    "module", "label", "category", "catalogDescriptionSha256", "typeId", "applyUrl", "catalogWorkClassId",
    "allowsInternetSubmission", "requires", "submitSuccessMessage",
)
RECORD_WARNING_KEYS = ("eReviewsEnabled", "feeEstimateAvailable", "typeName")


def _diff_attachments(scope: str, before: list[dict], after: list[dict]) -> list[dict[str, Any]]:
    findings = []
    old = {item["name"]: item for item in before}
    new = {item["name"]: item for item in after}
    for name in sorted(set(old) - set(new)):
        findings.append(_finding("blocking", scope, f"attachment category removed: {name}", old[name], None))
    for name in sorted(set(new) - set(old)):
        findings.append(_finding("blocking", scope, f"attachment category added: {name}", None, new[name]))
    for name in sorted(set(old) & set(new)):
        if canonical(old[name]) != canonical(new[name]):
            findings.append(_finding("blocking", scope, f"attachment rule changed: {name}", old[name], new[name]))
    return findings


def question_key(question: dict[str, Any], seen: dict[str, int]) -> str:
    """Stable key for a question; label-only rows (no field name) key by label."""
    base = question.get("fieldName") or f"(label) {question.get('label') or ''}"
    seen[base] = seen.get(base, 0) + 1
    return base if seen[base] == 1 else f"{base} #{seen[base]}"


def _keyed_questions(layout: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    seen: dict[str, int] = {}
    return {(group["group"], question_key(question, seen)): question for group in layout["groups"] for question in group["questions"]}


def _diff_layout(scope: str, before: dict, after: dict) -> list[dict[str, Any]]:
    findings = []
    old = _keyed_questions(before)
    new = _keyed_questions(after)
    old_names = {key[1]: key for key in old}
    new_names = {key[1]: key for key in new}
    for name in sorted(set(old_names) - set(new_names)):
        findings.append(_finding("blocking", scope, f"question removed: {name}", old[old_names[name]], None))
    for name in sorted(set(new_names) - set(old_names)):
        findings.append(_finding("blocking", scope, f"question added: {name}", None, new[new_names[name]]))
    for name in sorted(set(old_names) & set(new_names)):
        a, b = old[old_names[name]], new[new_names[name]]
        if old_names[name][0] != new_names[name][0]:
            findings.append(_finding("blocking", scope, f"question moved to another group: {name}", old_names[name][0], new_names[name][0]))
        if canonical(a) != canonical(b):
            findings.append(_finding("blocking", scope, f"question changed: {name}", a, b))
    if not findings and canonical(before["groups"]) != canonical(after["groups"]):
        findings.append(_finding("blocking", scope, "question groups or order changed", [g["group"] for g in before["groups"]], [g["group"] for g in after["groups"]]))
    if (before.get("name") or "") != (after.get("name") or ""):
        findings.append(_finding("warning", scope, "layout name changed (cosmetic)", before.get("name"), after.get("name")))
    return findings


def diff_maps(pinned: dict[str, Any], fresh: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    old_catalog = {item["menuId"]: item for item in pinned.get("catalog") or []}
    new_catalog = {item["menuId"]: item for item in fresh.get("catalog") or []}
    for menu_id in sorted(set(old_catalog) - set(new_catalog)):
        severity = "blocking" if old_catalog[menu_id].get("mapped") else "warning"
        findings.append(_finding(severity, f"catalog {menu_id}", "catalog entry removed", old_catalog[menu_id]["label"], None))
    for menu_id in sorted(set(new_catalog) - set(old_catalog)):
        findings.append(_finding("warning", f"catalog {menu_id}", "catalog entry added (not mapped by this plugin)", None, new_catalog[menu_id]["label"]))
    for menu_id in sorted(set(old_catalog) & set(new_catalog)):
        a, b = old_catalog[menu_id], new_catalog[menu_id]
        if not a.get("mapped") and canonical(a) != canonical(b):
            findings.append(_finding("warning", f"catalog {menu_id}", "unmapped catalog entry changed", a, b))

    old_types = {item["menuId"]: item for item in pinned.get("record_types") or []}
    new_types = {item["menuId"]: item for item in fresh.get("record_types") or []}
    for menu_id in sorted(set(old_types) - set(new_types)):
        findings.append(_finding("blocking", f"type {menu_id}", "mapped record type is no longer in the live catalog", old_types[menu_id]["label"], None))
    for menu_id in sorted(set(new_types) - set(old_types)):
        findings.append(_finding("blocking", f"type {menu_id}", "record type is new to the map", None, new_types[menu_id]["label"]))

    old_layouts = pinned.get("layouts") or {}
    new_layouts = fresh.get("layouts") or {}
    layout_users: dict[str, list[str]] = {}

    for menu_id in sorted(set(old_types) & set(new_types)):
        a, b = old_types[menu_id], new_types[menu_id]
        scope = f"type {menu_id} {a['label']}"
        for key in RECORD_BLOCKING_KEYS:
            if canonical(a.get(key)) != canonical(b.get(key)):
                before, after = a.get(key), b.get(key)
                if key == "catalogDescriptionSha256":
                    before, after = a.get("catalogDescription"), b.get("catalogDescription")
                findings.append(_finding("blocking", scope, f"{key} changed", before, after))
        for key in RECORD_WARNING_KEYS:
            if canonical(a.get(key)) != canonical(b.get(key)):
                findings.append(_finding("warning", scope, f"{key} changed", a.get(key), b.get(key)))
        old_classes = {item["id"]: item for item in a["workClasses"]}
        new_classes = {item["id"]: item for item in b["workClasses"]}
        for class_id in sorted(set(old_classes) - set(new_classes)):
            findings.append(_finding("blocking", scope, f"online work class removed: {old_classes[class_id]['label']}", class_id, None))
        for class_id in sorted(set(new_classes) - set(old_classes)):
            item = new_classes[class_id]
            findings.append(_finding("blocking", scope, f"online work class added: {item['label']} ({item['internetApplyType']})", None, class_id))
        for class_id in sorted(set(old_classes) & set(new_classes)):
            wa = dict(old_classes[class_id], attachments=attachments_for(pinned, old_classes[class_id]) or [], contacts=contacts_for(pinned, old_classes[class_id]) or [])
            wb = dict(new_classes[class_id], attachments=attachments_for(fresh, new_classes[class_id]) or [], contacts=contacts_for(fresh, new_classes[class_id]) or [])
            class_scope = f"{scope} / {wa['label']}"
            for key in WORK_CLASS_BLOCKING_KEYS:
                if key == "attachments":
                    findings.extend(_diff_attachments(class_scope, wa[key], wb[key]))
                elif canonical(wa.get(key)) != canonical(wb.get(key)):
                    findings.append(_finding("blocking", class_scope, f"{key} changed", wa.get(key), wb.get(key)))
            if canonical(wa.get("instructions")) != canonical(wb.get("instructions")):
                old_steps = (wa.get("instructions") or {}).get("steps") or {}
                new_steps = (wb.get("instructions") or {}).get("steps") or {}
                changed_steps = sorted(step for step in set(old_steps) | set(new_steps) if old_steps.get(step) != new_steps.get(step))
                if changed_steps:
                    findings.append(_finding("blocking", class_scope, "City instruction text changed", None, changed_steps))
                else:
                    findings.append(_finding("blocking", class_scope, "City instruction links changed", (wa.get("instructions") or {}).get("links"), (wb.get("instructions") or {}).get("links")))
            if wa.get("templateName") != wb.get("templateName"):
                cosmetic = template_stem(wa.get("templateName")) == template_stem(wb.get("templateName"))
                findings.append(
                    _finding(
                        "warning" if cosmetic else "blocking",
                        class_scope,
                        "templateName marker changed (cosmetic)" if cosmetic else "templateName changed",
                        wa.get("templateName"),
                        wb.get("templateName"),
                    )
                )
            if wa.get("layoutId") and wa.get("layoutId") == wb.get("layoutId"):
                layout_users.setdefault(wa["layoutId"], []).append(class_scope)
        old_off = {item["id"]: item["label"] for item in a.get("workClassesNotOnline") or []}
        new_off = {item["id"]: item["label"] for item in b.get("workClassesNotOnline") or []}
        if old_off != new_off:
            findings.append(_finding("warning", scope, "work classes that are not offered online changed", sorted(old_off.values()), sorted(new_off.values())))

    for layout_id in sorted(layout_users):
        if layout_id not in old_layouts or layout_id not in new_layouts:
            findings.append(_finding("blocking", f"layout {layout_id}", "layout missing from a map", layout_id in old_layouts, layout_id in new_layouts))
            continue
        users = layout_users[layout_id]
        scope = f"layout {layout_id} (used by {len(users)} work class(es), e.g. {users[0]})"
        findings.extend(_diff_layout(scope, old_layouts[layout_id], new_layouts[layout_id]))
    return findings
