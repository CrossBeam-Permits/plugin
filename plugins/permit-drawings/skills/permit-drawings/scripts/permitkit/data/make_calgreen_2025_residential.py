"""Build permitkit/data/calgreen-2025-residential.json from the repo code corpus.

Quotes are cut verbatim from the corpus by start and end anchors.
  python3 make_calgreen_2025_residential.py <repo root> <out json>
"""
import json
import os
import sys

ROOT, OUT = sys.argv[1], sys.argv[2]
SC = os.path.join(ROOT, "data", "state-code")
C3 = "part-11-green-building/chapter-3-green-building.md"
C4 = "part-11-green-building/chapter-4-residential-mandatory-measures.md"
_cache = {}


def text(rel):
    if rel not in _cache:
        with open(os.path.join(SC, rel), encoding="utf-8") as fh:
            _cache[rel] = fh.read()
    return _cache[rel]


def cut(rel, start, end):
    t = text(rel)
    i = t.find(start)
    if i < 0:
        raise SystemExit(f"start not found: {start!r}")
    j = t.find(end, i)
    if j < 0:
        raise SystemExit(f"end not found: {end!r}")
    s = t[i:j + len(end)]
    if len(s) > 700:
        raise SystemExit(f"quote too long ({len(s)}): {start!r}")
    return s


def m(section, division, title, start, end, responsibility, verification, guidance):
    return {"section": section, "division": division, "title": title, "file": C4,
            "quote": cut(C4, start, end), "responsibility": responsibility,
            "verification": verification, "guidance": guidance}


DIV = {
    "4.1": "DIVISION 4.1 PLANNING AND DESIGN",
    "4.3": "DIVISION 4.3 WATER EFFICIENCY AND CONSERVATION",
    "4.4": "DIVISION 4.4 MATERIAL CONSERVATION AND RESOURCE EFFICIENCY",
    "4.5": "DIVISION 4.5 ENVIRONMENTAL QUALITY",
}

