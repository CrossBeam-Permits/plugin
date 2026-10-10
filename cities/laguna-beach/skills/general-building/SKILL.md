---
name: general-building
description: "Minor Building Work permits in Laguna Beach, CA. Minor work no other kind names: drywall and interior finish patches, a stucco or siding patch, skylights in an existing roof, a shed, hardscape at grade, a plumbing fixture swap in place, a fire-sprinkler retrofit, a repair carried by an engineer letter. NOT anything that adds floor area, alters a bearing wall, cuts a new opening, or arrives with a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions general building in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2), California Residential Code (Part 2.5), California Plumbing Code (Part 5), California Energy Code (Part 6); California Business and Professions Code Division 3, Chapter 9; LBMC Ch. 14.70 (WUI Code), Ch. 14.50 (Building Code amendments), Ch. 14.52 (Fire sprinklers), Ch. 25.05 (Design Review), Ch. 25.07 (Coastal), Title 15 (Fire Prevention); City of Laguna Beach 'Building Plan Review Services' 06/08/2026"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Minor Building Work Permit

Handles minor building work permits in Laguna Beach end-to-end. Scope: Minor work no other kind names: drywall and interior finish patches, a stucco or siding patch, skylights in an existing roof, a shed, hardscape at grade, a plumbing fixture swap in place, a fire-sprinkler retrofit, a repair carried by an engineer letter. NOT anything that adds floor area, alters a bearing wall, cuts a new opening, or arrives with a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a minor building work permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Minor Building Work Permit

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

Override-only. Every state checklist item in `california-general-building` applies unless this
file overrides it. Load the state skill first.

Laguna issues this work over the counter, but three city layers reach even a $500 permit: the
fire zone, the sprinkler retrofit triggers, and the coastal zone. None of them is in state law.

---

### LB-1 — The work must be on the City's OTC list, or it is not counter work

`../city-reference/SKILL.md` §"Permit Processing Tracks" is the single home for the hours and the City's 11
numbered qualified-project items. Cite by number; do not restate the list.

The minor work this skill covers usually lands on:

| Scope | OTC item |
|---|---|
| Plumbing fixture swap, small electrical or mechanical repair or replacement | Item 9 |
| Deck, balcony or patio-cover repair with minor structural modification, no extension or replacement | Item 2 |
| Exterior siding replacement, which a stucco or siding patch sits under | Item 5 |

**Disqualifiers still apply to every one of them** (`../city-reference/SKILL.md`, same section): another City
department's review, an outside agency approval, geotechnical report review, extensive
structural design and modification, change of construction type, or a change of use to a more
restrictive occupancy. Any one of those and the permit is a full plan review, whatever its
valuation.

Work that is on no OTC item and is not on the full-review list is still a permit; say which
track it takes and why.

### LB-2 — Fire zone reaches exterior patches (Ch. 14.70)

Most of the city sits in a fire hazard severity zone; determine the parcel from the adopted 2025
LRA map, never from a citywide figure (`../city-reference/SKILL.md` §"Very High Fire Hazard Severity Zone").

- Exterior wall covering must be noncombustible, ignition-resistant and labelled for exterior
  use, or fire-retardant-treated wood (§14.70.030, amending WUI Code 504.5.2). Vinyl, untreated
  wood, and polypropylene do not comply.
- **§14.70.015 minor-repair exception**: with the **building official's approval**, a minor
  repair or replacement of exterior material may use the **same material as existing**. This is
  the exception a stucco or siding patch relies on. It is not automatic, it does not permit a new
  non-compliant material, and a full re-clad is not a minor repair. Route a whole wall or
  elevation to `laguna-beach-siding-replacement` instead of this skill.
- A shed is a structure in the fire zone. Its materials and its separation are city questions,
  not state ones.

### LB-3 — A small permit can fire the sprinkler retrofit

**Two independent triggers; either one fires.** The full rule is
`../residential-remodel/references/city-sprinkler-retrofit.md` — the single residential retrofit
reference. Do not restate it.

- **Ch. 14.52.030** — valuation: cumulative additions, alterations and repairs in **any
  three-year period** exceeding 50% of the pre-work valuation of the dwelling and attached
  garage.
- **Title 15 §1103.5.4** — scope: alteration of 50% or more of the building, work on 50% or more
  of the exterior, or an added story. One carve-out: work consisting only of the installation of
  fire-resistant siding.

**Why this matters on minor work:** the valuation trigger is cumulative. A series of small
permits inside three years reaches the 50% test even though no single permit comes close. Always
check the three-year permit history before clearing a minor permit as having no sprinkler
consequence, and say in the finding what history was checked.

A retrofit permit itself is designed to CRC §R309 or NFPA 13D and is a C-16 scope. The state
skill is explicit that there is no state retrofit trigger for an existing dwelling; in Laguna the
trigger is one of the two above.

### LB-4 — Planning route and coastal

- Match the current §25.05.040 closed lists. In-kind replacement takes Zone Clearance under
  §25.05.040(B)(2)(c); other non-major work no more than 15 ft ordinarily takes Zone Clearance
  under (B)(2)(a)-(b). Exterior work is **not** a default Design Review trigger — Urgency
  Ordinance No. 1732 repealed that default. The Director may refer a Zone Clearance or ADR
  project up (§25.05.040(A)(2)(d)).
