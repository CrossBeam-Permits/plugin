---
description: "Swimming Pool and spa permits in Laguna Beach, CA. Works in two modes: (A) BUILDER/HOMEOWNER — establishes the LBMC planning route, checks state and local compliance, and hands confirmed facts to the Laguna submit plugin; (B) CITY REVIEWER — checks a submitted pool/spa project and produces tight corrections output. Covers the 3-foot Design Review split, coastal/CDP analysis, 25-foot bluff setback, geotechnical triggers, and the separate six-part equipment test effective 2026-08-20."
version: "1.0"
source: "2025 CBC §§107.2, 1808.7.3, 3109; 2025 CRC Appendix CI; 2025 CEC Article 680; 2025 CPC Chapters 7 and 12; Health & Safety Code §§115920-115929; LBMC §§7.25.130, 25.05.040, 25.05.045, 25.07.008, 25.50.004; Laguna Beach Ordinances 1731, 1732, and 1733"
authority: "California Building Standards Commission and City of Laguna Beach"
law_as_of: "2026-08-24"
---

# Laguna Beach — Swimming Pool Permit

Handles swimming pool permits in Laguna Beach end-to-end.

**First thing in every conversation:** ask which mode the user is in.

> "Are you (A) planning to file a swimming pool permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **Builder / Homeowner Intake** below
- Mode B → walk **City Reviewer Checklist** below

Both modes share the same rules. The difference is direction of travel — builder scopes forward, reviewer checks backward.

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

## MODE A — Builder / Homeowner Intake

### A1. Intake

Before naming any Planning route, ask and establish:

1. Is the pool/spa more than 3 feet above **adjacent legal ground elevation**, no more than
   3 feet, or still unknown? If it is a portable spa, is it more than 600 gallons?
2. Is the parcel/work in the coastal zone, and does any CDP-exemption exception apply?
3. Is the parcel oceanfront or bluff-adjacent, and has the top of bluff been established?

Unknown answers stay unknown. Do not assume Design Review, Zone Clearance, a CDP
exemption, or bluff compliance. Then collect the remaining project, applicant, and
plan-check facts naturally, using the checklist below as the coverage floor.

#### Laguna Planning route

Route the pool/spa structure and its equipment separately:

- **Structure more than 3 feet above adjacent legal grade:** Design Review Board / Planning
  Commission under LBMC §25.05.040(B)(1)(j), using the one Design Review Application.
- **Structure no more than 3 feet, or portable spa no more than 600 gallons:** Zone
  Clearance under §25.05.040(B)(2)(t) and §25.05.045; this finishes through a Planning
  appointment, not online type 114.
- **Environmentally sensitive area:** an otherwise lower-tier item goes to (B)(1) unless
  the licensed-professional determination and peer review establish no impact.

The governing design-review tier is singular: `drb` outranks `admin_dr`, which outranks
`zone_clearance`. Name all matched components, but include the City's Design Review
Application only once. Add CDP, CUP, variance, and ADU/JADU forms when independently
required. CDP is a parallel completeness track and never substitutes for Design Review.

For equipment in or adjacent to a residential area, record each part of the
§7.25.130(C) test separately (effective 2026-08-20):

1. ground-mounted or wall-mounted at ground level;
2. outside required front and side setbacks;
3. at least 5 feet from every property line;
4. specification sheet with decibel rating, no more than 60 dB day / 50 dB night at the
   property line, and two maintained sound-attenuation techniques;
5. City-provided form computing property-line sound under ARI Standard 275 (1984, as
   amended)—the City's form title is unconfirmed, so do not invent it; and
6. a 3-foot path of travel around every structure.

All six yes → equipment Zone Clearance without Design Review under
§25.05.040(B)(2)(v). Any no → Administrative Design Review under
§25.05.040(B)(3)(a)(v). Any unknown → equipment route undetermined. This test does not
downgrade the structure route. The contractor acknowledgment in §7.25.130(A) remains an
issuance requirement.

Independently analyze the §25.07.008(A)(1) pool CDP exemption and its exceptions. For an
oceanfront/bluff parcel, enforce the 25-foot pool/spa setback from top of bluff in
§25.50.004(B)(4) using survey/geotechnical evidence. Require the City geotechnical branch
for a new pool on an ungraded lot, in a floodplain, or on a coastal bluff top; also flag
steep-hillside, liquefaction, prior-failure, unconventional-foundation, and Building
Official-discretion conditions.

### A2. Pre-submission Compliance Check

Once you have enough info, walk the Plan-Check Checklist below using the user's answers. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what additional info or documentation they need to gather
- **PASS** → confirm, move on

### A3. Submission Guide

When the Planning route is established and compliance is clean (or flag-only), produce a
route-specific submission guide. Do not promise over-the-counter issuance:

```
## Ready to Submit — Laguna Beach Swimming Pool Permit

**Planning route:** [Zone Clearance appointment, or the one Design Review Application]
**Parallel/additive applications:** [CDP, ADU/JADU, CUP, variance, or none]
**Building after Planning:** one pool Building application and its own valuation

### Required uploads
[Generated per skill — product data sheets, plan sketches, waste management plan if applicable, HBFD clearance if overlay-triggered, etc.]

### Inspection sequence
[Generated per skill — standard inspection milestones]
```

### A4. Optional — portal automation

If the dependent Laguna submit plugin is installed, hand the confirmed facts and filing
theory to `$laguna-permit-preparer`. It fills only verified official forms, uses a visible
browser abstraction when portal filing is supported, and stops at `portal_ready` with an
exact handoff when browser control is unavailable. It never submits without a fresh final
approval and a terminal confirmation receipt.

