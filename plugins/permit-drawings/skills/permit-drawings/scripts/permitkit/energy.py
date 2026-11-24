"""Title 24 Part 6 energy help for single-family additions and alterations.

What it does, all from project.json `energy` (references/energy-and-green.md):

- climate zone from a ZIP code, from the Energy Commission's ZIP list shipped in
  data/cec-building-climate-zones-by-zip.csv;
- prescriptive checks in the same shape as project.json `rules`: fenestration
  U-factor and SHGC, fenestration area, door U-factor, insulation R-values,
  duct insulation. Every limit comes from data/t24-2025-sfr.json, which holds
  the quoted code line, the citation and the corpus file it was cut from. A
  limit the data file does not hold (a table cell that could not be read, a
  package the kit does not model) becomes an `ask` row, never a guess;
- the requirements the scope triggers (water heating, HVAC, lighting, QII,
  ventilation), and which of them need ECC-Rater field verification, which
  means the Certificate of Compliance must be registered;
- two sheet panels: a Title 24 summary and a CF1R worksheet. The worksheet only
  pre-fills what a drafter types into the state form or CBECC-Res. It is not
  the certificate.

Which `change` and `assembly` each item has is the drafter's reading of the
scope, recorded in project.json. The kit maps those recorded facts to the code
sections that name them. It never reads free text to decide.
"""
from __future__ import annotations

import csv
import functools
import json
import math
import os
import re

from .model import PrintRefused, fv_sorted

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
ZIP_FILE = os.path.join(DATA, "cec-building-climate-zones-by-zip.csv")
T24_FILE = os.path.join(DATA, "t24-2025-sfr.json")
ZIP_SOURCE = "California Energy Commission, Building Climate Zones by ZIP Code"
RULE_PREFIX = "T24-"
KIT_KEY_PREFIX = "t24:"



# Code section ids keep their case in capitals: "150.2(b)1A", "10-103(a)1", "150.0(k)".
_SECTION_ID = re.compile(r"\bCEnC\b|\b\d+(?:[.-]\d+)*(?:\([a-z]\)[0-9A-Za-z]*)+")


def caps(text: str) -> str:
    """Upper-case sheet text while keeping code section ids as written. Mechanical formatting."""
    out, last = [], 0
    for m in _SECTION_ID.finditer(text):
        out.append(text[last:m.start()].upper())
        out.append(m.group(0))
        last = m.end()
    out.append(text[last:].upper())
    return "".join(out)

class EnergyError(ValueError):
    pass


# ---------------------------------------------------------------- data

@functools.lru_cache(maxsize=1)
def data() -> dict:
    with open(T24_FILE, encoding="utf-8") as fh:
        return json.load(fh)


@functools.lru_cache(maxsize=1)
def zip_table() -> dict:
    """ZIP code -> climate zone (int), read with the csv module."""
    out = {}
    with open(ZIP_FILE, newline="", encoding="utf-8") as fh:
        rows = csv.reader(fh)
        next(rows)                          # header: Zip Code, Building CZ
        for r in rows:
            if len(r) >= 2 and r[0].strip().isdigit() and r[1].strip().isdigit():
                out[r[0].strip().zfill(5)] = int(r[1])
    return out


def climate_zone_for_zip(zipcode: str) -> int:
    """The building climate zone the Energy Commission's list gives a ZIP code."""
    z = str(zipcode).strip()
    if not (len(z) == 5 and z.isdigit()):
        raise EnergyError(f"{zipcode!r} is not a five-digit ZIP code")
    if z not in zip_table():
        raise EnergyError(f"ZIP {z} is not in the Energy Commission's ZIP list; ask the city "
                          "for the building climate zone (Reference Joint Appendix JA2)")
    return zip_table()[z]


def zone_entry(zipcode: str) -> dict:
    """A ready Value and source entry for project.json, for `permitkit energy --zip`."""
    cz = climate_zone_for_zip(zipcode)
    return {
        "zip": zipcode, "climate_zone": cz,
        "value": {"climate_zone": {
            "v": cz, "unit": "count", "status": "DERIVED", "source": "CEC-CZ",
            "note": f"Building climate zone for ZIP {zipcode} from the Energy Commission's ZIP list. "
                    "A ZIP code can cross a zone line; confirm with the city when the site is near one."}},
        "source": {"id": "CEC-CZ", "kind": "document", "path": "(permitkit) data/cec-building-climate-zones-by-zip.csv",
                   "note": ZIP_SOURCE},
        "energy": {"zip": zipcode, "climate_zone": "$climate_zone"},
    }


def limit(lid: str, cz: int):
    """(kind, number or reason, entry) for limit `lid` in climate zone `cz`.

    kind is "limit" (a number from the quoted line), "nr" (the code sets no
    requirement in this zone), "unread" (the corpus line could not be read for
    this zone: ask) or "absent" (the entry names no value for this zone).
    """
    entry = data()["limits"][lid]
    if str(cz) in entry.get("unread_cz", {}):
        return "unread", entry["unread_cz"][str(cz)], entry
    if cz in entry.get("no_requirement_cz", []):
        return "nr", None, entry
    for v in entry["values"]:
        if cz in v["cz"]:
            return "limit", v["limit"], entry
    return "absent", None, entry


def threshold(tid: str) -> float:
    return float(data()["thresholds"][tid]["value"])


def _th(tid: str) -> str:
    """A sourced threshold as printed: 700, 1,000."""
    return f"{threshold(tid):,g}"


def requirement(rid: str) -> dict:
    return data()["requirements"][rid]


# ---------------------------------------------------------------- validation (model.py calls this)

_REF_FIELDS = {
    "addition": ("cfa", "existing_cfa", "fenestration_area", "west_fenestration_area"),
    "house": ("cfa", "fenestration_area", "west_fenestration_area"),
}
_ITEM_REFS = {
    "fenestration": {"area": "sf", "replaces_area": "sf", "u_factor": "u-factor", "shgc": "ratio"},
    "doors": {"area": "sf", "u_factor": "u-factor"},
    "insulation": {"r_value": "R-value", "u_factor": "u-factor"},
    "ducts": {"length": "in", "r_value": "R-value"},
}
_UNIT_OF = {"cfa": "sf", "existing_cfa": "sf", "fenestration_area": "sf", "west_fenestration_area": "sf"}


