---
description: "Reroof permits in Huntington Beach, CA. Works in two modes: (A) BUILDER/HOMEOWNER — walks through project scoping, checks compliance against state code + Huntington Beach local amendments, produces an Accela-ready submission guide; (B) CITY REVIEWER — runs the plan-check checklist against a submittal and produces tight corrections output. Inspection items deferred (not listed as corrections). Use when the user mentions reroof in Huntington Beach."
version: "1.0"
source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC, Part 4 CMC, Part 5 CPC, Part 6 Energy, Part 11 CALGreen)"
authority: "California Building Standards Commission"
law_as_of: "2025"
---

# Huntington Beach — Reroof Permit

Handles reroof permits in Huntington Beach end-to-end.

**First thing in every conversation:** ask which mode the user is in.

> "Are you (A) planning to file a reroof permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **Builder / Homeowner Intake** below
- Mode B → walk **City Reviewer Checklist** below

Both modes share the same rules. The difference is direction of travel — builder scopes forward, reviewer checks backward.

---

## City Info

| | |
|---|---|
| Permit portal | https://engage.huntingtonbeachca.gov/CitizenAccess/Default.aspx |
| Municipal code | https://ecode360.com/HU4937 |
| Building & Safety | (714) 536-5271 |
| Fire agency | HBFD |
| Code edition | 2025 California Building Standards Code · Local Amendments per HBMC Title 17 |
| Code prefix | HBMC |

---

## Key Huntington Beach deltas vs state baseline

City-specific checks layered on top of state code. Each is tagged `[HBMC]` in the checklist below.

- **HB-1** Class B minimum — explicit confirmation — **HARD FAIL**. HBMC Ch. 17.04 — Class B minimum required every reroof regardless of size; product data sheet with ASTM E108 or UL 790 label verified at submittal. Primary HB delta.
- **HB-2** 50% area threshold — whole-roof upgrade — **HARD FAIL**. HBMC Ch. 17.04 — if >50% of total roof area replaced within 12-month window, entire roof must upgrade to Class B. Verified from roof area calculations on plans.
- **HB-3** Coastal Zone CDP check — **flag**. Coastal Act §30610 — parcel coastal zone status must be verified. Like-for-like reroof typically exempt. Substantial roof type change (flat→pitched, adding dormers) requires Planning Division consult. HB issues own CDPs under certified LCP.
- **HB-4** Methane / Oil Production Overlay check — **flag**. HBMC Ch. 17.04; CBC Ch. 55 local addition — parcel overlay status must be verified. Standard reroof (no excavation, no structural) typically exempt. Scope expansion (new deck, grading, demo) triggers HBFD review.
- **HB-5** Solar panel coordination — **flag**. If existing solar panels must be removed and reinstalled, a separate solar/electrical permit is required. Reviewer scopes; notes applicant if missing.
- **HB-8** Open violations check — **flag**. Building dept policy — reviewer runs permit/violation history on parcel before issuance. Any unpermitted prior work must be resolved, legalized, or abated before final.
- **1** Class B minimum — explicit confirmation — **flag**
- **2** 50% area threshold — entire roof upgrade — **flag**
- **3** Coastal zone — CDP check — **flag**
- **4** Methane district — scope change check — **flag**
- **5** Solar panel coordination — **flag**
- **6** Permit type — Re-Roof permit in Accela — **flag**
- **7** Fire agency — HBFD, not OCFA — **flag**
- **8** Open violations check — **flag**
- **HB-6** Accela permit category — Re-roof — info. Procedural: submit as Residential/Commercial Re-roof in Accela, not general combo. No code rule; portal routing only.
- **HB-7** Fire agency is HBFD (not OCFA) — info. Informational: all fire-related review routes to HBFD (714) 536-5411. OCFA has no jurisdiction in HB.

---

## MODE A — Builder / Homeowner Intake

### A1. Intake

Collect project information to cover every plan-check item below. Ask questions naturally — don't interrogate. Start with project basics (address, scope, key product selections) then gather the rest as needed. The **Plan-Check Checklist** below enumerates exactly what must be satisfied at submittal; use it as your mental checklist for what to ask.

### A2. Pre-submission Compliance Check

Once you have enough info, walk the Plan-Check Checklist below using the user's answers. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what additional info or documentation they need to gather
- **PASS** → confirm, move on

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide:

