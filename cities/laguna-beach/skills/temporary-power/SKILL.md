---
name: temporary-power
description: "Temporary Power permits in Laguna Beach, CA. A temporary power pole or generator serving a construction site. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions temporary power in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Electrical Code (Title 24, Part 3) — Articles 230, 240, 250, 310, 400, 408, 590; 2025 California Fire Code (Title 24, Part 9) — Sections 107, 313, 603, 1203; LBMC Ch. 7.25, 14.70, 15.01; 2025 CEC"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Temporary Power Permit

Handles temporary power permits in Laguna Beach end-to-end. Scope: A temporary power pole or generator serving a construction site.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a temporary power permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Temporary Power Permit

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

For cross-cutting city info (portal, contact, codes), see `../city-reference/SKILL.md`.

---

### Scope of Overrides

**No electrical-install overrides.** Per LBMC §14.68.010, Laguna Beach adopts the 2025 California Electrical Code by reference with **no local amendments to NEC Article 590**. Every state-skill checklist item for the electrical installation itself (GFCI, grounding/bonding, conductor sizing, panelboard, transfer switch, AIC, GEC/EGC, etc.) passes through unchanged.

**Overrides are non-electrical.** The deltas are city overlays that affect the *siting, scheduling, and fueling* of the temp pole or generator:

1. Construction-hours / noise ordinance (LBMC §7.25.080) — stricter than most CA cities.
2. Public Works Right-of-Way Permit if the pole/generator sits in the public ROW.
3. Caltrans encroachment if the site touches PCH (SR-1) or Laguna Canyon Road (SR-133).
4. Memorial Day–Labor Day downtown / Coast Highway construction moratorium.
5. VHFHSZ / WUI overlay (LBMC Ch. 14.70 + §15.01.030) — affects generator siting (spark arresters, defensible clearance).
6. LBMC §15.01.060 **deletes CFC §5707** — on-demand mobile fueling of site generators is NOT permitted via the standard CFC pathway.

---

### City-Specific Notes

| Item | Detail |
|------|--------|
| **Permit type** | Issued under the standard Electrical, Mechanical, and Plumbing Permit Application via Community Development Building Division (Tyler EnerGov CivicAccess portal — lagunabeachca-energovweb.tylerhost.net/apps/SelfService). No separate "temp power" handout exists — temp pole permits are recorded as ELEC permits. |
| **Utility** | Southern California Edison (SCE) — confirm with SCE before ordering temp pole. |
| **Electrical code** | 2025 California Electrical Code (CEC) adopted by reference; **no local amendments to Article 590** (§14.68.010). |
| **Fire code** | 2025 California Fire Code adopted with LB amendments in Ch. 15.01. §15.01.060 deletes CFC §5707 (mobile fueling). |
| **WUI code** | 2025 California WUI Code adopted (Ch. 14.70) with extensive local amendments. Citywide VHFHSZ coverage: `../city-reference/SKILL.md`. |
| **AHJ for fire** | LBFD (Laguna Beach Fire Department) — Laguna runs its own municipal fire department, NOT OCFA. |

---

### Construction Hours (LBMC §7.25.080)

Materially stricter than most California cities. Temporary-power generators and any compressor/tool fed from a temp pole are construction-noise sources and are bound by these hours:

| Day | Permitted Hours |
|-----|----------------|
| **Monday – Friday (weekdays)** | 7:30 AM – 6:00 PM |
| **Saturday** | **PROHIBITED** (weekend day per §7.25.080(B)) |
| **Sunday** | **PROHIBITED** |
| **Federal holidays** | **PROHIBITED** |

Verbatim from §7.25.080(A)–(B): "No person ... shall operate any tool, equipment or machine in a manner which produces loud noise ... on any weekday except between the hours of seven-thirty a.m. and six p.m. ... on any weekend day or any federal holiday."

**There is no Saturday construction window in Laguna Beach.** This is the city's correction to the common-California pattern. The the city reference table has been updated to match.

**Exceptions (§7.25.080(D)):**
- Emergency construction authorized in writing by the director of community development or building official
- Public works by/for a public agency (subject to specific findings)
- Construction that demonstrably complies with the noise limits in §7.25.040
- Sawdust Festival / Art-A-Fair / Laguna Art Museum — extended hours per ordinance

