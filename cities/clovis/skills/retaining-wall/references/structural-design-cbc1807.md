---
title: "Structural Design of Retaining Walls — CBC 1807, Lateral Loads, Stability Analysis"
category: "Structural Design"
relevance: "Any retaining wall review involving structural calculations, lateral soil loads, footing design, reinforcement, stability analysis, or seismic design"
key_code_sections: "CBC 1807.2, 1807.2.2, 1807.2.3, 1807.2.4, 1610, 1809; ASCE 7-22"
---

# Structural Design of Retaining Walls — CBC 1807

Source: 2025 California Building Code (Title 24, Part 2), Chapter 18 — Soils and Foundations, Section 1807 — Foundation Walls, Retaining Walls, and Embedded Posts and Poles; Section 1610 — Soil Lateral Loads.

---

## General Design Requirements (CBC 1807.2.1)

Retaining walls must be designed to ensure stability against all of the following failure modes:

| Failure Mode | Description | Design Check |
|-------------|-------------|--------------|
| **Overturning** | Wall rotating about the toe due to lateral earth pressure | Resisting moment / Overturning moment >= safety factor |
| **Sliding** | Wall sliding horizontally along the base | Resisting force / Driving force >= safety factor |
| **Bearing failure** | Soil under footing unable to support vertical loads | Actual bearing pressure <= allowable bearing pressure |
| **Water uplift** | Hydrostatic pressure pushing upward on footing | Addressed by drainage system; if present, include in stability |
| **Structural failure** | Wall stem or footing member fails in flexure, shear, or compression | Design per ACI 318 (concrete) or TMS 402 (masonry) |

---

## Lateral Soil Loads (CBC 1807.2.2 / 1610)

### Equivalent Fluid Pressure Method

The most common method for calculating lateral earth pressure on retaining walls. The soil is modeled as a fluid with a unit weight equal to the "equivalent fluid pressure."

**Lateral pressure at depth h:**
```
P(h) = gamma_eq x h
```
Where:
- P(h) = lateral pressure at depth h (psf)
- gamma_eq = equivalent fluid pressure (pcf or psf/ft)
- h = depth below top of retained soil (ft)

**Total lateral force per linear foot of wall:**
```
F = 0.5 x gamma_eq x H^2
```
Where:
- F = total horizontal force per linear foot (lb/ft)
- H = total height of retained soil (ft)

**This force acts at H/3 above the base** (triangular pressure distribution).

### Equivalent Fluid Pressure Values

| Soil Description | Active Pressure (psf/ft) | At-Rest Pressure (psf/ft) | Passive Pressure (psf/ft) | Notes |
|-----------------|--------------------------|---------------------------|---------------------------|-------|
| Clean sand, gravel (GW, GP, SW, SP) | 30 | 55 | 300+ | Best backfill material — use this |
| Sand with silt (SM) | 40 | 60 | 200 | Common backfill |
| Sand-silt mix | 45 | 65 | 200 | Moderate drainage |
| Silty clay (CL, ML) | 55 | 75 | 150 | Poor backfill — avoid if possible |
| Clay, expansive (CH) | 60 | 85 | 100 | Worst backfill — requires special design |

**When to use active vs at-rest:**

| Condition | Use |
|-----------|-----|
| Cantilever retaining wall (free to rotate at top) | Active pressure |
| Basement wall, wall braced at top, wall restrained from movement | At-rest pressure |
| Propped cantilever, tied-back wall | At-rest pressure |
| Wall on rigid foundation (cannot translate) | At-rest pressure |

### Rankine Active Earth Pressure (for level backfill)

```
Ka = (1 - sin(phi)) / (1 + sin(phi))
```

| Soil Friction Angle (phi) | Ka | Equivalent Fluid Pressure (120 pcf soil) |
|--------------------------|-----|------------------------------------------|
| 25 degrees | 0.406 | 49 psf/ft |
| 28 degrees | 0.361 | 43 psf/ft |
| 30 degrees | 0.333 | 40 psf/ft |
| 32 degrees | 0.307 | 37 psf/ft |
| 34 degrees | 0.283 | 34 psf/ft |
| 36 degrees | 0.260 | 31 psf/ft |

