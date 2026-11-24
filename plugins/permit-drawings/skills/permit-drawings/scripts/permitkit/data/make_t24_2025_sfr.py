"""Build permitkit/data/t24-2025-sfr.json from the repo code corpus.

Every quote is cut verbatim from the corpus file it names, by start and end
anchors, so the data file never holds a retyped code line. Run:
  python3 make_t24_2025_sfr.py <repo root> <out json>
"""
import json
import os
import sys

ROOT = sys.argv[1]
OUT = sys.argv[2]
SC = os.path.join(ROOT, "data", "state-code")

S9 = "part-06-energy/subchapter-9-single-family-residential-buildings-additions-and-alterations-to-existing-residential-buildings.md"
S8 = "part-06-energy/subchapter-8-single-family-residential-buildings-performance-and-prescriptive-compliance-approaches.md"
S7 = "part-06-energy/subchapter-7-single-family-residential-buildings-mandatory-features-and-devices.md"
P1 = "part-01-admin/chapter-10-administrative-regulations-for-the-california-energy-commission-cec.md"
DEF = "part-01-admin/chapter-10-administrative-regulations-for-the-california-energy-commission-cec.md"

_cache = {}


def text(rel):
    if rel not in _cache:
        with open(os.path.join(SC, rel), encoding="utf-8") as fh:
            _cache[rel] = fh.read()
    return _cache[rel]


def cut(rel, start, end, nth=0):
    """The corpus text from `start` through `end` (inclusive). Fails loudly."""
    t = text(rel)
    i = -1
    for _ in range(nth + 1):
        i = t.find(start, i + 1)
        if i < 0:
            raise SystemExit(f"start anchor not found in {rel}: {start!r}")
    j = t.find(end, i)
    if j < 0:
        raise SystemExit(f"end anchor not found in {rel}: {end!r}")
    s = t[i:j + len(end)]
    if len(s) > 1600:
        raise SystemExit(f"quote too long ({len(s)}) for {start!r}")
    return s


def row(rel, label):
    for ln in text(rel).splitlines():
        if ln.startswith("| " + label + " |"):
            return ln
    raise SystemExit(f"table row {label!r} not found")


def table_limit(label, element, citation, op, unit, parse, unread=None):
    ln = row(S8, label)
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    vals = cells[1:]
    assert len(vals) == 16, (label, len(vals))
    groups, nr = {}, []
    unread = unread or {}
    for cz, cell in enumerate(vals, start=1):
        if str(cz) in unread:
            continue
        if cell in ("NR", "NA"):
            nr.append(cz)
            continue
        groups.setdefault((parse(cell), cell), []).append(cz)
    return {
        "element": element, "citation": citation, "file": S8, "quote": ln,
        "table_row": label, "op": op, "unit": unit,
        "values": [{"cz": czs, "limit": lim, "evidence": ev} for (lim, ev), czs in groups.items()],
        "no_requirement_cz": nr,
        "unread_cz": unread,
    }


def num(cell):
    return float(cell.replace("U-", "").replace("R-", "").replace("%", ""))


ALL = list(range(1, 17))

limits = {}

# ---- Table 150.1-A rows (prescriptive component package) -------------------------------
limits["T150.1-A:fen-u"] = table_limit(
    "Fenestration - Maximum U-factor12", "fenestration U-factor (maximum)",
    "2025 CEnC Table 150.1-A, Fenestration - Maximum U-factor", "<=", "u-factor", num)
limits["T150.1-A:fen-shgc"] = table_limit(
    "Fenestration - Maximum SHGC", "fenestration SHGC (maximum)",
    "2025 CEnC Table 150.1-A, Fenestration - Maximum SHGC", "<=", "ratio", num,
    unread={"15": "The corpus cell reads '0.203' (a footnote marker or a scrape error); the kit "
                  "does not guess. Sections 150.2(a)1Aiii and 150.2(b)1A Exception 1 state 0.23 for "
                  "Climate Zone 15 where they apply; otherwise read the printed table."})
limits["T150.1-A:fen-total-pct"] = table_limit(
    "Fenestration - Maximum Total Area", "total fenestration area (maximum, percent of CFA)",
    "2025 CEnC Table 150.1-A, Fenestration - Maximum Total Area", "<=", "pct", num)
limits["T150.1-A:fen-west-pct"] = table_limit(
    "Fenestration - Maximum West Facing Area", "west-facing fenestration area (maximum, percent of CFA)",
    "2025 CEnC Table 150.1-A, Fenestration - Maximum West Facing Area", "<=", "pct", num)
limits["T150.1-A:door-u"] = table_limit(
    "Door - Maximum U-Factor", "opaque swinging door U-factor (maximum)",
    "2025 CEnC Table 150.1-A, Door - Maximum U-Factor", "<=", "u-factor", num)
