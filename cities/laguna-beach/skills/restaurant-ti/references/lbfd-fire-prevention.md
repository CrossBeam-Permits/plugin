# Laguna Beach — LBFD Fire Prevention for Restaurant TI

**Operative code:** LBMC Title 15 (Fire Code adopted, local amendments); Sec. 15.01 (2025 CFC adoption); amendments to NFPA 13, NFPA 72, NFPA 96.
**Operative agency:** **Laguna Beach Fire Department (LBFD)** — Laguna Beach operates its OWN fire department. Do NOT route to OCFA.

**Contact:** fireprevention@lagunabeachcity.net / (949) 497-0352.

---

## Critical Distinction From Other OC Cities

Most Orange County cities are served by OCFA, which is the agency captured in a CrossBeam reference that is not included in this plugin. **Laguna Beach is one of the few OC cities with a municipal fire department.** Therefore:

- **DISCARD** the entire `## Overrides — OCFA (Fire Authority)` section of the OC overlay for Laguna projects (PR335 paths, PR630/PR635 simplified sprinkler paths, OCFA B-01 fire access, OCFA Fire Alarm System Coversheet, etc.).
- **KEEP** the OCHCA Environmental Health portion of the OC overlay — OCHCA still reviews every food facility in Orange County including those in Laguna.
- **APPLY** LBFD's submittal mechanics documented below.

---

## What LBFD Reviews

LBFD Fire Prevention plan-checks all multi-family, commercial, and industrial new construction and remodel projects prior to building permit issuance. For a restaurant TI this covers:

| Item | Submittal |
|------|-----------|
| Type I hood + grease duct | Mechanical plan set, submitted together as one application with architectural |
| Hood fire suppression (UL-300 wet chemical / Ansul) | Deferred submittal under separate cover, stamped by fire-suppression contractor |
| Fire sprinkler additions / modifications | Deferred submittal, NFPA 13 |
| Fire alarm | Deferred submittal, NFPA 72 |
| Class K fire extinguisher placement | Note on architectural |
| FDC location, size, signage | Site plan |
| Hydrant location and flow | Site plan + hydrant flow test report |
| Knox box, Knox switch | Site plan |
| Access roads, turning radii | Site plan |
| Address numbers, character size | Exterior elevations |

---

## LBMC Local Amendments (Title 15)

### Sprinkler Monitoring — Title 15 amended NFPA 72 Sec. 6.16.1
All sprinkler systems must have **24-hour UL-certified central station monitoring**. This includes:

- Waterflow alarm
- Tamper / supervisory on every control valve
- Phone-line or cellular communicator with battery backup
- Annual confidence test certification

This is stricter than the state baseline (which permits local alarm on certain small systems) and applies to every sprinkler system regardless of size.

### FDC Specifications — LBMC-amended NFPA 13 Sec. 16.12.1
| Requirement | LBMC standard |
|-------------|---------------|
| Minimum inlets | **Two 2½" inlets** |
| Color | **OSHA red** |
| Distance from hydrant | **≤150 ft from a public hydrant** |
| Sign | Per LBFD detail |
| Plumb | Vertical orientation, accessible to fire apparatus |

### Hydrant Flow Test — LBMC Sec. 28.1.3
Sprinkler system design submittals must include a **hydrant flow test ≤6 months old.** Older tests are not acceptable. Test must be from a hydrant within reasonable proximity and on the same loop serving the building.

### Sprinkler Scope Expansion — LBMC Sec. 903.2 amended
LBMC Sec. 903.2 expands sprinkler requirements beyond the state baseline — sprinklers required throughout all new buildings and structures regardless of size in many configurations. New restaurants in shell buildings should treat sprinklers as required. For existing-building retrofits see `sprinkler-retrofit-triggers.md`.

### Group R Retrofit — LBMC Title 15 Sec. 1103.5.4
Mixed-use buildings with residential above the restaurant: see `sprinkler-retrofit-triggers.md`. Scope-based trigger (50% of the building or an added story; 50% exterior alone is UNSETTLED) fires retrofit of the entire R fire area independent of building valuation.

---

## Type I Hood + Grease Duct Submittal

| Item | Detail |
|------|--------|
| Hood location | Show on mechanical floor plan + reflected ceiling |
| Hood overhang | Min 6" beyond cooking surface on all open sides (CMC 508.4.1) |
| Hood-to-cooking distance | Max 4 ft vertical (CMC 508.3) |
| Exhaust rate | Per CMC Table 508.5.1 by duty class (typical heavy duty 400 CFM/linear ft wall canopy) |
| Grease duct | Welded liquid-tight, min 16 ga (carbon) or 18 ga (SS), 1/4" per ft slope (CMC 510) |
| Duct clearance | Per CMC 510.7 to combustibles, or factory shaft-wrap rated assembly |
| Exhaust termination | 10 ft from operable windows / intakes, 3 ft above roof (CMC 510.8); LBFD may add screening/setback for visibility/odor under DR conditions |
| Makeup air | Sized to keep building negative pressure ≤0.02" wc (CMC 511.3) |
| Wash-down / cleaning access | Per CMC 510.5 and NFPA 96 |

---

## Hood Fire Suppression (UL-300 / Ansul)

