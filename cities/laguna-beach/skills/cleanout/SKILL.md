---
name: cleanout
description: "Cleanout permits in Laguna Beach, CA. A sewer cleanout added or replaced on an existing building drain. Plumbing only, no structure. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions cleanout in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Plumbing Code (Title 24, Part 5) — Chapter 7, Section 707; LBMC Title 17 PSL program; 2025 CPC"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Cleanout Permit

Handles cleanout permits in Laguna Beach end-to-end. Scope: A sewer cleanout added or replaced on an existing building drain. Plumbing only, no structure.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a cleanout permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Cleanout Permit

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

For cross-cutting city info (portal, contact, codes, VHFHSZ, coastal zone, DRB), see `../city-reference/SKILL.md`.

---

### City-Specific Notes

| Item | Detail |
|------|--------|
| **Permit type** | OTC-eligible for interior cleanout adds; PSL lateral work routes through Building + Water Quality |
| **Plumbing code adoption** | LBMC §14.64.010 adopts 2025 CPC with **zero amendments** — core §707 rules apply unchanged |
| **Sewer overlay** | LBMC Title 17, Chapter 17.50 (Private Sewer Laterals) + Chapter 17.12 (Connections) |
| **Conflict rule** | LBMC §14.64.010 — "more restrictive shall govern" when Title 17 stacks on CPC §707/§710 |
| **Reimbursement** | Up to 50% of cost, max $1,600/parcel, per Laguna PSL Program FAQ |

---

### Scope Trigger — When Do These Overrides Fire?

Not every cleanout permit triggers the full PSL overlay. Use this gate first:

| Scope | Overrides That Fire |
|-------|--------------------|
| Pure interior cleanout add (e.g., base-of-stack, change-of-direction) — no lateral work | None — state checklist only |
| New or replaced **private sewer lateral** (any portion) | LB-CLN-1, LB-CLN-2, LB-CLN-5 |
| Cleanout bundled with **bath / kitchen / laundry remodel** | LB-CLN-3 (PSL video inspection) |
| Cleanout bundled with **material sewage-flow increase** | LB-CLN-3 |
| Any project ≥ **$100,000 valuation** | LB-CLN-3 |
| **Hillside / oceanside / multi-level** parcel | LB-CLN-4 (Water Quality review) |
| Any trenching or work in the **public right-of-way** | LB-CLN-5 (parallel Public Works permit) |

---

### Review Checklist — Laguna Beach-Specific Items

| # | City Check | Pass Criteria | Code Section |
|---|-----------|---------------|--------------|
| LB-CLN-1 | **Property-line cleanout on new/replaced lateral** | Plan/site detail shows a cleanout located at or near the property line on every new or replaced private sewer lateral. | LBMC §17.50.040 / §17.50.050 |
| LB-CLN-2 | **Backflow preventor on new/replaced lateral** | Backflow preventor installed on the lateral regardless of fixture elevation (this goes beyond CPC §710, which is elevation-triggered). Device must be on Laguna's approved list and housed in a concrete or cast-iron box that is readily accessible. | LBMC §17.50.040 / §17.50.050; §17.12 (Connections) |
| LB-CLN-3 | **PSL video inspection trigger** | If cleanout work is bundled with a bath/kitchen/laundry remodel, a material sewage-flow increase, OR any project ≥ $100,000 valuation, the entire PSL must be cleaned and video-inspected by a qualified plumber. Video (with date, beginning/ending points, audio assessment, footage counter) and inspection report must be furnished to the city within **14 days**. | LBMC §17.50.020 (definitions of "private property building remodel" and "qualified plumber"); §17.50.054 (testing) |
| LB-CLN-4 | **Hillside / oceanside / multi-level backwater valve review** | On hillside, oceanside, or multi-level parcels, confirm backwater valve installation has been reviewed by the **Water Quality Division** (joint with Engineering), even when CPC §710's upstream-manhole rule would not otherwise trigger. | Laguna Beach Water Quality Division — Private Development Projects program |
| LB-CLN-5 | **Public Works (ROW) permit** | If any portion of the cleanout/lateral work crosses the **public right-of-way**, a parallel Public Works permit from the Building department is required, and the city must inspect the completed work for approval. | Laguna Beach PSL Program FAQ |
| LB-CLN-6 | **Correction grace period** | Defects identified during PSL inspection/testing must be corrected within the **correction grace period — 90 days** from the earlier of the triggering events listed in §17.50.020. The director may extend on written request for good cause. Property owner must furnish documentation of corrective measures completed within the grace period. | LBMC §17.50.020 (definition); §17.50.054 (testing); §17.50 corrective measures |
| LB-CLN-7 | **Code edition** | 2025 CPC cited (Laguna adopted 2025 CBSC with zero CPC amendments per §14.64.010). | LBMC §14.64.010 |

---

### Out-of-Scope (Handled by State Skill)

- CPC §707 cleanout type, sizing (Table 707.1), location (every 100 ft, change of direction >135°, upper terminal), access/clearance — **unchanged** in Laguna.
- CPC §710 elevation-triggered backwater valve — Laguna's §17.12 mirrors this rule; only the device-type list and box/access detail differ (covered by LB-CLN-2).
- C-36 (plumbing) contractor licensing — state law, no Laguna override.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Cleanout type appropriate?** | ❌ **fail** | Two-way at building drain/sewer junction; one-way at direction changes >135° | CPC 707.1, 707.4 |
| 3 | **Cleanout size correct?** | ❌ **fail** | Same size as pipe served, up to 4" max | CPC 707.9, Table 707.1 |
| 4 | **Administrative** | ❌ **fail** | Licensed C-36 (plumbing) contractor | State license law |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 2 | **Location accessible?** | Above grade or floor level; not buried or blocked; clearance per 707.9 | CPC 707.7, 707.8, 707.9 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/cleanout-requirements.md` — CPC Section 707 — Cleanout Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
