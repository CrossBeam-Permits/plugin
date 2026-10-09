---
name: hvac
description: "HVAC permits in Laguna Beach, CA. A furnace, air handler, condenser, or mini-split replaced or added, with its ducts and electrical. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions hvac in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Mechanical Code (Title 24, Part 4); 2025 California Plumbing Code (Title 24, Part 5); 2025 California Electrical Code (Title 24, Part 3); 2025 California Residential Code (Title 24, Part 2.5); 2025 California Energy Code (Title 24, Part 6)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — HVAC Permit

Handles hvac permits in Laguna Beach end-to-end. Scope: A furnace, air handler, condenser, or mini-split replaced or added, with its ducts and electrical.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a hvac permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. The Laguna Beach rules come first; the California checklist applies wherever Laguna does not override it.

---

## City Info

| | |
|---|---|
| Permit system | Tyler EnerGov Civic Access |
| Permit portal | https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home |
| Municipal code | https://ecode360.com/LA4953 |
| Fire agency | Laguna Beach Fire |
| Code edition | Title 14 Building & Housing · 2025 CBC/CRC |
| Code prefix | LBMC |

---

## Citywide Overlays

These apply to every permit in Laguna Beach before the rules below.

- **Wildfire — the whole city.** Treat every Laguna Beach parcel as inside a Fire Hazard Severity Zone / WUI area. Say so plainly: "assumed FHSZ based on citywide coverage; confirm the parcel on the City's adopted 2025 LRA map." Never tell an applicant a parcel is outside the zone without that map.
  Exterior work follows the California WUI Code (Title 24 Part 7; CBC Ch. 7A / CRC R337) as amended by LBMC Ch. 14.70, whose scope is set by LBMC §14.70.015. Class A roofing applies to any building in the City (LBMC §14.50.120, amending CBC §1505.1). Details: `../wildfire-wui/SKILL.md`.
- **Coastal zone — most of the city.** Check the parcel against the City's coastal zone map before naming a Planning route. Report a parcel that straddles the boundary as straddling. Coastal Development Permit analysis: `../coastal-development/SKILL.md`.

---

## MODE A — Builder / Homeowner Intake

### A1. Intake

Start by reading `../../references/homeowner-journey.md`; its opening exchange applies when this skill is selected directly. Read any files and answers the user already gave. For an idea-stage request with no files, briefly explain the help available and ask at most three opening questions: the address, the scope, and whether drawings exist.

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and then the California checklist using the user's answers. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach HVAC Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]

### Required uploads
[Generated per skill — plans, product data sheets, calculations, waste management plan if applicable, Laguna Beach Fire clearance if overlay-triggered, etc.]

### Inspection sequence
[Generated per skill — standard inspection milestones]
```

### A4. Filing

Hand the confirmed facts and filing theory to this plugin's included `laguna-permit-preparer` skill. It fills only verified official forms, uses a visible browser when portal filing is supported, and stops at `portal_ready` with an exact handoff when browser control is unavailable. It never submits without a fresh final approval and a confirmation receipt.

---

## MODE B — City Reviewer

### Procedure

1. Accept the submitted material (form data, PDF, photos, or pasted text)
2. Extract the key facts: project type, scope, materials, dimensions, parcel address, contractor
3. Walk the Laguna Beach rules, then the California checklist, in order
4. Produce output in the format below — hard fails first, then flags, then local flags, then a compliant bundle, then inspection deferrals

### Output format

```
PLAN CHECK — {address} ({permit})

❌ CORRECTIONS REQUIRED (N)
   [plan-check severity=fail items that are not satisfied]

⚠️ VERIFY BEFORE ISSUANCE (N)
   [plan-check severity=flag items needing documentation or clarification]

ℹ️ LOCAL FLAGS (N) — city discretion
   [LBMC-specific items — parcel overlays, city-specific checks]

✓ {N} checks PASS (expand for detail)

➡ {N} checks deferred to inspection

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides the California checklist below. Paths are relative to this file.

**Base skill:** `references/california-baseline.md`
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

---

### Decision Tree Router

| Project Type | Route |
|-------------|-------|
| **Before 2026-08-20** | The six-part test is not yet law. Use the prior five-part test in "Before 2026-08-20" below. Wall-mount-at-ground-level and the 3-ft path of travel do not apply yet. |
| **HVAC change-out** (same location, clearances, type) | Building-permit OTC may apply (hours below). OTC is the Building Division counter track, **not** a design-review exemption. If the equipment is exterior, still run the §7.25.130(C) test. Fail any part → Administrative Design Review; do not treat OTC as skipping that. |
| **Exterior HVAC or pool/spa equipment, residential or adjacent to residential** | Run the §7.25.130(C) six-part test below (five-part before 2026-08-20). Pass → Zone Clearance (no Design Review). Fail any part → Administrative Design Review per §25.05.040(B)(3)(a)(v) |
| **Exterior equipment on a lot in an environmentally sensitive area (ESA)** | Design Review per §25.05.040(B)(1). Zone Clearance is not available in an ESA unless a licensed professional determines, subject to peer review, that the work does not impact the ESA |
| **Commercial HVAC equipment** | Mechanical permit. The city may require a detailed acoustical study per §7.25.130(B) |

