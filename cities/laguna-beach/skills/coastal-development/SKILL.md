---
name: coastal-development
description: "Coastal Development Permit permits in Laguna Beach, CA. Work that needs a Coastal Development Permit in its own right. NOT ordinary building work that merely sits in the coastal zone. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions coastal development in Laguna Beach."
metadata:
  version: "2.0"
  source: "LBMC Ch. 25.07 (corpus codified through 2026-04-28); Urgency Ord. 1732 §§13-16 (25.07.006, 25.07.008(B), 25.07.012(J)-(K), 25.07.026) and 25.05.040; City CDP Application (March 2026); Coastal Commission report F9a (Nov. 2024); Gov. Code 66329"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Coastal Development Permit Permit

Handles coastal development permit permits in Laguna Beach end-to-end. Scope: Work that needs a Coastal Development Permit in its own right. NOT ordinary building work that merely sits in the coastal zone.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a coastal development permit permit, or (B) a city reviewer checking a submitted one?"

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
- **Coastal zone — most of the city.** Check the parcel against the City's coastal zone map before naming a Planning route. Report a parcel that straddles the boundary as straddling. Coastal Development Permit analysis: this skill.

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
## Ready to Submit — Laguna Beach Coastal Development Permit Permit

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
**This skill contains ONLY items where Laguna Beach differs from or adds to state Coastal Act requirements.**  
**All state coastal-development checklist items apply unless explicitly overridden below.**

For cross-cutting city info, see `../city-reference/SKILL.md`.

---

### Key Delta Summary

| Topic | State / Default | Laguna Beach Override |
|---|---|---|
| CDP trigger | Coastal Act requires CDP for development in coastal zone unless exempt | LBMC Section 25.07.004 requires a CDP for **all proposed development within the coastal zone** unless specifically exempted by Sections 25.07.008 or 25.07.010 |
| Local issuer | Certified LCP city may issue CDPs | City generally considers and issues CDPs, but some areas retain Coastal Commission initial jurisdiction |
| Retained CCC areas | Varies | City CDP application identifies Blue Lagoon, Lower Irvine Cove, and Three Arch Bay as areas where CCC retains jurisdiction over development |
| Appealable development | PRC Section 30603 | LBMC Section 25.07.006 defines appealable areas: between sea and first public road, within 300 ft of beach/mean high tide line, within 100 ft of wetland/estuary/stream, within 300 ft of coastal bluff top, plus major public works/energy facilities |
| SFR improvements | Often exempt, with state exceptions | LBMC Section 25.07.008(A)(1) normally exempts SFR improvements, including pools, fences, storage sheds, and landscaping, but the local exception list is broad and must be checked before clearing the exemption |
| Building permit sequencing | Development cannot start before CDP effective | Building permit review may proceed, but work cannot start until CDP appeal periods expire or appeals are exhausted per LBMC Section 25.07.016 |
| Public Permit Portal | Local procedure | March 2026 city CDP application requires new CDP applications through the Public Permit Portal |

---

### Decision Tree Router

#### STEP 1 - Is the parcel in the Coastal Zone?

Most of Laguna Beach is in the coastal zone. If parcel status is unknown, ask the applicant or require city/CCC confirmation. Do not assume a parcel is outside the coastal zone from address alone.

- **In coastal zone:** Continue to Step 2.
- **Outside coastal zone:** CDP skill does not apply; still apply zoning, WUI, geotech, and flood rules.
- **Unknown:** Flag `ask_the_city` and request Planning Division confirmation.

#### STEP 2 - Is the development in a retained Coastal Commission jurisdiction area?

The city CDP application states that in certain areas, including **Blue Lagoon, Lower Irvine Cove, and Three Arch Bay**, the California Coastal Commission retains jurisdiction over development, including initial CDP consideration.

- If retained CCC jurisdiction applies, route applicant to Coastal Commission first.
- Otherwise, Laguna Beach is the local CDP issuer under its certified LCP.

#### STEP 3 - Does a local exemption clearly apply?

Use LBMC Section 25.07.008. Do not stop at "SFR improvement" without checking the exception list.

Common SFR improvements normally associated with a dwelling can be exempt, including garages, swimming pools, fences, storage sheds, and landscaping, **unless** one of the local exceptions applies:

- Located on a beach, in a wetland or stream, seaward of mean high tide, within 50 ft of coastal bluff edge, in ESA, or in a highly scenic area.
- Located between sea and first public road, or within 300 ft of beach/mean high tide line, and the work causes a 10% or greater floor-area increase, 10% or greater height increase, or establishes a detached structure.
- Expansion or construction of a water well or septic system.
- Major water-using development, including swimming pools or landscaping irrigation, in an area the Coastal Commission has found has critically short water supply.
- A prior CDP condition says future improvements require a CDP.
- Significant landform alteration or vegetation removal in protected coastal resource areas.

If any exception applies or cannot be ruled out, flag CDP review.

Scope notes:

- The 10% floor-area, 10% height and detached-structure items apply **only** in the strip between the sea and the first public road, or within 300 ft of the beach or mean high tide line (§25.07.008(A)(1)(c)). Outside that strip they do not remove the exemption.
- "Highly scenic" means designated highly scenic in the certified Land Use Plan (§25.07.008(A)(1)(b)). No map of those areas is in the corpus. When it matters, return UNSETTLED and confirm with Planning at pre-application.
- UNSETTLED: Ord. 1732 added "slopes of 30% or greater" to the 25.08 definition of environmentally sensitive area. Ord. 1732 is not certified. Whether a steep lot is in an "environmentally sensitive area" for §25.07.008(A)(1)(b) is not decided; confirm with Planning at pre-application.
- A major remodel is not an "improvement": the October 2026 Major Remodel Quick Guide classifies it as new development, and §25.56.011 makes it a new building. Treat it as needing a CDP (detail: `../residential-remodel/references/city-cdp-coastal-zone.md`).
- An ADU is exempt only when the application converts existing livable space inside the primary dwelling (§25.07.008(A)(1)(a); Ord. 1713, LBMC 25.17.010(d)(1)(C)(ii)). See `../adu/SKILL.md`.

#### STEP 3a - Does the E-93-1 categorical exclusion apply?

Section 25.07.010 exempts development in a categorical exclusion area, except for the notice requirements of 14 CCR §13248. Categorical Exclusion Order E-93-1 covers "single family residential development" in eleven areas. Its Special Condition 8 requires conformity with the LCP or the order, whichever is more restrictive. In the Commission report F9a (Nov. 2024), the Executive Director found the LCP exemption list (§25.07.008) controls for an ADU added to a house (the City source document (not included in this plugin)).

- ADU in an exclusion area: E-93-1 does not clear it.
- Single-family remodel or accessory structure in an exclusion area: apply the stricter of §25.07.008 and the order. If §25.07.008 exempts the work, it is exempt either way. If not, whether E-93-1 clears it is UNSETTLED; confirm with Planning at pre-application.
- New house or major remodel in an exclusion area: UNSETTLED; confirm with Planning at pre-application.

#### STEP 4 - Is the project appealable?

Apply LBMC Section 25.07.006:

| Location / Scope | Result |
|---|---|
| Between sea and first public road paralleling the sea | Appealable |
| Within 300 ft of inland extent of beach or mean high tide line | Appealable |
| Within 100 ft of wetland, estuary, or stream | Appealable |
| Within 300 ft of top of seaward face of coastal bluff | Appealable |
| Major public works or major energy facility | Appealable |

For appealable CDPs, local decision finality depends on Coastal Commission notice and the Commission appeal window.

**ADU-only CDP.** A City CDP that covers only an ADU is decided within 60 days, concurrently with the ADU; no hearing is required; it is not appealable to the Coastal Commission even in the appealable area (Gov. Code 66329(a), (c); City ADU & JADU Application, footnote 4). A CDP that also covers other development follows this step.

#### STEP 5 - Which kind of CDP, and who decides?

| Kind | When | Decider | Source |
|---|---|---|---|
| De minimis waiver | Not appealable, not in an appeal area, no local hearing required, no possible adverse effect on coastal resources, no violation; not when there is known opposition or an LCP-conformity question | Director, written waiver; reported to City Council, which can void it | §25.07.009 |
| Administrative CDP | "Minor development": consistent with the LCP, needs no discretionary approval other than the CDP, no adverse effect | Director; hearing only if requested within 15 working days of notice | §25.07.013 |
| CDP with other permits | Project also needs Design Review, a variance, a CUP, etc. | The same body as the other permit, at the same time | §25.07.012(D) |
| CDP alone | Only a CDP is needed and it is not de minimis or minor | Director, at a public hearing | §25.07.012(D) |

- When Design Review goes with the CDP, the Design Review body (the DRB for single-family and two-family projects, the Planning Commission otherwise, §25.05.040(F)(1)) also makes the CDP findings in §25.07.012(F)-(G) (§25.05.040(F)(3)-(4)). CDP notice follows §25.07.014 instead of §25.05.065 (§25.05.040(E)).
- A Zone Clearance or Administrative Design Review project "may still require a Coastal Development Permit" (§25.05.040(A)(2)(e); §25.05.045(C)(4)). A Zone Clearance does not clear the CDP question.

#### STEP 6 - Ord. 1732 changes to Chapter 25.07 (not yet certified)

Urgency Ord. 1732 (effective 2026-07-22) amended Chapter 25.07. These amendments, like the rest of Ord. 1732, are not certified by the Coastal Commission; the City Council adopted a resubmittal resolution on 2026-09-22. Whether they bind a CDP before certification is UNSETTLED; confirm with Planning at pre-application.

