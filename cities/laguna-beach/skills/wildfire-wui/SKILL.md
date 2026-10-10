---
name: wildfire-wui
description: "Wildfire and wildland-urban interface (WUI) construction rules in Laguna Beach, CA: Fire Hazard Severity Zones, ignition-resistant roofs, eaves, vents, walls, windows, decks, and defensible space under the California WUI Code as amended by LBMC Ch. 14.70. Laguna Beach applies this overlay citywide. Use when the user asks about WUI, fire zones, Class A roofs, ember-resistant vents, or fire-resistant materials in Laguna Beach."
metadata:
  version: "2.0"
  source: "California Wildland-Urban Interface Code (Title 24, Part 7), 2025 Edition — effective January 1, 2026. CBC Chapter 7A and CRC R337 both redirect to Part 7 for all construction requirements.; LBMC Ch. 14.70, §14.50.120"
  authority: "California Building Standards Commission / Office of the State Fire Marshal and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Wildfire / WUI Overlay

Laguna Beach applies this overlay to the whole city. Treat every parcel as inside a Fire Hazard Severity Zone, say "assumed FHSZ based on citywide coverage; confirm the parcel on the City's adopted 2025 LRA map", and confirm on that map before telling anyone a parcel is outside the zone. LBMC Ch. 14.70 amends the WUI Code (scope at LBMC §14.70.015, with a building-official minor-repair exception). Class A roofing applies to any building in the City under LBMC §14.50.120.

The permit skills in this plugin link here. Use their Laguna Beach rules for the scope-specific amendments, and this skill for the state WUI baseline.

---

## City Info

| | |
|---|---|
| Permit system | Tyler EnerGov Civic Access |
| Permit portal | https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home |
| Municipal code | https://ecode360.com/LA4953 |
| Fire agency | Laguna Beach Fire |
| Code edition | Title 14 Building & Housing · 2025 CBC/CRC |
| Code prefix | LBMC |

---

## Laguna Beach WUI amendments by scope

The Laguna-specific WUI rules live with the permit they affect:

- `../commercial-ti/references/wui-commercial.md`
- `../deck-patio-repair/references/city-wui-decking.md`
- `../reroof/references/city-wui-roofing.md`
- `../residential-remodel/references/city-vhfhsz-wui.md`
- `../siding-replacement/references/city-wui-exterior-walls.md`
- `../single-family-residential/references/fire-wui-local-amendments.md`
- `../window-replacement/references/city-wui-glazing.md`

---

## California WUI Baseline

**Primary Authority:** California Wildland-Urban Interface Code (CWUIC), Title 24, Part 7 (2025 Edition, effective January 1, 2026). CBC Chapter 7A and CRC Section R337 are stub references that redirect here — all substantive requirements are in Part 7.

**What this covers:** State-minimum ignition-resistant construction requirements for buildings and structures located in a Wildland-Urban Interface area or Fire Hazard Severity Zone. Also covers defensible space, vegetation management, site access, and water supply.

**What this does NOT cover:** City/county WUI ordinances that may be more stringent; fire sprinkler requirements (governed by CFC / CBC Chapter 9); Title 24 Part 6 energy compliance; grading and geotechnical issues.

---

### How to Use This Skill

Follow the 3-step decision tree. Each step identifies which reference files to load. Load only what you need — most questions require 1–2 reference files.

---

### STEP 1 — Determine If WUI/FHSZ Rules Apply

> **Always start here.** If the project is not in a FHSZ or WUI area, no requirements from this skill apply.

| Trigger Condition | Zone Type | Load |
|---|---|---|
| State-designated SRA land (forests, wildlands — CAL FIRE jurisdiction) | SRA | `references/fhsz-applicability.md` |
| LRA land with Very High FHSZ designation (city or county adopted) | LRA VHFHSZ | `references/fhsz-applicability.md` |
| LRA land with High FHSZ designation (city or county adopted) | LRA HFHSZ | `references/fhsz-applicability.md` |
| Enforcing agency has locally designated WUI area not mapped as FHSZ | Local WUI | `references/fhsz-applicability.md` |
| Unsure — parcel in foothill/canyon/rural area, need to verify | Unknown | `references/fhsz-applicability.md` (check OSFM map) |

> **Shortcut:** If the jurisdiction has confirmed in writing that the parcel is in VHFHSZ or HFHSZ, skip to Step 2.

---

