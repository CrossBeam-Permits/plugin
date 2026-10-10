# California Baseline — Coastal Development Permit

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## Coastal Development — State-Level Skill

> California Coastal Act (PRC Division 20) + Title 14 CCR Division 5.5
> This skill covers **state law only**. City-specific CDP ordinances, fees, notice radii, and LCP details are in city overlay skills.

### When This Skill Applies

This skill is triggered when any of the following are true:
- The property is in the **Coastal Zone** (or the user is asking whether it is)
- The project involves a **Coastal Development Permit (CDP)**
- The question references the **California Coastal Act**, **Coastal Commission**, **LCP**, or **ESHA**
- The project is in a city that has a certified Local Coastal Program

### Decision Tree

#### STEP 1 — Is the property in the Coastal Zone?

If unknown, **ask the applicant**. Do not guess.

> **Tier 1 approach (current):** Ask the contractor/applicant directly.
> Future: geocoding + CCC boundary shapefile check.

- If **YES** → proceed to Step 2
- If **NO** → this skill does not apply. Standard permit rules only.
- If **UNKNOWN** → ask: "Is the property located within the California Coastal Zone? Your city's planning department or the Coastal Commission website can confirm this."

#### STEP 2 — Does the development require a CDP?

Load: `cdp-when-required.md`

Start with PRC §30600, including the emergency-project exceptions in §30600(e), then test every applicable §30610 exemption and its implementing regulation:
- **(a)** Improvements to an existing single-family residence; check 14 CCR §13250 for classes that still require a CDP
- **(b)** Improvements to a structure other than an SFR or public-works facility; check 14 CCR §13253
- **(c)** Maintenance dredging of existing navigation channels under the stated federal-permit route
- **(d)** Repair or maintenance without addition, enlargement, or expansion; check 14 CCR §13252
- **(e)** A development category or geographic category excluded by Commission order
- **(f)** A necessary utility connection between an existing service facility and approved development
- **(g)** Qualifying replacement of a non-public-works structure destroyed by disaster
- **(h)** The specified existing multi-unit residential time-share conversions
- **(i)** A temporary event the executive director finds has no significant adverse impact under Commission guidelines

Also test Commission categorical exclusions and the de minimis-waiver route under PRC §30624.7 and 14 CCR §§13238-13238.2. Do not decide an exemption from the shorthand above; load `cdp-when-required.md` and confirm the current statutory, regulatory, and any applicable Commission-order conditions.

- If an **exception, exemption, exclusion, or effective waiver applies** → document the exact basis and continue routing all other permits that may be required.
- If a **CDP is required** → proceed to Step 3.

#### STEP 3 — Who issues the CDP?

Load: `cdp-process.md`, `lcp-overview.md`

- **Certified LCP** → local government generally issues the CDP under the LCP; separately check Commission-retained jurisdiction and appealability.
- **Before LCP certification** → determine whether the local government is exercising PRC §30600(b), has delegated authority under §30600.5, or the Commission is the issuer under §30600(c). Also check whether §30601 requires a Commission CDP in addition to a local permit.
- **Local action before LCP certification or under §30600.5 delegation** → route appeals under PRC §30602, including §30600.5(d).
- **Post-LCP local action** → apply the exact PRC §30603 categories and appeal rules. Load `cdp-appeals.md` and `appealable-areas.md`.

#### STEP 4 — What resource protection policies apply?

Load the applicable resource protection references based on site characteristics:

| Site Characteristic | Load Reference |
|---|---|
| Near the shoreline / beach | `resource-protection-access.md` |
| Visitor-serving area / recreation | `resource-protection-recreation.md` |
| Near marine habitat, ESHA, wetlands | `resource-protection-marine.md` |
| Scenic area / visual corridor | `resource-protection-scenic.md` |
| Coastal bluff / hazard area / erosion | `resource-protection-landforms.md` |
| Agricultural land | `resource-protection-agriculture.md` |

If unsure which apply, load all Chapter 3 resource-protection references. The operative standard depends on the authority path: a nondelegated pre-LCP route applies §30604(a); interim delegation under §30600.5(c) uses conformity with the certified land use plan; after the §30519 transfer conditions, §30604(b) requires certified-LCP conformity; and §30604(c) adds the public-access and public-recreation finding for specified shoreline development.

#### STEP 5 — What findings must be made?

Load: `cdp-process.md`

For a **nondelegated pre-LCP route** (§30604(a)):
- Proposed development conforms with Chapter 3 policies
- Development will not prejudice local government's ability to prepare conforming LCP

For **interim delegated authority** (§30600.5(c)):
- The local government, or Commission on appeal under §30602, finds conformity with the certified land use plan.

For **post-LCP certification** (§30604(b)):
- Proposed development conforms with the certified LCP

For **development between the nearest public road and the sea or the shoreline of any body of water in the coastal zone** (§30604(c)):
- The permit also includes a specific finding of conformity with Chapter 3's public-access and public-recreation policies; this does not replace the §30604(b) certified-LCP finding.

### Quick-Reference Thresholds

| Item | Threshold | Citation |
|---|---|---|
| CDP default | Required for coastal-zone development unless a §30600 exception, §30610 exemption/exclusion, or effective waiver applies | PRC §30600, §30610, §30624.7 |
| SFR improvement exemption | Existing-SFR improvements, subject to the classes that still require a permit | PRC §30610(a), 14 CCR §13250 |
| Repair/maintenance exemption | No addition, enlargement, or expansion; extraordinary regulated methods can still require a permit | PRC §30610(d), 14 CCR §13252 |
| De minimis waiver | No potential for adverse effects and Chapter 3 consistency, subject to the statutory and regulatory process | PRC §30624.7, 14 CCR §§13238-13238.2 |
| Appeal period | 10 working days from Commission receipt of the local government's notice of final action | PRC §30603(c) |
| Commission hearing setting | No later than 49 working days after the application or appeal is filed | PRC §30621(a) |
| Commission-permit commencement | Generally 2 years from the Commission vote unless a different limit is imposed; 5 years for qualifying 100% affordable housing | 14 CCR §13156(g); extensions: §13169 |

### Key Principle

**The Coastal Act is a state-level overlay** — it applies in addition to local zoning, building codes, and other permit requirements. If the full §30600/§30610/waiver analysis shows that a CDP is required, the project needs both:
1. The CDP from the authorized issuer
2. All other permits required for that project

State law sets the framework. Cities implement via certified LCPs but cannot weaken Coastal Act protections.
