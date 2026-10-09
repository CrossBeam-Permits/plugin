# California Baseline — ADU (Accessory Dwelling Unit)

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California ADU Regulatory Decision Engine

This skill contains the California state-level ADU (Accessory Dwelling Unit) and JADU (Junior Accessory Dwelling Unit) rules extracted from the HCD ADU Handbook (January 2025) and the January 2026 Addendum. It covers Government Code §§ 66310-66342 (including new §§ 66311.5, 66333.5) as amended through January 1, 2026.

**What this covers**: State law — the floor that cities cannot go below. Cities may be more permissive but cannot impose standards more restrictive than what is stated here.

**What this does NOT cover**: City/county-specific ordinances, federal requirements (FHA, ADA), or project-specific engineering.

### How to Use This Skill

When answering an ADU question, follow the 4-step decision tree below. Each step tells you which reference files to load. Load only what you need — most questions require 3-5 reference files, not all 28.

After loading references, check the **Quick-Reference Thresholds** table below for the key numbers that come up in almost every query.

---

### Decision Tree Router

#### STEP 0 — Wildfire / WUI Pre-Check

For Laguna Beach the wildfire overlay is set citywide: use the `wildfire: 'all'` row below, and the `wildfire-wui` skill in this plugin for the Chapter 7A / WUI Code details.

| Overlay status                  | What to do                                                                                                                                                                                                                |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not loaded (no FHSZ in city)    | Skip WUI / Chapter 7A — the standard ADU checks below are complete on their own.                                                                                                                                          |
| Loaded — `wildfire: 'partial'`  | City has some FHSZ parcels but not the whole jurisdiction. Surface Chapter 7A findings **conditionally** with a disclaimer pointing applicants to the CalFire FHSZ viewer (osfm.fire.ca.gov). Do not fail on WUI grounds without parcel confirmation. State ADU law (§ 66329) also limits the FHSZ basis on which ADUs may be denied — see `zoning-hazards.md`. |
| Loaded — `wildfire: 'all'`      | Entire or substantial majority of the city is FHSZ. Apply Chapter 7A findings, prefaced with a brief "assumed FHSZ based on city coverage; confirm via osfm.fire.ca.gov — if outside, the WUI findings below do not apply" disclaimer. |

When the overlay is loaded, follow `../../wildfire-wui/SKILL.md` Steps 1–3 for component checks (roof assemblies, eaves/vents, walls/windows/doors/decks, defensible space) and fold those findings into the ADU review output. ADU-specific FHSZ scope (e.g. the ADU exception to sprinklering, statutory denial protections) stays in `standards-fire.md` and `zoning-hazards.md`.

#### STEP 1: Classify the Lot Type

What kind of lot is the ADU proposed on?

| Lot Type | Load These References |
|----------|----------------------|
| **Single-family lot** | `unit-types-66323.md`, `unit-types-adu-general.md` |
| **Multifamily lot** (2+ existing units) | `unit-types-multifamily.md`, `unit-types-66323.md` |
| **JADU only** (within existing/proposed single-family dwelling) | `unit-types-jadu.md` |
| **Unsure / mixed question** | `unit-types-66323.md` (start here — it has the combinations table) |

#### STEP 2: Classify the ADU Construction Type

How is the ADU being built?

| Construction Type | Load These References |
|-------------------|----------------------|
| **New detached construction** | `standards-height.md`, `standards-size.md`, `standards-setbacks.md` |
| **Conversion from existing space** (garage, basement, etc.) | `standards-size.md`, `zoning-nonconforming.md` |
| **Attached addition** to existing dwelling | `standards-height.md`, `standards-size.md`, `standards-setbacks.md` |
| **Manufactured/factory-built home** | `special-manufactured.md` |

#### STEP 3: Check Situational Modifiers

Does any of the following apply? Load the additional references.

When the same file reports `parcel.geometry.notable: true`, use that observation only to trigger a local lot-definition and setback question. Load the city zoning definitions and any diagram they incorporate; do not classify front, side, or rear lot lines from assessor geometry. Preserve the state floor: qualifying non-conversion ADUs may be required to provide no more than four feet from side and rear lot lines, and qualifying conversions may require no setback (Gov. Code §§66314(d)(7), 66321(b)(3), 66323(a)). An unavailable or non-notable geometry result is not proof that title, survey, easement, access, or fire issues are absent.

| Situation | Load These References |
|-----------|----------------------|
| **Near public transit** (parcel-resolved the parcel facts transit block) | `standards-height.md` (18 ft bonus), `standards-parking.md` (exemptions) |
| **In coastal zone** | `zoning-hazards.md` |
| **In fire hazard severity zone** | `zoning-hazards.md`, `standards-fire.md` |
| **In historic district** | `zoning-general.md`, `standards-design.md` |
| **Property has an HOA** | `ownership-hoa.md` |
| **Rental / short-term rental question** | `ownership-use.md` |
| **Selling or converting ADU to condo** | `ownership-sales.md` |
| **SB 9 lot split involved** | `special-sb9.md` |
| **Nonconforming zoning or building code violations** | `zoning-nonconforming.md` |
| **Solar / energy code question** | `standards-solar.md` |
| **Fire sprinkler question** | `standards-fire.md` |
| **Parking question** | `standards-parking.md` |
| **Design review / subjective standards question** | `standards-design.md` |
| **Irregular parcel geometry** (`parcel.geometry.notable`) | City zoning definitions/diagrams, `standards-setbacks.md` |

