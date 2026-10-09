# California Baseline — New Single-Family Home

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Single-Family Residential Code Decision Engine

This skill contains the California state-level code requirements for single-family residential construction (one- and two-family dwellings, townhouses) extracted from the 2025 Title 24 corpus. It covers the California Residential Code (CRC), California Building Code (CBC) for seismic/lateral, California Electrical Code (CEC), California Mechanical Code (CMC), California Plumbing Code (CPC), California Energy Code, and California Green Building Standards Code (CALGreen).

**What this covers**: State building code — the requirements that apply to every single-family residential project in California regardless of city.

**What this does NOT cover**: City/county-specific ordinances, local zoning standards (setbacks, lot coverage, FAR, height limits), federal requirements, or project-specific engineering calculations. ADU-specific requirements are in the separate `california-adu` skill.

### How to Use This Skill

When answering a single-family residential question, follow the 3-step decision tree below. Each step tells you which reference files to load. Load only what you need — most questions require 3-6 reference files, not all 17.

After loading references, check the **Quick-Reference Thresholds** table below for the key numbers that come up in almost every review.

---

### Decision Tree Router

#### STEP 0 — Wildfire / WUI Pre-Check

For Laguna Beach the wildfire overlay is set citywide: use the `wildfire: 'all'` row below, and the `wildfire-wui` skill in this plugin for the Chapter 7A / WUI Code details.

| Overlay status                  | What to do                                                                                                                                                                                                                |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not loaded (no FHSZ in city)    | Before skipping the overlay, confirm that WUI 101.3.1 does not apply through a State Responsibility Area or locally designated WUI area either; lack of an FHSZ overlay alone is not dispositive. |
| Loaded — `wildfire: 'partial'`  | City has some FHSZ parcels but not the whole jurisdiction. Surface Part 7 WUI findings **conditionally** with a disclaimer pointing applicants to the CalFire FHSZ viewer (osfm.fire.ca.gov). Do not fail on WUI grounds without parcel and WUI 101.3.1 applicability confirmation. |
| Loaded — `wildfire: 'all'`      | Entire or substantial majority of the city is FHSZ. Apply Part 7 WUI findings, prefaced with a brief "assumed FHSZ based on city coverage; confirm via osfm.fire.ca.gov — if outside, verify any other WUI 101.3.1 basis before omitting the findings" disclaimer. |

When the overlay is loaded, follow `../../wildfire-wui/SKILL.md` Steps 1–3 for the specific component checks (roof assemblies, eaves/vents, walls/windows/doors/decks, defensible space, site access) and fold those findings into the SFR review output alongside the standard checks below.

#### STEP 1: Identify the Discipline

What discipline is the question about? Load the relevant reference files.

| Discipline | Load These References |
|-----------|----------------------|
| **Fire-resistant construction** (exterior walls, garage separation, penetrations) | `fire-resistant-construction.md` |
| **Fire protection systems** (sprinklers, smoke alarms, CO alarms) | `fire-protection-systems.md` |
| **Egress** (doors, stairs, emergency escape, handrails, guards) | `egress.md` |
| **Habitability** (room sizes, ceiling height, light, ventilation, glazing) | `egress.md` |
| **Structural design criteria** (loads, seismic category, wind, deflection) | `structural-design-criteria.md` |
| **Structural project-evidence coordination** (proprietary shear walls, sealed calculations, caissons, concrete design strength) | `structural-project-evidence-playbook.md` + `structural-design-criteria.md`; add `structural-lateral-seismic.md`, `foundations.md`, or the submitted geotechnical basis only as the feature requires |
| **Foundations** (footings, foundation walls, anchor bolts, drainage, slabs) | `foundations.md` |
| **Lateral / seismic** (wall bracing, hold-downs, cripple walls, diaphragms) | `structural-lateral-seismic.md` |
| **Wall framing** (studs, headers, top plates, fireblocking, bracing) | `wall-framing.md` |
| **Floor framing** (joists, sheathing, slab-on-grade, decks) | `floor-framing.md` |
| **Roof / ceiling** (rafters, ceiling joists, ridge, ventilation, covering) | `roof-ceiling.md` |
| **Mechanical / HVAC** (ventilation, exhaust, ducts, combustion air, dryer) | `mechanical-hvac.md` |
| **Plumbing** (fixtures, water supply, drainage, vents, water heater) | `plumbing.md` |
| **Electrical** (service, circuits, GFCI/AFCI, receptacles, EV charging) | `electrical.md` |
| **Energy** (insulation, fenestration, solar PV, HVAC efficiency, HERS) | `energy.md` |
| **Residential lighting controls** (garage automatic-off, dimming, independent controls, outdoor controls) | `lighting-controls-playbook.md`; add `energy.md` only for broader energy-document coordination |
| **Green building / CALGreen** (water conservation, waste diversion, VOC, EV) | `calgreen-mandatory.md` |