| Parameter | Standard |
|-----------|----------|
| System type | UL-300 wet chemical (NOT CO2) |
| Actuation | Auto + manual |
| Manual pull height | 42-48" AFF |
| Manual pull location | Within 10 ft of egress from kitchen, within 25 ft of hood edge (LBFD adopts OCFA-style placement standard in practice) |
| Equipment shutoff | Gas and electric cooking equipment must auto-shutoff on system activation |
| Class K extinguisher | Within 30 ft of cooking equipment (CFC 906) |
| Glass baffles | Between fryers and surface flame cooking (CMC 509.5) |
| Submittal | Deferred, stamped by fire-suppression contractor |

### LBFD UL-300 Acceptance Testing Checklist (verbatim, Apr 27 2026 rev)

Local copy: the City source document (not included in this plugin). Issued by the Fire Marshal. The checklist is for the **licensed C-16 fire protection contractor** to prep for the LBFD inspection.

**Day-of inspection requirements:**

1. **Cooking operations cease** — All cooking and food service related to, under, or near the Type 1 cook hood shall cease operations. All food shall be removed from the area.
2. **Equipment cool and accessible** — All equipment and surfaces shall be cool and fully accessible.
3. **Hoods and ducts clean** — No grease buildup.
4. **Approved plans on site** — LBFD-approved stamped/signed plans AND a complete copy of the Technical Design and Installation Manual must be on site for all required inspections.
5. **All equipment exposed** — Contractor shall have all equipment, devices, piping, supports, and related items exposed and accessible. Appropriate and safe ladders / lifts must be provided.

**Acceptance test mechanics:**

6. **Dual-actuation test** — Final acceptance test consists of initiating each system by both **manual** (pull station) AND **automatic** (fusible link) means.
7. **Gas shut-off** — Location and type of gas shut-off valves for appliances under the Type 1 hood shall correlate with the plans. Gas to all appliances under the hood must shut down automatically on system initiation. Reset must be by manual means only and the valve must be readily accessible. **Pre-test required.**
8. **Electrical shut-off** — All electrical to and under the cook hood must shut off on system initiation, including receptacles, lights, switches, appliances, timers, controls. **Make-up air must shut off.** **Hood exhaust fan must stay on** (unless fan shut-down is required by a listed component of the ventilation system or by the design of the extinguishing system). Reset by manual means only. **Pre-test required.**
9. **Make-up air interlock** — Supply / make-up air must be provided equal to exhaust. Make-up air must be electrically interlocked with exhaust (switching one on activates the other).
10. **Building fire alarm interlock** — If a protected-premises fire alarm system is installed, the fire suppression system must transmit alarm signals to it.

**Deviations from approved plans:** Any deviation requires a **plan resubmittal for LBFD review and re-approval BEFORE calling for inspection**. Do not field-modify and expect pass at inspection.

**Reviewer FAIL/FLAG:**
- FAIL if plans rely on CO2 system, not UL-300 wet-chem.
- FAIL if deferred submittal not stamped by C-16 contractor with Technical Design & Installation Manual referenced.
- FAIL if gas-valve auto-shutoff or under-hood electrical interlock not shown on plans.
- FLAG if make-up air interlock not explicit on the M-sheets or hood schedule.

---

## Fire Alarm

| Item | Standard |
|------|----------|
| Code | NFPA 72 (LBMC-amended) |
| Monitoring | 24-hr UL central station (Sec. 6.16.1) |
| Triggers | Sprinkler waterflow, supervisory on every valve, hood suppression activation, manual pull (if required by occupancy) |
| Annunciator | Required in front lobby / main entrance when FACU not in initial-response area |
| Submittal | Deferred, stamped by C-10 fire-alarm contractor or qualified PE |
| Plans format | 1/8" = 1' per NFPA 72 7.4 |

---

## Fire Access & Site Items

| Item | LBFD standard |
|------|---------------|
| Address characters | Min 6", 1" stroke, visible from street |
| Knox box | Required at main entrance (LBFD-issued key) |
| Knox switch | On automatic gates if present |
| Hydrant proximity | Min 40 ft from building; 4" outlet facing fire lane; 3 ft clear; blue reflective road marker |
| Fire flow | Min 1,500 GPM for 2 hr (typical commercial); 50% reduction if fully sprinklered |
| Fire lane | If exterior wall of first story >150 ft from public roadway |

---

## Coordination With Building & Health

| Touchpoint | Detail |
|------------|--------|
| Hood mechanical plans | Submitted together with architectural to Building Division; LBFD reviews the mechanical set |
| Hood suppression | Separate deferred submittal to LBFD |
| Sprinkler / alarm | Separate deferred submittals to LBFD |
| OCHCA approval | Required before building permit issuance; OCHCA reviews the hood from a health perspective (grease drainage to floor sink, hood material, lighting) and LBFD reviews from a fire perspective |
| Equipment changes during construction | Any change in cooking medium, position, or equipment type triggers re-submittal to LBFD + OCHCA + Building |

---

## Output Findings

- **PASS** — All LBFD-required items shown; submittals filed or scheduled as deferred; hydrant test ≤6 mo.
- **FAIL** — Missing required deferred submittal, hood overhang/exhaust/duct spec wrong, no 24-hr monitoring noted, FDC not per LBMC standard, hydrant test stale or absent.
- **FLAG** — Hood schedule / suppression provider TBD; flow test pending; need LBFD coordination meeting.
- **N/A** — Pure interior TI with no cooking equipment, no sprinkler/alarm modifications (rare for restaurant scope).