*For sloping backfill, the Rankine formula includes the slope angle and Ka increases significantly.*

### At-Rest Earth Pressure

```
Ko = 1 - sin(phi)
```

| Soil Friction Angle (phi) | Ko | Equivalent Fluid Pressure (120 pcf soil) |
|--------------------------|-----|------------------------------------------|
| 25 degrees | 0.577 | 69 psf/ft |
| 28 degrees | 0.531 | 64 psf/ft |
| 30 degrees | 0.500 | 60 psf/ft |
| 32 degrees | 0.470 | 56 psf/ft |
| 34 degrees | 0.441 | 53 psf/ft |
| 36 degrees | 0.412 | 49 psf/ft |

---

## Surcharge Loads

### Uniform Surcharge

A uniform surcharge (e.g., driveway, stored materials) is converted to an equivalent height of soil:

```
h_eq = q / gamma_soil
```

Where:
- h_eq = equivalent height of soil (ft)
- q = surcharge pressure (psf)
- gamma_soil = unit weight of soil (typically 120 pcf)

The surcharge adds a **uniform** (rectangular) lateral pressure over the full height of the wall:

```
P_surcharge = Ka x q  (or Ko x q for at-rest)
```

### Common Surcharge Values

| Surcharge Source | Load (psf) | Equivalent Height (ft) at 120 pcf |
|-----------------|-----------|-----------------------------------|
| Passenger vehicles / light residential driveway | 100-250 | 0.8-2.1 |
| Residential driveway (ASCE 7 minimum) | 40 psf (uniform) | 0.3 |
| Heavy vehicles (H-20 truck) | 250-480 | 2.1-4.0 |
| Residential floor loads (adjacent building) | 40-50 psf per story | 0.3-0.4 per story |
| Construction equipment | 250-500 | 2.1-4.2 |
| Stored materials | Per actual load | Varies |

### Sloping Backfill Surcharge

Sloping backfill behind the wall increases the active earth pressure coefficient. The modified Rankine formula for sloping backfill:

```
Ka = cos(beta) x [cos(beta) - sqrt(cos^2(beta) - cos^2(phi))] / [cos(beta) + sqrt(cos^2(beta) - cos^2(phi))]
```

Where beta = angle of backfill slope from horizontal.

| Backfill Slope | Ka Multiplier (vs level) | Impact |
|---------------|--------------------------|--------|
| Level (0 deg) | 1.00x | Baseline |
| 2H:1V (26.6 deg) | ~1.4x | 40% increase in lateral load |
| 1.5H:1V (33.7 deg) | ~1.7x | 70% increase in lateral load |
| 1H:1V (45 deg) | ~2.5x | 150% increase in lateral load — requires special design |

---

## Stability Analysis (CBC 1807.2.3)

### Safety Factors

| Condition | Minimum Factor of Safety |
|-----------|-------------------------|
| Sliding resistance (without seismic) | 1.5 |
| Overturning resistance (without seismic) | 1.5 |
| Sliding resistance (with seismic) | 1.1 |
| Overturning resistance (with seismic) | 1.1 |

### Load Basis for Stability

Per CBC 1807.2.3, stability analysis uses:
- **0.7 times nominal earthquake loads**
- **1.0 times other nominal loads**
- Investigation with **one or more variable loads set to zero** (to find the worst case)

**Important**: The standard load combinations of CBC Section 1605 do NOT apply to retaining wall stability calculations. The safety factor approach above is used instead.

### Overturning Analysis

```
Factor of Safety (overturning) = Sum of Resisting Moments / Sum of Overturning Moments
```

**Resisting moments** (about the toe):
- Weight of wall x distance from toe to wall centroid
- Weight of soil on heel x distance from toe to soil centroid
- Passive pressure at toe x H_passive/3