---

### §7.25.130(C) — Six-Part Objective Test (effective 2026-08-20)

**Authority:** LBMC §7.25.130, "Heating, venting, and air conditioning (HVAC) and pool/spa equipment—special provisions", as amended by the 2026 Efficiency Ordinance (adopted 2026-07-21, **effective 2026-08-20**). Source: the City source document (not included in this plugin) line 45.

Applies to permits for HVAC and pool/spa equipment **in or adjacent to residential areas**. Equipment that meets **all six** requirements is reviewed and approved **without Design Review** (§7.25.130(C)). Equipment that fails **any** requirement is reviewed per §25.05.040 Design Review (§7.25.130(D)).

| # | Requirement | Pass criteria | Evidence to check |
|---|---|---|---|
| 1 | Mounting | Equipment is ground-mounted, or wall-mounted at ground level | Site plan / elevation showing mounting location and height |
| 2 | Setbacks | Equipment is **not** within the required front or side yard setbacks | Site plan with the zone's required front and side yard setbacks dimensioned |
| 3 | Property-line clearance | Equipment maintains a **five-foot clearance from all property lines** | Dimensioned site plan |
| 4 | Decibel rating + two attenuation techniques | Manufacturer's specification sheet is submitted with the application and includes the decibel rating. Maximum **60 dB day / 50 dB night, measured at the property line**. **Two sound attenuation techniques shall be utilized.** Techniques must be used and maintained per the manufacturer's specifications for the life of the equipment | Manufacturer's spec sheet with dB rating; plans or notes identifying **two** named attenuation techniques. Code examples: physical enclosures such as fencing with insulation, internal sound compression blanket, shock absorption base (the list is "including, but not limited to") |
| 5 | City sound-level form | Completed city-provided form detailing how the project meets the maximum sound levels measured at the property line. Method of computation is ARI Standard 275, "Standard Application of Sound Rated Outdoor Unitary Equipment" (1984, as amended) | The completed form. **Form name pending** — see "Open item" below |
| 6 | Path of travel | Equipment **does not obstruct a 3-foot path of travel around any structure** | Site plan showing the clear path of travel around the structure |

**Scoring rule:** all six parts must pass. Any single failure routes the equipment to Administrative Design Review. Do not treat part 4 as satisfied by the decibel rating alone — **the two attenuation techniques are a separate, independent requirement of part 4**, and both must be named in the submittal.

**Open item — the part 5 form name is not yet known.** The Efficiency Ordinance says only "a form provided by the city." The city's 2026 application set has not yet been harvested. Do not invent a form name. Ask the applicant for the city's sound-level form by description, or direct them to the Community Development Department.

#### Reconciling "without Design Review" with the Zone Clearance routing

These are the same path, not two competing rules:

- §7.25.130(C) says compliant equipment is "reviewed and approved **without Design Review**."
- §25.05.040(B)(2)(v) lists "Mechanical equipment, including, but not limited to, air conditioners and pool/spa equipment, that meet the requirements of Section 7.25.130(c)" under **"Exempt from Design Review (Zone Clearance)"**, effective 2026-07-22 per the urgency DR Efficiency Ordinance.
- **Zone Clearance IS the exempt-from-design-review path.** It is the ministerial verification under LBMC §25.05.045 that a structure complies with the Zoning Code. Passing the six-part test means Zone Clearance plus the building/mechanical permit — no DRB hearing, no ADR, no notice period.
- §25.05.040(B)(3)(a)(v) lists mechanical equipment that **does not** meet §7.25.130(C) under Administrative Design Review. The hearing may be waived only through the enacted 15-working-day notice/comment procedure when no other entitlement is required and no hearing request is timely received.

One exception to the Zone Clearance path: §25.05.040(B)(2) states the zone clearance process shall not be used for any listed project in an environmentally sensitive area, unless a licensed professional has determined, subject to peer review, that the development does not impact the ESA. Those projects go to Design Review under §25.05.040(B)(1).

#### Before 2026-08-20

