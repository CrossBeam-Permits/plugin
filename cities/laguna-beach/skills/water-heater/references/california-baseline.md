# California Baseline — Water Heater

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Water Heater -- State Regulatory Decision Engine

This skill contains California state-level water heater replacement rules extracted from the 2025 California Plumbing Code (CPC), California Mechanical Code (CMC), and California Energy Code (Title 24 Part 6). It covers residential water heater replacements -- the most common plumbing permit type.

**What this covers**: State plumbing, mechanical, and energy code -- the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local fee schedules, form field mappings, or project-specific engineering. Use the city-level water heater skill (e.g., `costa-mesa-water-heater`) for those.

### How to Use This Skill

When reviewing a water heater permit or answering a water heater code question, follow the decision tree below. The first branch point is **gas vs. electric** -- this determines which code sections apply.

Load only the reference files you need. Most reviews require 3-5 reference files, not all of them.

---

### Decision Tree Router

#### STEP 1: Gas or Electric?

| Fuel Type | What Applies | What Doesn't Apply |
|-----------|-------------|-------------------|
| **Gas (natural gas / propane)** | Venting, combustion air, gas line sizing, seismic strapping, T&P relief, piping/joints, valves, clearances, energy | -- |
| **Electric (standard resistance)** | Seismic strapping, T&P relief, piping/joints, valves, clearances, energy, dedicated circuit | Venting, combustion air, gas line sizing |
| **Heat pump (electric)** | Same as electric + condensate drain, may need clearance for air intake | Venting, gas line |
| **Tankless (gas)** | Same as gas, with vent category, material, and termination determined from the appliance listing and manufacturer instructions | Category I vent-sizing tables unless the appliance is listed Category I |
| **Tankless (electric)** | Dedicated circuit (often 2-3 circuits), no tank strapping, piping/joints, valves | Venting, gas line, seismic strapping |

#### STEP 2: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in, pass/fail out) | Load per fuel type from checklist below |
| **Venting or combustion air question** (gas only) | `venting-gas.md` |
| **Seismic strapping question** | `seismic-strapping.md` |
| **T&P relief or drain pan question** | `tp-relief-drain.md` |
| **Clearance or location question** | `clearances-location.md` |
| **Gas line sizing question** | `gas-line-sizing.md` |
| **Energy efficiency or UEF question** | `energy-efficiency.md` |
| **Piping materials or joints question** | `piping-materials-joints.md` |
| **Valves, connections, or insulation question** | `valves-connections.md` |

#### STEP 3: Walk the Review Checklist

For a full permit review, check each item in order. The gas/electric column tells you whether each check applies.