def validate(project) -> None:
    """Add issues for an energy block that cannot be checked: a reference to a
    value that does not exist, a value in the wrong unit, a climate zone that
    differs from the ZIP list without a source of its own, duplicate ids."""
    e = project.data.get("energy")
    if not e:
        return

    def ref(where, r, unit):
        try:
            val = project.lookup(r)
        except KeyError:
            project.issue("warning", "energy-value-unknown", where,
                          f"{r} is not a value yet; the energy check asks for it")
            return None
        if unit and val.unit != unit:
            project.issue("error", "energy-unit", where,
                          f"{r} has unit {val.unit!r}; this field needs a value in {unit!r}")
        return val

    cz = ref("energy.climate_zone", e["climate_zone"], "count")
    if cz is not None and not isinstance(cz.v, (list, tuple)):
        n = float(cz)
        if n != int(n) or not 1 <= n <= 16:
            project.issue("error", "energy-climate-zone", "energy.climate_zone",
                          f"climate zone {n:g} is not one of the 16 California building climate zones")
        elif e.get("zip"):
            try:
                listed = climate_zone_for_zip(e["zip"])
            except EnergyError as exc:
                project.issue("warning", "energy-zip", "energy.zip", str(exc))
            else:
                if listed != int(n):
                    src = (cz.source or "")
                    sev = "error" if src in ("", "CEC-CZ") else "warning"
                    project.issue(sev, "energy-zip-mismatch", "energy.climate_zone",
                                  f"climate zone {int(n)} differs from CZ {listed} that the Energy "
                                  f"Commission's ZIP list gives ZIP {e['zip']}. Keep a different zone "
                                  "only with its own source (the city's answer), never the ZIP list")
    for block, fields in _REF_FIELDS.items():
        for f in fields:
            if f in e.get(block, {}):
                ref(f"energy.{block}.{f}", e[block][f], _UNIT_OF[f])
    for kind, fields in _ITEM_REFS.items():
        seen = set()
        for it in e.get(kind, []):
            where = f"energy.{kind}.{it['id']}"
            if it["id"] in seen:
                project.issue("error", "energy-duplicate", where, "id appears twice")
            seen.add(it["id"])
            for f, unit in fields.items():
                if f in it:
                    ref(f"{where}.{f}", it[f], unit)
    if "addition" in e["work"] and not e.get("addition", {}).get("cfa"):
        project.issue("warning", "energy-addition-cfa", "energy.addition.cfa",
                      "an addition needs its conditioned floor area (addition.cfa) for the 150.2(a) checks")


# ---------------------------------------------------------------- the plan

def _val(project, r):
    if not r:
        return None
    try:
        return project.lookup(r)
    except KeyError:
        return None


def _fmt_num(x: float, unit: str) -> str:
    if unit in ("u-factor", "ratio"):
        s = f"{x:.3f}".rstrip("0")
        return s + "0" * max(0, 2 - len(s.split(".")[1])) if "." in s else f"{x:.2f}"
    if unit == "R-value":
        return f"R-{x:g}"
    if unit in ("sf",):
        cut = math.floor(x * 100 + 1e-6) / 100
        return (f"{cut:.2f}".rstrip("0").rstrip(".")) + " SQ FT"
    if unit == "pct":
        return f"{x:g}%"
    return f"{x:g}"


