"""Text that prints model values, and compliance notes.

A note template names value keys in braces: "SILL AT {w1_sill:in} AFF".
The kit fills each one from project.json, in fractions, and appends the
field-verify tag of every unverified input. So a note can never show an
ASSUMED number without its tag, and QA knows which keys each note printed.

Format codes after the colon: ftin, in, both (lengths), auto (any unit: a
length in the auto style, below 10'-0" in inches; any other unit its default
form), sf (an area whose unit is sf), n (a plain number that is not a
length), u (a number with its unit word: 100 A, 50 CFM, 2 HR, 2500 PSI),
explain (the arithmetic of a DERIVED value). A value with no unit in
project.json is a length in inches. Write {{ and }} for literal braces. Any other
brace refuses the note, so a mistyped field never prints as literal text.

Plain numbers (sf, n) print at the precision of their source and never round
up: a literal prints its own decimals (50 prints 50, 7.6 prints 7.6), a
computed value is cut (not rounded) to two decimals. An area always shows at
least two decimals.
"""
from __future__ import annotations

import math
import re

from .model import KEY, PrintRefused, Project, Value, fv_text, range_text, source_places
from .units import UnitError, fmt_len, fmt_len_exact, unit_info, unit_word

_FIELD = re.compile(r"\{\{|\}\}|\{(" + KEY + r")(?::([a-z]+))?\}")
_LENGTH_CODES = ("ftin", "in", "both", "auto")


class Txt(str):
    """A string that remembers the value keys and FV tags it printed."""

    keys: tuple = ()
    fv: tuple = ()
    claims: bool = False
    depends_on: tuple = ()
    cd: tuple = ()

    def __new__(cls, s, keys=(), fv=(), claims=False, depends_on=(), cd=()):
        obj = super().__new__(cls, s)
        obj.keys = tuple(keys)
        obj.fv = tuple(fv)
        obj.claims = claims
        obj.depends_on = tuple(depends_on)
        obj.cd = cd_ids(cd)
        return obj


def cd_ids(cd) -> tuple:
    """Code-decision ids as a tuple. Takes None, one id, or a list of ids.

    The ids are metadata for QA. They never print.
    """
    if not cd:
        return ()
    ids = (cd,) if isinstance(cd, str) else tuple(cd)
    for i in ids:
        if not isinstance(i, str) or not re.fullmatch(r"CD-[0-9]+[A-Z]?", i):
            raise PrintRefused(f"cd={i!r} is not a code-decision id such as 'CD-014'")
    return tuple(dict.fromkeys(ids))


def tags_for(project: Project, val: Value) -> tuple:
    """FV tags a printed value must carry. Raises PrintRefused if one is missing."""
    if val.status == "PLACEHOLDER":
        raise PrintRefused(f"{val.key} is a PLACEHOLDER and is not a design value; do not print it")
    ph = [u for u in val.unverified_inputs if project.values[u].status == "PLACEHOLDER"]
    if ph:
        raise PrintRefused(f"{val.key} derives from PLACEHOLDER {ph}. A PLACEHOLDER is not a design "
                           "value, so nothing computed from it prints. Replace it first")
    if not val.unverified:
        return ()
    missing = [u for u in val.unverified_inputs if not project.values[u].fv]
    if missing:
        raise PrintRefused(f"{val.key} rests on unverified {missing} with no FV tag. "
                           "Add an fv tag and a field_verify entry before printing it")
    return tuple(val.fv_tags)


def number_text(val: Value, min_places: int = 0, toward: str | None = None) -> str:
    """A plain number at its source precision, never rounded up unless `toward` is "up".

    A literal `v` keeps its own decimals. A computed value keeps two decimals
    when it is not whole. The digits past the last place are cut, so a printed
    number is never larger than the value (69.996 prints 69.99, not 70.00).
    With toward="up" (a value a rule caps: Project.round_toward) they round up
    instead, so the number is never smaller than the value (0.3049 prints 0.31).
    """
    x = float(val)
    raw = val.raw.get("v") if isinstance(val.raw, dict) else None
    if isinstance(raw, int) and not isinstance(raw, bool) and min_places == 0:
        return str(raw)                     # exact, even past float precision
    source = source_places(raw)
    if source is not None:
        places = max(min_places, source)
    else:
        places = max(min_places, 0 if abs(x - round(x)) < 1e-9 else 2)
    scale = 10 ** places
    cut = (math.ceil(x * scale - 1e-6) if toward == "up" else math.floor(x * scale + 1e-6)) / scale
    return f"{cut:.{places}f}"


def _no_unit(val: Value) -> str:
    """How a refusal names a value's unit: a value with no unit in project.json is a length."""
    if isinstance(val.raw, dict) and "unit" not in val.raw:
        return (f"{val.key} has no unit in project.json, so it is a length in inches (the schema "
                "default). If it is not a length, set its unit (count, pct, sf, A, cfm, psi, hr, days ...)")
    return f"{val.key} is a length"


