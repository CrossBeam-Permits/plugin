---
name: ltia-demolition
description: "LTIA Demolition permits in Laguna Beach, CA. Interior, non-structural demolition of a limited tenant improvement area, including asbestos abatement, with utilities capped and nothing structural removed. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions ltia demolition in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (CBC, Part 2), California Existing Building Code (CEBC, Part 10), California Electrical Code (CEC, Part 3), California Mechanical Code (CMC, Part 4), California Plumbing Code (CPC, Part 5), California Green Building Standards Code (CALGreen, Part 11)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — LTIA Demolition Permit

Handles ltia demolition permits in Laguna Beach end-to-end. Scope: Interior, non-structural demolition of a limited tenant improvement area, including asbestos abatement, with utilities capped and nothing structural removed.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a ltia demolition permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach LTIA Demolition Permit

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

This skill replaces the older generic `../demolition/SKILL.md` route for LTIA-style demolition scopes.

---

### Key Delta Summary

| Topic | State Default | Laguna Beach Override |
|---|---|---|
| City form | Varies | Laguna uses a **Demolition Notification** form from the Building Division |
| AQMD jurisdiction | Varies by air district | Laguna is in SCAQMD; city form states applicants must file SCAQMD asbestos demolition notification for **every demolition** |
| Definition emphasis | NESHAP/SCAQMD | City form says removal of even one load-bearing 2x4 can be demolition under Rule 1403 examples |
| Permit issuance | State baseline | Copy of 1403 Asbestos and/or 1403 Demolition online confirmation must be submitted to city before permit issuance when applicable; asbestos abatement certification required when applicable |
| Coastal zone | State Coastal Act | LBMC Section 25.07.006 defines development to include demolition; coastal-zone demolition requires CDP unless a specific exemption applies |
| Historic resources | LBMC Ch. 25.45; State CEQA baseline | Structures on the Laguna Beach Historic Register or Historic Inventory are flagged for Heritage/Historic review before demolition. Age alone does not trigger City heritage review. Whether CEQA needs a historic resource evaluation for an older unlisted structure is a Planning call: confirm with Planning at pre-application |
| Adjacent property | CBC baseline | Laguna Ch. 14.50 requires protection of adjoining property during demolition and 30-day certified notice for certain excavations near adjoining foundations |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Interior non-structural removal only | Confirm not a Rule 1403 demolition; still check asbestos/lead and waste diversion |
| Load-bearing member removal, structural demolition, or full/partial building demolition | City Demolition Notification + SCAQMD Rule 1403 path |
| Coastal-zone demolition | CDP analysis required before building/demolition permit issuance |
| Historic Register or Historic Inventory structure | Heritage/Historic review flag |
| Demolition with excavation deeper than adjoining foundation and close to property line | 30-day certified notice to adjacent owner before permit |

---

### Laguna-Specific Requirements

#### 1. Demolition Notification and SCAQMD Rule 1403

The city Demolition Notification form states that applicants must file with SCAQMD an asbestos demolition notification for **every demolition**. It defines demolition by reference to Rule 1403 as wrecking or taking out any load-supporting structural member, including foundation, roof support structures, exterior wall, related handling operations, or intentional burning.

Before permit issuance, require:

- Completed city Demolition Notification.
- SCAQMD Rule 1403 demolition notification confirmation, when applicable.
- SCAQMD Rule 1403 asbestos notification confirmation, when applicable.
- Asbestos abatement certification, when applicable.

#### 2. Coastal Development Permit

LBMC Section 25.07.006 defines development to include demolition and alteration of the size of a structure. LBMC Section 25.07.004 requires a CDP for development in the coastal zone unless exempt.

For Laguna coastal-zone demolition, do not say CDP is merely "likely." Treat CDP as required unless a specific Section 25.07.008 or 25.07.010 exemption/exclusion is identified and documented.

#### 2a. Planning Route (Ord. 1732, LBMC 25.05.040(B))

Source: the City source document (not included in this plugin).