The prior §7.25.130(C) also exempted compliant equipment from Design Review, but its test had **five** requirements. Three differences: it covered "air conditioning units and pool and spa equipment" rather than HVAC generally; part (1) required equipment to be **ground-mounted** only, with no wall-mounted-at-ground-level option; and there was **no part (6)** — the 3-foot path of travel is new. Parts (2) through (5) are substantively unchanged, so the setback, 5-ft clearance, decibel/attenuation, and city-form checks apply the same way in both versions.

---

### §7.25.130(A) — Contractor Noise Acknowledgment (current law; unchanged by the 2026 amendment)

Permits for HVAC and pool/spa equipment in or adjacent to residential areas are issued **only after the installation contractor signs an acknowledgment** that the installation will meet the noise limits established in §7.25.040.

This is a permit-issuance condition, not a design-review trigger. It applies whether or not the equipment passes the six-part test. Flag a submittal that has no signed contractor acknowledgment.

### §7.25.130(B) — Commercial Acoustical Study (current law; unchanged by the 2026 amendment)

Applicants for mechanical permits for **commercial** HVAC equipment **may be required** to submit a detailed acoustical study demonstrating compliance with the §7.25.040 noise limits.

This is discretionary — the city decides. Do not treat a missing acoustical study on a commercial mechanical permit as an automatic failure. FLAG it as a possible city requirement and cite §7.25.130(B).

---

### OTC-Eligible HVAC Projects

Residential HVAC change-outs qualify for over-the-counter **building-permit** review if:
- **Same location** as existing unit
- **Same clearances** maintained
- **Same type** of equipment (not changing from gas to electric or vice versa)
- No exterior changes beyond the like-for-like equipment swap

OTC does not exempt exterior equipment from §7.25.130(C). A rooftop unit, a unit in a required setback, or any other change-out that fails a part of the test still goes to Administrative Design Review per §7.25.130(D) / §25.05.040(B)(3)(a)(v) — same as a new installation. A change-out that relocates the unit is not a change-out; run the test on the new location.

**OTC-eligible per the city reference OTC item 8** — residential HVAC change-outs in same location, clearances, access and type. Hours and the full OTC list: `../city-reference/SKILL.md` §"Permit Processing Tracks".

---

### Local Code Adoption

Ch. 14.54 adopts the California Mechanical Code with NO local amendments. All mechanical code requirements come from the state-level skill (`california-hvac`).

### Permit Exemptions

Portable mechanical appliances and portable ventilating equipment for a single dwelling are exempt from building permits (§14.50.022).

---

### Review Checklist — Laguna Beach HVAC

| ID | Check | Pass Criteria |
|---|---|---|
| LB-HVAC-1 | Design review route | Equipment passing all six parts of §7.25.130(C) routed to Zone Clearance (no Design Review); equipment failing any part routed to Administrative Design Review per §25.05.040(B)(3)(a)(v) |
| LB-HVAC-2 | Mounting | Ground-mounted, or wall-mounted at ground level (§7.25.130(C)(1)) |
| LB-HVAC-3 | Setbacks and clearance | Outside required front and side yard setbacks; 5-ft clearance from all property lines (§7.25.130(C)(2)–(3)) |
| LB-HVAC-4 | Decibel rating | Manufacturer's spec sheet submitted with dB rating; ≤60 dB day / ≤50 dB night at the property line (§7.25.130(C)(4)) |
| LB-HVAC-5 | Two sound attenuation techniques | Two techniques identified in the submittal, with a note that they are used and maintained per manufacturer's specifications for the life of the equipment (§7.25.130(C)(4)) |
| LB-HVAC-6 | City sound-level form | City-provided sound-level form completed, computed per ARI Standard 275 (1984, as amended) (§7.25.130(C)(5)). Form name pending city application-set harvest |
| LB-HVAC-7 | Path of travel | Equipment does not obstruct a 3-ft path of travel around any structure (§7.25.130(C)(6)) |
| LB-HVAC-8 | Contractor acknowledgment | Installation contractor's signed noise acknowledgment on file before permit issuance (§7.25.130(A)) |
| LB-HVAC-9 | Commercial acoustical study | For commercial HVAC mechanical permits, acoustical study submitted or flagged as possibly required (§7.25.130(B)) |
| LB-HVAC-10 | ESA screen | If the lot is in an environmentally sensitive area, Zone Clearance is unavailable absent a peer-reviewed licensed-professional determination; route to Design Review (§25.05.040(B)(2)) |

---

### Key Laguna Beach HVAC Facts