**Overturning moments** (about the toe):
- Active earth pressure resultant x H/3
- Surcharge lateral force x H/2
- Seismic earth pressure increment x 0.6H (acts higher on wall)

### Sliding Analysis

```
Factor of Safety (sliding) = Resisting Forces / Driving Forces
```

**Resisting forces**:
- Friction at base: mu x total vertical load (mu = coefficient of friction, typically 0.3-0.5 for concrete on soil)
- Passive pressure at toe (if applicable — use with caution, often reduced by 50% or ignored)
- Shear key resistance (if provided)

**Driving forces**:
- Total active earth pressure
- Surcharge lateral force
- Seismic lateral force increment

### Bearing Pressure Check

```
q_max = (V / B) x (1 + 6e/B)    [for e <= B/6 — within kern]
q_max = 2V / (3a)                [for e > B/6 — outside kern, trapezoidal]
```

Where:
- V = total vertical load on footing
- B = footing width
- e = eccentricity = (B/2) - (sum of moments about toe / V)
- a = 3 x (B/2 - e) = length of bearing area when outside kern

**q_max must be <= allowable bearing pressure from soils report.**

---

## Seismic Design

### When Seismic Lateral Earth Pressure Applies

Per CBC 1807.2.2, retaining walls supporting more than **6 feet of backfill** in **Seismic Design Category D, E, or F** must incorporate additional seismic lateral earth pressure per the geotechnical investigation.

> Most of California is SDC D or higher. This applies to nearly all engineered retaining walls over 6 ft.

### Mononobe-Okabe Method

The most common method for seismic lateral earth pressure. Adds a dynamic increment to the static active pressure:

```
delta_Pae = 0.5 x gamma x H^2 x (Kae - Ka)
```

Where Kae is the seismic active earth pressure coefficient, dependent on:
- Soil friction angle (phi)
- Wall friction angle (delta)
- Horizontal seismic coefficient (kh = 0.5 x SDS for yielding walls, 0.67 x SDS for non-yielding)
- Vertical seismic coefficient (kv — often taken as 0)

The seismic increment acts at approximately **0.6H** above the base (higher than the static resultant at H/3).

### Seismic Design Parameters

| Parameter | Source |
|-----------|--------|
| SDS (short-period design spectral acceleration) | ASCE 7-22 site-specific or mapped |
| kh (horizontal seismic coefficient) | Typically 0.5 x SDS (yielding walls) |
| Seismic earth pressure increment | Geotechnical report (required) |
| Safety factor with seismic | 1.1 (sliding and overturning) |

---

## Footing Design

### General Requirements (CBC 1809)

| Requirement | Specification | Code Section |
|-------------|---------------|--------------|
| Minimum depth below lower grade | 12 inches | CBC 1809.4 |
| Minimum width | Per structural analysis (typically 0.5-0.7 x wall height) | CBC 1809.7 |
| Concrete strength | f'c >= 2,500 psi (typically 3,000 psi specified) | CBC 1904 |
| Reinforcement | Per structural analysis; minimum per ACI 318 | ACI 318 |
| Bearing on rock | May reduce footing size per geotechnical recommendation | CBC 1809.4 |
| Stepped footings | Horizontal step length >= 2 ft; vertical step <= 2/3 horizontal | CBC 1809.8 |

### Typical Footing Proportions (Cantilever Walls)

| Wall Height (H) | Footing Width | Toe Length | Heel Length | Footing Depth |
|-----------------|---------------|------------|-------------|---------------|
| 4 ft | 2.5-3 ft | 0.5-1 ft | 1.5-2 ft | 10-12" |
| 6 ft | 3.5-4.5 ft | 0.8-1.2 ft | 2-3 ft | 12-14" |
| 8 ft | 5-6 ft | 1-1.5 ft | 3-4 ft | 14-18" |
| 10 ft | 6-7.5 ft | 1.2-2 ft | 4-5 ft | 18-24" |
| 12 ft | 7-9 ft | 1.5-2.5 ft | 5-6 ft | 20-24" |

*These are approximate starting points. Actual dimensions determined by structural analysis based on soil conditions, surcharge, and seismic loads.*

