# California Baseline — Pool Demolition

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Pool/Spa Demolition — State Regulatory Decision Engine

This skill contains California state-level pool and spa demolition rules extracted from the 2025 California Building Code (CBC), California Electrical Code (CEC), and California Plumbing Code (CPC). It covers the most common pool demolition type: partial demolition where the pool shell remains below grade and the area is backfilled for landscape use.

**What this covers**: State building, electrical, and plumbing code requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local standard plan forms, specific inspection scheduling procedures, or fee schedules. Use the city-level pool-demolition skill (e.g., `costa-mesa-pool-demolition`) for city-specific overlays.

#### Full Pool Removal

When the entire pool shell is excavated and removed, the following apply instead of partial-demo items: (1) Grading permit typically required for excavation volume; (2) Backfill compaction report required (licensed geotech); (3) Compaction to 90% per ASTM D1557; (4) C&D waste plan required — concrete shell disposal; (5) Utility disconnects same as partial demo; (6) Final grade to match surrounding lot drainage; (7) No drainage holes/gravel layer needed (shell is removed). Note: City skills may have additional full-removal requirements.

### How to Use This Skill

When reviewing a pool demolition permit or answering a pool demo code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 2-3 reference files, not all of them.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (plans/form data in, pass/fail out) | `demolition-structural-cbc.md`, `electrical-disconnect-cec.md`, `plumbing-gas-capping-cpc.md`, `drainage-grading-erosion.md` |
| **Backfill/compaction question only** | `demolition-structural-cbc.md` |
| **Electrical disconnection question** | `electrical-disconnect-cec.md` |
| **Gas line capping question** | `plumbing-gas-capping-cpc.md` |
| **Water/sewer capping question** | `plumbing-gas-capping-cpc.md` |
| **Drainage or grading question** | `drainage-grading-erosion.md` |
| **Erosion control / BMP question** | `drainage-grading-erosion.md` |
| **General pool demo code question** | `demolition-structural-cbc.md` |

#### STEP 2: Determine Pool vs. Spa

The requirements differ slightly:

| Feature | Pool | Spa |
|---------|------|-----|
| **Drainage holes** | Two (2) at 36" diameter; one at lowest point, equally spaced | One (1) at 36" diameter at lowest point |
| **Coping/bond beam removal** | Remove to at least 18" below grade | Remove to at least 18" below grade |
| **Gravel layer** | 12" of #4 rock over drain holes and shell bottom | 12" of #4 rock over drain hole and shell bottom |
| **Backfill** | Self-compacting fill sand, clean fill, or per soils report | Same |
| **Utilities** | Typically has electrical sub-panel, gas (heater), water, sewer | May share house circuits; may not have gas heater |