- **Partial demolition that is not a major remodel:** Zone Clearance, 25.05.040(B)(2)(a) ("Demolition, alteration, or addition that does not constitute a major remodel").
- **Demolition that is part of a major remodel:** Design Review, (B)(1)(a). Major remodel test: `../residential-remodel/references/city-major-remodel-methodology.md`.
- **Removing a whole structure with nothing built in its place:** no list item clearly names it. **UNSETTLED; confirm with Planning at pre-application.**
- **Historic resource:** demolition goes through LBMC 25.45.014: Heritage Committee recommendation to the design review authority, a CDP, CEQA unless exempt, a 90-day waiting period with advertising, and findings before the demolition permit issues. Design Review of historic resources that does not qualify for administrative approval is (B)(1)(d).
- **Environmentally sensitive area** (includes slopes of 30% or greater): Design Review, (B)(1)(e), unless a peer-reviewed licensed professional finds no impact.
- Design Review is heard by the Design Review Board for single-family and two-family developments and by the Planning Commission otherwise (25.05.040(F)(1)).

#### 3. Historic and Heritage Review

Flag demolition for Planning/Historic review when:

- The structure is on the Laguna Beach Heritage Register or is otherwise a "historic resource" under LBMC 25.45 as amended by Ord. 1732 § 40: listed on the City, California or National Register, officially determined eligible, or one the City must treat as historic on substantial evidence. A missing recorded preservation agreement is not, on its own, proof a property is not on the City register (the City source document (not included in this plugin)).
- The structure is on the Historic Register or Historic Inventory and the application lacks a historic assessment.
- The project is in a historic district or affects a designated historic resource.

#### 4. Adjoining Property and Excavation Protection

Laguna Ch. 14.50 includes CBC 3307 protection requirements for adjoining public and private property during construction, remodeling, and demolition. If excavation will be deeper than adjoining walls/foundations and closer to the property line than the excavation depth, evidence of 30-day advance written notice by certified mail to adjacent property owners is required before permit issuance.

---

### Review Checklist - Laguna LTIA Demolition