limits["T150.1-A:wall-u"] = table_limit(
    "Above Grade Framed Walls3", "above-grade framed wall assembly U-factor (maximum)",
    "2025 CEnC Table 150.1-A, Above Grade Framed Walls", "<=", "u-factor", num)


def text_limit(element, citation, rel, start, end, op, unit, values, cz_evidence=None, nth=0, **extra):
    q = cut(rel, start, end, nth)
    for v in values:
        assert v["evidence"] in q, (element, v["evidence"])
    if cz_evidence:
        for ev in cz_evidence:
            assert ev in q, (element, ev)
    d = {"element": element, "citation": citation, "file": rel, "quote": q, "op": op, "unit": unit,
         "values": values, "no_requirement_cz": [], "unread_cz": {}}
    if cz_evidence:
        d["cz_evidence"] = cz_evidence
    d.update(extra)
    return d


# ---- 150.2(a) additions -------------------------------------------------------------------
limits["150.2(a)1Bi:ceiling-r"] = text_limit(
    "vented-attic ceiling insulation, addition 700 sq ft or less (minimum)",
    "2025 CEnC 150.2(a)1Bi", S9,
    "i. Roof and ceiling insulation in a ventilated attic", "R-30 or greater.", ">=", "R-value",
    [{"cz": [1, 2, 4] + list(range(8, 17)), "limit": 38, "evidence": "R-38"},
     {"cz": [3, 5, 6, 7], "limit": 30, "evidence": "R-30"}],
    cz_evidence=["Climate Zones 1, 2, 4, and 8 through 16", "Climate Zones 3, and 5 through 7"])
limits["150.2(a)1:wall-ext-2x4"] = text_limit(
    "cavity insulation, extension of an existing 2x4 wood-framed wall in an addition (minimum)",
    "2025 CEnC 150.2(a)1Ai and 150.2(a)1Biii", S9,
    "iii.Extensions of existing wood-framed walls", "R-21 in a 2 × 6 framing.", ">=", "R-value",
    [{"cz": ALL, "limit": 15, "evidence": "R-15 in a 2 × 4 framing"}])
limits["150.2(a)1:wall-ext-2x6"] = text_limit(
    "cavity insulation, extension of an existing 2x6 wood-framed wall in an addition (minimum)",
    "2025 CEnC 150.2(a)1Ai and 150.2(a)1Biii", S9,
    "iii.Extensions of existing wood-framed walls", "R-21 in a 2 × 6 framing.", ">=", "R-value",
    [{"cz": ALL, "limit": 21, "evidence": "R-21 in a 2 × 6 framing"}])
limits["150.2(a)1Biv:west-60"] = text_limit(
    "west-facing fenestration area, addition 700 sq ft or less (maximum)",
    "2025 CEnC 150.2(a)1Biv", S9,
    "iv. In Climate Zones 2, 4 and 6-15; the maximum allowed west-facing", "or b below:", "<=", "sf",
    [{"cz": [2, 4] + list(range(6, 16)), "limit": 60, "evidence": "60 square feet"}],
    cz_evidence=["Climate Zones 2, 4 and 6-15"])
limits["150.2(a)1Biv-a:total-400-700"] = text_limit(
    "total fenestration area, addition over 400 and up to 700 sq ft (maximum)",
    "2025 CEnC 150.2(a)1Biv(a)", S9,
    "a. For additions that are 700 square feet or less but greater than 400", "conditioned floor area of the addition.",
    "<=", "sf", [{"cz": [2, 4] + list(range(6, 16)), "limit": None, "evidence": "120 square feet"}],
    kind="greater_of", floor_sf=120, pct_of_cfa=25, evidence_pct="25 percent",
    cz_from="150.2(a)1Biv:west-60")
limits["150.2(a)1Biv-b:total-400"] = text_limit(
    "total fenestration area, addition 400 sq ft or less (maximum)",
    "2025 CEnC 150.2(a)1Biv(b)", S9,
    "b. For additions that are 400 square feet or less", "conditioned floor area of the addition.",
    "<=", "sf", [{"cz": [2, 4] + list(range(6, 16)), "limit": None, "evidence": "75 square feet"}],
    kind="greater_of", floor_sf=75, pct_of_cfa=30, evidence_pct="30 percent",
    cz_from="150.2(a)1Biv:west-60")
limits["150.2(a)1Aii:total-700"] = text_limit(
    "total fenestration area, addition over 700 sq ft (maximum)",
    "2025 CEnC 150.2(a)1Aii", S9,
    "ii. The maximum allowed fenestration area shall be the greater of 175", "requirements of Section 150.1(c).",
    "<=", "sf", [{"cz": ALL, "limit": None, "evidence": "175 square feet"}],
    kind="greater_of", floor_sf=175, pct_of_cfa=20, evidence_pct="20 percent")