**Review impact:** If the application schedule shows ANY generator/compressor/tool use on a Saturday, Sunday, or federal holiday, FAIL unless an emergency-authorization letter or one of the §7.25.080(D) exceptions is documented.

---

### Public Works Right-of-Way Permit

| When required | Pass criteria |
|---------------|---------------|
| Temp power pole, generator, or any conductor staged within the public ROW (sidewalk, parkway, curb cut, alley) | Separate Public Works Permit issued by PW Department in addition to the building/electrical permit. Traffic Control Plan Review (per-page fee) if lane/sidewalk closure. Night work requires advance written justification approved by City Engineer. |

Very common on tight Laguna lots where the pole stages on the sidewalk/parkway. Fees: Public Works encroachment permit fees (Utility Street Excavation "Non-Excavation", Miscellaneous Encroachment Permit, Traffic Control Plan Review) are in the FY 2026-27 Master Fee Schedule, Public Works section (the City source document (not included in this plugin)). The chat fee tool does not carry them; quote the current MFS row, never an older figure.

---

### Caltrans Encroachment (SR-1 / SR-133)

| When required | Pass criteria |
|---------------|---------------|
| Site fronts Coast Highway (SR-1 / PCH) or Laguna Canyon Road (SR-133), and any temp installation (pole, generator, conductor) is inside the state highway ROW | Caltrans Encroachment Permit (dot.ca.gov/programs/traffic-operations/ep) required IN ADDITION to LB Public Works permit. |

---

### Summer Construction Moratorium (Memorial Day → Labor Day)

| When applicable | Pass criteria |
|-----------------|---------------|
| Project site is in the downtown / Coast Highway corridor and the temp-power install is scheduled between Memorial Day and Labor Day | Most non-emergency construction in the downtown/PCH corridor is prohibited during this window per city policy + Caltrans agreement. Reschedule temp-power install to fall outside the moratorium, or obtain explicit relief from PW/City Engineer. |

Source: LB Public Works Permits page; CA Coastal Commission addendum (Mar 2022).

**Review impact:** For downtown/PCH sites, FAIL temp-power installs scheduled May–September unless a moratorium-relief letter is attached.

---

### VHFHSZ / WUI Overlay — Temp Generator Siting

Laguna Beach lies predominantly in the Very High Fire Hazard Severity Zone (citywide coverage: `../city-reference/SKILL.md`). LBMC §15.01.030 amends CFC Chapter 3 to tie construction-site vegetation/fuel management to the city's Defensible Space Guideline and Fuel Modification Guidelines (Resolution 89.104). Chapter 14.70 (California WUI Code) is adopted with local amendments §§14.70.015–14.70.075. §15.01.025 adds the local **SPARK ARRESTER** definition.

| For a temp generator in a VHFHSZ lot, require: | Pass criteria |
|------------------------------------------------|---------------|
| **Spark arrester** on internal-combustion / gasoline / diesel temp generator exhaust | Confirm spark arrester per §15.01.025 definition. FAIL if absent. |
| **Defensible-space clearance** around the generator location | Vegetation cleared per Defensible Space Guideline (referenced by §15.01.030). |
| **On-site fuel storage** compliant with CFC Ch. 57 **without** the §5707 mobile-fueling pathway | See next section. |

**Interaction with §15.01.030:** The CFC Chapter 3 amendments fold VHFHSZ vegetation/fuel-mod controls into routine construction-site review. Plan-checkers should not separate "WUI review" from "temp generator review" for VHFHSZ lots — they apply together.

---

### Mobile-Fueling Deletion (LBMC §15.01.060 deletes CFC §5707)

The 2025 CFC §5707 allows on-demand mobile fueling of site equipment under defined conditions. **Laguna Beach deletes §5707 entirely.** Contractors cannot rely on a fuel tanker re-fueling a stationary site generator under the standard CFC pathway.

| Scenario | Result |
|----------|--------|
| Temp-power scope shows expected on-site tanker re-fueling of a site generator (any size) | **FAIL** — §5707 is deleted in Laguna Beach. Plans relying on mobile/tanker re-fueling will be rejected. |
| Plan shows fixed on-site fuel storage (e.g., integral day tank, sub-base tank, or approved CFC Ch. 57 storage) re-filled off-site, OR generator runs only on its integral tank for the duration of the permit | **PASS** (subject to underlying CFC Ch. 57 + VHFHSZ requirements above). |
| Contractor seeks mobile fueling under "alternative means and methods" | **FLAG** — requires AMM application to LBFD; do not approve at counter. |

