# California Baseline — Deck/Patio

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Deck & Patio Permit Review

This skill covers **state-level** California requirements for residential deck and patio construction, repair, and replacement permits. The primary code is the California Residential Code (CRC), Section R507 (Exterior Decks), with supporting requirements from CRC Chapters 3 and 5.

**What this covers:**
- New deck construction and deck replacement
- Deck repair (structural member replacement, decking replacement)
- Ledger connections to the house (lag bolts, through-bolts, flashing)
- Structural requirements (joists, beams, posts, footings)
- Guardrails and handrails (height, baluster spacing, graspability)
- Stair requirements (rise/run, width, headroom, landings)
- Waterproofing and drainage (elevated decks over habitable space)
- Post-to-beam and post-to-foundation connections
- Lateral bracing and load path
- Material requirements (pressure-treated lumber, decay resistance)
- Permit exemptions (when a permit is NOT required)

**What this does NOT cover:**
- Patio covers / shade structures (see CRC Appendix BF)
- Swimming pool decks (see CBC Chapter 31B)
- Commercial decks or balconies over 3 stories (see CBC structural engineer)
- Electrical work on decks (see electrical permit skill)
- Roof decks on commercial buildings

---

### How to Use This Skill

1. Determine whether the project requires a permit (see Step 1 below)
2. Walk through the Decision Tree Router
3. For each checklist item, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 -- Permit Exemption Check

Before reviewing, determine if a permit is required. Per CRC R105.2, a permit is NOT required when ALL of the following are true:

| Condition | Threshold |
|---|---|
| Deck area | Does not exceed 200 sq ft |
| Height above grade | Not more than 30 inches above grade at any point within 36 inches of the edge |
| Attachment | Not attached to a dwelling or townhouse |
| Egress | Does not serve the exit door required by R318.4 |

If ANY condition is not met, a permit IS required. Repairs that involve cutting structural members, removing load-bearing supports, or changing means of egress also require a permit (CRC R105.2.2).

#### STEP 2 -- What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full new deck permit review** | `deck-structural.md`, `ledger-connections.md`, `guards-handrails.md`, `stairs-requirements.md` |
| **Deck repair / member replacement** | `deck-structural.md`, `ledger-connections.md` (if ledger involved) |
| **Ledger connection question** | `ledger-connections.md` |
| **Guard / handrail question** | `guards-handrails.md` |
| **Stair question** | `stairs-requirements.md` |
| **Waterproofing / drainage question** | `waterproofing-drainage.md` |
| **Material / decay resistance question** | `deck-structural.md` |

