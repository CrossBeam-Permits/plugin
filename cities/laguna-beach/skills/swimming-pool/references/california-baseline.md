# California Baseline — Swimming Pool/Spa

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Swimming Pool/Spa Construction — State Regulatory Decision Engine

This skill contains California state-level swimming pool and spa construction rules extracted from the 2025 California Building Code (CBC), California Residential Code (CRC), California Electrical Code (CEC), California Plumbing Code (CPC), and California Health & Safety Code. It covers new residential pool/spa construction -- the most common pool permit type.

**What this covers**: State building, electrical, plumbing, and safety code requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local standard plan forms, planning/zoning setback overrides, fee schedules, public/commercial pool health department requirements, or project-specific engineering. Use the city-level swimming-pool skill (e.g., `orange-county-swimming-pool`) for city-specific overlays.

### How to Use This Skill

When reviewing a swimming pool/spa construction permit or answering a pool code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 2-3 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every pool review.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (plans/form data in, pass/fail out) | `barriers-enclosures.md`, `electrical-bonding-680.md`, `structural-drainage.md`, `plumbing-filtration.md` |
| **Barrier/fencing question only** | `barriers-enclosures.md` |
| **Drowning prevention feature question** | `barriers-enclosures.md` |
| **Electrical bonding or GFCI question** | `electrical-bonding-680.md` |
| **Underwater lighting question** | `electrical-bonding-680.md` |
| **Pool motor/pump wiring question** | `electrical-bonding-680.md` |
| **Structural design or slope setback question** | `structural-drainage.md` |
| **Drainage, grading, or deck question** | `structural-drainage.md` |
| **Plumbing, filtration, or suction outlet question** | `plumbing-filtration.md` |
| **Anti-entrapment / VGBA question** | `plumbing-filtration.md` |
| **Pool heater installation question** | `plumbing-filtration.md`, `electrical-bonding-680.md` |
| **General pool code question** | `structural-drainage.md` |

#### STEP 2: Determine Pool vs. Spa

The requirements are largely the same but differ in a few areas:

| Feature | Pool | Spa / Hot Tub |
|---------|------|---------------|
| **Barrier required?** | Yes -- 60" min enclosure (HS Code 115923) | Exempt if equipped with locking safety cover meeting ASTM F1346 (HS Code 115925) |
| **Drowning prevention (2-of-7)?** | Required for new construction or remodel | Required unless exempted by safety cover |
| **Suction outlets** | Min 2 per pump, 3 ft apart (HS Code 115928) | Min 2 per pump, 3 ft apart |
| **Equipotential bonding** | Full bonding grid required (CEC 680.26) | Required per CEC 680.26 |
| **Water heater** | Common -- gas or heat pump | Common -- gas or electric |
| **Structural design** | Custom engineering typical | May use standard plans |

