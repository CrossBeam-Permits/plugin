# Scope Classification Decision Tree

> **Purpose:** classify any residential remodel submittal into a scope bucket so the parent skill can route to the right CEBC chapter, the right sub-skill, and the right trip-wire tests.
> **Inputs:** the submittal package (cover sheet, A-sheets, S-sheets, schedules, scope narrative, valuation, APN).
> **Outputs:** scope bucket + ordered sub-skill dispatch list + trip-wire test list.

---

## Scope buckets (mutually non-exclusive — a project can be in several at once)

1. **Interior-only remodel** — no exterior wall, no roof, no foundation, no fenestration changes; no added floor area.
2. **Exterior remodel** — siding, windows, doors, deck, railing, roof, exterior cladding work; no interior reconfiguration; no added floor area.
3. **Combined interior + exterior** — both 1 and 2.
4. **Kitchen remodel** — any work involving the kitchen (fixtures, layout, cabinets, appliances).
5. **Bathroom remodel** — any work involving any bathroom.
6. **Whole-house remodel / gut renovation** — work area >50% of building area (CEBC §604 Level 3 territory).
7. **Addition** — any added gross floor area (conditioned or unconditioned).
8. **Phased / multi-permit project** — current submittal is part of a sequence at the same APN within 18 months.

A typical submittal may be Bucket 4 + 5 + 1 (kitchen + bath + interior-only) or Bucket 6 + 7 (whole-house + addition).

---

## Decision tree

```
START: read cover sheet
  ├─ Project location (address, APN, coastal zone Y/N, city)
  ├─ Project type label (cover sheet stated scope)
  ├─ Declared valuation
  ├─ Existing building gross floor area
  └─ New building gross floor area (if different)

STEP 1: Is the project in the coastal zone?
  ├─ YES → flag for Trip Wire 1 (always run); will also need to invoke `../../coastal-development/references/california-baseline.md` if any trip wire fires
  └─ NO  → Trip Wire 1 N/A; continue

STEP 2: Does scope add any gross floor area?
  ├─ YES → bucket 7 (Addition). Apply CEBC Ch. 11. Dispatch to `../../residential-addition/references/california-baseline.md`. See `cebc-additions.md`.
  └─ NO  → continue

STEP 3: Compute work area / building area ratio
  ├─ Work area = sum of reconfigured floor area per CEBC §202 (excludes incidental work)
  ├─ Building area = total existing gross floor area (all stories)
  ├─ Ratio >50% → bucket 6 (whole-house). CEBC §604 Trip Wire 2 fires. Apply Ch. 7 + 8 + 9 cumulative.
  ├─ Ratio ≤50% AND any door/window add/remove OR system reconfig OR added equipment → CEBC §603 Level 2. Apply Ch. 7 + 8.
  └─ Ratio ≤50% AND like-for-like only → CEBC §602 Level 1. Apply Ch. 7.

STEP 4: Identify scope by location within the dwelling
  ├─ Kitchen touched (any of: cabinets, fixtures, appliances, layout) → bucket 4. Dispatch to `../../kitchen-bath-remodel/references/california-baseline.md`.
  ├─ Bathroom touched (any) → bucket 5. Dispatch to `../../kitchen-bath-remodel/references/california-baseline.md`.
  ├─ Both kitchen + bath → still single dispatch to `kitchen-bath-remodel`.
  ├─ Exterior walls/siding/cladding work → bucket 2. Dispatch to city skill the `city` skills in this plugin if exists.
  ├─ Window/door replacement → bucket 2. Dispatch to city skill the `city` skills in this plugin if exists.
  ├─ Roof work → bucket 2. Dispatch to city skill the `city` skills in this plugin if exists.
  └─ Other interior reconfiguration only → no specific sub-skill; parent reviews against CEBC Ch. 7/8/9 directly.

STEP 5: Identify structural scope
  ├─ Are gravity-load-carrying elements being altered? (bearing walls, posts, beams, footings, joists, rafters)
  │   └─ YES → run Trip Wire 3 (CEBC §202 SSA test). Compute tributary area + 5-yr permit lookback. See `cebc-substantial-structural-alteration.md`.
  └─ Is there evidence of substantial exterior wall replacement (≥50% LF on any floor)?
      └─ YES (and coastal zone) → Trip Wire 1 fires. Apply §13252(b) + CCC formula. Invoke `../../coastal-development/SKILL.md`.

STEP 6: Run phantom-remodel detection (always, regardless of scope)
  └─ See `phantom-remodel-detection.md`. 5 signals, 2-of-5 = manual review, 3-of-5 = presumptive new construction (re-run Steps 3 + 5 with the *actual* reconstructed scope).

STEP 7: Assemble output
  ├─ Scope buckets identified
  ├─ CEBC alteration level applied
  ├─ Trip wires fired (1, 2, 3)
  ├─ Phantom detection result
  ├─ Sub-skills dispatched
  ├─ Coastal cross-reference status
  └─ City overlay invocation (always; sprinkler retrofit and major-remodel definition live there)
```

---

## Scope bucket → sub-skill dispatch matrix

| Bucket | Sub-skill(s) to dispatch | Notes |
|--------|--------------------------|-------|
| Interior-only, no kitchen/bath | (none) — parent handles | Apply CEBC Ch. 7/8/9 directly per Level |
| Kitchen | `../../kitchen-bath-remodel/references/california-baseline.md` | |
| Bathroom | `../../kitchen-bath-remodel/references/california-baseline.md` | |
| Kitchen + bath | `../../kitchen-bath-remodel/references/california-baseline.md` (single dispatch) | |
| Window/door replacement | the `city` skills in this plugin | City-only skill exists for many cities |
| Siding replacement | the `city` skills in this plugin | City-only |
| Reroof | the `city` skills in this plugin | City-only |
| Addition (any added SF) | `../../residential-addition/references/california-baseline.md` | Plus apply Ch. 11 rules from `cebc-additions.md` |
| Whole-house / Level 3 | (no separate sub-skill) — parent applies Ch. 7+8+9 | Sub-skill dispatch still triggers for kitchen/bath/exterior components within scope |
| Coastal zone (any scope) | `../../coastal-development/references/california-baseline.md` | If trip wire 1 fires; also invoke for any work in appealable area |
| ADU | `../../adu/references/california-baseline.md` | If ADU is part of scope (CRC §R309.2 Exception 2 applies for sprinklers) |

---

## Citation discipline at scope-classification time

When the cover sheet says "remodel" but Step 3 computes work-area ratio >50%, the project's **operational classification** is Level 3 regardless of the label. The output must:
- State the operational classification (e.g., *"Operational classification: CEBC §604 Level 3 alteration. Cover sheet describes 'remodel' but work area / building area = 62%."*).
- Cite the §202 work-area definition verbatim if the applicant disputes the math.
- Apply Chapter 9 stack regardless of what the applicant labeled the project.

Same discipline for trip wires: an applicant cannot opt out of §13252(b) by labeling work as "repair." The 50% replacement test is objective.

---

## Cross-references
- CEBC classification framework: `cebc-classification-of-work.md`.
- Alteration levels (cumulative compliance): `cebc-alteration-levels.md`.
- Coastal trip wire: `coastal-replacement-structure.md`.
- SSA trip wire: `cebc-substantial-structural-alteration.md`.
- Additions: `cebc-additions.md`.
- Sprinkler retrofit framing: `crc-r309-sprinkler-state-exemption.md`.
- Phantom detection: `phantom-remodel-detection.md`.
- Energy code: `energy-code-additions-alterations.md`.
