# CEBC Chapter 6 — Classification of Work

> **Source:** 2025 CEBC Ch. 6, especially §§ 601.1, 602.1–602.2, 603, 604, and 606 (Title 24 Part 10, effective January 1, 2026).
> **Authority:** 2025 California Existing Building Code (CEBC), Title 24 Part 10
> **Effective:** January 1, 2026

This reference catalogs how CEBC Chapter 6 classifies any work done on an existing building. Every residential remodel must first be classified into one of these buckets before any other code section is applied.

---

## Why this matters

CEBC §601.1 binds: *"The provisions of this chapter shall be used in conjunction with Chapters 7 through 11 and shall apply to the alteration, addition and change of occupancy of existing structures, as referenced in Section 301.3.2. The work performed on an existing building shall be classified in accordance with this chapter."*

Misclassification is the #1 cause of phantom-remodel failures. A "remodel" labeled as Level 1 that should be Level 3 escapes Chapter 9 entirely. Always classify first, then apply downstream chapters.

---

## The seven classifications (CEBC §§602–608)

### 1. Repair (CEBC §405 / §601 framework)
- Restoration to predamage condition; not within Chapter 6 scope per se. Repairs comply with Chapter 4 (Repairs).
- *Trip wire to watch:* Coastal §13252(b) — replacement of ≥50% of an SFR is **not** repair and maintenance under PRC §30610(d). See `coastal-replacement-structure.md`.

### 2. Alteration — Level 1 (CEBC §602)
**Verbatim §602.1 Scope:** *"Level 1 alterations include the removal and replacement or the covering of existing materials, elements, equipment or fixtures using new materials, elements, equipment or fixtures that serve the same purpose."*

**Application (§602.2):** comply with Chapter 7.

Examples: like-for-like fixture swap, re-roof in same material, wall finish refresh, drywall patch.

### 3. Alteration — Level 2 (CEBC §603)
**Verbatim §603.1 Scope:** *"Level 2 alterations include the addition or elimination of any door or window, the reconfiguration or extension of any system, or the installation of any additional equipment, and shall apply where the work area is equal to or less than 50 percent of the building area."*

**Exception:** *"The movement or addition of nonfixed and movable fixtures, cases, racks, counters and partitions not over 5 feet 9 inches (1753 mm) in height shall not be considered a Level 2 alteration."*

**Application (§603.2):** comply with Chapter 7 (Level 1) **plus** Chapter 8.

Examples: kitchen reconfiguration with new windows; bathroom relocation; HVAC system extension.

### 4. Alteration — Level 3 (CEBC §604) — TRIP WIRE
**Verbatim §604.1 Scope:** *"Level 3 alterations apply where the work area exceeds 50 percent of the building area."*

**Application (§604.2):** comply with Chapters 7 and 8 **plus** Chapter 9. Cumulative — Level 1 + Level 2 + Level 3 requirements all stack.

This is **State Trip Wire 2.** See `cebc-alteration-levels.md` for full Level 3 stack consequences (sprinkler retrofit per CFC §1103, structural per §906, energy per §907, ERCES per §908).

### 5. Change of Occupancy (CEBC §605)
**Verbatim §605.1 Scope:** *"Change of occupancy provisions apply where the activity is classified as a change of occupancy as defined in Chapter 2."*
**Application:** Chapter 10.

Out of scope for typical residential remodel; flag only if the project converts (e.g., garage conversion that changes Group U → R-3 — likely an ADU, dispatch to ADU skill).

### 6. Additions (CEBC §606)
**Verbatim §606.1 Scope:** *"Provisions for additions shall apply where work is classified as an addition as defined in Chapter 2."*
**Application:** Chapter 11. See `cebc-additions.md`.

When scope adds floor area → dispatch to `../../residential-addition/references/california-baseline.md` and apply the §1101.2 nonconformity rule and the §1103.1 5% gravity-load trigger.

### 7. Historic Buildings (CEBC §607)
**Verbatim §607.1 Scope:** *"The provisions of the California Historical Building Code (Part 8, Title 24, C.C.R) shall apply to qualified historical buildings or properties."*

If on local, state, or federal historic register → CHBC governs. Flag for manual review.

### 8. Relocated Buildings (CEBC §608, not extracted here)
Out of scope for typical remodel. Flag for manual review if applicable.

---

## Work Area definition (CEBC §202, verbatim)

**This is the load-bearing definition for §603 / §604 thresholds:**

> *"WORK AREA. That portion or portions of a building consisting of all reconfigured spaces as indicated on the construction documents. Work area excludes other portions of the building where incidental work entailed by the intended work must be performed and portions of the building where work not initially intended by the owner is specifically required by this code."*

**Source:** 2025 CEBC § 202 (Work Area definition).

**Operational reading:**
- "Work area" is **reconfigured spaces** as drawn — NOT total demolished area, NOT total touched area.
- Spaces where incidental work is required (e.g., patching a wall to run a new circuit) are **excluded**.
- Spaces where new code requires work the owner did not intend (e.g., asbestos abatement triggered by demo) are **excluded**.
- For the §604 50%-of-building-area threshold: numerator = reconfigured floor area; denominator = total building area (gross floor area, all stories).

---

## Decision Tree for Classification

```
Is the project restoring damage to predamage condition only?
  YES → Repair (Chapter 4). Coastal trip wire still applies if ≥50% of SFR replaced.
  NO  → Continue.

Does the project add new conditioned/unconditioned floor area?
  YES → Addition (Chapter 11). Apply §1101.2 nonconformity + §1103.1 5% gravity-load trigger.
  NO  → Continue.

Is the work limited to like-for-like replacement (no new doors/windows, no system reconfig)?
  YES → Level 1 Alteration (Chapter 7).
  NO  → Continue.

Is the reconfigured floor area >50% of total building area?
  YES → Level 3 Alteration (Chapters 7 + 8 + 9). TRIP WIRE 2 fires.
  NO  → Level 2 Alteration (Chapters 7 + 8).

Independent of the above:
- Coastal §13252(b): is ≥50% of structure being replaced? → TRIP WIRE 1 (CDP required).
- §202 Substantial Structural Alteration: do gravity elements altered in 5 yrs support >30% of floor + roof area? → TRIP WIRE 3 (lateral upgrade).
```

A remodel can fire **all three trip wires simultaneously** — they are independent tests.

---

## Cross-references
- CEBC § 202 work-area definition.
- Level 1/2/3 detail: `cebc-alteration-levels.md`.
- §202 Substantial Structural Alteration: `cebc-substantial-structural-alteration.md`.
- Additions: `cebc-additions.md`.
- Coastal trip wire: `coastal-replacement-structure.md`.