#### STEP 3 -- Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Permit Exemption** | Verify project does not qualify for exemption per CRC R105.2. If exempt, no further review needed. If deck exceeds 200 sq ft, is more than 30" above grade, is attached to dwelling, or serves an egress door, permit IS required. | CRC R105.2 | N/A |
| 2 | **Footings & Foundations** | Footings required for all decks except: (a) joists directly on grade over entire length, or (b) freestanding decks <=200 sq ft with joists on precast pier blocks at grade, walking surface <=20" above grade. Min footing depth 12" below undisturbed ground. Footing size per Table R507.3.1 based on tributary area and soil bearing capacity. Frost protection required for decks attached to frost-protected structures. | CRC R507.3, R507.3.1, R507.3.2, R507.3.3 | `deck-structural.md` |
| 3 | **Posts** | Post size per Table R507.4 based on species, tributary area, and height. Max post height 14 ft for single-level decks. Post-to-footing connection: approved connectors or min 12" embedment in soil or concrete pier. 4x4 posts supporting guard loads shall NOT be notched at guard connection. | CRC R507.4, R507.4.1, R507.10.2 | `deck-structural.md` |
| 4 | **Beams** | Beam spans per Tables R507.5(1) through R507.5(4) based on joist span, live load, and species. Beam plies fastened with two rows of 10d nails at 16" OC. Beam bearing: min 1-1/2" on wood/metal, min 3" on concrete/masonry. Beam cantilever limited to 1/4 of adjacent beam span. Post-to-beam connection per Figures R507.5.2(1) and R507.5.2(2). | CRC R507.5, R507.5.1, R507.5.2 | `deck-structural.md` |
| 5 | **Joists** | Joist spans per Table R507.6 based on species, size, spacing, and load. Max cantilever per Table R507.6. Joist bearing: min 1-1/2" on wood/metal, min 3" on concrete/masonry. Lateral restraint at joist ends required (hangers, blocking, or rim joist). Rim joist to joist: min three 10d nails or three No. 10 x 3" screws. | CRC R507.6, R507.6.1, R507.6.2 | `deck-structural.md` |
| 6 | **Decking** | Max joist spacing per Table R507.7 based on decking thickness and orientation. 1-1/4" wood perpendicular: 16" max (multi-span). 2" wood perpendicular: 24" max. Diagonal decking reduces max spans. Each board attached with min two 8d deformed shank nails or two No. 8 screws per support. Plastic composite decking per R507.2.2 with labeling, flame spread <=200, and decay resistance. | CRC R507.7, R507.2.2 | `deck-structural.md` |
| 7 | **Ledger Connection** | Ledger min 2x8 nominal, No. 2 grade or better, pressure-treated or naturally durable. Lag screw or bolt spacing per Table R507.9.1.3(1). Lag screws: 1/2" diameter, pre-drilled 1/2" through ledger, 5/16"-3/8" through band joist. Band joist: min 2" nominal solid-sawn SPF or better, or min 1" engineered rim board. Bolt placement per Table R507.9.1.3(2): top edge 2", bottom edge 3/4", ends 2", row spacing 1-5/8" to 5". Ledger shall NOT bear on stone or masonry veneer. Ledger shall NOT support concentrated loads from beams. | CRC R507.9, R507.9.1, Table R507.9.1.3(1), Table R507.9.1.3(2) | `ledger-connections.md` |
| 8 | **Ledger Flashing** | Flashing installed above ledger, extending min 2" vertically above ledger. Horizontal extension: min 4" beyond ledger face OR to ledger face plus 1/4" down. Water-resistive barrier lapped over vertical leg by min 2". Existing walls without WRB: install WRB behind ledger and flashing with self-adhered counterflashing. Exterior wall coverings terminated above deck surface. Flashing not required if ledger spaced 1/4" from wall for drainage/ventilation. | CRC R507.9.1.5, R507.9.1.6, R507.9.1.7, R507.9.1.8 | `ledger-connections.md` |
| 9 | **Lateral Load Connection** | Lateral loads must transfer to ground or supporting structure. Hold-down tension devices: min 2 per deck within 24" of each end, each with ASD capacity >= 1,500 lb (per Figure R507.9.2(1)). Alternate: min 4 devices, each >= 750 lb ASD capacity (per Figure R507.9.2(2)). Attachment NOT permitted by toenails or nails subject to withdrawal (CRC R318.5). | CRC R507.9.2, R507.8, R318.5 | `ledger-connections.md` |
| 10 | **Guards (Guardrails)** | Required where walking surface is >30" above grade (measured within 36" horizontally of open edge). Height: min 42" measured vertically from walking surface. On open stair sides: min 34" from nosing line, or 34"-38" if top rail serves as handrail. Baluster spacing: no opening allows passage of 4" sphere. Stair triangle exception: 6" sphere at triangular opening formed by riser, tread, and bottom rail. Floor framing supporting guards per R502.11. | CRC R321.1.1, R321.1.2, R321.1.3, R507.10, R502.11 | `guards-handrails.md` |
| 11 | **Handrails** | Required on at least one side of stairs with 4 or more risers. Height: 34"-38" measured from nosing line. Grip size Type I: circular 1-1/4" to 2" OD, or non-circular perimeter 4" to 6-1/4" with max cross-section 2-1/4". Type II: perimeter >6-1/4" with graspable finger recess. Continuous for full flight length. Returned to wall, guard, or walking surface. Wall clearance: min 1-1/2". Max projection into stair: 4-1/2". Plastic composite handrails per R507.2.2. | CRC R320.1-R320.7, R318.7.8 | `guards-handrails.md` |
| 12 | **Stairs** | Riser height: max 7-3/4". Tread depth: min 10". Rise/run uniformity: max 3/8" variation within a flight. Stair width: min 36" clear above handrail, min 31-1/2" at/below one handrail, min 27" between two handrails. Headroom: min 6'-8". Max vertical rise per flight: 12'-7". Nosing: 3/4" to 1-1/4" projection. Open risers >30" above grade: no 4" sphere passage. Landing at top and bottom: min 36" depth in direction of travel. Bottom landing for exterior stairs to grade with <=3 risers: min 36" wide (if not serving egress door). Walking surface slope: max 2%. | CRC R318.7.1-R318.7.7 | `stairs-requirements.md` |
| 13 | **Decay Protection** | All wood structural members exposed to weather without adequate roof/eave protection must be naturally durable or pressure-treated (CRC R304.1 Item 8). Ground contact wood: pressure-treated per AWPA U1 for ground contact use (R304.1.2). Field-cut ends treated per AWPA M4 (R304.1.1). Quality mark required showing treating plant, preservative type, retention, end use, standard, and inspection agency (R304.2). Sawn lumber for joists/beams/posts: No. 2 grade or better (R507.2.1). | CRC R304.1, R304.1.1, R304.1.2, R304.2, R507.2.1 | `deck-structural.md` |
| 14 | **Fasteners & Connectors** | All metal fasteners for decks per Table R507.2.3 and R304.3. Nails: hot-dipped galvanized per ASTM A153 Class D, or stainless steel, silicon bronze, copper. Bolts: hot-dipped galvanized per ASTM A153 Class C/D, or mechanically galvanized per ASTM B695 Class 55, or stainless steel. Metal connectors: ASTM A653 type G185 zinc-coated or post hot-dipped per ASTM A123. Within 300 ft of salt water: stainless steel required. Through-bolt holes drilled 1/32" to 1/16" larger than bolt diameter. | CRC R507.2.3, R304.3, Table R507.2.3 | `deck-structural.md` |
| 15 | **Waterproofing (Elevated Decks)** | Where decks are over habitable space: wood structural members supporting moisture-permeable floors exposed to weather must be protected or separated by impervious moisture barrier with positive drainage (R304.1 Item 6). Enclosed framing in exterior balconies exposed to rain/snow: net-free ventilation area >= 1/150 of each separate space (R304.1.3). Flashing: corrosion-resistant metal >= 0.019" or approved non-metallic, compatible with substrate (R507.2.4). | CRC R304.1, R304.1.3, R507.2.4 | `waterproofing-drainage.md` |
| 16 | **Attachment to Structure** | Exterior decks, balconies, stairs, and landings must be positively anchored to primary structure for vertical AND lateral forces, or designed as self-supporting. Attachment NOT by toenails or nails subject to withdrawal. Where positive connection cannot be verified during inspection, deck must be self-supporting. Cantilevered framing connections must resist uplift from full live load on cantilever. | CRC R318.5, R507.8 | `ledger-connections.md` |
| 17 | **Contractor Licensing** | C-5 (Framing and Rough Carpentry), B (General Building), or A (General Engineering for larger projects) license required. Workers' compensation insurance required. | B&P Code 7028 | N/A |