- Item-specific routes that catch minor work: skylight without automatic night shade, ADR
  (B)(3)(a)(xii); door, window, siding or roofing change on a historic resource, ADR (B)(3)(a)(iv);
  any exterior work in an environmentally sensitive area (includes slopes of 30% or greater),
  Design Review (B)(1)(e) unless a peer-reviewed licensed professional finds no impact.
- Planning acts before Building issues for exterior work (§25.05.045(B)(3)); interior-only work is
  (B)(2)(d) and Building accepts it without a prior Planning record.
- Most of the city is in the Coastal Zone. On a single-family lot, minor work is normally an exempt
  improvement (§25.07.008(A)(1)) and like-for-like repair is exempt (§25.07.008(A)(3)). A change in
  appearance is not itself an exception; the exemption is lost in the listed cases (highly scenic
  area, ESA, within 50 ft of a bluff edge, prior CDP condition, and the first-road/300-ft strip
  triggers in (A)(1)(c)). A new detached shed in that strip is one of them.
- A building permit that is OTC-eligible is not thereby exempt from Design Review, Zone
  Clearance, or a CDP.

### LB-5 — Code cycle

Laguna is on the 2025 California codes for applications received on or after 2026-01-01; the
2022 cycle governs applications received on or before 2025-12-31. Use the building application
received date, never a planning filing date or an upload timestamp (`../city-reference/SKILL.md`
§"Building-application code-cycle table").

---

### City-overlay checklist

Walk these AFTER the state checklist. Record PASS / FAIL / FLAG / N/A with the section cited.

| # | Check | What to verify | Code section |
|---|---|---|---|
| LB-1 | OTC track | The scope matches a numbered OTC item, and no disqualifier applies. | `../city-reference/SKILL.md` §"Permit Processing Tracks" |
| LB-2 | Fire zone materials | Parcel fire-zone status from the adopted 2025 LRA map; exterior material complies, or the §14.70.015 same-material minor-repair exception is approved by the building official. | §14.70.030; §14.70.015 |
| LB-3 | Sprinkler retrofit triggers | Three-year cumulative valuation against Ch. 14.52.030, and the scope test under Title 15 §1103.5.4. | Ch. 14.52.030; Title 15 §1103.5.4 |
| LB-4 | Planning route | Zone Clearance, Administrative Design Review, or Design Review under the current §25.05.040 closed lists. | §25.05.040 |
| LB-5 | Coastal | Whether the work is development requiring a CDP, or is exempt. | Ch. 25.07 |
| LB-6 | Code cycle | Edition keyed to the building application received date. | `../city-reference/SKILL.md` cycle table |

---

### Key Laguna facts for minor work

- Minor plumbing, electrical and mechanical repairs and replacements are OTC item 9.
- A stucco or siding patch relies on the §14.70.015 same-material exception, and that needs the
  building official's approval.
- The sprinkler retrofit valuation trigger is **cumulative over three years** — the one rule most
  likely to be missed on a small permit.
- Most of the city is coastal; most of the city is in a fire hazard zone. Neither is optional.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope is minor** | ❌ **fail** | The described work fits a STEP 2 family and trips no STEP 1 trigger. Scope drives everything downstream, so a misread here is a FAIL, not a flag. | CRC R105.2, R105.2.2 |
| 6 | **Workers' compensation** | ❌ **fail** | A certificate on file, or the signed exemption declaration on the application. | CSLB licensing requirement |
| 8 | **Family requirements** | ❌ **fail** | The one or two state rules that still reach this scope (energy, safety glazing, water-conserving fixtures, sprinkler standard, hazmat). | see family |

### Checklist rows to place

These state rows have no current stage tag. For each one, decide from its text whether it is a plan-check item (and whether a miss is a correction or a flag) or an inspection item.

| # | Check | What to verify | Code |
|---|---|---|---|
| 2 | **Permit is actually required** | Work below the exemption thresholds needs no permit; say so rather than reviewing it. City thresholds are commonly lower than the state's. | CRC R105.2; CBC 105.2 |
| 3 | **Scope is described, not just labelled** | Location, quantity, and materials are on the application. "Repair as needed" is not a scope. | City intake practice |
| 4 | **Valuation is stated and plausible** | A dollar value is on the form and matches the described quantity. Valuation sets the fee and, in many cities, a cumulative sprinkler or upgrade trigger. | City fee schedule; city cumulative-valuation triggers |
| 5 | **Contractor licence** | An active CSLB licence in a classification that covers the work, or a valid owner-builder declaration on an owner-occupied dwelling where the owner performs the work. | B&P §7028, §7044 |
| 7 | **Code cycle** | Review against the edition in force for the application's received date, not today's edition. | CBSC cycle table |
| 9 | **Hazardous materials** | Pre-1978 paint disturbance (EPA RRP) or pre-1981 asbestos-suspect material: certification and work practices. FLAG for documentation; this is an EPA/Cal-OSHA overlay, not a building-department pass/fail. | 40 CFR 745; Cal/OSHA Title 8 §§1529, 1532.1 |
| 10 | **City overlay** | Fire hazard zone, coastal zone, historic status, and local exemption amendments reach even minor work. Always invoke the city skill. | city code |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/counter-administrative-check.md` — The Counter Check
- `references/escalation-triggers.md` — Escalation Triggers
- `references/minor-scope-families.md` — Minor Scope Families
- `references/permit-thresholds-exemptions.md` — When Minor Work Needs a Permit

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
