---
name: adu
description: "ADU (Accessory Dwelling Unit) permits in Laguna Beach, CA. A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions adu in Laguna Beach."
metadata:
  version: "2.0"
  source: "HCD ADU Handbook, January 2025 (54 pages) + January 2026 Addendum (pages 55-58); Urgency Ord. 1713 (adopted 2025-03-11; LBMC 25.17.010, 25.17.020); certified LCP Chapter 25.17 (Ord. 1687 and 1691, certified 2023-09-07); LBMC Ch. 25.07 (CDPs); Urgency Ord. 1732 (LBMC 25.05.040, 25.05.045, 25.08 ESA definition); City ADU & JADU Application (Updated August 2026); Coastal Commission report F9a, Nov. 2024; Gov. Code 66317, 66329"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — ADU (Accessory Dwelling Unit) Permit

Handles adu (accessory dwelling unit) permits in Laguna Beach end-to-end. Scope: A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a adu (accessory dwelling unit) permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. This skill carries the Laguna Beach layer: the City rules, the City submittal checklists and the filing steps. California code compliance comes from the CrossBeam connector (see **California Code Compliance** below).

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

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the Laguna Beach rules and the City submittal checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and the City submittal checklists using the user's answers. When a plan set exists, run the plan-set check (`../plan-set-check/SKILL.md`). For California code compliance, follow **California Code Compliance** below. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on
- **NOT CHECKED** → a California code item with no CrossBeam result: say so, and recommend a CrossBeam check before filing

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach ADU (Accessory Dwelling Unit) Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]
**California code compliance:** [CrossBeam result, or "not checked: run a CrossBeam check before filing"]

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
3. Walk the Laguna Beach rules and the City submittal checklists, in order. Get California code compliance as **California Code Compliance** below says
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

⛔ NOT CHECKED — California code compliance [unless a CrossBeam result covers it]

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Without a CrossBeam result, the verdict covers the Laguna Beach rules and the City checklists only. Say so beside it, and never call the set compliant with the California codes.

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides California law, which comes from the CrossBeam connector. Paths are relative to this file.

**Base skill:** the California ADU (Accessory Dwelling Unit) rules, which come from the CrossBeam connector (see "California Code Compliance" below)
**This skill contains ONLY items where Laguna Beach differs from state law.**
**All state checklist items apply unless explicitly overridden below.** State-law procedure (15-business-day completeness check, 60-day clock, deemed approval, ADU-only CDP rules in Gov. Code 66329) lives in the state skill: the California ADU (Accessory Dwelling Unit) rules (Permit Process — Ministerial Review, Timelines, and Deemed Approval), which come from the CrossBeam connector (see "California Code Compliance" below) and the California ADU (Accessory Dwelling Unit) rules (Hazard Zones — Fire, Coastal, and Environmental Constraints), which come from the CrossBeam connector (see "California Code Compliance" below).

Laguna ADUs are harder than in most California cities. Most of the city is in the coastal zone, so most new ADUs need a Coastal Development Permit (CDP), and two different versions of Chapter 25.17 are in play at once.

---

### STEP 0: Which Chapter 25.17 applies (read first)

| Text | Status as of 2026-10-10 | Use it for | Source |
|---|---|---|---|
| **Urgency Ord. 1713** (sections 25.17.010 and 25.17.020) | In force. Applies to applications that include an ADU or JADU filed on or after March 12, 2025. eCode360 lists it "Expires December 9, 2026". Not certified by the Coastal Commission. | The local ADU permit: approval path, local standards, process | the City source document (not included in this plugin); City ADU & JADU Application (Aug. 2026), footnote 3: "As of March 2025, LBMC Chapter 25.17 is replaced by Urgency Ordinance No. 1713." |
| **Certified LCP Chapter 25.17** (Ord. 1687 and 1691; sections 25.17.010-25.17.110) | Certified 2023-09-07. Still the text eCode360 shows. | The LCP-conformity finding for an ADU that needs a CDP | the City source document (not included in this plugin); the City source document (not included in this plugin) |
| Urgency Ord. 1707 / 1709 | Applied to ADU applications filed 12/11/2024-1/14/2025 (1707) and 1/1/2025-3/11/2025 (1709) | Older applications only | eCode360 editor's note, recorded in the Ord. 1713 file |
| **Ord. 1715** (permanent replacement, adopted 2025-03-25) | NOT certified. Pending as LCP-5-LGB-25-0036-1; on the October 2026 Commission agenda (item 17b) and postponed | Nothing yet | the City source document (not included in this plugin) |

