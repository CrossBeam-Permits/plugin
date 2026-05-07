---
title: "CEC Article 690 Part V -- Grounding and Bonding for PV Systems"
category: "Grounding and Bonding"
relevance: "Every solar PV review involving grounding, bonding, or ground-fault protection"
key_code_sections: "CEC 690.41, 690.42, 690.43, 690.45, 690.47, 250.122, 250.134, 250.166"
---

# Grounding and Bonding for PV Systems

Source: 2025 California Electrical Code (Title 24, Part 3), Article 690 Part V; Article 250.

---

## DC Circuit Grounding Configurations (690.41(A))

PV system DC circuits may use one or more of these configurations:
1. **2-wire with one functionally grounded conductor**
2. **Bipolar** with functional ground reference (center tap) per 690.7(C)
3. **Circuits not isolated** from grounded inverter output circuit
4. **Ungrounded** circuits
5. **Solidly grounded** as permitted in 690.41(B)
6. Circuits protected by **listed equipment identified for the use**

**Most residential microinverter systems use ungrounded DC inputs** and rely on the AC side equipment grounding conductor for the ground connection.

---

## DC Ground-Fault Protection (690.41(B))

### When Required
PV DC circuits exceeding **30V or 8A** shall have GFDI (Ground-Fault Detector-Interrupter) protection.

**Exception**: Solidly grounded PV source circuits with <=2 modules in parallel and NOT on/in buildings.

### GFDI Requirements

1. **Detection (690.41(B)(1))**: Device or system shall detect ground faults in PV DC circuits including functionally grounded conductors. Must be **listed for GFDI protection**.

2. **Faulted Circuit Control (690.41(B)(2))**: One of:
   - Automatically disconnect current-carrying conductors of faulted circuit
   - Cease supply to output circuits AND interrupt faulted circuits from ground reference

3. **Indication (690.41(B)(3))**: Fault indication at a **readily accessible location** (remote indicator light, display, alarm, web notification).

---

## Grounding Connection Point (690.42)

### With GFDI Protection (690.42(A))
Any circuit-to-ground connection made **by the GFDI equipment** (not elsewhere).

### Solidly Grounded (690.42(B))
Connection from any single point on PV DC system to the grounding electrode system per 690.47(A).

---

## Equipment Grounding and Bonding (690.43)

### General Requirement
**All** exposed noncurrent-carrying metal parts shall be connected to an equipment grounding conductor (EGC) per 250.134 or 250.136, **regardless of voltage**.

This includes:
- PV module frames
- Electrical equipment enclosures
- Conductor enclosures
- Mounting structures/racks

### Module Mounting Systems (690.43(A))
Devices and systems used for mounting that also bond module frames shall be **listed, labeled, and identified for bonding PV modules**.

Reference: UL 2703 (Mounting Systems, Clamping/Retention Devices, and Ground Lugs for PV Modules).

### Equipment on Grounded Metal Supports (690.43(B))
- Listed bonding/grounding devices permitted to bond equipment to grounded metal supports
- Metallic support structures shall have **identified bonding jumpers** between separate sections OR be **identified for equipment bonding** and connected to EGC

### EGC Location (690.43(C))
- EGC may run separately from PV conductors **within the PV array**
- Where PV conductors **leave the array vicinity**: EGC per 250.134 (in same raceway/cable as circuit conductors)

### Bonding for Over 250V (690.43(D))
Requirements of 250.97 apply only to **solidly grounded** PV circuits operating over 250V to ground.

---

## Equipment Grounding Conductor Sizing (690.45)

EGC sized per **Table 250.122**.

Where no OCPD in the circuit: use an **assumed OCPD rated per 690.9(B)** when applying Table 250.122.

**Voltage drop upsizing of EGC not required** (690.45).

### Table 250.122 -- Minimum Size Equipment Grounding Conductors

| OCPD Rating (A) | Copper (AWG) | Aluminum/Cu-Clad Al (AWG) |
|-----------------|-------------|--------------------------|
| 15 | #14 | #12 |
| 20 | #12 | #10 |
| 30 | #10 | #8 |
| 40 | #10 | #8 |
| 60 | #10 | #8 |
| 100 | #8 | #6 |
| 200 | #6 | #4 |
| 300 | #4 | #2 |
| 400 | #3 | #1 |

*Where necessary to comply with 250.4(A)(5) or (B)(4), EGC shall be sized larger than given in this table.*

---

## Grounding Electrode System (690.47)

### Buildings/Structures Supporting PV (690.47(A))

PV array EGC shall be connected to a grounding electrode system per Part VII of Article 250 (250.50 et seq.).

**For systems NOT solidly grounded** (most residential):
- The EGC connected to associated distribution equipment (e.g., inverter AC output to panelboard) that connects to the grounding electrode system is **sufficient** as the only ground connection (690.47(A)(1)).

**For solidly grounded systems**:
- Grounded conductor connected to grounding electrode system via grounding electrode conductor sized per **250.166** (690.47(A)(2)).
- Sizing per 250.166:
  - If neutral present: not smaller than neutral
  - If no neutral: not smaller than largest conductor
  - Minimum: #8 copper or #6 aluminum

### Additional Grounding Electrodes (690.47(B))
- Permitted per 250.52 and 250.54
- May connect directly to PV module frames or support structure
- Grounding electrode conductor sized per **250.66**
- Ground-mounted array support structure may serve as grounding electrode if meeting 250.52
- Building-mounted arrays may use metal structural frame per 250.68(C)(2)

---

## Practical Application for Residential Microinverter Systems

Most residential rooftop systems use microinverters with ungrounded DC inputs. The grounding path is:

1. **Module frames** bonded to **racking/mounting system** via listed bonding devices (UL 2703 lugs/clamps)
2. **Racking system** connected to **equipment grounding conductor (EGC)** via bonding jumper or listed bonding device
3. **EGC** run with AC circuit conductors in conduit back to **main panel**
4. **Main panel** connected to **grounding electrode system** (ground rod, Ufer, water pipe, etc.)

### Key Inspection Points
- Verify bonding lug/clamp at each module is listed for PV bonding (UL 2703)
- Verify continuity through entire array (bonding between rail sections)
- Verify EGC size per Table 250.122 based on OCPD rating
- Verify EGC runs with AC conductors after leaving array
- Verify connection to building grounding electrode system

---

## Grounded vs. Ungrounded System Summary

| Feature | Ungrounded (most residential) | Solidly Grounded |
|---------|------------------------------|-----------------|
| DC ground-fault protection | Required (GFDI) per 690.41(B) | Required per 690.41(B) unless <=2 parallel modules and not on buildings |
| Grounding connection | Via EGC to AC distribution equipment GES | Direct to GES via GEC per 250.166 |
| White conductor permitted | No -- only for solidly grounded (690.31(B)(2)) | Yes |
| Additional GEC sizing | N/A | Per 250.166 |
| Typical application | Microinverters, most string inverters | Older systems, some commercial |
