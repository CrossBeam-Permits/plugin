---
title: "Adding Dwelling Units to a Commercial Building (Residential over Commercial, Office-to-Residential)"
category: zoning
relevance: high
key_code_sections: "LBMC 25.19.002(DD), 25.19.008(E); 25.20.004(B); 25.25.002(W); 25.18.002(Q); 25.21.004(A)(5); 25.32.003(J); Ch. 25.16; 25.96.030; 25.52.004(E), 25.52.006(E),(G),(H), 25.52.012(D),(G); 25.56.002, .008, .009, .011; 25.07.006, .008(A)(2)(b), .009, .012(D), .013; 25.05.040(B),(F) (Ord. 1732)"
law_as_of: "2026-10-10"
---

# Adding Dwelling Units to a Commercial Building

Use this file when a project adds dwelling units to an existing commercial building, converts office or retail floor area to apartments, or builds residential over commercial. It covers the Laguna deltas only. Load the state floor (`california-multi-unit-residential`) for building-code content.

Sources: LBMC Title 25 corpus (the City source document (not included in this plugin), codified through 2026-04-28); Ord. 1732 overlay (the City source document (not included in this plugin), the City source document (not included in this plugin)); the LCP certification record (the City source document (not included in this plugin)). Ord. 1732 (adopted 2026-07-21, extended by Ord. 1733) is in effect locally but **not yet certified by the Coastal Commission**.

## 1. Ord. 1712 in one paragraph

Ord. 1712 was adopted 2025-03-11. The Coastal Commission certified it as **LCP-5-LGB-24-0026-1**, effective **2025-05-07** (the City source document (not included in this plugin)). In C-N, C-1, SLV and LBP it made residential a permitted use, with no use permit. Every current C-N, C-1 and SLV use section carries "Ord. 1712, 3/11/2025" in its history note.

What Ord. 1712 removed from C-N (the old CUP, the 50% residential floor-area cap, the 2,000 sf of lot area per unit rule, and extra residential open space) comes from the Coastal Commission exhibits for LCP-5-LGB-24-0026-1 (Exhibit 1, C-N strikeout). Those exhibits are **not in the repo**. What is verified: the current C-N text contains none of those limits. Treat the history as City record, not as code text.

## 2. Use permission by zone

| Zone | Rule | Where homes may go | Density | Authority |
|---|---|---|---|---|
| **C-N** | **Permitted** | Mixed-use site; above the ground floor, or ground floor behind a highway-fronting commercial use | None in zoning | §25.19.002(DD) |
| **C-1** | **Permitted** | Same as C-N | None in zoning | §25.20.004(B) |
| **SLV** | **Permitted** | Same as C-N | None in zoning | §25.25.002(W) |
| **LBP** | **Permitted** | Any; mixed use not required | 1 du per 2,000 sf of lot area, less 1 du per 1,000 sf (or fraction) of commercial floor area | §25.18.002(Q) |
| **CH-M** | **CUP** | Only as an ancillary use to a primary hotel-motel | R-3 density and standards; residential floor area max 50% of commercial floor area | §25.21.004(A)(5) |
| **M-1A** | Ordinary homes prohibited | Artists' work/live only, by CUP | Zone density | §25.32.003(J), §25.32.004(B) |
| **M-1B** | Artists' work/live by CUP | District text not in corpus | Confirm | §25.16.050(A)(1); Ch. 25.48 |
| **DSP districts** | See `dsp-mixed-use.md` | | | Ch. 25.40 / DSP 2022 |
| **Artists' work/live** (any allowable zone) | **CUP** (C-N: §25.19.006(K); C-1: §25.20.006) | At least half of each unit is work area (two-thirds in M-1A/M-1B) | Zone density | Ch. 25.16 |

The C-N text, quoted (C-1 §25.20.004(B) and SLV §25.25.002(W) are word-for-word the same):

> "(DD) Residential uses, subject to the following: 1. It shall be designed as part of a mixed-use commercial site and satisfy one of the following criteria: a. Located above the ground floor level; or b. Located on the ground floor, subject to the following additional requirements: i. The residential use is separated from the highway, with a commercial use fronting the highway; and ii. The commercial use has a useable, enclosed depth of no less than 30 feet at any point, measured perpendicular to the highway or primary street, except for areas used for open space, pedestrian circulation, or vehicular access. This standard may be modified by the Planning Commission ... 2. It shall comply with the property development standards of this Chapter."

