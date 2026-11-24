"""Structural help for drafters: prescriptive span checks and a preliminary calc.

Two tools, one `structure` block in project.json (`references/structural.md`):

1. Prescriptive checks. Each member (floor joist, rafter, ceiling joist,
   header, footing) is looked up in the 2025 CRC tables that travel with the
   kit in `data/crc2025_structural.json`. Every row in that file was parsed
   from a quoted line of the repo's code corpus and carries its citation,
   edition and source line. The lookup becomes a code rule of the same shape
   as a `rules` entry, so the QA `rules` check reports it with PASS, FAIL or
   WARN. A case past the table, or a case the code sends to engineered design
   (R301.1.3, R301.2.2.6, R802.4.4 ...), reports "OUTSIDE PRESCRIPTIVE LIMITS
   — ENGINEER REQUIRED" and fails until an engineer's design is recorded.

2. A preliminary calc for a simple member past the tables: a simply supported
   beam or header under uniform and point loads (moment, shear, deflection)
   in sawn lumber, glulam or structural composite lumber (LVL, PSL). Reference
   design values and adjustment factors are NOT in the corpus, so they are
   inputs the drafter or engineer supplies, each with a citation; the kit has
   no defaults. The output is headed PRELIM_BANNER and a member sized only by
   this engine prints on the drawings as "PRELIM — BY ENGINEER".

Interpolation follows each table's own footnotes: across building width in
Tables R602.7(1) and R602.7(2), across soil bearing value for footing width
in Table R403.1(1), nowhere else. Where a tabulated condition is not met
exactly, the lookup uses the next more severe tabulated condition (a larger
spacing, a heavier dead load, a heavier snow load, a wider building, a
lower soil value) and says so; it never extrapolates past the last column.

Standard library only. Deterministic: no sets in output order, no clocks.
"""
from __future__ import annotations

import json
import math
import os
import re
from fractions import Fraction

from .units import UnitError, convert

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "crc2025_structural.json")

PRELIM_BANNER = ("PRELIMINARY — FOR REVIEW AND STAMP BY A CALIFORNIA-LICENSED ENGINEER. "
                 "NOT A STRUCTURAL DESIGN.")
PRELIM_LABEL = "PRELIM — BY ENGINEER"
ENGINEER = "OUTSIDE PRESCRIPTIVE LIMITS — ENGINEER REQUIRED"

MEMBER_TYPES = ("floor_joist", "rafter", "ceiling_joist", "header", "beam", "post", "footing")
TABLE_TYPES = ("floor_joist", "rafter", "ceiling_joist", "header", "footing")
LIVE_CASES = ("L", "Lr", "S")      # load cases whose deflection is "live load" deflection
#: Seismic design categories D0, D1, D2, and "D" when the sub-category is not yet known
#: (then every D0-D2 limit applies, the conservative reading).
SDC_D = ("D", "D0", "D1", "D2")
DESIGN_UNITS = ("psi", "plf", "lb", "in", "factor")
#: Adjustment factors a reviewer expects to see listed for each material and
#: property (listing one at 1.0 is fine). A checklist for the drafter only:
#: the engine multiplies exactly the factors given and never adds one.
EXPECTED_FACTORS = {
    "sawn": {"Fb": ("CM", "Ct", "CL", "CF", "Cfu", "Ci", "Cr"), "Fv": ("CM", "Ct", "Ci"), "E": ("CM", "Ct", "Ci")},
    "glulam": {"Fb": ("CM", "Ct", "CL", "CV", "Cfu", "Cc", "CI"), "Fv": ("CM", "Ct", "Cvr"), "E": ("CM", "Ct")},
    "scl": {"Fb": ("CM", "Ct", "CL", "CV", "Cr"), "Fv": ("CM", "Ct"), "E": ("CM", "Ct")},
}

_tables_cache: dict | None = None


def tables() -> dict:
    """The sourced table file (parsed once)."""
    global _tables_cache
    if _tables_cache is None:
        with open(DATA_FILE, encoding="utf-8") as fh:
            _tables_cache = json.load(fh)
    return _tables_cache


def provision(pid: str) -> dict:
    for p in tables()["provisions"]:
        if p["id"] == pid:
            return p
    raise KeyError(pid)


def ftin_in(text: str) -> int | None:
    """'14-2' -> 170 inches. Mechanical parse of the tables' feet-inches format."""
    m = re.fullmatch(r"(\d+)-(\d+)", text.replace(" ", ""))
    return int(m.group(1)) * 12 + int(m.group(2)) if m else None


def fmt_floor(inches: float, denom: int = 16) -> str:
    """A length in feet and inches, rounded DOWN to 1/denom in. (for an allowable)."""
    return _fmt(math.floor(inches * denom + 1e-9) / denom)


def fmt_ceil(inches: float, denom: int = 32) -> str:
    """A length rounded UP to 1/denom in. (for a computed deflection or demand)."""
    return _fmt(math.ceil(inches * denom - 1e-9) / denom, feet=False)


