"""A small JSON Schema validator, standard library only.

It supports the keywords that schemas/project.schema.json uses: type, enum,
const, properties, required, additionalProperties, items, minItems, maxItems,
minimum, exclusiveMinimum, pattern, minLength, propertyNames, oneOf, anyOf, allOf,
$ref (local "#/$defs/..." only). Unknown keywords are ignored, as the JSON Schema spec
allows.
"""
from __future__ import annotations

import json
import os
import re

_TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool,
    "null": type(None),
}

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "schemas", "project.schema.json")


def load_schema(path: str = SCHEMA_PATH) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _is_type(x, t: str) -> bool:
    if t == "number":
        return isinstance(x, (int, float)) and not isinstance(x, bool)
    if t == "integer":
        return isinstance(x, int) and not isinstance(x, bool)
    return isinstance(x, _TYPES[t])


def validate(doc, schema: dict) -> list[str]:
    """Return a list of 'path: message' errors. An empty list means valid."""
    errors: list[str] = []
    _check(doc, schema, schema, "$", errors)
    return errors


def validate_against(doc, schema: dict, root: dict, path: str = "$") -> list[str]:
    """Validate one part of a document against a schema whose $refs point into `root`."""
    errors: list[str] = []
    _check(doc, schema, root, path, errors)
    return errors


def _resolve(ref: str, root: dict) -> dict:
    if not ref.startswith("#/"):
        raise ValueError(f"only local $ref is supported: {ref}")
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def _check(x, s: dict, root: dict, path: str, errors: list[str]) -> None:
    if "$ref" in s:
        _check(x, _resolve(s["$ref"], root), root, path, errors)
        return
    t = s.get("type")
    if t is not None:
        types = t if isinstance(t, list) else [t]
        if not any(_is_type(x, tt) for tt in types):
            errors.append(f"{path}: expected {' or '.join(types)}, got {type(x).__name__}")
            return
    if "const" in s and x != s["const"]:
        errors.append(f"{path}: must be {s['const']!r}")
    if "enum" in s and x not in s["enum"]:
        errors.append(f"{path}: {x!r} is not one of {s['enum']}")
    if isinstance(x, str) and "pattern" in s and not re.search(s["pattern"], x):
        errors.append(f"{path}: {x!r} does not match {s['pattern']}")
    if isinstance(x, str) and "minLength" in s and len(x) < s["minLength"]:
        errors.append(f"{path}: must have at least {s['minLength']} characters")
    if _is_type(x, "number"):
        if "minimum" in s and x < s["minimum"]:
            errors.append(f"{path}: {x} < minimum {s['minimum']}")
        if "exclusiveMinimum" in s and x <= s["exclusiveMinimum"]:
            errors.append(f"{path}: {x} <= {s['exclusiveMinimum']}")
    if isinstance(x, list):
        if "minItems" in s and len(x) < s["minItems"]:
            errors.append(f"{path}: needs at least {s['minItems']} items")
        if "maxItems" in s and len(x) > s["maxItems"]:
            errors.append(f"{path}: allows at most {s['maxItems']} items")
        if "items" in s:
            for i, item in enumerate(x):
                _check(item, s["items"], root, f"{path}[{i}]", errors)
    if isinstance(x, dict):
        for req in s.get("required", []):
            if req not in x:
                errors.append(f"{path}: missing required field {req!r}")
        if "propertyNames" in s:
            for k in x:
                _check(k, s["propertyNames"], root, f"{path}.{k} (name)", errors)
        props = s.get("properties", {})
        addl = s.get("additionalProperties", True)
        for k, v in x.items():
            if k in props:
                _check(v, props[k], root, f"{path}.{k}", errors)
            elif addl is False:
                errors.append(f"{path}: unknown field {k!r}")
            elif isinstance(addl, dict):
                _check(v, addl, root, f"{path}.{k}", errors)
    for sub in s.get("allOf", []):
        _check(x, sub, root, path, errors)
    for key in ("oneOf", "anyOf"):
        if key in s:
            passing = 0
            sub_errs: list[tuple[bool, list[str]]] = []
            for sub in s[key]:
                e: list[str] = []
                _check(x, sub, root, path, e)
                sub_errs.append((_type_admits(x, sub, root), e))
                if not e:
                    passing += 1
            if passing == 0:
                # Report the branch written for this kind of input. An object
                # given for "number or Value" should hear what the Value lacks
                # (for example a missing status), not "expected number".
                fitting = [e for ok, e in sub_errs if ok] or [e for _, e in sub_errs]
                errors.extend(min(fitting, key=len) or [f"{path}: matches none of {key}"])
            elif key == "oneOf" and passing > 1:
                errors.append(f"{path}: matches more than one oneOf branch")


def _type_admits(x, s: dict, root: dict) -> bool:
    """True when the branch's declared type (through $ref and allOf) accepts x."""
    while "$ref" in s:
        s = _resolve(s["$ref"], root)
    if "type" in s:
        types = s["type"] if isinstance(s["type"], list) else [s["type"]]
        return any(_is_type(x, t) for t in types)
    return all(_type_admits(x, sub, root) for sub in s.get("allOf", []))
