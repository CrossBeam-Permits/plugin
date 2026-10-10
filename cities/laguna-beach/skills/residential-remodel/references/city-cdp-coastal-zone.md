# Laguna Beach — Coastal Development Permit (Ch. 25.07)

This file documents the Laguna-specific overlay for CDP review. The state skill `../../coastal-development/references/california-baseline.md` covers the substantive CDP analysis (appealable areas, categorical exclusions, LCP consistency, public access, resource protections). This file layers in the Laguna-specific procedural rules and two consequential overlay flags: (1) the CDP requirement for a major remodel in the coastal zone (new development, not an exempt improvement), with E-93-1 areas left UNSETTLED, and (2) the Coastal Commission F9a (Nov. 2024) finding that Categorical Exclusion E-93-1 does not clear an ADU. Law as of 2026-10-10.

---

## Statutory Framework — Ch. 25.07

From the City source document (not included in this plugin). Key sections:

### §25.07.004 — CDP Required

Verbatim:

> *"A coastal development permit shall be required for all proposed development within the coastal zone except for development specifically exempted under Sections 25.07.008 and 25.07.010. Development undertaken pursuant to a coastal development permit shall conform to the plans, specifications, and terms and conditions approved or imposed in granting the permit."*

(Ord. 1253 § 1, 1992)

### §25.07.006 — Definitions (Appealable Development; Development)

"Appealable development" verbatim:

> *"'Appealable development' means any development project which may be appealed to the coastal commission in accordance with the adopted regulations of the coastal commission and is located within or constitutes any of the following:*
> *(1) Approval of a development project located within any appealable area, as follows:*
> *(a) All area between the sea and first public road paralleling the sea or within three hundred feet of the inland extent of any beach or the mean, high-tide line of the sea where there is no beach, whichever is the greater distance,*
> *(b) All area within one hundred feet of any wetland, estuary, or stream and all area within three hundred feet of the top of the seaward face of any coastal bluff;*
> *(2) Approval or denial of a development project which constitutes a major public works project or a major energy facility."*

These are the geometric definitions for the appealable-area polygon (Step J integration).

"Development" verbatim:

> *"'Development' means the placement or erection of any solid material or structure on land or in or under water; the discharge or disposal of any dredged material or of any gaseous, liquid, solid or thermal waste; the grading, removing, dredging, mining or extraction of any materials; a change in the density or intensity of use of land including, but not limited to, the subdivision of land pursuant to the Subdivision Map Act ... and any other division of land, including lot splits; change in intensity of use of water, or of access, thereto; the construction, reconstruction, demolition or alteration of the size of any structure, including any facility of any private, public or municipal utility; and the removal or harvesting of major vegetation other than for agricultural purposes; and kelp harvesting."*

A "major remodel" — per Step B — falls squarely within "the construction, reconstruction, demolition or alteration of the size of any structure" and "a change in the density or intensity of use of land."

### §25.07.008 — Exemptions (single-family-dwelling carveouts)

§25.07.008(A)(1) carves out routine SFR improvements. The carveouts to the carveouts are operative for major-remodel review:

§25.07.008(A)(1)(c) — improvements to any structure where the structure or improvement is **between the sea and the first public roadway paralleling the sea, or within 300 feet of the inland extent of any beach or mean high tide line where there is no beach, whichever is greater** — when such improvements would constitute or result in:

> *"1. An increase of ten percent or more of an internal floor area of the existing structure on the building site or an additional increase in floor area (meaning an improvement to the structure had previously occurred pursuant to an exemption) bringing the aggregate increase to ten percent or more cumulatively over time,*
> *2. An increase in height of more than ten percent of any structure,*
> *3. The construction, placement or establishment of a detached structure such as a garage, fence, shoreline protective works, or docks;"*

A major remodel crosses these thresholds (50% > 10%), so the SFR-improvement exemption does not apply to a major remodel **inside that strip** (first public road / 300 ft of the beach or mean high tide line). The strip is narrower than the appealable area, which also reaches 100 ft from wetlands and streams and 300 ft from bluffs. Outside the strip, (A)(1)(c) does not apply; the basis for a CDP is that a major remodel is new development (below).

§25.07.008(A)(1)(b) — improvements **on a beach, in a wetland or stream, seaward of the mean high tide line, within fifty feet of a coastal bluff edge, in an ESA, or in a highly scenic area** — never exempt.

§25.07.008(A)(3) — repair and maintenance activities that do not result in addition/enlargement/expansion are exempt, with carveouts for shoreline structures (sea wall revetment, bluff retaining wall, breakwater, groin, culvert, outfall) — substantial alteration of foundation/pilings, placement of rip-rap, replacement of ≥20% of materials with materials of a different kind, and presence of mechanized construction equipment within 20 ft of coastal waters/streams or on any sand area or bluff or ESA — are NOT exempt.