- §25.07.008(B): the record of exemptions is kept on the City's website; exemptions for appealable development are reported to the Commission's Executive Director within 7 calendar days.
- §25.07.012(J): changes to an approved CDP. The Director may approve minor changes without a hearing only if they are consistent with the LCP, do not touch a feature that was a basis for the environmental finding or a condition, do not expand the use, and do not alter the §25.07.012(G) findings. Other changes go back to the original review authority on a new application. Commission-issued CDPs are amended by the Commission.
- §25.07.012(K): CDP staking. Poles and ribbons showing the full structure, including decks and eaves, in place and surveyor-certified at least 21 calendar days before the first public hearing; re-staked at least 14 days before a later hearing if required; removed within 20 days after the final decision. The Director may waive staking in writing.
- §25.07.006: adds a definition of "Director of Community Development" (includes a designee).
- §25.07.026: LCP amendment procedure repealed and replaced.

Source: the City source document (not included in this plugin) (Sections 13-16; signed Ord. 1732 controls).

---

### Review Checklist - Laguna CDP

| ID | Check | Pass Criteria |
|---|---|---|
| LB-CDP-1 | Coastal zone status verified | Parcel confirmed in/out of coastal zone by city/CCC source, not guessed |
| LB-CDP-2 | CCC-retained area checked | Blue Lagoon, Lower Irvine Cove, Three Arch Bay, or other retained-jurisdiction area ruled out or routed to CCC |
| LB-CDP-3 | Development definition applied | Scope checked against LBMC Section 25.07.006, including construction, demolition, alteration, grading, utility work, vegetation removal, and intensity changes |
| LB-CDP-4 | Exemption support documented | If claiming exemption, cite the exact Section 25.07.008 exemption and explain why no exception applies |
| LB-CDP-5 | SFR exception traps checked | Bluff, beach, wetland/stream, ESA, highly scenic, appealable-area 10% triggers, detached structures, prior CDP conditions, and landform/vegetation alteration checked |
| LB-CDP-6 | Appealable status determined | Section 25.07.006 appealable area and major public works/energy facility triggers checked |
| LB-CDP-7 | Portal/application package complete | March 2026 CDP application package submitted through Public Permit Portal with required plan sheets and project summary table |
| LB-CDP-8 | Notice/appeal timing respected | Development does not commence until local and CCC appeal periods expire or appeals are exhausted |
| LB-CDP-9 | Other entitlements sequenced | Design Review, variance, zoning plan check, floodplain, bluff/geotech, and building permit conditions are coordinated with CDP; CDP decided by the same body as Design Review (§25.07.012(D)) |
| LB-CDP-10 | Categorical exclusion checked | E-93-1 area: ADU never cleared; other single-family work per Step 3a, UNSETTLED items flagged |
| LB-CDP-11 | CDP type identified | De minimis waiver, administrative, or regular CDP (Step 5); ADU-only CDP on the 66329 track |
| LB-CDP-12 | Staking | If a CDP hearing is held: §25.07.012(K) staking 21 days before (Ord. 1732, uncertified) unless waived in writing |

---

### Common Agent Errors to Avoid

- Do not say "most Laguna projects need a CDP" as a final answer. Run the exemption and exception analysis.
- Do not clear SFR pools, fences, sheds, or landscaping solely because they are SFR improvements. Laguna's exception list is broad.
- Do not treat an exempt building permit as exempt from CDP recordkeeping. LBMC Section 25.07.014(A) requires the city to maintain records for exempt development.
- Do not tell the applicant to start work after city approval if the CDP is appealable. Wait for appeal periods to expire or appeals to be exhausted.
- Do not route Blue Lagoon, Lower Irvine Cove, or Three Arch Bay CDPs to the city without confirming retained CCC jurisdiction.
- Do not apply the §25.07.008(A)(1)(c) 10% items outside the first-road/300-ft strip.
- Do not tell a resident E-93-1 clears an ADU.
- Do not treat a Zone Clearance stamp as a CDP exemption. Planning records the exemption separately (§25.07.008(B)).

---

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/appealable-areas.md` — Appealable Development Areas
- `references/categorical-exclusions.md` — Categorical Exclusions (PRC §30610(e), 14 CCR §13240-13249)
- `references/cdp-appeals.md` — CDP Appeals to the Coastal Commission
- `references/cdp-process.md` — CDP Application and Review Process
- `references/cdp-when-required.md` — When a CDP Is Required (PRC §30600, §30610)
- `references/definitions.md` — Key Definitions
- `references/lcp-overview.md` — Local Coastal Programs (LCPs)
- `references/resource-protection-access.md` — Public Access Policies (PRC §30210-30214)
- `references/resource-protection-agriculture.md` — Agricultural Land Policies (PRC §30241-30244)
- `references/resource-protection-landforms.md` — Coastal Bluffs, Hazards, and Erosion (PRC §30235, §30236, §30253, §30270)
- `references/resource-protection-marine.md` — Marine Resources, ESHA, and Wetlands (PRC §30230-30240)
- `references/resource-protection-recreation.md` — Recreation and Visitor-Serving Policies (PRC §30220-30224)
- `references/resource-protection-scenic.md` — Scenic and Visual Resource Policies (PRC §30251-30253)

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