class Plan:
    """The energy reading of one project: checks, requirements, asks, ECC list."""

    def __init__(self, project):
        self.p = project
        self.e = project.data["energy"]
        self.work = list(self.e["work"])
        self.path = self.e["path"]
        self.prescriptive = self.path == "prescriptive"
        self.cz_val = _val(project, self.e["climate_zone"])
        self.cz = int(round(float(self.cz_val))) if self.cz_val is not None else None
        self.checks: list[dict] = []        # rule-shaped rows with a sourced limit
        self.asks: list[dict] = []          # items the kit cannot settle from its data
        self.reqs: list[dict] = []          # requirements the scope triggers
        self.info: list[dict] = []          # exceptions taken, no-requirement rows
        add = self.e.get("addition", {})
        self.cfa_val = _val(project, add.get("cfa"))
        self.cfa = float(self.cfa_val) if self.cfa_val is not None else None
        if self.cz is None:
            self.ask("climate zone", "The climate-zone value is missing. Record the CEC climate zone of the site ZIP code "
                                     "with its source.", "energy.climate_zone")
            return
        if "addition" in self.work:
            self._addition()
        if "alteration" in self.work:
            self._alteration()
        self._fenestration()
        self._doors()
        self._insulation()
        self._ducts()
        self._hvac()
        self._water()
        self._lighting()
        if not self.prescriptive:
            rid = "150.2(a)2:performance" if "addition" in self.work else "150.2(b)2:performance"
            self.req(rid, "The drafter chose the performance path (energy.path). A CBECC-Res run by the "
                          "documentation author decides compliance; this sheet checks mandatory measures only.")
            self.req("150.1(b):software", "Performance path.")

    # -- row makers
    def ask(self, item, message, where, cite=None):
        self.asks.append({"item": item, "message": message, "where": where, "citation": cite})

    def req(self, rid, why, status="applies", item=None):
        r = requirement(rid)
        self.reqs.append({"id": rid, "item": item, "title": r["title"], "citation": r["citation"],
                          "plain": r["plain"], "quote": r["quote"], "ecc": bool(r["ecc"]) and status == "applies",
                          "why": why, "status": status})

    def note(self, item, message, cite):
        self.info.append({"item": item, "message": message, "citation": cite})

    def check(self, item_id, item, tag, lid, ref, unit, note="", fixed=None, limit_text=None, deps=()):
        """One rule-shaped check of value `ref` against limit `lid` in this zone."""
        if fixed is None:
            kind, num, entry = limit(lid, self.cz)
        else:
            kind, num, entry = "limit", fixed, data()["limits"][lid]
        if kind == "nr":
            self.note(item, f"{entry['element']}: no requirement in Climate Zone {self.cz} "
                            f"({entry['citation']}).", entry["citation"])
            return
        if kind in ("unread", "absent"):
            reason = num if kind == "unread" else "the data file holds no value for this zone"
            self.ask(item, f"{entry['element']}: no sourced limit is recorded for Climate Zone {self.cz} "
                           f"({reason}). Read {entry['citation']} and record the limit with its citation.",
                     ref or item_id, entry["citation"])
            return
        if not ref:
            what = {"u-factor": "U-factor (NFRC label or data sheet)", "ratio": "SHGC (NFRC label)",
                    "R-value": "installed R-value", "sf": "area"}.get(unit, "value")
            self.ask(item, f"{entry['element']}: enter the {what} as a Value (MANUFACTURER with its data "
                           f"sheet, or PLACEHOLDER until chosen). Limit: {_fmt_num(num, unit)} "
                           f"{'max.' if entry['op'] == '<=' else 'min.'} ({entry['citation']}).",
                     item_id, entry["citation"])
            return
        self.checks.append({
            "id": f"{RULE_PREFIX}{item_id}-{tag}", "item": item, "element": entry["element"],
            "citation": entry["citation"], "quote": entry["quote"], "limit_id": lid,
            # a computed limit (fixed) is in the caller's unit; a table limit is in the data file's
            "op": entry["op"], "limit": float(num),
            "unit": unit if fixed is not None else entry["unit"], "value": ref, "note": note,
            "limit_text": limit_text,
            # every limit was chosen by the climate zone, so a check rests on it too
            "deps": tuple(deps) + ((self.cz_val.key,) if self.cz_val is not None else ())})

    # -- addition-wide
    def _addition(self):
        add = self.e.get("addition", {})
        if self.cfa is None:
            self.ask("addition", "Enter the addition's conditioned floor area (energy.addition.cfa).",
                     "energy.addition.cfa", "2025 CEnC 150.2(a)")
            return
        self.req("150.2(a):scope", "The work is an addition.")
        small = self.cfa <= threshold("addition-small")
        self.req("150.2(a)-x6:pv", "Addition.")
        if small:
            self.req("150.2(a)1Bv:no-qii", f"Addition of {_fmt_num(self.cfa, 'sf')}, not over {_th('addition-small')} sq ft.")
            if self.prescriptive and self.cz in requirement("150.2(a)1Bii:radiant-barrier")["zones"]:
                self.req("150.2(a)1Bii:radiant-barrier", f"Addition not over {_th('addition-small')} sq ft in Climate Zone {self.cz}.")
        elif self.prescriptive:
            self.req("150.2(a)1A:qii", f"Addition of {_fmt_num(self.cfa, 'sf')}, over {_th('addition-small')} sq ft.")
            self.ask(f"addition over {_th('addition-small')} sq ft",
                     f"An addition over {_th('addition-small')} sq ft meets the full Section 150.1(c) package (Table 150.1-A, "
                     "roof Option B or C, radiant barrier, whole-house fan, ducts) with the 150.2(a)1A "
                     "modifications. This sheet checks only the fenestration, doors and insulation it lists. "
                     "Use CBECC-Res or the state CF1R form for the whole package.",
                     "energy.addition", "2025 CEnC 150.2(a)1A")
        if self.cfa <= threshold("addition-ventilation"):
            self.req("150.2(a)1Ci:ventilation", f"The addition adds {_th('addition-ventilation')} sq ft or less of conditioned floor area.")
        self.req("150.2(a)1Cii:local-exhaust", "Addition: applies to any bathroom or kitchen it adds.")
        if add.get("new_dwelling_unit"):
            self.ask("new dwelling unit", "The addition is a new dwelling unit: its whole-dwelling ventilation "
                     "airflow follows 150.0(o) for the new unit (150.2(a)1Ci(c)), and the CZ 5 small-unit "
                     "U-factor exception may apply. This sheet does not check these.", "energy.addition",
                     "2025 CEnC 150.2(a)1Ci")
        if not self.prescriptive:
            return
        # fenestration area of the addition
        if small:
            lid = ("150.2(a)1Biv-b:total-400" if self.cfa <= threshold("addition-tiny")
                   else "150.2(a)1Biv-a:total-400-700")
            self._greater_of("addition", "addition fenestration", "AREA", lid, add.get("fenestration_area"))
            kind, num, entry = limit("150.2(a)1Biv:west-60", self.cz)
            if kind == "limit":
                self.check("addition", "addition fenestration", "WEST", "150.2(a)1Biv:west-60",
                           add.get("west_fenestration_area"), "sf",
                           note="west-facing fenestration of the addition")
            else:
                self.note("addition fenestration", f"No west-facing or total-area limit for an addition of "
                          f"{_th('addition-small')} sq ft or less in Climate Zone {self.cz} (150.2(a)1Biv names CZ 2, 4 and 6-15).",
                          "2025 CEnC 150.2(a)1Biv")
        else:
            self._greater_of("addition", "addition fenestration", "AREA", "150.2(a)1Aii:total-700",
                             add.get("fenestration_area"))
            self._greater_of("addition", "addition fenestration", "WEST", "150.2(a)1Aii:west-700",
                             add.get("west_fenestration_area"))

    def _greater_of(self, item_id, item, tag, lid, ref):
        entry = data()["limits"][lid]
        if not any(self.cz in v["cz"] for v in entry["values"]):
            self.note(item, f"{entry['element']}: no limit in Climate Zone {self.cz} ({entry['citation']}). "
                            + entry.get("nr_note", ""), entry["citation"])
            return
        if "pct_from" in entry:
            k, pct, _ = limit(entry["pct_from"], self.cz)
            if k != "limit":
                self.note(item, f"{entry['element']}: Table 150.1-A sets no percentage in Climate Zone "
                                f"{self.cz}.", entry["citation"])
                return
        else:
            pct = entry["pct_of_cfa"]
        lim = max(float(entry["floor_sf"]), pct / 100.0 * self.cfa)
        lim = math.floor(lim * 100 + 1e-6) / 100
        text = (f"{_fmt_num(lim, 'sf')} MAX. (GREATER OF {entry['floor_sf']} SQ FT OR {pct:g}% OF "
                f"{{{self.cfa_val.key}:sf}} CFA)")
        self.check(item_id, item, tag, lid, ref, "sf", fixed=lim, limit_text=text,
                   note=f"limit = greater of {entry['floor_sf']} sq ft or {pct:g}% of the addition CFA "
                        f"({self.cfa_val.key})", deps=(self.cfa_val.key,))

    def _alteration(self):
        self.req("150.2(b)1:scope", "The work alters an existing dwelling.")

    # -- fenestration
    def _fenestration(self):
        items = self.e.get("fenestration", [])
        repl_vertical = [it for it in items if it["change"] == "replacement" and it["kind"] != "skylight"]
        repl_area, repl_unverified = 0.0, False
        for it in repl_vertical:
            v = _val(self.p, it["area"])
            if v is not None:
                repl_area += float(v)
                repl_unverified |= v.unverified
        small_repl = repl_area <= threshold("alteration-replaced-fen")
        added_total, added_unverified, added_known = 0.0, False, True
        for it in items:
            label = f"{it['id']} ({it['kind'].replace('_', ' ')}, {it['change']})"
            u, s = it.get("u_factor"), it.get("shgc")
            # mandatory 150.0(q), both paths
            self.check(it["id"], label, "U-MAND", "150.0(q):u-040", u, "u-factor",
                       note="mandatory maximum U-factor; see 150.0(q) for its small-area exceptions")
            if it["change"] == "added":
                a, r = _val(self.p, it["area"]), _val(self.p, it.get("replaces_area"))
                if a is None:
                    added_known = False
                else:
                    added_total += float(a) - (float(r) if r is not None else 0.0)
                    added_unverified |= a.unverified or (r is not None and r.unverified)
            if not self.prescriptive:
                continue
            if it["change"] == "replacement":
                if it["kind"] == "skylight":
                    self.check(it["id"], label, "U", "150.2(b)1B-x2:skylight-u", u, "u-factor")
                    self.check(it["id"], label, "SHGC", "150.2(b)1B-x2:skylight-shgc", s, "ratio")
                    continue
                if small_repl:
                    why = (f"replacement vertical fenestration totals {_fmt_num(repl_area, 'sf')}, not over {_th('alteration-replaced-fen')} sq ft"
                           + (" (rests on unverified areas)" if repl_unverified else ""))
                    self.check(it["id"], label, "U", "150.2(b)1B-x1:u", u, "u-factor", note=why)
                    if self.cz == 15:
                        self.check(it["id"], label, "SHGC", "150.2(b)1B-x3:cz15-shgc", s, "ratio")
                    else:
                        self.check(it["id"], label, "SHGC", "150.2(b)1B-x1:shgc", s, "ratio", note=why)
                    continue
                self.check(it["id"], label, "U", "T150.1-A:fen-u", u, "u-factor",
                           note=f"150.2(b)1B: replacement over {_th('alteration-replaced-fen')} sq ft meets 150.1(c)3A")
                self.check(it["id"], label, "SHGC",
                           "150.2(b)1B-x3:cz15-shgc" if self.cz == 15 else "T150.1-A:fen-shgc", s, "ratio",
                           note="150.2(b)1B")
            else:   # addition or added
                self.check(it["id"], label, "U", "T150.1-A:fen-u", u, "u-factor",
                           note="150.2(a)1 / 150.2(b)1A: Table 150.1-A")
                if self.cz == 15:
                    lid = ("150.2(b)1A-x1:cz15-shgc" if it["change"] == "added" else
                           "150.2(a)1Aiii:cz15-shgc" if self.cfa is not None and self.cfa > threshold("addition-small")
                           else "T150.1-A:fen-shgc")
                else:
                    lid = "T150.1-A:fen-shgc"
                self.check(it["id"], label, "SHGC", lid, s, "ratio", note="Table 150.1-A")
        if self.prescriptive and any(it["change"] == "added" for it in items):
            limit16 = threshold("alteration-added-fen")
            tag = " (rests on unverified areas)" if added_unverified else ""
            if added_known and added_total <= limit16:
                self.note("added fenestration",
                          f"The alteration adds {_fmt_num(max(added_total, 0), 'sf')} of fenestration, not over "
                          f"{_th('alteration-added-fen')} sq ft{tag}: the total and west-facing area limits do not apply (150.2(b)1A "
                          "Exception 2).", "2025 CEnC 150.2(b)1A Exception 2")
            else:
                house = self.e.get("house", {})
                for tag2, lid, f in (("AREA", "T150.1-A:fen-total-pct", "fenestration_area"),
                                     ("WEST", "T150.1-A:fen-west-pct", "west_fenestration_area")):
                    self._house_pct("house", "whole-house fenestration", tag2, lid, house.get(f), house.get("cfa"))

    def _house_pct(self, item_id, item, tag, lid, ref, cfa_ref):
        kind, pct, entry = limit(lid, self.cz)
        if kind == "nr":
            self.note(item, f"{entry['element']}: no requirement in Climate Zone {self.cz}.", entry["citation"])
            return
        cfa = _val(self.p, cfa_ref)
        if kind != "limit" or cfa is None or not ref:
            self.ask(item, f"The alteration adds more than {_th('alteration-added-fen')} sq ft of fenestration, so the house meets "
                           f"{entry['element']} ({entry['citation']}). Enter energy.house.cfa and the "
                           "house's total and west-facing fenestration area after the work.",
                     "energy.house", entry["citation"])
            return
        lim = math.floor(pct / 100.0 * float(cfa) * 100 + 1e-6) / 100
        self.check(item_id, item, tag, lid, ref, "sf", fixed=lim, deps=(cfa.key,),
                   limit_text=f"{_fmt_num(lim, 'sf')} MAX. ({pct:g}% OF {{{cfa.key}:sf}} CFA)",
                   note=f"limit = {pct:g}% of the house CFA ({cfa.key})")

    def _doors(self):
        if not self.prescriptive:
            return
        for d in self.e.get("doors", []):
            lid = "150.2(b)1N:door-u" if d["change"] == "added" else "T150.1-A:door-u"
            self.check(d["id"], f"{d['id']} (opaque door, {d['change']})", "U", lid, d.get("u_factor"), "u-factor")

    # -- insulation
    def _insulation(self):
        small = self.cfa is not None and self.cfa <= threshold("addition-small")
        for it in self.e.get("insulation", []):
            a, ch, r = it["assembly"], it["change"], it.get("r_value")
            label = f"{it['id']} ({a.replace('_', ' ')}, {ch})"
            if a in ("vented_attic_ceiling", "rafter_roof"):
                mand = "150.0(a)2-x:ceiling-alt-r19" if ch == "altered" else "150.0(a)2:ceiling-r22"
                self.check(it["id"], label, "R-MAND", mand, r, "R-value", note="mandatory")
                if not self.prescriptive or a == "rafter_roof":
                    continue
                if ch == "addition":
                    if small:
                        self.check(it["id"], label, "R", "150.2(a)1Bi:ceiling-r", r, "R-value")
                    else:
                        self.ask(label, f"Ceiling insulation for an addition over {_th('addition-small')} sq ft follows Table "
                                 "150.1-A Option B or C; record the option and its limit.", it["id"],
                                 "2025 CEnC Table 150.1-A")
                else:
                    kind, _, _ = limit("150.2(b)1Ji:ceiling-r49", self.cz)
                    if kind == "limit":
                        self.check(it["id"], label, "R", "150.2(b)1Ji:ceiling-r49", r, "R-value",
                                   note="150.2(b)1J has exceptions (existing R-38, asbestos, knob and tube)")
            elif a in ("wall_extension_2x4", "wall_extension_2x6"):
                lid = "150.2(a)1:wall-ext-2x4" if a.endswith("2x4") else "150.2(a)1:wall-ext-2x6"
                self.check(it["id"], label, "R", lid, r, "R-value")
            elif a in ("wall_2x4", "wall_2x6"):
                lid = "150.0(c)6:wall-2x4" if a.endswith("2x4") else "150.0(c)6:wall-2x6"
                self.check(it["id"], label, "R-MAND", lid, r, "R-value",
                           note="mandatory, R-value route of 150.0(c)6")
                if self.prescriptive and ch == "addition":
                    self.check(it["id"], label, "U", "T150.1-A:wall-u", it.get("u_factor"), "u-factor",
                               note="assembly U-factor of a new framed wall (Reference Joint Appendix JA4)")
            elif a == "raised_floor":
                self.check(it["id"], label, "R-MAND", "150.0(d):floor-r19", r, "R-value", note="mandatory")

    def _ducts(self):
        for d in self.e.get("ducts", []):
            label = f"{d['id']} (ducts, {d['change']}, {d['location']} space)"
            if d["location"] == "unconditioned" and self.prescriptive:
                self.check(d["id"], label, "R", "T150.2-D:duct-r", d.get("r_value"), "R-value")
            exc = d.get("ecc_exception")
            if d["change"] == "extension":
                self.req("150.2(a)-x4:ducts-extended" if "addition" in self.work else "150.2(b)1D:duct-sealing",
                         "Ducts extended from the existing system.", item=d["id"],
                         status="exception claimed" if exc else "applies")
                continue
            length = _val(self.p, d.get("length"))
            if length is None:
                self.ask(label, "Enter the length of new or replacement duct (energy.ducts.length): over "
                                "25 ft triggers 150.2(b)1D duct sealing with field verification.", d["id"],
                         "2025 CEnC 150.2(b)1D")
                continue
            feet = float(length) / 12.0
            if feet > threshold("alteration-new-duct-ft"):
                self.req("150.2(b)1D:duct-sealing", f"{feet:g} ft of new or replacement duct"
                         + (" (unverified length)" if length.unverified else "") + ".", item=d["id"],
                         status="exception claimed" if exc else "applies")
            else:
                self.note(label, "25 ft or less of new or replacement duct: 150.2(b)1D is not triggered "
                                 "by length.", "2025 CEnC 150.2(b)1D")

    def _hvac(self):
        tr = data()["table_requirements"]
        for h in self.e.get("hvac", []):
            sysname, ch = h["system"], h["change"]
            item = f"{h['id']} ({sysname.replace('_', ' ')}, {ch.replace('_', ' ')})"
            exc = h.get("ecc_exception")
            refrig_cz = (tr["T150.1-A:refrig-hp"]["req_cz"] if sysname == "heat_pump"
                         else tr["T150.1-A:refrig-ac"]["req_cz"] if sysname == "air_conditioner" else [])
            if ch == "extended":
                self.req("150.2(a)-x3:hvac-extended", "Heating or cooling extended from the existing system.", item=item)
                continue
            if ch == "new":
                if "addition" in self.work:
                    self.req("150.2(a)1E:loads", "New space-conditioning equipment for the addition.", item=item)
                if self.cz in refrig_cz:
                    self.req("150.1(c)7A:refrigerant", f"New {sysname.replace('_', ' ')}; Table 150.1-A "
                             f"requires refrigerant charge verification in Climate Zone {self.cz}.", item=item,
                             status="exception claimed" if exc else "applies")
                if sysname == "electric_resistance" and self.prescriptive:
                    self.ask(item, "Table 150.1-A: electric resistance space heating is not allowed in the "
                             "prescriptive package (\"Space Heating - Electric Resistance Allowed: No\"). "
                             "Change the system or use the performance path.", h["id"], "2025 CEnC Table 150.1-A")
                continue
            # alterations
            if ch == "complete_replacement":
                self.req("150.2(b)1C:complete-replacement", "Entirely new or complete replacement system.", item=item)
            if ch in ("complete_replacement", "equipment_replaced"):
                self.req("150.2(b)1E:duct-sealing", "Space-conditioning equipment installed or replaced.",
                         item=item, status="exception claimed" if exc else "applies")
            if ch in ("complete_replacement", "refrigerant_altered") and sysname in ("heat_pump", "air_conditioner"):
                verify = self.cz in refrig_cz      # zones from the sourced Table 150.1-A rows
                self.req("150.2(b)1F:refrigerant", "Refrigerant-containing components installed or replaced.",
                         item=item)
                if verify:
                    self.req("150.2(b)1Fii:verify", f"{sysname.replace('_', ' ')} in Climate Zone {self.cz}.",
                             item=item, status="exception claimed" if exc else "applies")
            if sysname == "electric_resistance":
                if h.get("exception"):
                    self.req("150.2(b)1G:no-resistance", f"Electric resistance heat; exception claimed: "
                             f"{h['exception']}", item=item, status="exception claimed")
                else:
                    self.req("150.2(b)1G:no-resistance", "The altered system uses electric resistance as the "
                             "primary heat source and no exception is recorded.", item=item, status="FAIL")
            elif ch in ("complete_replacement", "equipment_replaced"):
                self.req("150.2(b)1G:no-resistance", "Altered space-heating system.", item=item)

    def _water(self):
        for w in self.e.get("water_heating", []):
            item = f"{w['id']} ({w['type'].replace('_', ' ')} water heater, {w['change']})"
            if w["change"] == "new" and "addition" in self.work:
                ok = w["type"] == "heat_pump" or (
                    w["type"] == "electric_point_of_use" and self.cfa is not None
                    and self.cfa <= threshold("addition-wh-point-of-use"))
                self.req("150.2(a)1D:water-heater", "A water heater is added for the addition.", item=item,
                         status="applies" if ok or not self.prescriptive else "FAIL")
            else:
                ok = w["type"] in ("gas", "propane", "heat_pump") or (
                    w["type"] == "consumer_electric" and w.get("existing_type") == "electric_resistance")
                self.req("150.2(b)1H:water-heater", "The water heater is replaced or altered.", item=item,
                         status="applies" if ok or not self.prescriptive else "FAIL")
            if w["type"] == "other":
                self.ask(item, "Water heater type 'other': 150.2(a)1D and 150.2(b)1H allow a system the "
                         "Executive Director has determined equivalent. Record that determination.", w["id"],
                         "2025 CEnC 150.2(b)1H")

    def _lighting(self):
        lt = self.e.get("lighting")
        if not lt or lt["change"] == "none":
            return
        if "alteration" in self.work:
            self.req("150.2(b)1K:lighting", "The lighting is altered.")
        for rid in ("150.0(k)1A:ja8", "150.0(k)1C:recessed", "150.0(k)1E:blank-boxes", "150.0(k)2A:on-off",
                    "150.0(k)2E:auto-off", "150.0(k)2F:dimming", "150.0(k)2G:independent", "150.0(k)3A:outdoor"):
            self.req(rid, "New or altered lighting.")

    # -- results
    def rules(self) -> list[dict]:
        """The checks as project.json `rules` entries (schema shape)."""
        out = []
        for c in self.checks:
            r = {"id": c["id"], "element": f"{c['item']}: {c['element']}", "citation": c["citation"],
                 "source_from": "code", "kit_key": KIT_KEY_PREFIX + c["limit_id"],
                 "check": {"value": c["value"], "op": c["op"], "limit": c["limit"], "unit": c["unit"]}}
            if self.e.get("cd"):
                r["cd"] = self.e["cd"]
            if c["note"]:
                r["note"] = c["note"]
            out.append(r)
        return out

    def report(self) -> list[dict]:
        """Each check with its QA status (the kit's rules check), plus a limit
        that rests on an unverified value (an unverified CFA) downgraded to warn."""
        from .qa import rules_report
        rows = rules_report(_RulesOnly(self.p, self.rules()))
        for row, c in zip(rows, self.checks):
            row.update(item=c["item"], requirement=c["element"], quote=c["quote"], limit_id=c["limit_id"], limit_text=c["limit_text"],
                       deps=c["deps"])
            bad = [d for d in c["deps"] if self.p.value(d).unverified]
            row["limit_unverified"] = bad
            row["limit_fv"] = fv_sorted(t for d in bad for t in self.p.value(d).fv_tags)
            row["would"] = row["status"]
            if bad and row["status"] in ("pass", "fail"):
                row["status"] = "warn"
                row["message"] += (f"; {'would pass' if row['would'] == 'pass' else 'WOULD FAIL'}, but the "
                                   f"limit rests on unverified {bad}")
        return rows

    @property
    def ecc(self) -> list[dict]:
        return [r for r in self.reqs if r["ecc"]]

    @property
    def registration_required(self) -> bool:
        return bool(self.ecc)

    def forms(self) -> list[dict]:
        """Suggested state forms, with where each name comes from."""
        fm = {f["id"]: f for f in data()["forms"]}
        out = []
        if not self.prescriptive:
            return [fm["CF1R-PRF-01-E"]]
        if "addition" in self.work:
            out.append(fm["CF1R-ADD"])
        if "alteration" in self.work:
            fen = any(f["change"] == "replacement" for f in self.e.get("fenestration", []))
            wh = bool(self.e.get("water_heating")) and "addition" not in self.work
            hv = any(h["change"] in ("complete_replacement", "equipment_replaced", "refrigerant_altered")
                     for h in self.e.get("hvac", []))
            if fen or wh:
                out.append(fm["CF1R-ALT-05-E"])
            if hv:
                out.append(fm["CF1R-ALT-02-E"])
            if not (fen or wh or hv) or any(f["change"] == "added" for f in self.e.get("fenestration", [])) \
                    or self.e.get("lighting", {}).get("change") not in (None, "none"):
                out.append(fm["CF1R-ALT-01-E"])
        return list({f["id"]: f for f in out}.values())

    def summary(self) -> dict:
        rows = self.report()
        counts = {k: sum(1 for r in rows if r["status"] == k) for k in ("pass", "fail", "warn")}
        fails = [r for r in self.reqs if r["status"] == "FAIL"]
        return {
            "climate_zone": self.cz, "climate_zone_value": self.cz_val.key if self.cz_val else None,
            "path": self.path, "work": self.work, "checks": counts,
            "check_lines": [f"{r['status'].upper():4}  {r['message']}" for r in rows],
            "requirements_failed": [f"{r['id']} {r['item'] or ''}: {r['why']}" for r in fails],
            "asks": [f"{a['item']}: {a['message']}" for a in self.asks],
            "ecc_field_verification": [f"{r['citation']}: {r['title']}" + (f" [{r['item']}]" if r["item"] else "")
                                       for r in self.ecc],
            "registration_required": self.registration_required,
            "performance_run_required": not self.prescriptive,
            "forms": [f["id"] for f in self.forms()],
            "notes": [i["message"] for i in self.info],
        }