| # | Check | Gas | Elec | What to Verify | Code Section | Reference File |
|---|-------|-----|------|---------------|--------------|----------------|
| 1 | **Venting system** | Yes | No | Select an allowed venting-system path under CPC Table 509.4 and the appliance listing. Size the connector and vent from the appliance outlet/listing and CPC 509/510 or CMC 802/803. Verify the applicable termination, cap, flashing, connector slope, and listed clearances. For CPC installations through insulated assemblies, verify the 26-gauge/2-inch shield in CPC 509.6.1.1; do not impose an unsupported concealed-framing shield-plate recipe. | CPC 509, 510; CMC 802, 803 | `venting-gas.md` |
| 2 | **Combustion air** | Yes | No | Verify an applicable CPC 506 / CMC 701 method. Indoor air may use the standard-volume or known-infiltration method; known infiltration below 0.40 ACH requires the known-rate calculation. For ducts, verify CPC 506.9 / CMC 701.11 construction, unobstructed termination, single-space service, upper/lower separation, attic-screen prohibition, upper-horizontal-duct slope, chimney-annulus prohibition, and the correct 12-inch exterior-intake subitem. Screens are conditional and have a minimum 1/4-inch mesh opening; nonmotorized louvers/grilles are fixed open; manual dampers are prohibited and prior-approved power louvers require interlock. | CPC 506; CMC 701 | `venting-gas.md` |
| 3 | **Seismic strapping** | Yes | Tank | Two straps (upper 1/3, lower 1/3), 24-gauge min plumber's tape or listed kit, attached to wall studs, lower strap min 4 in above controls. Flexible connections at water/gas lines for seismic movement (CPC 507.3). General appliance anchoring per CPC 302.4. | CPC 507.2, 507.3, 302.4; H&S 19211 | `seismic-strapping.md` |
| 4 | **T&P relief valve** | Yes | Yes | Pressure relief device at WH (CPC 504.4); temperature probe in top 6 in (CPC 504.5); opens at 150 PSI or 210 deg F; no shutoff/check valves before or after | CPC 504.4, 504.5, 504.6, 608.3, 608.4 | `tp-relief-drain.md` |
| 5 | **T&P discharge pipe** | Yes | Yes | Min 3/4 in, full size to flood level, gravity flow, terminate 6-24 in above grade pointing down, no threads on end, no traps/uphill runs, not into drain pan, not into crawlspace, each piped independently, readily observable | CPC 608.5 | `tp-relief-drain.md` |
| 6 | **Drain pan** | Yes | Yes | Required where leakage causes damage (attic, floor assembly); min 1.5 in deep, 3/4 in drain to approved location; relief valve discharge into pan prohibited | CPC 507.5 | `tp-relief-drain.md` |
| 7 | **Expansion tank** | Yes | Yes | Required if closed system (backflow preventer, check valve, or PRV present); on cold water supply; properly sized; complies with IAPMO/ANSI Z1088 | CPC 608.2, 608.3 | `tp-relief-drain.md` |
| 8 | **Clearances & combustibles** | Yes | Yes | Apply the code, listing, and manufacturer instructions concurrently. Select single-wall vent clearance from the applicable CPC Table 509.7.3.4(1) or CMC Table 802.7.3.3 row and conditions; Type B clearance follows its listing/manufacturer. | CPC 507.26, Table 509.7.3.4(1); CMC 303.10, Table 802.7.3.3 | `clearances-location.md` |
| 9 | **Location restrictions** | Yes | Yes | Not in bedrooms/baths (unless direct-vent or sealed closet with gasketed self-closing door); not where flammables stored; garage: 18 in elevation (FVIR exempt) + vehicle barrier; ground support: min 3 in concrete pad | CPC 504.1, 507.4, 507.12, 507.13 | `clearances-location.md` |
| 10 | **Access & working space** | Yes | Yes | Min 30 in x 30 in working platform; attic: 22x30 in access opening, 24 in passageway with solid floor (508.4.2), max 20 ft (if <6 ft height), light switch at passageway entrance (508.4.4), working platform 30x30 in at service side (508.4.5); appliance accessible for service/inspection/removal. Clearances to combustibles per manufacturer AND per code (CPC 504.3.1). | CPC 504.3.1, 507.25, 508.4, 508.4.2, 508.4.4, 508.4.5 | `clearances-location.md` |
| 11 | **Water heater connectors** | Yes | Yes | Flex connectors max 24 in (copper/stainless), comply with ASME A112.18.6; PEX/PE-RT not within first 18 in of piping at WH; connectors accessible | CPC 604.5, 604.13 | `piping-materials-joints.md` |
| 12 | **Piping materials** | Yes | Yes | All materials NSF 61 compliant; lead content max 0.25% (pipe/fittings) / 0.2% (solder/flux); no reused piping for potable water | CPC 604.1, 604.2, 604.8 | `piping-materials-joints.md` |
| 13 | **Joints & connections** | Yes | Yes | Solder per ASTM B828/B813; dielectric fittings at copper-to-galvanized; dissimilar metals at accessible locations only; press-connect with O-ring and mfr tool; push-fit per ASSE 1061 | CPC 605.1.4, 605.16, 310.6 | `piping-materials-joints.md` |
| 14 | **Valves** | Yes | Yes | Fullway shutoff on cold supply (accessible); control valve at appliance; unions within 12 in for removal | CPC 606.2, 606.5, 606.6, 609.5 | `valves-connections.md` |
| 15 | **Hot water insulation** | Yes | Yes | All hot water piping insulated; thickness >= pipe diameter (up to 2 in pipes), 2 in for larger; first 5 ft from WH minimum R-4 | CPC 609.12; Part 6 Section 150.0(j) | `valves-connections.md` |
| 16 | **Water pressure** | Yes | Yes | Min 15 PSI residual after losses; expansion tank/device if PRV or backflow preventer prevents pressure dissipation | CPC 608.1, 608.2, 608.3 | `valves-connections.md` |
| 17 | **Water hammer** | Yes | Yes | ASSE 1010 mechanical arrestors (not air chambers) near quick-close valves if applicable | CPC 609.11 | `valves-connections.md` |
| 18 | **Vacuum relief** | Yes | Yes | Required when WH is above fixture outlets (e.g., attic installation) | CPC 608.7 | `valves-connections.md` |
| 19 | **Gas line** | Yes | No | Existing line adequate for BTU rating; approved flex connector (max 6 ft, same room, not concealed); sediment trap/drip leg; shutoff valve within 6 ft, accessible | CPC 1208, 1212, 1215 | `gas-line-sizing.md` |
| 20 | **Hot water max developed length** | Yes | Yes | Maximum 100 ft developed length from hot water source to furthest fixture; exceeding requires recirculation system or point-of-use heater | CPC 609.11 | `valves-connections.md` |
| 21 | **Manifold sizing** | Yes | Yes | Cold water manifold fed from end shall be one size larger than water heater supply connection; ensures adequate flow distribution | CPC 610.8 | `valves-connections.md` |
| 22 | **Listing and labeling** | Yes | Yes | Installation/maintenance instructions must remain affixed to unit (CPC 507.24); WH used for space heating must be labeled for both purposes (CPC 501.1) | CPC 501.1, 507.24 | `clearances-location.md` |
| 23 | **Energy compliance** | Yes | Yes | Meets federal/state minimum UEF per draw pattern; nameplate verification; replacement triggers pipe insulation requirement; recirculation must be demand-controlled if present | Part 6 Section 110.3, Section 150.2 | `energy-efficiency.md` |

