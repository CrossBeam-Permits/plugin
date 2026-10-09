# Coastal Replacement Structure — TRIP WIRE 1 (14 CCR §13252(b))

> **Sources:**
> - 14 CCR § 13252, especially § 13252(b) (2026 text)
> - CCC enforcement interpretation codified in San Diego IB-402, Santa Barbara LCP, Santa Cruz County LCP, San Carlos LCP (referenced; not duplicated here)
> **Authority:** California Coastal Commission, under Public Resources Code §30610(d)
>
> ⚠️ **Citation discipline:** §13252(b) the regulation **does not contain** the operative "≥50% of exterior wall linear feet, structural elements only, floor-by-floor" formula. That formula is CCC's **settled enforcement interpretation**, codified into many city/county Local Coastal Programs. The skill must always cite **both** the regulation and the operative formula and label which is which.

---

## The regulation (verbatim §13252(b))

From 14 CCR Subchapter 7 — Repair and Maintenance Activities that Require a Permit, §13252:

> *"§ 13252. Repair and Maintenance of Activities Requiring a Permit.*
> *...*
> *(b) Unless destroyed by natural disaster, the replacement of 50 percent or more of a single family residence, seawall, revetment, bluff retaining wall, breakwater, groin or any other structure is not repair and maintenance under Section 30610(d) but instead constitutes a replacement structure requiring a coastal development permit."*

**Source:** 14 CCR § 13252(b) (2026 text).

**Plain reading:** if ≥50% of an SFR (or seawall/revetment/etc.) is replaced, the work is **not** "repair and maintenance" exempt under PRC §30610(d). It is a **replacement structure** that requires a Coastal Development Permit (CDP).

---

## The operative formula (CCC settled enforcement interpretation)

⚠️ **Not in §13252(b) itself.** The formula below is CCC's settled enforcement practice, applied in cease-and-desist orders and codified into multiple LCPs.

**The formula:** ≥50% of any of the following triggers replacement-structure status —
- **Exterior wall replacement** measured by **linear feet of exterior wall**, computed **floor-by-floor**, counting **structural elements only** (studs, sheathing, top plates, sills, headers, sole plates, posts in walls — not finishes, not windows/doors, not interior partitions).
- **Major structural framework** — roof framing, floor framing, foundation, primary lateral system.

The CCC applies the test **scope-cumulative**, meaning phased permits at the same APN are aggregated when CCC opens an enforcement file (this is how 11 Lagunita LLC v. CCC unfolded — multiple "selective" permits totaled to a teardown).

### LCP codifications (examples)

The skill should cite the appropriate LCP when reviewing in a city/county that has codified the formula:
- **City of San Diego IB-402** (Information Bulletin 402) — explicitly defines the floor-by-floor exterior wall LF test for SFRs in the coastal zone.
- **Santa Barbara LCP** — adopts the 50% exterior wall LF test.
- **Santa Cruz County LCP** — same.
- **San Carlos LCP** — same.

For cities without a codified LCP formula (including Laguna Beach), CCC enforcement applies the same test as a matter of settled practice. Cite both §13252(b) and CCC's enforcement interpretation; note the LCP codifications as supporting precedent.

---

## Consequence — what fires when this trip wire trips

1. **Loss of repair/maintenance exemption** — the project can no longer rely on PRC §30610(d) repair/maintenance status.
2. **CDP required** — a Coastal Development Permit must be obtained from the local government (with LCP), or from CCC directly (without LCP), before any work proceeds.
3. **Appealable-zone review under current LCP** — if the property is in the appealable area (typically: between the sea and the first public road; between the sea and 300 ft inland; within 100 ft of any wetland/stream/coastal bluff edge; or specially designated areas), the CDP becomes appealable to CCC, and the entire project is reviewed against **current** LCP standards (not the LCP standards in effect when the building was built).
4. **No more "remodel" framing** — the project is reviewed as **new development**. All current setbacks, floor-area ratios, height limits, geological hazard analyses (bluff-edge setbacks, sea-level-rise projections), public-access requirements, sensitive-habitat protections, view-corridor protections, and design-review tiers apply.

This is why the trip wire matters: a project that the city would rubber-stamp as a "remodel" gets re-classified as new construction with full LCP review, and any nonconforming aspect of the existing structure must be cured before approval.

---

## Cross-reference: 11 Lagunita LLC v. CCC (2020)

This case is the precedent for why the trip wire exists in operational practice:
- Owner pulled City of Laguna Beach permits labeled "remodel."
- Took all exterior walls to studs, replaced roof and framing, reinforced seawall.
- CCC overruled the city, classified work as new construction (replacement structure).
- **$1M penalty + cease-and-desist + seawall removal.**
- California Supreme Court denied review (2020).