### STEP 2 — Identify Project Type and Scope

What work is being permitted?

| Project Type | Primary Reference | Also Load |
|---|---|---|
| **New SFR or duplex** | `references/roof-eaves-vents.md` + `references/walls-windows-doors-decks.md` | `references/site-access-defensible-space.md` |
| **New ADU (attached or detached)** | `references/roof-eaves-vents.md` + `references/walls-windows-doors-decks.md` | `references/fhsz-applicability.md` (ADU scope note) |
| **Addition to existing SFR** | `references/roof-eaves-vents.md` + `references/walls-windows-doors-decks.md` | — |
| **Reroof (≥50% in 12 months, or all-new)** | `references/roof-eaves-vents.md` | — |
| **Window / door replacement** | `references/walls-windows-doors-decks.md` | — |
| **New deck, balcony, or stair** | `references/walls-windows-doors-decks.md` | — |
| **New accessory building (garage, workshop, ADU prep)** | `references/roof-eaves-vents.md` + `references/walls-windows-doors-decks.md` | `references/fhsz-applicability.md` (accessory thresholds) |
| **Patio cover, trellis, arbor, gazebo** | `references/walls-windows-doors-decks.md` (§ 504.11) | — |
| **New subdivision or land division** | `references/site-access-defensible-space.md` | `references/fhsz-applicability.md` |
| **Landscape or vegetation plan only** | `references/site-access-defensible-space.md` | — |

---

### STEP 3 — Identify the Component or Issue

Once you have the project type, go directly to the component:

#### Building Envelope Components

| Component Question | Load |
|---|---|
| Roof assembly, roof covering, Class A requirement | `references/roof-eaves-vents.md` |
| Roof valleys, cap sheet, underlayment | `references/roof-eaves-vents.md` |
| Eaves — enclosed soffit, open eave, fascia | `references/roof-eaves-vents.md` |
| Gutters and downspouts | `references/roof-eaves-vents.md` |
| Attic, crawl space, ridge, gable-end or under-eave vents | `references/roof-eaves-vents.md` |
| Skylight (operable or fixed) | `references/roof-eaves-vents.md` |
| Spark arrestor on chimney or stovepipe | `references/roof-eaves-vents.md` |
| Exterior wall assembly or cladding / siding | `references/walls-windows-doors-decks.md` |
| Underfloor enclosure, crawl space walls | `references/walls-windows-doors-decks.md` |
| Projections (cantilevered floors, balconies) | `references/walls-windows-doors-decks.md` |
| Decks, porches, balconies, stairs — walking surface | `references/walls-windows-doors-decks.md` |
| Deck-to-wall flashing | `references/walls-windows-doors-decks.md` |
| Exterior windows, glazed doors, window walls | `references/walls-windows-doors-decks.md` |
| Exterior entry doors, garage doors | `references/walls-windows-doors-decks.md` |
| Garage door battery backup / ember gap | `references/walls-windows-doors-decks.md` |

#### Site / Civil Components

| Component Question | Load |
|---|---|
| Defensible space zones (30 ft and 100 ft) | `references/site-access-defensible-space.md` |
| Vegetation management / fuel modification | `references/site-access-defensible-space.md` |
| Landscape / planting plan for WUI | `references/site-access-defensible-space.md` |
| Building setbacks from property lines / roads | `references/site-access-defensible-space.md` |
| Access road width, grade, turnaround, dead-end limits | `references/site-access-defensible-space.md` |
| Fire apparatus access, water supply, hydrant spacing | `references/site-access-defensible-space.md` |
| Firewood or combustible material storage | `references/site-access-defensible-space.md` |
| LP-gas tank location and clearance | `references/site-access-defensible-space.md` |
| Ridgeline protection, strategic ridgelines | `references/site-access-defensible-space.md` |
| Fire protection plan requirement | `references/site-access-defensible-space.md` |

---

### Quick-Reference Thresholds

> These numbers appear in nearly every WUI plan check. Memorize them.

