# Laguna Beach — Coastal Development Permit (Ch. 25.07)

This file documents the Laguna-specific overlay for CDP review. The state skill `../../coastal-development/references/california-baseline.md` covers the substantive CDP analysis (appealable areas, categorical exclusions, LCP consistency, public access, resource protections). This file layers in the Laguna-specific procedural rules and two consequential overlay flags: (1) the major-remodel-in-coastal-zone CDP requirement regardless of E-93-1 categorical exclusion, and (2) the CCC F9a-11-2024 ADU coastal-exemption pushback.

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

A major remodel **automatically** crosses these thresholds (50% > 10%) — so SFR-improvement exemption does not apply to a major remodel in the appealable area.

§25.07.008(A)(1)(b) — improvements **on a beach, in a wetland or stream, seaward of the mean high tide line, within fifty feet of a coastal bluff edge, in an ESA, or in a highly scenic area** — never exempt.

§25.07.008(A)(3) — repair and maintenance activities that do not result in addition/enlargement/expansion are exempt, with carveouts for shoreline structures (sea wall revetment, bluff retaining wall, breakwater, groin, culvert, outfall) — substantial alteration of foundation/pilings, placement of rip-rap, replacement of ≥20% of materials with materials of a different kind, and presence of mechanized construction equipment within 20 ft of coastal waters/streams or on any sand area or bluff or ESA — are NOT exempt.

§25.07.008 ordinance history (verbatim trailer): *"(Ord. 1253 § 1, 1992; Ord. 1649 § 2, 2020; Ord. 1653 § 4, 2021; Ord. 1665, 11/16/2021; Ord. 1679 § 4, 2022; Ord. 1688, 7/11/2023)"* — Ord. 1688 amended §25.07.008. (Note: Ord. 1688 amended §25.07 CDP procedures, NOT the bluff overlay — see `city-bluff-overlay.md` for that distinction.)

### §25.07.009 — De Minimis Waiver

Director may waive CDP for de minimis development if (1) within coastal zone but not appealable, not in appealable area, not in CCC-retained-jurisdiction area, and no local public hearing required; (2) consistent with LCP and no individual or cumulative adverse effect on coastal resources; (3) no violation involved. Coastal Commission notice required.

### §25.07.010 — Categorical Exclusions

Verbatim:

> *"Development included in any categorical exclusion area adopted pursuant to the California Coastal Act is exempt from the regulations contained in this chapter except for the notice requirements contained within California Code of Regulations Section 13248."*

E-93-1 is Laguna's categorical exclusion. Its scope is **narrower** than Laguna staff historically assumed — see CCC F9a-11-2024 below.

### §25.07.012 — Procedure

Director (or designee) determines CDP applicability (within CCC original jurisdiction, appealable to CCC, non-appealable, or categorically excluded/exempt). CDP review processed concurrently with other permits required by underlying zoning. §25.07.012(F) review criteria — 9 LCP consistency findings.

### §25.07.014 — Noticing

- Appealable development: 10-day mail notice prior to first public hearing or within 10 days of accepting the application (whichever is greater); to applicant, persons who requested notice, all property owners within 100 ft, all residents within 100 ft, and the Coastal Commission.
- Non-appealable development: 10-day mail notice; property owners within 300 ft, residents within 100 ft, Coastal Commission. Newspaper publication if Planning Commission hearing.

### §25.07.016 — Appeals

Appealable development may be appealed to CCC by a qualified appellant within **10 working days** from the date of CCC receipt of the notice of final action. Grounds limited to (a) non-conformity with the certified LCP or (b) failure to comply with public access policies of Coastal Act Ch. 3.

---

## Major Remodel in Coastal Zone — Always Requires CDP

### Operative Rule

A "major remodel" — as determined by the Step B methodology in `city-major-remodel-methodology.md` — is "development" under §25.07.006(D) and is NOT within the §25.07.008(A)(1) SFR-improvement exemption (because the carveouts in §25.07.008(A)(1)(c)(1) at 10% floor area, (c)(2) at 10% height, (c)(3) at detached-structure construction will all fire long before the project reaches the 50% major-remodel threshold).

A major remodel in the coastal zone therefore **always requires a CDP**, regardless of any E-93-1 categorical exclusion claim. The categorical exclusion mechanism in §25.07.010 doesn't reach a project of major-remodel scope.

### Practical Application

For any Laguna project where Step B classifies the work as a major remodel AND the parcel is in the coastal zone (Step J point-in-polygon or applicant-supplied):

1. Cite **§25.07.004** (CDP required).
2. Cite the **§25.07.008(A)(1)(c) carveouts** (10% floor area, 10% height) showing why SFR exemption does not apply.
3. Determine whether the parcel is in the **appealable area** (§25.07.006(A)(1) — between sea and first public road; within 300 ft of inland extent of any beach; within 100 ft of any wetland/estuary/stream; within 300 ft of seaward face of any coastal bluff). This drives noticing + CCC appeal availability.
4. Route to `../../coastal-development/references/california-baseline.md` for the substantive CDP analysis.

