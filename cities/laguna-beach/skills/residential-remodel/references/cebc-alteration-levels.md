# CEBC Alteration Levels 1, 2, 3 — Thresholds and Cumulative Compliance

> **Source:** 2025 CEBC Chs. 6, 8, and 9, especially §§ 602.1, 602.2, 604.1–604.2, and 906.2 (Title 24 Part 10, effective January 1, 2026).
> **Authority:** 2025 California Existing Building Code (CEBC), Title 24 Part 10
> **Effective:** January 1, 2026

The CEBC alteration framework is **cumulative**. Higher-level alterations layer on top of lower-level requirements. Level 3 = Ch. 7 + Ch. 8 + Ch. 9 (all stack).

---

## Level 1 — Like-for-like (Chapter 7 governs)

**Verbatim CEBC §602.1:** *"Level 1 alterations include the removal and replacement or the covering of existing materials, elements, equipment or fixtures using new materials, elements, equipment or fixtures that serve the same purpose."*

**Application (§602.2):** Chapter 7.

**What Chapter 7 requires (high-level):**
- New materials must comply with current code requirements for the materials used (§702).
- Existing materials may remain (§702.2) provided they are in good condition.
- Replacement glass — safety glazing per current CRC §R308 if in hazardous location.
- Reroofing — comply with CRC §R908 / CBC §1511.

**Trigger to escalate:** any new door/window opening, any system reconfiguration, any added equipment → escalate to Level 2.

---

## Level 2 — Reconfiguration ≤50% of building (Chapter 7 + Chapter 8)

**Verbatim CEBC §603.1:** *"Level 2 alterations include the addition or elimination of any door or window, the reconfiguration or extension of any system, or the installation of any additional equipment, and shall apply where the work area is equal to or less than 50 percent of the building area."*

**Exception (§603.1):** *"The movement or addition of nonfixed and movable fixtures, cases, racks, counters and partitions not over 5 feet 9 inches (1753 mm) in height shall not be considered a Level 2 alteration."*

**Application (§603.2):** Chapter 7 (Level 1) **plus** Chapter 8.

**What Chapter 8 adds within the work area (high-level):**
- §802 — building elements and materials within work area (interior finish, sound transmission, fire ratings).
- §803 — fire protection (sprinklers, alarms within work area).
- §804 — means of egress within work area.
- §805 — structural (gravity-load changes, lateral-load changes, voluntary lateral upgrades).
- §806 — electrical.
- §807 — mechanical.
- §808 — reserved in California.
- §809 — energy conservation (Title 24 Part 6).

---

## Level 3 — Work area >50% of building (Chapter 7 + 8 + 9) — TRIP WIRE 2

**Verbatim CEBC §604.1:** *"Level 3 alterations apply where the work area exceeds 50 percent of the building area."*

**Verbatim CEBC §604.2:** *"Level 3 alterations shall comply with the provisions of Chapters 7 and 8 for Level 1 and 2 alterations, respectively, as well as the provisions of Chapter 9."*

**Verbatim CEBC §901.2:** *"In addition to the provisions of this chapter, work shall comply with all of the requirements of Chapters 7 and 8. The requirements of Sections 802, 803, 804 and 805 shall apply within all work areas whether or not they include exits and corridors shared by more than one tenant and regardless of the occupant load."*

### What Chapter 9 adds (verbatim subsection-by-subsection)

**§903 Building elements and materials.**
- §903.1 — *"Existing stairways that are part of the means of egress shall be enclosed in accordance with Section 802.2.1 from the highest work area floor to, and including, the level of exit discharge and all floors below."*
- §903.2.1 (R-3 / townhouse) — *"Where the work area is in any attached dwelling unit in Group R-3 or any multiple single-family dwelling (townhouse), walls separating the dwelling units that are not continuous from the foundation to the underside of the roof sheathing shall be constructed to provide a continuous fire separation using construction materials consistent with the existing wall or complying with the requirements for new structures."*
- §903.3 — interior finish in exits per §802.4.