def _fmt(x: float, feet: bool = True) -> str:
    frac = Fraction(x).limit_denominator(64)
    ft = int(frac // 12) if feet and frac >= 12 else 0
    rest = frac - 12 * ft
    whole = int(rest)
    part = rest - whole
    ptxt = f"{part.numerator}/{part.denominator}" if part else ""
    if ft:
        inch = f"{whole}" + (f" {ptxt}" if ptxt else "")
        return f"{ft}'-{inch}\""
    if whole and ptxt:
        return f"{whole} {ptxt}\""
    return f"{ptxt or whole}\""


def norm_size(s: str) -> str:
    """'2 x 10', '2-2X10', '2-2 × 10' -> canonical '2x10' / '2-2x10'. Mechanical."""
    return s.replace(" ", "").replace("×", "x").replace("X", "x")


# ================================================================ registration (model.py)

def _is_value(node) -> bool:
    return isinstance(node, dict) and "status" in node and ("v" in node or "expr" in node) \
        and "citation" not in node


def _is_text(node) -> bool:
    return isinstance(node, dict) and "text" in node and "status" in node


def inline_values(block: dict) -> dict:
    """Value keys for the Values inside the structure block, for model.py.

    Every inline Value gets a key from its path: structure.criteria.wind_speed,
    structure.members.J-1.span, structure.members.B-1.calc.loads.0.trib. A list
    item with an `id` uses the id. A text criterion ({"text": "D2", "status":
    ...}) gets a status carrier, a count Value of 0 that carries the status and
    FV tag so checks that rest on it inherit them; print it with criteria_text().
    Design values (anything with a `citation`) stay with this module.
    """
    out: dict = {}

    def walk(node, path):
        if _is_value(node):
            out[path] = node
            return
        if _is_text(node):
            carrier = {"v": 0, "unit": "count", "status": node["status"],
                       "note": f"status of the text value {node['text']!r}"}
            for k in ("fv", "source"):
                if k in node:
                    carrier[k] = node[k]
            out[path] = carrier
            return
        if isinstance(node, dict):
            for k in sorted(node):
                walk(node[k], f"{path}.{k}")
        elif isinstance(node, list):
            for i, item in enumerate(node):
                ident = item.get("id") if isinstance(item, dict) else None
                walk(item, f"{path}.{ident if ident else i}")
    walk(block, "structure")
    return out


def fv_tags(block) -> set:
    """Every FV tag written anywhere in the structure block (design values included)."""
    out: set = set()

    def walk(node):
        if isinstance(node, dict):
            for t in str(node.get("fv") or "").split(","):
                if t.strip():
                    out.add(t.strip())
            for k in sorted(node):
                walk(node[k])
        elif isinstance(node, list):
            for x in node:
                walk(x)
    walk(block)
    return out


def attach(project) -> dict:
    """Run the structural checks, register their basis Values, and return the
    project data with the derived rules appended to `rules` (model.py calls this
    once, before its own checks, so QA's `rules` check reports them)."""
    res = Checker(project).run()
    project.struct = res
    for issue in res["issues"]:
        project.issue(issue["severity"], issue["code"], issue["where"], issue["msg"])
    data = dict(project.data)
    data["rules"] = list(project.data.get("rules", [])) + res["rules"]
    return data


# ================================================================ the checker

class Checker:
    def __init__(self, project):
        self.p = project
        self.block = project.data.get("structure", {})
        self.rows: list[dict] = []
        self.rules: list[dict] = []
        self.issues: list[dict] = []
        self.calcs: dict = {}
        self.members = self.block.get("members", [])
        self.crit = self.block.get("criteria", {})

    # ---- values

    def key(self, path: str, node):
        """The Value a field names: "$key" -> that value; inline -> its path key."""
        if node is None:
            return None
        if isinstance(node, str) and node.startswith("$"):
            try:
                return self.p.value(node)
            except KeyError:
                return None
        if isinstance(node, dict):
            return self.p.values.get(path)
        return None

    def mval(self, m, name):
        return self.key(f"structure.members.{m['id']}.{name}", m.get(name))

    def cval(self, name):
        return self.key(f"structure.criteria.{name}", self.crit.get(name))

    def ctext(self, name):
        node = self.crit.get(name)
        return node.get("text") if isinstance(node, dict) else None

    def issue(self, severity, code, where, msg):
        self.issues.append({"severity": severity, "code": code, "where": where, "msg": msg})

    # ---- rows

    def _basis(self, rid: str, drawn, inputs) -> object:
        """Register structure.checks.<rid>: the drawn value, tainted by every input it was checked with."""
        from .model import Value, parse_expr
        unverified, tags = [], []
        for v in [drawn] + [i for i in inputs if i is not None]:
            for u in v.unverified_inputs:
                if u not in unverified:
                    unverified.append(u)
        for u in unverified:
            fv = self.p._raw[u].get("fv")
            if fv and fv not in tags:
                tags.append(fv)
        key = f"structure.checks.{rid}"
        raw = {"expr": drawn.key, "status": "DERIVED", "unit": drawn.unit,
               "note": f"basis of structural check {rid}: {drawn.key} checked with "
                       f"{', '.join(i.key for i in inputs if i is not None) or 'no other input'}"}
        val = Value(key, drawn.v, "DERIVED", note=raw["note"], expr=drawn.key, unit=drawn.unit,
                    deps=[drawn.key], unverified_inputs=unverified, fv_tags=tags, raw=raw)
        self.p.values[key] = val
        self.p._raw[key] = raw
        self.p._trees[key] = parse_expr(drawn.key)
        return val

    def _count(self, rid: str, inputs) -> object:
        """A count Value of 1 meaning 'engineer required', tainted by its inputs."""
        from .model import Value
        unverified, tags = [], []
        for v in inputs:
            if v is None:
                continue
            for u in v.unverified_inputs:
                if u not in unverified:
                    unverified.append(u)
        for u in unverified:
            fv = self.p._raw[u].get("fv")
            if fv and fv not in tags:
                tags.append(fv)
        key = f"structure.checks.{rid}"
        raw = {"v": 1, "status": "DERIVED", "unit": "count", "expr": "1",
               "note": f"1 = engineered design required ({rid})"}
        val = Value(key, 1, "DERIVED", note=raw["note"], unit="count",
                    unverified_inputs=unverified, fv_tags=tags, raw=raw)
        self.p.values[key] = val
        self.p._raw[key] = raw
        from .model import parse_expr
        self.p._trees[key] = parse_expr("1")
        return val

    @staticmethod
    def _status(val, ok: bool):
        if val.unverified:
            return "warn", ("would pass" if ok else "WOULD FAIL")
        return ("pass" if ok else "fail"), None

    def check(self, rid, member, what, element, citation, drawn, op, limit, unit, inputs, lookup):
        """A comparable prescriptive check: drawn `op` limit. Adds a row and a rule."""
        basis = self._basis(rid, drawn, inputs)
        x = convert(float(drawn), drawn.unit, unit)
        tol = max(abs(limit), 1.0) * 1e-6
        ok = {"<=": x <= limit + tol, ">=": x >= limit - tol, "==": abs(x - limit) <= tol}[op]
        status, would = self._status(basis, ok)
        placeholders = [u for u in basis.unverified_inputs if self.p.values[u].status == "PLACEHOLDER"]
        row = {"id": rid, "member": member, "what": what, "element": element, "citation": citation,
               "status": status, "value": f"${basis.key}", "drawn_key": drawn.key, "drawn": x,
               "op": op, "limit": limit, "unit": unit, "fv": list(basis.fv_tags),
               "unverified": list(basis.unverified_inputs), "placeholder": placeholders,
               "would": would, "lookup": lookup, "engineer": False}
        self.rows.append(row)
        self.rules.append({"id": rid, "element": element, "citation": citation, "source_from": "code",
                           "kit_key": f"struct:{what}",
                           "check": {"value": f"${basis.key}", "op": op, "limit": limit, "unit": unit},
                           "note": lookup.get("trace", "")})
        return row

    def engineer(self, rid, member, what, reason, citation, inputs, lookup=None, element=None):
        """A case outside the prescriptive limits. Adds a row and a rule that fails until designed.
        `element` replaces the default '<reason>: OUTSIDE PRESCRIPTIVE LIMITS ...' wording."""
        cnt = self._count(rid, inputs)
        status = "warn" if cnt.unverified else "engineer"
        element = element or f"{reason}: {ENGINEER}"
        row = {"id": rid, "member": member, "what": what, "element": element,
               "citation": citation, "status": status, "value": f"${cnt.key}", "drawn": 1, "op": "==",
               "limit": 0, "unit": "count", "fv": list(cnt.fv_tags), "unverified": list(cnt.unverified_inputs),
               "placeholder": [], "would": "WOULD FAIL" if cnt.unverified else None,
               "lookup": lookup or {}, "engineer": True}
        self.rows.append(row)
        self.rules.append({"id": rid, "element": element, "citation": citation,
                           "source_from": "code", "kit_key": f"struct:{what}",
                           "check": {"value": f"${cnt.key}", "op": "==", "limit": 0, "unit": "count"},
                           "note": "1 = engineered design required. Record the engineer's design for this "
                                   "member (design: engineer, engineer.stamped: true) or change the design."})
        return row

    def need(self, m, names) -> list:
        """The member's Values for names; a missing one is an issue, returns None for it."""
        out = []
        for n in names:
            v = self.mval(m, n)
            if v is None:
                self.issue("warning", "struct-input-missing", f"structure.members.{m['id']}.{n}",
                           f"{m['type']} {m['id']} needs `{n}` (a Value or a \"$key\") for its table check")
            out.append(v)
        return out

    # ---- run

    def run(self) -> dict:
        ids = [m["id"] for m in self.members]
        for d in sorted({i for i in ids if ids.count(i) > 1}):
            self.issue("error", "struct-duplicate", f"structure.members.{d}", "member id appears twice")
        self.criteria_checks()
        for m in self.members:
            try:
                self.member(m)
            except UnitError as exc:
                self.issue("error", "struct-unit", f"structure.members.{m['id']}", str(exc))
        for b in self.block.get("bracing", []):
            self.bracing(b)
        self.triggers()
        for m in self.members:
            if m.get("calc"):
                self.calcs[m["id"]] = Calc(self, m).run()
        counts = {k: sum(1 for r in self.rows if r["status"] == k) for k in ("pass", "fail", "warn", "engineer")}
        return {"rows": self.rows, "rules": self.rules, "issues": self.issues, "calcs": self.calcs,
                "counts": counts, "members": {m["id"]: self.member_summary(m) for m in self.members},
                "edition": tables()["edition"]}

    # ---- design criteria and code triggers

    def sdc(self) -> str | None:
        t = self.ctext("seismic_design_category")
        return t.strip().upper() if t else None

    def criteria_checks(self):
        gs = self.cval("ground_snow_load")
        if gs is not None:
            pr = provision("snow_engineered")
            if float(gs) > pr["value"]:
                self.engineer("STRUCT-SNOW", None, "snow", "ground snow load over 70 psf", pr["citation"], [gs],
                              {"quote": pr["quote"]})
            else:
                self.check("STRUCT-SNOW", None, "snow", "ground snow load within the prescriptive range",
                           pr["citation"], gs, "<=", pr["value"], "psf", [], {"quote": pr["quote"]})
        sdc = self.sdc()
        sdc_v = self.cval("seismic_design_category")
        if sdc == "E":
            pr = provision("sdc_e")
            self.engineer("STRUCT-SDC-E", None, "seismic", "Seismic Design Category E", pr["citation"], [sdc_v],
                          {"quote": pr["quote"]})
        ws = self.cval("wind_speed")
        if ws is not None:
            pr = provision("wind_design")
            if float(ws) >= pr["value"]:
                self.engineer("STRUCT-WIND", None, "wind", f"ultimate design wind speed {float(ws):g} mph",
                              pr["citation"], [ws], {"quote": pr["quote"]})
            else:
                # the rule ops are <=, >=, ==; 140 mph itself took the engineer branch above
                self.check("STRUCT-WIND", None, "wind", f"ultimate design wind speed below {pr['value']:g} mph "
                           "(at or above it, wind design is required)",
                           pr["citation"], ws, "<=", pr["value"], "mph", [], {"quote": pr["quote"]})
        st = self.cval("stories")
        if st is not None and sdc in ("D", "D2"):
            pr = provision("d2_stories")
            self.check("STRUCT-D2-STORIES", None, "stories", "stories above grade in SDC D2", pr["citation"],
                       st, "<=", pr["value"], "count", [sdc_v], {"quote": pr["quote"]})
        if st is not None:
            pr = provision("stories_stamp")
            if float(st) > pr["value"]:
                self.engineer("STRUCT-STORIES", None, "stories", "woodframe dwelling over two stories",
                              pr["citation"], [st], {"quote": pr["quote"]})

    def triggers(self):
        """Engineered-design triggers the drafter answered (R301.2.2.6 irregularities and the like).
        `applies` is a count Value: 0 = does not apply, 1 = applies. Whether it applies is the
        drafter's reading of the code text, recorded with its status; the kit only counts it."""
        for t in self.block.get("triggers", []):
            v = self.key(f"structure.triggers.{t['id']}.applies", t.get("applies"))
            rid = f"STRUCT-TRIG-{t['id']}"
            if v is None:
                self.issue("warning", "struct-trigger-unanswered", f"structure.triggers.{t['id']}",
                           "trigger has no `applies` Value (0 or 1); it is not checked")
                continue
            if (t.get("engineer") or {}).get("stamped"):
                continue
            self.check(rid, t.get("member"), "trigger", f"{t['question']} (1 = yes: {ENGINEER})",
                       t["citation"], v, "==", 0, "count", [], {"trace": t.get("note", "")})

    # ---- members

    def member(self, m):
        mt = m["type"]
        design = m.get("design", "table")
        if design == "engineer" and (m.get("engineer") or {}).get("stamped"):
            return
        if design == "engineer":
            # by engineer, stamped design not in hand: an open item that fails until it is
            pr = provision("engineered_design")
            label = (m.get("label") or mt.replace("_", " "))
            self.engineer(f"STRUCT-{m['id']}-ENG", m["id"], "engineer_pending", f"{label} {m['id']}",
                          pr["citation"], [], {"quote": pr["quote"]},
                          element=f"{label} {m['id']}: by engineer, stamped design pending — ENGINEER REQUIRED")
            return
        if design == "prelim":
            return
        sdc = self.sdc()
        if mt == "floor_joist":
            self.span_member(m, [t for t in tables()["tables"].values() if t.get("member") == "floor_joist"])
            if sdc in SDC_D:
                self.dead_limit(m, "sdc_d_floor_dead", "floor dead load in SDC D0-D2")
        elif mt == "rafter":
            self.rafter(m)
            if sdc in SDC_D:
                self.dead_limit(m, "sdc_d_roof_dead", "roof and ceiling dead load in SDC D0-D2")
        elif mt == "ceiling_joist":
            attic = m.get("attic")
            tabs = [t for t in tables()["tables"].values() if t.get("member") == "ceiling_joist"
                    and t["attic"] == attic]
            if not tabs:
                self.issue("error", "struct-attic", f"structure.members.{m['id']}",
                           "ceiling joist needs attic: no_storage or limited_storage (Table R802.5.1(1) or (2))")
                return
            self.span_member(m, tabs)
        elif mt == "header":
            self.header(m)
        elif mt == "footing":
            self.footing(m)
        else:
            span = self.mval(m, "span")
            self.engineer(f"STRUCT-{m['id']}-TABLE", m["id"], "no_table",
                          f"{m['type']} {m['id']}: no prescriptive table covers this member",
                          provision("engineered_design")["citation"], [span],
                          {"quote": provision("engineered_design")["quote"]})

    def dead_limit(self, m, pid, what):
        dl = self.mval(m, "dead_load")
        if dl is None:
            return
        pr = provision(pid)
        self.check(f"STRUCT-{m['id']}-SDCDL", m["id"], "dead_load", f"{m['id']} {what}", pr["citation"],
                   dl, "<=", pr["value"], "psf", [self.cval("seismic_design_category")], {"quote": pr["quote"]})

    def species_ok(self, m) -> bool:
        if m.get("species") is None or m.get("grade") is None:
            self.issue("warning", "struct-input-missing", f"structure.members.{m['id']}",
                       f"{m['id']} needs species and grade for its table check")
            return False
        return True

    def span_member(self, m, tabs, load_psf=None, factor=1.0, factor_note=None, extra_inputs=()):
        """Floor joists, ceiling joists and rafters: one span table chosen from `tabs`.

        load_psf None: the member's live_load picks the table (floor and ceiling joists).
        load_psf given: the governing roof load picks it (rafters, R301.6).
        """
        mid = m["id"]
        if not self.species_ok(m):
            return
        names = ["span", "spacing", "dead_load"] + (["live_load"] if load_psf is None else [])
        vals = self.need(m, names)
        if any(v is None for v in vals):
            return
        span, spacing, dl = vals[:3]
        ll = vals[3] if load_psf is None else None
        inputs = [spacing, dl] + ([ll] if ll is not None else []) + list(extra_inputs)
        size = norm_size(m.get("size", ""))
        # the table: the lightest tabulated live load that is not less than the member's
        load = float(ll) if ll is not None else load_psf
        key = "live_load_psf" if ll is not None else "load_psf"
        cands = sorted((t for t in tabs if t.get(key) is not None and t[key] >= load - 1e-9), key=lambda t: t[key])
        if not cands:
            top = max(t[key] for t in tabs)
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                          f"{m['type']} {mid}: design load {load:g} psf is above the heaviest table ({top} psf)",
                          tabs[0]["citation"], [span] + inputs)
            return
        t = cands[0]
        dls = sorted(int(x) for x in t["dead_loads_psf"])
        dcol = next((d for d in dls if d >= float(dl) - 1e-9), None)
        if dcol is None:
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                          f"{m['type']} {mid}: dead load {float(dl):g} psf is above the table's {dls[-1]} psf",
                          t["citation"], [span] + inputs)
            return
        if size not in t["sizes"]:
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                          f"{m['type']} {mid}: size {m.get('size')} is not in {t['citation']} "
                          f"(sizes {', '.join(t['sizes'])})", t["citation"], [span] + inputs)
            return
        spacings = sorted({r["spacing_in"] for r in t["rows"]})
        sp = float(convert(float(spacing), spacing.unit, "in"))
        scol = next((s for s in spacings if s >= sp - 1e-6), None)
        if scol is None:
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                          f"{m['type']} {mid}: spacing {sp:g} in. is wider than the table's {spacings[-1]:g} in.",
                          t["citation"], [span] + inputs)
            return
        row = next((r for r in t["rows"] if r["spacing_in"] == scol and r["species"] == m["species"]
                    and r["grade"] == m["grade"]), None)
        if row is None:
            self.issue("error", "struct-no-row", f"structure.members.{mid}",
                       f"no row for {m['species']} {m['grade']} at {scol:g} in. in {t['citation']}")
            return
        cell = row["spans"][str(dcol)][size]
        limit = ftin_in(cell)
        notes = []
        ex = t.get("note_span_exceeds")
        foot = re.fullmatch(r"(\d+-\d+)([a-z])", cell.replace(" ", ""))   # "16-10a": a span with a footnote mark
        if foot:
            limit = ftin_in(foot.group(1))
            q = re.search(rf"(?:^|\.){foot.group(2)}\. (.+?\.)(?=[a-z]\. |$)", t.get("footnotes") or "")
            notes.append(f"{cell}: footnote {foot.group(2)}" + (f": {q.group(1)}" if q else ""))
        elif limit is None and ex and cell == ex["note"]:
            limit = ex["ft"] * 12
            notes.append(f"{cell}: {ex['quote']} Checked against {ex['ft']} ft")
        elif limit is None:
            self.issue("error", "struct-bad-cell", f"structure.members.{mid}",
                       f"{t['citation']} cell {cell!r} for {m['species']} {m['grade']} {size} is not a span")
            return
        tab_limit = limit
        limit = limit * factor
        if scol != sp:
            notes.append(f"used the {scol:g} in. spacing column for {sp:g} in. (next wider tabulated "
                         "spacing; the table has no interpolation)")
        if dcol != float(dl):
            notes.append(f"used the dead load = {dcol} psf column for {float(dl):g} psf")
        if load != t[key]:
            notes.append(f"used the {t[key]} psf table for {load:g} psf")
        if factor_note:
            notes.append(factor_note)
        trace = (f"{t['citation']} {t['conditions_line'] or ''}: {m['species']} {m['grade']} {size} "
                 f"@ {scol:g} in., dead load {dcol} psf -> {cell}"
                 + (f" x {factor:g} = {fmt_floor(limit)}" if factor != 1.0 else "")
                 + ("; " + "; ".join(notes) if notes else ""))
        lookup = {"table": t["id"], "citation": t["citation"], "edition": t["edition"],
                  "source_line": row["source_line"], "cell": cell, "tabulated_in": tab_limit,
                  "factor": factor, "limit_in": limit, "spacing_col": scol, "dead_col": dcol,
                  "notes": notes, "trace": trace}
        self.check(f"STRUCT-{mid}-SPAN", mid, "span",
                   f"{m.get('label') or m['type']} {mid} {size} @ {scol:g} in. span", t["citation"],
                   span, "<=", limit, "in", inputs, lookup)

    def rafter(self, m):
        mid = m["id"]
        slope = self.mval(m, "slope")
        pr = provision("ridge_beam_slope")
        if slope is not None:
            if float(slope) < pr["value"]:
                self.engineer(f"STRUCT-{mid}-SLOPE", mid, "slope",
                              f"rafter {mid}: roof slope {float(slope):g}:12 is below 3:12, so the ridge, hips "
                              "and valleys must be designed as beams", pr["citation"], [slope], {"quote": pr["quote"]})
            else:
                self.check(f"STRUCT-{mid}-SLOPE", mid, "slope", f"rafter {mid} roof slope (below 3:12 the ridge "
                           "is a designed beam)", pr["citation"], slope, ">=", pr["value"], "in/ft", [],
                           {"quote": pr["quote"]})
        else:
            self.issue("warning", "struct-input-missing", f"structure.members.{mid}.slope",
                       f"rafter {mid} needs slope (in/ft) for the R802.4.4 check")
        rll, gs = self.cval("roof_live_load"), self.cval("ground_snow_load")
        if rll is None or gs is None:
            self.issue("warning", "struct-input-missing", "structure.criteria",
                       "rafter checks need criteria roof_live_load and ground_snow_load (psf)")
            return
        if "ceiling_attached" not in m:
            self.issue("warning", "struct-input-missing", f"structure.members.{mid}.ceiling_attached",
                       f"rafter {mid} needs ceiling_attached (true/false) to pick the table")
            return
        # R301.6: the greater of roof live load and ground snow load governs
        gov = max(float(rll), float(gs))
        tabs = [t for t in tables()["tables"].values() if t.get("member") == "rafter"
                and t["ceiling_attached"] == bool(m["ceiling_attached"])]
        factor, fnote, extra = 1.0, None, []
        r = self.mval(m, "tie_height_ratio")
        if r is not None:
            adj = tables()["tables"]["R802.4.1(9)"]
            ratio = float(r)
            rows = sorted(adj["rows"], key=lambda x: x["hc_hr"])
            pick = next((x for x in rows if x["hc_hr"] >= ratio - 1e-9 or (x["or_less"] and ratio <= x["hc_hr"])),
                        None)
            if pick is None:
                self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                              f"rafter {mid}: ceiling joists or rafter ties at HC/HR {ratio:.3g}, above the "
                              "table's 1/3", adj["citation"], [r])
                return
            factor = pick["factor"]
            fnote = (f"{adj['citation']}: HC/HR {ratio:.3g} -> row {pick['cells'][0]} (next higher tabulated "
                     f"ratio), factor {pick['cells'][1]}")
            extra = [r]
        # the 20 psf roof-live-load tables and the 30/50/70 psf ground snow tables
        self.span_member(m, tabs, load_psf=gov, factor=factor, factor_note=fnote,
                         extra_inputs=[rll, gs] + extra)

    def header(self, m):
        mid = m["id"]
        wall = m.get("wall")
        tid = {"exterior": "R602.7(1)", "interior": "R602.7(2)"}.get(wall)
        if tid is None:
            self.issue("error", "struct-header-wall", f"structure.members.{mid}.wall",
                       "header needs wall: exterior or interior (Table R602.7(1) or R602.7(2))")
            return
        t = tables()["tables"][tid]
        if not self.species_ok(m):
            return
        span, bw = self.need(m, ["span", "building_width"])
        if span is None or bw is None:
            return
        inputs = [bw]
        size = norm_size(m.get("size", ""))
        sup = m.get("supporting")
        rows = [r for r in t["rows"] if r["supporting"] == sup]
        if not rows:
            self.issue("error", "struct-header-supporting", f"structure.members.{mid}.supporting",
                       f"supporting {sup!r} is not a row of {t['citation']}: "
                       + "; ".join(dict.fromkeys(r["supporting"] for r in t["rows"])))
            return
        if m["species"] not in ("Douglas fir-larch", "Hem-fir", "Southern pine", "Spruce-pine-fir") \
                or m["grade"] not in ("SS", "#1", "#2"):
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span",
                          f"header {mid}: {m['species']} {m['grade']} is outside the table basis ({t['species_note'] if 'species_note' in t else 'No. 2 grade'})",
                          t["citation"], [span])
            return
        row = next((r for r in rows if r["size"] == size), None)
        if row is None:
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span", f"header {mid}: size {m.get('size')} is not a row of "
                          f"{t['citation']} for {sup}", t["citation"], [span] + inputs)
            return
        notes = []
        vals = row["values"]
        if wall == "exterior":
            gs, rll = self.cval("ground_snow_load"), self.cval("roof_live_load")
            if gs is None or rll is None:
                self.issue("warning", "struct-input-missing", "structure.criteria",
                           "exterior header checks need criteria ground_snow_load and roof_live_load")
                return
            inputs += [gs, rll]
            g = float(gs)
            sf = t["snow_floor"]
            if g < sf["min_psf"] and float(rll) <= sf["max_roof_live_psf"]:
                notes.append(f"ground snow {g:g} psf: {sf['quote']}")
                g = sf["min_psf"]
            gcol = next((s for s in t["ground_snow_psf"] if s >= g - 1e-9), None)
            if gcol is None:
                self.engineer(f"STRUCT-{mid}-SPAN", mid, "span", f"header {mid}: ground snow {g:g} psf is "
                              f"above the table's {max(t['ground_snow_psf'])} psf", t["citation"], [span] + inputs)
                return
            if gcol != g:
                notes.append(f"used the {gcol} psf ground snow column for {g:g} psf (no interpolation of "
                             "snow load in this table)")
            vals = vals[str(gcol)]
        w = float(convert(float(bw), bw.unit, "ft"))
        widths = t["building_width_ft"]
        if w > widths[-1] + 1e-9:
            self.engineer(f"STRUCT-{mid}-SPAN", mid, "span", f"header {mid}: building width {w:.4g} ft is wider "
                          f"than the table's {widths[-1]} ft", t["citation"], [span] + inputs)
            return
        interp = t["interpolation"][0]["quote"]
        if w <= widths[0]:
            lo = hi = widths[0]
            if w < widths[0]:
                notes.append(f"used the {widths[0]} ft column for {w:.4g} ft (the narrowest tabulated width)")
        else:
            hi = next(x for x in widths if x >= w - 1e-9)
            lo = widths[widths.index(hi) - 1] if hi != w and widths.index(hi) > 0 else hi
        s_lo, s_hi = ftin_in(vals[str(lo)]["span"]), ftin_in(vals[str(hi)]["span"])
        nj = max(vals[str(lo)]["nj"], vals[str(hi)]["nj"])
        if lo == hi:
            limit = float(s_lo)
            cell = vals[str(lo)]["span"]
        else:
            limit = s_lo + (s_hi - s_lo) * (w - lo) / (hi - lo)
            cell = f"{vals[str(lo)]['span']} at {lo} ft, {vals[str(hi)]['span']} at {hi} ft"
            notes.append(f"interpolated for a {w:.4g} ft building width ({interp}): "
                         f"{s_lo} + ({s_hi} - {s_lo}) x ({w:.4g} - {lo}) / ({hi} - {lo}) = {limit:.2f} in.")
            if vals[str(lo)]["nj"] != vals[str(hi)]["nj"]:
                notes.append(f"NJ {vals[str(lo)]['nj']} and {vals[str(hi)]['nj']} in the two columns; the "
                             f"larger, {nj}, is required (NJ is not interpolated)")
        tab = limit
        ub = t["unbraced_top"]
        top = m.get("top_braced")
        if top is None:
            self.issue("warning", "struct-input-missing", f"structure.members.{mid}.top_braced",
                       f"header {mid} needs top_braced (true when perpendicular framing braces its top)")
            return
        if not top and any(size.endswith(s) for s in ub["sizes"]):
            limit *= ub["factor"]
            notes.append(f"top not laterally braced: x {ub['factor']:.2f} ({ub['quote']})")
        trace = (f"{t['citation']}: {sup}, {size}, building width {w:.4g} ft -> {cell}; max span "
                 f"{fmt_floor(limit)}, NJ = {nj}" + ("; " + "; ".join(notes) if notes else ""))
        lookup = {"table": tid, "citation": t["citation"], "edition": t["edition"], "source_line": row["source_line"],
                  "cell": cell, "tabulated_in": tab, "limit_in": limit, "nj": nj, "notes": notes, "trace": trace}
        self.check(f"STRUCT-{mid}-SPAN", mid, "span", f"{m.get('label') or 'header'} {mid} {size} span",
                   t["citation"], span, "<=", limit, "in", inputs, lookup)
        js = self.mval(m, "jack_studs")
        if js is not None:
            self.check(f"STRUCT-{mid}-NJ", mid, "jack_studs", f"header {mid} jack studs each end ({t['nj_note']})",
                       t["citation"], js, ">=", nj, "count", inputs, {"trace": trace, "nj": nj})
        if wall == "exterior":
            self.full_height(m, span)

    def full_height(self, m, span):
        mid = m["id"]
        fh = self.mval(m, "full_height_studs")
        if fh is None:
            return
        t = tables()["tables"]["R602.7.5"]
        ws, exp = self.cval("wind_speed"), self.ctext("wind_exposure")
        if ws is None or exp is None:
            self.issue("warning", "struct-input-missing", "structure.criteria",
                       "full-height stud check needs criteria wind_speed (mph) and wind_exposure (text)")
            return
        v, e = float(ws), exp.strip().upper()
        jacks = self.mval(m, "jack_studs")
        def within(colkey):  # the column header's own wind limits (data file column_limits)
            return any(e == lim["exposure"] and (v <= lim["mph"] if lim["op"] == "<=" else v < lim["mph"])
                       for lim in t["column_limits"][colkey])
        # note b: the 115 mph column applies where jack studs support the header
        if within("le115B") and jacks is not None and float(jacks) >= 1:
            col = "le115B"
        elif within("lt140B_lt130C"):
            col = "lt140B_lt130C"
        else:
            self.engineer(f"STRUCT-{mid}-FHS", mid, "full_height_studs",
                          f"header {mid}: {v:g} mph Exposure {e} is outside Table R602.7.5", t["citation"],
                          [ws, self.cval("wind_exposure")])
            return
        sp_ft = float(convert(float(span), span.unit, "ft"))
        row = next((r for r in t["rows"] if r["max_span_ft"] >= sp_ft - 1e-9), None)
        if row is None:
            self.engineer(f"STRUCT-{mid}-FHS", mid, "full_height_studs",
                          f"header {mid}: span over {t['rows'][-1]['max_span_ft']} ft", t["citation"], [span])
            return
        need = row["studs"][col]
        trace = (f"{t['citation']}: span {sp_ft:.4g} ft -> row {row['max_span_ft']} ft ({t['between_rule']}); "
                 f"column {t['columns'][col]} -> {need}")
        self.check(f"STRUCT-{mid}-FHS", mid, "full_height_studs", f"header {mid} full-height studs each end",
                   t["citation"], fh, ">=", need, "count", [ws, self.cval("wind_exposure"), span],
                   {"trace": trace, "source_line": row["source_line"]})

    def footing(self, m):
        mid = m["id"]
        t = tables()["tables"]["R403.1(1)"]
        width, thick, soil = self.need(m, ["width", "thickness", "soil_bearing"])
        if width is None or thick is None or soil is None:
            return
        gs, rll = self.cval("ground_snow_load"), self.cval("roof_live_load")
        if gs is None or rll is None:
            self.issue("warning", "struct-input-missing", "structure.criteria",
                       "footing checks need criteria ground_snow_load and roof_live_load")
            return
        story = m.get("story")
        labels = list(dict.fromkeys(r["story"] for r in t["rows"]))
        if story not in labels:
            self.issue("error", "struct-footing-story", f"structure.members.{mid}.story",
                       f"story {story!r} is not a row of {t['citation']}: {'; '.join(labels)}")
            return
        g, r = float(gs), float(rll)
        notes = []
        first = next(k for k, x in t["loads"].items() if "roof_live_psf" in x)   # the first load row
        if r <= t["loads"][first]["roof_live_psf"] and g <= t["loads"][first]["ground_snow_psf"]:
            load = first
        else:
            load = next((k for k, v in t["loads"].items() if k != first and v["ground_snow_psf"] >= max(g, r) - 1e-9),
                        None)
            if load is None:
                self.engineer(f"STRUCT-{mid}-W", mid, "footing", f"footing {mid}: snow {g:g} psf over the table",
                              t["citation"], [gs, rll])
                return
        row = next(x for x in t["rows"] if x["load"] == load and x["story"] == story)
        soils = t["soil_psf"]
        s = float(soil)
        inputs = [soil, gs, rll]
        if s < soils[0] - 1e-9:
            self.engineer(f"STRUCT-{mid}-W", mid, "footing", f"footing {mid}: soil bearing {s:g} psf is below the "
                          f"table's {soils[0]} psf (extrapolation is not permitted)", t["citation"], inputs)
            return
        if s >= soils[-1]:
            lo = hi = soils[-1]
            if s > soils[-1]:
                notes.append(f"used the {soils[-1]} psf column for {s:g} psf (the last column; no extrapolation)")
        else:
            hi = next(x for x in soils if x >= s - 1e-9)
            lo = hi if hi == s else soils[soils.index(hi) - 1]
        a, b = row["values"][str(lo)], row["values"][str(hi)]
        if lo == hi:
            w_req = float(a["width_in"])
        else:
            w_req = a["width_in"] + (b["width_in"] - a["width_in"]) * (s - lo) / (hi - lo)
            notes.append(f"width interpolated between {lo} and {hi} psf ({t['interpolation'][0]['quote']})")
        t_req = float(max(a["thickness_in"], b["thickness_in"]))
        if lo != hi and a["thickness_in"] != b["thickness_in"]:
            notes.append("thickness: the larger of the two columns (the table permits interpolation of width only)")
        bwv = self.mval(m, "building_width")
        adj = t["width_adjust"]
        if bwv is None:
            notes.append(f"building width not given: the table's {adj['basis_ft']} ft basis is used with no "
                         "decrease; a wider building needs a wider footing")
        else:
            inputs.append(bwv)
            bw = float(convert(float(bwv), bwv.unit, "ft"))
            if bw > adj["basis_ft"]:
                steps = math.ceil((bw - adj["basis_ft"]) / adj["step_ft"] - 1e-9)
                w_req += steps * adj["width_in"]
                t_req += steps * adj["thickness_in"]
                notes.append(f"building width {bw:.4g} ft: +{steps} x 4 ft step(s), rounded up ({adj['quote_increase']})")
            elif bw < adj["basis_ft"]:
                steps = math.floor((adj["basis_ft"] - bw) / adj["step_ft"] + 1e-9)
                if steps:
                    w_req = max(adj["min_width_in"], w_req - steps * adj["width_in"])
                    t_req = max(adj["min_thickness_in"], t_req - steps * adj["thickness_in"])
                    notes.append(f"building width {bw:.4g} ft: -{steps} full 4 ft step(s) ({adj['quote_decrease']})")
        mn = provision("footing_min")
        w_req, t_req = max(w_req, float(mn["value"])), max(t_req, float(mn["depth_in"]))
        trace = (f"{t['citation']}: {load}, {story}, soil {s:g} psf -> {fmt_floor(w_req)} wide x "
                 f"{fmt_floor(t_req)} thick" + ("; " + "; ".join(notes) if notes else "")
                 + f"; minimum per {mn['citation']}")
        lookup = {"table": t["id"], "citation": t["citation"], "edition": t["edition"],
                  "source_line": row["source_line"], "width_in": w_req, "thickness_in": t_req,
                  "notes": notes, "trace": trace}
        self.check(f"STRUCT-{mid}-W", mid, "footing_width", f"footing {mid} width", t["citation"],
                   width, ">=", w_req, "in", inputs, lookup)
        self.check(f"STRUCT-{mid}-T", mid, "footing_thickness", f"footing {mid} thickness", t["citation"],
                   thick, ">=", t_req, "in", inputs, lookup)

    def bracing(self, b):
        bid = b["id"]
        path = f"structure.bracing.{bid}"
        sp = self.key(f"{path}.spacing", b.get("spacing"))
        t = tables()["tables"]["R602.10.1.3"]
        sdc = self.sdc()
        sdc_v = self.cval("seismic_design_category")
        if sp is not None and sdc:
            exc = b.get("exception")
            if sdc in SDC_D:
                rows = [r for r in t["rows"] if r["condition"] == "SDC D0, D1, D2"]
                row = rows[0] if exc == "single_room_900sf" else rows[-1] if exc == "adjusted_bracing" else rows[0]
                lim = row["max_ft"]
                if exc in ("single_room_900sf", "adjusted_bracing"):
                    lim = row["exception_max_ft"] or lim
                inputs = [sdc_v]
            elif sdc in ("A", "B", "C") and b.get("building", "detached") == "detached":
                row = next(r for r in t["rows"] if r["application"] == "Wind bracing")
                lim = row["max_ft"]
                ws = self.cval("wind_speed")
                inputs = [sdc_v, ws]
                if ws is not None and float(ws) >= provision("wind_design")["value"]:
                    self.engineer(f"STRUCT-BWL-{bid}", None, "bracing", f"braced wall line {bid}: wind "
                                  f"{float(ws):g} mph is outside Table R602.10.1.3", t["citation"], inputs)
                    row = None
            else:
                row = None
                self.issue("warning", "struct-bracing-case", path, f"SDC {sdc} {b.get('building')}: this kit "
                           "checks detached dwellings only; read Table R602.10.1.3 for this case")
            if row is not None:
                trace = f"{t['citation']}: {row['application']}, {row['condition']}, {row['building']} -> {lim} ft" + \
                        (f" (exception: {row['exception']})" if exc else "")
                self.check(f"STRUCT-BWL-{bid}", None, "bracing_spacing",
                           f"braced wall line {bid} spacing", t["citation"], sp, "<=", lim, "ft", inputs,
                           {"trace": trace, "source_line": row["source_line"]})
        req = self.key(f"{path}.required_length", b.get("required_length"))
        prov = self.key(f"{path}.provided_length", b.get("provided_length"))
        if prov is not None and req is not None:
            self.check(f"STRUCT-BWL-{bid}-LEN", None, "bracing_length",
                       f"braced wall line {bid} bracing length (required length from {b.get('required_citation', 'the drafter')})",
                       b.get("required_citation") or "2025 CRC R602.10.3", prov, ">=",
                       float(convert(float(req), req.unit, prov.unit)), prov.unit, [req],
                       {"trace": f"required {req.key}; Tables R602.10.3(1) and R602.10.3(3) are read by the drafter "
                                 "(the seismic table in the corpus lost its story-location column)"})

    # ---- what a member prints as

    def member_summary(self, m) -> dict:
        rows = [r for r in self.rows if r["member"] == m["id"]]
        design = m.get("design", "table")
        eng = m.get("engineer") or {}
        if design == "engineer" and eng.get("stamped"):
            status = "engineer-design"
        elif design == "engineer":
            status = "engineer-pending"
        elif design == "prelim":
            status = "prelim"
        elif any(r["engineer"] for r in rows):
            status = "engineer"
        elif any(r["status"] == "fail" for r in rows):
            status = "fail"
        elif any(r["status"] == "warn" for r in rows):
            status = "warn"
        elif rows:
            status = "pass"
        else:
            status = "unchecked"
        return {"type": m["type"], "design": design, "status": status, "rows": [r["id"] for r in rows],
                "size": m.get("size")}


