# Phantom-Remodel Detection — 5-Signal Module

> **Purpose:** detect submittals labeled as "remodel" that are operationally new construction. Phantom remodels are the highest-stakes false-negative in California coastal cities — they cost municipalities millions in CCC enforcement and sometimes force seawall removal.
> **Precedent case:** 11 Lagunita LLC v. CCC (2020) — Laguna Beach oceanfront SFR, owner-issued "remodel" permits, CCC enforcement → $1M penalty, cease-and-desist, seawall removal, Cal. Sup. Ct. denied review.

The detector computes 5 independent signals from the submittal, applies a 2-of-5 / 3-of-5 decision rule, and dispatches downstream. Every signal must include a **graceful-degradation rule** for missing data.

---

## Decision rule (locked)

| Signals fired | Action |
|---------------|--------|
| 0–1 | Routine review path. Phantom not flagged. |
| 2 | **Manual review path with phantom-remodel checklist.** Reviewer eyeballs each fired signal + spot-checks the other three. |
| 3+ | **Presumptive new construction.** Output requires (a) Coastal §13252(b) replacement-structure analysis (if coastal zone), (b) full major-remodel determination per city threshold, (c) trip-wire 3 SSA check. |

The detector does not auto-reject. It re-routes to a higher level of scrutiny. Frame externally as a "review prioritization tool, not a gatekeeper."

---

## Signal 1 — Valuation ratio

**Definition:** declared construction valuation ÷ assessor market value of the structure (improvement value, not land + improvement).

**Thresholds:**
- **<40%:** signal does not fire.
- **≥40% and <50%:** **YELLOW** flag (counts as ½ signal — does not fire alone, but combines with other yellows). For decision-rule simplicity, count yellow as 1.
- **≥50%:** **RED** — signal fires.
- **Coastal SFR cost-per-square-foot sanity check:** typical coastal SFR remodels run **$200–400/sf**. **>$500/sf** is an additional phantom signal regardless of valuation ratio (suggests a near-teardown costed as remodel).

**Where to find each input:**
- **Declared valuation:** building-permit application cover sheet, "Valuation" / "Estimated Cost of Construction" field. Sometimes on cost-estimate worksheet.
- **Assessor market value:** county assessor parcel record (lookup by APN). Use **structure value only** (not total parcel value) — assessor records typically split improvement value vs land value.
- **Cost-per-sf:** declared valuation ÷ existing building gross floor area.

**Graceful degradation:**
- If declared valuation missing → flag "manual review needed: valuation field empty on cover sheet"; do not fire.
- If assessor value not retrieved → use $/sf sanity check only; if $/sf >$500, fire signal with note "assessor value unavailable; signal based on $/sf only."
- If both missing → flag "Signal 1 cannot be computed; obtain via city/assessor lookup."

---

## Signal 2 — Demo plan vs structural plan mismatch

**Definition:** the architectural demo plan (A-sheets, typically AD-series or D-series) shows existing-to-remain wall hatching covering ≥50% of the building footprint, but the structural plan (S-sheets) shows new structural elements at or under those "existing" walls.