#### STEP 3: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Permit type correct?** | Pool/spa demolition permit; partial demo (shell remains below grade) for landscape use only. If structure will be built over the area, full removal with geotech report is required -- different permit process. | CBC 105.1 | `demolition-structural-cbc.md` |
| 2 | **Site plan complete?** | Property lines with dimensions, all buildings/structures shown, pool/spa location, easements/setbacks, driveways, streets, north arrow, fence locations with heights, electrical panel and gas meter locations, proposed fill material specified, debris/backfill storage location, erosion control measures. | CBC 107.2.6 | `demolition-structural-cbc.md` |
| 3 | **Scope of work defined?** | Permit is for demolition of existing pool/spa including capping of associated plumbing and electrical. No other improvements allowed under this permit. | CBC 3303.1 | `demolition-structural-cbc.md` |
| 4 | **Pool dimensions provided?** | Length, width, deepest depth, shallowest depth, estimated volume in gallons. These determine backfill quantity and inspection scope. | -- | -- |
| 5 | **Drainage holes adequate?** | Pool: 2 holes at 36" dia, one at lowest point. Spa: 1 hole at 36" dia at lowest point. Holes equally spaced across deep end and levels. | CBC 3303.5 | `drainage-grading-erosion.md` |
| 6 | **Gravel layer specified?** | 12-inch layer of #4 rock (1" to 2.5" Class II permeable free-draining rock) over drain holes and pool shell bottom. | CBC 3303.5 | `drainage-grading-erosion.md` |
| 7 | **Coping/bond beam removal adequate?** | Remove pool coping, bond beam, and steel rebar around entire perimeter to at least 18 inches below finished grade. | CBC 3303.4 | `demolition-structural-cbc.md` |
| 8 | **Backfill material specified?** | Self-compacting fill sand (SE25 type), clean fill dirt, or as specified in soils report. No organic material, construction debris, cobbles, or boulders. Fill to within 30 inches of final surface, then planting medium for upper 18 inches. | CBC 1804.3, J107.4 | `demolition-structural-cbc.md` |
| 9 | **Compaction method specified?** | Hand compaction equipment, 6-inch lifts, prudent use of water. 90% minimum (90-95% typical) per ASTM D1557 Modified Proctor. Soil compaction report required at final inspection. | CBC 1804.6, 1705.6, J107.5 | `demolition-structural-cbc.md` |
| 10 | **Geotechnical filter fabric?** | Filter fabric applied after backfilling, before planting medium layer. Separates structural backfill from planting medium. | -- | `demolition-structural-cbc.md` |
| 11 | **Electrical properly decommissioned?** | Sub-panel and all related conductors removed back to service supply connection. Pool bonding system disconnected. Separate permit required if converting electrical for other uses. | CEC 680.13, CBC 3303.6 | `electrical-disconnect-cec.md` |
| 12 | **Gas line capped at both ends?** | Gas line disconnected and capped gastight at BOTH the meter AND the equipment location. Must use screw joint fitting. | CPC 1206.3, 1210.8.1 | `plumbing-gas-capping-cpc.md` |
| 13 | **Water supply capped?** | Water supply line to pool fill/autofill disconnected and capped at nearest active branch. | CPC 601.1, 309.6 | `plumbing-gas-capping-cpc.md` |
| 14 | **Sewer/drain capped?** | Pool drain connection to sanitary sewer properly capped to prevent sewer gas and debris entry. | CPC 305.1, 701.1 | `plumbing-gas-capping-cpc.md` |
| 15 | **Above-ground equipment removed?** | All above-ground pool equipment (pump, filter, heater, chlorinator, etc.) and associated plumbing removed. | CBC 3303.6 | `plumbing-gas-capping-cpc.md` |
| 16 | **Pool water discharge plan?** | Water must be de-chlorinated before discharge to storm drain. Chlorinated/contaminated water must go off-site. No filter backwash or cleaning wastewater to storm drain. | NPDES/BMP | `plumbing-gas-capping-cpc.md` |
| 17 | **Drainage/grading adequate?** | Finished grade slopes minimum 2% away from all existing structures. Drainage pattern does not increase runoff to neighboring properties. | CBC 1804.4 | `drainage-grading-erosion.md` |
| 18 | **Erosion control measures?** | BMP measures during construction: silt fencing, gravel bags at storm drains, covered stockpiles. Erosion control on finished slopes before final inspection. | CBC 3304.1.5, J110.1 | `drainage-grading-erosion.md` |
| 19 | **Owner disclosure signed?** | Owner acknowledges: area for landscape only, no structures; differential settlement risk; disclosure upon sale required (size, location, partial demolition method, backfilled). | -- | -- |

#### STEP 4: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what is wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation (e.g., gas line capping when pool has no gas heater)

---

### Quick-Reference Tables

#### Inspection Sequence (Typical)