- Ord. 1713 renumbers the chapter. Cite 25.17.010(a)-(j) and 25.17.020(a)-(d). Do not cite the certified section numbers (25.17.030, 25.17.040, 25.17.050) as the local rule.
- Ord. 1730 and Ord. 1732 do not amend Chapter 25.17.
- **UNSETTLED:** which ADU rules apply to an application filed after December 9, 2026, or after Ord. 1715 is certified. Confirm with Planning at pre-application.

Full standards for both texts: `references/city-adu-ordinance.md`.

---

### STEP 1: Does the ADU need a CDP?

An ADU or JADU application "is considered 'development' under LBMC Chapter 25.07" (25.17.010(d)(1)(C)(i)). In the coastal zone, a CDP is required unless an exemption applies.

Nearly all of Laguna is in the coastal zone: "Only the 522-acre Sycamore Hills area within the City is excluded" (certified Land Use Element). Treat the parcel as coastal unless `lookup_property` says otherwise; do not branch the answer on "if outside the coastal zone".

| Project | CDP? | Source |
|---|---|---|
| Not in the coastal zone | No | 25.07.004 |
| Coastal zone. Application **only** converts existing livable space in a legally established primary dwelling into an ADU or a JADU | No, exempt (but see the loss rules below) | 25.17.010(d)(1)(C)(ii); 25.07.008(A)(1)(a) |
| Coastal zone. New detached or attached ADU, or an addition | **Yes** | 25.17.010(d)(1)(C)(iii) |
| Coastal zone. Garage, accessory structure, or other non-habitable space converted to an ADU or JADU | **Yes.** A garage is not "habitable area" under 25.07.008(A)(1)(a) | 25.07.008(A)(1)(a) |
| Coastal zone, inside a Categorical Exclusion Order E-93-1 area | Yes, the same as above. E-93-1 does not clear an ADU; the LCP exemption list controls | Coastal Commission report F9a, Nov. 2024 (the City source document (not included in this plugin)) |
| Blue Lagoon, Lower Irvine Cove, Three Arch Bay | Apply to the Coastal Commission directly | City ADU & JADU Application, footnote 4 |

A JADU is **not** always exempt. Only a JADU that converts existing livable space is exempt. A JADU in an attached garage needs a CDP.

**When a conversion loses the exemption.** The exemption is part of 25.07.008(A)(1), which does not apply when the improvement is "classified as one of the following". Check each:

- (b) The structure or the improvement is on a beach, in a wetland or stream, seaward of the mean high tide line, within 50 ft of a coastal bluff edge, in an environmentally sensitive area, or in an area designated highly scenic in the certified Land Use Plan.
- (c) **Only** where the structure or improvement is between the sea and the first public road paralleling the sea, or within 300 ft of the inland extent of any beach (or of the mean high tide line where there is no beach): a 10% or greater increase in internal floor area (cumulative over time), a height increase of more than 10%, or a new detached structure. Outside that strip, (c) does not apply.
- (d) Expansion or construction of a water well or septic system.
- (e) Improvements in a Commission-designated critically short water supply area.
- (f) A prior CDP for the structure says future improvements need a CDP.
- (g) Significant landform alteration or vegetation removal on a beach, wetland or dune, within 50 ft of a bluff edge or stream, or in natural vegetation or another ESA.

Where any item applies or cannot be ruled out, return FLAG and require a Planning CDP determination.

**UNSETTLED:** Ord. 1732 added "slopes of 30% or greater" to the 25.08 definition of environmentally sensitive area. Ord. 1732 is not certified by the Coastal Commission. Whether a conversion on a lot sloped 30% or more loses the 25.07.008(A)(1)(b) exemption is not decided. Confirm with Planning at pre-application.

---

### STEP 2: Which approval path (25.17.010(d))

| Path | When | Approval | Standards that apply |
|---|---|---|---|
| **(d)(1) CDP** | A CDP is required under Step 1 | CDP under Ch. 25.07, decided with the ADU application | 25.17.020 plus the certified LCP. See Step 4 for the open question on (f) and (g) |
| **(d)(2) Building permit only** | No CDP, the ADU meets (f), and it fits one of four scenarios | Building permit only | (f) |
| **(d)(3) ADU permit** | No CDP, and not a (d)(2) scenario | ADU permit plus building permit | (f) and (g) |

The four (d)(2) scenarios:

- (A) **Converted, single-family lot.** One ADU and one JADU within the space of a proposed or existing single-family dwelling, or (ADU only) within an existing accessory structure plus up to 150 sf for ingress and egress. Independent exterior access; side and rear setbacks sufficient for fire and safety.
- (B) **Limited detached, single-family lot: the guaranteed 800 sf path.** One new detached ADU with side and rear setbacks of at least 4 ft, total floor area of 800 sf or less, and peak height within (f)(2). This path needs no ADU permit and no (g) standards.
- (C) **Converted, multifamily lot.** ADUs in non-livable space of existing multifamily structures, at least one and up to 25% of the existing units.
- (D) **Limited detached, multifamily lot.** Up to two detached ADUs with 4 ft side and rear setbacks and (f)(2) height.

**Two or more detached houses on one lot** (for example an R-2 lot with two detached single-family dwellings). Ord. 1713 defines "multifamily dwelling" as "a structure with two or more attached primary dwellings on a single lot" (25.17.010(c)(8)), so the lot fits neither the single-family scenarios as written nor (C)/(D). Do not force-fit a (d)(2) scenario: use (d)(3) (ADU permit) when no CDP is needed and (d)(1) when one is. In the coastal zone, improvements to a non-single-family property are exempt only without a change in intensity of use (25.07.008(A)(2)), and a new unit adds intensity; expect a CDP unless the conversion exemption applies (Step 1). City practice on such a lot: the ADU's CDP is usually administrative when nothing else needs a hearing, and staff may open an ADR record beside the ADU without stating why, likely for the non-ADU pieces (parking, site work); the ADU itself stays ministerial (a CrossBeam reference that is not included in this plugin Step 4h). UNSETTLED; confirm with Planning at pre-application.

Because (d)(2) and (d)(3) both require "no CDP", a new detached ADU in the coastal zone cannot use the 800 sf path. It goes through (d)(1).

For a (d)(3) ADU permit, (g)(1)(C) also guarantees size: no percent-of-primary limit and no front setback "may require the ADU to be less than 800 square feet."

---

### STEP 3: Process

**ADU without a CDP.** Decided ministerially, "without discretionary review or a hearing" (25.17.010(e)(2)(A)). The 60-day rule and its exceptions are state law (state skill). Laguna-specific points:

- The City may delay the ADU decision only when the ADU "is submitted with a permit application to create a new single-family or multifamily dwelling on the lot" (25.17.010(e)(2)(B)(ii)). A remodel or an addition is not a new dwelling. The ADU's clock runs even if the remodel goes to a hearing.
- A demolition permit for a detached garage replaced by an ADU is reviewed and issued with the ADU (25.17.010(e)(2)(D)).
- A denial must list every deficiency and how to fix it, within the 60 days (25.17.010(e)(2)(C)).

**ADU with a CDP.**

- Each ADU CDP "is processed in accordance with LBMC chapter 25.07" (25.17.010(e)(1)) as de minimis development, minor development under 25.07.013, or regular development under 25.07.012 (25.17.010(d)(1)(C)(iii)). Ord. 1713 cites "25.07.008" for de minimis; the de minimis waiver itself is 25.07.009. Planning picks the type. City practice since Ord. 1732: an ADU filed alone usually gets an **Administrative CDP** under 25.07.013 (Director decides; hearing only if someone asks within 15 working days of the notice), sometimes a waiver. When the ADU is filed with other work that needs ADR or Design Review, the body hearing that work (the Director at ADR; the DRB or Planning Commission at Design Review) decides the ADU's CDP with the project (25.07.012(D)). Method: a CrossBeam reference that is not included in this plugin, "Picking the kind for a project with an ADU". Procedures: `references/city-coastal-permits.md`.
- Ord. 1713 lets the City "elect to hold public hearings" on an ADU CDP (25.17.010(d)(1)(A)). The state floor still applies: decision within 60 days, concurrent with the ADU, no hearing required, and the local decision is not appealable to the Coastal Commission (Gov. Code 66329(a), (c); state skill).
- Local appeals follow Chapters 25.07 and 25.05 (25.17.010(d)(1)(C)(iv); 25.05.070).
- The City ADU & JADU Application requires the CDP Application to be "processed concurrently with this ADU/JADU Application".
- **ADU with other work that needs ADR or Design Review: lead with one CDP decided by that hearing body.** The CDP is "processed concurrently" with the other permits and "the approving body for the coastal development permit shall be the same as that for the permit required by the underlying zoning district" (25.07.012(D)); City practice matches (above). That combined CDP follows the normal Chapter 25.07 procedure and appeal area. The alternative: a CDP that covers only the ADU keeps the 66329 track (60 days, no hearing required, no Commission appeal). The applicant may ask Planning at pre-application to file it separately; Planning decides. Give it second, not as an equal branch.
- CDP findings look at LCP conformity and coastal resources. Public views count; private views do not (PRC 30251; `references/city-adu-faq.md`). Opposition to the ADU itself is not a ground for denial.