Zone Clearance remains an appointment workflow. For type 114, include all confirmed
Planning forms once in the single `Application` PDF and keep the CDP checklist/result
separate. After Planning approval is effective, create the pool Building record separately
from remodel, ADU, or other Building scopes, each with its own valuation.

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
   [LBMC-specific flag items — parcel overlays, city-specific checks]

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
| 1 | **Site plan complete?** | ⚠️ **flag** | Property lines, all structures with dimensions and setbacks, proposed pool location, easements, driveways, fencing locations with heights, utility locations, north arrow, scale | CBC 107.2 |
| 2 | **Pool/spa plan details?** | ⚠️ **flag** | Structural details, dimensions, material specifications, cross-sections showing existing slopes and retaining walls to 5 ft beyond property lines | CBC 3109, 107.2 |
| 3 | **Structural calculations?** | ❌ **fail** | Required if non-standard plan. Standard plans (where approved by jurisdiction) may be exempt. | CBC 1901, 3109 |
| 4 | **Slope setback adequate?** | ❌ **fail** | Pool-to-slope setback = half the building footing setback distance. Pool wall within 7 ft horizontal of slope top must support water without soil support. Soil report required if pool is within 15 ft of slope top or 8 ft of slope toe (slope steeper than 1:3). | CBC 1808.7.3 |
| 5 | **Concrete/shotcrete specs?** | ❌ **fail** | Min f'c = 4,500 psi 28-day, Type V cement (sulfate-resistant), max w/c ratio = 0.45 per ACI 318. Special inspection required for gunite/shotcrete per CBC 1705.3, 1908. | CBC Ch. 19, ACI 318 |
| 6 | **Soil report provided (if required)?** | ❌ **fail** | Required when pool is near slopes (see item 4). Geotechnical memo confirming excavation suitability required before steel inspection. | CBC 1803.2 |
| 7 | **Barrier/enclosure compliant?** | ❌ **fail** | Min 60" high, max 2" ground clearance, no 4" sphere passage, no climbable features, gates self-closing/self-latching with latch at min 60" above ground, gates swing away from pool | HS Code 115923, CRC App. CI |
| 8 | **Drowning prevention features (2-of-7)?** | ❌ **fail** | Two different qualifying features from seven options. Certain combinations prohibited (e.g., exit alarm + door latch on same door, pool cover + pool alarm). | HS Code 115922 |
| 9 | **Safety glazing near pool?** | ❌ **fail** | Required for glazing within 60" above standing surface and within 60" horizontal of water's edge | CRC R324.4.5 |
| 10 | **Equipotential bonding grid?** | ❌ **fail** | Pool shell rebar bonded, perimeter surfaces bonded within 3 ft of pool edge, all metallic components bonded. Bonding to perimeter at min 4 points uniformly spaced. Conductor: min #8 AWG solid copper. | CEC 680.26 |
| 11 | **GFCI protection adequate?** | ❌ **fail** | All 125V receptacles within 20 ft of pool edge GFCI-protected. Receptacle required 6-20 ft from pool edge. No receptacles within 6 ft. | CEC 680.22 |
| 12 | **Underwater lighting compliant?** | ❌ **fail** | Wet-niche fixtures: GFCI-protected, max 150V, forming shell grounded to equipment grounding conductor. Low-voltage (15V or less) listed LED fixtures permitted. | CEC 680.23 |
| 13 | **Pool pump/motor wiring?** | ❌ **fail** | Disconnect within sight and min 5 ft from pool edge. Motors GFCI-protected per 680.21(C). Wiring methods suitable for corrosive environments. No aluminum conduit. | CEC 680.21, 680.13, 680.14 |
| 14 | **Pool heater compliant?** | ❌ **fail** | Gas: installed per CPC, manufacturer instructions, Energy Code 110.4 certification. Electric: proper circuit sizing, disconnect. Cover required if outdoor heat pump or gas heater (Cal Energy Code 110.4). | CPC, CEC 680.9 |
| 15 | **Suction outlets anti-entrapment?** | ❌ **fail** | Min 2 suction outlets per pump, hydraulically balanced, min 3 ft apart. Anti-entrapment grates per ANSI/APSP-16, removable only with tools. | HS Code 115928 |
| 16 | **Drain system adequate?** | ❌ **fail** | Two return drains required -- one at bottom, one at side 2" within bottom, min 4 ft apart, with anti-vortex covers. | HS Code 115928, CPC |
| 17 | **Plumbing/filtration per code?** | ❌ **fail** | Water supply with backflow prevention, filtration system, water heater piping per CPC. All drains/grates/skimmer covers approved before installation. | CPC Ch. 7, 12 |
| 18 | **Drainage/grading adequate?** | ⚠️ **flag** | Deck and surrounding grade slope minimum 2% away from structures. Pool drainage does not increase runoff to neighboring properties. | CBC 1804.4 |
| 19 | **Erosion/sediment control?** | ⚠️ **flag** | Erosion and sediment control plan required. BMP measures during construction. NPDES compliance for dewatering. | CBC 3304.1.5 |
| 20 | **Equipment listing?** | ❌ **fail** | All pool equipment (pump, filter, heater, lighting, GFCI devices) listed and installed per manufacturer instructions. | CEC 110.3(B), CBC 3109 |

---

## References

Deep-dive references are in `references/` — load on demand for specific code questions. State skill source: `skills/california/swimming-pool/`. City overlay source: `skills/cities/laguna-beach/swimming-pool/`.

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
