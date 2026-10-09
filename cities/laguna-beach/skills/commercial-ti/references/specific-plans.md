# Laguna Beach — Specific Plans and Overlay Districts for Commercial TI

**Authority:** LBMC **Chapter 25.40** (Downtown Specific Plan). LBMC **Chapter 25.35** (Arch Beach Heights Specific Plan). LBMC Title 25, Chapter 25.20 series (baseline commercial zones). City-administered Three Arch Bay private community process.

Identifying the applicable specific plan or overlay district is a **first-step gate** for any commercial TI. A specific plan may layer development standards, route restrictions, and (in the case of Downtown) Coastal Commission-approved LCP standards on top of baseline zoning; do not assume every plan still supplies separate design guidelines after Ord. 1732.

---

## 1. Downtown Specific Plan (LBMC Ch. 25.40)

**Boundary:** The downtown basin, generally framed by:

- **North/Northwest:** Laguna Canyon Frontage Road
- **South/Southwest:** Pacific Ocean
- **East:** Legion Street
- **North:** Cliff Drive

(This is the Central Business District / "CBD" boundary. Confirm with the GIS layer or the DSP map for parcel-specific edges.)

**Adoption history (verbatim from the DSP cover and amendment table):**

- **Originally adopted by City Council on January 24, 1989** (Ordinance No. 1167)
- Amended October 2, 1990 (Ord. 1204); December 15, 1992 (Ord. 1256); October 20, 1998 (Ord. 1348); March 28, 2000 (Ord. 1367); May 1, 2001 (Ord. 1377); October 2, 2001 (Res. 01.058); January 16, 2007 (Res. 07.004); August 5, 2008 (Ord. 1489); September 2, 2008 (Res. 08.077)
- **Most recent amendment: February 15, 2022 (Resolution 22.013, Ordinance 1667)** — the CCC-certified version that adopted current design guidelines and use-table changes

**Full text of the CCC-certified 2022 DSP** is mirrored at the City source document (not included in this plugin) (9.5 MB).

**Key features:**

- Goals and policies for downtown character preservation
- **Downtown Design Guidelines** — tighter than baseline commercial-zone design requirements (storefront proportions, signage, awnings, colors, lighting, transparency, materials)
- Land use districts within the DSP (varies by block — verify against the DSP map)
- Development standards (height, setback, parking, ground-floor activation)

**Routing implications for commercial TI:**

- If a DSP project matches a current Design Review category, non-residential jurisdiction routes it to the **Planning Commission** under §25.05.040(F). Jurisdiction does not itself create the trigger.
- The former DSP Public Works ADR exclusion at `(B)(3)(a)(vi)` was repealed. City projects now route by current major-CIP `(B)(1)(p)`, de-minimis-CIP `(B)(2)(bb)`, and minor-CIP `(B)(3)(a)(xvii)` categories.
- Sign programs in the DSP are common; verify whether the building has an approved sign program (which may delegate sign approval to the Director).
- Public-realm interface (sidewalk café, encroachment into ROW, outdoor dining) typically triggers a separate revocable encroachment permit (doc ID 18755) coordinated with Public Works.

**Practical commercial-TI flag:** DSP standards and CDP review frequently matter, but Design Review still requires a match to the current closed lists. The DSP boundary intersects prime commercial frontage on Forest Ave, Ocean Ave, North Coast Hwy below Cliff Dr, and Coast Hwy southbound through downtown.

---

## 2. Arch Beach Heights Specific Plan (LBMC Ch. 25.35)

**Boundary:** Arch Beach Heights neighborhood (primarily residential).

**Scope:** Primarily residential, but governs neighborhood commercial scattered within the plan area. Commercial TI in Arch Beach Heights is rare but possible — verify the underlying zoning before defaulting to the SP standards.

**Routing implications:** Apply the current §25.05.040 closed lists and a separate CDP analysis. Ord. 1732 §§34–35 removed the former blanket Design Review trigger and most former §25.35.080 design criteria. The retained standards cover R-1 lot coverage, no roof decks/upper-story roof-height limits, under-building enclosure, screened trash storage, and general garage/carport storage. Do not reintroduce the deleted architectural, lighting, landscaping, or massing criteria as current §25.35.080 standards. The integrated eCode page remains pre-ordinance.