**Fees.** Do not quote dollar amounts. Use the fee tool (`estimate_fees`, Master Fee Schedule). Impact-fee limits are state law.

---

### STEP 4: Which text binds a CDP ADU (settled by 25.17.010(d)(1)(B))

A coastal ADU that needs a CDP is reviewed as an ADU and as coastal development. The text says which standards bind it:

- "When an ADU or JADU requires a coastal development permit under the City's certified Local Coastal Program ("LCP"), including this chapter, the ADU or JADU must comply with the requirements of the City's certified LCP" (25.17.010(d)(1)(B), Ord. 1713).
- "No ADU or JADU may cause a violation of any provision in the certified LCP" (25.17.020(d)(1)). A CDP needs a finding of conformity with the certified LCP (25.07.012(G)(1)). The certified Chapter 25.17 is the Ord. 1687/1691 text, not Ord. 1713.
- Ord. 1713 (f) covers ADUs "approved under subsections (d)(2) or (d)(3)", and (g) applies "only to ADUs that require an ADU permit under subsection (d)(3)". A CDP ADU is approved under (d)(1).

So:

1. **CDP ADU:** apply the certified 25.17.040 limits (height (D)(4) and (E)(2), size (D)(1), outdoor living (E)(5)(c), parking (E)(6)) plus every Ord. 1713 25.17.020 rule (it applies by its own terms, 25.17.020(a)). **Height of a detached CDP ADU is the certified (D)(4) limit (16 ft; 18 ft near major transit, plus 2 ft to match the roof pitch; 18 ft on a multistory multifamily lot), not a lower zone or specific-plan building height:** "In the event of a conflict between the development standards set forth in the zone and the standards of this chapter, the provisions of this chapter shall take precedence" (certified 25.17.030(D)). Only an attached ADU takes the zone's limit, because (D)(4)(d) names it: "25 feet or the zoning code height limitation applicable to the primary dwelling, whichever is lower". Ord. 1713 (f)/(g) limits outside 25.17.020 do not bind it; if Planning applies one anyway, FLAG it, do not FAIL.
2. **ADU with no CDP:** Ord. 1713 only.
3. **Still open:** a certified limit below the state floor (Gov. Code 66329(a) keeps the Coastal Act in force; whether a limit that does not carry out the Coastal Act survives is a state-law question; FLAG, do not FAIL), and how the City reads a topic where both texts bind and differ (meet both). Confirm with Planning at pre-application.

The differences, and the over-height route: `references/city-adu-ordinance.md` → Part D.

---

### STEP 5: Laguna coastal ADU standards (25.17.020)

These apply to every ADU and JADU in the coastal zone that does not qualify for the conversion exemption (25.17.020(a)). More restrictive standards may be imposed to protect coastal resources, including hazardous areas, ESAs, wetlands, public views, and trails (25.17.020(b)).

| # | Standard | Rule | Source |
|---|---|---|---|
| 1 | Front setback | The underlying zone's front setback | 25.17.020(c)(1)(A) |
| 2 | Additional front and rear setback | 25.50.004(D) additional building setback | 25.17.020(c)(1)(B) |
| 3 | Bluff | 25 ft minimum from the top of an oceanfront bluff | 25.17.020(c)(1)(C) |
| 4 | Watercourse | 25 ft from the centerline; 25 ft from top of bank for a USGS blue-line stream | 25.17.020(c)(1)(D) |
| 5 | Replacement parking | **Required for every ADU or JADU that needs a CDP**, a garage conversion included. Garage, carport or covered parking demolished or converted: reviewed with the ADU; "The number of existing parking spaces for a single-family or multifamily dwelling must be replaced on-site at a one-to-one ratio", not more than the dwelling's required minimum ((c)(2)(A)(ii)). May be uncovered, tandem, or in a setback (not a bluff or watercourse setback) if at least 3 ft from every property line. Entirely on private property and not in a required turnaround. State-law note below | 25.17.020(c)(2)(A); 25.17.010(g)(4)(C); certified 25.17.040(E)(6)(a) |
| 6 | **Firefighter access path** | "An all-weather firefighter access path must be provided from the right-of-way to the front door of the ADU or JADU. The access must be a minimum of 3 feet wide and non-combustible. Stairs must be provided for any slope greater than 10 percent." | 25.17.020(c)(3) |
| 7 | Vehicular access | Use the primary dwelling's access unless Fire and Public Works find secondary access will not degrade safety or traffic. New vehicular access is subject to discretionary design review (Design Review under 25.05.040(B)(1)(k)) | 25.17.020(c)(4) |
| 8 | Outdoor living space | Covered porches, decks, patios and other outdoor living spaces attached to an ADU meet the ADU's height and setbacks. **CDP ADU:** also "limited to 20% maximum floor area of the ADU" (certified LCP, which binds it under 25.17.010(d)(1)(B); our reading counts a loft in that floor area, Step 7 row 6c) | 25.17.020(c)(5)(A); certified 25.17.040(E)(5)(c) |
| 9 | Roof decks | **Prohibited on any coastal-zone ADU or JADU that needs a CDP.** A roof deck is "a deck above the uppermost story of a building, with no access from interior living space at the same floor level". A deck on the ADU roof reached only by an exterior stair, or from the floor below, is a roof deck and is barred. A deck at the same level as interior living space with direct access from it is not a roof deck (it is outdoor living space, row 8). The certified LCP also prohibits roof decks (25.17.040(E)(5)(c)) | 25.17.020(c)(5)(B) |
| 10 | Major remodel | ADUs do not count toward the major-remodel calculation, "except as necessary to comply with section 30253 of the Coastal Act limiting alterations of existing bluff top, beachfront, and coastal canyons" | 25.17.020(d)(2) |