**§904 Fire protection.**
- §904.1 — *"An automatic sprinkler system shall be provided in accordance with Section 903 of the California Building and California Fire Codes."* (Note: this triggers compliance with the CFC sprinkler thresholds, which for one- and two-family dwellings reach back to CRC §R309 — see `crc-r309-sprinkler-state-exemption.md`. State-level CRC R309 exempts existing un-sprinklered SFRs from retrofit; city-level overlays may add a trigger.)
- §904.2 — fire alarm and detection per CBC §907 / CFC §907 + §1103.7.

**§905 Means of egress.** §905.1–905.4: lighting, exit signs, two-way communication systems where required.

**§906 Structural.** See `cebc-substantial-structural-alteration.md` — §906.2 is the Substantial Structural Alteration trigger (TRIP WIRE 3, independent of the §604 work-area test).

**§907 Energy conservation.** *"Level 3 alterations to existing buildings or structures shall comply with applicable provisions of the California Energy Code (Part 6, Title 24, C.C.R)."* See `energy-code-additions-alterations.md`.

**§908 Emergency Responder Communication Enhancement System (ERCES).** Building must undergo signal-strength evaluation; install ERCES if coverage fails CFC §510.

---

## Cumulative compliance — the load-bearing point

A Level 3 alteration is not "the Chapter 9 stuff." It is **all of Chapter 7 + all of Chapter 8 (in the work area + sometimes building-wide) + all of Chapter 9 (typically building-wide for fire protection).**

**Common phantom-remodel pattern:** project labeled Level 1 ("we're just refinishing") but reconfigured floor area is 60% of the building. Real classification is Level 3, which means:
- Sprinkler retrofit per §904.1 (subject to CRC R309 state exemption — see notes).
- Substantial Structural Alteration check per §906 (likely fires too if walls are coming down).
- Full energy code compliance per §907 / Title 24 Pt 6 §150.2(b).
- ERCES evaluation per §908.

The skill must compute the work area / building area ratio independently of the applicant's classification.

---

## Exceptions to Level 3 (Chapter 9) compliance

**§901.2 Exception:** *"Buildings in which the reconfiguration of space affecting exits or shared egress access is exclusively the result of compliance with the accessibility requirements of Section 306.7.1 shall not be required to comply with this chapter."*

(I.e., if the only reason the project triggers Level 3 is forced accessibility upgrades, Ch. 9 doesn't apply.)

**§906.2 Exception 1 (R-occupancy carve-out for lateral upgrade only):** *"Buildings of Group R occupancy with not more than five dwelling or sleeping units used solely for residential purposes that are altered based on the conventional light-frame construction methods of the California Building Code or in compliance with the provisions of the California Residential Code."*

This exception applies to the §906.2 lateral-system-upgrade requirement only. It does **not** exempt SFRs from the rest of Chapter 9 (sprinklers, energy, ERCES, etc.).

---

## Quick-Reference Table

| Level | Threshold | Required Chapters | Common Triggers |
|-------|-----------|-------------------|-----------------|
| 1 | Like-for-like; same purpose | Ch. 7 | Fixture swap, refinish, like-for-like reroof |
| 2 | Add/eliminate door/window OR reconfig system OR add equipment, AND work area ≤50% | Ch. 7 + Ch. 8 | Most kitchen/bath remodels; HVAC swap with new ducting |
| 3 | Work area >50% of building area | Ch. 7 + Ch. 8 + Ch. 9 | Whole-house remodel; gut renovation |

---

## Cross-references
- §202 Work Area definition: 2025 CEBC § 202.
- Substantial Structural Alteration (independent test): `cebc-substantial-structural-alteration.md`.
- Sprinkler retrofit (state exemption + city overlay): `crc-r309-sprinkler-state-exemption.md`.
- Energy code component triggers: `energy-code-additions-alterations.md`.