**Plain-language note for builders:** In Laguna Beach, you have to either (a) bring in a generator with enough fuel on board to last the permit and re-fuel it at a gas station off-site, or (b) install permitted fixed fuel storage. You cannot have a fuel-truck visit the site to top up a temp generator the way you can in most CA cities.

---

### Review Checklist — Laguna Beach-Specific Items

These items are **additions** to the state checklist. None of the state CEC Article 590 items are overridden — all state checks still apply.

| # | City Check | Pass Criteria | Code Section |
|---|-----------|---------------|--------------|
| LB-TP-1 | **Electrical-install overrides** | NONE — state CEC Article 590 governs unchanged. Confirm no city-specific install rules were assumed in error. | LBMC §14.68.010 |
| LB-TP-2 | **Construction hours — weekends & holidays** | Generator/temp-power use is PROHIBITED on Saturdays, Sundays, AND federal holidays. There is no Saturday construction window in Laguna Beach. FAIL unless one of the §7.25.080(D) exceptions is documented (emergency authorization, public-works exception, demonstrable compliance with §7.25.040 noise limits, or art-org schedule). | LBMC §7.25.080(B) |
| LB-TP-3 | **Construction hours — weekday window** | Weekdays only: 7:30 AM – 6:00 PM. Earlier-start (e.g., 7:00 AM warm-up) FAILs. | LBMC §7.25.080(A) |
| LB-TP-4 | **Public Works ROW permit** | If the temp pole, generator, or any conductor sits in the public sidewalk/parkway/curb/alley, a separate Public Works Permit number is required in addition to the building/electrical permit. FAIL if missing. | LBMC Title 11; PW permit policy |
| LB-TP-5 | **Caltrans encroachment (SR-1 / SR-133)** | If the site fronts Coast Highway or Laguna Canyon Road and any temp installation touches the state highway ROW, a Caltrans Encroachment Permit is required. FAIL if missing. | CA Streets & Highways Code; Caltrans EP program |
| LB-TP-6 | **Summer moratorium (downtown / PCH)** | If the project is in the downtown / Coast Highway corridor AND the temp-power install is scheduled Memorial Day → Labor Day, require either a re-scheduled install date OR a moratorium-relief letter from PW / City Engineer. FAIL otherwise. | LB PW Permits policy; CCC Mar 2022 addendum |
| LB-TP-7 | **VHFHSZ spark arrester** | If the lot is in VHFHSZ, any combustion temp generator must have a spark arrester per LB definition. FAIL if absent or unspecified on plans. | LBMC §15.01.025, §15.01.030; Ch. 14.70 |
| LB-TP-8 | **VHFHSZ defensible-space clearance** | If in VHFHSZ, plans must show vegetation/fuel-mod clearance around the generator location per LB Defensible Space Guideline. FLAG if site plan does not depict clearance. | LBMC §15.01.030; Resolution 89.104 |
| LB-TP-9 | **Mobile fueling NOT permitted** | LBMC §15.01.060 deletes CFC §5707. Plans relying on tanker / on-demand mobile re-fueling of a site generator FAIL. Only integral-tank operation or approved fixed CFC Ch. 57 storage with off-site re-fueling acceptable. Mobile fueling via alternative-means-and-methods FLAG to LBFD. | LBMC §15.01.060 |
| LB-TP-10 | **LBFD is AHJ for fire** | Where state-skill items reference "fire AHJ" (e.g., CFC 313 clearances, fuel storage, signage, fire access), the AHJ is the Laguna Beach Fire Department — not OCFA. | LB municipal organization |

---

### Open Verification Items (post-skill TODO)