#### STEP 2: Add Related Files for Common Overlaps

Many questions span multiple disciplines. Load additional files based on these common overlaps.

| If the question involves... | Also load... |
|----------------------------|-------------|
| **Garage** (any aspect) | `fire-resistant-construction.md` (R302.6 separation) + `fire-protection-systems.md` (sprinklers) + `electrical.md` (GFCI) |
| **New construction** (whole-house) | `fire-protection-systems.md` (sprinklers, smoke/CO) + `energy.md` (PV mandate) + `calgreen-mandatory.md` (EV, water) |
| **Stairs / stairways** | `egress.md` (geometry, handrails, guards) + `wall-framing.md` (under-stair framing) |
| **Seismic / lateral** | `structural-lateral-seismic.md` + `structural-design-criteria.md` (SDC) + `foundations.md` (anchor bolts) |
| **Proprietary or engineered structural system** | `structural-project-evidence-playbook.md` + `structural-design-criteria.md`; add `structural-lateral-seismic.md`, `foundations.md`, or the submitted geotechnical basis only as the feature requires |
| **Framing** (general) | `wall-framing.md` + `floor-framing.md` + `roof-ceiling.md` |
| **Foundation to framing connection** | `foundations.md` (anchor bolts) + `structural-lateral-seismic.md` (plate washers, hold-downs) |
| **Water heater** | `plumbing.md` (T&P, strapping) + `mechanical-hvac.md` (combustion air) + `energy.md` (heat pump requirement) |
| **Kitchen / bathroom** | `plumbing.md` (fixtures) + `electrical.md` (GFCI, dedicated circuits) + `mechanical-hvac.md` (exhaust) |
| **New or altered residential lighting** | `lighting-controls-playbook.md`; add `energy.md` only for broader energy-document coordination |
| **Exterior walls** | `fire-resistant-construction.md` (fire rating) + `wall-framing.md` (framing) + `energy.md` (insulation) |
| **Roof** | `roof-ceiling.md` (framing, covering) + `energy.md` (cool roof, insulation) |
| **Deck** | `floor-framing.md` (R507 deck requirements) + `egress.md` (guards) |
| **EV charging** | `electrical.md` (CRC R338) + `calgreen-mandatory.md` (4.106.4) |

#### STEP 3: Check Situational Modifiers

Does any of the following apply? Load additional references.