# ================================================================ preliminary calc

def _value_source(v, prefix=""):
    """Where a kit Value comes from, for the calc input table: its key, formula, source id and note."""
    key = v.key[len(prefix):] if prefix and v.key.startswith(prefix) else v.key
    parts = [f"PROJECT FILE {key}"]
    if v.expr:
        parts.append(f"= {v.expr}")
    if v.source:
        parts.append(f"SOURCE {v.source}")
    if v.note:
        parts.append(str(v.note)[:90])
    return "; ".join(parts)


class Calc:
    """Simply supported member: moment, shear, deflection, from supplied design values."""

    def __init__(self, checker: Checker, m: dict):
        self.ck = checker
        self.p = checker.p
        self.m = m
        self.c = m["calc"]
        self.base = f"structure.members.{m['id']}.calc"
        self.inputs: list[dict] = []
        self.missing: list[str] = []
        self.errors: list[str] = []
        self.unverified: list[str] = []
        self.placeholders: list[str] = []
        self.tags: list[str] = []

    # ---- inputs

    def _record(self, name, v, unit, status, src, fv, key=None, note=None):
        self.inputs.append({"name": name, "v": v, "unit": unit, "status": status, "source": src, "fv": fv,
                            "key": key, "note": note})
        if status in ("ASSUMED", "PLACEHOLDER"):
            if name not in self.unverified:
                self.unverified.append(name)
            if status == "PLACEHOLDER":
                self.placeholders.append(name)
        if fv and fv not in self.tags:
            self.tags.append(fv)

    def kit(self, name, path, node, unit):
        """A kit Value (span, trib width, psf, lb) as a number in `unit`."""
        if node is None:
            self.missing.append(name)
            return None
        v = self.ck.key(path, node)
        if v is None:
            self.errors.append(f"{name}: {node!r} is not a value key")
            return None
        try:
            x = convert(float(v), v.unit, unit)
        except (UnitError, TypeError) as exc:
            self.errors.append(f"{name}: {exc}")
            return None
        status = "ASSUMED" if v.unverified and not any(
            self.p.values[u].status == "PLACEHOLDER" for u in v.unverified_inputs) else (
            "PLACEHOLDER" if v.unverified else v.status)
        tags = list(v.fv_tags)
        self._record(name, x, unit, status, _value_source(v, self.base.rsplit(".", 1)[0] + "."),
                     ", ".join(tags) or None, key=v.key, note=v.note)
        return x

    def design(self, name, node, unit):
        """A design value or factor: inline, with a citation, never a default."""
        if node is None:
            self.missing.append(name)
            return None
        if isinstance(node, str) and node.startswith("$"):
            return self.kit(name, None, node, unit)
        if not isinstance(node, dict) or "v" not in node:
            self.errors.append(f"{name}: not a design value")
            return None
        cite = (node.get("citation") or "").strip()
        if not cite:
            self.errors.append(f"{name}: no citation. Design values and factors come only from a recorded "
                               "source (NDS Supplement table, manufacturer evaluation report); the kit has no "
                               "defaults")
            return None
        if node.get("unit", unit) != unit:
            self.errors.append(f"{name}: unit {node.get('unit')!r}, expected {unit!r}")
            return None
        fv = node.get("fv")
        if node["status"] == "ASSUMED" and not fv:
            self.errors.append(f"{name}: ASSUMED with no fv tag")
        if fv and fv not in self.p.fv:
            self.errors.append(f"{name}: fv tag {fv} is not in field_verify")
        self._record(name, float(node["v"]), unit, node["status"], cite, fv, note=node.get("note"))
        return float(node["v"])

    # ---- run

    def run(self) -> dict:
        c, m = self.c, self.m
        mat = c.get("material")
        L = self.kit("L (span)", f"{self.base}.span" if "span" in c else f"structure.members.{m['id']}.span",
                     c.get("span", m.get("span")), "in")
        b = self.section("b", c.get("b"))
        d = self.section("d", c.get("d"))
        plies = int(c.get("plies", 1))
        Fb = self.design("Fb", c.get("Fb"), "psi")
        Fv = self.design("Fv", c.get("Fv"), "psi")
        E = self.design("E", c.get("E"), "psi")
        fac = {}
        for prop in ("Fb", "Fv", "E"):
            fac[prop] = {}
            for fname in sorted((c.get("factors") or {}).get(prop, {})):
                fac[prop][fname] = self.design(f"{fname} ({prop})", c["factors"][prop][fname], "factor")
        loads = self.loads()
        combos = []
        for i, cb in enumerate(c.get("combos", [])):
            if not (cb.get("citation") or "").strip():
                self.errors.append(f"combination {cb.get('name', i)}: no citation")
            cd = self.design(f"CD ({cb.get('name', i)})", cb.get("CD"), "factor")
            combos.append({"name": cb.get("name", f"combo {i + 1}"), "factors": dict(cb.get("factors", {})),
                           "CD": cd, "citation": cb.get("citation")})
        if not combos:
            self.missing.append("combos (load combinations, each with CD and a citation)")
        defl = self.deflection_limits()
        checklist = [f"{prop}: {', '.join(n for n in EXPECTED_FACTORS.get(mat, {}).get(prop, ()) if n not in fac[prop])}"
                     for prop in ("Fb", "Fv", "E")
                     if any(n not in fac[prop] for n in EXPECTED_FACTORS.get(mat, {}).get(prop, ()))]
        out = {"member": m["id"], "label": m.get("label"), "size": m.get("size"), "material": mat,
               "banner": PRELIM_BANNER, "inputs": self.inputs, "missing": self.missing, "errors": self.errors,
               "unverified": self.unverified, "placeholders": self.placeholders, "fv": self.tags,
               "factor_checklist": checklist, "deflection": defl, "status": None}
        if mat not in EXPECTED_FACTORS:
            self.errors.append(f"material {mat!r}: use sawn, glulam or scl")
        for ld in loads or ():
            if ld["kind"] == "point" and L is not None and not 0 <= ld["a"] <= L:
                self.errors.append(f"load {ld['id']}: a = {ld['a']:g} in. is outside the span (0 to {L:g} in.)")
        if self.errors or self.missing or None in (L, b, d, Fb, Fv, E) or any(
                v is None for f in fac.values() for v in f.values()) or any(cb["CD"] is None for cb in combos) \
                or loads is None or defl is None:
            out["status"] = "input-required"
            return out
        if self.placeholders:
            out["status"] = "placeholder"
            return out
        res = beam(L, loads, combos, b * plies, d, Fb, Fv, E, fac, defl)
        out.update(res)
        out["status"] = "unverified" if self.unverified else "computed"
        return out

    def section(self, name, node):
        if isinstance(node, dict) and "citation" in node:
            return self.design(name, node, "in")
        return self.kit(name, f"{self.base}.{name}", node, "in")

    def loads(self):
        out = []
        ok = True
        for i, ld in enumerate(self.c.get("loads", [])):
            lid = ld.get("id", str(i))
            path = f"{self.base}.loads.{lid}"
            case = ld.get("case")
            if case not in ("D", "L", "Lr", "S"):
                self.errors.append(f"load {lid}: case must be D, L, Lr or S")
                ok = False
                continue
            if ld.get("kind") == "uniform":
                if "plf" in ld:
                    w = self.design(f"w {lid} ({case})", ld["plf"], "plf")
                    w = None if w is None else w / 12.0
                else:
                    q = self.kit(f"q {lid} ({case})", f"{path}.psf", ld.get("psf"), "psf")
                    t = self.kit(f"trib {lid}", f"{path}.trib", ld.get("trib"), "in")
                    w = None if q is None or t is None else q * t / 144.0     # lb per in. of span
                if w is None:
                    ok = False
                    continue
                out.append({"id": lid, "kind": "uniform", "case": case, "w": w})
            elif ld.get("kind") == "point":
                P = self.kit(f"P {lid} ({case})", f"{path}.P", ld.get("P"), "lb")
                a = self.kit(f"a {lid}", f"{path}.a", ld.get("a"), "in")
                if P is None or a is None:
                    ok = False
                    continue
                out.append({"id": lid, "kind": "point", "case": case, "P": P, "a": a})
            else:
                self.errors.append(f"load {lid}: kind must be uniform or point")
                ok = False
        if not out:
            self.missing.append("loads")
            return None
        return out if ok else None

    def deflection_limits(self):
        d = self.c.get("deflection") or {}
        t1, t2 = tables()["tables"]["R301.7"], tables()["tables"]["1604.3"]
        live = next((r for r in t1["rows"] if r["member"] == d.get("live")), None)
        tot = next((r for r in t2["rows"] if r["member"] == d.get("total")), None)
        if live is None or live["ratio"] is None:
            self.missing.append("deflection.live: a STRUCTURAL MEMBER row of Table R301.7, one of "
                                + "; ".join(r["member"] for r in t1["rows"] if r["ratio"]))
            return None
        if tot is None or tot["total_ratio"] is None:
            self.missing.append("deflection.total: a CONSTRUCTION row of Table 1604.3 with a D + L limit, one of "
                                + "; ".join(r["member"] for r in t2["rows"] if r.get("total_ratio")))
            return None
        if "dry_service" not in d:
            self.missing.append("deflection.dry_service (true: dry at installation and in use)")
            return None
        creep = t2["creep"]["dry"] if d["dry_service"] else t2["creep"]["other"]
        return {"live_ratio": live["ratio"], "live_row": live["member"], "live_citation": t1["citation"],
                "live_source": live["source_line"], "total_ratio": tot["total_ratio"], "total_row": tot["member"],
                "total_citation": t2["citation"], "total_source": tot["source_line"], "creep": creep,
                "creep_quote": t2["creep"]["quote"] if d["dry_service"] else t2["creep"]["quote_other"]}