```
## Ready to Submit — Huntington Beach Reroof Permit

**Portal:** https://engage.huntingtonbeachca.gov/CitizenAccess/Default.aspx
**Typical issuance:** same-day OTC if documents complete and no overlay triggers

### Required uploads
[Generated per skill — product data sheets, plan sketches, waste management plan if applicable, HBFD clearance if overlay-triggered, etc.]

### Inspection sequence
[Generated per skill — standard inspection milestones]
```

### A4. Optional — portal automation

If browser tools (`mcp__claude-in-chrome__*`) are available, offer to open the portal and walk the user through the form. Never auto-submit — always pause for user confirmation at key moments.

---

## MODE B — City Reviewer

### Procedure

1. Accept submitted form data (JSON, PDF, photos, or pasted text)
2. Extract key fields: project type, scope, materials, dimensions, parcel address, contractor
3. Walk the Plan-Check Checklist below in order
4. Produce output in the format below — hard fails first, then flags, then a compliant bundle, then inspection deferrals

### Output format

```
PLAN CHECK — {address} ({permit})

❌ CORRECTIONS REQUIRED (N)
   [plan-check severity=fail items that are not satisfied]

⚠️ VERIFY BEFORE ISSUANCE (N)
   [plan-check severity=flag items needing documentation or clarification]

ℹ️ LOCAL FLAGS (N) — city discretion
   [HBMC-specific flag items — parcel overlays, city-specific checks]

✓ {N} checks PASS (expand for detail)

➡ {N} checks deferred to inspection

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time. Severity drives reviewer-mode output.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope: Tear-off or Overlay?** `[HBMC]` | ❌ **fail** | If overlay: existing roof must have <=1 layer already (max 2 total). Cannot overlay over slate, clay, cement, or asbestos-cement tile. Cannot overlay if existing is water-soaked or deteriorated. If tear-off: all layers removed to deck. | CBC 1512.2, 1512.3; CRC R908.3 |
| 2 | **Fire Classification** `[HBMC]` | ❌ **fail** | All new roofing in California must be fire-retardant rated at minimum Class C (CBC 1505.1.2). If >50% of roof replaced in one year, entire roof must be minimum Class C. In Very High Fire Hazard Severity Zones (VHFHSZ), Class A is mandatory regardless of construction type. Materials must bear testing agency labels (ASTM E108 or UL 790). Minimum per construction type: Type IA/IB/IIA/IV/VA = Class B; Type IIB/IIIB/VB = Class C (Table 1505.1). | CBC 1505.1, 1505.1.2, Table 1505.1; CRC R902.1, R902.1.2 |
| 3 | **Wind Speed Zone** | ⚠️ **flag** | Determine wind speed zone for project location (typically 110-115 mph for most of California per ASCE 7-22/CBC 1609). Wind speed zone affects underlayment requirements and wind-resistance labeling. Verify roofing material wind resistance labeling per ASTM D7158 or ASTM D3161 (CRC R905.2.4/CBC 1504.2). | CBC 1609, 1504.2; CRC R905.2.4 |
| 4 | **Material-Slope Compatibility** | ❌ **fail** | Verify selected material is allowed at the stated roof slope. Each material has a minimum slope. Low slopes require additional underlayment. | CBC 1507.2-1507.13; CRC R905.2-R905.8 |
| 5 | **Tile Weight / Structural** | ⚠️ **flag** | If clay or concrete tile: verify weight (psf) is provided. If weight exceeds original roofing by >3 psf or original framing was not designed for tile, structural analysis may be required. Permit valid for materials <=6 lbs/SF on standard plans. | CBC 1607.13; CRC R301.1 |
| 6 | **ICC-ESR Product Approval** | ⚠️ **flag** | If tile: ICC-ES evaluation report number should be provided. This verifies the product meets code. Note the number -- validation is city staff's responsibility. | CBC 1507.3; CRC R905.3 |
| 11 | **Cool Roof Compliance** | ❌ **fail** | Low-slope (<=2:12): SRI >=75. Steep-slope (>2:12): SRI >=16. Commercial low-slope: aged reflectance >=0.63, emittance >=0.75. Residential steep-slope: aged reflectance >=0.20, emittance >=0.75. Heavy roofs >=25 lb/ft2 exempt. BIPV/solar thermal exempt. | Energy Code 150.2(b)1I |
| 16 | **Waste Diversion** | ❌ **fail** | Tear-off projects: 65% minimum nonhazardous waste diversion from landfill (CALGreen 5.408). Waste management plan required. | CALGreen 5.408 |
| 17 | **Contractor Licensing** | ❌ **fail** | C-39 (Roofing) or B (General Building) license required. C-43 (Sheet Metal) for metal roofing. Workers' compensation insurance required. | B&P Code 7028 |
| HB-1 | **Class B minimum — explicit confirmation** `[HBMC]` | ❌ **fail** | HBMC Ch. 17.04 — Class B minimum required every reroof regardless of size; product data sheet with ASTM E108 or UL 790 label verified at submittal. Primary HB delta. |  |
| HB-2 | **50% area threshold — whole-roof upgrade** `[HBMC]` | ❌ **fail** | HBMC Ch. 17.04 — if >50% of total roof area replaced within 12-month window, entire roof must upgrade to Class B. Verified from roof area calculations on plans. |  |
| HB-3 | **Coastal Zone CDP check** `[HBMC]` | ⚠️ **flag** | Coastal Act §30610 — parcel coastal zone status must be verified. Like-for-like reroof typically exempt. Substantial roof type change (flat→pitched, adding dormers) requires Planning Division consult. HB issues own CDPs under certified LCP. |  |
| HB-4 | **Methane / Oil Production Overlay check** `[HBMC]` | ⚠️ **flag** | HBMC Ch. 17.04; CBC Ch. 55 local addition — parcel overlay status must be verified. Standard reroof (no excavation, no structural) typically exempt. Scope expansion (new deck, grading, demo) triggers HBFD review. |  |
| HB-5 | **Solar panel coordination** `[HBMC]` | ⚠️ **flag** | If existing solar panels must be removed and reinstalled, a separate solar/electrical permit is required. Reviewer scopes; notes applicant if missing. |  |
| HB-8 | **Open violations check** `[HBMC]` | ⚠️ **flag** | Building dept policy — reviewer runs permit/violation history on parcel before issuance. Any unpermitted prior work must be resolved, legalized, or abated before final. |  |
| 1 | **Class B minimum — explicit confirmation** `[HBMC]` | ⚠️ **flag** | Verify roofing product is rated Class B or Class A. Product data sheet or manufacturer label must appear in submittal. Confirm against ASTM E108 or UL 790 listing. This applies to every reroof regardless of scope size. | HBMC Ch. 17.04 Local Amendment |
| 2 | **50% area threshold — entire roof upgrade** `[HBMC]` | ⚠️ **flag** | If the scope covers more than 50% of total roof area within any one-year period, the remainder of the roof must also be brought to Class B. Review submitted roof area calculations; flag if percentage is near or above 50% and only partial replacement is shown. | HBMC Ch. 17.04 Local Amendment |
| 3 | **Coastal zone — CDP check** `[HBMC]` | ⚠️ **flag** | Confirm whether parcel is in the Coastal Zone (CZ) Overlay District. Routine like-for-like reroof is generally exempt from Coastal Development Permit (CDP) under Coastal Act §30610 — no CDP is needed for standard material replacement. If the applicant is significantly changing roof type (e.g., flat to pitched, or adding dormers), consult City Planning Division. Unlike Seal Beach, HB has a certified LCP and issues its own CDPs — not the CCC directly. | Coastal Act §30610; HBMC Ch. 245 |
| 4 | **Methane district — scope change check** `[HBMC]` | ⚠️ **flag** | Confirm whether parcel is in the Methane Overlay District or Oil Production Overlay. A standard reroof (same footprint, no excavation, no structural change) does not typically trigger methane district provisions. However, if the project scope expands (new structural deck, demolition, grading), HBFD review may be required. Flag the parcel location if in a methane/oil overlay zone. | HBMC Ch. 17.04, CBC Ch. 55 (local addition) |
| 5 | **Solar panel coordination** `[HBMC]` | ⚠️ **flag** | If existing solar panels must be removed and reinstalled to complete the reroof, a separate solar/electrical permit is required. Verify this is addressed in the submittal or a note to applicant is issued. | City process / CEC |
| 6 | **Permit type — Re-Roof permit in Accela** `[HBMC]` | ⚠️ **flag** | Reroof permits are submitted as a dedicated permit type in Accela Citizen Access: "Residential Re-roof" or "Commercial Re-roof" categories. Both are available. Do not process under a general Residential Combo permit unless instructed by Building & Safety. | City process — Accela portal |
| 7 | **Fire agency — HBFD, not OCFA** `[HBMC]` | ⚠️ **flag** | All fire-related plan check and inspections are handled by the Huntington Beach Fire Department (HBFD). OCFA has no jurisdiction in HB. For any reroof in a methane overlay zone or involving fire sprinkler-related scope, coordinate with HBFD Plan Check at (714) 536-5411. | HBMC §17.56; HBFD |
| 8 | **Open violations check** `[HBMC]` | ⚠️ **flag** | If unpermitted work is discovered during plan review or field inspection (e.g., unpermitted addition, structural alteration, or prior unpermitted reroof), the reroof permit cannot be finaled until the violation is resolved, legalized, or abated. | HBMC / Building department policy |

---

## Documentation Items (informational)

Procedural / informational items with no enforceable rule. Include in the submission record; don't fail or flag in plan check.

| # | Item | Note |
|---|---|---|
| HB-6 | **Accela permit category — Re-roof** `[HBMC]` | Procedural: submit as Residential/Commercial Re-roof in Accela, not general combo. No code rule; portal routing only. |
| HB-7 | **Fire agency is HBFD (not OCFA)** `[HBMC]` | Informational: all fire-related review routes to HBFD (714) 536-5411. OCFA has no jurisdiction in HB. |

---

## Deferred to Inspection

These items are verified by the inspector in the field — **not** part of plan-check corrections. The reviewer should NOT flag these as corrections to the applicant. Inspector responsibilities:

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 7 | **Sheathing** | On tear-off: all missing, rotten, termite-eaten, or damaged sheathing must be replaced. Min thickness 1/2". Nailing: 6" OC at perimeter, 12" OC in field. Gaps in spaced sheathing <=1/4" or per manufacturer. Shingles shall be fastened only to solidly sheathed decks. | CRC R803.1, R803.2, R905.2.1 |
| 8 | **Underlayment** | Required under all roof coverings. Type depends on wind zone and material. Low-slope (2:12-4:12) requires double underlayment for shingles. Fastening: 12" grid between side laps, 6" at side/end laps. Drip edge: over underlayment at eaves, under underlayment at rakes. | CBC 1507.1.1; CRC R905.1.1, Table R905.1.1(2), Table R905.1.1(3) |
| 9 | **Flashing** | Required at wall/roof intersections, slope changes, penetrations. Metal >=0.019" (26 gage galvanized). Step flashing: min 4" legs, 2" offset from shingle edge. Sub-flashing required behind step flashing at dormers. Counter-flashing at chimney/masonry. Soffit flashing at chimney cricket. Kickout flashing at eave/sidewall intersections. Crickets for penetrations >30" wide. Valley lining installed BEFORE roofing material. Drip edge fastener spacing 12" OC. Prime metal flashing before applying bituminous materials. Rusted/damaged flashings must be replaced. | CBC 1503.2, 1503.5, 1512.5; CRC R903.2, R905.2.8, R905.2.8.3 |
| 10 | **Roof Drainage** | Drains at low points unless designed to drain over edges. Overflow drains or scuppers required where parapets trap water (inlet 2" above low point). Scuppers: 3x drain size, min 4" opening height. Drainage must not discharge onto adjacent property. | CRC R903.4, R903.4.1; CBC 1503.4 |
| 12 | **Attic Ventilation** | Vented attics: cross ventilation required. NFA = area/150 (unbalanced) or area/300 (balanced with 40-50% upper vents + vapor barrier). 1" min clearance between insulation and sheathing at vents. Vaulted ceilings: each bay ventilated individually. | CRC R806.1, R806.2, R806.3 |
| 13 | **Insulation & Radiant Barrier** | Reroof may trigger insulation upgrade to min R-22 (residential). Radiant barrier required in CZ 2-15 when vented attic with 1" air gap. Commercial low-slope: R-14 continuous insulation in CZ 1-2, 4, 8-16. | Energy Code 150.0(A), 150.1(C)1-2 |
| 14 | **Smoke & CO Alarms** | Verified at final inspection. Working alarms required in each bedroom, outside sleeping areas, each story. CO alarms required where fuel-fired appliances or attached garage. Detectors >10 years old must be replaced. For reroof-only: hardwired/interconnected upgrade NOT required (exterior work exception). | CRC R310, R311 |
| 15 | **Gas Vent Terminations** | Gas vents must extend through roof flashing/jack and terminate with listed cap. Type B/L: min 5 ft above draft hood. Height above roof per slope table. Min 3 ft above forced air inlet within 10 ft. Clearance to combustibles: 6" single-wall, 1" Type B. Pipe boots replaced during reroof. | CMC 802.6.1, 802.6.2 |

---

## References

Deep-dive references are in `references/` — load on demand for specific code questions. State skill source: `skills/california/reroof/`. City overlay source: `skills/cities/huntington-beach/reroof/`.

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