#### STEP 3: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Site plan complete?** | Property lines, all structures with dimensions and setbacks, proposed pool location, easements, driveways, fencing locations with heights, utility locations, north arrow, scale | CBC 107.2 | `structural-drainage.md` |
| 2 | **Pool/spa plan details?** | Structural details, dimensions, material specifications, cross-sections showing existing slopes and retaining walls to 5 ft beyond property lines | CBC 3109, 107.2 | `structural-drainage.md` |
| 3 | **Structural calculations?** | Required if non-standard plan. Standard plans (where approved by jurisdiction) may be exempt. | CBC 1901, 3109 | `structural-drainage.md` |
| 4 | **Slope setback adequate?** | Pool-to-slope setback = half the building footing setback distance. Pool wall within 7 ft horizontal of slope top must support water without soil support. Soil report required if pool is within 15 ft of slope top or 8 ft of slope toe (slope steeper than 1:3). | CBC 1808.7.3 | `structural-drainage.md` |
| 5 | **Concrete/shotcrete specs?** | Min f'c = 4,500 psi 28-day, Type V cement (sulfate-resistant), max w/c ratio = 0.45 per ACI 318. Special inspection required for gunite/shotcrete per CBC 1705.3, 1908. | CBC Ch. 19, ACI 318 | `structural-drainage.md` |
| 6 | **Soil report provided (if required)?** | Required when pool is near slopes (see item 4). Geotechnical memo confirming excavation suitability required before steel inspection. | CBC 1803.2 | `structural-drainage.md` |
| 7 | **Barrier/enclosure compliant?** | Min 60" high, max 2" ground clearance, no 4" sphere passage, no climbable features, gates self-closing/self-latching with latch at min 60" above ground, gates swing away from pool | HS Code 115923, CRC App. CI | `barriers-enclosures.md` |
| 8 | **Drowning prevention features (2-of-7)?** | Two different qualifying features from seven options. Certain combinations prohibited (e.g., exit alarm + door latch on same door, pool cover + pool alarm). | HS Code 115922 | `barriers-enclosures.md` |
| 9 | **Safety glazing near pool?** | Required for glazing within 60" above standing surface and within 60" horizontal of water's edge | CRC R324.4.5 | `barriers-enclosures.md` |
| 10 | **Equipotential bonding grid?** | Pool shell rebar bonded, perimeter surfaces bonded within 3 ft of pool edge, all metallic components bonded. Bonding to perimeter at min 4 points uniformly spaced. Conductor: min #8 AWG solid copper. | CEC 680.26 | `electrical-bonding-680.md` |
| 11 | **GFCI protection adequate?** | All 125V receptacles within 20 ft of pool edge GFCI-protected. Receptacle required 6-20 ft from pool edge. No receptacles within 6 ft. | CEC 680.22 | `electrical-bonding-680.md` |
| 12 | **Underwater lighting compliant?** | Wet-niche fixtures: GFCI-protected, max 150V, forming shell grounded to equipment grounding conductor. Low-voltage (15V or less) listed LED fixtures permitted. | CEC 680.23 | `electrical-bonding-680.md` |
| 13 | **Pool pump/motor wiring?** | Disconnect within sight and min 5 ft from pool edge. Motors GFCI-protected per 680.21(C). Wiring methods suitable for corrosive environments. No aluminum conduit. | CEC 680.21, 680.13, 680.14 | `electrical-bonding-680.md` |
| 14 | **Pool heater compliant?** | Gas: fuel piping under the applicable CPC route; venting under the appliance listing/manufacturer instructions and applicable CMC Chapter 8 route; Energy Code 110.4 certification. Electric: proper circuit sizing and disconnect. Cover required if an outdoor heat pump or gas heater triggers Energy Code 110.4. | CPC Ch. 12; CMC Ch. 8; CEC 680.9 | `plumbing-filtration.md` |
| 15 | **Suction outlets anti-entrapment?** | Min 2 suction outlets per pump, hydraulically balanced, min 3 ft apart. Anti-entrapment grates per ANSI/APSP-16, removable only with tools. | HS Code 115928 | `plumbing-filtration.md` |
| 16 | **Drain system adequate?** | Two return drains required -- one at bottom, one at side 2" within bottom, min 4 ft apart, with anti-vortex covers. | HS Code 115928, CPC | `plumbing-filtration.md` |
| 17 | **Plumbing/filtration per code?** | Water supply with backflow prevention, filtration system, water heater piping per CPC. All drains/grates/skimmer covers approved before installation. | CPC Ch. 7, 12 | `plumbing-filtration.md` |
| 18 | **Drainage/grading adequate?** | Deck and surrounding grade slope minimum 2% away from structures. Pool drainage does not increase runoff to neighboring properties. | CBC 1804.4 | `structural-drainage.md` |
| 19 | **Erosion/sediment control?** | Erosion and sediment control plan required. BMP measures during construction. NPDES compliance for dewatering. | CBC 3304.1.5 | `structural-drainage.md` |
| 20 | **Equipment listing?** | All pool equipment (pump, filter, heater, lighting, GFCI devices) listed and installed per manufacturer instructions. | CEC 110.3(B), CBC 3109 | `electrical-bonding-680.md` |

#### STEP 4: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what is wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation (e.g., slope setback when lot is flat)

---

### Quick-Reference Tables

#### Pool Barrier Requirements Summary

| Requirement | Private Pool (HS Code 115923) |
|-------------|-------------------------------|
| Minimum barrier height | 60 inches (5 ft) from outside |
| Maximum ground clearance | 2 inches |
| Maximum opening | No 4-inch sphere passage |
| Gate swing direction | Away from pool |
| Gate closing | Self-closing (gravity or spring) |
| Gate latching | Self-latching, min 60 inches above ground |
| Climbability | No handholds/footholds for children under 5 |
| Spa exemption | Exempt if locking safety cover meets ASTM F1346 |

##### Above-Ground Pools — No Barrier Exemption in California

**California did NOT adopt the model-code exception** (ISPSC/IRC pool appendices) that lets an above-ground pool's own wall serve as the barrier (≥48" non-climbable wall + removable ladder). No such exemption exists anywhere in the Swimming Pool Safety Act: HS Code 115922 contains only subdivisions (a)–(c), and the only statutory exemptions are in HS Code 115925 (public pools; hot tubs/spas with locking ASTM F1346 safety covers; settings other than single-family homes). HS Code 115921's definition of "swimming pool" expressly **includes** above-ground structures.

An above-ground pool at a single-family home therefore still requires at least 2 of the 7 drowning-prevention features of HS Code 115922(a), and an enclosure used as feature #1 must meet the HS Code 115923 characteristics (60-inch minimum height, etc.) — a 48-inch pool wall does not meet that standard. **If a plan relies on "pool wall as barrier," flag it** and cite HS Code 115922(a) + 115923.

#### Drowning Prevention — 2-of-7 Features (HS Code 115922)