---

## 3. Three Arch Bay (Private Community)

**Status:** Private community with a separate development application process administered via the Three Arch Bay Association (TABA) and the Three Arch Bay Community Services District (TABCSD).

**Process:** TABA + TABCSD comment/consent letter sequencing is required before the city will accept a complete application (handout doc ID 11971). This is in **addition to** the standard city permit process — not in lieu of it.

**Commercial TI:** TAB is overwhelmingly residential; commercial TI is rare. Any commercial TI inside the TAB boundary must include the TABA + TABCSD letters in the submittal package.

---

## 4. Village Entrance / North Coast Highway Corridor

**Status:** Not a formal specific plan, but a frequently-flagged commercial frontage corridor.

**Features:**

- Coastal commercial frontage along North Coast Hwy / Hwy 1
- Heavy intersect with the Coastal Zone (most parcels) and frequently inside the **CCC-appealable area** (within 300 ft inland extent of beach / MHW, or between sea and first public road)
- Many parcels in VHFHSZ
- Many older commercial buildings (50+ years) → Heritage Committee trigger likely
- Caltrans encroachment permit required for any work touching the Hwy 1 ROW

**Routing implications:** Match the current Design Review/Zone Clearance/ADR lists; CDP and CCC-appealability checks remain mandatory; Caltrans encroachment permit may be required.

---

## 5. Baseline Commercial Zones (LBMC Ch. 25.20 series)

The baseline commercial zones in Laguna Beach are:

| Zone | Name | Typical use |
|------|------|-------------|
| **C-1** | Local Business | Local-serving retail and service commercial; baseline commercial zone outside specific plans |
| **CN** | Neighborhood Commercial | Smaller-scale neighborhood-serving commercial |
| **LB** | Laguna Beach | Central business / mixed use (downtown periphery) |
| **CB** | Central Business | Central business / downtown core (when not in DSP) |

Refer to the §25.20 series for permitted/conditional use lists, lot/setback/height/coverage standards, and parking ratios per zone. Use-permit triggers (CUP) vary by zone and use.

---

## 6. Other Overlay Considerations

| Overlay | Effect |
|---------|--------|
| **Coastal Zone** | CDP requirement under Ch. 25.07 (see `coastal-development-permit.md`) |
| **VHFHSZ** | Ch. 14.70 WUI requirements (see `wui-commercial.md`) |
| **Historic Register / 1980-81 Inventory** | Heritage Committee review (see `heritage.md`) |
| **Fuel Modification designation** | Pre-permit fuel modification plans (see `wui-commercial.md` §8) |
| **FEMA flood zone** | Floodplain Development Permit under Ch. 14.78 (typically not commercial-TI-relevant unless the building footprint is altered) |
| **Caltrans frontage (PCH / Laguna Canyon Rd)** | Caltrans encroachment permit (see `submittal-package.md`) |

---

## 7. Required Findings Output

For each commercial TI specific-plan / overlay review, output:

```markdown
**Specific plan / overlay status:**
  - Downtown SP (Ch. 25.40): IN | OUT
  - Arch Beach Heights SP (Ch. 25.35): IN | OUT
  - Three Arch Bay: IN | OUT (if IN — TABA + TABCSD letters required, doc ID 11971)
  - Village Entrance / N. Coast Hwy corridor: IN | OUT
**Baseline zone (if outside SPs):** C-1 | CN | LB | CB | Other (specify)
**CIP route, if City project:** Major DR | De minimis Zone Clearance | Minor ADR | N/A
**Coastal Zone:** IN | OUT
**CCC-appealable area:** YES | NO
**VHFHSZ:** YES | NO
**50+ year historic trigger:** YES | NO
**Caltrans frontage:** YES (encroachment permit required) | NO
```

Cite Ch. 25.40 for the DSP, Ch. 25.35 for Arch Beach Heights, current §25.05.040(B)(1)(p)/(B)(2)(bb)/(B)(3)(a)(xvii) for CIP routing, and the applicable baseline commercial chapter.
