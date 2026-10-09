---
name: rewire
description: "Rewire permits in Laguna Beach, CA. Branch circuits or the wiring of an existing dwelling replaced or extended, without moving the service. Laguna issues this on the state skill alone, with no city delta. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions rewire in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Electrical Code (Title 24, Part 3) — Articles 210, 220, 310, 334; 2025 California Residential Code (Title 24, Part 2.5) — Sections R310, R311"
  authority: "California Building Standards Commission / National Electrical Code with California Amendments"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Rewire Permit

Handles rewire permits in Laguna Beach end-to-end. Scope: Branch circuits or the wiring of an existing dwelling replaced or extended, without moving the service. Laguna issues this on the state skill alone, with no city delta.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a rewire permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Rewire Permit

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
| 1 | **Service capacity adequate?** | ❌ **fail** | If full rewire: verify panel can handle all circuits; load calc per 220.83(A) | CEC 220.83(A) |
| 2 | **Outlet spacing correct?** | ❌ **fail** | Habitable rooms: no point >6' from receptacle; kitchen countertop: no point >24" from receptacle | CEC 210.52 |
| 3 | **GFCI protection?** | ❌ **fail** | Required in: bathrooms, kitchens, garages, outdoors, laundry, crawl spaces, basements, near sinks/tubs | CEC 210.8(A) |
| 4 | **AFCI protection?** | ❌ **fail** | Required in: kitchens, bedrooms, family/living/dining rooms, hallways, closets, laundry, rec rooms | CEC 210.12(B) |
| 5 | **Dedicated circuits?** | ❌ **fail** | Kitchen: 2× 20A small-appliance; bathroom: 20A; laundry: 20A; garage: 20A | CEC 210.11(C) |
| 6 | **Wire type and sizing?** | ❌ **fail** | NM cable (Romex) for residential; #14 for 15A, #12 for 20A; conduit where exposed | CEC 334, Table 310.16 |
| 8 | **Contractor licensing?** | ⚠️ **flag** | Licensed C-10 Electrical Contractor required (CA B&P Code §7028). Owner-builder exemption per B&P §7044 only for owner-occupied residential where owner personally performs the work. Verify active CSLB license and workers' comp insurance. | CA B&P §7028, §7044 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 7 | **Smoke/CO detectors?** | Rewire triggers requirement to bring smoke/CO up to current code if wall/ceiling finishes are removed | CRC R310, R311 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/gfci-afci-210.md` — CEC Sections 210.8 and 210.12 — GFCI and AFCI Protection
- `references/outlet-spacing-210.md` — CEC Section 210.52 — Dwelling Unit Receptacle Outlet Spacing
- `references/smoke-co-detectors.md` — CRC R310 / R311 — Smoke and CO Alarm Requirements Triggered by Rewire

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