| # | Feature | Standard |
|---|---------|----------|
| 1 | Enclosure isolating pool from home | HS Code 115923 |
| 2 | Removable mesh fencing with key-lockable gate | ASTM F2286 |
| 3 | Safety pool cover (manual or power) | ASTM F1346 |
| 4 | Exit alarms on doors/windows to pool | Audible continuous alarm |
| 5 | Self-closing/self-latching device on doors (latch min 54") | -- |
| 6 | Pool alarm detecting unauthorized water entry | ASTM F2208, independently certified |
| 7 | Other approved means of equal protection | Independently verified by approved lab |

**Prohibited combinations**: (1) Exit alarm + self-closing latch on same door; (2) Exit alarm + door latch on separate doors; (3) Safety pool cover + pool alarm.

#### Electrical Clearance Zones (CEC Article 680)

| Zone | Distance from Pool Edge | Restriction |
|------|------------------------|-------------|
| **0-5 ft** | Inside walls to 5 ft | No receptacles, no switches, no disconnect means (except listed pool equipment) |
| **5-10 ft** | 5 ft to 10 ft | Disconnect means permitted (must be within sight of equipment). GFCI-protected receptacles permitted. |
| **6-20 ft** | 6 ft to 20 ft | Min one 125V GFCI-protected receptacle required |
| **>20 ft** | Beyond 20 ft | Standard rules apply |
| **Overhead** | Min 22.5 ft above water (480V), 14.5 ft (insulated <15kV) | No power lines over pool |

#### Slope Setback Requirements (CBC 1808.7.3)

| Condition | Setback Rule |
|-----------|-------------|
| Pool near ascending slope | Setback = half the building footing setback (H/3, max 15 ft from toe) |
| Pool near descending slope | Setback = half the building footing setback (H/3, max 40 ft from top) |
| Pool wall within 7 ft of slope top | Must be capable of supporting water without soil support |
| Soil report trigger | Pool within 15 ft of slope top or 8 ft of slope toe (slope steeper than 1:3) |

#### Concrete and Shotcrete Specifications

| Parameter | Requirement | Source |
|-----------|-------------|--------|
| Minimum compressive strength (f'c) | 4,500 psi at 28 days | CBC Ch. 19, ACI 318 |
| Cement type | Type V (sulfate-resistant) | ACI 318 Table 19.3.1.1 |
| Maximum water/cement ratio | 0.45 | ACI Table 19.3.2.1 |
| Special inspection | Required for gunite/shotcrete | CBC 1705.3, 1908, Table 1705.3 |
| Expansive soils EFP | 100 PCF (level lot), 125 PCF (slopes) | Geotech standard |

#### Suction Outlet / Anti-Entrapment Summary

| Requirement | Specification | Source |
|-------------|---------------|--------|
| Minimum suction outlets per pump | 2 | HS Code 115928 |
| Minimum separation between outlets | 3 ft | HS Code 115928 |
| Hydraulic balance | Required | HS Code 115928 |
| Anti-entrapment grate standard | ANSI/APSP-16 | HS Code 115928 |
| Grate removal | Only with tools | HS Code 115928 |
| Return drains | 2 required: 1 at bottom, 1 at side 2" within bottom, min 4 ft apart | Industry standard |
| Anti-vortex covers | Required on all drains | HS Code 115928 |

---

### Additional Checklist Items

#### Contractor Licensing

CSLB C-53 (Swimming Pool) license required for in-ground pool construction. B (General Building) license alone is NOT sufficient for pool shell construction.

#### Drainage Discharge

Pool drainage (including backwash, draining, and maintenance water) must discharge to the sanitary sewer system, NOT to the storm drain. Verify routing on the plumbing plan. Storm drain discharge is an illicit discharge violation per local MS4 NPDES permit.

---

### Key Principles

1. **Pool/spa definition**: Any structure intended for swimming or recreational bathing containing water over 18 inches deep. Includes in-ground, aboveground, hot tubs, spas, portable spas, and nonportable wading pools (HS Code 115921).

2. **Barrier is mandatory**: Every new private pool must have a 60-inch enclosure meeting HS Code 115923. The only exemption is spas/hot tubs with a locking safety cover meeting ASTM F1346 (HS Code 115925).

3. **Two-of-seven drowning prevention**: New pool/spa construction or remodel at a private single-family home requires at least 2 of 7 qualifying drowning prevention features. The building official must inspect these before final approval (HS Code 115922).

4. **Equipotential bonding is non-negotiable**: CEC 680.26 requires a comprehensive bonding grid connecting pool shell rebar, perimeter surfaces, metallic components, and equipment. This prevents voltage gradients that cause electrocution.

5. **Anti-entrapment is federal + state law**: The Virginia Graeme Baker Pool & Spa Safety Act (federal) and HS Code 115928 (state) both require dual suction outlets, anti-entrapment grates, and SVRS compliance. This is a life-safety requirement.

6. **Special inspection required**: Gunite and shotcrete pool construction requires special inspection per CBC 1705.3 and 1908. The geotechnical engineer must provide a memo confirming excavation suitability before steel inspection.

7. **Slope setbacks are half the building setback**: CBC 1808.7.3 sets pool-to-slope setback at half the building footing setback distance. The pool wall within 7 ft horizontal of the slope top must support water without soil support.

8. **Local government can be stricter**: Per HS Code 115927, the Swimming Pool Safety Act is subject to local government modification. Cities may adopt additional or stricter barrier, gate, or safety requirements.