#### STEP 4 -- Output Format

For each checklist item, produce:

```
## [#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation of what was verified or what failed]
```

- **PASS** -- Requirement met per submitted information
- **FAIL** -- Requirement not met; cite code section and explain the deficiency
- **FLAG** -- Cannot determine from submitted data; explain what additional info is needed
- **N/A** -- Does not apply to this project (e.g., ledger checks on freestanding deck)

---

### Quick-Reference Tables

#### Permit Exemption Summary (CRC R105.2)

| Condition | Must Meet ALL |
|---|---|
| Area | <= 200 sq ft |
| Height | <= 30" above grade at any point within 36" of edge |
| Attachment | NOT attached to dwelling |
| Egress | Does NOT serve required exit door |

#### Guard Requirements

| Location | Min Height | Opening Limit |
|---|---|---|
| Deck/balcony/porch (>30" above grade) | 42" | 4" sphere |
| Open side of stairs | 34" from nosing line | 4-3/8" sphere |
| Stair triangle (riser/tread/rail) | -- | 6" sphere |

#### Stair Dimensional Requirements (CRC R318.7)

| Dimension | Requirement |
|---|---|
| Max riser height | 7-3/4" |
| Min tread depth | 10" |
| Max rise/run variation in flight | 3/8" |
| Min width above handrail | 36" |
| Min width at/below one handrail | 31-1/2" |
| Min headroom | 6'-8" |
| Max vertical rise per flight | 12'-7" |
| Nosing projection | 3/4" to 1-1/4" |
| Landing depth (direction of travel) | 36" min |

#### Handrail Requirements (CRC R320)

| Dimension | Requirement |
|---|---|
| Height (from nosing line) | 34" to 38" |
| Type I circular OD | 1-1/4" to 2" |
| Type I non-circular perimeter | 4" to 6-1/4" |
| Wall clearance | Min 1-1/2" |
| Max projection into stair | 4-1/2" |

#### Deck Joist Maximum Spans (40 psf, No. 2 DF-L/HF/SPF, Common Sizes)

| Joist Size | 12" OC | 16" OC | 24" OC |
|---|---|---|---|
| 2x6 | 9'-6" | 8'-4" | 6'-10" |
| 2x8 | 12'-6" | 11'-1" | 9'-1" |
| 2x10 | 15'-8" | 13'-7" | 11'-1" |
| 2x12 | 18'-0" | 15'-9" | 12'-10" |

#### Ledger Fastener Spacing (40 psf, 1/2" Lag Screw, 1/2" Max Sheathing)

| Joist Span | On-Center Spacing |
|---|---|
| 6 ft | 30" |
| 8 ft | 23" |
| 10 ft | 18" |
| 12 ft | 15" |
| 14 ft | 13" |
| 16 ft | 11" |
| 18 ft | 10" |

#### Deck Post Maximum Height (40 psf, 4x4, DF-L/HF/SPF)

| Tributary Area (sq ft) | Max Height |
|---|---|
| 20 | 14'-0" |
| 40 | 13'-6" |
| 60 | 10'-10" |
| 80 | 9'-3" |
| 100 | 8'-0" |
| 120 | 7'-0" |

#### Decking Attachment & Max Joist Spacing (Table R507.7)

| Decking Type & Orientation | Single Span | Multiple Span |
|---|---|---|
| 1-1/4" wood, perpendicular | 12" OC | 16" OC |
| 2" wood, perpendicular | 24" OC | 24" OC |
| 1-1/4" wood, diagonal (max 45 deg) | 8" OC | 12" OC |
| 2" wood, diagonal (max 45 deg) | 18" OC | 24" OC |

---

### Key Principles

1. **Ledger connections are the #1 failure point.** The connection between a deck ledger and the house band joist is the most common point of catastrophic deck collapse. Lag screw or through-bolt spacing must comply with Table R507.9.1.3(1). Flashing above the ledger is mandatory. The ledger must never bear on masonry veneer.
2. **Guards are life-safety.** Any walking surface more than 30 inches above grade requires a guard at least 42 inches high with no opening that allows passage of a 4-inch sphere. This is non-negotiable.
3. **Pressure treatment is required for weather-exposed wood.** All deck structural members exposed to weather without roof protection must be naturally durable or pressure-preservative-treated per AWPA U1 (CRC R304.1 Item 8). Ground-contact members require ground-contact-rated treatment (R304.1.2).
4. **Lateral bracing prevents collapse.** Decks must transfer lateral loads to the ground. Hold-down tension devices are required at the ledger connection -- minimum two devices with 1,500 lb ASD capacity each within 24 inches of each end of the deck.
5. **Footings go below frost line.** Deck footings must extend at least 12 inches below undisturbed ground. Where attached to a frost-protected structure, footings must extend below the frost line or use other approved frost protection.
6. **The 200 sq ft / 30 inch exemption has limits.** A permit is not required only if the deck is under 200 sq ft, under 30 inches above grade, not attached to the dwelling, and does not serve an egress door. If ANY condition fails, a permit is required.
7. **Stair uniformity prevents falls.** Within any flight of stairs, the greatest riser height and tread depth cannot vary from the smallest by more than 3/8 inch. This is a critical safety dimension.
8. **Fasteners must resist corrosion.** All fasteners for decks must be hot-dipped galvanized, stainless steel, silicon bronze, or copper. Within 300 feet of salt water, stainless steel is required.
