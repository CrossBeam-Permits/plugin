# CRC §R309 — Automatic Sprinkler Systems (State-Level Exemption — NOT a Trip Wire)

> **Source:** 2025 CRC § R309 (Title 24 Part 2.5, effective January 1, 2026).
> **Authority:** 2025 California Residential Code (CRC), Title 24 Part 2.5
> **Effective:** January 1, 2026

⚠️ **This is a CORRECTION reference, not a trip wire.** The original residential-remodel plan draft (and many builder/reviewer assumptions) treated CRC R313.2 as a state-level sprinkler retrofit trigger. **It is not.** California's 2025 CRC is renumbered relative to IRC and contains an explicit exemption for existing un-sprinklered SFRs.

---

## Numbering correction (CA CRC vs IRC)

In the **2025 California Residential Code**:
- **§R309** = "Automatic Sprinkler Systems" (this section)
- **§R313** = "Ceiling Height" (NOT sprinklers)

In the **base IRC**:
- **R309** = "Garages and Carports" / similar
- **R313** = "Automatic Sprinkler Systems"

California renumbered. **Any reference to "CRC R313 sprinklers" in California is wrong.** The correct California citation is **CRC §R309**.

---

## CRC §R309.1 — Townhouses (verbatim)

> *"R309.1 Townhouse automatic sprinkler systems.*
> *An automatic sprinkler system shall be installed in townhouses.*
> *Exception: An automatic sprinkler system shall not be required where additions or alterations are made to existing townhouses that do not have an automatic sprinkler system installed."*

**Source:** chapter-3 R309 file lines 12–16.

**Plain reading:** new townhouses require sprinklers. Existing un-sprinklered townhouses are **exempt** when undergoing additions or alterations. There is **no state-level townhouse retrofit trigger**.

---

## CRC §R309.2 — One- and Two-Family Dwellings (verbatim)

> *"R309.2 One- and two-family dwellings automatic sprinkler systems.*
> *An automatic sprinkler system shall be installed in one- and two-family dwellings.*
> *Exceptions:*
> *1. An automatic sprinkler system shall not be required for additions or alterations to existing buildings that are not already provided with a sprinkler system.*
> *2. Accessory Dwelling Unit, provided that all of the following are met:*
>    *2.1. The unit meets the definition of an Accessory Dwelling Unit as defined in the Government Code Section 66313.*
>    *2.2. The existing primary residence does not have automatic fire sprinklers.*
>    *2.3. The accessory detached dwelling unit does not exceed 1,200 square feet in size.*
>    *2.4. The unit is on the same lot as the primary residence."*

**Source:** chapter-3 R309 file lines 24–31.

**Load-bearing rule (Exception 1):**

> *"An automatic sprinkler system shall not be required for additions or alterations to existing buildings that are not already provided with a sprinkler system."*

**Plain reading:** if an existing SFR or duplex was built without sprinklers (and almost all California homes built before ~2011 were), **no addition or alteration triggers a state-level sprinkler retrofit**. Period. There is no scope-percentage threshold in state law that flips this exemption off.

---

## What this means for the residential-remodel skill

### The state-level rule is silence-as-exemption
- A whole-house gut remodel of an un-sprinklered SFR built in 1965 → **no state sprinkler retrofit required.**
- A 2,500 sf addition to an un-sprinklered SFR → **no state sprinkler retrofit required.**
- A new ADU on a lot with un-sprinklered primary residence (≤1,200 sf, same lot, GC §66313 ADU) → **no sprinkler required for the ADU under CRC §R309.2 Exception 2.**

### Sprinkler retrofit triggers exist ONLY at the city level

Many California cities and counties have local fire-code amendments under the California Fire Code §1103 / Health and Safety Code §13869.7 framework that **add** sprinkler retrofit triggers beyond CRC §R309. These are **local overlays** and must be invoked through the city skill, not the state skill.

**Examples of city overlays that DO trigger sprinkler retrofit:**
- **Laguna Beach LBMC Title 15 §1103.5.4** — *"An automatic sprinkler system installed in accordance with Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring a building permit that involves alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories."* (Cited from a CrossBeam reference that is not included in this plugin overlay; also tracked in the City source document (not included in this plugin).)
- Other coastal cities and high-risk wildfire jurisdictions have similar amendments.

**The skill must:**
1. Apply the state R309 exemption as the default — no state-level retrofit trigger.
2. **Always check for a city overlay** in the city skill (e.g., `../SKILL.md`).
3. Output language must clearly state: *"No state-level sprinkler retrofit triggered (CRC §R309.2 Exception 1). Local jurisdiction may impose a retrofit trigger — see city overlay."*

### What about CEBC §904.1?

CEBC §904.1 (within Chapter 9, applicable to Level 3 alterations) says: *"An automatic sprinkler system shall be provided in accordance with Section 903 of the California Building and California Fire Codes."*

This is a **reference** to CBC/CFC §903 — it does not itself create a retrofit trigger. CBC/CFC §903 sprinkler thresholds reach back to occupancy classifications and the underlying CRC for one- and two-family dwellings. The CRC §R309.2 Exception 1 exemption controls for SFR/duplex. For Group R-2/R-3 multi-family, CBC/CFC §903.2.8 requirements apply.

---

## Output checklist for sprinkler analysis

| # | Check | What to Verify | Source |
|---|-------|----------------|--------|
| SP-1 | Building occupancy | SFR (R-3) / townhouse / duplex / multi-family / ADU | Cover sheet |
| SP-2 | Existing sprinkler status | Is the building already sprinklered? | Existing-conditions plan |
| SP-3 | If un-sprinklered SFR/townhouse → CRC §R309 Exception 1 | State retrofit not required | This reference |
| SP-4 | If new ADU → CRC §R309.2 Exception 2 check | Verify ≤1,200 sf, same lot, primary unsprinklered, GC §66313 ADU | This reference |
| SP-5 | City overlay check | Does the city have a sprinkler retrofit ordinance? Invoke city skill. | City skill (e.g., a CrossBeam reference that is not included in this plugin) |
| SP-6 | Output framing | "No state retrofit trigger; check city overlay" — never say "no sprinklers required" without the city check | Skill output discipline |

---

## Common errors to avoid

1. **Citing "CRC R313" for sprinklers in California.** Wrong — R313 in CA is ceiling height. Use R309.
2. **Inventing a "≥50% walls AND ≥50% roof in 1 yr" state retrofit trigger.** This is the historical IRC R313.2 language; California **explicitly amended it out** when adopting the IRC. Stating this as a state requirement is a hallucination.
3. **Treating silence in CEBC §904.1 as a retrofit mandate.** §904.1 is a pointer to CBC/CFC §903, which itself defers to occupancy-specific thresholds. SFR/duplex retrofit is governed by CRC §R309.
4. **Failing to invoke the city overlay.** The state silence is exactly what the city overlay fills. Output without checking the city skill is incomplete.

---

## Cross-references
- Source: 2025 CRC § R309.
- City overlay (Laguna Beach example): consult the current Laguna Beach municipal fire-prevention code, Title 15, when that local overlay is in scope.
- CEBC §904.1 reference: `cebc-alteration-levels.md` (under Level 3 — Fire Protection).