§25.07.008 ordinance history (verbatim trailer): *"(Ord. 1253 § 1, 1992; Ord. 1649 § 2, 2020; Ord. 1653 § 4, 2021; Ord. 1665, 11/16/2021; Ord. 1679 § 4, 2022; Ord. 1688, 7/11/2023)"* — Ord. 1688 amended §25.07.008. (Note: Ord. 1688 amended §25.07 CDP procedures, NOT the bluff overlay — see `city-bluff-overlay.md` for that distinction.)

### §25.07.009 — De Minimis Waiver

Director may waive CDP for de minimis development if (1) within coastal zone but not appealable, not in appealable area, not in CCC-retained-jurisdiction area, and no local public hearing required; (2) consistent with LCP and no individual or cumulative adverse effect on coastal resources; (3) no violation involved. Coastal Commission notice required.

### §25.07.010 — Categorical Exclusions

Verbatim:

> *"Development included in any categorical exclusion area adopted pursuant to the California Coastal Act is exempt from the regulations contained in this chapter except for the notice requirements contained within California Code of Regulations Section 13248."*

E-93-1 is Laguna's categorical exclusion for single-family residential development in eleven areas. It does not clear an ADU (Commission report F9a, Nov. 2024), and whether it clears a major remodel is UNSETTLED — see below.

### §25.07.012 — Procedure

Director (or designee) determines CDP applicability (within CCC original jurisdiction, appealable to CCC, non-appealable, or categorically excluded/exempt). CDP review processed concurrently with other permits required by underlying zoning. §25.07.012(F) review criteria — 9 LCP consistency findings.

### §25.07.014 — Noticing

- Appealable development: 10-day mail notice prior to first public hearing or within 10 days of accepting the application (whichever is greater); to applicant, persons who requested notice, all property owners within 100 ft, all residents within 100 ft, and the Coastal Commission.
- Non-appealable development: 10-day mail notice; property owners within 300 ft, residents within 100 ft, Coastal Commission. Newspaper publication if Planning Commission hearing.

### §25.07.016 — Appeals

Appealable development may be appealed to CCC by a qualified appellant within **10 working days** from the date of CCC receipt of the notice of final action. Grounds limited to (a) non-conformity with the certified LCP or (b) failure to comply with public access policies of Coastal Act Ch. 3.

---

## Major Remodel in the Coastal Zone — CDP Required

### Operative Rule

- A major remodel "shall be classified as new development subject to current zoning regulations and all requirements applicable to the construction of a new building or structure" (October 2026 Major Remodel Quick Guide, paragraph 1), and §25.56.011 (Ord. 1732) makes it a new building.
- The §25.07.008(A)(1) exemption covers "Improvements to single-family dwellings". A replacement of half or more of a structure is treated as a replacement structure, not an improvement or repair (14 CCR §13252(b); `../../coastal-development/references/cdp-when-required.md`).
- So a major remodel in the coastal zone needs a CDP. The Design Review body decides it with the Design Review (§25.07.012(D)); the DRB for single-family and two-family projects (§25.05.040(F)(1)).
- Inside the first-road/300-ft strip, the (A)(1)(c) 10% items independently remove the exemption.

**UNSETTLED — E-93-1 areas.** Categorical Exclusion Order E-93-1 excludes "single family residential development" in eleven areas; its Special Condition 8 requires conformity with the LCP or the order, whichever is more restrictive (the City source document (not included in this plugin)). Whether E-93-1 clears a major remodel in one of those areas has not been decided. Treat the CDP as required and confirm with Planning at pre-application.

### Practical Application

For any Laguna project where Step B classifies the work as a major remodel AND the parcel is in the coastal zone (Step J point-in-polygon or applicant-supplied):

1. Cite **§25.07.004** (CDP required) and the new-development classification (handout paragraph 1; §25.56.011).
2. If the parcel is in the first-road/300-ft strip, also cite the **§25.07.008(A)(1)(c) items**.
3. Determine whether the parcel is in the **appealable area** (§25.07.006: between sea and first public road; within 300 ft of the inland extent of any beach; within 100 ft of any wetland/estuary/stream; within 300 ft of the seaward face of any coastal bluff). This drives noticing and Commission appeal.
4. Route to `../../coastal-development/references/california-baseline.md` for the substantive CDP analysis.

### Non-Major Remodel

A remodel that is not a major remodel is normally exempt under §25.07.008(A)(1) and recorded by Planning (§25.07.008(B)), unless one of (A)(1)(b)-(g) applies. Item (b) (beach, wetland, stream, seaward of mean high tide, within 50 ft of a bluff edge, ESA, highly scenic LUP area) applies anywhere; item (c) only in the strip. UNSETTLED: Ord. 1732 added slopes of 30% or more to the 25.08 ESA definition but is not certified by the Coastal Commission; whether a steep lot is an "environmentally sensitive area" for (A)(1)(b) is not decided. Confirm with Planning at pre-application.

---

## ADUs — E-93-1 Does Not Clear Them

In the Commission report F9a (Nov. 2024 meeting), the Executive Director found that the LCP exemption list (§25.07.008) controls for an ADU added to a single-family home, so Categorical Exclusion E-93-1 does not clear an ADU (the City source document (not included in this plugin); the Commission vote on that interpretation was not checked).

