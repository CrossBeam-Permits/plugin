# California Baseline — Demolition (Full Structure)

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Demolition -- State Regulatory Decision Engine

This skill governs **FULL-STRUCTURE demolition** in California: the complete or substantial demolition of a building or its primary structural elements. Examples include whole-house teardown, garage demo to slab, commercial shell demolition, partial demolition of load-bearing walls/structural framing, and any demolition that removes the exterior envelope.

**Boundary -- this skill vs. california-ltia-demolition:** LTIA covers interior non-structural gut-outs of tenant spaces (drywall, finishes, fixtures only). The moment a project touches a load-bearing wall, the exterior envelope, the roof structure, or removes a whole building, it is full demolition and belongs to THIS skill. See `boundary-vs-ltia.md` for the decision matrix.

**What this covers:** State building code (CBC Ch. 33), regional AQMD asbestos rules (SCAQMD / BAAQMD -- the two AQMDs that cover the bulk of California population), federal lead-paint rules as enforced in California (EPA RRP + CDPH Title 17), CALGreen waste diversion, tenant relocation noticing where applicable, and utility-disconnect prerequisites. Every California city must enforce at least these standards.

**What this does NOT cover:** Title 8 Cal/OSHA worker safety (separate regulatory domain), federal NESHAP enforcement procedures, CEQA review (handled at planning/CEQA lead-agency level, not building), city-specific dust-control ordinances, historic-preservation overlays, or local demolition tax/in-lieu fees. Use the city overlay skill for city-specific additions.

---

### How to Use This Skill

When reviewing a full-structure demolition permit, follow the decision tree. Load only the reference files you need.

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (plans + checklist, pass/fail out) | `cbc-chapter-33.md`, `asbestos-neshap-rule-1403.md`, `cd-debris-diversion.md`, `utility-disconnect.md` |
| **Boundary question** (is this LTIA or full demo?) | `boundary-vs-ltia.md` |
| **Pedestrian-protection / site-safety question** | `cbc-chapter-33.md` |
| **Asbestos / AQMD notification question** | `asbestos-neshap-rule-1403.md` |
| **Lead-paint question (pre-1978 housing)** | `lead-safe-work-pre-1978.md` |
| **Waste diversion / CALGreen question** | `cd-debris-diversion.md` |
| **Tenant displacement / relocation question** | `relocation-noticing.md` |
| **Utility disconnect / sign-off question** | `utility-disconnect.md` |