Reading notes:

- "Mixed-use commercial site" means commercial use stays on the site. Converting a whole commercial building to homes is not this use. Check LBP (where mixed use is not required) or a state path.
- A ground-floor unit that fronts the highway does not fit (DD). The City treated a C-N ground-floor live/work request as a use "not expressly listed" and left the path undecided (one recent project; see a CrossBeam reference that is not included in this plugin). The only listed residential path there is artists' work/live by CUP.
- (DD) covers new and converted space alike. The Ord. 1712 staff reports framed it around new second floors; they do not discuss converting existing upper-floor offices (City record). No interior office-to-apartment conversion under Ord. 1712 had been processed as of 2026-10. **Ask Planning to confirm the use path in writing at pre-application.**
- C-N also lists "(GG) Supportive or affordable housing, provided it is a residential component of a mixed-use project" as permitted.
- Artists' work/live (Ch. 25.16) carries its own rules: an artist occupancy permit (§25.16.030), 1.5 parking spaces per unit (§25.16.050), and a CDP (§25.16.035). Do not route ordinary apartments through it.

## 3. Density and unit size

- C-N: "(A) Lot Area and Dimension Standards. No requirements." (§25.19.008(A)). No lot area per unit and no unit cap. Unit count is set by the building envelope, parking and the building code.
- C-1 and SLV: no residential density standard in the zone text.
- LBP keeps its density rule (§25.18.002(Q)(1)-(2)). Do not apply the LBP rule in C-N.
- Zoning sets no minimum unit size in C-N, C-1 or SLV. Unit and room minimums are building-code items. Use the state floor (`california-multi-unit-residential`); do not restate them here.
- Unit size still matters locally: 700 sf is the line for the reduced parking rate (Section 6) and for the setback waiver (Section 7).

## 4. Height, stories and the existing building

**C-N limit.** "The height of any building ... shall not exceed thirty feet and two floors, including parking garage floor levels with access ramps located outside the structure's ground floor footprint." Subterranean floors are exempt from both limits (§25.19.008(E)(2)). The 30 ft includes chimneys, vents, mechanical equipment, elevator shafts and stairways. Other zones: C-1, LBP and CH-M 36 ft with no floor count; SLV two stories, 22 ft excluding roof, 30 ft from grade (§25.25.008(F)(2)). Each of these zones (C-N too) also has a slope-based height table that is often lower; check it (for example §25.19.008(E)(1), §25.20.008(D)).

**An existing third floor in C-N** that was lawfully built is a legal nonconforming structure (§25.56.002). It "may be continued and maintained." Converting its use inside the walls does not add height or floors.

**Rebuild-to-conform rule.** §25.56.009: "If any part of a nonconforming portion of the structure is substantially removed or modified in such a way that it compromises the structural integrity of the building, that portion must be rebuilt in conformance with zoning regulations." For an over-height floor, conforming means losing it. Keep structural work on the nonconforming portion light, and have the engineer address this rule in writing.

**Enlarging a nonconforming structure.** §25.56.008 allows it only if the enlargement complies with Title 25 in every respect and "(C) The required number of parking spaces is provided per Chapter 25.52." A floor-area addition is therefore a parking event (see Section 6, and the 25.96.030(C)(3) relief in Section 7).

**Major remodel.** §25.56.011 (added by Ord. 1732): "Whenever modifications to an existing building or structure constitute a major remodel, the construction shall be classified as a new building or structure subject to the current development standards of the subject zone, and all requirements applicable to the construction of a new building or structure including undergrounding requirements, required dedication of on- and off-site improvements, and payment of new development fees." Consequence: the over-height floor and any parking deficit lose their nonconforming protection, except that §25.96.030(C)(3) lets a major remodel caused only by a residential floor-area addition keep nonconformities of the non-residential use, including parking (Section 7). §25.52.004(E)(1) independently requires current parking for a major remodel.