class _RulesOnly:
    """A project seen through a different `rules` list, for qa.rules_report."""

    def __init__(self, project, rules):
        self._p = project
        self.data = dict(project.data, rules=rules)

    def __getattr__(self, name):
        return getattr(self._p, name)


def plan(project) -> Plan | None:
    """The energy plan, or None when project.json has no `energy` block."""
    return Plan(project) if project.data.get("energy") else None


def rules_in_sync(project) -> dict:
    """Compare the T24- rules in project.json with the ones the energy block generates."""
    pl = plan(project)
    want = pl.rules() if pl else []
    have = [r for r in project.data.get("rules", []) if r["id"].startswith(RULE_PREFIX)]
    key = lambda r: json.dumps(r, sort_keys=True)
    return {"in_sync": sorted(map(key, want)) == sorted(map(key, have)),
            "generated": len(want), "in_file": len(have),
            "missing": [r["id"] for r in want if key(r) not in set(map(key, have))],
            "stale": [r["id"] for r in have if key(r) not in set(map(key, want))]}


def write_rules(project_path: str) -> dict:
    """Replace the T24- rules in project.json with the generated ones. Other rules stay in order."""
    from .model import Project
    p = Project.load(project_path)
    pl = plan(p)
    if pl is None:
        raise EnergyError("project.json has no energy block")
    with open(project_path, encoding="utf-8") as fh:
        text = fh.read()
    raw = json.loads(text)
    # keep the file's own indent (mechanical: the first indented line)
    first = next((ln for ln in text.splitlines()[1:] if ln.strip()), "")
    indent = (len(first) - len(first.lstrip(" "))) or 1
    kept = [r for r in raw.get("rules", []) if not r["id"].startswith(RULE_PREFIX)]
    raw["rules"] = kept + pl.rules()
    with open(project_path, "w", encoding="utf-8") as fh:
        json.dump(raw, fh, indent=indent, ensure_ascii=False)
        fh.write("\n")
    return {"written": len(pl.rules()), "kept": len(kept)}


