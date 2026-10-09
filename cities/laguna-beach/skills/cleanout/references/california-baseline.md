# California Baseline — Cleanout

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Cleanout — State Regulatory Decision Engine

This skill contains California state-level sewer cleanout installation rules extracted from the 2025 California Plumbing Code (CPC), Title 24 Part 5. Cleanouts are access points in the drainage system for clearing blockages — this is one of the simplest permit types.

**What this covers**: State plumbing code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local fee schedules, or project-specific engineering. Use the city-level cleanout skill (e.g., `buena-park-cleanout`) for those.

### How to Use This Skill

Cleanout reviews are simple — there's one reference file and a 4-item checklist. Load `cleanout-requirements.md` for any cleanout question.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in → pass/fail out) | `cleanout-requirements.md` |
| **Cleanout type/location question** | `cleanout-requirements.md` |
| **Cleanout sizing question** | `cleanout-requirements.md` |
| **Any cleanout code question** | `cleanout-requirements.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order:

| # | Check | What to Verify | Code Section |
|---|-------|---------------|--------------|
| 1 | **Cleanout type appropriate?** | Two-way at building drain/sewer junction; one-way at direction changes >135° | CPC 707.1, 707.4 |
| 2 | **Location accessible?** | Above grade or floor level; not buried or blocked; clearance per 707.9 | CPC 707.7, 707.8, 707.9 |
| 3 | **Cleanout size correct?** | Same size as pipe served, up to 4" max | CPC 707.9, Table 707.1 |
| 4 | **Administrative** | Licensed C-36 (plumbing) contractor | State license law |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this installation

---

### Quick-Reference Tables

#### Cleanout Sizing (CPC Table 707.1)

| Pipe Size | Cleanout Size | Threads Per Inch |
|-----------|--------------|-----------------|
| 1-1/2" | 1-1/2" | 11-1/2 |
| 2" | 1-1/2" | 11-1/2 |
| 2-1/2" | 2-1/2" | 8 |
| 3" | 2-1/2" | 8 |
| 4" and larger | 3-1/2" | 8 |

#### Clearance Requirements (CPC 707.9)

| Pipe Size | Minimum Clearance in Front |
|-----------|---------------------------|
| 2" and under | 18" x 18" |
| Over 2" | 24" x 24" |

#### When Cleanouts Are Required (CPC 707.4)

| Condition | Cleanout Required |
|-----------|------------------|
| Upper terminal of horizontal drain | Yes — always |
| Every 100 feet of horizontal run | Yes |
| Direction change >135° (aggregate) | Yes |
| Horizontal drain <5 feet (not serving sinks/urinals) | Exception — may omit |
| Building drain/sewer junction | Yes — two-way cleanout |

---

### Key Principles

1. **Access is everything**: Cleanouts exist to provide access for clearing blockages. If a cleanout isn't accessible, it's useless. The code requires they be above grade, not buried, and with adequate clearance for rodding equipment.

2. **Two-way at the junction**: The cleanout at the building drain/sewer connection must be two-way (allows cleaning in both directions — toward the building and toward the sewer).

3. **Watertight and gastight**: All cleanouts must be watertight and gastight (CPC 707.3) — sewer gas must not escape.

4. **Under-floor rules**: Under-floor cleanouts must extend to or above the finished floor, OR extend to the outside of the building. If vertical clearance is less than 18", they must be within 5 feet of an access door, trap door, or crawl hole (CPC 707.9).
