---
name: adu
description: "ADU (Accessory Dwelling Unit) permits in Laguna Beach, CA. A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions adu in Laguna Beach."
metadata:
  version: "2.0"
  source: "HCD ADU Handbook, January 2025 (54 pages) + January 2026 Addendum (pages 55-58)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — ADU (Accessory Dwelling Unit) Permit

Handles adu (accessory dwelling unit) permits in Laguna Beach end-to-end. Scope: A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a adu (accessory dwelling unit) permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach ADU (Accessory Dwelling Unit) Permit

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

**Laguna Beach ADUs are significantly more complex than typical CA cities** because most of the city is in the Coastal Zone, requiring a Coastal Development Permit (CDP) before a building permit can issue.

---

### Decision Tree Router

#### STEP 1: Is the Property in the Coastal Zone?

**Most of Laguna Beach IS in the Coastal Zone.** If unsure, assume yes and check.

| Location | CDP Required? | Process |
|----------|--------------|---------|
| NOT in Coastal Zone | NO | Ministerial → 60-day shot clock |
| IN Coastal Zone, converting existing livable space | NO (exempt) — **see note below** | Ministerial → 60-day shot clock |
| IN Coastal Zone, new construction/addition | **YES** | CDP process (de minimis / minor / standard) |

#### STEP 2: ADU or JADU?

| Type | CDP Required? | Key Rules |
|------|--------------|-----------|
| **JADU** (≤500 sf, within SFR) | **NO** — always exempt from CDP | Building permit only, 60-day shot clock |
| **ADU** (not in Coastal Zone) | **NO** | Building permit only, 60-day shot clock |
| **ADU** (Coastal Zone, converting livable space) | **NO** (exempt) — **see note below** | Building permit only, 60-day shot clock |
| **ADU** (Coastal Zone, new construction) | **YES** | See CDP process below |

**CDP exemption-loss note**: The "converting existing livable space = CDP exempt" rule is LOST under §25.07.008(A)(1)(b)-(g) when the project is: near a bluff edge, within ESHA (environmentally sensitive habitat area), in a scenic area, or when the project increases floor area by more than 10%. In those cases, a CDP is required even for conversions.

#### STEP 3: For ADUs Requiring CDP — Which Category?

| Category | When to Use | Fee | Hearing? | Appeal? |
|----------|-----------|-----|----------|---------|
| **De minimis** | No adverse coastal impact, not in appealable area, no LCP questions, no public opposition | $125 | No | N/A |
| **Minor** | No adverse coastal impact, no LCP questions, no other discretionary entitlements | $952 | Only if requested | Yes |
| **Standard** | When de minimis and minor don't apply | $952 | Yes (public hearing) | Yes |

#### STEP 4: Review Checklist

| # | Check | What to Verify |
|---|-------|---------------|
| 1 | Coastal Zone status? | Determine if property is in Coastal Zone |
| 2 | ADU or JADU? | JADU always exempt from CDP |
| 3 | New construction or conversion? | Converting existing livable space = CDP exempt |
| 4 | CDP category? | De minimis / minor / standard based on circumstances |
| 5 | State ADU standards met? | Size limits, setbacks, height per state skill |
| 6 | LBMC Ch. 25.17 standards met? | Local development standards |
| 7 | LCP conformity? | Certified Local Coastal Program compliance |
| 8 | Coastal resource impacts? | Public views, habitat, access — private views NOT considered |
| 9 | Other discretionary approvals? | Grading, elevated decks, etc. → separate process |
| 10 | Building code compliance? | CBC/CRC per state code + city amendments (sprinklers!) |

---

### Critical Laguna Beach ADU Rules

#### Fire Sprinklers
ADUs require fire sprinklers ONLY if the primary dwelling is already sprinklered or if the ADU project fires a sprinkler retrofit trigger on the primary dwelling. If the primary dwelling has no sprinklers, the ADU itself is exempt per §25.17.050(D) — state ADU law bars a sprinkler requirement on an ADU where the primary dwelling is not required to have one.

