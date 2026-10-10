# Laguna Beach - Floodplain Overlay (LBMC Ch. 25.38)

Sources:

- LBMC **Chapter 25.38 — Floodplain Management** (Title 25, Zoning — the operative floodplain chapter; raw text at the City source document (not included in this plugin))
- City handouts: `floodplain-development-permit-residential.pdf`, `floodplain-regulations-development-vegetation.pdf` (the City source document (not included in this plugin) rows 18 and 49)
- FEMA Flood Insurance Study for City of Laguna Beach (effective **12/3/2009** + subsequent FIRM/FBFM revisions)
- Citywide reference: `../../city-reference/SKILL.md` (Floodplain row in permit decision matrix)

---

## Chapter Reconciliation — Ch. 25.38 is Operative

Earlier versions of this overlay incorrectly cited "Ch. 14.78." That chapter does not exist in the current LBMC. The operative floodplain management chapter is **LBMC Ch. 25.38**, sitting under Title 25 (Zoning). Verified via a clean scrape of the ecode360 table of contents on 2026-05-12.

Always cite **Ch. 25.38**. If a downstream artifact still references "Ch. 14.78," it is stale and should be patched.

---

## Chapter Structure

Ch. 25.38 is organized into six articles:

| Article | Sections | Topic |
|---|---|---|
| I | §25.38.010 – .013 | Statutory authorization, findings, purpose, methods of reducing flood losses |
| II | §25.38.020 | Definitions |
| III | §25.38.030 – .036 | General provisions — lands covered, basis for SFHA, compliance, severability |
| IV | §25.38.040 – .043 | Administration — Floodplain Administrator, duties, FDP issuance, appeals |
| V | §25.38.050 – .057 | Provisions for flood hazard reduction — standards of construction, utilities, subdivisions, manufactured homes, RVs, contingency floodproofing, floodways, **coastal high-hazard (V-zone) areas** |
| VI | §25.38.060 – .062 | Variance procedure |

The **Floodplain Development Permit (FDP)** authority is in **§25.38.042**; the FDP is a separate gate from the building permit and must be issued before construction starts.

---

## Scope and Trigger

Ch. 25.38 applies to:

- All **areas of special flood hazard (SFHA)** identified by the FEMA Flood Insurance Study for Laguna Beach (effective 12/3/2009) and subsequent revisions, including all Zone A, AE, AO, AH, and V/VE areas shown on the city's Flood Insurance Rate Maps (FIRMs) and Flood Boundary and Floodway Maps (FBFMs). Per §25.38.031.
- Areas later identified by the floodplain administrator as flood-prone per §25.38.030.

Most of Laguna Beach is NOT in an SFHA. Floodplain review is not a default-active overlay; check the parcel against the FIRM panel before applying this reference. The principal in-scope geographies are:

- **Aliso Creek** floodplain (lower canyon).
- **Laguna Canyon Creek** floodplain (along Laguna Canyon Road).
- **Coastal V-zones** at the immediate shoreline (open-coast wave hazard) — see §25.38.057.

---

## V-Zone (Coastal High Hazard) Requirements — §25.38.057

For new construction or substantial improvements in a designated V-zone (open-coast wave hazard):

- Foundation must be **open pile or column** designed to withstand storm surge and wave forces.
- Portions below Base Flood Elevation (BFE) must be built with **flood-damage-resistant materials**.
- No fill for structural support below BFE.
- No habitable enclosed space below BFE; below-BFE space limited to parking, access, or storage.
- **BFE adjusted for sea-level rise** for the expected life of the development, **minimum 75 years**, using the 2018 California SLR Guidance medium-high scenario (≈6.6 ft).
- **Elevation Certificate** required at foundation stage AND at finished-construction stage.

---

## A-Zone (Riverine) Requirements — §25.38.050

For new construction or substantial improvements in a designated A-zone (riverine flooding, e.g., Aliso Creek, Laguna Canyon Creek):

- Lowest floor (including basement) elevated to or above BFE plus city freeboard.
- Below-BFE space limited to parking, access, or storage; openings sized to equalize hydrostatic pressure where required.
- Flood-damage-resistant materials below BFE.
- Anchored to resist flotation, collapse, and lateral movement.
- Utilities (mechanical, electrical, plumbing) elevated above BFE or floodproofed — see §25.38.051.
- Elevation Certificate required.

---

## Required Submittals When Ch. 25.38 Applies

In addition to the standard SFR submittal package (`submittal-requirements.md`):

- **Floodplain Development Permit application** — §25.38.042 (separate city form per `floodplain-development-permit-residential.pdf` handout).
- **FIRM/FBFM panel** showing parcel and flood zone designation.
- **BFE determination** (from FIS or city floodplain administrator).
- **SLR-adjusted BFE calculation** for V-zone projects (75-year design life, 2018 SLR Guidance medium-high scenario).
- **Elevation Certificate** (FEMA Form 086-0-33) at foundation stage AND finished construction stage.
- **Open-foundation structural calculations** (V-zone) demonstrating capacity to resist storm surge / wave forces.
- **Wave runup / coastal hazards report** (V-zone; ties into the bluff-edge package on oceanfront lots — see `../../residential-remodel/references/city-bluff-overlay.md`).

---

## Output Format Addition

When the parcel is in an SFHA, add a row to the city overlay output:

```markdown
**Floodplain (Ch. 25.38):** PASS | FAIL | FLAG | N/A
- FEMA flood zone: [V/VE | AE | A | AO | AH | X | Unknown]
- BFE (FIRM): [elevation NAVD88]
- SLR-adjusted BFE (V-zone, 75-yr): [elevation NAVD88]
- Floodplain Development Permit (§25.38.042): [Issued | Pending | Not yet applied]
- Elevation Certificate (foundation): [On file | Pending | N/A]
- Elevation Certificate (finished construction): [On file | Pending | N/A]
```

If the parcel is not in an SFHA per the FIRM, mark `N/A` and proceed without further floodplain analysis. Do not invent a flood zone — if the FIRM panel is ambiguous, FLAG and route to the city floodplain administrator.

---

## Cross-References

- `../../city-reference/SKILL.md` — floodplain row in permit decision matrix (now correctly cites Ch. 25.38).
- `../../residential-remodel/references/city-bluff-overlay.md` — coastal-bluff package; V-zone wave runup analysis often overlaps the bluff-edge report stack.
- `planning-coastal-routing.md` — CDP routing for oceanfront / V-zone parcels.