| ID | Check | Pass Criteria |
|---|---|---|
| LB-DEMO-1 | City demolition form | Completed Laguna Demolition Notification included |
| LB-DEMO-2 | SCAQMD jurisdiction | Rule 1403 notification path used; not another air district |
| LB-DEMO-3 | Structural demolition classification | Load-bearing member removal identified and not misclassified as non-demolition |
| LB-DEMO-4 | Asbestos/abatement documentation | Rule 1403 confirmation and abatement certification included where applicable |
| LB-DEMO-5 | Coastal/CDP | Coastal-zone demolition has CDP or documented exemption |
| LB-DEMO-6 | Historic/heritage | Historic Register/Inventory status checked |
| LB-DEMO-7 | Adjacent property protection | CBC 3307 protection and 30-day excavation notice checked where applicable |
| LB-DEMO-8 | Utilities capped | Gas, electrical, water, sewer, and fire systems disconnected/capped per state skill and utility requirements |
| LB-DEMO-9 | Waste diversion | CALGreen/Green Halo construction and demolition waste path documented |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope is non-structural?** | ❌ **fail** | Plans clearly indicate ONLY non-load-bearing partitions are removed. No structural columns, load-bearing walls, shear walls, or exterior envelope work. Structural columns identified and marked for protection. | CEBC 701.2, 805.2, 805.3 |
| 2 | **Demolition plan complete?** | ⚠️ **flag** | Existing and demo floor plan shows all rooms, doors, demising walls. Demolition scope clearly indicated. Area of demolition stated in SF. Occupancy type listed per room. | CBC 3303.1, CEBC 601.2 |
| 3 | **Demising walls remain?** | ❌ **fail** | Walls between adjacent tenant spaces (fire partitions) are shown to remain. Fire-resistance rating noted. | CBC 708.1, 708.3 |
| 4 | **Fire separation walls shown?** | ❌ **fail** | Fire barriers, fire-rated corridors, and door ratings identified on plans. Penetrations through fire-rated assemblies will be firestopped. | CBC 707.1, 707.7, 714.2, 716.1 |
| 5 | **Egress path shown?** | ❌ **fail** | Egress path from tenant space to building exits clearly marked. All exit locations shown. Dead-end corridors comply with limits. | CBC 1003.6, 1020.5, 3303.3, 3310.2 |
| 6 | **Accessibility / path of travel shown?** | ⚠️ **flag** | Path of travel from public sidewalk/parking to tenant space shown. Main entrance, restrooms, drinking fountains identified. Note on plans that accessibility requirements will be maintained. | CBC 11B-206, 11B-207 |
| 7 | **Reflected ceiling plan (if applicable)?** | ⚠️ **flag** | If ceiling demolition is in scope, reflected ceiling plan provided showing items to be removed and items to remain (sprinklers, smoke detectors). | Standard practice |
| 8 | **Utility capping addressed?** | ❌ **fail** | Plans indicate that all electrical, plumbing, gas, and HVAC will be properly capped/disconnected. Note on plans: "All utility lines must be properly and safely capped as needed." | CBC 3303.6, CPC 1206.3 |
| 13 | **Waste diversion note on plans?** | ❌ **fail** | Plans include: "65% minimum of nonhazardous construction and demolition waste shall be recycled and/or salvaged for reuse." (CALGreen 5.408.1) | CALGreen 5.408.1 |
| 14 | **Lead/asbestos testing noted?** | ❌ **fail** | For buildings pre-1978: lead testing may be required. AQMD notification for asbestos prior to permit issuance. | State/federal hazmat regulations |
| 15 | **Universal waste addressed?** | ⚠️ **flag** | Fluorescent lamps, ballasts, mercury thermostats to be disposed as universal waste, not in general debris. | CALGreen 5.408.2 |
| 16 | **Required notes on plans?** | ⚠️ **flag** | General compliance note, fire/life safety/accessibility note, utility capping note, shoring note, waste diversion note, scope limitation note. | Various |
| 17 | **Shoring note present?** | ⚠️ **flag** | Plans include: "Contractor is responsible for all temporary shoring prior to the start of demolition." | Standard practice |
| 18 | **Door removal scope complete?** | ⚠️ **flag** | ALL doors and frames at demolition walls AND at walls slated to remain shall be removed (except exterior doors and doors required for egress or fire separation). This includes doors at non-demo partition walls within the tenant space. | Standard practice |
| 19 | **Site plan requirements met?** | ⚠️ **flag** | CBC 107.2.6 requires a site plan drawn to scale showing the size/location of new and existing construction, distances from lot lines, established street grades and proposed finished grades, and flood-hazard data where applicable; for demolition it must show construction to be removed and the location/size of construction to remain. Require easements, tenant-space location, access points, north arrow, fire-department access, or a hazardous-material inventory only from a named jurisdiction/agency and current checklist title with edition/effective date, exact locator, geography, project scope, and currency confirmation. | CBC 107.2.6; source-specific additions |
| 20 | **Post-demolition conditions addressed?** | ⚠️ **flag** | Plans address: contractor coordination with MEP trades and telecom prior to demo; field verification of conditions/dimensions before demo begins; patching/texturing/repair of surfaces where demo meets remaining construction; floors left clean and smooth; walls to receive tape and texture; objects protruding above slab verified and protected/removed/ground/capped; tenant space left broom clean. | Standard practice |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 9 | **Electrical tie-back to panels?** | Electrical components at removed fixtures/devices to be tied back to panels. Circuits de-energized and properly terminated. | CEC, CBC 3303.6 |
| 10 | **Gas piping capped gastight?** | Gas outlets capped with screw joint fittings, gastight. Branch valve shut off. | CPC 1206.3 |
| 11 | **Plumbing capped?** | Water supply lines capped at nearest valve. DWV connections capped/plugged. Plumbing stacks to be reused (not demolished). | CPC, CBC 3303.6 |
| 12 | **HVAC ducts capped?** | Open duct ends sealed. Fire/smoke dampers preserved. Shared ductwork maintained. | CMC, CBC 3303.6 |
| 21 | **Pre-existing penetrations addressed?** | Non-conforming penetrations through fire-rated assemblies discovered during demolition shall be firestopped with UL-approved materials per CBC 714. | CBC 714.2 |
| 22 | **Separate TI permit noted?** | Plans indicate that all tenant improvements shall be processed under a separate permit. No other improvements allowed under this permit. | Standard practice |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/accessibility-path-of-travel.md` — Accessibility & Path of Travel
- `references/demolition-safeguards-cbc3303.md` — CBC Chapter 33 & CEBC Chapter 15 -- Demolition Safeguards
- `references/egress-corridors-cbc1003-1020.md` — CBC Means of Egress & Corridors
- `references/existing-building-cebc-601-701.md` — CEBC -- Classification of Work & Alterations
- `references/fire-rated-assemblies-cbc707-714.md` — CBC Fire-Rated Assemblies -- Fire Barriers, Fire Partitions, Penetrations & Opening Protectives
- `references/plan-requirements-submittals.md` — LTIA Demolition -- Plan Submittal Requirements
- `references/scope-verification-structural.md` — Scope Verification -- Non-Structural Demolition Only
- `references/utility-capping-cpc-cmc-cec.md` — Utility Disconnection & Capping
- `references/waste-management-calgreen-5408.md` — CALGreen Section 5.408 -- Construction Waste Management

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