limits["150.2(a)1Aiii:cz15-shgc"] = text_limit(
    "fenestration SHGC in Climate Zone 15, addition over 700 sq ft (maximum)",
    "2025 CEnC 150.2(a)1Aiii", S9,
    "iii.Alterations that add fenestration area shall have a maximum SHGC value of 0.23 in Climate Zone 15.",
    "in Climate Zone 15.", "<=", "ratio", [{"cz": [15], "limit": 0.23, "evidence": "0.23"}])

# ---- 150.2(b) alterations -----------------------------------------------------------------
limits["150.2(b)1A-x1:cz15-shgc"] = text_limit(
    "SHGC of fenestration that increases area, Climate Zone 15 (maximum)",
    "2025 CEnC 150.2(b)1A Exception 1", S9,
    "Exception 1 to Section 150.2(b)1A: Alterations that increase fenestration area", "in Climate Zone 15.",
    "<=", "ratio", [{"cz": [15], "limit": 0.23, "evidence": "0.23"}])
limits["150.2(b)1B-x1:u"] = text_limit(
    "replacement vertical fenestration U-factor, 75 sq ft or less (maximum)",
    "2025 CEnC 150.2(b)1B Exception 1", S9,
    "Exception 1 to Section 150.2(b)1B:", "Climate Zones 2, 4 and 6 through 15.", "<=", "u-factor",
    [{"cz": ALL, "limit": 0.40, "evidence": "U-factor no greater than 0.40 in Climate Zones 1–16"}])
limits["150.2(b)1B-x1:shgc"] = text_limit(
    "replacement vertical fenestration SHGC, 75 sq ft or less (maximum)",
    "2025 CEnC 150.2(b)1B Exception 1", S9,
    "Exception 1 to Section 150.2(b)1B:", "Climate Zones 2, 4 and 6 through 15.", "<=", "ratio",
    [{"cz": [2, 4] + list(range(6, 16)), "limit": 0.35, "evidence": "SHGC value no greater than 0.35"}],
    cz_evidence=["Climate Zones 2, 4 and 6 through 15"])
limits["150.2(b)1B-x2:skylight-u"] = text_limit(
    "replaced skylight U-factor (maximum)", "2025 CEnC 150.2(b)1B Exception 2", S9,
    "Exception 2 to Section 150.2(b)1B:", "SHGC value no greater than 0.30.", "<=", "u-factor",
    [{"cz": ALL, "limit": 0.40, "evidence": "U-factor no greater than 0.40"}])
limits["150.2(b)1B-x2:skylight-shgc"] = text_limit(
    "replaced skylight SHGC (maximum)", "2025 CEnC 150.2(b)1B Exception 2", S9,
    "Exception 2 to Section 150.2(b)1B:", "SHGC value no greater than 0.30.", "<=", "ratio",
    [{"cz": ALL, "limit": 0.30, "evidence": "SHGC value no greater than 0.30"}])
limits["150.2(b)1B-x3:cz15-shgc"] = text_limit(
    "replacement vertical fenestration SHGC, Climate Zone 15 (maximum)",
    "2025 CEnC 150.2(b)1B Exception 3", S9,
    "Exception 3 to Section 150.2(b)1B:", "in Climate Zone 15.", "<=", "ratio",
    [{"cz": [15], "limit": 0.23, "evidence": "0.23"}])
limits["150.2(b)1Ji:ceiling-r49"] = text_limit(
    "vented-attic ceiling insulation, altered ceiling (minimum)", "2025 CEnC 150.2(b)1Ji", S9,
    "i.In Climate Zones 1 through 4, 6, and 8 through 16 insulation", "R-49 or greater for the insulation alone",
    ">=", "R-value", [{"cz": [1, 2, 3, 4, 6] + list(range(8, 17)), "limit": 49, "evidence": "R-49"}],
    cz_evidence=["Climate Zones 1 through 4, 6, and 8 through 16"])
limits["T150.2-D:duct-r"] = text_limit(
    "insulation of new ducts in unconditioned space (minimum)", "2025 CEnC Table 150.2-D", S9,
    "TABLE 150.2-D—DUCT INSULATION R-VALUE", "R-6R-8", ">=", "R-value",
    [{"cz": [3, 5, 6, 7], "limit": 6, "evidence": "R-6"},
     {"cz": [1, 2, 4] + list(range(8, 17)), "limit": 8, "evidence": "R-8"}],
    cz_evidence=["3, 5 through 7", "1, 2, 4, 8 through 16"])

# ---- 150.0 mandatory ------------------------------------------------------------------------
limits["150.0(q):u-040"] = text_limit(
    "fenestration weighted average U-factor, mandatory (maximum)", "2025 CEnC 150.0(q)", S7,
    "- (q) Fenestration products.", "maximum weighted average U-factor of 0.40.", "<=", "u-factor",
    [{"cz": ALL, "limit": 0.40, "evidence": "0.40"}])
