# Builder Mode — Sanity Check for EV Charger and Water Heater

Quick walk-through confirming the new flattened skills have enough structure to drive a natural builder conversation. Both pass the test — the Plan-Check Checklist tables function as an implicit question list Claude can walk through.

---

## EV Charger — "I want to install a Level 2 charger in Huntington Beach"

Intake Claude would naturally run, keyed to plan-check items:

| Plan-check item | Intake question |
|---|---|
| #1 Charger amperage | What EVSE are you installing? Brand, model, amp rating? |
| #12 Equipment listed | (inferred from brand/model — Claude verifies NRTL listing) |
| #6 Service panel capacity | What's your main panel size (100A/125A/200A)? |
| #7 Equipment location | Where will it be mounted? Garage, exterior wall, driveway? |
| #9 GFCI protection | (inferred — required for garage/outdoor; Claude notes) |
| #10 Disconnect means (>60A) | What's the circuit ampacity — 40A, 50A, 60A, higher? |
| #13 Weatherproof enclosure | (asked only if location is exterior) |
| #17 Contractor license | C-10 contractor or owner-builder? |
| HB-3 Panel upgrade | Does this require a panel upgrade? |
| HB-4 Coastal CDP | What's your address? (parcel check: west of PCH?) |
| HB-5 Methane overlay | (parcel check from same address) |
| HB-6 AB 1236 OTC | (Claude determines if project qualifies — 200A service + dedicated 240V/50A + UL-listed + no subpanel upgrade + load calc OK → same-day OTC mandated) |

Compliance check output would be structured per the checklist. Submission guide identifies HB's dedicated "EV Charger" Accela category and flags the AB 1236 entitlement if applicable.

**Verdict:** ✓ Skill structure supports natural builder flow. ~12 intake questions, but many are conditional (only ask about CDP if address is coastal, only ask about outdoor weatherproof if mounted outside). A well-run conversation compresses this to 5-7 real questions.

---

## Water Heater — "Replacing my water heater in Huntington Beach"

Intake Claude would run:

| Plan-check item | Intake question |
|---|---|
| — | Fuel type — gas, electric, heat pump? |
| #19 Gas line sizing | (if gas) What's the BTU rating of the new unit? Existing gas line adequate? |
| #1 Venting system | (if gas) Replacement same-vent or new vent? |
| #2 Combustion air | (if gas, closet-located) What's the closet volume + combustion air setup? |
| #5 T&P discharge pipe | Where will the T&P relief terminate? (HB override: within 6" of floor or approved drain) |
| #6 Drain pan | Installation location — garage floor, attic, elevated? |
| #7 Expansion tank | Is there a PRV or backflow preventer on the water main? |
| #18 Vacuum relief | Is the WH above any fixture outlets (attic install)? |
| #23 Energy compliance | What's the UEF rating on the new unit nameplate? |
| #17 Contractor license | C-36 plumbing license or owner-builder? |
| HB-2 Methane overlay | What's your address? (parcel check) |
| HB-3 Gas-fired methane | (only if fuel=gas AND parcel is in overlay → HBFD clearance) |
| HB-4 Coastal new vent | (only if new exterior vent penetration in CZ) |

**Verdict:** ✓ Heat pump water heater in a typical garage install has the shortest intake — maybe 5 questions (fuel, size, location, address, contractor). Gas with a new vent in the methane overlay has the longest — 10-12 questions. The skill handles both.

Submission guide points applicants to the HB water heater installation handout (HB-6 documentation item) and flags HB's Accela plumbing category (HB-1).

---

## Open observation — inspection deferrals are harmless in builder mode

In builder mode, the "Deferred to Inspection" section of each skill ISN'T surfaced to the applicant during intake. The applicant doesn't need to front-load info about strapping/clearances/piping materials — the inspector verifies those in the field. The skill correctly limits builder-mode questions to what's actually needed for plan-check submittal. This matches how a real contractor would approach it: "get the paperwork right, the inspector sees the install."

---

## Success criteria for builder mode

- [x] Skill's Plan-Check Checklist provides an implicit intake question list
- [x] HB-specific additions appear in the intake flow when triggered (parcel, scope)
- [x] Inspection items NOT asked about in builder mode (correctly hidden)
- [x] Documentation items don't drive intake — referenced in submission guide
- [x] Conditional questions (outdoor weatherproof, overlay checks) handled gracefully

Skill structure is sound. Ready for live testing in Claude Code.