**How to measure major remodel.** Use `../../residential-remodel/references/city-major-remodel-methodology.md` (October 2026 Quick Guide). It applies to commercial buildings: the guide's floor-area rule names "a principal structure, such as a residence or commercial building." Non-appealable coastal area: exterior walls only, per floor; 50% or more removed is a major remodel; additions over 50% cumulative since the structure that "legally existed on the site on January 13, 1993." Appealable area: the stricter method in the same file. Interior demolition does not count in the non-appealable method.

**UNSETTLED:** the guide excludes attached non-habitable or unconditioned area from the baseline. It does not say how to treat such space converted into a unit. Return FLAG and show both numbers; confirm with Planning at pre-application.

## 5. Change of use is not automatically new parking

§25.52.004(E)(1): "When a new building is constructed or when a major remodel is proposed, or a use is changed to a use which has a greater parking requirement, or when the floor area of an existing building is enlarged, then the property owner or applicant shall provide parking or purchase in-lieu parking certificates equivalent to the number of parking spaces required by current parking regulations ... less credit for" spaces on site, credits under §25.52.006(G), paid in-lieu certificates, and the 1958-rule credit for pre-1958 buildings ((E)(1)(a)-(d)).

For an interior conversion that is not a major remodel and adds no floor area, the only trigger is "a use is changed to a use which has a greater parking requirement." Compare:

- Office: "1 space for each 250 square feet of gross floor area" (§25.52.012(G), General office).
- Units in C-N, C-1, SLV: 0.5 or 1 per unit (Section 6).

Small units usually need fewer spaces than the office they replace. Show the comparison for the converted floor area. Where existing parking or credits serve a larger premises, allocate them by gross floor area (§25.52.004(E)(3)). Required spaces may not be "eliminated, reduced or converted" without equivalent spaces (§25.52.004(C)(2)).

## 6. Parking for the units

**Zone rate (C-N, C-1, SLV).** §25.19.002(DD)(3), same in §25.20.004(B)(3) and §25.25.002(W)(3): "The required number of parking spaces shall be 0.5 spaces for each dwelling unit located within a quarter mile walking distance of a fixed public transit stop and not exceeding 700 square feet in gross floor area, and one space for all other dwelling units. Residential parking may be covered or uncovered. Parking requirements may also be modified or reduced pursuant to Section 25.52.006. Applicants may request to purchase in-lieu parking certificates in a lump sum or amortized basis to satisfy all or part of the residential parking requirement."

- Both conditions apply for 0.5: 700 sf or less AND a quarter-mile walk (not straight line) to a fixed stop. Document the walking route.
- Rounding: fractions round up (§25.52.012(D)). 3 small units = 1.5 = 2 spaces.
- Covered spaces: not required for "multi-family dwellings in commercial zones with existing or proposed non-residential uses on the same building site" (§25.52.012(G), multifamily row, Exception (1)).
- LBP and CH-M have no reduced rate: use the §25.52.012(G) multifamily row.
- State law may cut further (AB 2097 near a major transit stop). Use `california-transit-parking-reduction`; do not restate it.

**Relief tools.**

| Tool | What it does | Authority |
|---|---|---|
| In-lieu certificates | City Council relief, only in a designated special parking district; up to 3 per site; 4+ need a parking demand study; max 50% of required spaces for one use; "A coastal development permit shall be required with issuance of parking in lieu certificate(s)." | §25.52.006(E) |
| Incentive / TDM reduction | City Council CUP (and CDP) where the use promotes transit, bikes, walking, and public access is not harmed; (G)(3) "innovative parking solutions" needs 1-year and 5-year studies and expires five years after certification of LCP-5-LGB-19-0139-1 (date not in corpus; per City record notes the Coastal Commission acted in May 2021, so it may have lapsed about May 2026. UNSETTLED; confirm with Planning at pre-application) | §25.52.006(G) |
| Off-site spaces | CUP (and CDP); one site within 600 ft; deed-restricted; residential spaces "available at all times" | §25.52.006(H) |
| Shared / joint use | CUP with study | §25.52.006(B),(C) |

§25.52.006(H) now reads: "Additional parking that is required for an intensification of nonresidential uses, or residential uses in mixed-use zones, may be satisfied by providing off-site parking spaces ... Except for infill housing projects in mixed-use zones that create new housing units, the intensification of use may not involve floor area additions." (Ord. 1712.) A 2023 City redline on one recent project said (H) applies only to non-residential intensification. That predates the amendment; the current text reaches residential in mixed-use zones.