**Specific tells:**
- **New continuous footings** drawn on the foundation plan **under "existing" walls.** A wall whose footing is being replaced is not staying.
- **New shear panels** specified at every wall location — even ones drawn as "existing-to-remain" on A-sheets.
- **New hold-downs at every stud bay** of "existing" walls — engineering-grade retrofit only happens when walls are coming down to studs.
- **New top plates / sole plates** called out as "N" on the framing plan at "existing" walls.
- **Net change in plate height** at "existing" walls (e.g., existing 8'-0" plate, new 9'-0" plate at same wall) — physically impossible without rebuild.

**Where to find each input:**
- **Existing-to-remain wall hatching:** A-sheets, demo plan (AD-1, AD-2…) and existing-conditions plan (A-1.0). Compute footprint % covered by "existing" hatch.
- **New structural at "existing" wall:** S-sheets — foundation plan (S-2 typical), framing plans (S-3, S-4), shear-wall plan (S-5), and hold-down schedule.
- Use sheet legend to confirm "N" / "E" notation conventions.

**Graceful degradation:**
- No structural sheets in submittal → flag "Signal 2 cannot be computed (S-sheets missing). Manual review needed if structural scope is non-trivial."
- A-sheet hatching ambiguous (no legend distinguishing existing vs new) → flag "Signal 2: A-sheet hatching legend missing or ambiguous."
- Computer-vision extraction confidence <70% → flag for manual review on Signal 2.

---

## Signal 3 — Framing key tells

**Definition:** the framing plan's member legend / key shows ~all "N" (new) members, but the cover sheet calls the project a remodel; OR plate-height changes; OR roof-pitch changes at "existing" walls.

**Specific tells:**
- Framing schedule lists 90%+ "N" (new) joists, rafters, beams, posts. Existing-condition member counts <10%.
- New roof pitch differs from existing roof pitch at any "existing-to-remain" wall (the wall framing must absorb the change → wall is being rebuilt).
- New plate heights differ from existing plate heights anywhere "existing" walls are shown.
- New floor-to-floor heights differ from existing.
- "Existing" walls shown receiving new headers at openings that didn't previously exist (the wall had to come down to install the header).

**Where to find each input:**
- **Framing plan:** S-3 / S-4 typically; framing schedule on same sheet.
- **Plate heights:** building section sheets (A-3, A-4) and elevations.
- **Roof pitch:** roof framing plan + elevations.

**Graceful degradation:**
- No framing schedule provided → flag "Signal 3 partial (no framing schedule); evaluate plate-height/roof-pitch tells only."
- Single-line framing (no annotation) → flag "Signal 3 cannot be evaluated from single-line drawings."

---

## Signal 4 — Window/door schedule = 100% new

**Definition:** the window schedule and door schedule show every fenestration as "N" (new), while the wall plan claims those walls are existing-to-remain.

**Specific tells:**
- Window schedule: every row marked new; no "E" or "existing-to-remain" entries.
- Door schedule: every exterior door new.
- Cross-check: do the window/door rough openings on the schedule match existing dimensions (suggesting like-for-like replacement) or are they all new sizes (suggesting wall rebuild to accommodate)?

**Why it matters:** replacing 100% of windows/doors in walls labeled "existing-to-remain" implies either (a) those walls were taken down and rebuilt around new openings, or (b) every existing opening was enlarged or moved (which itself is wall reconstruction). Either way, the "existing" label is misleading.

**Where to find each input:**
- **Window schedule:** A-sheets typically A-7 or A-8.
- **Door schedule:** typically same sheet or adjacent.

**Graceful degradation:**
- Schedule provided but rough-opening dimensions not matched to existing → fire signal if 100% new with note "schedule shows 100% new; cannot confirm openings match existing."
- No schedule → flag "Signal 4 cannot be evaluated (schedules missing)."

---

## Signal 5 — Phased-permit history at the APN

**Definition:** ≥2 building permits within an 18-month rolling window at the same APN with cumulative declared valuation **>50% of the structure's market value.**

**Specific tells:**
- Most common pattern: a "demo" or "soft demo" or "selective interior demo" permit pulled 6–14 months ago, followed by the current "remodel" permit. Cumulative work is a teardown disguised as two separate scopes.
- Other pattern: roof permit + structural-frame permit + interior-finish permit pulled in sequence over 12 months.
- Flag if any prior permit at the APN included demolition keywords ("demo," "remove," "abate") and the current permit's structural drawings show extensive new structure.

**Where to find each input:**
- **City permit records:** ePermit / online portal (varies by city; Laguna uses ThePermitPortal). For onboarded cities, query the permit-history API. For non-onboarded cities, manual lookup or CPRA request.
- **APN match:** parcel APN field on current permit application.
- **Time window:** rolling 18-month lookback from current submittal date.

**Graceful degradation:**
- Permit history API unavailable for the city → flag "Signal 5 cannot be evaluated (no permit-history access for this jurisdiction). Manual lookup recommended."
- APN field empty or invalid → flag "Signal 5 cannot be computed (APN missing)."
- Prior permits found but valuation fields empty → use sf or scope-keyword approximation; flag with note.

**Lookback comparison to other rolling windows:**
- Phantom signal 5: **18-month** rolling window.
- CEBC §202 SSA (Trip Wire 3): **5-year** rolling window.
- CCC §13252(b) enforcement: no specified window; CCC aggregates "scope of work" which can include phased permits going back longer.

The skill must track each lookback **independently** and not conflate them.

---

## Signal-extraction guidance summary

| Signal | Primary source(s) on plan set | Secondary | Computer-vision tractable? |
|--------|------------------------------|-----------|----------------------------|
| 1 — Valuation ratio | Cover sheet "Valuation" field; assessor record (external) | Cost worksheet | Yes (text extraction) + external lookup |
| 2 — Demo vs structural mismatch | A-sheets (existing/demo) vs S-sheets (foundation, framing, shear) | Wall legends | Partial (vision + legend NLP) |
| 3 — Framing key tells | S-sheets framing plans + schedule; A-sheets sections + elevations | Roof plan | Partial (legend NLP + dimension extraction) |
| 4 — Window/door schedule | A-sheets schedules | Wall plan | Yes (table extraction) |
| 5 — Phased permit history | City permit-history API; APN | CPRA request | Yes (API) — depends on city onboarding |

---

## Output format for the phantom detector

```
## Phantom-Remodel Detection

| Signal | Status | Evidence |
|--------|--------|----------|
| 1. Valuation ratio | FIRED / NOT FIRED / FLAG | $X declared ÷ $Y assessor = Z%; $/sf = $W |
| 2. Demo vs structural mismatch | FIRED / NOT FIRED / FLAG | "existing" hatch covers N% of footprint; S-sheets show new continuous footings under those walls (S-2 sheet, locations [...]) |
| 3. Framing key tells | FIRED / NOT FIRED / FLAG | Framing schedule shows N/(N+E) = X% new; plate-height change at wall [grid line] |
| 4. Windows/doors 100% new | FIRED / NOT FIRED / FLAG | Window schedule: Z/Z new. Door schedule: D/D new. |
| 5. Phased permit history | FIRED / NOT FIRED / FLAG | Prior permits at APN within 18 mo: [...]. Cumulative valuation = X% of market value. |

**Total signals fired:** [n] / 5
**Decision:** [routine / manual-review-with-checklist / presumptive-new-construction]
**Cited precedent (if 3+):** 11 Lagunita LLC v. CCC (2020) — Laguna Beach oceanfront SFR, $1M penalty for owner-issued "remodel" permits that constituted replacement structure.
```

---

## When phantom detection fires, what else fires

If 3+ signals fire (presumptive new construction), the parent skill must also:
1. **Run Trip Wire 1 (Coastal §13252(b))** — even if scope reads as "interior remodel," the structural reality may push the project across the 50% replacement threshold. See `coastal-replacement-structure.md`.
2. **Run Trip Wire 2 (CEBC §604 Level 3)** — re-compute work area / building area using the *actual* reconstruction scope, not the labeled scope.
3. **Run Trip Wire 3 (CEBC §202 SSA)** — pull S-sheet structural element list, compute tributary area, apply 5-year lookback. See `cebc-substantial-structural-alteration.md`.
4. **Cite 11 Lagunita LLC v. CCC** in the corrections-letter body as the operative precedent.
5. **Recommend a major-remodel determination** request to the city (city skill handles the actual threshold).

---

## Cross-references
- Trip Wire 1 (Coastal): `coastal-replacement-structure.md`.
- Trip Wire 2 (Level 3): `cebc-alteration-levels.md`.
- Trip Wire 3 (SSA): `cebc-substantial-structural-alteration.md`.
- Sprinkler retrofit framing (state silence + city overlay): `crc-r309-sprinkler-state-exemption.md`.
