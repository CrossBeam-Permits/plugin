---
name: demolition
description: "Demolition (Full Structure) permits in Laguna Beach, CA. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions demolition in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2), Chapter 33; 2025 California Existing Building Code (Title 24, Part 10), Chapter 15; 2025 California Green Building Standards Code (Title 24, Part 11), §4.408 / §5.408; SCAQMD Rule 1403; BAAQMD Regulation 11 Rule 2; EPA Lead Renovation, Repair & Painting Rule (40 CFR Part 745, Subpart E); CDPH Title 17 CCR §35001 et seq.; California Government Code §§7260–7277"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026 (2025 Code Cycle effective date)"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Demolition (Full Structure) Permit

Handles demolition (full structure) permits in Laguna Beach end-to-end.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a demolition (full structure) permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Demolition (Full Structure) Permit

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

Note: Demolition rules are predominantly local — most of this skill's content represents city-specific requirements.

---

### Decision Tree Router

| Topic | Route |
|-------|-------|
| **Full demolition of structure** | Demolition Notification form required + permits below |
| **Partial demolition (remodel)** | Check major remodel threshold first (see `laguna-beach-residential-addition`) |
| **Heritage/historic property** | Heritage Committee review may be required |

---

### Demolition Requirements

#### Demolition Notification
- **Demolition Notification form required** (standard-plans/demolition-notification.pdf)
- Must be submitted to Building Division before permit issuance

#### Required Permits/Reviews

| Trigger | Required |
|---------|----------|
| Any demolition | Building Permit + Demolition Notification |
| Property in Coastal Zone | **Coastal Development Permit REQUIRED** — §25.07.004 + §25.07.006(D) explicitly include demolition in definition of development |
| Property 50+ years old | **Heritage Committee review** potential |
| Any demolition | **SCAQMD Rule 1403 notification** required for ALL demolitions (SCAQMD defines demolition broadly as "wrecking or taking out of any load-supporting structural member") |
| Partial demo crossing 50% threshold | Treated as **major remodel** (new construction standards) |

#### Major Remodel Connection
Demolition of 50%+ of exterior walls (computed on each floor and for the whole structure; if a floor is at 50%+ but the whole-structure total is under 50%, return FLAG — see `../residential-remodel/references/city-major-remodel-methodology.md`), or combined roof/walls/foundation in the coastal zone appealable area, measured for each building or structure separately, triggers the major remodel definition (Major Remodel Interpretation Quick Guide, Updated June 2026), which means the remaining/new construction must meet new construction standards. See `laguna-beach-residential-addition` skill for detailed calculation methods.

**ADU demolition is EXEMPT** from the major remodel calculation.

---

### Additional Demolition Requirements

#### Utility Meter Removal
Utility meters (gas, electric, water) must be removed/disconnected before demolition. Coordinate with utility providers for meter pulls prior to permit issuance.

#### Green Halo Program — C&D Recycling/Diversion
Construction & demolition (C&D) debris recycling/diversion is required under the Green Halo Program. Demolition projects must comply with waste diversion requirements.

#### Protection of Adjoining Property
Per §14.50.132, the applicant must provide:
- **30-day written notice** to owners of adjoining property before demolition
- **Bond** for protection of adjoining property

---

### Key Facts

- **Demolition Notification**: Required form, submitted to Building Division
- **Heritage review**: Properties 50+ years old may trigger Heritage Committee review
- **Coastal Zone**: CDP REQUIRED for demolition in Coastal Zone (§25.07.004 + §25.07.006(D))
- **SCAQMD**: Rule 1403 notification required for ALL demolitions
- **Utility meters**: Must be removed/disconnected before demolition
- **C&D diversion**: Green Halo Program recycling/diversion required
- **Adjoining property**: 30-day notice + bond required (§14.50.132)

---

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/asbestos-neshap-rule-1403.md` — AQMD Asbestos Notification & Survey
- `references/boundary-vs-ltia.md` — Skill Boundary -- Demolition vs. LTIA Demolition
- `references/cbc-chapter-33.md` — CBC Chapter 33 -- Safeguards During Construction (Demolition Focus)
- `references/cd-debris-diversion.md` — CALGreen Construction & Demolition Waste Diversion
- `references/lead-safe-work-pre-1978.md` — Lead-Safe Work Practices for Pre-1978 Demolition
- `references/relocation-noticing.md` — Tenant Relocation Noticing for Demolition Projects
- `references/utility-disconnect.md` — Utility Disconnect Verification

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
