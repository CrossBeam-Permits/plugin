# California Baseline — Sign

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Sign Permit Review

This skill covers **state-level** California requirements for commercial, industrial, and institutional sign permits. It addresses building code (structural, materials, fire) and electrical code (illuminated signs, wiring, disconnects) requirements.

**What this covers:**
- Sign types: wall-mounted, freestanding/monument, projecting, roof, marquee, pole, awning, channel letter, digital/electronic
- Structural design: wind loads, seismic, attachment, foundations
- Electrical requirements for illuminated signs (CEC Article 600)
- Height, projection, and clearance limits (state code defaults)
- Materials and fire resistance by sign type
- Electrical disconnects, branch circuits, GFCI
- Enclosures, grounding, bonding
- Temporary signs, banners, portable signs
- Sign lighting (internal vs. external illumination)
- Glass panel requirements
- Animated/moving sign fail-safe devices

**What this does NOT cover:**
- Local zoning sign regulations (size limits, setbacks, sign area per frontage, aesthetic standards) — see city overlay skill
- Caltrans/MUTCD traffic sign requirements
- ADA/accessibility signage (see CBC Chapter 11B)
- Billboard-specific state regulations (Outdoor Advertising Act)
- Historic district sign restrictions

---

### How to Use This Skill

1. Determine the **sign type** (wall, projecting, ground/monument, pole, roof, marquee, channel letter, digital)
2. Determine whether the sign is **illuminated** (internally, externally, or non-illuminated)
3. Walk through the Decision Tree Router below
4. For each checklist item, load the referenced file from `/` as needed
5. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 — Determine Sign Type

| Sign Type | Code Sections | Key Requirements |
|---|---|---|
| Wall sign (flat against building) | H111, CEC 600 (if illuminated) | Material >40 sq ft noncombustible, attachment, no parapet support |
| Projecting sign (extends from wall at angle) | H112, CEC 600 (if illuminated) | All noncombustible, no nails/staples, projection/thickness limits |
| Ground/monument sign (freestanding on ground) | H109, CEC 600 (if illuminated) | Height limits, 3 ft bottom clearance, foundation |
| Pole sign (supported by pole in ground) | H109, CEC 600 (if illuminated) | Same as ground sign plus pole structural |
| Roof sign (on or above roof) | H110, CEC 600 (if illuminated) | All noncombustible, 6 ft roof clearance, height limits by type |
| Marquee sign (on permanent canopy) | H113, CBC 3106, CEC 600 | Within marquee perimeter, height limits |
| Channel letters (individual letters on building) | H111 (wall) + CEC 600 | Per-letter or raceway-mounted, electrical for illuminated |
| Awning sign (on retractable/fixed awning) | CBC 3105, CEC 600 | Awning material compliance, CPAI-84 or NFPA 701 |
| Digital/electronic (EMC) | CEC 600, local zoning | Full electrical, brightness/dimming per local code |
| Portable/temporary | H114, CBC 3103 | Stability, applicable type requirements |

#### STEP 2 — What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full permit review** (form data in, pass/fail out) | `sign-types-clearances.md`, `sign-structural.md`, `sign-electrical.md` (if illuminated), `sign-materials-fire.md` |
| **Sign type / clearance question only** | `sign-types-clearances.md` |
| **Structural / wind / attachment question** | `sign-structural.md` |
| **Electrical / disconnect / wiring question** | `sign-electrical.md` |
| **Material / fire resistance question** | `sign-materials-fire.md` |