def value_text(project: Project, val: Value, code: str | None = None) -> str:
    """The printed form of one value, without tags. Raises PrintRefused when
    the format code does not fit the value's unit.

    A value that rests on a range of estimates prints its low and high end,
    9/16" TO 5/8" (a DERIVED value from a ranged input too); `explain` refuses it.
    """
    rng = None if code == "explain" or isinstance(val.v, (list, tuple)) or not val.unverified \
        else project.range_of(val.key)
    if rng is None:
        return _one_text(project, val, code)
    # Each end prints at the precision its own `range` entry was written with;
    # a derived end has no literal, so it prints like any computed number.
    literals = val.raw["range"] if project.own_range(val.key) else (None, None)
    texts = []
    for x, lit in zip(rng, literals):
        raw = {"unit": val.raw["unit"]} if "unit" in val.raw else {}
        if lit is not None:
            raw["v"] = lit
        texts.append(_one_text(project, Value(val.key, x, val.status, unit=val.unit, raw=raw), code))
    return range_text(*texts)


def _one_text(project: Project, val: Value, code: str | None = None) -> str:
    """value_text for one number."""
    # A length prints in the drawing's style, an area as sf, any other unit
    # (count, pct, cfm, A ...) as a plain number. 'auto' is that default for
    # any unit (a length in the auto length style); 'u' adds the unit word.
    if code == "auto" and val.unit != "in":
        code = None
    code = code or (project.dim_style if val.unit == "in" else "sf" if val.unit == "sf" else "n")
    if isinstance(val.v, (list, tuple)):
        raise PrintRefused(f"{val.key} is a point; print its coordinates as separate values")
    x = float(val)
    if code in _LENGTH_CODES:
        if val.unit != "in":
            raise PrintRefused(f"{val.key} has unit {val.unit}; it is not a length")
        if x and abs(x) * project.denom < 0.5:
            # it would print 0": keep its value in decimal inches (a 0.019 in. flashing)
            return fmt_len_exact(x, code, project.denom, source_places(val.raw.get("v"))
                                 if isinstance(val.raw, dict) else None)
        return fmt_len(x, code, project.denom, project.round_toward(val.key))
    if code == "sf":
        if val.unit != "sf":
            raise PrintRefused(f"{val.key} has unit {val.unit}, not sf. Store the area as its own "
                               "value with unit sf (for example an expr that divides by 144)")
        return number_text(val, 2, project.round_toward(val.key)) + " SQ FT"
    if code in ("n", "u"):
        if val.unit == "in":
            raise PrintRefused(f"{_no_unit(val)}; print it with a length format (ftin, in, both, auto), "
                               f"not {code!r}")
        try:
            dim, factor = unit_info(val.unit)
        except UnitError as exc:
            raise PrintRefused(f"{val.key}: {exc}") from None
        places = 2 if dim == "U-factor" or (dim == "percent" and factor != 1.0) else 0
        t = number_text(val, places, project.round_toward(val.key))
        if code == "n":
            return t
        if val.unit == "sf":
            return t + " SQ FT"
        if dim == "thermal resistance, R-value":
            return f"R-{t}"
        word = unit_word(val.unit)
        return t + ("" if not word else word if word == "%" else f" {word}")
    if code == "explain":
        return project.explain(val.key)
    raise PrintRefused(f"unknown format code {code!r} in a field for {val.key}; codes: ftin, in, both, "
                       "auto, sf, n, u, explain")


def fill(project: Project, template: str, claims: bool = False, depends_on=(), cd=()) -> Txt:
    """Fill a note template from project values. See the module docstring."""
    keys: list[str] = []
    tags: list[str] = []

    pos = 0
    for m in _FIELD.finditer(template):
        _no_stray_brace(template, template[pos:m.start()])
        pos = m.end()
    _no_stray_brace(template, template[pos:])

    def sub(m):
        tok = m.group(0)
        if tok == "{{":
            return "{"
        if tok == "}}":
            return "}"
        try:
            val = project.value(m.group(1))
        except KeyError as exc:
            raise PrintRefused(f"{exc.args[0]} (in note {template!r})") from None
        t = tags_for(project, val)
        if val.key not in keys:
            keys.append(val.key)
        for tag in t:
            if tag not in tags:
                tags.append(tag)
        return value_text(project, val, m.group(2)) + (f" ({fv_text(t)})" if t else "")

    text = _FIELD.sub(sub, str(template))
    deps = tuple(dict.fromkeys(list(keys) + list(depends_on)))
    if claims:
        project.check_claim(text, deps)
    return Txt(text, keys=keys, fv=tags, claims=claims, depends_on=deps, cd=cd)


def _no_stray_brace(template: str, gap: str) -> None:
    if "{" in gap or "}" in gap:
        raise PrintRefused(
            f"note {template!r} has a brace that is not a field. Write {{key}} or {{key:code}} "
            "with no spaces, using a known format code; write {{ and }} for a literal brace")