### Operative Rule

When a residential remodel scope **includes an ADU** (attached, detached, JADU, or conversion) AND the parcel is in the coastal zone, flag:

1. The ADU is exempt from the major-remodel calculation (`city-major-remodel-methodology.md`), except Coastal Act section 30253 work on bluff-top, beachfront and coastal-canyon lots.
2. The ADU needs a CDP unless it only converts existing livable space in the primary dwelling (§25.07.008(A)(1)(a); Ord. 1713, LBMC 25.17.010(d)(1)(C)(ii)).
3. The ADU's CDP is separate from any CDP for the rest of the remodel. An ADU-only CDP is decided within 60 days, concurrently with the ADU, with no required hearing and no Coastal Commission appeal (Gov. Code 66329(a), (c)).

### Flag Format

```
## ADU in a Coastal Remodel Scope
**Applicability:** Project scope includes ADU AND parcel is in coastal zone: YES | NO
**Result:** FLAG (if YES) | N/A (if NO)
**Code:** LBMC §25.07.008(A)(1)(a); §25.07.010; Coastal Commission report F9a (Nov. 2024); Ord. 1713 LBMC 25.17.010(d)(1)
**Finding:** E-93-1 does not clear an ADU. The ADU needs a CDP unless it only converts existing livable space in the primary dwelling.
**Action required:** File the ADU & JADU Application with its own CDP Application. Route to `../../adu/SKILL.md`.
```

---

## Categorical Exclusion (E-93-1) — Scope Limited

§25.07.010 incorporates "any categorical exclusion area adopted pursuant to the California Coastal Act." E-93-1 is Laguna's categorical exclusion order for single-family residential development in eleven areas, subject to Special Condition 8 (the LCP or the order, whichever is more restrictive).

For major remodels and bluff/oceanfront work, **do not assume E-93-1 covers the project.** Apply the §25.07.008 analysis and FLAG the E-93-1 question for Planning:
- If §25.07.008(A)(1)(b) applies (beach, wetland, seaward of mean high tide, within 50 ft of a bluff edge, ESA, highly scenic area) → not exempt.
- If §25.07.008(A)(1)(c) applies (in the first-road/300-ft strip: 10% floor area, 10% height, detached structure) → not exempt.
- For repair/maintenance under §25.07.008(A)(3): any addition, enlargement or expansion takes the project out of that exemption.

---

## Ord. 1688 (7/11/2023) — Procedural Amendment, Not Bluff Setback

The §25.07.008 ordinance history confirms Ord. 1688 amended §§25.07.008 and 25.07.012 (CDP procedural rules). Ord. 1688 is **not** in the §25.50.004 ordinance history. The bluff overlay predates Ord. 1688 (Ord. 811 1974 → Ord. 1416 2002 — see `city-bluff-overlay.md`).

When citing CDP procedural rules, Ord. 1688 may be relevant. When citing the bluff setback rule, do **not** attribute to Ord. 1688.

---

## Output Format

```
## Coastal Development Permit — Ch. 25.07
**In coastal zone:** YES | NO (basis: GeoJSON polygon hit | applicant-supplied)
**In appealable area:** YES | NO (basis: GeoJSON polygon hit | applicant-supplied | §25.07.006(A)(1) test)

**CDP Required:** YES | NO | EXEMPT
**Basis:**
  - §25.07.008(A)(1) SFR-improvement exemption applies: YES | NO (note carveouts)
  - §25.07.008(A)(1)(b) location-based carveout fires (beach/wetland/seaward MHW/within 50 ft bluff/ESA/highly scenic): YES | NO
  - §25.07.008(A)(1)(c) project-scale carveout fires (only in the first-road/300-ft strip: 10% floor area / 10% height / detached structure): YES | NO | N/A (outside strip)
  - §25.07.010 categorical exclusion applicable: YES | NO | UNSETTLED (E-93-1; do not assume coverage for a major remodel or bluff/oceanfront work; never for an ADU)
  - §25.07.009 de minimis waiver applicable: YES | NO

**Major Remodel + Coastal Zone:** CDP REQUIRED (new development; E-93-1 area: FLAG UNSETTLED)

**ADU + Coastal Zone:** FLAG — E-93-1 does not clear an ADU (Commission report F9a, Nov. 2024); separate ADU-only CDP under Gov. Code 66329

**Procedural envelope:**
  - Approving authority per §25.07.012(D): [Director / DRB / PC]
  - Public hearing required per §25.07.012(E): YES (appealable) | NO (non-appealable, exempt, or categorically excluded)
  - Notice period: 10 calendar days mail notice; 100 ft / 300 ft radius depending on appealable status
  - CCC appeal window: 10 working days from CCC receipt of notice of final action

**Citation:** LBMC §25.07.004; §25.07.006; §25.07.008(A)(1); §25.07.010; §25.07.012; §25.07.014; Commission report F9a, Nov. 2024 (when ADU + coastal)
**Action required:** [Submit CDP application concurrently with building permit application per §25.07.012(D); provide 10-day notice; route appealable development to CCC after final local action.]
```