**Replacement parking: the City rule turns on the CDP.** Ord. 1713 waives replacement only for an ADU that needs no CDP: demolished or converted spaces "are not required to be replaced. For clarity, this paragraph does not apply to an ADU or JADU that requires a CDP" (25.17.010(g)(4)(C)). For an ADU or JADU that needs a CDP (a garage or other non-habitable conversion, a new ADU, an addition; STEP 1), the coastal standards apply by their own terms (25.17.020(a)) and the existing spaces "must be replaced on-site at a one-to-one ratio" (25.17.020(c)(2)(A)(ii)); the certified LCP says the same (25.17.040(E)(6)(a)). Lead with that: a garage conversion that needs a CDP must replace the garage's spaces 1:1 on site, up to the dwelling's required minimum, uncovered or tandem allowed. Review it as a requirement: missing replacement parking on a CDP ADU is a correction.

State-law note (one line in an answer): Gov. Code 66314(d)(11) bars requiring replacement of parking demolished for or converted to an ADU, but the ADU article does not "supersede or in any way alter or lessen the effect or application of the California Coastal Act" (66329(a)); an applicant may argue the rule is not needed to carry out the Coastal Act, which is a challenge to raise with Planning, not the default answer. Detail: `references/city-coastal-permits.md`, "Replacement parking".

---

### STEP 6: Planning route under Ord. 1732

- **Zone Clearance:** 25.05.040(B)(2)(h), "Accessory dwelling units, only as set forth in Chapter 25.17" (procedure in 25.05.045). The new-building Design Review item excludes ADUs: (B)(1)(b) "All new buildings, except as otherwise provided in Section 25.05.040(B)(2) relating to ADUs".
- File the City's ADU & JADU Application. "Additional applications are required when an applicant is requesting additional entitlements, such as a Coastal Development Permit or a permit for Design Review."
- Other parts of the project keep their own list item. Grading over 20 cubic yards outside the footprint: Design Review (B)(1)(f). Retaining wall over 5 ft exposed: Design Review (B)(1)(g). New vehicular access or driveway widening: Design Review (B)(1)(k). Decks: the one rule below. Added covered or tandem parking: ADR (B)(3)(a)(vi). Equipment failing 7.25.130(C): ADR (B)(3)(a)(v). So an ADU project can carry an ADR or Design Review application beside the ADU application; never say flatly "no Design Review" for the whole project.
- **Decks with an ADU: one rule.** A deck is its own piece; the ADU stays on the ADU application. In the Coastal Zone, every deck attached to the ADU meets the ADU's height and setbacks (25.17.020(a), (c)(5)(A)). Then, in order:
  1. **Is it allowed?** In the coastal zone on an ADU that needs a CDP, a deck "above the uppermost story of a building, with no access from interior living space at the same floor level" is a roof deck and is barred (Step 5, row 9). Stop there.
  2. **On top of enclosed space** (on the ADU, house or garage roof, reached from living space at that level): headline ADR (B)(3)(a)(iii), the ordinance item. Design Review is possible only in this case, on two facts: City intake treats a deck on top of a structure as establishing Design Review (Sept. 2026 intake ruling, untested), and a roof guard read as a "rooftop appurtenance" with its top more than 15 ft up is (B)(1)(c) (a CrossBeam reference that is not included in this plugin Step 4f). Confirm at pre-application.
  3. **Any other deck more than 3 ft above adjacent legal grade** (open, on posts or cantilevered, nothing enclosed under it; free-standing, or off a door at floor level): Administrative Design Review (B)(3)(a)(iii) at any height, hearing not waivable ((B)(3)(b)); never Design Review on the intake rule. The City's ADU & JADU Application footnote 2 and certified 25.17.040(E)(5)(c) say such decks need "design review"; under Ord. 1732 that review is ADR. For a CDP ADU, which is judged against the certified LCP, FLAG the wording; do not route to the DRB on it.
  4. **3 ft or less:** Zone Clearance (B)(2)(m).
