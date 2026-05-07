---
title: "CEC Article 250 — Supply-Side Bonding, Intersystem Bonding, and Piping Bonding"
category: "Bonding"
relevance: "Panel upgrade reviews — supply-side bonding, intersystem bonding termination, piping and structural bonding"
key_code_sections: "CEC 250.8, 250.10, 250.12, 250.24(D), 250.64(B), 250.64(C), 250.64(E), 250.64(F), 250.68, 250.70, 250.86, 250.92, 250.94, 250.96, 250.102(C), 250.104, 250.106, 250.142"
---

# CEC Article 250 — Supply-Side Bonding, Intersystem Bonding, and Related Requirements

Source: 2025 California Electrical Code (Title 24, Part 3), Article 250.

This reference covers the bonding requirements beyond the basic grounding electrode system — specifically supply-side bonding of service raceways, intersystem bonding for communications, piping and structural steel bonding, GEC connection details, and connection methods. These are commonly cited in panel upgrade inspections.

---

## Supply-Side Bonding (250.92)

All service equipment, raceways, cable armor, and enclosures containing service conductors must be **effectively bonded**.

### 250.92(A) — What Must Be Bonded

On the supply side of the service (between the utility connection and the service disconnect):
- Service raceways (conduit from meter to panel)
- Cable armor or sheath
- Enclosures containing service conductors
- All metallic components between the point of attachment and the service disconnect

### 250.92(B) — Bonding Methods

| Method | Acceptable? |
|--------|-------------|
| **Threaded couplings or listed threaded hubs, wrench-tight** | Yes (250.92(B)(2)) |
| **Standard locknuts** | **NO** — not acceptable on supply side (250.92(B)(2)) |
| **Bonding locknuts** | Yes, but only where no remaining concentric knockouts are present (250.92(B)(4)) |
| **Bonding jumpers around impaired connections** | Required where concentric knockouts or reducing washers are present (250.92(B)(2)) |
| **Bonding bushings** | Yes — grounding-type bushings with bonding jumper |

**Common violation**: Using standard locknuts on service entrance conduit connections instead of bonding means.

### 250.102(C) — Supply-Side Bonding Jumper Sizing

Supply-side bonding jumpers shall be sized per **Table 250.102(C)(1)** — the same table used for the main bonding jumper. See the grounding-bonding-250.md reference for the full table.

### 250.142(A) — Neutral as Bonding Means (Supply Side)

On the **supply side** of the service, the neutral (grounded conductor) **may** be used to bond equipment. This is acceptable because:
- There is no overcurrent protection between the utility and the service disconnect
- The neutral is bonded to the equipment at the service panel

### 250.142(B) — Load Side Restrictions