Cite this case in any review where the phantom-remodel detector flags ≥3-of-5 signals on a coastal-zone property.

---

## How to apply the test

### Step 1 — Determine if the property is in the coastal zone
- Check CCC coastal zone boundary maps (statewide GIS).
- If yes → §13252(b) potentially applies.
- If no → trip wire does not fire (skip to other state trip wires).

### Step 2 — Determine if the property is in the appealable zone
- Between the sea and the first public road parallel to the sea, OR
- Within 300 ft of the inland extent of the beach or mean high tide line, OR
- Within 100 ft of any wetland, stream, or coastal bluff edge, OR
- Within 300 ft of the top of the seaward face of a coastal bluff, OR
- Other specially designated appealable areas.

This determines whether a CDP issued by the city is appealable to CCC.

### Step 3 — Compute exterior wall LF replacement, floor-by-floor

For each floor of the existing structure:
- Total linear feet of exterior wall on that floor.
- Linear feet of exterior wall whose **structural elements** (studs, sheathing, sole/top plates, headers, posts) will be removed and replaced.
- If the percentage on **any single floor** ≥50%, the trip wire fires.

Per CCC enforcement, also test: roof framing replacement %, floor framing replacement %, foundation replacement %. ≥50% replacement of any one of these is independently disqualifying.

### Step 4 — Check phased permit history at the APN

Pull all building permits for the same APN over the prior 5+ years. Sum the cumulative replacement scope across permits. If cumulative ≥50%, the trip wire still fires (this is how Lagunita was caught). The §13252(b) regulation does not specify a lookback, but CCC enforcement practice aggregates phased permits.

### Step 5 — Cross-reference `coastal-development` skill

When this trip wire fires, **invoke** `../../coastal-development/references/california-baseline.md`. That skill has 12 references covering CDP process, when-required, appealable areas, categorical exclusions, LCP overview, appeals, definitions, and resource protections. **Do not duplicate that content here.** The parent residential-remodel skill's job is to **detect** the trip wire and **dispatch** to the coastal skill for the full CDP analysis.

---

## Output checklist

| # | Check | What to Verify | Source |
|---|-------|----------------|--------|
| C-1 | Coastal zone determination | Is the parcel in the CCC coastal zone? | CCC GIS |
| C-2 | Appealable-zone determination | Is the parcel in the appealable area (sea/first road, 300 ft, 100 ft of wetland/bluff)? | CCC GIS |
| C-3 | Exterior wall LF replacement, floor-by-floor | For each floor, % of exterior wall LF being replaced (structural only) | A-sheets + S-sheets |
| C-4 | Roof framing replacement % | % of roof framing being replaced | S-sheets |
| C-5 | Floor framing replacement % | % of floor framing being replaced | S-sheets |
| C-6 | Foundation replacement % | % of foundation being replaced | S-sheets |
| C-7 | Phased permit cumulative scope | Sum prior permits at APN; aggregate replacement % | City permit records |
| C-8 | Trip-wire determination | If C-3 (any floor), C-4, C-5, C-6, or C-7 ≥50% → trip wire fires | Aggregation |
| C-9 | Dispatch to coastal-development skill | If trip wire fires, route to `../../coastal-development/references/california-baseline.md` for CDP analysis | Sub-skill dispatch |

---

## Citation discipline reminder

When citing in output:
- **Regulation:** *"14 CCR §13252(b) — replacement of ≥50% of an SFR is not repair/maintenance under PRC §30610(d) but a replacement structure requiring a CDP. (verbatim text quoted)"*
- **Operative formula:** *"Per CCC settled enforcement interpretation (codified in San Diego IB-402, Santa Barbara LCP, Santa Cruz County LCP, San Carlos LCP), the 50% threshold is applied as ≥50% of exterior wall linear feet measured floor-by-floor, structural elements only. CCC also applies the test independently to ≥50% of roof framing, floor framing, and foundation replacement."*
- **Precedent:** *"See 11 Lagunita LLC v. CCC (2020) — Laguna Beach oceanfront SFR, owner-issued city 'remodel' permits, CCC enforcement classified as replacement structure, $1M penalty + cease-and-desist + seawall removal, Cal. Sup. Ct. denied review."*

Never present the formula as if it were in the regulation itself. The regulation gives the 50% threshold without defining how to measure; CCC's enforcement defines the measurement.

---

## Cross-references
- Source regulation: 14 CCR § 13252(b).
- Sub-skill dispatch (always invoke when trip wire fires): `../../coastal-development/references/california-baseline.md`.
- Phantom-remodel signals tied to this trip wire: `phantom-remodel-detection.md`.