def beam(L, loads, combos, B, d, Fb, Fv, E, fac, defl, n: int = 400) -> dict:
    """Simply supported rectangular member. Lengths in., forces lb, stresses psi.

    loads: [{"kind": "uniform", "case", "w" (lb/in)} | {"kind": "point", "case", "P" (lb), "a" (in)}]
    Bending and shear are checked for each combination (its load factors and CD);
    deflection under the service loads: live = L, Lr and S cases, total = creep x D + live
    (CBC Table 1604.3 note d). Moment and deflection are evaluated on n + 1 points
    plus the point-load positions; shear is the larger support reaction.
    """
    A = B * d
    S = B * d * d / 6.0
    I = B * d ** 3 / 12.0
    xs = sorted({L * i / n for i in range(n + 1)} | {ld["a"] for ld in loads if ld["kind"] == "point"})

    def effects(fn):
        """(max moment, max reaction) for loads weighted by fn(case)."""
        RA = RB = 0.0
        for ld in loads:
            f = fn(ld["case"])
            if ld["kind"] == "uniform":
                RA += f * ld["w"] * L / 2
                RB += f * ld["w"] * L / 2
            else:
                RA += f * ld["P"] * (L - ld["a"]) / L
                RB += f * ld["P"] * ld["a"] / L
        best = 0.0
        for x in xs:
            M = 0.0
            for ld in loads:
                f = fn(ld["case"])
                if ld["kind"] == "uniform":
                    M += f * ld["w"] * x * (L - x) / 2
                else:
                    a = ld["a"]
                    M += f * ld["P"] * ((L - a) * x / L if x <= a else a * (L - x) / L)
            best = max(best, M)
        return best, max(RA, RB)

    def deflect(fn, Ep):
        best = 0.0
        for x in xs:
            y = 0.0
            for ld in loads:
                f = fn(ld["case"])
                if not f:
                    continue
                if ld["kind"] == "uniform":
                    y += f * ld["w"] * x * (L ** 3 - 2 * L * x * x + x ** 3) / (24 * Ep * I)
                else:
                    a = ld["a"]
                    bb = L - a
                    if x <= a:
                        y += f * ld["P"] * bb * x * (L * L - bb * bb - x * x) / (6 * Ep * I * L)
                    else:
                        y += f * ld["P"] * a * (L - x) * (L * L - a * a - (L - x) ** 2) / (6 * Ep * I * L)
            best = max(best, y)
        return best

    prod = {k: math.prod(v.values()) if v else 1.0 for k, v in fac.items()}
    rows = []
    for cb in combos:
        M, V = effects(lambda case, cb=cb: float(cb["factors"].get(case, 0.0)))
        fb, fv = M / S, 1.5 * V / A
        Fbp = Fb * cb["CD"] * prod["Fb"]
        Fvp = Fv * cb["CD"] * prod["Fv"]
        rows.append({"name": cb["name"], "factors": cb["factors"], "CD": cb["CD"], "citation": cb["citation"],
                     "M": M, "V": V, "fb": fb, "Fb_adj": Fbp, "fb_ratio": fb / Fbp, "fv": fv, "Fv_adj": Fvp,
                     "fv_ratio": fv / Fvp})
    Ep = E * prod["E"]
    d_live = deflect(lambda case: 1.0 if case in LIVE_CASES else 0.0, Ep)
    d_dead = deflect(lambda case: 1.0 if case == "D" else 0.0, Ep)
    d_total = defl["creep"] * d_dead + d_live
    lim_live, lim_total = L / defl["live_ratio"], L / defl["total_ratio"]
    gov_b = max(rows, key=lambda r: r["fb_ratio"])
    gov_v = max(rows, key=lambda r: r["fv_ratio"])
    ratios = {"bending": gov_b["fb_ratio"], "shear": gov_v["fv_ratio"], "deflection_live": d_live / lim_live,
              "deflection_total": d_total / lim_total}
    return {"section": {"B": B, "d": d, "A": A, "S": S, "I": I}, "combos": rows,
            "factor_products": prod, "E_adj": Ep,
            "deflection_results": {"live": d_live, "dead": d_dead, "total": d_total, "limit_live": lim_live,
                                   "limit_total": lim_total},
            "ratios": ratios, "within": all(v <= 1.0 + 1e-9 for v in ratios.values()),
            "governing": {"bending": gov_b["name"], "shear": gov_v["name"]}}


