# California Baseline — LTIA Demolition

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California LTIA Demolition -- State Regulatory Decision Engine

This skill contains California state-level rules for L.T.I.A. (Limited Tenant Improvement Area) interior non-structural demolition. LTIA demolition covers the gut-out of an existing tenant space in a mall, shopping center, or high-rise building within a pre-designated LTIA zone -- removing all interior finishes, fixtures, and non-structural partitions while capping all utilities, preserving structural elements, and maintaining fire/life safety systems.

**What this covers**: State building code requirements that apply everywhere in California for interior non-structural demolition. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local permit fees, AQMD-specific notification procedures, or the subsequent tenant improvement (TI) build-out (which requires a separate permit). Use the city-level overlay skill for city-specific additions.

### How to Use This Skill

When reviewing an LTIA demolition permit or answering an LTIA demolition code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 3-4 reference files, not all of them.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (plans in, pass/fail out) | `scope-verification-structural.md`, `plan-requirements-submittals.md`, `utility-capping-cpc-cmc-cec.md`, `fire-rated-assemblies-cbc707-714.md` |
| **Scope verification question** (is this truly non-structural?) | `scope-verification-structural.md` |
| **Utility capping question** (how to cap electrical/plumbing/gas/HVAC) | `utility-capping-cpc-cmc-cec.md` |
| **Fire separation / rated wall question** | `fire-rated-assemblies-cbc707-714.md` |
| **Egress or corridor question** | `egress-corridors-cbc1003-1020.md` |
| **Accessibility / path of travel question** | `accessibility-path-of-travel.md` |
| **Waste management / recycling question** | `waste-management-calgreen-5408.md` |
| **Construction safety / safeguards question** | `demolition-safeguards-cbc3303.md` |
| **Existing building code classification question** | `existing-building-cebc-601-701.md` |
| **General LTIA code question** | `scope-verification-structural.md`, `demolition-safeguards-cbc3303.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Scope is non-structural?** | Plans clearly indicate ONLY non-load-bearing partitions are removed. No structural columns, load-bearing walls, shear walls, or exterior envelope work. Structural columns identified and marked for protection. | CEBC 701.2, 805.2, 805.3 | `scope-verification-structural.md` |
| 2 | **Demolition plan complete?** | Existing and demo floor plan shows all rooms, doors, demising walls. Demolition scope clearly indicated. Area of demolition stated in SF. Occupancy type listed per room. | CBC 3303.1, CEBC 601.2 | `plan-requirements-submittals.md` |
| 3 | **Demising walls remain?** | Walls between adjacent tenant spaces (fire partitions) are shown to remain. Fire-resistance rating noted. | CBC 708.1, 708.3 | `fire-rated-assemblies-cbc707-714.md` |
| 4 | **Fire separation walls shown?** | Fire barriers, fire-rated corridors, and door ratings identified on plans. Penetrations through fire-rated assemblies will be firestopped. | CBC 707.1, 707.7, 714.2, 716.1 | `fire-rated-assemblies-cbc707-714.md` |
| 5 | **Egress path shown?** | Egress path from tenant space to building exits clearly marked. All exit locations shown. Dead-end corridors comply with limits. | CBC 1003.6, 1020.5, 3303.3, 3310.2 | `egress-corridors-cbc1003-1020.md` |
| 6 | **Accessibility / path of travel shown?** | Path of travel from public sidewalk/parking to tenant space shown. Main entrance, restrooms, drinking fountains identified. Note on plans that accessibility requirements will be maintained. | CBC 11B-206, 11B-207 | `accessibility-path-of-travel.md` |
| 7 | **Reflected ceiling plan (if applicable)?** | If ceiling demolition is in scope, reflected ceiling plan provided showing items to be removed and items to remain (sprinklers, smoke detectors). | Standard practice | `plan-requirements-submittals.md` |
| 8 | **Utility capping addressed?** | Plans indicate that all electrical, plumbing, gas, and HVAC will be properly capped/disconnected. Note on plans: "All utility lines must be properly and safely capped as needed." | CBC 3303.6, CPC 1206.3 | `utility-capping-cpc-cmc-cec.md` |
| 9 | **Electrical tie-back to panels?** | Electrical components at removed fixtures/devices to be tied back to panels. Circuits de-energized and properly terminated. | CEC, CBC 3303.6 | `utility-capping-cpc-cmc-cec.md` |
| 10 | **Gas piping capped gastight?** | Gas outlets capped with screw joint fittings, gastight. Branch valve shut off. | CPC 1206.3 | `utility-capping-cpc-cmc-cec.md` |
| 11 | **Plumbing capped?** | Water supply lines capped at nearest valve. DWV connections capped/plugged. Plumbing stacks to be reused (not demolished). | CPC, CBC 3303.6 | `utility-capping-cpc-cmc-cec.md` |
| 12 | **HVAC ducts capped?** | Open duct ends sealed. Fire/smoke dampers preserved. Shared ductwork maintained. | CMC, CBC 3303.6 | `utility-capping-cpc-cmc-cec.md` |
| 13 | **Waste diversion note on plans?** | Plans include: "65% minimum of nonhazardous construction and demolition waste shall be recycled and/or salvaged for reuse." (CALGreen 5.408.1) | CALGreen 5.408.1 | `waste-management-calgreen-5408.md` |
| 14 | **Lead/asbestos testing noted?** | For buildings pre-1978: lead testing may be required. AQMD notification for asbestos prior to permit issuance. | State/federal hazmat regulations | `waste-management-calgreen-5408.md` |
| 15 | **Universal waste addressed?** | Fluorescent lamps, ballasts, mercury thermostats to be disposed as universal waste, not in general debris. | CALGreen 5.408.2 | `waste-management-calgreen-5408.md` |
| 16 | **Required notes on plans?** | General compliance note, fire/life safety/accessibility note, utility capping note, shoring note, waste diversion note, scope limitation note. | Various | `plan-requirements-submittals.md` |
| 17 | **Shoring note present?** | Plans include: "Contractor is responsible for all temporary shoring prior to the start of demolition." | Standard practice | `plan-requirements-submittals.md` |
| 18 | **Door removal scope complete?** | ALL doors and frames at demolition walls AND at walls slated to remain shall be removed (except exterior doors and doors required for egress or fire separation). This includes doors at non-demo partition walls within the tenant space. | Standard practice | `scope-verification-structural.md` |
| 19 | **Site plan requirements met?** | CBC 107.2.6 requires a site plan drawn to scale showing the size/location of new and existing construction, distances from lot lines, established street grades and proposed finished grades, and flood-hazard data where applicable; for demolition it must show construction to be removed and the location/size of construction to remain. Require easements, tenant-space location, access points, north arrow, fire-department access, or a hazardous-material inventory only from a named jurisdiction/agency and current checklist title with edition/effective date, exact locator, geography, project scope, and currency confirmation. | CBC 107.2.6; source-specific additions | `plan-requirements-submittals.md` |
| 20 | **Post-demolition conditions addressed?** | Plans address: contractor coordination with MEP trades and telecom prior to demo; field verification of conditions/dimensions before demo begins; patching/texturing/repair of surfaces where demo meets remaining construction; floors left clean and smooth; walls to receive tape and texture; objects protruding above slab verified and protected/removed/ground/capped; tenant space left broom clean. | Standard practice | `plan-requirements-submittals.md` |
| 21 | **Pre-existing penetrations addressed?** | Non-conforming penetrations through fire-rated assemblies discovered during demolition shall be firestopped with UL-approved materials per CBC 714. | CBC 714.2 | `fire-rated-assemblies-cbc707-714.md` |
| 22 | **Separate TI permit noted?** | Plans indicate that all tenant improvements shall be processed under a separate permit. No other improvements allowed under this permit. | Standard practice | `scope-verification-structural.md` |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what's wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this project

---

### Quick-Reference Tables

#### LTIA Demolition Scope Summary

| Demolish (Remove) | Protect / Remain |
|-------------------|-----------------|
| Non-load-bearing partition walls | Structural columns |
| Ceiling tiles and suspended grid | Demising walls (fire partitions between tenants) |
| Floor finishes (carpet, VCT, vinyl) | Fire barriers and fire-rated corridors |
| Cabinets, millwork, built-ins | Plumbing stacks (shared risers) |
| Plumbing fixtures | Fire/smoke dampers |
| Light fixtures and electrical devices | Sprinkler system (heads may be relocated) |
| Restroom toilet partitions | Building envelope (exterior walls, windows, roof) |
| Doors and frames at demo walls | Fire alarm system components |
| Wall coverings and finishes | Structural framing and load-bearing walls |
| All existing finishes | Exit signage and emergency lighting (during demo) |

#### Utility Capping Summary

| System | Cap Method | Code Reference |
|--------|-----------|---------------|
| Electrical | De-energize, remove to panel, terminate, label | CBC 3303.6, CEC |
| Water supply | Shut valve, cap with approved fitting, leak test | CBC 3303.6, CPC |
| Drain/waste/vent | Cap or plug all open connections | CBC 3303.6, CPC |
| Gas piping | Shut branch valve, cap gastight with screw fitting | CPC 1206.3 |
| HVAC ductwork | Seal open ends, preserve dampers | CBC 3303.6, CMC |

#### Fire Partition Ratings (Tenant Demising Walls)

| Wall Type | Minimum Rating | Code Section |
|-----------|---------------|-------------|
| Tenant separation in mall | 1 hour | CBC 708.1, 708.3 |
| Corridor wall (sprinklered, B/M, >30 occ.) | 0 hours | CBC Table 1020.2 |
| Corridor wall (unsprinklered, B/M, >30 occ.) | 1 hour | CBC Table 1020.2 |
| Fire barrier between fire areas (B/M) | 2 hours | CBC 707.3.10 |

#### Required Plan Notes

| Note | Content |
|------|---------|
| General compliance | All work shall comply with CBC, CEC, CMC, CPC, CFC, CALGreen, CRC, and local municipal code |
| Fire/life/safety | All applicable fire, life, safety, and accessibility requirements shall be maintained |
| Utility capping | All utility lines must be properly and safely capped as needed |
| Shoring | Contractor is responsible for all temporary shoring prior to the start of demolition |
| Waste diversion | 65% minimum of nonhazardous C&D waste shall be recycled/salvaged (CALGreen 5.408.1) |
| Scope | Interior non-structural demolition only; TI under separate permit |

---

### Additional Checklist Items

#### Contractor Licensing

CSLB C-21 (Demolition) license required for demolition scope work. B (General Building) license may suffice if demolition is incidental to a broader construction scope. For standalone demolition projects, C-21 is required.

---

### Key Principles

1. **Non-structural only**: LTIA demolition is strictly limited to interior, non-structural work. No load-bearing walls, structural columns, or building envelope modifications. If ANY structural element is affected, the project requires a different permit type with structural engineering review.

2. **Building must not become less safe**: Per CEBC 701.2, the demolition must not make the building less safe than its existing condition. This means all fire ratings, egress paths, structural capacity, and accessibility must be maintained.

3. **All utilities must be properly capped**: Per CBC 3303.6, service utility connections shall be discontinued and capped per the applicable code. Gas outlets must be capped gastight (CPC 1206.3). Electrical circuits must be properly terminated at the panel.

4. **Fire-rated assemblies are inviolable**: Demising walls between tenants, fire barriers, fire-rated corridors, and fire/smoke dampers must remain intact and functional. Any penetrations through fire-rated assemblies created or exposed during demolition must be firestopped per CBC 714.

5. **Egress and accessibility maintained during demolition**: Means of egress and accessible means of egress must be maintained at all times during demolition (CBC 3310.2). The path of travel from the public way must be shown on plans.

6. **65% waste diversion**: CALGreen 5.408.1 requires a minimum of 65% of nonhazardous construction and demolition waste to be recycled or salvaged. Waste hauler receipts are required for final inspection.

7. **Hazardous materials are a separate process**: Asbestos testing (AQMD notification) and lead-based paint testing are typically required for pre-1978 buildings before the demolition permit is issued, but they are regulated by separate agencies (AQMD, Cal/OSHA).

8. **TI is always a separate permit**: The LTIA demolition permit covers demo only. All tenant improvement construction requires a separate permit application.