# ---------------------------------------------------------------- sheet panels

def _txt(kit, template, cd=()):
    """Literal text (braces escaped, not a template) through kit.text, with its cd for QA."""
    return kit.text(str(template).replace("{", "{{").replace("}", "}}"), cd=cd or ())


def _drawn(kit, row, cd):
    key = row.get("resolved_key")
    if row["value_status"] is None:
        return "NOT ENTERED"
    val = kit.project.value(key)
    if not _printable(kit, val):
        return "NOT SELECTED"
    pre = {"R-value": "R-"}.get(val.unit, "")
    code = "sf" if val.unit == "sf" else "n"
    return kit.text(pre + "{" + key + ":" + code + "}", cd=cd)


def _status_cell(kit, row, cd):
    st = row["status"]
    if st == "pass":
        deps = [row["resolved_key"], *row.get("deps", ())]
        return kit.claim("MEETS", depends_on=deps, cd=cd)
    if st == "fail":
        return "DOES NOT MEET"
    if row["value_status"] is None:
        return "ENTER VALUE"
    val = kit.project.value(row["resolved_key"])
    if not _printable(kit, val):
        return "SELECT PRODUCT"
    if not val.unverified and row.get("limit_unverified"):
        word = "WOULD MEET" if row.get("would") == "pass" else "WOULD NOT MEET"
        return f"{word}; CONFIRM " + (" ".join(row["limit_fv"]) or "THE LIMIT")
    if "WOULD FAIL" in row["message"]:
        return "UNVERIFIED: WOULD NOT MEET"
    return "UNVERIFIED: WOULD MEET"