limits["150.0(d):floor-r19"] = text_limit(
    "raised-floor insulation, wood framed, mandatory (minimum)", "2025 CEnC 150.0(d)", S7,
    "- (d) Raised-floor insulation.", "R-value of 19 or greater.", ">=", "R-value",
    [{"cz": ALL, "limit": 19, "evidence": "R-value of 19"}])
limits["150.0(c)6:wall-2x4"] = text_limit(
    "wall cavity insulation, 2x4 wood framing, mandatory (minimum)", "2025 CEnC 150.0(c)6", S7,
    "6. In wood framed assemblies, compliance with U-factors may be demonstrated by installing wall insulation",
    "with 16 inches on center spacing.", ">=", "R-value",
    [{"cz": ALL, "limit": 15, "evidence": "R-15 in 2x4 assemblies"}])
limits["150.0(c)6:wall-2x6"] = text_limit(
    "wall cavity insulation, 2x6 wood framing, mandatory (minimum)", "2025 CEnC 150.0(c)6", S7,
    "6. In wood framed assemblies, compliance with U-factors may be demonstrated by installing wall insulation",
    "with 16 inches on center spacing.", ">=", "R-value",
    [{"cz": ALL, "limit": 21, "evidence": "R-21 in 2x6 assemblies"}])
limits["150.0(a)2-x:ceiling-alt-r19"] = text_limit(
    "ceiling or rafter-roof insulation in an alteration, mandatory (minimum)",
    "2025 CEnC 150.0(a)2 Exception", S7,
    "Exception to Section 150.0(a)2: Ceilings and rafter roofs in an alteration", "R-19 or greater.",
    ">=", "R-value", [{"cz": ALL, "limit": 19, "evidence": "R-19"}])
limits["150.2(b)1N:door-u"] = dict(limits["T150.1-A:door-u"])
limits["150.2(b)1N:door-u"].update({
    "element": "opaque door U-factor where an alteration adds exterior door area (maximum)",
    "citation": "2025 CEnC 150.2(b)1N and Table 150.1-A, Door - Maximum U-Factor",
    "also_quote": cut(S9, "N.Exterior doors.", "requirement of Section 150.1(c)5."), "also_file": S9})

limits["150.2(a)1Aii:west-700"] = text_limit(
    "west-facing fenestration area, addition over 700 sq ft (maximum)",
    "2025 CEnC 150.2(a)1Aii and Table 150.1-A, Fenestration - Maximum West Facing Area", S9,
    "ii. The maximum allowed fenestration area shall be the greater of 175", "requirements of Section 150.1(c).",
    "<=", "sf", [{"cz": limits["T150.1-A:fen-west-pct"]["values"][0]["cz"], "limit": None, "evidence": "70 square feet"}],
    kind="greater_of", floor_sf=70, pct_from="T150.1-A:fen-west-pct",
    nr_note="Where Table 150.1-A shows NR for west-facing area, 150.1(c) sets no percentage; the kit prints no limit.")
limits["150.0(a)2:ceiling-r22"] = text_limit(
    "ceiling or rafter-roof insulation, mandatory (minimum)", "2025 CEnC 150.0(a)2", S7,
    "2. Ceilings and rafter roofs shall be insulated to achieve an area-weighted average U-factor not exceeding U-0.043",
    "R-22 or greater for the insulation alone.", ">=", "R-value",
    [{"cz": ALL, "limit": 22, "evidence": "R-22"}])


def table_req(label, citation):
    ln = row(S8, label)
    cells = [c.strip() for c in ln.strip().strip("|").split("|")][1:]
    assert len(cells) == 16
    return {"citation": citation, "file": S8, "quote": ln, "table_row": label,
            "req_cz": [cz for cz, c in enumerate(cells, start=1) if c in ("REQ", "Yes")]}


table_requirements = {
    "T150.1-A:refrig-hp": table_req("Refrigerant Charge Verification Heat Pumps",
                                    "2025 CEnC Table 150.1-A, Refrigerant Charge Verification Heat Pumps"),
    "T150.1-A:refrig-ac": table_req("Refrigerant Charge Verification Air Conditioners",
                                    "2025 CEnC Table 150.1-A, Refrigerant Charge Verification Air Conditioners"),
    "T150.1-A:qii": table_req("Quality Insulation Installation", "2025 CEnC Table 150.1-A, Quality Insulation Installation"),
}


def thr(value, unit, citation, rel, start, end, evidence):
    q = cut(rel, start, end)
    assert evidence in q, evidence
    return {"value": value, "unit": unit, "citation": citation, "file": rel, "quote": q, "evidence": evidence}