### Shear Key

A shear key is a vertical projection below the bottom of the footing that increases sliding resistance:

| Component | Typical Dimension |
|-----------|-------------------|
| Width | 4-6 inches |
| Depth | 6-12 inches below bottom of footing |
| Location | Usually at the stem or slightly toward the heel |
| Reinforcement | #4 or #5 dowels connecting key to footing |

The shear key engages passive soil pressure in front of the key, significantly increasing sliding resistance.

---

## Segmental Retaining Walls (CBC 1807.2.4)

### Standards

Dry-cast concrete units for segmental retaining walls (SRW) must comply with **ASTM C1372** — Standard Specification for Segmental Retaining Wall Units.

### Key Requirements

| Requirement | Specification |
|-------------|---------------|
| Block material | ASTM C1372 dry-cast concrete |
| Minimum compressive strength | 3,000 psi (average of 3 units) |
| Maximum water absorption | 10 lb/ft^3 (average of 3 units) |
| Batter (setback per course) | Typically 3/4" to 1-1/4" per course (manufacturer-specific) |
| Geogrid reinforcement | Required for walls over 3-4 ft (manufacturer design tables) |
| Base course | Leveling pad of compacted crushed stone, minimum 6" thick x 24" wide |
| Drainage | Drain rock fill behind blocks required; perforated pipe at base |
| Filter fabric | Between drain rock and native soil |

### Geogrid Reinforcement for SRW

| Wall Height | Geogrid Layers (typical) | Minimum Embedment Length |
|-------------|--------------------------|--------------------------|
| Up to 3 ft | 0 (gravity wall OK) | N/A |
| 3-5 ft | 1-2 layers | 4-6 ft beyond back of block |
| 5-8 ft | 2-4 layers | 6-8 ft beyond back of block |
| 8-12 ft | 4-6 layers | 8-12 ft beyond back of block |
| Over 12 ft | Per engineered design | Per engineered design |

*Geogrid spacing and embedment length per manufacturer design tables or site-specific engineering. Most SRW manufacturers (Allan Block, Keystone, Versa-Lok) provide free design software and engineering support.*

---

## Retaining Wall Types — Structural Comparison

| Wall Type | Typical Height Range | Engineering Required? | Key Design Feature |
|-----------|---------------------|----------------------|-------------------|
| Gravity (mass concrete, stone) | Up to 3-4 ft | No (prescriptive OK) | Self-weight resists overturning |
| Cantilever (reinforced concrete L or T) | 4-12 ft | Yes | Heel soil weight assists stability |
| Counterfort / buttress | 12-25 ft | Yes | Vertical ribs reduce stem bending |
| Segmental (SRW with geogrid) | Up to 15-20 ft | Yes (>4 ft) | Batter + geogrid reinforcement |
| Soldier pile / lagging | Any (typically >8 ft) | Yes | H-piles with lagging panels |

---

## Common Structural Review Flags

1. **No stability analysis shown**: Every engineered retaining wall submission must include overturning and sliding safety factor calculations. If only the structural member design is shown without stability, flag it.

2. **Active pressure used where at-rest applies**: If the wall is restrained at the top (e.g., slab or pavement at top of wall), at-rest pressure must be used, which is 50-80% higher than active pressure.

3. **Surcharge not included**: Check the site plan for driveways, buildings, or slopes behind the wall. If present, the structural calculations must include the surcharge.

4. **Bearing pressure exceeds allowable**: Compare the maximum bearing pressure (toe of footing) with the allowable bearing pressure from the soils report. Eccentric loading concentrates pressure at the toe.

5. **No seismic design for walls >6 ft**: In SDC D/E/F (most of California), walls retaining >6 ft of backfill must include seismic lateral earth pressure per CBC 1807.2.2.

6. **Safety factors calculated with wrong load combinations**: CBC 1605 standard load combinations do NOT apply to retaining wall stability. Use the CBC 1807.2.3 approach (0.7x seismic + 1.0x other, SF of 1.5/1.1).