def _limit_cell(kit, row, cd):
    if row.get("limit_text"):
        return kit.text(row["limit_text"], cd=cd)
    word = "MAX." if row["op"] == "<=" else "MIN." if row["op"] == ">=" else "EXACTLY"
    return f"{_fmt_num(row['limit'], row['unit'])} {word}"


def summary_panel(kit, sheet, cell, title="TITLE 24 PART 6 ENERGY COMPLIANCE SUMMARY"):
    """Path, climate zone, scope, every check (limit, proposed value, status),
    the triggered requirements and what the kit cannot do."""
    p = kit.project
    pl = plan(p)
    if pl is None:
        raise EnergyError("project.json has no energy block")
    cd = pl.e.get("cd") or ()
    d = data()
    pan = sheet.panel(cell, title)
    pan.para(f"CODE: {d['edition'].upper()}. BUILDING: SINGLE-FAMILY (2025 CEnC 150.2). "
             f"WORK: {' AND '.join(w.upper() for w in pl.work)}.", size=7.5, bold=True)
    facts = [["CLIMATE ZONE", kit.text("CZ {" + pl.cz_val.key + ":n}", cd=cd) if pl.cz_val else "MISSING",
              _cz_source(p, pl)],
             ["COMPLIANCE PATH", pl.path.upper(), caps(pl.e.get("path_reason", "")) or "DRAFTER'S CHOICE"]]
    if pl.cfa_val is not None:
        facts.append(["ADDITION CONDITIONED FLOOR AREA", kit.text("{" + pl.cfa_val.key + ":sf}", cd=cd),
                      f"SETS THE 150.2(a) BRANCH ({_th('addition-tiny')} / {_th('addition-small')} / {_th('addition-ventilation')} SQ FT)"])
    pan.table([("ITEM", 2.4), ("ENTRY", 1.9, "wrap"), ("BASIS", None, "wrap")], facts, size=7.6)
    rows = pl.report()
    if rows:
        pan.heading("PRESCRIPTIVE AND MANDATORY CHECKS" if pl.prescriptive else "MANDATORY CHECKS", size=8.5)
        body = []
        for r in rows:
            body.append([r["item"].upper(), caps(r["requirement"]), r["citation"].replace("2025 CEnC ", "CEnC "),
                         _limit_cell(kit, r, cd), _drawn(kit, r, cd), _status_cell(kit, r, cd)])
        pan.table([("ITEM", 1.55, "wrap"), ("REQUIREMENT", None, "wrap"), ("CODE", 1.55, "wrap"),
                   ("LIMIT", 1.35, "wrap"), ("PROPOSED", 0.95, "wrap"), ("STATUS", 1.0, "wrap")], body, size=7.6)
    if pl.info:
        pan.heading("EXCEPTIONS AND ZONES WITH NO REQUIREMENT", size=8.5)
        for i in pl.info:
            pan.para(_txt(kit, caps(i["message"]), cd), size=7.6)
    if pl.asks:
        pan.heading("OPEN ITEMS THIS SHEET CANNOT SETTLE", size=8.5)
        for a in pl.asks:
            pan.para(_txt(kit, caps(f"{a['item']}: {a['message']}"), cd), size=7.6)
    pan.heading("WHAT THIS SET CANNOT DO", size=8.5)
    for line in cannot_do(pl):
        pan.para(line, size=7.2, bold=True)
    return pan


