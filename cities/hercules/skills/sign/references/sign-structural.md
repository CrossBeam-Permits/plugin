---
title: "Sign Structural Requirements"
category: "Structural"
relevance: "Every sign permit — wind loads, seismic design, attachment, foundations for freestanding signs"
key_code_sections: "CBC 3107.1, Appendix H (H105.1-H105.6, H109-H112); CBC 1609 (wind loads); ASCE 7 Ch 29 (sign wind loads)"
---

# Sign Structural Requirements

Source: 2025 California Building Code (Title 24, Part 2), Chapter 31 Section 3107, Appendix H, Chapter 16; ASCE 7-22.

---

## General Design Requirement

CBC 3107.1 states simply: "Signs shall be designed, constructed and maintained in accordance with this code." This one-line section directs all sign structural design to the general structural provisions of Chapter 16 and the detailed sign provisions of Appendix H.

## Wind Load Design (CBC 1609 / ASCE 7)

### Wind Speed Determination

Signs must be designed for wind loads per CBC Chapter 16 (H105.3). Wind speed is determined from CBC Figures 1609.3(1) through 1609.3(4) based on Risk Category.

| Risk Category | Typical Use | Wind Speed Source |
|---|---|---|
| I | Low-hazard structures | Figure 1609.3(1) |
| II | Standard commercial buildings | Figure 1609.3(2) — most common |
| III | Assembly, high-occupancy | Figure 1609.3(3) |
| IV | Essential facilities | Figure 1609.3(4) |

For most of California, the basic wind speed V for Risk Category II is 110-115 mph. Coastal areas may be higher.

### Sign Wind Pressure Calculation (ASCE 7 Chapter 29)

ASCE 7-22, Chapter 29 provides the method for calculating wind loads on signs (classified as "Other Structures — Signs"):

- **Freestanding solid signs** (ground/monument signs): Use ASCE 7 Section 29.3, which provides force coefficients (Cf) based on the aspect ratio (B/s) and clearance ratio (s/h).
- **Attached signs** (wall-mounted, projecting): Treated as components and cladding of the building structure per ASCE 7 Chapter 30.
- **Open signs** (channel letters, skeleton): Reduced effective area applies — typically use the solid area ratio.

### Key Wind Design Parameters

| Parameter | Description | Source |
|---|---|---|
| V | Basic wind speed (mph) | CBC Figures 1609.3(1)-(4) |
| Kz | Velocity pressure exposure coefficient | ASCE 7 Table 26.10-1 |
| Kzt | Topographic factor | ASCE 7 Section 26.8 |
| Kd | Wind directionality factor (0.85 for signs) | ASCE 7 Table 26.6-1 |
| Cf | Force coefficient (varies by sign type/aspect ratio) | ASCE 7 Figure 29.3-1 |
| qz | Velocity pressure at height z | ASCE 7 Eq. 26.10-1 |

### Exposure Categories (CBC 1609.4)

| Exposure | Description |
|---|---|
| B | Urban/suburban, closely spaced obstructions |
| C | Open terrain, scattered obstructions <30 ft — default when B or D does not apply |
| D | Flat, unobstructed areas, water surfaces |

## Seismic Design

### General Rule (H105.4)

Signs designed to withstand wind pressures are generally considered capable of withstanding earthquake loads. However, this exception does not apply where Chapter 16 specifically requires seismic analysis.

### When Seismic Analysis is Required

ASCE 7 Chapter 13 (Nonstructural Components) applies to signs attached to buildings:
- Signs with a weight exceeding 400 lbs or occupying more than a certain area may trigger nonstructural component seismic design per ASCE 7 Section 13.5.
- Freestanding signs over 4 ft tall supported on the ground require seismic design per ASCE 7 Chapter 15 (Nonbuilding Structures).
- In Seismic Design Categories D, E, or F (most of California), seismic design is generally required for all signs.

## Working Stresses (H105.5)

For outdoor advertising display signs:
- Allowable working stresses must conform to CBC Chapter 16.
- Steel: Per Chapter 22 (Steel).
- Wood: Per Chapter 23 (Wood).
- Wire rope and fastenings: Not to exceed 25% of ultimate strength.
- Chains, cables, guys, steel rods: Not to exceed 1/5 (20%) of ultimate strength.