#### STEP 3 — Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Sign Type Classification** | Classify the sign as wall, projecting, ground/monument, pole, roof, marquee, channel letter, awning, digital/electronic, or portable/temporary. The type determines which CBC Appendix H sections apply and material/height requirements. | H102.1 | `sign-types-clearances.md` |
| 2 | **Permit Exemption Check** | Verify whether the sign requires a permit. Exempt: painted nonilluminated signs, temporary sale/rent signs, transportation authority signs, projecting signs <=2.5 sq ft, and changing moveable parts of an approved changeable sign. | H101.2 | `sign-types-clearances.md` |
| 3 | **Location Restrictions** | Sign must not obstruct exit signs, fire escapes, means of egress doors/windows, or required ventilation openings. Must not be attached to a fire escape. Must not prevent free passage on a roof. Must not confuse or interfere with traffic signs/signals. | H101.1, H103.1 | `sign-types-clearances.md` |
| 4 | **Material Compliance** | Verify materials comply with sign type requirements. Wall signs >40 sq ft: noncombustible. Projecting, roof, marquee signs: entirely noncombustible (with exceptions for letters/trim per H107.1 and internally illuminated facings per H106.1.1). Plastics: must pass ASTM D635 (<=2.5 in/min burn rate). Electric sign plastic faces: max 200 sq ft each. | H107, H110.1, H111.1, H112.1, H113.1 | `sign-materials-fire.md` |
| 5 | **Height and Projection Limits** | Verify sign does not exceed height limits for its type. Ground signs: 35 ft (combustible) / 100 ft (noncombustible). Roof signs: 24 ft (solid), 75/40 ft (open by construction type), 50/35 ft (closed). Projecting signs: must not exceed roof/cornice height (limited exception for 18" perpendicular signs). Marquee signs: max 6 ft above, 1 ft below, 8 ft total vertical. | H109.1, H110.3-H110.5, H112.4, H113.3-H113.4 | `sign-types-clearances.md` |
| 6 | **Clearance Requirements** | Ground signs: min 3 ft bottom clearance above grade. Roof signs: min 6 ft between roof and lowest sign part, min 5 ft between supports. Vehicle areas: min 14 ft above grade (CEC 600.9). Pedestrian clearances: per local code (state code sets vehicle height only). | H109.2, H110.1, CEC 600.9(A) | `sign-types-clearances.md` |
| 7 | **Structural — Wind Load Design** | Signs must be designed for wind loads per CBC Chapter 16 / ASCE 7. Verify wind speed for project location (typically 110-115 mph V for Risk Category II in CA). Freestanding signs: ASCE 7 Section 29.3. Attached signs: components and cladding per Chapter 30. Construction documents must show loads, stresses, and anchors. | H105.3, CBC 1609, ASCE 7 Ch 29 | `sign-structural.md` |
| 8 | **Structural — Seismic Design** | Signs designed for wind are generally deemed adequate for seismic (H105.4), but ASCE 7 Chapter 13 (nonstructural components) and Chapter 15 (nonbuilding structures) may apply. In Seismic Design Categories D-F (most of CA), verify seismic analysis for large or heavy signs. | H105.4, CBC 1613, ASCE 7 Ch 13/15 | `sign-structural.md` |
| 9 | **Structural — Attachment** | Attachment to masonry/concrete/steel: metal anchors, bolts, or expansion screws of sufficient size. Wall signs: min 3/8" diameter, min 5" embedment. No wood block anchorage (except on wood buildings). Projecting signs: no nails/staples, min 3/8" supports, min 5/8" lag screws, turnbuckles required. No anchorage to unbraced parapets. | H105.6, H111.2, H112.1-H112.3 | `sign-structural.md` |
| 10 | **Structural — Foundation (Freestanding)** | For ground/pole signs: verify foundation design per CBC Chapter 18. Must resist overturning from wind and seismic. Wood in ground contact must be pressure treated. Soil bearing analysis required for large signs. | H109.3, CBC Ch 18 | `sign-structural.md` |
| 11 | **Electrical — Branch Circuit** | Each commercial occupancy must have a dedicated 20A branch circuit at each pedestrian entrance for signs. Neon signs: max 30A branch circuit. All other signs: max 20A. Sign loads are continuous loads (125% sizing). | CEC 600.5 | `sign-electrical.md` |
| 12 | **Electrical — Disconnect** | Each sign must have an externally operable switch or circuit breaker opening all ungrounded conductors, controlling no other load. Must be accessible. Located at point of entry to sign, within sight of sign, within sight of controller, or at marked remote location. Switch must be rated for inductive loads or 2x transformer/power supply current. | CEC 600.6 | `sign-electrical.md` |
| 13 | **Electrical — Grounding & Bonding** | All metal equipment must be grounded via equipment grounding conductor. All metal parts bonded together and to transformer/power supply EGC. Metal building parts shall NOT be used for bonding. Bonding conductors: copper min 14 AWG or copper-clad aluminum min 12 AWG. | CEC 600.7 | `sign-electrical.md` |
| 14 | **Electrical — Listing & Labeling** | Electric signs must be listed and labeled (UL 48), with installation instructions, and installed per listing. Field-installed skeleton tubing exempt from listing if installed per CEC. Markings: manufacturer name, input voltage, current rating, visible after installation. | CEC 600.3, 600.4 | `sign-electrical.md` |
| 15 | **Electrical — Enclosure** | Live parts (other than lamps/neon tubing) must be enclosed. Enclosures: metal or listed. Min metal thickness: copper/aluminum 0.020", steel 0.016". Metal parts protected from corrosion. | CEC 600.8 | `sign-electrical.md` |
| 16 | **Electrical — GFCI** | Portable/mobile signs in wet or damp locations: listed GFCI protection required, integral to attachment plug or within 12" of it. Cords: hard-service type with EGC. | CEC 600.10(C)(2) | `sign-electrical.md` |
| 17 | **Electrical — Transformers/Power Supplies** | Must be listed, accessible, securely fastened. Neon transformers: secondary-circuit ground-fault protection required (with exceptions). Max secondary voltage 15,000V. Max secondary current 300 mA. Working space: min 3 ft x 3 ft x 3 ft. Secondary outputs NOT in parallel or series. | CEC 600.21-600.24 | `sign-electrical.md` |
| 18 | **Combustible Material Proximity** | Sign must not subject adjacent combustible materials to temperatures >194 deg F. Min 2" spacing between wood/combustibles and incandescent/HID lamps. Internally illuminated signs: 2" min clearance from wiring to facing. Illumination by electrical means only — no open flames. | CEC 600.9(C), H106.1, H106.1.1 | `sign-materials-fire.md` |
| 19 | **Wet Location Compliance** | Exterior signs (wet location): weatherproof or listed watertight. Drain holes: 1/4" to 1/2", at every low point, no obstructions. Transformers/power supplies: weatherproof or outdoor type protected in sign body. | CEC 600.9(D), 600.21(C) | `sign-electrical.md` |
| 20 | **Animated/Moving Devices** | Signs with moving sections/ornaments: fail-safe device required to prevent release. Must support full dead weight. Max center-of-gravity shift: 15 inches. Fail-safe independent of operating mechanism. | H108.1 | `sign-structural.md` |
| 21 | **Sign Identification** | Outdoor advertising display signs requiring permits must be marked with erector/maintainer name and permit number (or approved ID) on front. | H104.1 | `sign-types-clearances.md` |
| 22 | **Construction Documents** | Plans must show dimensions, materials, construction details, loads, stresses, and anchors. For illuminated signs: electrical plan showing branch circuit, disconnect location, transformer/power supply, and wiring methods. | H105.2, CEC 600.5(D) | `sign-structural.md` |
| 23 | **Contractor Licensing** | C-45 (Electrical Sign) license required for installing, altering, or repairing all types of signs. C-10 (Electrical) for electrical wiring to sign. B (General Building) may perform structural work. | B&P Code 7028 | N/A |

#### STEP 4 — Output Format

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
- **N/A** -- Does not apply to this project (e.g., foundation check for a wall sign, GFCI for a permanent hardwired sign)

---

### Quick-Reference Tables

#### Material Requirements by Sign Type

| Sign Type | Material Required | Combustible Allowed? | Code Section |
|---|---|---|---|
| Wall sign <=40 sq ft | No restriction | Yes | H111.1 |
| Wall sign >40 sq ft | Metal or noncombustible | Only for letters/trim (H107.1) | H111.1 |
| Projecting sign | Entirely noncombustible | Only for letters/trim (H107.1) | H112.1 |
| Ground sign | No restriction (height varies) | Yes (35 ft max height) | H109.1 |
| Roof sign | Entirely noncombustible | Only for letters/trim (H107.1) | H110.1 |
| Marquee sign | Entirely noncombustible | Only per H106.1.1, H107.1 | H113.1 |

#### Height Limits Summary

| Sign Type | Max Height | Condition | Code Section |
|---|---|---|---|
| Ground sign (combustible frame) | 35 ft | -- | H109.1 |
| Ground sign (noncombustible) | 100 ft | Approval required for greater | H109.1 |
| Roof sign (solid surface) | 24 ft above roof | All construction types | H110.3 |
| Roof sign (open, >=40% open) | 75 ft above roof | Type I/II construction | H110.4 |
| Roof sign (open, >=40% open) | 40 ft above roof | Type III/IV/V construction | H110.4 |
| Roof sign (closed) | 50 ft above roof | Type I/II construction | H110.5 |
| Roof sign (closed) | 35 ft above roof | Type III/IV/V construction | H110.5 |
| Marquee sign | 6 ft above marquee | Max 8 ft total vertical | H113.4 |
| Projecting sign | Roof/cornice height | 18"-wide perpendicular signs may extend 2 ft above | H112.4 |

#### Clearance Requirements Summary

| Location | Minimum Clearance | Code Section |
|---|---|---|
| Ground sign bottom coping to grade | 3 ft | H109.2 |
| Roof sign: roof to lowest sign part | 6 ft | H110.1 |
| Roof sign: between vertical supports | 5 ft | H110.1 |
| Vehicle areas (sign/outline lighting) | 14 ft above grade | CEC 600.9(A) |
| Neon tubing to nearest surface | 1/4 in | CEC 600.41(C) |
| Incandescent/HID lamp to combustibles | 2 in | CEC 600.9(C) |

#### Projection Thickness Limits (Projecting Signs)

| Projection from Wall (ft) | Maximum Sign Thickness (ft) |
|---|---|
| 5 | 2 |
| 4 | 2.5 |
| 3 | 3 |
| 2 | 3.5 |
| 1 | 4 |

#### Plastic Area Limits for Electric Signs

| Display Surface Area | Max Plastic Area | Code Section |
|---|---|---|
| <=200 sq ft | 200 sq ft (full area) | H107.1.2 |
| >200 sq ft | 200 + 50% of (total - 200), max 1,100 sq ft | H107.1.3 |

#### Electrical Branch Circuit Requirements

| Sign Type | Max Branch Circuit | Load Classification |
|---|---|---|
| Neon tubing signs | 30A | Continuous |
| All other signs | 20A | Continuous |
| Required sign outlet per entrance | Dedicated 20A | -- |

#### Glass Panel Requirements

| Max Dimension (in) | Max Area (sq in) | Min Thickness | Glass Type |
|---|---|---|---|
| 30 | 500 | 1/8" | Plain, plate, or wired |
| 45 | 700 | 3/16" | Plain, plate, or wired |
| 144 | 3,600 | 1/4" | Plain, plate, or wired |
| >144 | >3,600 | 1/4" | Wired glass only |

---

### Key Principles

1. **Sign type drives everything.** The first step is always classifying the sign. The type determines material requirements, height limits, attachment rules, and applicable code sections. A wall sign has different rules than a projecting sign, even if they look similar.

2. **Noncombustible is the default for most sign types.** Projecting signs, roof signs, and marquee signs must be entirely noncombustible. Wall signs >40 sq ft must also be noncombustible. Only ground signs and small wall signs may use combustible framing.

3. **Every illuminated sign triggers CEC Article 600.** Any sign containing electrical wiring (including LEDs, neon, fluorescent, or any powered illumination) must comply with Article 600 in full: listing, disconnect, branch circuit, grounding/bonding, enclosure, and transformer requirements.

4. **Disconnects are mandatory and must be accessible.** Each electric sign needs its own disconnect opening all ungrounded conductors, controlling no other load. Location must be at point of entry, within sight, or at a marked remote location accessible to first responders.

5. **Structural design is required — even for small signs.** All signs must be designed for wind loads (CBC 1609 / ASCE 7). Most of California is in Seismic Design Categories D-F, meaning seismic design is typically required for all but the smallest signs.

6. **Attachment details matter.** No wood block anchorage (except on wood buildings). No nails or staples for projecting signs. No anchorage to unbraced parapets. Minimum fastener sizes are specified.

7. **Local zoning controls most aesthetic and size issues.** The state building code governs structural, electrical, fire, and life safety. Sign area limits, setbacks, maximum number of signs, brightness/dimming for digital signs, and aesthetic standards are almost always set by the local jurisdiction's zoning ordinance — not the CBC.

8. **Plastic area is limited.** Individual electric sign plastic faces max 200 sq ft. Total plastic on large signs follows a sliding scale capped at 1,100 sq ft. All plastics must pass the ASTM D635 burn rate test.