thresholds = {
    "addition-small": thr(700, "sf", "2025 CEnC 150.2(a)1B", S9,
                          "B. Additions that are 700 square feet or less shall meet the requirements of Section 150.1(c)",
                          "with the following modifications:", "700 square feet"),
    "addition-tiny": thr(400, "sf", "2025 CEnC 150.2(a)1Biv(b)", S9,
                         "b. For additions that are 400 square feet or less", "or less", "400 square feet"),
    "addition-roofing": thr(300, "sf", "2025 CEnC 150.2(a) Exception 1", S9,
                            "Exception 1 to Section 150.2(a):", "Section 150.1(c)11.", "300 square feet"),
    "addition-ventilation": thr(1000, "sf", "2025 CEnC 150.2(a)1Ci(a)1", S9,
                                "1. Additions to an existing dwelling unit that increase the conditioned floor area",
                                "1000 square feet.", "1000 square feet"),
    "alteration-added-fen": thr(16, "sf", "2025 CEnC 150.2(b)1A Exception 2", S9,
                                "Exception 2 to Section 150.2(b)1A:", "150.1(c)3B and C.", "16 square feet"),
    "alteration-replaced-fen": thr(75, "sf", "2025 CEnC 150.2(b)1B Exception 1", S9,
                                   "Exception 1 to Section 150.2(b)1B:", "Climate Zones 1–16", "75 square feet"),
    "alteration-new-duct-ft": thr(25, "ft", "2025 CEnC 150.2(b)1D", S9,
                                  "D. Altered duct systems—duct sealing.", "ducts are installed",
                                  "more than 25 feet"),
    "addition-wh-point-of-use": thr(500, "sf", "2025 CEnC 150.2(a)1Diii", S9,
                                    "iii. For additions that are 500 square feet or less", "RA4.4.5", "500 square feet"),
}


def req(title, citation, rel, start, end, plain, ecc=False, nth=0):
    return {"title": title, "citation": citation, "file": rel, "quote": cut(rel, start, end, nth),
            "plain": plain, "ecc": ecc}