On the **load side** of the service, grounding load-side equipment to the neutral is **NOT acceptable**, with limited exceptions for existing ranges and dryers (minimum #10 Cu or #8 Al, insulated neutral, originating at service equipment).

---

## GEC Connection Details

### 250.24(D) — What the GEC Connects

The grounding electrode conductor (GEC) connects:
- Equipment grounding conductors
- Service equipment enclosure
- Service neutral (grounded conductor)

...to the grounding electrode system.

### 250.24(A)(1) — GEC Connection Point

The GEC must connect to the grounded (neutral) conductor at an accessible point from the load end of the service drop or service lateral to (and including) the neutral bus in the service disconnect.

### 250.64(C) — Splice Restrictions

The GEC shall be **continuous without splice**, except:
- Listed irreversible compression connectors
- Exothermic welding
- Connections to busbars per 250.64(F)(3)

### 250.68(A) — Accessibility of Connections

All GEC connections shall be **accessible** for inspection, except:
- Connections buried in earth
- Connections encased in concrete (250.68(A) Exception 1)

---

## GEC Connection to Electrodes (250.64(F))

### 250.64(F)(1) — Common Electrode Connection

The GEC may connect to **any single electrode** in the grounding electrode system where all other electrodes are interconnected by bonding jumpers.

### 250.64(F)(2) — Individual GECs

Individual GECs may connect separately to individual electrodes within the system.

### 250.64(F)(3) — Common Bus

GECs may connect to a **common grounding bus** that is:
- Securely fastened
- Accessible
- At least 6 mm (1/4 in) thick and 50 mm (2 in) wide

### 250.68(C)(2) — Structural Steel as Connection Point

Metal structural framing may be used to interconnect GECs. Hold-down anchor bolts of metal structural columns can serve as connection points.

### 250.68(C)(3) — Ufer Extension as Connection Point

A Ufer (concrete-encased electrode) bar extended through the foundation may be used as a GEC connection point if:
- Accessible
- Not subject to corrosion

**Important**: The Ufer itself shall **not** be used to interconnect other electrodes (250.68(C)(3) Note 19).

---

## GEC Protection (250.64(B))

### Physical Protection Requirements

| GEC Size | Protection Required? |
|----------|---------------------|
| **#8 AWG** | Must be in raceway or armor (250.64(B)(3)) |
| **#6 AWG or larger** | Not required if securely fastened on building surface and not exposed to physical damage (250.64(B)(1)) |
| **Any size exposed to damage** | Must be protected with RMC, IMC, PVC Schedule 80, RTRC, EMT, or cable armor (250.64(B)(2)) |

### 250.64(E) — Ferrous Raceway Bonding

If the GEC is enclosed in a **ferrous (steel) raceway**, both ends of the raceway must be bonded to:
- The GEC, or
- The enclosure, or
- The electrode

The bonding jumper must be the **same size as the enclosed GEC** (250.64(E)(2)).

**Why**: Without bonding at both ends, electromagnetic induction in the steel conduit creates heating and impedes fault current flow.

---

## Connection Methods (250.70, 250.8)

### 250.70 — Electrode Connection Methods

| Connection Type | Requirement |
|----------------|-------------|
| **Buried clamps** | Must be listed and labeled for direct burial (marked "DB") |
| **Water pipe clamps** | Must be listed for use on copper water tubing |
| **Ufer clamps** | Must be listed for rebar/concrete encasement |
| **Maximum conductors per clamp** | One conductor unless listed for more |

### 250.8(A) — Permitted Bonding Connection Methods

- Listed pressure connectors
- Terminal bars
- Exothermic welding
- Machine screws engaging at least 2 threads (or secured with a nut)
- Thread-forming machine screws with at least 2 threads in the enclosure
- Connections that are part of a listed assembly

### 250.8(A) — Prohibited Methods

- **Sheet metal screws** — NOT permitted for bonding connections
- **Drywall screws** — NOT permitted for bonding connections

### 250.8(B) — No Solder-Only Connections

Connections shall **not depend solely on solder** for electrical continuity.

### 250.12 / 250.96 — Clean Contact Surfaces

Nonconductive coatings (paint, enamel, lacquer) must be **removed from contact surfaces** to ensure electrical continuity.

### 250.10 — Protection of Fittings

Clamps and fittings shall be protected from physical damage by location or enclosures, unless approved for applications without protection.

---

## Intersystem Bonding (250.94)

An **intersystem bonding termination (IBT)** device is required at the service equipment. This is for bonding communication systems (phone, cable TV, data) to the electrical grounding system.

### 250.94(A) — IBT Requirements

| Requirement | Specification |
|-------------|---------------|
| **Location** | External to service equipment and at disconnecting means of separate buildings (250.94(A)(1)) |
| **Accessibility** | Must be accessible for connection and inspection (250.94(A)(1)) |
| **No interference** | Must not interfere with opening the enclosure cover (250.94(A)(3)) |
| **Mounting** | Mount to meter enclosure, service enclosure, or nonflexible metal service raceway — OR connect with **#6 Cu** from IBT to one of these (250.94(A)(4)) |
| **Separate buildings** | Mount to disconnecting means or connect with #6 Cu (250.94(A)(5)) |
| **Listed** | Must be listed as grounding and bonding equipment (250.94(A)(6)) |

### 250.94(B) — IBT Specifications

The IBT may be:
- An aluminum or copper busbar
- Minimum **6 mm (1/4 in) thick** by **50 mm (2 in) wide**
- Sufficient length for at least **3 terminals** for communication systems

### Minimum Bond Wires

| Bond | Minimum Size |
|------|-------------|
| IBT to service enclosure | #6 Cu |
| Communication system bonds to IBT | #14 Cu |

---

## Bonding of Piping and Building Steel (250.104)

### 250.104(B) — Other Metal Piping

Any metal piping system **capable of becoming energized** must be bonded, including:
- Gas piping
- Metal HVAC ducts
- Other metal piping

### 250.104(C) — Structural Building Steel

Structural metal building frames shall be bonded using bonding jumpers sized per Table 250.102(C)(1). Bond to:
- Service enclosure
- Grounded service conductor
- GEC
- Disconnecting means for buildings supplied by a feeder

### Water Pipe Bonding

Water pipe bonding jumpers shall be sized per **Table 250.102(C)(1)**. The bonding must ensure continuity around:
- Water meters
- Filters
- Pressure regulators
- Similar equipment that might break the metallic path (250.53(D)(1))

### 250.106 — Lightning Protection

Where a building has a lightning protection system, it shall be **bonded to the grounding electrode system (GES)**.

---

## Bonding of Other Enclosures (250.86, 250.96)

### 250.86 — Metal Enclosures

Metal enclosures of conductors, devices, and equipment must be bonded to the EGC.

**Exception**: Short sections of protective metal raceways are exempt when isolated by at least 450 mm (18 in) of soil cover or 50 mm (2 in) of concrete.

### 250.96(A) — Raceway and Cable Bonding

Metal raceways, cable armor, cable sheath, enclosures, frames, and fittings that serve as EGCs shall be bonded. Nonconductive coatings must be removed before adding bonding jumpers, or fittings that make such removal unnecessary must be used.

---

## Common Supply-Side/Bonding Inspection Failures

1. **Standard locknuts on service conduit** — must use bonding means
2. **Missing IBT device** — no intersystem bonding termination for communication systems
3. **GEC splice with wire nut** — must use irreversible compression or exothermic welding
4. **#8 GEC exposed without protection** — must be in raceway or armor
5. **Steel conduit on GEC not bonded at both ends** — inductive heating hazard
6. **Paint not removed from bonding surfaces** — prevents electrical continuity
7. **Water pipe bonding jumper missing around meter** — continuity broken at meter
8. **Gas piping not bonded** — metal piping capable of becoming energized
9. **Sheet metal screws used for bonding** — prohibited method