---

### Additional Guidance

#### Like-for-Like Replacement Scope

When reviewing a like-for-like replacement (same fuel type, same capacity, same location), the following checks should be scored as **N/A** because nothing in that domain changed:

| Check | N/A Condition |
|-------|---------------|
| #16 Water pressure | Same location, no piping changes, existing PRV/expansion tank unchanged |
| #17 Water hammer | No new quick-acting valves added in this scope |
| #20 Hot water max developed length | Same location, no piping layout changes |
| #21 Manifold sizing | No new manifold installed |

These items become active checks when the replacement involves a location change, fuel type change, technology change (tank to tankless), or any piping modifications.

#### Tankless-Specific Decision Rules

When reviewing a tankless (instantaneous) water heater, apply these rules:

| Item | Rule | Code Basis |
|------|------|------------|
| **T&P relief valve** | N/A — tankless with internal passages <=3" diameter are exempt | CPC 608.3 Exception |
| **T&P discharge pipe** | N/A — follows from T&P exemption | CPC 608.5 |
| **Seismic strapping** | Bracket-to-stud mounting satisfies seismic anchoring. Two-strap method does NOT apply to tankless units (no tank). | CPC 507.2, H&S 19211 |
| **Expansion tank** | **PASS** per CPC 608.3 Exception — instantaneous non-storage heaters are exempt from thermal expansion provisions regardless of whether a PRV creates a closed system. Negligible stored water volume. Do NOT flag for AHJ interpretation — the code exception is explicit. | CPC 608.3 Exception |
| **Drain pan** | Apply same rules as tank. Required where leakage causes structural damage. | CPC 507.5 |
| **Gas line sizing** | **Critical check.** Tankless BTU input (150k-199k) is 3-4x higher than tank (30k-50k). Must verify TOTAL connected load from gas meter, not just the branch to the tankless. Use longest-length method per CPC Table 1215.2(1). If total load exceeds pipe capacity at the run length from meter, this is a **FAIL** (code violation), not a FLAG — the pipe is physically undersized. | CPC 1208, 1215, Table 1215.2(1) |
| **Venting** | Determine category and vent material from the appliance listing and manufacturer instructions. Direct-vent appliances follow CPC 509.2.6; through-wall terminations also follow Table 509.8.1. Above 150,000 Btu/h, use manufacturer instructions and no less than the table's non-direct-vent row-B clearance. | CPC 509, 510 |
| **Water hammer** | N/A unless the tankless installation adds quick-acting valves (e.g., new solenoid-driven fixtures). Tankless electronic flow sensors are not "quick-acting valves" per CPC 609.11. | CPC 609.11 |
| **Water pressure** | N/A for same-location replacement with no supply piping changes. Active check if location changes or supply piping is modified. Note: tankless activation requires minimum flow rate — this is a manufacturer spec, not a CPC plan-check item. | CPC 608.1 |
| **Developed length** | N/A for same-location replacement with no piping changes. If piping is modified, check max 100 ft. Note: tankless minimum activation flow at distant fixtures is a manufacturer spec concern, not a CPC code check. | CPC 609.11 |

---

#### STEP 4: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what's wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation (e.g., venting for electric unit)

---

### Quick-Reference Tables

#### Common Water Heater Gas Input Ratings (CPC Table 1208.3.1)

| Water Heater Type | Typical BTU/h Input |
|-------------------|-------------------|
| Tank, 30-40 gallon | 35,000 |
| Tank, 50 gallon | 50,000 |
| Tank, 75 gallon | 75,000 |
| Tankless, 2 GPM | 142,800 |
| Tankless, 4 GPM | 285,000 |
| Tankless, 6 GPM (whole-house) | 428,400 |

#### First-Hour Rating Sizing (CPC Table 501.1(2))