requirements = {
    "150.2(a):scope": req(
        "Additions: mandatory measures and a compliance path", "2025 CEnC 150.2(a)", S9,
        "- (a)Additions. Additions to existing single-family residential buildings shall meet",
        "and either Section 150.2(a)1 or 2.",
        "An addition meets Sections 110.0 to 110.9, the listed 150.0 mandatory measures, and either the prescriptive or the performance approach."),
    "150.2(a)-x6:pv": req(
        "Additions: no PV system required", "2025 CEnC 150.2(a) Exception 6", S9,
        "Exception 6 to Section 150.2(a):", "are not required for additions.",
        "A photovoltaic system is not required for an addition."),
    "150.2(a)-x3:hvac-extended": req(
        "Additions: heating or cooling extended from the existing system", "2025 CEnC 150.2(a) Exception 3", S9,
        "Exception 3 to Section 150.2(a): Space-conditioning system.", "CRC 303.10.",
        "Existing heating and cooling equipment extended to the addition need not comply with Part 6; capacity must meet CRC 303.10."),
    "150.2(a)-x4:ducts-extended": req(
        "Additions: ducts extended from the existing duct system", "2025 CEnC 150.2(a) Exception 4", S9,
        "Exception 4 to Section 150.2(a): Space-conditioning system ducts.", "150.2(b)1Dii.",
        "Extended and existing ducts meet 150.2(b)1Di (insulation) and 150.2(b)1Dii (sealing, field verified).",
        ecc=True),
    "150.2(a)1Bv:no-qii": req(
        "Additions 700 sq ft or less: QII not required", "2025 CEnC 150.2(a)1Bv", S9,
        "v. Quality Insulation Installation (QII) requirements of Section 150.1(c)1E do not apply.",
        "do not apply.", "Quality Insulation Installation (QII) does not apply to an addition of 700 sq ft or less."),
    "150.2(a)1Bii:radiant-barrier": dict(req(
        "Additions 700 sq ft or less: radiant barrier", "2025 CEnC 150.2(a)1Bii", S9,
        "ii. Radiant barriers shall be installed in Climate Zones 2-15.", "Climate Zones 2-15.",
        "A radiant barrier is installed (Climate Zones 2 to 15)."),
        zones=list(range(2, 16)), zones_evidence="Climate Zones 2-15"),
    "150.2(a)1A:qii": req(
        "Additions over 700 sq ft: QII", "2025 CEnC 150.2(a)1A; 150.1(c)1E", S8,
        "E. All buildings shall comply with the quality insulation installation (QII) requirements shown in Table 150.1-A",
        "Reference Appendix RA3.5.",
        "Quality Insulation Installation applies (Table 150.1-A: Yes in every climate zone) and is field verified.",
        ecc=True),
    "150.2(a)1Ci:ventilation": req(
        "Additions: whole-dwelling ventilation airflow", "2025 CEnC 150.2(a)1Ci", S9,
        "a. Dwelling units that meet the conditions in Subsection 1 or 2 below shall not be required",
        "less than or equal to 1000 square feet.",
        "An addition of 1,000 sq ft or less of conditioned floor area does not trigger the whole-dwelling ventilation airflow of 150.0(o)1C, E or F."),
    "150.2(a)1Cii:local-exhaust": req(
        "Additions: local mechanical exhaust", "2025 CEnC 150.2(a)1Cii", S9,
        "ii. Local mechanical exhaust. Additions to existing buildings shall comply", "150.0(o)1G and 150.0(o)2.",
        "Bathroom and kitchen local exhaust in the addition meets 150.0(o)1G and 150.0(o)2."),
    "150.2(a)1D:water-heater": req(
        "Additions: an additional water heater", "2025 CEnC 150.2(a)1D", S9,
        "D. Water heater. When an additional water heater is installed as part of the addition",
        "ANSI/CTA-2045-B communication port; or",
        "A new water heater for the addition is a heat pump water heater (or another type 150.2(a)1D lists)."),
    "150.2(a)1E:loads": req(
        "Additions: load calculations and system capacity", "2025 CEnC 150.2(a)1E", S9,
        "E.Space-conditioning load calculations and system capacity.", "described in Section 150.0(h).",
        "Space-conditioning equipment for the addition is sized from a load calculation (150.0(h))."),
    "150.1(c)7A:refrigerant": req(
        "New heat pump or air conditioner: refrigerant charge and airflow verification",
        "2025 CEnC 150.1(c)7A; Table 150.1-A, Refrigerant Charge Verification", S8,
        "A. Refrigerant charge. When refrigerant charge verification is shown as  required by Table 150.1-A",
        "including but not limited to ducted split systems, ducted packaged systems, small duct high velocity systems, and mini-split systems",
        "Where Table 150.1-A requires it (heat pumps: every climate zone), refrigerant charge and system airflow are field verified.",
        ecc=True),
    "150.2(b)1:scope": req(
        "Alterations: altered components meet the mandatory measures", "2025 CEnC 150.2(b)1", S9,
        "1. Prescriptive approach. The altered component and any newly installed equipment serving the alteration",
        "150.0(p) through (q); and",
        "The altered component and new equipment serving it meet Sections 110.0 to 110.9 and the listed 150.0 mandatory measures."),
    "150.2(b)1C:complete-replacement": req(
        "Alterations: entirely new or complete replacement space-conditioning system", "2025 CEnC 150.2(b)1C", S9,
        "C. Entirely new or complete replacement space-conditioning systems installed as part of an alteration",
        "and Table 150.2-A.",
        "A complete new or replacement system meets 150.0(h), (i), (j), (m) and 150.2(b)1F and G."),
    "150.2(b)1D:duct-sealing": req(
        "Alterations: more than 25 ft of new or replacement ducts", "2025 CEnC 150.2(b)1D", S9,
        "D. Altered duct systems—duct sealing. In all climate zones, when more than 25 feet",
        "the ducts shall comply with the applicable requirements of Subsections i and ii below.",
        "Ducts are insulated per Table 150.2-D and the altered duct system is sealed and field verified.", ecc=True),
    "150.2(b)1E:duct-sealing": req(
        "Alterations: altered space-conditioning equipment, duct sealing", "2025 CEnC 150.2(b)1E", S9,
        "E. Altered space-conditioning system—duct sealing.", "Reference Residential Appendix RA3.1,",
        "Installing or replacing an air handler, condensing unit or coil triggers duct sealing with field verification (exceptions apply).",
        ecc=True),
    "150.2(b)1F:refrigerant": req(
        "Alterations: altered refrigerant-containing components", "2025 CEnC 150.2(b)1F", S9,
        "F. Altered space-conditioning system—mechanical cooling.", "Section 110.2(c).",
        "Thermostats are replaced with setback thermostats; refrigerant charge and airflow are field verified where 150.2(b)1Fii applies.",
        ecc=True),
    "150.2(b)1Fii:verify": req(
        "Alterations: which altered systems get charge and airflow verification", "2025 CEnC 150.2(b)1Fii", S9,
        "ii.Air-cooled air conditioners in Climate Zones 2 and 8 through 15 and air-source heat pumps in all climate zones",
        "shall comply with Subsections a and b,",
        "Air conditioners in Climate Zones 2 and 8 to 15, and heat pumps in every climate zone, get refrigerant charge and airflow verification.",
        ecc=True),
    "150.2(b)1G:no-resistance": req(
        "Alterations: altered space-heating system", "2025 CEnC 150.2(b)1G", S9,
        "G.  Altered space-heating system.", "electric resistance as the primary heat source.",
        "An altered or replacement space-heating system does not use electric resistance as the primary heat source (exceptions apply)."),
    "150.2(b)1H:water-heater": req(
        "Alterations: altered or replacement water heating", "2025 CEnC 150.2(b)1H", S9,
        "iii.Water heating system. The water heating system shall meet one of the following:",
        "a consumer electric water heater; or",
        "A replacement water heater is gas or propane, a heat pump water heater, or a consumer electric water heater where the existing one is electric resistance."),
    "150.2(b)1K:lighting": req(
        "Alterations: altered lighting", "2025 CEnC 150.2(b)1K", S9,
        "K.Lighting. The altered lighting system shall meet the lighting requirements of Section 150.0(k).",
        "luminaire efficacy requirements of Section 150.0(k).",
        "Altered lighting meets Section 150.0(k)."),
    "150.2(b)2:performance": req(
        "Alterations: performance approach", "2025 CEnC 150.2(b)2", S9,
        "2.Performance approach. The energy budget for alterations is expressed in terms of long-term system cost (LSC)",
        "Subsections A, B, and C below.",
        "Performance compliance compares long-term system cost with Commission-certified software (CBECC-Res)."),
    "150.2(a)2:performance": req(
        "Additions: performance approach", "2025 CEnC 150.2(a)2", S9,
        "2. Performance approach. The energy budget for additions is expressed in terms of long-term system cost (LSC).",
        "Items A, B and C below.",
        "Performance compliance compares long-term system cost with Commission-certified software (CBECC-Res)."),
    "150.1(b):software": req(
        "Performance approach: certified software", "2025 CEnC 150.1(b)", S8,
        "- (b) Performance approach. A building complies with the performance approach",
        "using Commission-certified compliance software as specified by Sections 10-109(c) and 10-116.",
        "Performance compliance uses Commission-certified compliance software."),
    "150.0(k)1A:ja8": req(
        "Lighting: luminaire efficacy (JA8)", "2025 CEnC 150.0(k)1A", S7,
        "A.Luminaire efficacy. All installed luminaires and light sources shall comply with Reference Joint Appendix JA8",
        "certified and marked as required by JA8.",
        "Every installed luminaire and light source is JA8 compliant, certified and marked."),
    "150.0(k)1C:recessed": req(
        "Lighting: recessed downlights", "2025 CEnC 150.0(k)1C", S7,
        "C. Recessed downlight luminaires in ceilings.", "when tested in accordance with ASTM E283.",
        "Recessed ceiling luminaires have no screw-base sockets and are labeled airtight."),
    "150.0(k)1E:blank-boxes": req(
        "Lighting: blank electrical boxes", "2025 CEnC 150.0(k)1E", S7,
        "E. Blank electrical boxes.", "no greater than the number of bedrooms.",
        "Blank boxes more than 5 ft above the floor do not outnumber the bedrooms."),
    "150.0(k)2A:on-off": req(
        "Lighting: wall-mounted ON/OFF controls", "2025 CEnC 150.0(k)2A", S7,
        "A. Lighting shall have readily accessible wall-mounted controls", "manually turned ON and OFF.",
        "Lighting has readily accessible wall-mounted ON/OFF controls."),
    "150.0(k)2E:auto-off": req(
        "Lighting: automatic-off controls", "2025 CEnC 150.0(k)2E", S7,
        "i.In bathrooms, garages, laundry rooms, utility rooms and walk-in closets",
        "occupancy or vacancy sensor providing automatic-off functionality.",
        "In bathrooms, garages, laundry, utility rooms and walk-in closets one luminaire is on an occupancy or vacancy sensor."),
    "150.0(k)2F:dimming": req(
        "Lighting: dimming controls in habitable spaces", "2025 CEnC 150.0(k)2F", S7,
        "F.Dimming controls. Lighting in habitable spaces", "manually adjusted up and down.",
        "Lighting in habitable spaces, including kitchens and bedrooms, has wall-mounted dimmers."),
    "150.0(k)2G:independent": req(
        "Lighting: independent controls", "2025 CEnC 150.0(k)2G", S7,
        "G. Independent controls.", "iv. Switched outlets.",
        "Undercabinet, undershelf and display-cabinet lighting and switched outlets are controlled separately from ceiling lighting."),
    "150.0(k)3A:outdoor": req(
        "Lighting: outdoor lighting on the building", "2025 CEnC 150.0(k)3A", S7,
        "A.Outdoor lighting permanently mounted to a residential building", "c. Controlled by an astronomical time clock control.",
        "Outdoor lighting mounted to the building has a manual switch plus photocell/motion, photocell/time switch, or astronomical clock control."),
    "150.0(q):fenestration": req(
        "Fenestration: mandatory maximum U-factor", "2025 CEnC 150.0(q)", S7,
        "- (q) Fenestration products.", "Wildland-Urban Interface (WUI) Fire Areas as designated by the local enforcement agency.",
        "Fenestration has a weighted average U-factor of 0.40 or less (exceptions for small areas, garden windows and WUI areas)."),
    "10-103(a)1B:registration": req(
        "Registration when field verification is required", "2025 Title 24 Part 1 §10-103(a)1B", P1,
        "B. For all low-rise residential buildings for which compliance requires field verification",
        "for registration and retention to an ECC-Provider data registry in compliance with Section 10-103.3.",
        "When compliance requires field verification, the Certificate of Compliance is registered with an ECC-Provider data registry."),
    "10-103(a)1C:discretion": req(
        "Small alterations without field verification", "2025 Title 24 Part 1 §10-103(a)1C", P1,
        "C. For alterations to existing residential buildings for which field verification is not required",
        "simplified Certificate of Compliance documentation for demonstrating compliance with the Standards.",
        "For window or water-heater replacements and additions under 300 sq ft with no field verification, the city may waive or simplify the CF1R."),
    "10-103:signatures": req(
        "Who signs the Certificate of Compliance", "2025 Title 24 Part 1 §10-103(a)", P1,
        "v. Be signed by the documentation author to certify the documentation is accurate and complete.",
        "eligible under Division 3 of the Business and Professions Code to accept responsibility for the design to certify conformance with Part 6.",
        "The CF1R is signed by its documentation author and by the person responsible for the design."),
    "ecc-rater": req(
        "ECC-Rater", "2025 Title 24 Part 1 §10-102, ECC-RATER", P1,
        "ECC-RATER is a person trained, tested, and certified by an ECC-Provider", "pursuant to the requirements of Section 10-103.",
        "Field verification and diagnostic testing is done by a certified ECC-Rater (earlier cycles called this a HERS Rater)."),
}

