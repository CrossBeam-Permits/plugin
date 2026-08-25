#!/usr/bin/env python3
"""Small dependency-free validator for the JSON Schema subset used by this skill."""

from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any
from urllib.parse import urlparse


def _resolve(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError(f"only local schema references are supported: {reference}")
    current: Any = root
    for token in reference[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[token]
    return current


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def validate_instance(instance: Any, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def visit(value: Any, rule: dict[str, Any], path: str) -> None:
        if "$ref" in rule:
            visit(value, _resolve(schema, rule["$ref"]), path)
            return
        if "anyOf" in rule:
            branches = []
            for candidate in rule["anyOf"]:
                before = len(errors)
                visit(value, candidate, path)
                branch_errors = errors[before:]
                del errors[before:]
                branches.append(branch_errors)
            if all(branch for branch in branches):
                errors.append(f"{path}: no anyOf branch matched: {branches}")
            return
        if "const" in rule and value != rule["const"]:
            errors.append(f"{path}: expected constant {rule['const']!r}, got {value!r}")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{path}: {value!r} is not in {rule['enum']!r}")
        expected_type = rule.get("type")
        if expected_type is not None:
            choices = [expected_type] if isinstance(expected_type, str) else expected_type
            if not any(_type_matches(value, item) for item in choices):
                errors.append(f"{path}: expected type {choices!r}, got {type(value).__name__}")
                return
        if isinstance(value, dict):
            required = rule.get("required") or []
            for name in required:
                if name not in value:
                    errors.append(f"{path}: missing required property {name}")
            properties = rule.get("properties") or {}
            if rule.get("additionalProperties") is False:
                for name in value:
                    if name not in properties:
                        errors.append(f"{path}: unexpected property {name}")
            for name, child in properties.items():
                if name in value:
                    visit(value[name], child, f"{path}.{name}")
        if isinstance(value, list):
            if "minItems" in rule and len(value) < rule["minItems"]:
                errors.append(f"{path}: requires at least {rule['minItems']} items")
            if rule.get("uniqueItems"):
                encoded = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
                if len(encoded) != len(set(encoded)):
                    errors.append(f"{path}: array items are not unique")
            if isinstance(rule.get("items"), dict):
                for index, item in enumerate(value):
                    visit(item, rule["items"], f"{path}[{index}]")
        if isinstance(value, str):
            if "minLength" in rule and len(value) < rule["minLength"]:
                errors.append(f"{path}: string is shorter than {rule['minLength']}")
            if "pattern" in rule and re.fullmatch(rule["pattern"], value) is None:
                errors.append(f"{path}: string does not match {rule['pattern']}")
            if rule.get("format") == "date-time":
                try:
                    datetime.fromisoformat(value.replace("Z", "+00:00"))
                except ValueError:
                    errors.append(f"{path}: invalid date-time")
            if rule.get("format") == "uri":
                parsed = urlparse(value)
                if not parsed.scheme or not parsed.netloc:
                    errors.append(f"{path}: invalid absolute URI")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in rule and value < rule["minimum"]:
                errors.append(f"{path}: value is below minimum {rule['minimum']}")
            if "maximum" in rule and value > rule["maximum"]:
                errors.append(f"{path}: value is above maximum {rule['maximum']}")

    visit(instance, schema, "$")
    return errors
