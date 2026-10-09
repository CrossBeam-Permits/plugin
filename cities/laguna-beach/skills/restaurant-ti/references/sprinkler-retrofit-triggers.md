# Laguna Beach — Sprinkler Retrofit Triggers for Restaurant TI

**Operative code:**
- **LBMC Sec. 14.50.104** (Title 14, Building Code adoption) — Group A trigger, **valuation-based** per CBC Sec. 903.6 framework
- **LBMC Title 15 Sec. 1103.5.4** (Fire Code Ch. 11 local amendment) — Group R trigger, **scope-based**, used when there is residential above the restaurant
- **LBMC Sec. 903.2 (amended)** — sprinklers required throughout new construction regardless of size

---

## Two Independent Triggers — Check Both

For any restaurant TI in an existing building, run BOTH analyses and apply whichever fires first. They are not mutually exclusive; in mixed-use buildings (restaurant downstairs, residential above), both can fire on the same project.

### Trigger 1 — Group A (Restaurant Proper) — LBMC Sec. 14.50.104 / CBC Sec. 903.6

Valuation-based. The restaurant proper is the Group A-2 fire area (Group B if occupant load <50 per CBC 303.1.1).

**Test:** Sum the value of permitted work to the Group A fire area over any **3-year rolling period.** If the cumulative value exceeds **50%** of the building value (Group A portion), a fully compliant automatic sprinkler system per CBC Sec. 903.3 is required throughout the Group A fire area.

| Input | How to compute |
|-------|----------------|
| Cumulative work value | Sum of valuation on all permits in the 3-year rolling window for the Group A fire area |
| Building value | Use ICC Building Valuation Data for the Group A occupancy times the floor area, or city-approved appraised value |
| 50% threshold | Cumulative work value / building value × 100 |

If trigger fires:
- Full NFPA 13 sprinkler system throughout the Group A fire area
- 24-hour UL central station monitoring (Title 15 Sec. 6.16.1)
- FDC per LBMC-amended NFPA 13 Sec. 16.12.1 (two 2½" inlets, OSHA red, ≤150 ft from public hydrant)
- Hydrant flow test ≤6 mo (LBMC Sec. 28.1.3)
- Deferred submittal to LBFD

### Trigger 2 — Group R Component Above (Mixed-Use) — LBMC Title 15 Sec. 1103.5.4

Scope-based, independent of valuation. Applies when the building has any existing Group R fire area — most commonly apartments above the restaurant.

**Verbatim (Sec. 1103.5.4):**

> An automatic sprinkler system installed in accordance with Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring a building permit that involves alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories.
>
> Exception: Work that consists only of the installation of fire-resistant siding.

Any ONE of the three prongs independently fires the retrofit:

1. **Alteration of 50% or more of the building** — the city's major-remodel methodology (per `../../residential-remodel/references/city-major-remodel-methodology.md`) is the operational test. Counts demolition, removal of structural elements, and new construction toward the percentage.
2. **Work on 50% or more of the building's exterior** — façade, roof, exterior walls. A storefront overhaul + façade upgrade combined with a roof patch can easily exceed 50%.
3. **Addition of one or more stories** — any vertical addition.

If trigger fires:
- Full NFPA 13 sprinkler system **throughout all existing Group R fire areas** (not just the restaurant)
- Same monitoring / FDC / flow test stack as Trigger 1
- The owner of the residential portion must allow access for installation — this is often a major friction point on mixed-ownership buildings

**Practical effect:** A "modest restaurant TI" with a new storefront, refreshed façade, and new awnings can cross the 50%-of-exterior threshold and pull retrofit obligations onto the residential floors above. Always check.

### Trigger 3 — New Building Sprinkler Requirement — LBMC Sec. 903.2 (amended)

If the building is **new construction** (shell-and-core), LBMC Sec. 903.2 expands the state sprinkler scope and effectively requires sprinklers throughout. Restaurant TIs into brand-new shells inherit this — confirm shell sprinkler installation is in place and the restaurant TI ties in correctly.

---

## Analysis Worksheet

For each restaurant TI, document:

| Field | Value |
|-------|-------|
| Building type | New construction / existing |
| Mixed-use Group R component? | Yes / No |
| If yes: prior sprinkler status of Group R area | Sprinklered / Not sprinklered |
| Current TI work value | $______ |
| Permitted work in prior 36 months (Group A area only) | $______ |
| Cumulative 3-yr value (Group A) | $______ |
| Group A building value | $______ |
| Trigger 1 fired? (cumulative > 50% of value) | Y / N |
| Total altered area (sf) / total building area (sf) | ____ / ____ = ____% |
| Trigger 2 prong 1 fired? (alteration ≥50%) | Y / N |
| Exterior work area (sf) / total exterior area (sf) | ____ / ____ = ____% |
| Trigger 2 prong 2 fired? (exterior ≥50%) | Y / N |
| Stories added | ____ |
| Trigger 2 prong 3 fired? (added story) | Y / N |
| Retrofit scope required | None / Group A only / Group R only / Both |

---

## Existing Building Code Coordination

Where retrofit is required, the state CEBC (California Existing Building Code) governs the construction work itself. See `existing-building.md` for alteration levels and hazard category tables. LBMC Title 14/15 is the local trigger; CEBC is the state implementation rulebook for how to actually execute the work.

---

## Carve-Outs and Limits

- **Fire-resistant siding only:** Sec. 1103.5.4 exception. A pure siding replacement project — even if it covers >50% of the building exterior — does NOT fire Trigger 2 prong 2.
- **Painting / minor repair:** Does not count toward 50%-of-exterior calculation.
- **Re-roof only (no walls):** May or may not fire Trigger 2 prong 2 depending on city interpretation; the roof is part of the "exterior" envelope. Combined with any wall work the threshold is easier to hit.

---

## Output Findings

- **PASS** — No retrofit trigger fires; OR all required retrofit work is in the permit set with proper sprinkler design, monitoring, FDC, hydrant test.
- **FAIL** — A trigger clearly fires and the permit set does not include the required sprinkler retrofit.
- **FLAG** — Cumulative valuation history or scope percentage cannot be determined from submittal; need 3-yr permit history and certified scope calculation.
- **N/A** — New shell construction where sprinklers are installed under the shell permit and the TI ties in correctly.