1. **§7.25.080 verbatim** — RESOLVED 2026-05-12 via Parallel Extract. Weekdays 7:30 AM–6 PM only; weekends and federal holidays prohibited (no Saturday window). See the City source document (not included in this plugin).
2. **Summer moratorium boundaries** — recon cites the moratorium policy but does not enumerate the exact downtown / Coast Highway parcels covered. Pull the current PW moratorium memo before producing a corrections letter that turns on parcel location.
3. **CDP interaction** — recon concludes no CDP is required for a typical temp power pole (utility, removable, not "development" in coastal-zone meaning). Re-confirm for any commercial/multi-unit job where the temp installation duration exceeds the construction window.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 2 | **Equipment listed?** | ❌ **fail** | Generator and all distribution equipment listed by NRTL (UL, etc.); installed per manufacturer instructions | CEC 110.3(B) |
| 3 | **Load calculations provided?** | ❌ **fail** | Article 220 load calc; continuous load adjustments (125%); largest motor load; generator kW sufficient for load | CEC 220, 590.4(B) |
| 4 | **Single line diagram complete?** | ❌ **fail** | Shows transfer of loads; feeder/wiring methods; equipment ratings (V, A, AIC); grounding details; breakers/fuses; panelboard; disconnects | CEC 590.4 |
| 5 | **Conductor sizing correct?** | ❌ **fail** | Conductors sized per Table 310.16 (75 deg C column for THHN in conduit); ambient temperature correction applied for above-ground runs | CEC Table 310.16, 310.15, 400.5 |
| 7 | **Overcurrent protection correct?** | ❌ **fail** | Breakers sized for load; listed for panel; back-fed breakers secured; service OCPDs current-limiting if >10kA AIC | CEC 240.4, 408.36(D), 590.8 |
| 9 | **Grounding electrode system?** | ❌ **fail** | For power poles: full GES per 250.50; for portable generators on trailer with tires: ground rod NOT required per 250.34; for separately derived systems: GES per 250.30 | CEC 250.34, 250.50 |
| 10 | **GEC and EGC sizing correct?** | ❌ **fail** | GEC per Table 250.66; EGC per Table 250.122; bonding jumpers per Table 250.102(C)(1) | CEC 250.66, 250.122 |
| 12 | **Transfer switch compliant?** | ❌ **fail** | Listed by UL; voltage, amperage, poles specified; automatic or manual noted; unused loads disconnected; back-fed breakers have hold-down kits | Generator-specific |
| 13 | **AIC rating adequate?** | ❌ **fail** | Available fault current from utility and generator shown; all equipment rated for available fault current | CEC 590.8(B) |
| 20 | **Air quality approval?** | ⚠️ **flag** | SCAQMD approval required (Southern CA); generators >50 BHP or gas turbines >2,975,000 BTU/hr need Permit to Construct | SCAQMD Rules |
| 22 | **Site plan complete?** | ⚠️ **flag** | Property lines, buildings, distances, north arrow, streets, driveways, generator/pole location, conduit routing (above/below grade), fire access, screening | Plan review |

### Checklist rows to place

These state rows have no current stage tag. For each one, decide from its text whether it is a plan-check item (and whether a miss is a correction or a flag) or an inspection item.

