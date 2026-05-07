---
title: "GFCI Protection and Equipment Location Requirements"
category: "Safety"
relevance: "EV charger reviews involving location, GFCI, and physical protection"
key_code_sections: "CEC 110.26, 210.8(A), 210.8(F), 625.50, 625.54, 625.56, 110.27(B)"
---

# GFCI Protection and Equipment Location for EV Chargers

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 210, 625, and 110.

---

## GFCI Protection Requirements

EV charger installations have **two overlapping GFCI requirements**:

### 1. All EV Receptacles — CEC 625.54

**All receptacles installed for electric vehicle charging shall have GFCI protection for personnel.**

This is a blanket requirement — regardless of location (indoor, outdoor, garage). If it's an EV charging receptacle, it needs GFCI.

### 2. Location-Based GFCI — CEC 210.8(A)

All 125-250V receptacles on single-phase branch circuits rated 150V or less to ground require Class A GFCI protection in these dwelling unit locations:

| Location | GFCI Required? | Relevant to EV? |
|----------|---------------|-----------------|
| **Garages and accessory buildings** (floors at/below grade) | **Yes** | **Primary EV location** |
| **Outdoors** | **Yes** | **Common EV location** |
| Bathrooms | Yes | No |
| Crawl spaces at/below grade | Yes | Rarely |
| Basements | Yes | Sometimes |
| Kitchens | Yes | No |
| Within 6 ft of sinks | Yes | No |
| Laundry areas | Yes | No |
| Indoor damp/wet locations | Yes | Sometimes |

### 3. Outdoor Outlet GFCI — CEC 210.8(F)

**All outdoor outlets** for dwellings supplied by single-phase circuits rated ≤150V to ground and ≤50A shall have GFCI protection. This includes:
- Garages with floors at or below grade
- Accessory buildings
- All other outdoor receptacle outlets

**Exception 1**: Receptacles not readily accessible and supplied by a dedicated branch circuit for snow-melting, deicing, or pipeline heating equipment (CEC 426.28 or 427.22 applies instead).

### Practical Impact for EV Chargers

| EV Charger Location | GFCI Required By |
|---------------------|-----------------|
| Inside garage | CEC 625.54 + 210.8(A)(2) |
| Outside on wall | CEC 625.54 + 210.8(A)(3) + 210.8(F) |
| Outside on pedestal | CEC 625.54 + 210.8(A)(3) + 210.8(F) |
| Inside basement | CEC 625.54 + 210.8(A)(5) |
| Carport | CEC 625.54 + 210.8(A)(3) |

**Bottom line**: GFCI/personnel protection is always required for residential EV chargers, no exceptions.

### Hardwired EVSE — Do NOT Mark GFCI as "N/A"

CEC 625.54 says "receptacles" but CEC 625.22 requires a "listed system of protection against electric shock" for ALL EVSE — including hardwired units. Most listed Level 2 hardwired EVSE (Tesla Wall Connector, Grizzl-E, ChargePoint Home Flex, etc.) have GFCI protection built into the unit.

**For permit review**: When the installation is hardwired (not receptacle-based), mark GFCI as **PASS** if the EVSE manufacturer specs confirm built-in ground fault protection. Only mark FAIL if the unit lacks built-in GFCI and no external GFCI breaker is specified. Never mark N/A — personnel protection is always required per 625.22.

---

## Weatherproof Enclosures — Outdoor Installations (625.56)

All receptacles in **wet locations** used for EV charging shall have an enclosure that is weatherproof with the attachment plug inserted or removed.

- Outlet box hood installed for this purpose shall be **listed and identified as "extra duty"**
- Other listed products providing weatherproof protection are not required to be marked "extra duty"

---

## Equipment Mounting Height (625.50)

Unless specifically listed and marked otherwise:

| Location | Minimum Height for Coupling Means |
|----------|----------------------------------|
| **Indoor** | **18 inches (450 mm)** above floor level |
| **Outdoor** | **24 inches (600 mm)** above grade level |

**Exception**: Does not apply to portable EVSE connected per 625.44(A).

**Why this matters**: The EV connector (the plug that goes into the car) must be stored or mounted at these minimum heights. This prevents damage and keeps the connector off the ground.

---

## Working Space Requirements (110.26)

All electrical equipment (including EVSE, panels, and disconnects) must have adequate working space for safe operation, maintenance, and emergency access.

### Minimum Working Space Dimensions

| Dimension | Requirement | Code Section |
|-----------|------------|--------------|
| **Depth** | 36 inches (914 mm) minimum from front of equipment | CEC 110.26(A)(1), Condition 1 |
| **Width** | 30 inches (762 mm) minimum, or width of equipment, whichever is greater | CEC 110.26(A)(2) |
| **Height** | 6 ft 6 in (2.0 m) minimum, or height of equipment, whichever is greater | CEC 110.26(A)(3) |

### Working Space Conditions (Table 110.26(A)(1))

For equipment rated 0-150V nominal to ground (typical residential 120/240V EVSE):

| Condition | Description | Min. Depth |
|-----------|------------|------------|
| **Condition 1** | Exposed live parts on one side, no live/grounded parts on other side | 3 ft (914 mm) |
| **Condition 2** | Exposed live parts on one side, grounded parts on other side (concrete/brick wall counts as grounded) | 3 ft (914 mm) |
| **Condition 3** | Exposed live parts on both sides | 3 ft (914 mm) |

> For residential EV charger installations (0-150V to ground), all three conditions require the same 3-foot depth. The working space must extend to the floor or grade and must not be used for storage. Equipment doors must be openable to at least 90 degrees.

### Practical Application for EV Chargers

- **Panel working space**: The main electrical panel must maintain 30" wide x 36" deep x 6'6" tall clear space. If the EV charger circuit originates from this panel, verify this space is maintained.
- **EVSE working space**: The EVSE itself must have adequate clearance for operation and maintenance.
- **Garage installations**: Common issue — storage items (shelves, bikes, boxes) encroaching on panel or EVSE working space. The working space cannot be used for storage.

---

## Physical Protection (110.27(B))

Equipment shall be protected against physical damage. For EV chargers, this means:

- **Garage installations**: Mount EVSE on the side wall, out of the direct vehicular path
- **Outdoor installations**: Consider bollards, posts, or other physical protection if the EVSE is in a driveway or parking area
- **General**: Equipment likely to be exposed to physical damage shall be protected by guards, enclosures, or location

> The CEC does not prescribe specific guard dimensions — it's a performance requirement. The inspector will evaluate whether the installation is adequately protected given the specific conditions.

---

## Summary: Location Compliance Checklist

For any EV charger installation, verify:

- [ ] GFCI protection provided (required everywhere for EV)
- [ ] Coupling means at correct height (18" indoor / 24" outdoor)
- [ ] Working space maintained (30" wide x 36" deep x 6'6" high minimum)
- [ ] Physical protection adequate (not in vehicular path, guards if needed)
- [ ] Weatherproof enclosure if outdoor/wet location
- [ ] Equipment listed by NRTL (UL, ETL, CSA, etc.)