# ================================================================ output: report, labels, panels, package

def result(project) -> dict:
    """The structural result for a loaded project (model.py ran it at load)."""
    res = getattr(project, "struct", None)
    if res is None:
        res = {"rows": [], "rules": [], "issues": [], "calcs": {}, "counts": {}, "members": {},
               "edition": tables()["edition"]}
    return res


def report(project) -> dict:
    res = result(project)
    order = {"fail": 0, "engineer": 1, "warn": 2, "pass": 3}
    lines = []
    for r in sorted(res["rows"], key=lambda r: order[r["status"]]):
        lines.append(f"{r['status'].upper():8s} {row_message(r)}")
    for mid, c in res["calcs"].items():
        lines.append(f"CALC     {mid}: {calc_line(c)}")
    errors = [i for i in res["issues"] if i["severity"] == "error"]
    return {"ok": not errors and not res["counts"].get("fail") and not res["counts"].get("engineer"),
            "edition": res["edition"], "counts": res["counts"], "lines": lines, "issues": res["issues"],
            "members": res["members"], "rows": res["rows"], "calcs": res["calcs"], "banner": PRELIM_BANNER}


def row_message(r: dict) -> str:
    tags = f" {' '.join(r['fv'])}" if r["fv"] else ""
    head = f"{r['id']} {r['element']} ({r['citation']})"
    if r["engineer"]:
        return head + (f": rests on unverified inputs{tags}" if r["status"] == "warn" else "")
    drawn = _show(r["drawn"], r["unit"])
    lim = _show(r["limit"], r["unit"], floor=r["op"] == "<=")
    need = {"<=": "at most", ">=": "at least", "==": "exactly"}[r["op"]]
    msg = f"{head}: {drawn}, {need} {lim}"
    if r["status"] == "warn":
        msg += f" - unverified{tags}, {r['would']}"
    trace = (r.get("lookup") or {}).get("trace")
    return msg + (f" [{trace}]" if trace else "")