forms = [
    {"id": "CF1R-ALT-05-E", "for": "replacement fenestration (also section H of CF1R-ALT-01-E); water-heater replacement uses section K",
     "source": "skills/california/submittal-requirements/building/requirements.json rows state_energy_alteration_fenestration and state_energy_alteration_water_heater",
     "confidence": "CrossBeam state requirement rows; confirm on the Energy Commission's 2025 forms page"},
    {"id": "CF1R-ALT-02-E", "for": "space-conditioning system change-out (150.2(b)1C, E, F, G)",
     "source": "skills/california/submittal-requirements/building/requirements.json row state_energy_alteration_hvac",
     "confidence": "CrossBeam state requirement row; confirm on the Energy Commission's 2025 forms page"},
    {"id": "CF1R-ALT-01-E", "for": "other prescriptive alterations (general alteration certificate)",
     "source": "skills/california/submittal-requirements/building/requirements.json row state_energy_alteration_fenestration (section H)",
     "confidence": "named by a CrossBeam state requirement row; confirm the sections on the 2025 form"},
    {"id": "CF1R-ADD", "for": "prescriptive addition certificate (CrossBeam has no sourced 2025 form number)",
     "source": "no CrossBeam state row names the 2025 addition form number",
     "confidence": "unsourced form number: take it from the Energy Commission's 2025 forms page or the city's handout"},
    {"id": "CF1R-PRF-01-E", "for": "performance certificate printed by CBECC-Res (addition or alteration)",
     "source": "city skills that cite CBECC-Res output (for example skills/cities/*/residential-addition)",
     "confidence": "cited by city skills; the software prints the form"},
]