#### STEP 4: Check Process, Fees, and Compliance

What stage is the project at?

| Topic | Load These References |
|-------|----------------------|
| **Permit application / timeline / pre-approved plans** | `permit-process.md` |
| **Impact fees / connection fees** | `permit-fees.md` |
| **Financing / grants / loans** | `permit-funding.md` |
| **Unpermitted existing ADU** (legalization) | `compliance-unpermitted.md` |
| **Local ordinance question / HCD enforcement** | `compliance-ordinances.md` |
| **Housing element / RHNA credit** | `compliance-housing.md` |
| **Utility connections** | `compliance-utilities.md` |
| **Legislative history / bill tracking** | `legislative-changes.md` |
| **Definition of a term** | `glossary.md` |

---

### Quick-Reference Thresholds

These numbers come up in almost every ADU query. Check here first before loading a reference file — you may already have the answer.

| Threshold | Value | Reference File |
|-----------|-------|----------------|
| JADU maximum size | 500 sq ft of **interior livable space** | `unit-types-jadu.md` |
| 66323(a) converted/detached max | 800 sq ft | `unit-types-66323.md` |
| Minimum ADU size (efficiency unit) | 150 sq ft | `standards-size.md` |
| Min. local max allowed (0-1 bedroom) | 850 sq ft of **interior living space** | `standards-size.md` |
| Minimum ADU size (2+ bedrooms) | 1,000 sq ft of **interior living space** | `standards-size.md` |
| Maximum detached ADU (no local ordinance) | 1,200 sq ft of **interior living space** | `standards-size.md` |
| Fee exemption threshold | ≤ 750 sq ft of **interior livable space** (§ 66311.5) | `permit-fees.md` |
| Maximum side/rear setback | 4 ft | `standards-setbacks.md` |
| Detached height — base | 16 ft | `standards-height.md` |
| Detached height — near transit or multistory primary | 18 ft | `standards-height.md` |
| Detached height — transit + additional 2 ft for roof pitch | 18 ft (+2 ft) | `standards-height.md` |
| Attached ADU height | 25 ft (or primary dwelling height) | `standards-height.md` |
| Completeness check deadline | **15 business days** | `permit-process.md` |
| Approval/denial deadline | 60 days | `permit-process.md` |
| Minimum rental term | 30 days | `ownership-use.md` |
| Unpermitted ADU amnesty cutoff | Before January 1, 2020 | `compliance-unpermitted.md` |
| Multifamily detached ADU cap | 8 units or 25% of existing | `unit-types-multifamily.md` |

---

### Key Principles

1. **State preemption**: State law sets minimum ADU rights. Cities cannot impose standards more restrictive than those in these reference files. Cities *can* be more permissive.

2. **Ministerial approval**: ADU permits must be approved ministerially (no discretionary review, no public hearings, no CEQA). See `permit-process.md`.

3. **No density count**: ADUs and JADUs do not count toward allowable density for the lot. See `zoning-general.md`.

4. **Objective standards only**: Cities may only apply objective (measurable, verifiable) development standards to ADUs — not subjective design review. See `standards-design.md`.

5. **Owner-occupancy**: Required for JADUs **only if the JADU shares sanitation facilities** with the primary structure. Not required for ADUs (except for separate conveyance under AB 1033). See `ownership-use.md`.

---

### Energy Compliance (Title 24 Part 6) — Delegated

This skill does **not** reproduce Title 24 Part 6 energy requirements. Title 24 Part 6 is generic residential state law — it applies to ADUs the same way it applies to any other dwelling unit on the same lot type, and duplicating it here would recreate the overlay-bloat pattern we eliminated from city skills.

For envelope, HVAC, fenestration, insulation, cool roof, water heater, solar PV, duct insulation, radiant barrier, and air-leakage compliance, load the appropriate residential energy skill based on ADU type:

| ADU Context | Load This Reference |
|-------------|---------------------|
| Detached or attached ADU on a **single-family lot** | `../../single-family-residential/references/energy.md` |
| ADU on a **multifamily lot** (2+ existing units) | `../../multi-unit-residential/references/energy-envelope.md` |
| Converted ADU (garage, basement, existing interior space) | Same as host lot type above — alteration rules in the referenced file apply |

**ADU-specific overrides (stay in this skill):** Check `standards-solar.md` for ADU-only size thresholds — AB 2188 solar streamlining, and the ≤ 750 sq ft interior exemption from the Title 24 new-construction PV mandate per Gov. Code § 65850.12. These are the only energy-code items that differ for ADUs vs. other dwellings and they stay here.

**Do not** transcribe Title 24 tables, CZ values, or prescriptive numbers into this skill. If you find yourself reaching for a CZ-indexed requirement, you are in the wrong skill — go to the residential energy reference above.