## Attachment Requirements (H105.6)

Signs attached to masonry, concrete, or steel must be fastened with:
- Metal anchors
- Bolts
- Approved expansion screws
- Sufficient size and anchorage to safely support applied loads

**Critical rule:** Wood blocks shall NOT be used for anchorage, except for wall signs on wood-framed buildings (H111.2).

### Wall Sign Attachment (H111.2)

| Fastener Type | Min Size | Min Embedment | Material |
|---|---|---|---|
| Expansion screws/bolts in masonry/concrete | 3/8" diameter | 5" | Metal |
| Through-bolts in wood walls | Per engineering | Through wall, plated on interior | Metal |

**Prohibited:** Anchorage to an unbraced parapet wall (H111.2, H112.3).

### Projecting Sign Attachment (H112.1-H112.3)

- Must use metal supports: bolts, anchors, chains, guys, or steel rods.
- **Staples and nails are prohibited** for projecting signs.
- Dead load and wind load supports: chains/guys/steel rods with minimum 3/8" net cross-section diameter.
- Supports at minimum 45-degree angle with horizontal (dead load) and 45 degrees with sign face (wind).
- If sign exceeds 30 sq ft facial area: minimum 2 supports per side, max 8 ft apart.
- Turnbuckles required in chains/guys/steel rods.
- Lag screws: minimum 5/8" bolt or lag screw with expansion shield.

### Projecting Sign Service Loads (H112.5)

Projecting sign structures that may support a person on a ladder for servicing must withstand:
- 100-lb concentrated horizontal load, AND
- 300-lb concentrated vertical load
- Applied at the point of most eccentric loading.
- The building component to which the sign is attached must also be designed for these loads.

## Freestanding/Ground Sign Requirements (H109)

### Height Restrictions (H109.1)

| Construction | Maximum Height |
|---|---|
| Combustible structural frame | 35 ft above ground |
| Entirely noncombustible | 100 ft above ground |
| Greater heights | Only if approved and not creating a public hazard |

### Required Clearance (H109.2)

The bottom coping of every ground sign must be minimum **3 feet** above ground or street level. This space may be filled with platform decorative trim or light wooden construction.

### Wood Anchors/Supports (H109.3)

Where wood anchors or supports are embedded in soil, the wood must be pressure-treated with an approved preservative.

### Foundation Design

Foundations for freestanding signs must be designed per CBC Chapter 18 (Soils and Foundations):
- Soil bearing capacity analysis required for large signs.
- Frost depth consideration (generally not an issue in coastal California).
- Lateral load resistance (overturning moment from wind).
- Foundation must resist both vertical dead load and lateral wind/seismic overturning forces.

## Roof Sign Requirements (H110)

### Materials (H110.1)

Roof signs must be constructed entirely of metal or approved noncombustible material, except:
- Combustible materials allowed per H106.1.1 (internally illuminated sign facings) and H107.1.

### Clearance Requirements (H110.1)

| Requirement | Dimension |
|---|---|
| Clear space between roof level and lowest part of sign | Min 6 ft |
| Clearance between vertical supports | Min 5 ft |
| Projection beyond exterior wall | Not permitted |

**Exception:** Signs on flat roofs where every part of the roof is accessible.

### Bearing Plates (H110.2)

Bearing plates must distribute loads directly to:
- Masonry walls
- Steel roof girders
- Columns or beams

The building must be designed to avoid overstress of these members.

### Height Limits for Roof Signs

| Sign Type | Type I/II Construction | Type III/IV/V Construction |
|---|---|---|
| Solid surface | 24 ft max (any construction) | 24 ft max |
| Open (>=40% open area) | 75 ft max | 40 ft max |
| Closed | 50 ft max | 35 ft max |

## Construction Documents Required (H105.2)

Where a permit is required, construction documents must show:
- Dimensions
- Materials
- Details of construction
- Loads
- Stresses
- Anchors

## Animated/Moving Signs (H108.1)

Signs with moving sections or ornaments must have:
- Fail-safe device to prevent release/falling.
- Fail-safe device must be independent of the operating mechanism.
- Must support the full dead weight of the moving section when mechanism releases.
- Maximum shift of center of gravity: 15 inches.