There are **two retrofit triggers on the primary dwelling, and either one fires** (full rule: `../residential-remodel/references/city-sprinkler-retrofit.md`):
- **Ch. 14.52.030** (valuation) — cumulative additions, alterations and repairs in any three-year period exceeding 50% of the pre-work valuation.
- **Title 15 §1103.5.4** (scope) — alteration of ≥50% of the building, OR work on ≥50% of the exterior, OR an added story.

An attached ADU or a conversion that reworks the main house can fire either one. A detached new ADU generally does not.

#### Design Review
ADUs are ministerial approvals and should NOT require Design Review Board hearing. However, if the ADU project includes other discretionary components (grading, elevated decks), those components go through normal discretionary process.

#### Major Remodel Exemption
ADU construction and remodeling are **EXEMPT** from major remodel calculation. Building an ADU does not count toward the 50% threshold. **Exception**: §25.17.030(A)(3) carves out blufftop, beachfront, and canyon projects — these may still be treated as major remodels even when an ADU is involved.

#### Opposition Cannot Block ADU
For CDP hearings, the decision-maker can ONLY consider LCP conformity and coastal resource impacts. **Opposition to the ADU itself cannot be considered.** City cannot deny CDP based on private view impacts.

---

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/compliance-housing.md` — Housing Elements, RHNA, and Prohousing Designation
- `references/compliance-ordinances.md` — Local ADU Ordinances and HCD Enforcement
- `references/compliance-unpermitted.md` — Unpermitted ADUs and Legalization
- `references/compliance-utilities.md` — Utility Connections and CPUC Complaints
- `references/glossary.md` — Glossary of Defined Terms
- `references/legislative-changes.md` — Legislative Changes and SB 477 Renumbering
- `references/ownership-hoa.md` — HOA Restrictions and CC&R Nullification
- `references/ownership-sales.md` — Separate Conveyance, Condominiums, and Qualified Nonprofits
- `references/ownership-use.md` — Owner-Occupancy, Rental Terms, and Deed Restrictions
- `references/permit-fees.md` — Fees — Impact Fees, Proportionality, School Fees, and Utility Connections
- `references/permit-funding.md` — Funding and Financing for ADUs
- `references/permit-process.md` — Permit Process — Ministerial Review, Timelines, and Deemed Approval
- `references/special-manufactured.md` — Manufactured Homes and Mobilehome Parks
- `references/special-sb9.md` — SB 9 Interaction with ADU Law
- `references/standards-design.md` — Design Standards — Objective vs. Subjective
- `references/standards-fire.md` — Fire Protection and Sprinkler Requirements
- `references/standards-height.md` — Height Limits by ADU Type
- `references/standards-parking.md` — Parking Requirements and Exemptions
- `references/standards-setbacks.md` — Setback Rules
- `references/standards-size.md` — Size Requirements and Restrictions
- `references/standards-solar.md` — Solar and Energy Code Requirements
- `references/unit-types-66323.md` — 66323 Units — Four State-Mandated ADU Categories
- `references/unit-types-adu-general.md` — ADU Definition and Three Physical Types
- `references/unit-types-jadu.md` — Junior Accessory Dwelling Units (JADUs)
- `references/unit-types-multifamily.md` — Multifamily ADU Rules
- `references/zoning-general.md` — General Zoning Rules
- `references/zoning-hazards.md` — Hazard Zones — Fire, Coastal, and Environmental Constraints
- `references/zoning-nonconforming.md` — Nonconforming Zoning and Building Code Violations

**Laguna Beach rules**

- `references/city-adu-faq.md` — Laguna Beach ADU/JADU — FAQ & Coastal Development Permit Process
- `references/city-adu-ordinance.md` — Laguna Beach ADU/JADU Development Standards — Quick Reference
- `references/city-coastal-permits.md` — Laguna Beach ADU — Coastal Development Permit Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