def _show(x, unit, floor=False):
    if unit == "in":
        return fmt_floor(x) if floor else fmt_floor(x + 1e-9)
    if unit == "ft":
        return fmt_floor(x * 12)
    return f"{x:g} {unit}"


def calc_line(c: dict) -> str:
    if c["status"] in ("input-required", "placeholder"):
        what = c["errors"] + [f"missing {m}" for m in c["missing"]] + (
            [f"PLACEHOLDER {', '.join(c['placeholders'])}"] if c["placeholders"] else [])
        return f"{c['status'].upper()}: " + "; ".join(what)
    r = c["ratios"]
    return (f"{c['status'].upper()} ({PRELIM_LABEL}) bending {r['bending']:.2f}, shear {r['shear']:.2f}, "
            f"live deflection {r['deflection_live']:.2f}, total deflection {r['deflection_total']:.2f}"
            + (f" (unverified: {', '.join(c['unverified'])})" if c["unverified"] else ""))


def criteria_text(project, name: str) -> str | None:
    node = project.data.get("structure", {}).get("criteria", {}).get(name)
    return node.get("text") if isinstance(node, dict) else None


def size_label(project, member_id: str):
    """What a sheet prints for a member's size. A Txt with the check's keys and tags.

    table design, checks pass  -> the size, with the FV tags of any unverified input
    table design, check fails  -> "SEE STRUCTURAL CHECK" (a failing size never prints as designed)
    outside the tables         -> "BY ENGINEER"
    prelim (this kit's calc)   -> "PRELIM — BY ENGINEER"
    engineer, not stamped      -> "BY ENGINEER (PENDING)", an open ENGINEER REQUIRED row in QA
    engineer, stamped          -> the size and the engineer's calc reference
    """
    from .notes import Txt, fv_text
    res = result(project)
    m = next(x for x in project.data["structure"]["members"] if x["id"] == member_id)
    s = res["members"][member_id]
    keys, tags = [], []
    for rid in s["rows"]:
        k = f"structure.checks.{rid}"
        keys.append(k)
        for t in project.values[k].fv_tags:
            if t not in tags:
                tags.append(t)
    size = (m.get("size") or "").upper()
    st = s["status"]
    if st == "engineer-design":
        ref = m["engineer"].get("calc_ref", "ENGINEER'S CALCULATIONS")
        return Txt(f"{size} PER {ref.upper()}")
    if st == "prelim":
        return Txt(PRELIM_LABEL)
    if st == "engineer-pending":
        return Txt("BY ENGINEER (PENDING)", keys=keys, fv=tags)
    if st == "engineer":
        return Txt("BY ENGINEER", keys=keys, fv=tags)
    if st == "fail":
        return Txt("SEE STRUCTURAL CHECK", keys=keys, fv=tags)
    return Txt(size + (f" {fv_text(tags)}" if tags else ""), keys=keys, fv=tags)