| Bedrooms | Bathrooms | Min First-Hour Rating (gal) |
|----------|-----------|---------------------------|
| 1 | 1 | 38 |
| 2 | 1 | 38 |
| 2 | 2 | 46 |
| 3 | 2 | 56 |
| 4 | 2 | 60 |
| 4 | 3 | 66 |
| 5 | 3 | 74 |

#### Seismic Strapping Quick Check

- **Two straps required**: upper 1/3 and lower 1/3 of tank
- **Lower strap**: min 4 inches above controls
- **Strap material**: 3/4 in x 24-gauge (min) perforated steel plumber's tape or listed kit
- **Fasteners**: 1/4 in x 3 in lag screws to studs (flat wall: 5 in lag through gypsum)
- **Attachment**: Wall studs or masonry -- never drywall alone
- **Flexible connections**: Required at water/gas to allow seismic movement
- **Tankless**: Mounting bracket to studs satisfies requirement

#### T&P Discharge Pipe Quick Check

- **Diameter**: Min 3/4 in, same as valve outlet, full size to end
- **Termination**: 6-24 in above floor or grade, pointing down
- **End**: Not threaded (prevents capping)
- **Direction**: Slope downward continuously, no traps or uphill runs
- **Material**: Hard-drawn copper or galvanized pipe (rated for temperature)
- **Cannot discharge**: Into drain pan, into crawlspace, where it causes injury/damage, where subject to freezing
- **Independent**: Each T&P piped separately (not shared with condensate or other relief)
- **Observable**: Termination point must be readily visible

#### Hot Water Pipe Insulation Quick Check

| Nominal Pipe Diameter | Min Insulation Thickness |
|-----------------------|-------------------------|
| Up to 1 in | 1 in |
| Over 1 in to under 2 in | 1.5 in |
| 2 in and larger | 2 in |

Rule: Insulation thickness >= pipe diameter for pipes up to 2 in; 2 in for larger pipes.

#### Combustion Air Sizing Quick Check (Gas Only)

| Method | Sizing per Opening |
|--------|-------------------|
| Single exterior opening (upper 12 in) | 1 sq in / 3,000 BTU/h |
| Two direct exterior openings | 1 sq in / 4,000 BTU/h each |
| Two horizontal ducted openings | 1 sq in / 2,000 BTU/h each |
| Two vertical ducted openings | 1 sq in / 4,000 BTU/h each |
| Indoor air — standard method | 50 cu ft / 1,000 BTU/h room volume |
| Indoor air — known infiltration | Calculate under CPC 506.2.2 / CMC 701.4.2; required where known infiltration is below 0.40 ACH |
| Indoor openings to adjacent space | 1 sq in / 1,000 BTU/h, min 100 sq in |

#### Water Heater Connector Limits

| Connector Type | Max Length | Code |
|----------------|-----------|------|
| Copper/stainless flex | 24 in | CPC 604.13 |
| PEX/PE-RT proximity to WH | Not within first 18 in | CPC 604.13 |
| Gas flex connector | Per listing (typically 4-6 ft) | CPC 1212.1 |

---

### Key Principles

1. **Gas vs. electric is the primary branch**: Gas water heaters need venting, combustion air, and gas line checks. Electric units skip all of that but need dedicated circuit verification.

2. **Seismic strapping is always required in California**: Health & Safety Code 19211 requires all water heaters to be braced, strapped, or anchored. No exemptions for residential. This is the single most common inspection failure.

3. **Like-for-like is the easy path**: A same-fuel, same-capacity replacement in the same location is straightforward. Fuel switching (gas to electric) or capacity changes (tank to tankless) trigger additional code requirements.

4. **T&P relief is non-negotiable**: Every storage water heater must have a properly piped T&P relief valve. The discharge pipe requirements are specific and commonly violated (wrong termination height, threaded end, discharged into crawlspace or wall cavity, piped into drain pan).

5. **Location matters**: Bedroom/bathroom installations have combustion safety requirements. Garage installations have elevation requirements (though FVIR units are exempt) and require vehicle barriers. Attic/roof installations have access and platform requirements.

6. **Expansion tank depends on system type**: Only required when a backflow preventer, check valve, or PRV creates a closed system -- but many homes have these, so it comes up frequently.

7. **Piping and materials compliance**: All potable water materials must be NSF 61 compliant with lead content at or below 0.25%. Dissimilar metal joints require dielectric fittings at accessible locations. PEX and similar plastic tubing cannot be within 18 inches of the water heater.

8. **Hot water piping must be insulated**: CPC 609.12 requires insulation on all domestic hot water piping, with thickness matching or exceeding the pipe diameter. This is a commonly missed requirement on water heater replacements.