- **UNSETTLED: slope and other ESA lots.** The (B)(2) preamble says Zone Clearance "may not be used for any listed project in an environmentally sensitive area" unless a licensed professional finds, subject to peer review, no impact; otherwise (B)(1) Design Review applies. The ESA definition now includes slopes of 30% or more (25.08, Ord. 1732). Read literally, that sends an ADU on a steep lot to a Design Review hearing. That conflicts with state law, which requires ADU approval "ministerially without discretionary review or a hearing, notwithstanding ... any local ordinance" (Gov. Code 66317(a)(1)), and with 25.17.010(e)(2)(A) for a non-CDP ADU. For a CDP ADU, coastal resources are protected through the CDP (25.17.020(b)), where the City may hold a hearing. Do not route an ADU to the Design Review Board on the ESA rule alone. Report the conflict as UNSETTLED, recommend the peer-reviewed professional no-impact finding, and confirm with Planning at pre-application.
- **Second-story ADU or ADU over a garage, roof over 15 ft.** (B)(1)(b) carves ADUs out by name; (B)(1)(c) (improvement over 15 ft) does not mention ADUs. (B)(2)(h) routes ADUs "only as set forth in Chapter 25.17", and state law bars discretionary review or a hearing (Gov. Code 66317(a)(1)). Review the ADU itself on the ADU application against its Ch. 25.17 height and story limits, not at the DRB. The garage below and any decks are separate pieces. UNSETTLED; confirm with Planning at pre-application (a CrossBeam reference that is not included in this plugin Step 4f).
- **ADU built on top of a non-ADU accessory room** (garage, studio or workshop below, ADU above). Work it in this order:
  1. **Attached or detached** is tested against the primary dwelling: (f)(2)(D) covers "An ADU that is attached to the primary dwelling". An ADU over a detached garage or studio is a detached ADU, whatever it shares with the room below. Over an attached garage our lean is attached, because "an enclosed use within the residence, such as an attached garage, is considered to be a part of and contained within the single-family structure" ((c)(5)(B), JADU definition).
  2. **Height counts the whole structure.** Height "is measured from existing legal grade or the level of the lowest floor, whichever is lower, to the peak of the structure", and the peak limit "applies to every part of the structure" ((f)(2)(E)). The room below is inside that measurement. A CDP ADU is measured the same way, to the lowest floor or grade (certified 25.17.040(E)(2)(b)). A detached two-level structure seldom fits 16 ft (18 or 20 ft near transit, (f)(2)(B)), so height usually decides the case first.
  3. **Stories:** a (d)(3) detached ADU may not "have more than one story" ((g)(7)). Whether the room below counts as a story of the ADU is UNSETTLED; the height limit usually settles the project before this does.
  4. **Size:** the 850 / 1,000 sf cap ((g)(1)(A)) counts the ADU's floor area, not the room below (our reading).
  5. **Setbacks:** 4 ft side and rear ((g)(2)(A)). The no-setback rule for an ADU built "in the same location and to the same dimensions as an existing structure" ((g)(2)(B)) does not cover a new story on top, because that changes the dimensions (our lean).
  6. **Over a limit:** a CUP under (j) (Planning Commission, which then hears the whole project, row 6 of Step 7), or redesign: convert the room itself ("within the existing space of an accessory structure, plus up to 150 additional square feet" for ingress and egress, (d)(2)(A)(i)), attach the ADU to the house ((f)(2)(D): 25 ft or the zone limit, two stories), or build it at grade. Height within the state floor never needs a CUP (Gov. Code 66321(b)(4)).
  7. **The room below is its own piece**, routed by its own list item (a CrossBeam reference that is not included in this plugin Step 4); a roof over 15 ft is the question in the bullet above.
- The Director's referral power (25.05.040(A)(2)(d)) raises the same state-law conflict for the ADU itself.
- Ord. 1732 is not certified by the Coastal Commission. A CDP is judged against the certified LCP (25.07.012(G)(1)).

---

### STEP 7: Review checklist