def _cz_source(p, pl):
    v = pl.cz_val
    if v is None:
        return ""
    src = p.sources.get(v.source or "", {})
    zipc = pl.e.get("zip")
    base = f"ZIP {zipc}: " if zipc else ""
    return caps(base + (src.get("note") or v.source or "NO SOURCE"))


def cannot_do(pl) -> list[str]:
    out = []
    if not pl.prescriptive:
        out.append("PERFORMANCE PATH: A CBECC-RES (COMMISSION-CERTIFIED SOFTWARE) RUN DECIDES COMPLIANCE. "
                   "THIS SHEET DOES NOT RUN IT; THE ENERGY CONSULTANT OR DOCUMENTATION AUTHOR DOES.")
    if pl.registration_required:
        out.append("ECC (HERS) FIELD VERIFICATION IS REQUIRED: THE CF1R MUST BE REGISTERED WITH AN ECC-PROVIDER "
                   "DATA REGISTRY (TITLE 24 PART 1 10-103(a)1B), AND A CERTIFIED ECC-RATER MUST TEST ON SITE. "
                   "THIS SET CANNOT REGISTER OR VERIFY IT.")
    out.append("THE CERTIFICATE OF COMPLIANCE (CF1R) COMES FROM THE STATE FORM OR CBECC-RES AND IS SIGNED BY ITS "
               "DOCUMENTATION AUTHOR AND THE RESPONSIBLE PERSON (10-103(a)). THIS SHEET IS NOT A CF1R.")
    return out


def requirements_panel(kit, sheet, cell, title="REQUIREMENTS THE SCOPE TRIGGERS"):
    """The triggered requirements: code section, what it requires, why it applies, ECC."""
    pl = plan(kit.project)
    cd = pl.e.get("cd") or ()
    pan = sheet.panel(cell, title)
    rows = []
    for r in pl.reqs:
        if r["id"].startswith("150.0(k)"):
            continue                     # lighting notes print in mandatory_notes
        st = {"applies": "APPLIES", "FAIL": "NOT MET", "exception claimed": "EXCEPTION CLAIMED"}[r["status"]]
        rows.append([r["citation"].replace("2025 CEnC ", "CEnC "), _txt(kit, caps(r["plain"]), cd),
                     _txt(kit, caps(((r["item"] + ": ") if r["item"] else "") + r["why"]), cd),
                     ("YES" if r["ecc"] else "NO"), st])
    pan.table([("CODE", 1.5, "wrap"), ("REQUIREMENT", None, "wrap"), ("WHY IT APPLIES", 2.1, "wrap"),
               ("ECC", 0.4), ("STATUS", 0.95, "wrap")], rows, size=7.6)
    return pan


def mandatory_notes(kit, ids=None) -> list:
    """Plan notes for the triggered 150.0(k) lighting measures and 150.0(q), quoted, with citation."""
    pl = plan(kit.project)
    cd = pl.e.get("cd") or ()
    out = []
    for r in pl.reqs:
        if not r["id"].startswith("150.0(k)") or (ids and r["id"] not in ids):
            continue
        out.append(_txt(kit, f"{r['citation'].replace('2025 CEnC', '2025 CEnC SECTION')}: "
                             f"\"{_clean(r['quote'])}\"", cd))
    return out


def _clean(q: str) -> str:
    """Corpus text for print: collapse whitespace and drop markdown list dashes. Mechanical."""
    return " ".join(q.replace("\n- ", " ").split())