D1 = "part-06-energy/subchapter-1-all-occupancies-general-provisions--section-100-1-definitions-and-rules-of-construction.md"
definitions = {
    "cfa": {"citation": "2025 CEnC 100.1, CONDITIONED FLOOR AREA", "file": D1,
            "quote": cut(D1, "CONDITIONED FLOOR AREA (CFA) is the floor area", "enclosing the conditioned space.")},
    "fenestration-area": {"citation": "2025 CEnC 100.1, FENESTRATION AREA", "file": D1,
                          "quote": cut(D1, "FENESTRATION AREA is the rough opening area", "fenestration product.")},
    "west-facing": {"citation": "2025 CEnC 100.1, ORIENTATION, WEST-FACING", "file": D1,
                    "quote": cut(D1, "WEST-FACING is oriented to within 45 degrees of true west", "south of west (SW).")},
}

for _r in requirements.values():
    if "zones" in _r:
        assert _r["zones_evidence"] in _r["quote"], _r["citation"]

data = {
    "about": ("Title 24 Part 6 (2025 California Energy Code) limits for single-family additions and "
              "alterations, cut verbatim from the CrossBeam code corpus. Each limit names the corpus "
              "file it was read from. A climate zone a row could not be read for is listed in "
              "unread_cz and the kit asks the drafter instead of guessing."),
    "edition": "2025 California Energy Code (Title 24, Part 6), effective 2026-01-01",
    "corpus": "data/state-code in the CrossBeam repo (scraped from codes.iccsafe.org/content/CAEC2025P2)",
    "definitions": definitions, "limits": limits, "table_requirements": table_requirements, "thresholds": thresholds, "requirements": requirements, "forms": forms,
}
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
print("wrote", OUT, len(limits), "limits", len(thresholds), "thresholds", len(requirements), "requirements")