| # | Check | What to verify | Code |
|---|---|---|---|
| 1 | **Purpose and duration valid?** | Installation remains within the CEC 590.3 purpose/duration that applies: construction work, 90-day decorative/event use, emergency/test use, or an allowed experiment/development use. Any local permit condition is separately sourced. | CEC 590.3 |
| 14 | **Temporary fire permit and fueled-equipment scope?** | If CFC 105 requires a permit, apply CFC 107. Portable fueled equipment is not stored, operated or repaired inside a building unless a stated CFC 313.1 exception applies. | CFC 107, 313.1 |
| 15 | **Fuel/fire review sourced?** | Fuel type, capacity and location are identified and the applicable current CFC/local provisions are cited; no invented 313 tank/setback/containment table is used. | Project-specific CFC/local source |
| 17 | **Required identification complete?** | CEC-required directories/identification are complete; any generator/fuel/emergency sign has an applicable current source. | CEC 408.4; source-specific |
| 18 | **Local screening/fencing source?** | Apply screening or fencing only from a current named jurisdiction/utility/permit source with exact locator and scope. | Local/utility source |
| 19 | **Exhaust/ventilation path?** | CFC 313.1 indoor fueled-equipment prohibition/exceptions are resolved; any allowed indoor or required-system installation follows its approved design, listing and applicable CFC 1203/NFPA route. | CFC 313.1, 1203; approved design/listing |
| 30 | **Fire/electrical code routes complete?** | CEC Article 590 governs temporary wiring; CFC 603 routes CFC/CBC-required electrical equipment to the CEC; CFC 107/313.1/1203 apply only in their stated scopes. CFC 605 is not a temporary-power section. | CEC 590; CFC 107, 313.1, 603, 1203 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 6 | **Wiring methods compliant?** | Cables rated for hard usage or extra-hard usage per Table 400.4; not on floor/ground; supported and protected from damage | CEC 590.4(B), (C), (H), (J), Table 400.4 |
| 8 | **GFCI protection provided?** | All 125V, 1-phase, 15/20/30A receptacles have GFCI; generator receptacles on 15 kW or less generators have GFCI; all temporary receptacles GFCI-protected | CEC 590.6 |
| 11 | **Neutral/EGC separation correct?** | Service panels: bonded; subpanels: neutrals NOT bonded; EGCs and neutrals on separate terminals; back-fed panels: "neutrals isolated from grounding connections" | CEC 250.24, 408.41 |
| 16 | **Physical protection provided where required?** | Temporary conductors are protected from damage; any vehicle-impact barrier is tied to an applicable project-specific provision and design. | CEC 590.4(H); applicable CFC/design source |
| 21 | **Utility notification?** | Serving utility (SCE, PG&E, etc.) notified and approved prior to installation | Utility requirements |
| 23 | **Panelboard requirements met?** | Vertical installation; dead-front cover; circuit directory; proper torque; wire bending space per Table 312.6(A); fill limits (40% splices, 75% total); cables secured to cabinet (312.5(C)); not face-up (408.43 Ex.2) | CEC 240.33, 408.4, 408.38, 312.5(C), 312.6, 312.7, 312.8, 408.43 |
| 24 | **Panel location restrictions met?** | Not exposed to physical damage (240.24(C)); not near ignitable materials (240.24(D)); not in bathrooms (240.24(E)); not over stairway steps (240.24(F)). Breaker ON/OFF position correct (up = ON for vertical, 240.81). | CEC 240.24(C-F), 240.81 |
| 25 | **Wire bending space adequate?** | Wire bending space at terminals per Table 312.6(A): #14-10 = not specified; #8-6 = 1-1/2 in.; #4-3 = 2 in.; #2 = 2-1/2 in.; #1 = 3 in.; #1/0-2/0 = 3-1/2 in.; #3/0-4/0 = 4 in. (1 wire per terminal). | CEC Table 312.6(A) |
| 26 | **One wire per terminal?** | No double-tapped breakers unless terminal is listed for two conductors (110.14(A)). Neutrals and EGCs on separate terminals (408.41). | CEC 110.14(A), 408.41 |
| 27 | **Neutral identification and continuity?** | White or gray factory finish for #6 and smaller; white/gray tape for #4 and larger (200.6). No OCPD in series with neutral (240.22). Neutral pigtailed in MWBCs -- continuity must not depend on connected device (300.13(B)). | CEC 200.6, 240.22, 300.13(B) |
| 28 | **MWBC requirements met?** | MWBCs on opposite legs (208/240V between hots); simultaneous disconnect via 2-pole breaker or handle ties (210.4(B), 240.15(B)(1)). | CEC 210.4(A), 210.4(B), 240.15(B)(1) |
| 29 | **Subpanel bonding correct?** | Feeder-supplied panels: neutrals NOT bonded to ground; bonding jumper removed; feeder origin label required (408.4(B)). | CEC 250.24(A)(5), 408.4(B) |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/conductors-wiring-methods.md` — Conductors, Wiring Methods, and Neutral/EGC Identification
- `references/fire-code-temporary-power.md` — California Fire-Code Routing for Temporary Power
- `references/generator-requirements.md` — Temporary Generator Requirements
- `references/grounding-bonding-250.md` — Grounding Electrode System, GECs, EGCs, and Bonding
- `references/panelboard-overcurrent-240-408.md` — Panelboard, Overcurrent Protection, and Enclosure Requirements
- `references/temporary-installations-590.md` — CEC Article 590 — Temporary Installations
- `references/temporary-power-pole.md` — Temporary Power Pole Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