#### STEP 2: Walk the Review Checklist

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Scope correctly classified as full demolition?** | Plans show whole-building, load-bearing, exterior-envelope, or structural-framing removal. If interior-only / non-structural, route to LTIA skill instead. | Project description + CEBC 701.2 boundary | `boundary-vs-ltia.md` |
| 2 | **Demolition plans + schedule submitted?** | Construction documents and demolition schedule submitted as required by building official. Existing floor plan, site plan, and demo extents shown. | CBC 3303.1 | `cbc-chapter-33.md` |
| 3 | **Site safety plan submitted and approved?** | Written site safety plan with all 13 components (site safety director, fire-dept access, extinguisher locations, hot-work plan, hazmat storage, etc.) approved before permit issuance. | CBC 3302.1, 3302.1.1 | `cbc-chapter-33.md` |
| 4 | **Pedestrian protection per Table 3306.1?** | Construction railings, barriers, or covered walkways shown per height-vs-lot-line table. Walkways min 4 ft wide, accessible. Directional barricades where walkway enters street. | CBC 3306.1, 3306.2, 3306.3, Table 3306.1 | `cbc-chapter-33.md` |
| 5 | **Adjacent-property protection + 10-day excavation notice?** | Written notice to adjacent property owners at least 10 days before any excavation. Protection of footings, party walls, chimneys, skylights shown. | CBC 3307.1 | `cbc-chapter-33.md` |
| 6 | **Vacant-lot grading note?** | Plans state lot will be filled/graded to existing grade or jurisdiction standard after structure is removed. | CBC 3303.4 | `cbc-chapter-33.md` |
| 7 | **Water-accumulation / erosion control?** | Storm-water drainage during construction addressed (CALGreen Ch. 4 Div. 4.1 for sites under 1 acre). Foundation/adjacent-property water protection shown. | CBC 3303.5, 3304.1.5 | `cbc-chapter-33.md` |
| 8 | **AQMD asbestos survey + notification?** | Pre-demolition asbestos survey by CAC/CSST attached. AQMD Rule 1403 (SCAQMD) or Reg 11 Rule 2 (BAAQMD) notification submitted ≥10 working days before demo start. Applies regardless of building age. | SCAQMD Rule 1403; BAAQMD Reg 11-2-401.3 | `asbestos-neshap-rule-1403.md` |
| 9 | **Pre-1978 lead-paint plan?** | If structure built pre-1978: EPA RRP-Certified Renovator on file OR Cal/OSHA Title 8 §1532.1 lead-work plan. Lead survey OR presumed-positive declaration. | 40 CFR 745 Subpart E; CDPH Title 17 §35001+; Cal/OSHA T8 §1532.1 | `lead-safe-work-pre-1978.md` |
| 10 | **Utility disconnect confirmations?** | Written disconnect / cap confirmations from gas, electric, water, sewer (and any other service: data, fuel-oil). Must be in file before permit issues. | CBC 3303.6; utility-co. policies | `utility-disconnect.md` |
| 11 | **65% C&D waste diversion plan?** | Construction Waste Management Plan submitted (CALGreen 4.408 residential / 5.408 nonresidential). Plan identifies materials, diversion facilities, source-separated vs. single-stream. Hauler receipts required at final. | CALGreen 4.408.1 / 5.408.1 | `cd-debris-diversion.md` |
| 12 | **Universal waste called out?** | Fluorescent lamps, ballasts, mercury thermostats, refrigerants, batteries to be diverted from landfill; list in construction docs. | CALGreen 4.408.2 / 5.408.2 | `cd-debris-diversion.md` |
| 13 | **Standpipe maintained (multi-story demo)?** | If existing standpipe in structure: maintained operable during demo; not demolished more than one floor below current demo floor. | CBC 3311.2 | `cbc-chapter-33.md` |
| 14 | **Fire extinguishers + fire watch (where applicable)?** | Portable extinguishers at stairs and storage sheds. Fire watch during nonworking hours for buildings >40 ft tall or new MS construction >50,000 sf/story. | CBC 3309.1, 3314.1 | `cbc-chapter-33.md` |
| 15 | **Tenant relocation notice (if displacing residents)?** | If a public entity is causing displacement OR a local rent ordinance applies: tenant relocation noticing per Gov. Code §7260 et seq. + city ordinance. Owner-occupied / vacant structure: N/A. | Gov. Code §§7260–7277 | `relocation-noticing.md` |
| 16 | **C-21 (Demolition) contractor?** | CSLB C-21 license required for standalone demolition. Class B General Building acceptable when demo is incidental to a broader new-construction permit. | CSLB B&P §7058 / 16 CCR §832-21 | `cbc-chapter-33.md` |
| 17 | **Means of egress maintained (occupied adjacent space)?** | Where structure is attached to or shares egress with an occupied building, egress and accessible egress maintained at all times or temporary egress approved. | CBC 3303.3, 3310.2 | `cbc-chapter-33.md` |

#### STEP 3: Output the Review Result

For each item: **PASS / FAIL / FLAG / N/A** with code citation and one-sentence rationale.

---

### Key Principles

1. **Full demolition is structural by definition.** If structural elements aren't being touched, this is the wrong skill -- route to LTIA. See `boundary-vs-ltia.md`.

2. **Asbestos survey is universal in SCAQMD jurisdiction.** Rule 1403 has no construction-year exemption -- every demolition requires a survey by a Certified Asbestos Consultant (CAC) or CSST before notification, regardless of building age. The pre-1980 trigger is a *practical risk* threshold, not a regulatory exemption. BAAQMD also requires notification for every demolition.

3. **Pre-1978 = lead. Pre-1980 = high-risk asbestos.** These thresholds are distinct and easy to confuse:
   - **1978** -- federal residential lead-based-paint ban (HUD 1978). RRP Rule + Cal/OSHA T8 §1532.1 trigger.
   - **1980** -- practical cutoff for high-likelihood asbestos in friable building materials (Cal/OSHA presumes ACM in flooring/insulation/plaster pre-1981 unless tested).

4. **65% diversion is mandatory, not aspirational.** CALGreen §4.408 (residential) and §5.408 (nonresidential) both require 65% of nonhazardous C&D waste recycled or salvaged. Hauler receipts at final inspection.

5. **Utility disconnects are a permit prerequisite, not an inspection item.** Most California cities require written disconnect/cap confirmations from gas, electric, water, sewer in the permit file *before* issuance. Verify all four (plus any data/fuel-oil) before sign-off.

6. **Tenant relocation noticing only applies in specific circumstances** -- public-entity displacement (Gov. Code §7260) OR a local just-cause / rent-stabilization ordinance with relocation triggers. Owner-occupied teardowns and vacant structures: not applicable.

7. **CEQA, historic-preservation, and zoning are not building-code matters.** Flag them for the planning department but do not block the demolition permit on those grounds at the building-code level.
