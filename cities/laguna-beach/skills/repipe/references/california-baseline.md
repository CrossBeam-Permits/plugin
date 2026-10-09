# California Baseline — Repipe

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Repipe — State Regulatory Decision Engine

This skill contains California state-level whole-house repipe rules extracted from the 2025 California Plumbing Code (CPC), Title 24 Part 5. It covers residential water supply repiping — replacing existing supply piping with new approved materials.

**What this covers**: State plumbing code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local fee schedules, or project-specific engineering. Use the city-level repipe skill (e.g., `costa-mesa-repipe`) for those.

### How to Use This Skill

When reviewing a repipe permit or answering a repipe code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 3-4 reference files.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every repipe review.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in -> pass/fail out) | `pipe-materials.md`, `pipe-sizing.md`, `valves.md`, `joints-connections.md` |
| **Pipe material question only** | `pipe-materials.md` |
| **Pipe sizing / fixture count question** | `pipe-sizing.md` |
| **Water pressure question** | `water-pressure.md` |
| **Joint or fitting question** | `joints-connections.md` |
| **Valve question** | `valves.md` |
| **Underground / slab piping question** | `pipe-protection-underground.md` |
| **Hot water / insulation question** | `hot-water-piping.md` |
| **Backflow / hose bibb question** | `backflow-prevention.md` |
| **General repipe code question** | `pipe-materials.md`, `pipe-sizing.md`, `valves.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Pipe material approved?** | Material is on CPC Table 604.1 approved list; polybutylene (PB) is NOT approved for new; PEX-AL-PEX not adopted for HCD 1 & 2 potable water | CPC 604.1, Table 604.1 | `pipe-materials.md` |
| 2 | **NSF 61 & lead content?** | All materials comply with NSF 61; max 0.25% weighted avg lead (drinking water); max 0.2% lead in solder/flux | CPC 604.1, 604.2, 604.2.1 | `pipe-materials.md` |
| 3 | **Copper type adequate?** | If copper: Type L minimum; Type M only aboveground; markings: K=green, L=blue, M=red | CPC 604.3, 604.4 | `pipe-materials.md` |
| 4 | **Pipe sizing adequate?** | Based on fixture count -> WSFU -> pipe size per pressure range and developed length | CPC 610.3, Table 610.3, Table 610.4 | `pipe-sizing.md` |
| 5 | **Building supply minimum?** | Minimum 3/4" water service; 1/2" branch minimum; water heater manifold one size larger if fed from end | CPC 610.8, CRC P2903.7 | `pipe-sizing.md` |
| 6 | **Water pressure?** | Min 15 psi at fixtures; PRV required if >80 psi; pipe sizing at 80% of regulated pressure | CPC 608.1, 608.2 | `water-pressure.md` |
| 7 | **Expansion tank?** | Required downstream of PRV; also required where check valve or backflow preventer creates a closed system | CPC 608.2, 608.3 | `water-pressure.md` |
| 8 | **Valves correct?** | Main fullway valve per building after meter (606.3); water heater fullway valve on cold supply; control valve at each fixture/appliance; all accessible. Multi-unit buildings: individual shutoff valves for each dwelling unit (CPC 606.3). | CPC 606.2, 606.3, 606.5, 606.6 | `valves.md` |
| 9 | **Unions near equipment?** | Within 12 in. of water heater, softeners, filters, regulators, similar equipment | CPC 609.5 | `valves.md` |
| 10 | **Joint method correct?** | Solder per ASTM B828 (max 0.2% lead); CPVC one-step cements yellow or red (605.2.2); female threaded CPVC fittings with male plastic only (605.2.3); PVC threaded fittings minimum Schedule 80 (605.12.3); press-connect per mfr; push-fit per ASSE 1061; plastic-to-other-piping adapter fittings per 605.16.2 | CPC 605.1.4, 605.2.2, 605.2.3, 605.1.3.2, 605.9.3, 605.12.3, 605.16.2 | `joints-connections.md` |
| 11 | **Dissimilar metals?** | Dielectric unions/fittings at copper-to-galvanized connections; dissimilar metal connections at accessible locations only | CPC 605.15, 605.16.1, 310.6 | `joints-connections.md` |
| 12 | **Pipe protection?** | Steel nail plates (min 18 ga.) where pipes are within 1-1/4 in. of framing face; plates extend 1-1/2 in. beyond pipe OD; 2 in. above/below sole and top plates | CPC 312.9 | `pipe-protection-underground.md` |
| 13 | **Underground installation?** | Min 12 in. below grade; min 6 in. below frost line (CPC 609.1); tracer wire on plastic (#14 blue, CPC 604.10.1); common trench separation from sewer (12 in. above, 12 in. horizontal, CPC 609.2); no pipes within 45 deg. of footings (CPC 314.1). Backfill: smooth continuous bearing support; no rocks in first 12 in.; thin layers max 6 in. tamped; no heavy equipment until 12 in. of tamped earth over pipe (CPC 314.4, 314.4.1). Piping not directly embedded in concrete/masonry (CPC 312.2); protective sheath min 8 mil plastic for corrosive soil (CPC 312.3). Bored/drilled openings: sleeve not required but annular spaces sealed (CPC 312.10.2). | CPC 312.2, 312.3, 314.1, 314.4, 314.4.1, 604.10.1, 609.1, 609.2 | `pipe-protection-underground.md` |
| 14 | **Under-slab piping?** | Galvanized prohibited; copper joints brazed (not soldered) with wrought-copper fittings; Type L minimum; pressure tested before pouring | CPC 609.3, 604.3, 609.4 | `pipe-protection-underground.md` |
| 15 | **Hot water insulation?** | All hot water piping insulated; thickness >= pipe diameter (up to 2 in.), 2 in. for larger pipe | CPC 609.12.1, 609.12.2 | `hot-water-piping.md` |
| 16 | **Water hammer arrestors?** | Mechanical ASSE 1010 devices (not air chambers) near quick-close valves (dishwasher, clothes washer) | CPC 609.11 | `hot-water-piping.md` |
| 17 | **Backflow prevention?** | Hose bibbs need vacuum breaker; irrigation systems need AVB/PVB/SVB/RP; pool/spa makeup needs air gap or RP | CPC 603.5.7, 603.5.6, 603.5.21 | `backflow-prevention.md` |
| 18 | **Pressure test?** | Test at working pressure or min 50 psi (air); hold 15 min with no leakage | CPC 609.4 | `pipe-protection-underground.md` |
| 19 | **PVC/PEX UV protection?** | PVC: no direct sunlight (exception: max 24 in. with 0.04 in. UV tape); PEX: min 30-day UV protection per CPC | CPC 605.12, 605.9 | `pipe-materials.md` |
| 20 | **General installation?** | Burred ends reamed; dead legs have flushing method; flex connectors accessible; no reuse of non-potable pipe; slip joints on exposed fixture supply only | CPC 609.1, 309.6, 604.5, 604.8, 605.14 | `hot-water-piping.md` |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this installation

---

### Quick-Reference Tables

#### Approved Pipe Materials for Water Supply (CPC Table 604.1)

| Material | Approved? | Common Standards | Notes |
|----------|-----------|-----------------|-------|
| **Copper** | Yes | ASTM B88 (Type K, L, M) | Type L min; Type M aboveground only; K=green, L=blue, M=red |
| **CPVC** | Yes | ASTM D2846, F441/F442 | Schedule 40/80; primer orange; not permitted for OSHPD potable water |
| **PEX** | Yes | ASTM F876 | UV-sensitive; min 30-day UV protection; brass fittings meet NSF 14 |
| **PEX-AL-PEX** | Limited | ASTM F1281 | NOT adopted for HCD 1 & HCD 2 potable water (BSC, DSA-SS) |
| **Galvanized Steel** | Yes | ASTM A53 | Approved but rarely used for new repipe; NOT permitted under slab |
| **PVC** | Supply only | ASTM D1785, D2241 | Cold water building supply only, not distribution; no direct sunlight |
| **Polybutylene (PB)** | **NO** | -- | NOT approved for new installation |

#### Fixture Unit Quick Reference (CPC Table 610.3)

| Fixture (Private Use) | Cold WSFU | Hot WSFU | Total WSFU |
|-----------------------|-----------|----------|------------|
| Water Closet (1.6 GPF) | 2.5 | -- | 2.5 |
| Bathtub/Shower | 1.0 | 1.0 | 1.4 |
| Kitchen Sink | 1.0 | 1.0 | 1.4 |
| Lavatory | 0.5 | 0.5 | 0.7 |
| Clothes Washer | 1.0 | 1.0 | 1.4 |
| Dishwasher | -- | 1.4 | 1.4 |
| Hose Bibb | 2.5 | -- | 2.5 |
| Laundry Tray | 1.0 | 1.0 | 1.4 |

#### Minimum Pipe Size by Fixture Units (Simplified)

| Total WSFU | Min. Pipe Size (30-45 psi) | Min. Pipe Size (46-60 psi) |
|-----------|---------------------------|---------------------------|
| 1-4 | 3/4" | 1/2" |
| 5-15 | 3/4" | 3/4" |
| 16-25 | 1" | 3/4" |
| 26-40 | 1" | 1" |
| 41+ | 1-1/4" | 1" |

*Actual sizing depends on developed length and elevation -- see `pipe-sizing.md` for full Table 610.4.*

#### Required Valves Quick Reference

| Valve Location | Type | Code Section |
|----------------|------|-------------|
| Main supply (after meter) | Fullway, accessible, with bleed | CPC 606.2 |
| Water heater (cold supply) | Fullway, not throttled | CPC 606.2 |
| Each fixture/appliance | Control valve | CPC 606.5 |
| All required shutoffs | Accessible | CPC 606.6 |

#### Pipe Protection Quick Reference

| Protection | When Required | Code Section |
|-----------|--------------|-------------|
| Steel nail plate (18 ga. / 0.0478 in. min) | Plastic or copper pipe within 1 in. of exposed framing face | CPC 312.9 |
| Plate extends 1-1/2 in. beyond pipe OD | All nail plate installations | CPC 312.9 |
| Plate extends 2 in. above/below sole & top plates | All nail plate installations | CPC 312.9 |
| Sleeve (2 sizes larger) through foundation | All pipe penetrations through foundation/footings | CPC 312.10.1 |
| #14 blue tracer wire | Plastic pipe underground | CPC 604.10.1 |

#### Underground Installation Quick Reference

| Requirement | Detail | Code Section |
|-------------|--------|-------------|
| Smooth continuous bearing support | Pipes in trench on firm bed | CPC 314.1 |
| No rocks in first 12 in. of backfill | Over pipe crown | CPC 314.4 |
| Backfill in thin layers | Max 6 in., tamped | CPC 314.4 |
| No heavy equipment | Until 12 in. tamped earth over pipe | CPC 314.4.1 |
| Min burial depth | 12 in. below finished grade; 6 in. below frost line | CPC 609.1 |
| No direct embedding in concrete | Use sleeves or protective sheath | CPC 312.2 |
| Corrosive soil protection | Min 8 mil plastic sheath | CPC 312.3 |
| Not within 45 deg. of footings | Prevents structural load on pipe | CPC 314.1 |

#### Water Pressure Quick Reference

| Parameter | Value | Code Section |
|-----------|-------|-------------|
| Minimum residual at fixtures | 15 psi | CPC 608.1 |
| Maximum static pressure | 80 psi | CPC 608.2 |
| PRV standard | ASSE 1003 / AWWA C530 | CPC 608.2 |
| Pipe sizing with PRV | 80% of regulated pressure | CPC 608.2 |
| Expansion tank standard | ASSE 1024 / IAPMO Z1088 | CPC 608.3 |
| Test pressure (air) | Min 50 psi, 15 min | CPC 609.4 |

#### Hot Water Insulation Quick Reference

| Pipe Diameter | Min. Insulation Thickness | Code Section |
|--------------|--------------------------|-------------|
| Up to 2 in. | Equal to or greater than pipe diameter | CPC 609.12.2 |
| 2 in. or more | 2 in. | CPC 609.12.2 |

---

### Key Principles

1. **Material must be listed**: All pipe materials must conform to standards in CPC Table 604.1, comply with NSF 61, and meet lead content limits. Unlisted or unapproved materials (like polybutylene) cannot be used for new installation.

2. **Fixture unit method for sizing**: Pipe sizing is based on the number and type of fixtures served, converted to Water Supply Fixture Units (WSFU), then sized using Table 610.4 based on available pressure and developed pipe length.

3. **Dissimilar metals**: Where different metals connect (e.g., copper to galvanized), dielectric unions or approved transition fittings are required. For HCD residential: dielectric unions at ALL dissimilar metal connections. Connections must be at accessible locations (CPC 310.6).

4. **Pressure regulation**: If supply pressure exceeds 80 psi, a PRV (ASSE 1003) is required, preceded by a strainer, with an expansion tank downstream. Pipe sizing uses 80% of regulated pressure (CPC 608.2).

5. **Hot water insulation**: ALL hot water piping must be insulated. Thickness must be at least equal to the pipe diameter for pipes up to 2 in. (CPC 609.12).

6. **Valve requirements**: Main fullway valve after meter, fullway valve on water heater cold supply (not throttled), control valve at each fixture/appliance. All required valves must be accessible.

7. **Pipe protection**: Steel nail plates required where pipes penetrate framing within 1-1/4 in. of face. Underground service min 12 in. deep. Galvanized prohibited under slab. Copper under slab must be brazed (not soldered).

8. **Backflow prevention**: Hose bibbs require vacuum breakers. Irrigation systems need appropriate backflow devices based on hazard level.

9. **Pressure testing**: All completed systems must pass a pressure test -- min working pressure or 50 psi air, held 15 minutes with no leakage.

10. **Water hammer**: ASSE 1010 mechanical water hammer arrestors (not air chambers) required near quick-acting valves.

---

### Additional Guidance

#### Partial vs. Full Repipe Scoping

A repipe permit may cover a full whole-house repipe or a partial scope (e.g., hot water lines only, or replacing only galvanized sections). Key considerations:

- **Full repipe** replaces all water supply piping from the meter/main to every fixture. Straightforward — all checklist items apply.
- **Partial repipe** replaces only a subset of piping (e.g., hot water only, or galvanized-to-copper in specific areas). Additional considerations:
  - **Transition connections**: Where new pipe connects to existing pipe, verify proper transition fittings (CPC 605.16). Dissimilar metal connections require dielectric unions or approved adapters at accessible locations (CPC 310.6, 605.15).
  - **Scope boundaries**: Clearly define on plans which piping is being replaced and which is remaining. The permit scope should not leave ambiguity about what the contractor is responsible for.
  - **Pre-existing deficiencies**: If existing piping that is NOT in scope has visible code violations (missing shutoffs, undersized pipe, galvanized under slab), note them but do not fail the permit for them — they pre-date this scope. Flag for the record.
  - **Insta-Permit eligibility**: Some cities' standard plan forms (e.g., CBRP) may not explicitly address partial repipe scope. If the form language is ambiguous, flag for AHJ interpretation. The form typically says "replacement of water piping serving existing plumbing fixtures" — a partial repipe arguably qualifies if it serves existing fixtures, but a strict reading could require whole-house scope.

#### CPVC Temperature Limitations in Unconditioned Spaces

CPVC (ASTM D2846) is approved for hot and cold water distribution per CPC Table 604.1, but it has temperature-dependent pressure derating:

- **Rated max operating temperature**: 180°F (most manufacturers) at rated pressure
- **Ambient temperature concern**: In unconditioned attic spaces, summer ambient temperatures in Southern California can reach 140-160°F. When CPVC carries hot water (typically 120-140°F) through a 150°F+ attic, the effective pressure rating drops significantly.
- **Code position**: CPC does not explicitly prohibit CPVC in attics. The material is technically within its rated temperature range.
- **Manufacturer position**: Most CPVC manufacturers recommend against installation in attic spaces where ambient temperatures may exceed 120°F, or require pressure derating. Violating manufacturer installation guidelines may void warranty.
- **Practical recommendation**: When CPVC is routed through unconditioned attic space, **flag this for the reviewer** with a note: "CPVC in unconditioned attic — verify manufacturer ambient temperature guidelines. Consider PEX (rated to 200°F) as an alternative for the attic trunk run." Insulating CPVC in the attic helps with both energy code compliance and thermal protection.
- This is not a hard FAIL — it's a FLAG for practical awareness and inspector judgment.

#### Water Pressure — The 80 psi Boundary Value

CPC 608.2 states maximum building water pressure "shall not exceed 80 psi." A pressure reading of exactly 80 psi raises a boundary-value question:

- **Literal reading**: 80 psi does NOT "exceed" 80 psi. The code says "shall not exceed 80 psi" — at exactly 80 psi, the requirement is met. No PRV is legally required.
- **Practical reality**: Static pressure fluctuates throughout the day (lower during peak demand, higher during low-demand hours like 2 AM). A reading of 80 psi during a daytime test could easily be 85+ psi at night.
- **Recommended approach**: PASS the pressure check (the literal reading is compliant), but add a FLAG note: "Static pressure at 80 psi — technically compliant but at the code maximum. Recommend PRV installation as a practical measure. If PRV is installed, expansion tank also becomes required per CPC 608.3." This gives the applicant and inspector the full picture without incorrectly failing a compliant submission.
- **Cascading requirement**: If the AHJ determines a PRV is needed, then an expansion tank is also required downstream per CPC 608.3 (closed-system thermal expansion protection). These two requirements are linked — flag both together.