def cf1r_panel(kit, sheet, cell, title="CF1R WORKSHEET: VALUES TO ENTER ON THE STATE FORM"):
    """What a drafter types into the state CF1R form or CBECC-Res, from project.json."""
    p = kit.project
    pl = plan(p)
    cd = pl.e.get("cd") or ()
    pan = sheet.panel(cell, title)
    pan.para("NOT A CERTIFICATE OF COMPLIANCE. THE CF1R ITSELF COMES FROM THE STATE FORM OR CBECC-RES AND MUST BE "
             "SIGNED BY ITS AUTHOR. THIS WORKSHEET ONLY LISTS THE ENTRIES, EACH FROM THE PROJECT DATA OF THIS SET.", size=7.0, bold=True)
    rows = []
    forms = pl.forms()
    rows.append(["FORM", " / ".join(f["id"] for f in forms),
                 caps("; ".join(f["confidence"] for f in forms))])
    rows.append(["PROJECT ADDRESS", _txt(kit, p.meta["address"]), "TITLE BLOCK"])
    if pl.cz_val is not None:
        rows.append(["CLIMATE ZONE", kit.text("{" + pl.cz_val.key + ":n}", cd=cd), _cz_source(p, pl)])
    rows.append(["COMPLIANCE METHOD", pl.path.upper() + (" (CBECC-RES)" if not pl.prescriptive else ""), "ENERGY.PATH"])
    rows.append(["BUILDING TYPE", "SINGLE-FAMILY", "ENERGY.BUILDING"])
    add = pl.e.get("addition", {})
    for f, label in (("cfa", "ADDITION CFA"), ("existing_cfa", "EXISTING CFA")):
        v = _val(p, add.get(f))
        if v is not None:
            rows.append([label, _entry(kit, [("", v, "")], cd), v.key.upper()])
    for it in pl.e.get("fenestration", []):
        parts = [("AREA ", _val(p, it.get("area")), ""), ("U ", _val(p, it.get("u_factor")), ""),
                 ("SHGC ", _val(p, it.get("shgc")), "")]
        tail = f"; FACES {it['orientation']}" if it.get("orientation") else ""
        rows.append([f"FENESTRATION {it['id']} ({it['kind'].replace('_', ' ')}, {it['change']})".upper(),
                     _entry(kit, parts, cd, tail), (it.get("product") or "PRODUCT NOT RECORDED").upper()])
    for d in pl.e.get("doors", []):
        rows.append([f"DOOR {d['id']} ({d['change']})".upper(),
                     _entry(kit, [("U ", _val(p, d.get("u_factor")), "")], cd), (d.get("product") or "").upper()])
    for it in pl.e.get("insulation", []):
        rows.append([f"INSULATION {it['id']}".upper(),
                     _entry(kit, [(it["assembly"].replace("_", " ").upper() + ": ", _val(p, it.get("r_value")), "R-")],
                            cd), (it.get("product") or "").upper()])
    for h in pl.e.get("hvac", []):
        rows.append([f"HVAC {h['id']}".upper(), f"{h['system']} {h['change']}".replace("_", " ").upper()
                     + (", DUCTLESS" if h.get("ducted") is False else ""), (h.get("product") or "").upper()])
    for d in pl.e.get("ducts", []):
        rows.append([f"DUCTS {d['id']}".upper(), f"{d['change']}, {d['location']} space".upper(),
                     _entry(kit, [("R-VALUE ", _val(p, d.get("r_value")), "R-")], cd) if d.get("r_value") else ""])
    for w in pl.e.get("water_heating", []):
        rows.append([f"WATER HEATER {w['id']}".upper(), f"{w['type']} ({w['change']})".replace("_", " ").upper(),
                     (w.get("product") or "").upper()])
    ecc = pl.ecc
    rows.append(["ECC FIELD VERIFICATION", "; ".join(sorted({r["citation"].replace("2025 CEnC ", "")
                                                             for r in ecc})) or "NONE TRIGGERED BY THE ITEMS ABOVE",
                 "ECC-RATER ON SITE (CF3R)" if ecc else ""])
    rows.append(["REGISTRATION", "REQUIRED: ECC-PROVIDER DATA REGISTRY" if ecc else
                 "NOT TRIGGERED BY THE ITEMS ABOVE; THE CITY MAY STILL ASK FOR A CF1R", "TITLE 24 PART 1 10-103(a)1"])
    rows.append(["SIGNATURES", "DOCUMENTATION AUTHOR AND RESPONSIBLE PERSON SIGN THE STATE FORM", "10-103(a)"])
    pan.table([("FORM FIELD", 2.1, "wrap"), ("ENTER", None, "wrap"), ("FROM", 2.2, "wrap")], rows, size=7.6)
    return pan


def _printable(kit, v) -> bool:
    if v is None or v.status == "PLACEHOLDER":
        return False
    return not any(kit.project.values[u].status == "PLACEHOLDER" for u in v.unverified_inputs)


def _entry(kit, parts, cd, tail=""):
    """One table cell from (label, Value or None, prefix) parts, filled by kit.text in one call,
    so the cell keeps every key and FV tag. A missing value prints NOT ENTERED, a PLACEHOLDER
    NOT SELECTED; neither prints a number."""
    bits = []
    for label, v, pre in parts:
        lab = label.replace("{", "{{").replace("}", "}}")
        if v is None:
            bits.append(lab + "NOT ENTERED")
        elif not _printable(kit, v):
            bits.append(lab + "NOT SELECTED")
        else:
            bits.append(lab + pre + "{" + v.key + (":sf" if v.unit == "sf" else ":n") + "}")
    return kit.text("; ".join(bits) + tail.replace("{", "{{").replace("}", "}}"), cd=cd)


def stack(sheet, x, w, builders, gap=0.3):
    """Draw panels top to bottom in one column at (x, w) inches. Each builder
    takes a cell and returns its Panel; the panel's cell is then trimmed to
    what it used, so the next one starts right below it. Overflow still raises."""
    PT = 72.0
    top = sheet.drawing_area_in[1]
    for build in builders:
        pan = build((x, 0, w, top))
        bottom = pan.y - pan.pad
        box = (pan.box[0], bottom, pan.box[2], pan.box[3])
        sheet.cells[:] = [(rid, box if rid == pan.id else b) for rid, b in sheet.cells]
        pan.box = box
        top = round((bottom - sheet.da[1]) / PT - gap, 3)
    return top


def sheet(kit, sid, notes_ids=None, green=False):
    """A whole Title 24 sheet: the summary and checks, then the triggered
    requirements (left column); the CF1R worksheet, then the CALGreen measures
    when `green` (right column); lighting measures in the notes column."""
    sh = kit.sheet(sid)
    w, _ = sh.drawing_area_in
    left = round(w * 0.52, 2)
    stack(sh, 0, left - 0.25, [lambda c: summary_panel(kit, sh, c), lambda c: requirements_panel(kit, sh, c)])
    right = [lambda c: cf1r_panel(kit, sh, c)]
    if green:
        from . import greensheets
        right.append(lambda c: greensheets.measures_panel(kit, sh, c))
    stack(sh, left, w - left, right)
    notes = mandatory_notes(kit, notes_ids)
    sh.notes(notes, title="LIGHTING (2025 CEnC 150.0(k))") if notes else sh.notes([])
    return sh