_STATUS_WORD = {"pass": "WITHIN TABLE", "fail": "EXCEEDS TABLE", "engineer": "ENGINEER REQUIRED",
                "prelim": PRELIM_LABEL, "engineer-design": "BY ENGINEER", "engineer-pending": "BY ENGINEER (PENDING)",
                "unchecked": "NOT CHECKED"}


def check_rows(project, member_ids=None) -> list[list]:
    """Rows for a framing check table: MARK, MEMBER, SIZE, SPACING, SPAN, TABLE MAX, BASIS, CHECK.

    Every number prints from project.json through the kit: the member values with
    their FV tags, the table limit from the sourced table file, and its citation.
    """
    from .notes import PrintRefused, Txt, fill, fv_text
    res = result(project)
    out = []
    for m in project.data.get("structure", {}).get("members", []):
        mid = m["id"]
        if member_ids is not None and mid not in member_ids:
            continue
        s = res["members"][mid]
        rows = [r for r in res["rows"] if r["member"] == mid]
        main = next((r for r in rows if r["what"] in ("span", "footing_width")), rows[0] if rows else None)

        def val(name):
            node = m.get(name)
            if node is None:
                return ""
            key = node[1:] if isinstance(node, str) else f"structure.members.{mid}.{name}"
            try:
                return fill(project, "{" + key + ":ftin}")
            except PrintRefused:
                raise
            except Exception:
                return ""
        spacing = val("spacing")
        span = val("span") if m["type"] != "footing" else val("width")
        basis = main["citation"].replace("2025 CRC ", "CRC ").upper() if main else (
            "CALC (PRELIM)" if s["status"] == "prelim" else "")
        if main and not main["engineer"] and main["unit"] == "in":
            lim = Txt(("MIN. " if main["op"] == ">=" else "") + fmt_floor(main["limit"]))
        else:
            lim = Txt("—")
        st = s["status"]
        if st == "warn":
            tags = []
            for r in rows:
                for t in r["fv"]:
                    if t not in tags:
                        tags.append(t)
            word = Txt("VERIFY " + fv_text(tags), fv=tags,
                       keys=[f"structure.checks.{r['id']}" for r in rows])
        else:
            word = _STATUS_WORD.get(st, st.upper())
        label = (m.get("label") or m["type"].replace("_", " ")).upper()
        out.append([mid, label, size_label(project, mid), spacing, span, lim, basis, word])
    return out


def framing_check_panel(kit, sheet, cell, title="STRUCTURAL FRAMING CHECK (PRESCRIPTIVE, 2025 CRC)",
                        member_ids=None, notes=True, size=7.0):
    """A panel with the framing check table and the code basis of each line.

    Draw it with the other panels of a structural sheet:
        struct.framing_check_panel(kit, sh, cell=(0, 0, 14, 5))
    """
    pn = sheet.panel(cell, title)
    rows = check_rows(kit.project, member_ids)
    pn.table([("MARK", 0.55), ("MEMBER", 1.6, "wrap"), ("SIZE", 1.35, "wrap"), ("SPACING", 0.75),
              ("SPAN / WIDTH", 1.1, "wrap"), ("TABLE MAX.", 0.95), ("BASIS", 1.45, "wrap"),
              ("CHECK", None, "wrap")], rows, size=size)
    if notes:
        res = result(kit.project)
        lines = []
        for r in res["rows"]:
            if r["engineer"] or r["status"] in ("fail",):
                lines.append(f"{r['id'].replace('STRUCT-', '')}: {r['element'].upper()}")
        for mid, c in res["calcs"].items():
            if c["status"] in ("input-required", "placeholder"):
                lines.append(f"{mid}: PRELIMINARY CALC NOT RUN - INPUT REQUIRED FROM THE DRAFTER OR ENGINEER "
                             f"({'; '.join(c['missing'] + c['errors'] + c['placeholders'])[:160].upper()})")
        lines.append("TABLE MAX. IS THE ALLOWABLE FROM THE CITED 2025 CRC TABLE FOR THE SPECIES, GRADE, SPACING, "
                     "LOADS AND BUILDING WIDTH IN THE PROJECT FILE. VERIFY = A VALUE IT RESTS ON IS NOT YET "
                     "FIELD-VERIFIED.")
        pn.space(4)
        pn.numbered(lines, size=size)
    return pn