| Situation | Load These References |
|-----------|----------------------|
| **Townhouse** (common wall with another unit) | `fire-resistant-construction.md` (R302.2 separation walls) |
| **Two-family dwelling** (duplex) | `fire-resistant-construction.md` (R302.3 separation) |
| **Attached garage** | `fire-resistant-construction.md` (R302.6 garage separation — #1 correction item) |
| **SDC D0, D1, or D2** (most of California) | `structural-lateral-seismic.md`, `foundations.md` |
| **WUI / fire hazard zone** | `roof-ceiling.md` (R806.1.1 WUI vents, R902 fire classification) |
| **Re-roof** | `roof-ceiling.md` (R902.1.2 Class C minimum outside FHSZ/WUI; R902.1.1 and WUI 504.2 Class A in applicable Part 7 areas) |
| **Addition / alteration** | `energy.md` (CEnC 150.2 addition/alteration triggers) |

---

### Quick-Reference Thresholds

These numbers come up in almost every single-family residential review. Check here first before loading a reference file.

| Threshold | Value | Reference File |
|-----------|-------|----------------|
| **CRC scope** | 1- and 2-family dwellings, townhouses ≤3 stories above grade | `structural-design-criteria.md` |
| **Sprinklers required** | New townhouses and 1- and 2-family dwellings, subject to R309.1/R309.2 exceptions | `fire-protection-systems.md` |
| **Garage separation — wall** | 1/2" gypsum (garage side), 5/8" Type X (if below habitable) | `fire-resistant-construction.md` |
| **Garage separation — door** | 1-3/8" solid wood or 20-min rated | `fire-resistant-construction.md` |
| **Smoke alarms** | Each sleeping room + outside each sleeping area + each story, with additional R310.3 locations/rules | `fire-protection-systems.md` |
| **CO alarms** | Outside each sleeping area + each occupiable level, plus bedroom trigger in R311.3 | `fire-protection-systems.md` |
| **Egress door clear width** | 32 in min at the designated required egress door | `egress.md` |
| **Stair rise / run** | 7-3/4 in max rise / 10 in min run | `egress.md` |
| **Emergency escape opening** | 5.7 sf min (5.0 sf at grade), sill ≤44 in, where R319.1 requires an opening | `egress.md` |
| **Guard height** | 42 in at triggered walking surfaces; 34 in at triggered open stair sides | `egress.md` |
| **Handrail height** | 34-38 in above stair nosing | `egress.md` |
| **Min habitable room** | 70 sf where R312.1 applies; evaluate kitchen and other stated exceptions | `egress.md` |
| **Ceiling height** | 7 ft habitable and hallways; 6 ft 8 in baths/toilet rooms/laundry | `egress.md` |
| **Light / ventilation** | 8% glazing / 4% openable baseline, subject to R325.1 alternatives and exceptions | `egress.md` |
| **Live load — floors** | 40 psf (30 psf sleeping rooms) | `structural-design-criteria.md` |
| **Live load — roof** | 20 psf (or per snow load) | `structural-design-criteria.md` |
| **Footing depth** | 12 in min below undisturbed ground | `foundations.md` |
| **Anchor bolts** | 1/2 in dia, 6 ft o.c., within 12 in of ends | `foundations.md` |
| **Plate washers (SDC D)** | 3 in x 3 in x 0.229 in at each bolt | `foundations.md` |
| **Slab-on-grade thickness** | 3.5 in min | `foundations.md` |
| **Vapor retarder under slab** | 6-mil polyethylene | `foundations.md` |
| **Stud spacing (bearing)** | Determine size/spacing from Table R602.3(5) by unsupported height and supported roof/floor loads, including footnotes and R602.3.1 exceptions | `wall-framing.md` |
| **Roof ventilation ratio** | 1/150 baseline; 1/300 only when all R806.2 exception conditions are met, including the applicable CZ 6-8 vapor retarder and 40-50% upper/balance-lower vent distribution | `roof-ceiling.md` |
| **Attic access** | 22 in x 30 in min, 30 in clearance | `roof-ceiling.md` |
| **Service size** | 100A, 3-wire minimum for a one-family dwelling and not less than calculated load | `electrical.md` |
| **GFCI required** | Apply complete CEC 210.8 scope and exceptions | `electrical.md` |
| **AFCI required** | 120V single-phase 10A/15A/20A circuits in complete CEC 210.12(B) location scope | `electrical.md` |
| **EV charging** | CALGreen 4.106.4 infrastructure for in-scope new attached private garages, subject to exceptions | `electrical.md` |
| **Kitchen exhaust** | Current CEnC 150.0(o)1G path: Table 150.0-G hood, 300 CFM other demand control, or qualifying 5-ACH continuous | `mechanical-hvac.md` |
| **Bathroom exhaust** | 50 CFM demand-controlled or 20 CFM continuous | `mechanical-hvac.md` |
| **Dryer vent max length** | 14 ft default including two 90° elbows; subtract 2 ft per additional 90°, subject to approved alternatives | `mechanical-hvac.md` |
| **Toilets** | 1.28 GPF max | `calgreen-mandatory.md` |
| **Showerheads** | 1.8 GPM max | `calgreen-mandatory.md` |
| **Waste diversion** | 65% minimum | `calgreen-mandatory.md` |
| **Solar PV** | Required for new single-family buildings where §150.1(c)14 applies, subject to that section's exceptions; size varies by CFA/climate zone | `energy.md` |
| **Duct leakage** | 5% postconstruction; rough-in 5% with air handler or 4% without | `energy.md` |

---

### Key Principles

1. **CRC scope and engineered design**: The CRC governs one- and two-family dwellings and townhouses within R101.2. The CBC applies where the CRC invokes it and where a permitted or required engineered design follows the CBC; CBC 1613 is one alternate seismic-design-category route under CRC R301.2.2.1.

2. **Sprinkler trigger**: New townhouses and one- and two-family dwellings require an automatic sprinkler system under CRC R309.1 or R309.2, subject to their stated exceptions, and designed and installed under Section R309 or NFPA 13D as those sections permit. Sprinkler installation can affect other code paths where those provisions expressly say so.

3. **Garage separation**: CRC R302.5 governs garage opening protection, ducts, and penetrations; CRC R302.6 and Table R302.6 govern the separation materials at walls, rooms above, and supporting construction.

4. **California is seismic country**: Most of California is SDC D0, D1, or D2. This triggers enhanced bracing lengths, plate washers at anchor bolts, cripple wall bracing, and hold-down requirements throughout the CRC prescriptive tables.

5. **Energy code is California-specific**: The California Energy Code (Part 6) requires solar PV for new single-family buildings where §150.1(c)14 applies, subject to its exceptions. It also establishes the water-heating paths in 150.1(c)(8) and applicable field verification and diagnostic testing—performed by an ECC-Rater where required—for duct sealing under 150.0(m)(11) and QII under 150.1(c)(1)(E), Table 150.1-A, and Reference Residential Appendix 3.5.

6. **Prescriptive path covers most projects**: The CRC provides prescriptive span tables, bracing amounts, and connection details for conventional wood-frame construction. Projects that exceed prescriptive limits require engineered design per CBC.