**Existing-deficit credit ("grandfathered" parking).** City staff use the word "grandfathered" for a legal nonconforming parking deficit. They gave the credit on one recent project (2025) and kept that project's commercial count at its 1958 ratio (2025). They refused it on one recent project (2026) because the project was a major remodel, and the 2023 TDM review on that project found "no grandfathered parking." Cite the code basis, not the word: §25.56.002 (continued and maintained) and the credits in §25.52.004(E)(1)(a)-(d). See a CrossBeam reference that is not included in this plugin.

## 7. Infill and mixed-use exceptions (§25.96.030)

Applies "to the C-N, C-1, and SLV zoning districts only" (§25.96.030(B)). Every exception requires a covenant: "the property owner agrees to enter into a recorded covenant with the City, ensuring that the residential units will not be converted to short-term lodging units as defined in Chapter 25.23 ... The covenant shall be in a form approved by the City Attorney and binding upon all future owners and successors in interest. The approval and recordation shall occur prior to issuance of building permits." (§25.96.030(C)).

| Exception | Conditions | Authority |
|---|---|---|
| **(1) Additional setback waiver.** Waives the §25.50.004(D) added setback for up to two exclusively residential floor levels with two or more units immediately above the ground floor | (a) at least half the units "do not exceed 700 square feet in gross floor area (halves are rounded up)"; (b) plate height 9 ft or less and, if the top floor, roof "does not exceed 16 feet above the residential finished floor" | §25.96.030(C)(1) |
| **(2) Nonconforming open space.** Residential above an existing commercial ground floor may reduce the nonresidential open space "only as necessary to accommodate access improvements, bicycle storage, and trash storage serving the residential use" | Existing commercial ground floor | §25.96.030(C)(2) |
| **(3) Major-remodel nonconformities.** "Residential additions that constitute a major remodel of an existing building or structure shall not be required to bring nonconformities associated with the non-residential use or uses into compliance with this Title, including nonconforming parking, provided that the project constitutes a major remodel due to the size of the floor area addition only." | Not available "when a project meets one or more of the major remodel demolition thresholds"; bluff and shoreline policies (LUE 7.3, 10.2) still apply | §25.96.030(C)(3) |

That project's letter (2026-10-08) and, per the Tyler record summary, that project's resolution (2026-0844) cite this as "25.95.030(C)(3)". Ch. 25.95 is the SB 9 chapter; the codified section is §25.96.030(C)(3).

Related rules in Ch. 25.96:

- Inclusionary housing applies to "all development that will result in ten or more residential units or lots, including new development, conversion, adaptive reuse, redevelopment" (§25.96.070(C)). Below 10 units it does not apply.
- "Adaptive Reuse Project" means a change from nonresidential use to dwelling units in a building "constructed in accordance with building and zoning codes in effect prior to July 1, 1974, or which has been determined to be a historically significant building" (§25.96.070(B)(1)). It matters only for the inclusionary exemption in §25.96.070(D)(4).

## 8. Open space

| Zone | Rule | Authority |
|---|---|---|
| C-N | 25% of nonresidential gross floor area, exclusive of parking and driveways. No separate residential requirement in the zone text | §25.19.008(B)(5) |
| C-1 | 25% of nonresidential GFA; "Mixed-use properties with residential uses shall not be required to provide additional open space beyond what is required for the nonresidential uses." | §25.20.008(C)(5) |
| SLV | Same as C-1 | §25.25.008(B)(4) |
| LBP | 25% of nonresidential GFA, "in addition to that required for residential uses"; residential yards and open space set by the design review board | §25.18.008(B)(5), (C) |
| CH-M | 25% of nonresidential GFA plus residential open space of at least 40% of total gross living area | §25.21.006(C)(5)(a)-(b) |

Converting commercial floor area to units lowers the nonresidential base in C-N, C-1 and SLV. Show the calculation anyway.

## 9. Permit stack

**Coastal Development Permit — required.** Adding units is development: the definition includes "a change in the density or intensity of use of land" (§25.07.006). The exemption for improvements to non-single-family structures does not apply to "(b) Improvements to any structure which would result in a change in the intensity of use of the structure" (§25.07.008(A)(2)(b)). Expect a CDP even when the work is interior only.