measures = [
    m("4.106.2", "4.1", "Storm water drainage and retention during construction",
      "Projects which disturb less than one acre of soil", "manage storm water drainage during construction.",
      "CONTRACTOR", "INSPECTOR DURING CONSTRUCTION",
      "Site work that disturbs soil (footings, grading). Interior-only work usually disturbs none."),
    m("4.106.3", "4.1", "Grading and paving",
      "Construction plans shall indicate how the site grading or drainage system will manage",
      "keep water from entering buildings.", "DESIGNER (SHOW ON SITE PLAN)", "PLAN CHECK; INSPECTOR",
      "Has its own exception: additions and alterations not altering the drainage path."),
    m("4.106.4", "4.1", "Electric vehicle (EV) charging for new construction",
      "New construction shall comply with Section 4.106.4.1 or 4.106.4.2.",
      "New construction shall comply with Section 4.106.4.1 or 4.106.4.2.", "DESIGNER / ELECTRICIAN",
      "PLAN CHECK; INSPECTOR",
      "The text names new construction. An addition or alteration needs a sourced reason (for example a city amendment) to apply it."),
    m("4.303.1", "4.3", "Water conserving plumbing fixtures and fittings",
      "Plumbing fixtures (water closets and urinals) and fittings (faucets and showerheads) shall comply",
      "Sections 4.303.1.1, 4.303.1.2, 4.303.1.3 and 4.303.1.4.", "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL",
      "New or replaced fixtures and fittings in the area of work."),
    m("4.303.1 Note", "4.3", "Noncompliant plumbing fixtures (Civil Code 1101.1)",
      "Note:  All noncompliant plumbing fixtures in any residential real property shall be replaced",
      "or final permit approval by the local building department.", "OWNER / CONTRACTOR",
      "INSPECTOR AT FINAL",
      "A note to the Civil Code: read Civil Code 1101.1 et seq. for which homes and fixtures it covers (age of the building, the kind of permit) before applying it."),
    m("4.303.1.1", "4.3", "Water closets",
      "The effective flush volume of all water closets shall not exceed 1.28 gallons per flush.",
      "WaterSense Specification for Tank-type Toilets.", "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL",
      "A new or replaced water closet."),
    m("4.303.1.3.1", "4.3", "Showerheads",
      "4.303.1.3.1 Single showerhead.", "WaterSense Specification for Showerheads.",
      "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL", "A new or replaced showerhead (a hand-held shower counts)."),
    m("4.303.1.3.2", "4.3", "Multiple showerheads serving one shower",
      "4.303.1.3.2 Multiple showerheads serving one shower.", "only one shower outlet to be in operation at a time.",
      "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL", "A shower with more than one outlet."),
    m("4.303.1.4.1", "4.3", "Residential lavatory faucets",
      "4.303.1.4.1 Residential lavatory faucets.", "less than 0.8 gallons per minute at 20 psi.",
      "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL", "A new or replaced lavatory faucet."),
    m("4.303.1.4.4", "4.3", "Kitchen faucets",
      "4.303.1.4.4 Kitchen faucets.", "default to a maximum flow rate of 1.8 gallons per minute at 60 psi.",
      "CONTRACTOR / PLUMBER", "INSPECTOR AT FINAL", "A new or replaced kitchen faucet."),
    m("4.303.3", "4.3", "Standards for plumbing fixtures and fittings",
      "Plumbing fixtures and fittings shall be installed in accordance with the California Plumbing Code",
      "Table 1701.1 of the California Plumbing Code.", "CONTRACTOR / PLUMBER", "INSPECTOR",
      "Any new plumbing fixture or fitting."),
    m("4.304.1", "4.3", "Outdoor potable water use in landscape areas",
      "Residential developments shall comply with a local water efficient landscape ordinance",
      "whichever is more stringent.", "OWNER / LANDSCAPE CONTRACTOR", "PLAN CHECK (LANDSCAPE PLAN)",
      "New or rehabilitated landscape that the project installs; read MWELO for its own area thresholds."),
    m("4.406.1", "4.4", "Rodent proofing",
      "Annular spaces around pipes, electric cables, conduits or other openings in sole/bottom plates at exterior walls",
      "a similar method acceptable to the enforcing agency.", "CONTRACTOR", "INSPECTOR AT FRAMING",
      "New exterior wall sole plates with penetrations."),
    m("4.408.1", "4.4", "Construction waste management",
      "Recycle and/or salvage for reuse a minimum of 65 percent",
      "more stringent local construction and demolition waste management ordinance.", "CONTRACTOR",
      "DOCUMENTATION TO THE CITY (4.408.5)", "Construction or demolition waste from the work."),
    m("4.408.2", "4.4", "Construction waste management plan",
      "Submit a construction waste management plan in conformance with Items 1 through 5.",
      "available during construction for examination by the enforcing agency.", "CONTRACTOR",
      "PLAN SUBMITTED; KEPT ON SITE", "One of the three ways to show 4.408.1 (4.408.2, 4.408.3 or 4.408.4)."),
    m("4.408.3", "4.4", "Waste management company",
      "Utilize a waste management company, approved by the enforcing agency",
      "material diverted from the landfill complies with Section 4.408.1.", "CONTRACTOR",
      "HAULER DIVERSION RECORDS", "One of the three ways to show 4.408.1."),
    m("4.408.4", "4.4", "Waste stream reduction alternative [LR]",
      "Projects that generate a total combined weight of construction and demolition waste disposed of in landfills, which do not exceed 3.4 pounds",
      "requirement in Section 4.408.1.", "CONTRACTOR", "DISPOSAL WEIGHT RECORDS",
      "One of the three ways to show 4.408.1."),
    m("4.408.5", "4.4", "Documentation",
      "Documentation shall be provided to the enforcing agency which demonstrates compliance with Section 4.408.2",
      "Section 4.408.3 or Section 4.408.4.", "CONTRACTOR", "BEFORE FINAL INSPECTION",
      "Goes with 4.408.1."),
    m("4.410.1", "4.4", "Operation and maintenance manual",
      "At the time of final inspection, a manual, compact disc, web-based reference or other media acceptable",
      "shall be placed in the building:", "CONTRACTOR", "INSPECTOR AT FINAL",
      "Read the list of contents; it is written for whole buildings."),
    m("4.503.1", "4.5", "Fireplaces",
      "Any installed gas fireplace shall be a direct-vent sealed-combustion type.",
      "certified to meet the emission limits.", "CONTRACTOR", "INSPECTOR",
      "A fireplace, woodstove or pellet stove the project installs."),
    m("4.504.1", "4.5", "Covering of duct openings and protection of mechanical equipment during construction",
      "At the time of rough installation, during storage on the construction site",
      "which may enter the system.", "CONTRACTOR (MECHANICAL)", "INSPECTOR AT ROUGH",
      "New or altered ducts or air-distribution equipment."),
    m("4.504.2.1", "4.5", "Adhesives, sealants and caulks",
      "Adhesives, sealants and caulks used on the project shall meet the requirements of the following standards",
      "air pollution or air quality management district rules apply:", "CONTRACTOR",
      "PRODUCT DATA AT THE CITY'S REQUEST (4.504.2.4)", "Adhesives, sealants or caulks used on the job."),
    m("4.504.2.2", "4.5", "Paints and coatings",
      "Architectural paints and coatings shall comply with VOC limits in Table 1 of the ARB Architectural Suggested Control Measure",
      "unless more stringent local limits apply.", "CONTRACTOR",
      "PRODUCT DATA AT THE CITY'S REQUEST (4.504.2.4)", "Paint or coating applied on the job."),
    m("4.504.2.3", "4.5", "Aerosol paints and coatings",
      "Aerosol paints and coatings shall meet the Product-weighted MIR Limits for ROC",
      "commencing with Section 94520", "CONTRACTOR", "PRODUCT DATA AT THE CITY'S REQUEST (4.504.2.4)",
      "Aerosol paint used on the job."),
    m("4.504.2.4", "4.5", "Verification",
      "Verification of compliance with this section shall be provided at the request of the enforcing agency.",
      "Verification of compliance with this section shall be provided at the request of the enforcing agency.",
      "CONTRACTOR", "AT THE CITY'S REQUEST", "Goes with 4.504.2.1 to 4.504.2.3."),
    m("4.504.3", "4.5", "Carpet systems",
      "All carpet installed in the building interior shall meet the requirements of the California Department of Public Health",
      "(Emission testing method for California Specification 01350).", "CONTRACTOR / FLOORING",
      "PRODUCT DATA", "Carpet the project installs."),
    m("4.504.4", "4.5", "Resilient flooring systems",
      "Where resilient flooring is installed, at least 80 percent of floor area receiving resilient flooring",
      "(Emission testing method for California Specification 01350).", "CONTRACTOR / FLOORING",
      "PRODUCT DATA", "Resilient flooring (vinyl, LVT, linoleum, rubber) the project installs."),
    m("4.504.5", "4.5", "Composite wood products",
      "Hardwood plywood, particleboard and medium density fiberboard composite wood products",
      "as shown in Table 4.504.5.", "CONTRACTOR / CABINET SUPPLIER", "PRODUCT DATA (4.504.5.1)",
      "Cabinets, shelving or panels of plywood, particleboard or MDF."),
    m("4.505.2", "4.5", "Concrete slab foundations",
      "Concrete slab foundations required to have a vapor retarder by the California Building Code",
      "shall also comply with this section.", "CONTRACTOR", "INSPECTOR BEFORE POUR",
      "A new slab that needs a vapor retarder; then 4.505.2.1 (capillary break)."),
    m("4.505.3", "4.5", "Moisture content of building materials",
      "Building materials with visible signs of water damage shall not be installed.",
      "exceed 19 percent moisture content.", "CONTRACTOR", "INSPECTOR BEFORE COVER (READINGS RECORDED)",
      "New wall or floor framing that will be enclosed."),
    m("4.506.1", "4.5", "Bathroom exhaust fans",
      "Each bathroom shall be mechanically ventilated and shall comply with the following:",
      "fans must be controlled by a humidity control.", "CONTRACTOR (ELECTRICAL / MECHANICAL)",
      "INSPECTOR AT FINAL", "A bathroom (a room with a bathtub or shower) in the area of work."),
    m("4.507.2", "4.5", "Heating and air-conditioning system design",
      "Heating and air-conditioning systems shall be sized, designed and have their equipment selected using the following methods:",
      "(Residential Equipment Selection) or other equivalent design software or methods.",
      "MECHANICAL DESIGNER / CONTRACTOR", "LOAD CALCULATIONS AT PLAN CHECK",
      "A new or replaced heating or cooling system."),
]

trigger = {
    "section": "301.1.1", "title": "Additions and alterations", "file": C3,
    "quote": cut(C3, "[HCD] The mandatory provisions of Chapter 4 shall be applied to additions or alterations",
                 "to and/or within the specific area of the addition or alteration."),
    "note_quote": cut(C3, "Note: Repairs including, but not limited to, resurfacing",
                      "are not considered alterations for the purpose of this section."),
}

data = {
    "about": ("CALGreen (2025 California Green Building Standards Code, Title 24 Part 11) Chapter 4 "
              "residential mandatory measures that commonly reach additions and alterations, with short "
              "quotes cut verbatim from the CrossBeam code corpus. The drafter decides which apply to the "
              "project and records why; the kit never selects a measure by itself. responsibility and "
              "verification are suggested defaults the drafter may change; they are not code text."),
    "edition": "2025 California Green Building Standards Code (CALGreen, Title 24, Part 11), effective 2026-01-01",
    "corpus": "data/state-code in the CrossBeam repo (scraped from codes.iccsafe.org/content/CAGBC2025P3)",
    "divisions": DIV, "trigger": trigger, "measures": measures,
}
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
print("wrote", OUT, len(measures), "measures")