| # | Inspection | What Is Verified | When |
|---|-----------|-----------------|------|
| 1 | **Pre-construction / Public Works** | Site access, BMP/erosion control in place, NPDES compliance | Before any work begins |
| 2 | **NPDES / BMP** | Erosion control measures, proper water discharge | During construction |
| 3 | **Sewer Cap** | Sewer/drain line properly capped, gas line capped, water line capped | After utility disconnect, before backfill |
| 4 | **Final Demolition** | Drainage holes, gravel layer, coping/bond beam removal depth, backfill material and compaction, grading, soil compaction report, equipment removal, electrical removal | After backfill complete |

#### Backfill Layer Summary (Bottom to Top)

| Layer | Material | Depth/Thickness |
|-------|----------|----------------|
| **Pool shell bottom** | Remaining shell with drainage holes | Existing |
| **Gravel drainage** | #4 rock (1"-2.5" Class II permeable) | 12 inches |
| **Debris layer** (optional) | Coping/bond beam fragments, max 3" pieces | Variable |
| **Structural backfill** | Self-compacting fill sand (SE25), clean fill, or per soils report | To within 30" of final surface |
| **Filter fabric** | Geotechnical filter fabric | Membrane |
| **Planting medium** | Suitable planting soil | Upper 18 inches |
| **Finished grade** | Landscaping, minimum 2% slope from structures | Surface |

#### Utility Disconnection Summary

| Utility | Action | Cap Method | Cap Location | Code |
|---------|--------|-----------|-------------|------|
| **Electrical** | Remove sub-panel + conductors back to service | N/A (removal) | At main panel | CEC 680.13 |
| **Gas** | Disconnect and cap | Screw joint fitting, gastight | Both meter AND equipment | CPC 1206.3 |
| **Water** | Disconnect and cap | Cap fitting | Nearest active branch | CPC 601.1 |
| **Sewer/drain** | Disconnect and cap | Mechanical plug or cap | Building sewer connection | CPC 305.1 |

#### Pool Shell Modification Summary

| Feature | Pool | Spa |
|---------|------|-----|
| **Drainage holes** | 2 holes, 36" diameter | 1 hole, 36" diameter |
| **Hole placement** | One at lowest point; equally spaced across deep end | At lowest point |
| **Bond beam removal** | 18" minimum below finished grade | 18" minimum below finished grade |
| **Rebar removal** | Remove with bond beam around perimeter | Remove with bond beam around perimeter |

---

### Key Principles

1. **Partial demolition only**: This skill covers partial pool demolition where the shell remains below grade. The area is restricted to landscape/garden use only. No structures, driveways, decks, patios, or similar elements can be placed over the backfilled area under this permit type.

2. **Full removal is a different permit**: If the area will support a structure (addition, patio, deck, driveway), the entire pool shell must be removed, the excavation backfilled with engineered and compacted fill, and a geotechnical report by a licensed engineer is required. This is a significantly more complex and expensive process.

3. **Four utility systems**: Every pool demolition involves decommissioning up to four utility systems -- electrical, gas, water, and sewer. Each has distinct code requirements. The electrical system is removed (not just capped); gas, water, and sewer are capped.

4. **Compaction is critical**: Backfill compaction (90-95% per ASTM D1557) is the single most important structural requirement. A soil compaction report from a licensed geotechnical professional is required at final inspection. Inadequate compaction leads to differential settlement.

5. **Drainage prevents failure**: The drainage holes + gravel layer system is what prevents hydrostatic pressure buildup inside the remaining shell. Without proper drainage, the shell can "float" or the backfill can become saturated and fail.

6. **Disclosure is permanent**: The owner must disclose the demolished pool upon sale of the property. The disclosure must include size, location, that it was partial demolition (shell remains), and that it was backfilled. This is a real estate disclosure requirement, not a code requirement, but it is part of the permit process.

7. **Electrical conversion requires separate permit**: If any part of the pool electrical system will be reused for other purposes (landscape lighting, outdoor kitchen circuit, etc.), a separate electrical permit is required. The pool demolition permit does not authorize electrical conversion work.