| Requirement | Standard | Code Citation |
|---|---|---|
| Roof classification | Class A minimum (ASTM E108 / UL 790) | CWUIC § 504.2 |
| Vent mesh — performance tested | OSFM-listed WUI vent (ASTM E2886) | CWUIC § 504.10.1 |
| Vent mesh — off-ridge/ridge slope vents | 1/16″ min, 1/8″ max, noncombustible | CWUIC § 504.10.2 |
| Exterior glazing | Multilayered with ≥1 tempered pane (CBC § 2406) | CWUIC § 504.8 |
| Gable-end/dormer vent setback | ≥10 ft from lot line | CWUIC § 504.10.3 |
| Deck-to-wall flashing | 6″ metal flashing, vertical | CWUIC § 504.7.3.1 |
| Wall-to-ground/deck/roof flashing | 6″ metal flashing, vertical | CWUIC § 504.5.1 |
| Ignition-resistant material flame spread | ≤25 FSI (ASTM E84 / UL 723, 30-min test) | CWUIC § 503.2.4.1 |
| Garage door ember gap | ≤1/8″ gaps at all edges | CWUIC § 504.9.2 |
| Garage door opener | Battery backup required | CWUIC § 504.9.1 |
| Gutters | Noncombustible + debris-prevention cover | CWUIC § 504.4 |
| Reroof trigger | ≥50% replaced in 12 months → full Class A | CWUIC § 507.1 |
| Accessory bldg — full ignition-resistant | >120 sq ft and <50 ft from habitable bldg | CWUIC § 504.11.3 |
| Accessory bldg — exempt | ≥50 ft from applicable buildings AND Group U | CWUIC § 501.1 Exception 1 |
| Defensible space Zone 1 | 30 ft — non-fire-smart veg cleared/managed | CWUIC § 603.3.1 |
| Defensible space Zone 2 | 100 ft — fuel reduction maintained | CWUIC § 603.3.1; PRC § 4291 |
| Building setback from property line / road | 30 ft minimum | CWUIC § 608.2 |
| Firewood storage setback | 30 ft from structure (or fire-resistant cover) | CWUIC § 607.1 |
| Spark arrestor mesh | 12-gauge, ≤1/2″ openings, net free area ≥4× flue outlet | CWUIC § 605.1 |

---

### Material Qualification Paths

When a plan shows a specific product, verify it qualifies by one of these paths:

| Material Type | Qualification Route |
|---|---|
| Noncombustible | Tested per ASTM E136 or ASTM E2652 | CWUIC § 503.2.1 |
| Fire-retardant-treated wood (exterior) | Listed per CBC § 2303.2, labeled for exterior use | CWUIC § 503.2.2 |
| FRTW roof shingles/shakes | OSFM-listed, Class A assembly per CBC § 1505.6 | CWUIC § 503.2.3 |
| Other ignition-resistant material | FSI ≤25, flame front ≤10'6″, 30-min ASTM E84 extended test | CWUIC § 503.2.4 |
| WUI vents | OSFM-listed OR ASTM E2886-tested, no sustained flaming | CWUIC § 504.10.1 |
| Deck material | ASTM E2632 + E2726 (Class A size brand) | CWUIC § 504.7.3.3 |

> **Paint / surface treatments do NOT qualify** as ignition-resistant materials. § 503.2.5.

---

### Code Hierarchy Quick Guide

```
Title 24, Part 7 — California Wildland-Urban Interface Code (2025)
  ├── Chapter 2 — Definitions (FHSZ, ignition-resistant material, WUI area, etc.)
  ├── Chapter 3 — WUI Area Designations (OSFM mapping)
  ├── Chapter 4 — Access Roads & Water Supply (§§ 401–404)
  ├── Chapter 5 — Building Construction Requirements (§§ 501–507)
  │     ├── § 503 — Ignition-Resistant Material Standards
  │     ├── § 504 — Ignition-Resistant Construction (all components)
  │     └── § 507 — Reroof / Replacement Trigger
  ├── Chapter 6 — Fire Protection / Defensible Space (§§ 601–612)
  └── Referenced Standards — SFM 12-7A-1 through 12-7A-4

CBC (Title 24, Part 2) Chapter 7A → redirects to Part 7
CRC (Title 24, Part 2.5) Section R337 → redirects to Part 7
```

---

## References

Load these on demand. Paths are relative to this file.

**California rules**

- `references/fhsz-applicability.md` — FHSZ / WUI Applicability
- `references/roof-eaves-vents.md` — Roof Assembly, Eaves, Gutters, Vents & Spark Arrestors
- `references/site-access-defensible-space.md` — Site Requirements — Defensible Space, Vegetation, Access & Water
- `references/walls-windows-doors-decks.md` — Exterior Walls, Underfloor, Projections, Decks, Windows & Doors

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