- **OTC eligible**: Yes — for same-location, same-type change-outs on the **building-permit** track. Exterior equipment still runs the §7.25.130(C) test; a fail is ADR, not OTC-as-exemption
- **Design Review**: governed by the §7.25.130(C) six-part objective test, **effective 2026-08-20**. Pass → Zone Clearance. Fail → Administrative Design Review (Director level) per §25.05.040(B)(3)(a)(v)
- **Noise limits**: 60 dB day / 50 dB night at the property line, computed per ARI Standard 275 (§7.25.130(C)(4)–(5))
- **Contractor acknowledgment** required before permit issuance (§7.25.130(A))
- **Local amendments**: Ch. 14.54 adopts CMC with NO local amendments
- **Permit exemption**: Portable mechanical appliances for single dwelling exempt (§14.50.022)

Note: The city's mechanical equipment handout covers landscape design guidelines for screening equipment, not mechanical code requirements.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Equipment location valid?** | ⚠️ **flag** | Bedroom/bathroom furnace or boiler installation follows a permitted CMC 904.2 configuration; proper access, passageway, platform per installation type | CMC 904.2, 304.4, 305.1 |
| 3 | **System properly sized?** | ❌ **fail** | Load calc per ACCA Manual J; equipment selected per Manual S; capacity within limits | Energy Code 150.0(h) |
| 4 | **Equipment efficiency meets minimum?** | ❌ **fail** | SEER2/HSPF2/AFUE meets federal minimums | Energy Code 110.1 |
| 5 | **Thermostat compliant?** | ⚠️ **flag** | Programmable setback thermostat (4 periods/24 hr); heat pump supplementary heater controls | Energy Code 110.2(c), 110.2(b) |
| 7 | **Combustion air adequate?** (gas systems only) | ⚠️ **flag** | Indoor air volume OR outdoor openings sized to BTU load | CMC 701.1-701.11 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 2 | **Clearance to combustibles OK?** | Per manufacturer's instructions; closet/alcove volume rule; floor installation uses a complete CMC 904.4 method or exception | CMC 303.1, 303.2, 904.4 |
| 6 | **Gas piping correct?** (gas systems only) | Shutoff valve within 6 ft, sediment trap, proper connectors, CSST bonding, pressure test | CPC 1212.6, 1212.9, 1213.3 |
| 8 | **Venting correct?** (gas systems only) | Type B/direct vent per listing; 5 ft above collar; proper termination height; clearance to combustibles | CMC 802.0-803.0 |
| 9 | **Ductwork compliant?** (ducted systems) | Sized per Manual D; sealed to Class A; insulated to R-6/R-8; leakage test | CMC 601.2, 603.9; Energy Code 150.2(b) |
| 10 | **Condenser installation correct?** (A/C or heat pump) | Equipment selected for the calculated load; pad/support and anchorage compliant; refrigerant piping supported | CMC 1105.1, 1105.2, 1109.6 |
| 11 | **Electrical disconnect provided?** | Disconnect in sight of equipment; dedicated circuit for furnace; 120V receptacle within 25 ft | CMC 301.4; CEC 422.10, 440.14 |
| 12 | **Condensate drain installed?** | Primary drain with 1/8 in./ft slope; overflow protection (pan, switch, or secondary drain) where damage could result | CMC 310.1, 310.2 |
| 13 | **Refrigerant charge verified?** (cooling system replacement) | Standard charge or weigh-in procedure; minimum 300 CFM/ton airflow | Energy Code 150.2(b)1F |
| 14 | **A/C electrical requirements met?** | Disconnect rating min 115% of nameplate rated-load current or branch-circuit selection current (440.12(A)(1)); disconnect within sight and readily accessible from equipment, not on access panels or obscuring nameplates (440.14); branch circuit conductor sizing per compressor nameplate (440.32, 440.33); motor controller disconnect accessible (440.13); A/C equipment anchored/secured including seismic (CEC 440.12, CMC 303.4). | CEC 440.12, 440.13, 440.14, 440.32, 440.33; CMC 303.4 |
| 15 | **Smoke and CO alarms compliant?** | Smoke alarms in all required locations (retrofit on permitted work); CO alarms where fuel appliances exist | CRC R310, R311 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/air-conditioning-refrigerant.md` — Air Conditioning & Refrigerant Piping
- `references/clearance-combustibles.md` — Clearance to Combustibles & Furnace Installation
- `references/combustion-air.md` — Combustion Air Requirements
- `references/ductwork.md` — Ductwork Requirements
- `references/electrical-disconnect.md` — Electrical Requirements for HVAC
- `references/energy-code-hvac.md` — Energy Code Requirements for HVAC
- `references/equipment-location.md` — Equipment Location & Access
- `references/gas-piping.md` — Gas Piping Requirements
- `references/smoke-co-alarms.md` — Smoke and Carbon Monoxide Alarm Requirements
- `references/venting-chimneys.md` — Gas Venting & Chimney Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