def calc_panel(kit, sheet, cell, member_id, size=6.5):
    """A calc sheet panel for one member's preliminary calc. Headed with PRELIM_BANNER."""
    from .notes import Txt, fv_text
    c = result(kit.project)["calcs"][member_id]
    pn = sheet.panel(cell, f"PRELIMINARY CALC — {member_id} {(c.get('label') or '').upper()}")
    pn.para(PRELIM_BANNER, size=size + 0.5, bold=True)
    tags = c["fv"]
    tg = (" " + fv_text(tags)) if tags else ""
    if c["status"] in ("input-required", "placeholder"):
        pn.para("NOT CALCULATED. INPUT REQUIRED:", size=size, bold=True)
        pn.numbered([x.upper() for x in c["errors"] + [f"MISSING {m}" for m in c["missing"]] +
                     [f"PLACEHOLDER {p}" for p in c["placeholders"]]], size=size)
        return pn
    rows = []
    for i in c["inputs"]:
        rows.append([i["name"].upper(), _num(i["v"], i["unit"]), i["status"],
                     Txt(((i["source"] or "") + (f" {i['fv']}" if i["fv"] and i["fv"] not in (i["source"] or "")
                                                 else "")).upper(),
                         fv=[t.strip() for t in (i["fv"] or "").split(",") if t.strip()])])
    pn.table([("INPUT", 1.3, "wrap"), ("VALUE", 1.0), ("STATUS", 0.9), ("SOURCE / CITATION", None, "wrap")],
             rows, size=size)
    s = c["section"]
    lines = [f"SECTION: B = {_num(s['B'], 'in')}, D = {_num(s['d'], 'in')}; A = B X D = {s['A']:.2f} IN2; "
             f"S = B X D2 / 6 = {s['S']:.2f} IN3; I = B X D3 / 12 = {s['I']:.2f} IN4."]
    for r in c["combos"]:
        lines.append(f"{r['name'].upper()} (CD = {r['CD']:g}): M = {r['M'] / 12:,.0f} LB-FT, V = {r['V']:,.0f} LB; "
                     f"FB = M / S = {r['fb']:,.0f} PSI <= F'B = FB X CD X {c['factor_products']['Fb']:.3g} = "
                     f"{r['Fb_adj']:,.0f} PSI ({r['fb_ratio']:.2f}); FV = 1.5 V / A = {r['fv']:,.0f} PSI <= "
                     f"F'V = {r['Fv_adj']:,.0f} PSI ({r['fv_ratio']:.2f}).")
    dr, dl = c["deflection_results"], c["deflection"]
    lines.append(f"DEFLECTION (E' = {c['E_adj']:,.0f} PSI): LIVE {fmt_ceil(dr['live'])} <= L/{dl['live_ratio']} = "
                 f"{fmt_floor(dr['limit_live'], 32)} ({dl['live_citation'].upper()}, {dl['live_row'].upper()}); "
                 f"{dl['creep']:g} X DEAD + LIVE {fmt_ceil(dr['total'])} <= L/{dl['total_ratio']} = "
                 f"{fmt_floor(dr['limit_total'], 32)} ({dl['total_citation'].upper()}, NOTE D).")
    r = c["ratios"]
    lines.append(f"RATIOS (TRIAL SIZE {(c.get('size') or '').upper()}): BENDING {r['bending']:.2f}, SHEAR "
                 f"{r['shear']:.2f}, LIVE DEFLECTION {r['deflection_live']:.2f}, TOTAL DEFLECTION "
                 f"{r['deflection_total']:.2f}." + (f" UNVERIFIED INPUTS{tg}: RESULT IS NOT RELIABLE UNTIL "
                                                     "VERIFIED." if c["unverified"] else ""))
    if c["factor_checklist"]:
        lines.append("FACTORS NOT LISTED (CONFIRM THEY DO NOT APPLY): " + "; ".join(c["factor_checklist"]).upper())
    lines.append(f"ON THE DRAWINGS THIS MEMBER PRINTS AS '{PRELIM_LABEL}'.")
    pn.numbered([Txt(x, fv=tags) if tags and x.endswith("VERIFIED.") else x for x in lines], size=size)
    return pn


def _num(x, unit):
    if unit == "in":
        return _fmt(x)
    if unit == "factor":
        return f"{x:g}"
    return f"{x:,.0f} {unit.upper()}" if abs(x) >= 100 else f"{x:g} {unit.upper()}"


def calc_markdown(project) -> str:
    """The preliminary calc package as markdown: every input, formula and result."""
    res = result(project)
    meta = project.meta
    out = [f"# {PRELIM_BANNER}", "",
           f"Project: {meta.get('title', '')}, {meta.get('address', '')}  ",
           f"Prepared with permitkit (struct.py) from `project.json` (sha256 {getattr(project, 'sha256', '')[:12]}).  ",
           f"Code basis: {res['edition']}.", "",
           "This package is a preliminary check for an engineer to review. It is not a structural design. "
           "Reference design values and adjustment factors are the inputs listed with their citations; the kit "
           "supplies none. Members sized only by this package print on the drawings as "
           f"\"{PRELIM_LABEL}\".", ""]
    crit = project.data.get("structure", {}).get("criteria", {})
    if crit:
        out += ["## Design criteria", "", "| Item | Value | Status | Source |", "|---|---|---|---|"]
        for k in sorted(crit):
            node = crit[k]
            if isinstance(node, dict) and "text" in node:
                out.append(f"| {k} | {node['text']} | {node['status']} {node.get('fv', '')} | {node.get('source', '')} {node.get('note', '')} |")
            else:
                v = project.values.get(f"structure.criteria.{k}") if isinstance(node, dict) else (
                    project.values.get(node[1:]) if isinstance(node, str) else None)
                if v is not None:
                    st = v.status + ("".join(f" {t}" for t in v.fv_tags) if v.unverified else "")
                    out.append(f"| {k} | {v.v:g} {v.unit} | {st} | {_value_source(v, 'structure.criteria.')} |")
        out.append("")
    if res["rows"]:
        out += ["## Prescriptive checks (2025 CRC tables)", "",
                "| Check | Status | Result | Table row or provision (verbatim) |", "|---|---|---|---|"]
        for r in res["rows"]:
            lk = r.get("lookup") or {}
            src = lk.get("source_line", "").replace("|", "\\|")
            cell = f"`{src}`" if src else (f"\"{lk['quote']}\"" if lk.get("quote") else "(question answered in the "
                                                                                      "project file)")
            out.append(f"| {r['id']} | {r['status'].upper()} | {row_message(r).replace('|', '/')} | {cell} |")
        out.append("")
    for mid, c in res["calcs"].items():
        out += [f"## {mid} — {c.get('label') or ''} (trial size {c.get('size') or 'not given'})", "",
                f"**{PRELIM_BANNER}**", "", f"Material: {c.get('material')}. Status: {c['status']}.", ""]
        out += ["### Inputs", "", "| Input | Value | Unit | Status | Source / citation |", "|---|---|---|---|---|"]
        for i in c["inputs"]:
            note = i.get("note") if i.get("note") and str(i["note"])[:90] not in (i["source"] or "") else None
            num = f"{i['v']:,.0f}" if abs(i["v"]) >= 1e5 else f"{i['v']:.6g}"
            out.append(f"| {i['name']} | {num} | {i['unit']} | {i['status']}{' ' + i['fv'] if i['fv'] else ''} "
                       f"| {i['source']}{' — ' + note if note else ''} |")
        out.append("")
        if c["status"] in ("input-required", "placeholder"):
            out += ["### Not calculated", ""] + [f"- {x}" for x in c["errors"]] + \
                   [f"- missing: {x}" for x in c["missing"]] + [f"- PLACEHOLDER: {x}" for x in c["placeholders"]] + [""]
            continue
        s = c["section"]
        out += ["### Section", "",
                f"- B = {s['B']:.4g} in. (all plies), d = {s['d']:.4g} in.",
                f"- A = B x d = {s['A']:.4g} in²", f"- S = B d² / 6 = {s['S']:.4g} in³",
                f"- I = B d³ / 12 = {s['I']:.4g} in⁴", "",
                "### Bending and shear (simply supported; M and the deflection evaluated at 401 points and at "
                "each point load; V = the larger reaction)", ""]
        fp = c["factor_products"]
        for r in c["combos"]:
            fs = ", ".join(f"{k} x {v:g}" for k, v in sorted(r["factors"].items()))
            out += [f"**{r['name']}** ({fs}; {r['citation']}; CD = {r['CD']:g})", "",
                    f"- M = {r['M']:,.1f} lb-in = {r['M'] / 12:,.1f} lb-ft; V = {r['V']:,.1f} lb",
                    f"- fb = M / S = {r['fb']:,.1f} psi; F'b = Fb x CD x {fp['Fb']:.4g} = {r['Fb_adj']:,.1f} psi; "
                    f"fb / F'b = {r['fb_ratio']:.3f}",
                    f"- fv = 1.5 V / A = {r['fv']:,.1f} psi; F'v = Fv x CD x {fp['Fv']:.4g} = {r['Fv_adj']:,.1f} psi; "
                    f"fv / F'v = {r['fv_ratio']:.3f}", ""]
        dr, dl = c["deflection_results"], c["deflection"]
        out += ["### Deflection (service loads)", "",
                f"- E' = E x {fp['E']:.4g} = {c['E_adj']:,.0f} psi",
                f"- Live (L, Lr, S): {dr['live']:.4f} in.; limit L/{dl['live_ratio']} = {dr['limit_live']:.4f} in. "
                f"({dl['live_citation']}, row \"{dl['live_row']}\": `{dl['live_source']}`)",
                f"- Total: {dl['creep']:g} x dead ({dr['dead']:.4f} in.) + live = {dr['total']:.4f} in.; limit "
                f"L/{dl['total_ratio']} = {dr['limit_total']:.4f} in. ({dl['total_citation']}, row "
                f"\"{dl['total_row']}\": `{dl['total_source']}`; note d: \"{dl['creep_quote']}\")", "",
                "### Result", "",
                f"| Check | Ratio |", "|---|---|"] + [f"| {k} | {v:.3f} |" for k, v in c["ratios"].items()] + [""]
        if c["unverified"]:
            out += [f"Unverified inputs: {', '.join(c['unverified'])} ({', '.join(c['fv'])}). The ratios are not "
                    "reliable until these are verified.", ""]
        if c["factor_checklist"]:
            out += ["Factors not listed (the engineer confirms each does not apply): "
                    + "; ".join(c["factor_checklist"]), ""]
        out += [f"Within the trial size by this preliminary check: {'yes' if c['within'] else 'NO'}. "
                "This is not a design; the engineer of record decides.", ""]
    return "\n".join(out).rstrip() + "\n"
