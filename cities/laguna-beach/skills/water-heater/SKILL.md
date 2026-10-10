---
name: water-heater
description: "Water Heater permits in Laguna Beach, CA. A water heater replaced or relocated, with its venting, seismic strapping, pan, and expansion control. Laguna issues this on the state skill alone, with no city delta. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions water heater in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Plumbing Code (Title 24, Part 5), 2025 California Mechanical Code (Title 24, Part 4), 2025 California Energy Code (Title 24, Part 6)"
  authority: "California Building Standards Commission / IAPMO Uniform Plumbing Code with California Amendments"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Water Heater Permit

Handles water heater permits in Laguna Beach end-to-end. Scope: A water heater replaced or relocated, with its venting, seismic strapping, pan, and expansion control. Laguna issues this on the state skill alone, with no city delta.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a water heater permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Water Heater Permit

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

> Laguna Beach's local layer for this permit.

Laguna Beach has no local amendment for this permit; the City issues it on the California rules alone (verified in the City's code research). The California checklist below applies in full. The citywide overlays above still apply when the scope reaches them.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Venting system** | ❌ **fail** | Select an allowed venting-system path under CPC Table 509.4 and the appliance listing. Size the connector and vent from the appliance outlet/listing and CPC 509/510 or CMC 802/803. Verify the applicable termination, cap, flashing, connector slope, and listed clearances. For CPC installations through insulated assemblies, verify the 26-gauge/2-inch shield in CPC 509.6.1.1; do not impose an unsupported concealed-framing shield-plate recipe. | CPC 509, 510; CMC 802, 803 |
| 2 | **Combustion air** | ❌ **fail** | Verify an applicable CPC 506 / CMC 701 method. Indoor air may use the standard-volume or known-infiltration method; known infiltration below 0.40 ACH requires the known-rate calculation. For ducts, verify CPC 506.9 / CMC 701.11 construction, unobstructed termination, single-space service, upper/lower separation, attic-screen prohibition, upper-horizontal-duct slope, chimney-annulus prohibition, and the correct 12-inch exterior-intake subitem. Screens are conditional and have a minimum 1/4-inch mesh opening; nonmotorized louvers/grilles are fixed open; manual dampers are prohibited and prior-approved power louvers require interlock. | CPC 506; CMC 701 |
| 4 | **T&P relief valve** | ❌ **fail** | Pressure relief device at WH (CPC 504.4); temperature probe in top 6 in (CPC 504.5); opens at 150 PSI or 210 deg F; no shutoff/check valves before or after | CPC 504.4, 504.5, 504.6, 608.3, 608.4 |
| 5 | **T&P discharge pipe** | ❌ **fail** | Min 3/4 in, full size to flood level, gravity flow, terminate 6-24 in above grade pointing down, no threads on end, no traps/uphill runs, not into drain pan, not into crawlspace, each piped independently, readily observable | CPC 608.5 |
| 6 | **Drain pan** | ❌ **fail** | Required where leakage causes damage (attic, floor assembly); min 1.5 in deep, 3/4 in drain to approved location; relief valve discharge into pan prohibited | CPC 507.5 |
| 7 | **Expansion tank** | ❌ **fail** | Required if closed system (backflow preventer, check valve, or PRV present); on cold water supply; properly sized; complies with IAPMO/ANSI Z1088 | CPC 608.2, 608.3 |
| 16 | **Water pressure** | ⚠️ **flag** | Min 15 PSI residual after losses; expansion tank/device if PRV or backflow preventer prevents pressure dissipation | CPC 608.1, 608.2, 608.3 |
| 17 | **Water hammer** | ⚠️ **flag** | ASSE 1010 mechanical arrestors (not air chambers) near quick-close valves if applicable | CPC 609.11 |
| 18 | **Vacuum relief** | ❌ **fail** | Required when WH is above fixture outlets (e.g., attic installation) | CPC 608.7 |
| 19 | **Gas line** | ❌ **fail** | Existing line adequate for BTU rating; approved flex connector (max 6 ft, same room, not concealed); sediment trap/drip leg; shutoff valve within 6 ft, accessible | CPC 1208, 1212, 1215 |
| 20 | **Hot water max developed length** | ⚠️ **flag** | Maximum 100 ft developed length from hot water source to furthest fixture; exceeding requires recirculation system or point-of-use heater | CPC 609.11 |
| 21 | **Manifold sizing** | ❌ **fail** | Cold water manifold fed from end shall be one size larger than water heater supply connection; ensures adequate flow distribution | CPC 610.8 |
| 23 | **Energy compliance** | ❌ **fail** | Meets federal/state minimum UEF per draw pattern; nameplate verification; replacement triggers pipe insulation requirement; recirculation must be demand-controlled if present | Part 6 Section 110.3, Section 150.2 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 3 | **Seismic strapping** | Two straps (upper 1/3, lower 1/3), 24-gauge min plumber's tape or listed kit, attached to wall studs, lower strap min 4 in above controls. Flexible connections at water/gas lines for seismic movement (CPC 507.3). General appliance anchoring per CPC 302.4. | CPC 507.2, 507.3, 302.4; H&S 19211 |
| 8 | **Clearances & combustibles** | Apply the code, listing, and manufacturer instructions concurrently. Select single-wall vent clearance from the applicable CPC Table 509.7.3.4(1) or CMC Table 802.7.3.3 row and conditions; Type B clearance follows its listing/manufacturer. | CPC 507.26, Table 509.7.3.4(1); CMC 303.10, Table 802.7.3.3 |
| 9 | **Location restrictions** | Not in bedrooms/baths (unless direct-vent or sealed closet with gasketed self-closing door); not where flammables stored; garage: 18 in elevation (FVIR exempt) + vehicle barrier; ground support: min 3 in concrete pad | CPC 504.1, 507.4, 507.12, 507.13 |
| 10 | **Access & working space** | Min 30 in x 30 in working platform; attic: 22x30 in access opening, 24 in passageway with solid floor (508.4.2), max 20 ft (if <6 ft height), light switch at passageway entrance (508.4.4), working platform 30x30 in at service side (508.4.5); appliance accessible for service/inspection/removal. Clearances to combustibles per manufacturer AND per code (CPC 504.3.1). | CPC 504.3.1, 507.25, 508.4, 508.4.2, 508.4.4, 508.4.5 |
| 11 | **Water heater connectors** | Flex connectors max 24 in (copper/stainless), comply with ASME A112.18.6; PEX/PE-RT not within first 18 in of piping at WH; connectors accessible | CPC 604.5, 604.13 |
| 12 | **Piping materials** | All materials NSF 61 compliant; lead content max 0.25% (pipe/fittings) / 0.2% (solder/flux); no reused piping for potable water | CPC 604.1, 604.2, 604.8 |
| 13 | **Joints & connections** | Solder per ASTM B828/B813; dielectric fittings at copper-to-galvanized; dissimilar metals at accessible locations only; press-connect with O-ring and mfr tool; push-fit per ASSE 1061 | CPC 605.1.4, 605.16, 310.6 |
| 14 | **Valves** | Fullway shutoff on cold supply (accessible); control valve at appliance; unions within 12 in for removal | CPC 606.2, 606.5, 606.6, 609.5 |
| 15 | **Hot water insulation** | All hot water piping insulated; thickness >= pipe diameter (up to 2 in pipes), 2 in for larger; first 5 ft from WH minimum R-4 | CPC 609.12; Part 6 Section 150.0(j) |
| 22 | **Listing and labeling** | Installation/maintenance instructions must remain affixed to unit (CPC 507.24); WH used for space heating must be labeled for both purposes (CPC 501.1) | CPC 501.1, 507.24 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/clearances-location.md` — Clearances, Location & Access Requirements
- `references/energy-efficiency.md` — Energy Code & Efficiency Requirements for Water Heater Permits
- `references/gas-line-sizing.md` — Gas Line Sizing & Connections
- `references/piping-materials-joints.md` — Piping Materials, Joints & Connections
- `references/seismic-strapping.md` — Seismic Strapping Requirements for Water Heaters
- `references/tp-relief-drain.md` — T&P Relief Valve, Discharge Pipe, Drain Pan & Expansion Tank
- `references/valves-connections.md` — Valves, Connections & Water Supply
- `references/venting-gas.md` — Gas Water Heater Venting & Combustion Air

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