| # | Check | What to verify |
|---|---|---|
| 1 | Filing date and governing text | Filed on or after 3/12/2025 → Ord. 1713. After 12/9/2026 → UNSETTLED (Step 0) |
| 2 | Coastal zone and CDP | Step 1, including the conversion-exemption loss rules and the first-road/300-ft strip scope of (c) |
| 3 | Approval path | (d)(1), (d)(2) scenario, or (d)(3) (Step 2) |
| 4 | Local standards | CDP ADU: certified 25.17.040 plus Ord. 1713 25.17.020 (25.17.010(d)(1)(B)); no CDP: Ord. 1713 (f)/(g) (Step 4) |
| 5 | Coastal standards | All ten 25.17.020 items, including the 3 ft noncombustible firefighter access path and the roof-deck ban (Step 5) |
| 6 | Height and stories | Detached: 16 ft, or 18 ft near a major transit stop (up to 20 ft to match the primary dwelling's roof pitch) or on a lot with a multistory multifamily dwelling (25.17.010(f)(2)(A)-(C)); one story ((g)(7)). Attached: 25 ft or the zone limit, whichever is lower, two stories at most ((f)(2)(D)). Measured "from existing legal grade or the level of the lowest floor, whichever is lower, to the peak", including chimneys, vents and equipment ((f)(2)(E)). **Over a limit:** redesign, or a conditional use permit: an ADU that "does not conform to the objective design or development standards set forth in subsections (a) through (i) ... may be allowed by the city with a conditional use permit" (25.17.010(j)). The CUP goes to the Planning Commission (25.05.030(E)), which then hears the whole project, ADU and every other piece, with its Design Review and CDP (25.05.040(F)(1)(ii); 25.07.012(D); a CrossBeam reference that is not included in this plugin Step 7). **CDP ADU:** the certified limits bind (Step 4: (D)(4), measured to the lowest floor or grade, (E)(2)(b)), and "ADUs above the height limitations shall be subject to design review" ((E)(2)(a)); our reading is that the CUP is the route and that design review is held at the same Planning Commission hearing (`references/city-adu-ordinance.md` Part D, "Over-height ADU"). Height within the state floor (Gov. Code 66321(b)(4)) never needs a CUP. Never call an over-height ADU "allowed by right" |
| 6a | Zone, specific-plan or special height area limits | A detached CDP ADU takes the certified 25.17.040(D)(4) height even where a zone or specific plan sets a lower building height (certified 25.17.030(D) precedence); an attached ADU takes the lower of 25 ft and the zone limit. Special height area (`lookup_property`): 14 ft above mean front curb (25.10.010(B)); see "Special height areas and lot coverage" below |
| 6b | JADU deed restriction | Every JADU: recorded before certificate of occupancy (25.17.010(f)(8)); see "JADU deed restriction" below |
| 6c | Lofts and mezzanines | Title 25 does not mention lofts. **Floor area:** gross floor area is "the sum of the gross horizontal areas of the several floors of a building", excluding only attic areas "devoted exclusively to uses accessory to the operation of the building" (25.08); our reading is that a loft you can stand or sleep in counts toward the ADU's size cap and toward the base of the certified 20% outdoor-living cap ("limited to 20% maximum floor area of the ADU", 25.17.040(E)(5)(c)). **Stories:** the building code places a loft "between the floor and ceiling of any story" when it is no more than one-third of the room (CRC R202 "Mezzanine, loft"), but the zoning "Story" definition (25.08) counts the space between floor surfaces and does not say. Whether a loft breaks the one-story limit ((g)(7)) is UNSETTLED. Height is unaffected: the peak limit governs ((f)(2)(E)). Confirm at pre-application |
| 7 | Other entitlements | Grading, retaining walls, new access, elevated decks (Step 6) |
| 8 | ESA / slope | Professional no-impact finding, or FLAG the UNSETTLED ESA routing (Step 6) |
| 9 | Historic | California Register property: (g)(6) placement and character-defining-feature limits |
| 10 | Building code | State skill plus city amendments; sprinklers below |

---

### Other Laguna ADU Rules

#### Fire sprinklers

- Sprinklers are required in an ADU "if sprinklers are required in the primary residence" (25.17.010(f)(3)(A)).
- "The construction of an ADU does not trigger a requirement for fire sprinklers to be installed in the existing primary dwelling" (25.17.010(f)(3)(B)). Leave the ADU's own work out of the primary dwelling's retrofit tests.
- Other work on the primary dwelling in the same project is tested on its own under both retrofit triggers, LBMC 14.52.030 (valuation) and Title 15 §1103.5.4 (scope). Either one firing requires the retrofit. Full rule: `../residential-remodel/references/city-sprinkler-retrofit.md`.

#### Major remodel

ADUs are left out of the major-remodel calculation (25.17.020(d)(2); Major Remodel Quick Guide, Oct. 2026: "The construction and remodeling of accessory dwelling units are exempt from major remodel calculations"). Exception: work governed by Coastal Act section 30253 on bluff-top, beachfront and coastal-canyon lots. On those lots, FLAG and confirm with Planning.

#### JADU deed restriction

LBMC 25.17.010(f)(8): "Prior to issuance of a certificate of occupancy for a JADU, a deed restriction must be recorded against the title of the property in the County Recorder's office and a copy filed with the Community Development Director." The deed restriction runs with the land, bars selling the JADU separately (except under Gov. Code 66341), and restricts the JADU to its approved size and attributes ((f)(8)(A)-(C)). The City provides the form. City record: ZPC-2026-1813.

- It applies to **every JADU**, whether or not the JADU shares a bathroom with the house. State law requires the same deed restriction for every JADU (Gov. Code 66333(c)). The shared-sanitation condition in state law is the owner-occupancy trigger (66333(b)), not the deed-restriction trigger.
- Timing in the code: before the certificate of occupancy. It is not a zoning-plan-check completeness item. Do not ask for it at intake; list it as a condition to satisfy before final.
- Subsection (f) by its terms covers JADUs approved under (d)(2) or (d)(3); for a CDP JADU ((d)(1)), Gov. Code 66333(c) still requires the deed restriction.

#### Special height areas and lot coverage

- **Special height area.** In the mapped area (Tracts 4623, 5509, 6721 and lands between Skyline Drive and Park Avenue), "no building or structure shall have a height greater than fourteen feet above the mean front curb height" (25.10.010(B)). `lookup_property` shows whether the parcel is in it.
- **For the house or an attached ADU, exceeding it, or the lot coverage limit, takes a variance** (25.05.025; a CrossBeam reference that is not included in this plugin Step 6 item 3; City practice, VAR-2025-1912 with DR-2025-1911).
- **CDP ADU (most of Laguna): settled.** A detached ADU that needs a CDP takes the certified 25.17.040(D)(4) height, and the chapter "shall take precedence" over a conflicting zone or specific-plan standard (certified 25.17.030(D)), the 14-ft curb line included. The 14-ft line still binds an attached ADU, whose limit is the lower of 25 ft and the zone limit ((D)(4)(d)).
- **State height floor (UNSETTLED for an ADU with no CDP).** A local agency may not set a height limit below 16 ft for a detached ADU (18 ft near major transit, 18 ft on a multistory multifamily lot) (Gov. Code 66321(b)(4)(A)-(C)). An attached ADU may be held to "25 feet or the height limitation in the local zoning ordinance that applies to the primary dwelling, whichever is lower" (66321(b)(4)(D)), so the 14-ft curb line binds an attached ADU. For a detached ADU, whether the 14-ft curb line can cut below the 16-ft state floor, or whether the ADU gets 16 ft measured under 25.17.010(f)(2)(E), has not been ruled on. Do not require a variance for a detached ADU that is within the state floor. FLAG it as UNSETTLED; confirm with Planning at pre-application. The same applies to lot coverage: lot coverage may not block an ADU of at least 800 sf of interior livable space with 4-ft side and rear setbacks (Gov. Code 66321(b)(3)).

#### Nonconforming ADU

An ADU that does not meet the objective standards in 25.17.010(a)-(i) may be allowed with a conditional use permit (25.17.010(j)).

---

## City Submittal Checklists

The City's own lists of what a submittal must contain. They ship in this plugin; paths are relative to this file.

- `../../requirements/README.md` — the index: which checklist covers which scope
- `../../requirements/plan-sheets/plan-sheet-matrix.md` — which plan sheets the project needs and what each sheet must show
- `../../requirements/building/` — the Building Division submittal checklists
- `../../requirements/planning/application-index.md` — which Planning application to file
- `../../requirements/issuance/issuance-checklist.md` — what is due after approval, before the permit issues

Choose the checklists from the project scope the evidence shows, not from the permit name. When a plan set exists, run `../plan-set-check/SKILL.md` on it. These are completeness checks. They do not check the design against the code.

---

## California Code Compliance

This plugin does not carry the California code checklist for ADU (Accessory Dwelling Unit) plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "adu"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for ADU (Accessory Dwelling Unit) permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/city-adu-faq.md` — Laguna Beach ADU/JADU — FAQ & Coastal Development Permit Process
- `references/city-adu-ordinance.md` — Laguna Beach ADU/JADU Standards — Ord. 1713 (in force) and certified Chapter 25.17 (LCP)
- `references/city-coastal-permits.md` — Laguna Beach ADU — Coastal Development Permit Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
