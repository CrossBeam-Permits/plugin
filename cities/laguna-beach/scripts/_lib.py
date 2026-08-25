#!/usr/bin/env python3
"""Shared deterministic helpers for the Laguna permit skill."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> Any:
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def write_json(path: str | Path, value: Any) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    temporary.replace(destination)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_pypdf():
    try:
        import pypdf  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "pypdf is required. Install it with: python3 -m pip install pypdf"
        ) from exc
    return pypdf


def pdf_scalar(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def field_tree(reader: Any) -> list[dict[str, Any]]:
    fields = reader.get_fields() or {}
    return [
        {
            "name": name,
            "type": pdf_scalar(field.get("/FT")),
            "tooltip": pdf_scalar(field.get("/TU")),
            "flags": int(field.get("/Ff", 0)),
        }
        for name, field in sorted(fields.items())
    ]


def field_tree_sha256(reader: Any) -> str:
    encoded = json.dumps(
        field_tree(reader), sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def inherited_value(obj: Any, key: str) -> Any:
    current = obj
    visited: set[int] = set()
    while current is not None:
        resolved = current.get_object() if hasattr(current, "get_object") else current
        identity = id(resolved)
        if identity in visited:
            return None
        visited.add(identity)
        if key in resolved:
            return resolved.get(key)
        current = resolved.get("/Parent")
    return None


def full_field_name(obj: Any) -> str | None:
    parts: list[str] = []
    current = obj
    visited: set[int] = set()
    while current is not None:
        resolved = current.get_object() if hasattr(current, "get_object") else current
        identity = id(resolved)
        if identity in visited:
            break
        visited.add(identity)
        if resolved.get("/T") is not None:
            parts.append(str(resolved.get("/T")))
        current = resolved.get("/Parent")
    return ".".join(reversed(parts)) if parts else None


def widget_inventory(reader: Any) -> list[dict[str, Any]]:
    widgets: list[dict[str, Any]] = []
    for page_index, page in enumerate(reader.pages, start=1):
        annotations = page.get("/Annots") or []
        for annotation in annotations:
            widget = annotation.get_object()
            if str(widget.get("/Subtype")) != "/Widget":
                continue
            appearance = widget.get("/AP")
            normal = None
            if appearance is not None:
                appearance = appearance.get_object()
                normal = appearance.get("/N")
            normal_states = []
            if normal is not None:
                resolved_normal = normal.get_object() if hasattr(normal, "get_object") else normal
                if hasattr(resolved_normal, "keys"):
                    normal_states = sorted(str(item) for item in resolved_normal.keys())
            rect = widget.get("/Rect")
            widgets.append(
                {
                    "page": page_index,
                    "field_name": full_field_name(widget),
                    "field_type": pdf_scalar(inherited_value(widget, "/FT")),
                    "value": pdf_scalar(inherited_value(widget, "/V")),
                    "appearance_state": pdf_scalar(widget.get("/AS")),
                    "has_normal_appearance": normal is not None,
                    "normal_appearance_states": normal_states,
                    "rect": [float(item) for item in rect] if rect is not None else None,
                }
            )
    return widgets


def fact_index(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    facts = document.get("facts")
    if not isinstance(facts, list):
        raise ValueError("project-facts.json must contain a facts array")
    result: dict[str, dict[str, Any]] = {}
    for fact in facts:
        fact_id = fact.get("id")
        if not isinstance(fact_id, str) or not fact_id:
            raise ValueError("every fact must have a non-empty id")
        if fact_id in result:
            raise ValueError(f"duplicate fact id: {fact_id}")
        result[fact_id] = fact
    return result


def confirmed_fact_value(fact: dict[str, Any]) -> tuple[bool, Any, str | None]:
    if fact.get("value") is None:
        return False, None, "value is null"
    if fact.get("source") is None:
        return False, None, "source receipt is missing"
    conflicts = fact.get("conflicts") or []
    if any(item.get("status") == "unresolved" for item in conflicts):
        return False, None, "fact has an unresolved conflict"
    confirmation = fact.get("confirmation") or {}
    if confirmation.get("required") and confirmation.get("status") != "confirmed":
        return False, None, "applicant confirmation is pending"
    return True, fact.get("value"), None