---

## CCC F9a-11-2024 — ADU Coastal Exemption Pushback

The California Coastal Commission's F9a-11-2024 Notice of Pending Action (and subsequent CCC enforcement direction) **rejected Laguna's E-93-1 ADU categorical exemption** as applied to ADUs in the coastal zone. ADUs in Laguna's coastal zone still need a Coastal Development Permit.

### Operative Rule

When a residential remodel scope **includes an ADU** (attached, detached, JADU, or conversion) AND the parcel is in the coastal zone, **flag prominently**:

1. ADU is exempt from the major-remodel calculation (per `city-major-remodel-methodology.md`, the only carveout).
2. ADU is **NOT** exempt from CDP merely because the city's E-93-1 categorical exclusion claims it.
3. The ADU likely still needs a CDP processed under Ch. 25.07.
4. This is **independent** of whether the rest of the remodel triggers a CDP.

### Practical Application

For any Laguna project where scope includes an ADU AND the parcel is in the coastal zone:

1. Cite **CCC F9a-11-2024** (the CCC pushback) in the corrections-letter body.
2. Cite **§25.07.010** (categorical exclusion provision) and note that its scope was narrowed for ADUs.
3. Process the ADU CDP separately or concurrently with any rest-of-remodel CDP.
4. Route to `../../adu/SKILL.md` for ADU-specific Laguna review.
5. Route to `../../coastal-development/references/california-baseline.md` for the substantive CDP analysis on the ADU portion.

### Flag Format

```
## CCC F9a-11-2024 — ADU Coastal Exemption Pushback
**Applicability:** Project scope includes ADU AND parcel is in coastal zone: YES | NO
**Result:** FLAG (if YES) | N/A (if NO)
**Code:** LBMC §25.07.010 (categorical exclusion); CCC F9a-11-2024 (Notice of Pending Action)
**Finding:** The CCC F9a-11-2024 rejected Laguna's E-93-1 ADU categorical exemption as applied to ADUs in the coastal zone. The ADU portion of this scope likely still requires a CDP regardless of any E-93-1 exemption claim.
**Action required:** Process ADU CDP under Ch. 25.07. Do not rely on E-93-1 categorical exclusion for the ADU portion. Route to `../../adu/SKILL.md` and `../../coastal-development/references/california-baseline.md` for CDP analysis.
```

---

## Categorical Exclusion (E-93-1) — Scope Limited

§25.07.010 incorporates "any categorical exclusion area adopted pursuant to the California Coastal Act." E-93-1 is Laguna's categorical exclusion order. Its scope is narrower than Laguna staff historically assumed; CCC F9a-11-2024 narrowed it further for ADUs.

For major remodels and bluff/oceanfront work, **do not assume E-93-1 covers the project.** Apply the §25.07.008 analysis instead:
- If the carveouts in §25.07.008(A)(1)(b) (beach, wetland, seaward of MHW, within 50 ft of bluff edge, ESA, highly scenic area) apply → never exempt.
- If the carveouts in §25.07.008(A)(1)(c) (10% floor area, 10% height, detached structure) fire → SFR exemption does not apply.
- For repair/maintenance carveouts under §25.07.008(A)(3): note that any addition/enlargement/expansion takes the project out of the repair/maintenance exemption.

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
  - §25.07.008(A)(1)(c) project-scale carveout fires (10% floor area / 10% height / detached structure): YES | NO
  - §25.07.010 categorical exclusion applicable: YES | NO (E-93-1 scope narrowed; do not assume coverage for major remodel or bluff/oceanfront work)
  - §25.07.009 de minimis waiver applicable: YES | NO

**Major Remodel + Coastal Zone:** AUTO-CDP-REQUIRED (if Step B = major remodel AND coastal zone = YES)

**ADU + Coastal Zone:** CCC F9a-11-2024 FLAG (ADU still requires CDP regardless of E-93-1)

**Procedural envelope:**
  - Approving authority per §25.07.012(D): [Director / DRB / PC]
  - Public hearing required per §25.07.012(E): YES (appealable) | NO (non-appealable, exempt, or categorically excluded)
  - Notice period: 10 calendar days mail notice; 100 ft / 300 ft radius depending on appealable status
  - CCC appeal window: 10 working days from CCC receipt of notice of final action

**Citation:** LBMC §25.07.004; §25.07.006; §25.07.008(A)(1); §25.07.010; §25.07.012; §25.07.014; CCC F9a-11-2024 (when ADU + coastal)
**Action required:** [Submit CDP application concurrently with building permit application per §25.07.012(D); provide 10-day notice; route appealable development to CCC after final local action.]
```