| CDP question | Rule | Authority |
|---|---|---|
| Who decides | Same body as the other permits; "In the case where a project requires only a coastal development permit, such permit may be approved or denied by the Director of Community Development." | §25.07.012(D), (D)(1) |
| Hearing waiver (administrative CDP) | "Minor development": consistent with the LCP, "no discretionary approvals other than a coastal development permit," no adverse coastal effect. Hearing held only if requested "within fifteen (15) working days from the date of sending the notice" | §25.07.013(A), (B)(1)(a)(1) |
| De minimis waiver | Only if not appealable, not in an appeal area, and "no local public hearing is required"; "If a project site involves a violation ... it is not de minimus." Sites with "alleged or outstanding violations of the LCP" are listed exclusions | §25.07.009(B)(1), (B)(3) |
| Appealable or not | From site facts (appeal area). Appealable development gets at least one public hearing | §25.07.006, §25.07.012(E) |

**Design Review — Ord. 1732 closed lists** (§25.05.040(B)):

| Scope | Track | Authority |
|---|---|---|
| Interior only: "Interior modifications to existing structures that do not modify the exterior of such structures" | Zone Clearance | (B)(2)(d) |
| Exterior "Demolition, alteration, or addition that does not constitute a major remodel" | Zone Clearance, unless a (B)(1) item applies | (B)(2)(a) |
| Major remodel | Design Review | (B)(1)(a) |
| "Any improvement that exceeds a height of 15 feet" (landscape and lighting plans required) | Design Review | (B)(1)(c) |
| "Commercial or industrial parking and loading areas" | Design Review | (B)(1)(l) |
| In-kind repair, railings, re-roof (same pitch, not light colored), skylights with automatic night shades, mechanical equipment meeting §7.25.130(c) | Zone Clearance | (B)(2)(c), (e), (r), (s), (v) |

Hearing body, §25.05.040(F)(1): "i. The design review board shall conduct a noticed public hearing on design review applications for all single-family or two-family developments ... ii. The planning commission shall conduct a noticed public hearing on all other design review applications, including but not limited to: residential development of three-families or more, all projects located in the downtown specific plan area, all non-residential development ..." Mixed-use projects go to the **Planning Commission**. The Director may refer any Zone Clearance or Administrative Design Review project up (§25.05.040(A)(2)(d)).

**UNSETTLED — confirm with Planning at pre-application:**

1. Ord. 1732 is not LCP-certified. The certified C-N text says "All buildings, structures and improvements are subject to design review as provided in Section 25.05.040" (§25.19.008(D)); C-1, SLV and CH-M have the same sentence. Which track applies to a coastal-zone project is not settled.
2. Whether a (B)(2) list item (railings, re-roofing, mechanical) stays Zone Clearance when it sits on a building already over 15 ft, or whether (B)(1)(c) controls. City practice since Ord. 1732 points to Zone Clearance; see the guide's planning-approvals Step 4f.
3. Interior-only conversion: whether the City wants a Zone Clearance application plus the CDP, or the CDP alone. The Zone Clearance form says it is for projects that "DO NOT require a discretionary planning entitlement, such as Design Review or a Coastal Development Permit."

**Use permit.** None in C-N, C-1, SLV or LBP for ordinary units. A CUP is needed for CH-M residential, artists' work/live, parking relief under §25.52.006(B), (C), (G) or (H), and any separate CUP use on the site (for example a café serving alcohol, §25.19.006(B)).

## 10. Not an ADU project

State ADU conversion rights inside multifamily buildings apply to "existing multifamily dwelling structures" (Gov. Code §66323(a)(3)). A commercial building with no dwellings has nothing to convert under that rule. The new units are ordinary apartments under the zone's use permission. Do not file ADU applications, and never one per unit. See the California ADU (Accessory Dwelling Unit) rules (General Zoning Rules), which come from the CrossBeam connector (see "California Code Compliance" in `../../adu/SKILL.md`) for the state rule. After the units exist, the building may hold multifamily dwellings, and later ADU conversions may become possible; that is a separate, later question.

## 11. State alternatives — when each fits

Point only; the rules live in the state skills. Start with `california-entitlements` (the index).

