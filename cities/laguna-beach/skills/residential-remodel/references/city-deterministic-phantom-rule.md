# Laguna Beach — Deterministic Phantom-Remodel Rule (Codified 6th Signal)

The parent state skill (the California Residential Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" in `../SKILL.md`)) runs a **heuristic** 5-signal phantom-remodel detector with a 2-of-5 / 3-of-5 decision rule (valuation ratio, demo vs structural mismatch, framing key tells, 100% new windows/doors, phased-permit history). Inside Laguna, the city has **codified an additional deterministic signal** in the May 2026 republish of the Building Plan Check Submittal Requirements that supplements (does not replace) the parent's heuristic detector.

---

## Source Verbatim

From the City source document (not included in this plugin), Page 4 (file mod date **2026-04-30**, May 2026 republish), under "PLAN INFORMATION":

> *"Show the existing and proposed floor plan that includes the existing walls to remain, demolished walls (unless a detailed demolition plan is included) and the new walls. Include a wall legend for the existing walls to remain, walls to be demolished and new walls shall be provided. **Existing walls with structural upgrades/modifications affecting the foundation or the lateral support (shear) are considered new walls. Existing walls with the drywall removed are considered part of the area of renovation.**"*

The two emphasized sentences are the operative deterministic rule. They convert two categories of "existing to remain" walls into "new" or "renovation" walls **by definition**, no judgment call required.

---

## Why "Deterministic" — Contrast with Parent's Heuristic Signals

The parent's 5 signals are heuristic — they are framed as "if 2 of 5 fire, manual review; if 3 of 5 fire, presumptive new construction." Each signal is a probabilistic indicator of phantom-remodel intent.

Laguna's rule is **deterministic** because the city has codified the conversion as a definition. There is no judgment call:
- A wall annotated "existing to remain" but carrying new continuous footings, new shear panels, or new hold-downs IS, by city definition, a new wall.
- A wall annotated "existing to remain" with drywall removed IS, by city definition, part of the area of renovation.

This means the rule does not "fire" or "not fire" — it converts. The downstream effect is to re-run the Step B coastal zone appealable or coastal zone non-appealable major-remodel methodology with those walls counted in the renovation column instead of the existing column. Recount the walls on each floor of the affected structure; the June 2026 handout counts walls "on each floor". A project that appeared to be at 30% wall demolition under the original plan-set classification may land at 60% under the corrected classification.

---

## How to Apply (7-Step)

For every Laguna residential remodel review:

1. **From the demolition plan** (typically A-1.1 or "Demolition Plan" sheet referenced on the cover sheet — required per the Building Plan Check Submittal Requirements page 3 list): identify every wall annotated "existing to remain" or labeled as part of the existing wall hatching legend.

2. **Cross-check against the structural plans** (S-sheets — foundation plan, framing plans, shear-wall plan, hold-down schedule). For each "existing to remain" wall, check whether any of the following appears at that wall:
   - New continuous footing under the wall
   - New shear panel sheathing
   - New hold-down at any stud bay
   - New strap or other lateral-system reinforcement
   - Structural upgrade or modification affecting the foundation or lateral support
   If yes → **convert wall to "new" by city definition.**

3. **Cross-check against the demolition plan's drywall scope.** For each "existing to remain" wall, check whether the wall has its drywall removed (typically called out in the demolition plan or on the wall legend). If yes → **convert wall to "part of the area of renovation" by city definition.**

4. **Recompute** the Step B methodology with the converted walls counted in the renovation column. Do this for each structure separately, and for walls on each floor. In the coastal zone appealable area: re-run the foundation + walls + roof calculation. In the coastal zone non-appealable area: re-run the exterior-walls-only calculation.

5. **Compare to 50%.** A project that crosses the 50% threshold under the corrected calculation is a **major remodel** under the June 2026 Major Remodel Quick Guide's coastal zone appealable or coastal zone non-appealable methodology [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639179723814800000, as of 2026-09-29]. Combine the floors with the three-way floor rule in `city-major-remodel-methodology.md` (Unit of Measurement). If a converted floor reaches 50% or more but the whole-structure total stays under 50%, return FLAG with both numbers; the City must confirm how floors combine.

6. **Output PASS / FLAG / TRIGGERED:**
   - **PASS** — no walls converted; project does not change classification.
   - **FLAG** — walls converted but cumulative renovation still below 50%; record the conversions in the corrections letter so the applicant cannot game the count mid-construction.
   - **TRIGGERED** — converted walls push the project across 50%; project is **re-classified as a major remodel**.

7. **If TRIGGERED on coastal-zone property,** cite **11 Lagunita LLC v. CCC (2020)** in the corrections-letter body alongside the verbatim §1103.5.4 fire-retrofit consequence (if it also fires) and the LCP/handout/§25.10.008(O) authority chain. 11 Lagunita is the operative California precedent: a Laguna oceanfront SFR owner pulled "remodel" permits on what was operationally a teardown; CCC reclassified as new construction; $1M penalty + cease-and-desist + seawall removal. California Supreme Court denied review (2020).

---

## Interaction with Parent's Heuristic 5-Signal Detector

Both run. The deterministic rule converts walls; the heuristic detector then runs on the corrected wall count. So:

- If the parent heuristic flags Signal 2 (demo-plan vs structural-plan mismatch — existing-hatch >50% but new continuous footings + new shear panels + new hold-downs every stud bay) on a Laguna project, the **same evidence** that triggers parent Signal 2 ALSO triggers the deterministic rule's wall conversion. The two are not redundant — Signal 2 is "this looks like phantom intent based on the mismatch," and the deterministic rule is "the city has codified that those walls are new walls by definition."

- If the deterministic rule converts walls but the parent's other 4 signals don't fire, the parent's decision rule (2-of-5 → manual review, 3-of-5 → presumptive new construction) may not promote the project on its own. The deterministic rule is sufficient on its own — if the corrected calculation crosses 50%, the project is a major remodel regardless of how many parent signals fired.

- If the parent fires 3-of-5 signals AND the deterministic rule converts walls AND the corrected calculation crosses 50%, the project is **presumptive new construction** per the parent's decision rule AND a **major remodel** per Step B AND a **sprinkler retrofit** per Step D. The corrections letter should walk all three independently.

---

## Why This Rule Exists

The deterministic rule is the city's response to the phantom-remodel pattern that 11 Lagunita made famous: a permit applicant labels exterior walls "existing to remain" on the demolition plan to keep the demolition percentage below the major-remodel threshold, while the structural plans show new continuous footings, new shear panels, and new hold-downs at every stud bay — meaning that operationally the wall is being rebuilt from the studs out. The original framing is being reused only nominally.

The deterministic rule closes that loophole by codifying that:
- A wall whose foundation or lateral system is being upgraded **is** a new wall.
- A wall whose drywall is removed **is** part of the renovation.

This is the city's response. It is operationally enforced via the Building Plan Check Submittal Requirements; the plan-checker is required to apply this rule before signing off on the cover sheet.

---

## Diff Discipline — May 2026 Republish

The May 2026 republish of the Building Plan Check Submittal Requirements (file mod date 2026-04-30) is the current document. Its predecessor (the 2022-cycle file at the City source document (not included in this plugin)) does not contain the deterministic rule in this form. Cite the May 2026 republish.

**Stale citations to avoid:**
- The May 2026 republish has a single stale line (line 78: *"Two (2) copies wet stamped hydrology study for site drainage consistent with 2022 CB Standards."*) — this is a known city oversight in the May 2026 republish; do not cite. The rest of the document was refreshed.
- The Residential Room Alteration / Remodel Checklist (May 2026 republish) still says "2022 editions" in the body code-list (line 18: "indicate that all work will be done in compliance with the 2022 editions of the California Residential Code, ..."). The Building Plan Check Submittal Requirements page 4 (lines 149–156) is correct (lists 2025 cycle). The 2025 cycle applies regardless — cite Building Plan Check Submittal Requirements for the code list.

---

## Output Format

```
## Deterministic Phantom-Remodel Signal — Laguna Codified Rule
**Result:** PASS | FLAG | TRIGGERED
**Code:** Building Plan Check Submittal Requirements (mod date 2026-04-30), Page 4 — wall legend rule
**Citation:** "Existing walls with structural upgrades/modifications affecting the foundation or the lateral support (shear) are considered new walls. Existing walls with the drywall removed are considered part of the area of renovation."
**Walls converted to NEW by definition:** [list of wall IDs from plan set with brief reason — e.g., "Wall A-1: new continuous footing per S-2.0 detail 4; converted to new per city rule"]
**Walls converted to RENOVATION by definition:** [list of wall IDs with brief reason]
**Recomputed % under [coastal zone appealable | coastal zone non-appealable] methodology, for each structure and each floor:** [original %] → [recomputed %]
**Crosses 50% threshold?** YES | NO
**Action required:** [If TRIGGERED on coastal property: cite 11 Lagunita and re-run major-remodel determination per Step B; promote tier to DRB-required; trigger §1103.5.4 retrofit; trigger Ch. 25.07 CDP. If TRIGGERED in the coastal zone non-appealable area: same; the CDP still applies when the parcel is in the coastal zone (Step G). If FLAG: record conversions in corrections letter.]
```