| Path | Fits when | Skill |
|---|---|---|
| AB 507 Office to Housing Conversion Act (Gov. Code §65658 et seq., operative 2026-07-01) | Larger conversions that can meet its residential-share, affordability and prevailing-wage terms (mixed-use projects need at least half the floor area residential). No Laguna implementing ordinance found as of 2026-10 | `california-adaptive-reuse` (`references/ab507-office-to-housing.md`) |
| AB 2011 (Gov. Code §65912.100 et seq.) | Commercial-corridor site; project meets its affordability and labor terms; ministerial | `california-commercial-corridor-housing` |
| SB 6 (Gov. Code §65852.24) | Residential on commercially zoned land meeting its site and density terms | `california-commercial-corridor-housing` (`references/sb6.md`) |
| SB 330 / Housing Accountability Act | Mixed-use counts as a housing development project only with at least two-thirds of the floor area residential | `california-sb330`; `california-entitlements` |
| Density Bonus (Gov. Code §65915; LBMC §25.96.010) | Project includes affordable or senior units and needs waivers (height, stories, parking) | `california-density-bonus`; `state-preemption.md` |

The local path in C-N, C-1 and SLV already allows small upper-floor units by right with no affordability terms. A state path adds terms; use it when the local path cannot fit (for example, a whole-building conversion, or a needed height or story waiver).

## 12. Filing shape

- **One project, one set of Planning applications** covering every unit (CDP, plus Zone Clearance or Design Review). Not one per unit.
- Then **one building permit**: the EnerGov "Mixed Use Permit" (type 374) for a building with both residential and non-residential use (`../../city-website/references/submit-mixed-use.md`). Fire sprinklers are a separate fire permit.
- Change of occupancy B (office) to R-2 is a building-code question. Use the state floor: CEBC Chapter 10 (change of occupancy), CBC 508 (mixed-occupancy separation), and CBC 1006.3.4 (single exit for R-2: at most 4 dwelling units per story, through the third story, sprinklered). Start with the California Multi-Unit Residential rules (Change of Occupancy — Office (B) to R-2 Apartments), which come from the CrossBeam connector (see "California Code Compliance" in `../SKILL.md`); egress detail is in the California Multi-Unit Residential rules (Egress and Exits — Number of Exits, Separation, Travel Distance, and Emergency Escape Openings), which come from the CrossBeam connector (see "California Code Compliance" in `../SKILL.md`). Laguna deltas: VHFHSZ Ch. 14.70 and the sprinkler retrofit triggers (`../../residential-remodel/references/city-vhfhsz-wui.md`, `city-sprinkler-retrofit.md`).
- What to put in the Planning submittal: `submittal-kit-office-to-residential.md`.

## 13. UNSETTLED list — ask Planning at pre-application

1. Which plan-sheet matrix row applies to an office-to-apartment conversion ("Tenant Improvement" or "New Multi-family (2+ units)").
2. Interior-only: Zone Clearance application plus CDP, or CDP alone.
3. Which Design Review track applies in the coastal zone while Ord. 1732 is uncertified.
4. Whether (B)(2) list items stay Zone Clearance on a building over 15 ft. City practice since Ord. 1732 points to Zone Clearance; see the guide's planning-approvals Step 4f.
5. How the October 2026 major-remodel guide treats non-habitable space converted into a unit.
6. City Attorney deposit amount and trigger. The July and August 2026 Planning application forms (Zone Clearance 2026-07 and Design Review 2026-08, Exhibit A) list "Housing Development Project ... Deposit: $5,000* *When requested by CAO." Footnote 3 uses the Gov. Code 65589.5(h)(2) definition, which includes "Mixed-use developments with at least two-thirds of the square footage designated for residential use." The City fee schedule (Master Fee Schedule adopted May 12, 2026; `../../../requirements/fees/fee-schedule.json`) lists no City Attorney deposit. On one recent project the City charged $10,000 (incomplete letter, 2026-10-08). So: forms say $5,000 when the City Attorney's office requests it; one 2026 project was charged $10,000. A conversion that leaves less than two-thirds of the floor area residential may fall outside the footnote. Amount and trigger UNSETTLED; confirm with Planning at pre-application.
7. For a building with an over-height floor or a parking deficit: confirmation of its legal nonconforming status and the parking credits the City will count (ask for or check the Real Property Report).
