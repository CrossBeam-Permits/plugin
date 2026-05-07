# Sidecar Tags — State-Level Execution Plan

**Date:** 2026-04-23
**Status:** Ready to execute in a fresh Claude Code session.
**Parent plan:** `plan-simple-permits-open-source-0422.md` (strategic context — optional to read).

---

## Purpose

Add a **tags.json sidecar** next to each simple-permit state skill so the open-source flatten pipeline can distinguish plan-check items from inspection items, and hard-fails from flags.

**Non-negotiable constraint:** DO NOT modify any existing `SKILL.md`, `CLAUDE.md`, or `references/*.md` files under `skills/california/` or `skills/cities/`. Production CrossBeam loads these today and must continue working unchanged. The sidecar is additive and read only by the open-source tooling.

**Scope of this execution:** tagging state-level simple-permit skills only. No flatten script, no city tagging, no SKILL.md edits. This is the pure "tags layer" — a one-time metadata pass that downstream tools will consume.

**Why state-level only:** tags on state skills propagate to every city × permit flatten automatically. Build once, reuse across all 275+ cities. City overlays get their own sidecars later (small overrides + city-specific additions) but not in this pass.

---

## Architecture

```
skills/california/{permit}/
├── SKILL.md              ← untouched. Production CrossBeam loads this.
├── CLAUDE.md             ← untouched
├── references/*.md       ← untouched
└── tags.json             ← NEW. Sidecar metadata. Open-source tooling only.
```

Production CrossBeam is oblivious to `tags.json`. Only the open-source flatten script (future work) reads it.

### Tag semantics

**`stage`** — when the check is enforced:
- `plan-check` — must be satisfied at submittal time (blocks permit issuance if failed)
- `inspection` — verified by the inspector in the field (not part of plan check corrections)
- `documentation` — paperwork or scope documentation only; no verifiable rule (e.g., contractor info)

**`severity`** — how serious:
- `fail` — blocks issuance; must be in the corrections letter
- `flag` — needs clarification, additional documentation, or reviewer judgment; not an automatic block
- `verify` — inspector confirms in the field (paired with `stage: inspection`)
- `advisory` — informational only; never fails or flags

Typical combinations:
- `plan-check` + `fail` → hard fail, corrections letter item
- `plan-check` + `flag` → needs documentation or reviewer judgment before issuance
- `inspection` + `verify` → deferred to field inspection
- `documentation` + `advisory` → informational pass-through

---

## Schema

Place the schema at `scripts/schemas/tags.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "tags.schema.json",
  "title": "CrossBeam Simple Permits — State Skill Tags",
  "type": "object",
  "required": ["version", "state_skill", "items"],
  "additionalProperties": false,
  "properties": {
    "version": { "type": "string", "enum": ["1.0"] },
    "state_skill": {
      "type": "string",
      "description": "Must match the frontmatter `name` field in the sibling SKILL.md.",
      "pattern": "^california-[a-z0-9-]+$"
    },
    "items": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "title", "stage", "severity"],
        "additionalProperties": false,
        "properties": {
          "id": { "type": "integer", "minimum": 1 },
          "title": {
            "type": "string",
            "description": "Short title — must reasonably match the checklist row in SKILL.md (exact match preferred; case-insensitive partial accepted by validator with a warning)."
          },
          "stage": { "enum": ["plan-check", "inspection", "documentation"] },
          "severity": { "enum": ["fail", "flag", "verify", "advisory"] },
          "notes": {
            "type": "string",
            "description": "Optional rationale — why this tag. Helps future maintainers."
          }
        }
      }
    }
  }
}
```

### Example — reroof

```json
{
  "version": "1.0",
  "state_skill": "california-reroof",
  "items": [
    { "id": 1,  "title": "Scope: Tear-off or Overlay",   "stage": "plan-check", "severity": "fail" },
    { "id": 2,  "title": "Fire Classification",          "stage": "plan-check", "severity": "fail" },
    { "id": 3,  "title": "Wind Speed Zone",              "stage": "plan-check", "severity": "flag", "notes": "Wind labeling required but often documented in product data sheet rather than form" },
    { "id": 4,  "title": "Material-Slope Compatibility", "stage": "plan-check", "severity": "fail" },
    { "id": 5,  "title": "Tile Weight / Structural",     "stage": "plan-check", "severity": "flag" },
    { "id": 6,  "title": "ICC-ESR Product Approval",     "stage": "plan-check", "severity": "flag" },
    { "id": 7,  "title": "Sheathing",                    "stage": "inspection", "severity": "verify" },
    { "id": 8,  "title": "Underlayment",                 "stage": "inspection", "severity": "verify" },
    { "id": 9,  "title": "Flashing",                     "stage": "inspection", "severity": "verify" },
    { "id": 10, "title": "Roof Drainage",                "stage": "inspection", "severity": "verify" },
    { "id": 11, "title": "Cool Roof Compliance",         "stage": "plan-check", "severity": "fail" },
    { "id": 12, "title": "Attic Ventilation",            "stage": "inspection", "severity": "verify" },
    { "id": 13, "title": "Insulation & Radiant Barrier", "stage": "inspection", "severity": "verify" },
    { "id": 14, "title": "Smoke & CO Alarms",            "stage": "inspection", "severity": "verify" },
    { "id": 15, "title": "Gas Vent Terminations",        "stage": "inspection", "severity": "verify" },
    { "id": 16, "title": "Waste Diversion",              "stage": "plan-check", "severity": "fail" },
    { "id": 17, "title": "Contractor Licensing",         "stage": "plan-check", "severity": "flag" }
  ]
}
```

---

## Scope — skills to tag

Tag these **22 state-level simple-permit skills**. All live under `skills/california/{permit}/`.

| # | Permit directory |
|---|---|
| 1 | block-wall |
| 2 | cleanout |
| 3 | deck-patio-repair |
| 4 | ev-charger |
| 5 | fence |
| 6 | fireworks-temp-use |
| 7 | hvac |
| 8 | ltia-demolition |
| 9 | panel-upgrade |
| 10 | patio-cover |
| 11 | pool-demolition |
| 12 | repipe |
| 13 | reroof |
| 14 | retaining-wall |
| 15 | rewire |
| 16 | siding-replacement |
| 17 | sign |
| 18 | solar |
| 19 | swimming-pool |
| 20 | temporary-power |
| 21 | water-heater |
| 22 | window-replacement |

### Explicitly excluded (do NOT tag)

- **Complex permits** (stay in CrossBeam paid product): `adu`, `kitchen-bath-remodel`, `multi-unit-residential`, `residential-addition`, `restaurant-ti`, `single-family-residential`
- **Overlays** (handled separately): `coastal-development`, `wildfire-wui`
- **Dev scratch dirs**: `reroof-workspace`

If any skill directory in the scope list above does not exist on disk, skip it and note the absence in the execution summary — do not create placeholder tags.

---

## Tagging heuristic

For each skill, read the full `SKILL.md` and classify every numbered checklist row using these rules:

**`plan-check` items** — rules that are enforced before permit issuance based on submittal data:
- Anything listed on the application form or required document
- Load calculations, sizing calculations, code path decisions
- Fire classification, material selections, product approvals
- Licensing, waste management plans, valuation

**`inspection` items** — rules physically verified in the field:
- Sheathing condition, framing, nailing schedules
- Flashing, underlayment install quality
- Alarm presence and age
- Gas vent terminations, clearances
- Ventilation NFA physical verification
- Grounding, bonding, physical clearances

**`documentation` items** — paperwork only, no verifiable rule:
- Contractor contact info
- Project description / scope narrative
- General code-path declarations

**Severity guidance:**
- `fail` = this being wrong means the permit cannot issue
- `flag` = reviewer needs something (doc, number, clarification) but not always a hard block
- `verify` = inspector's responsibility (paired with `stage: inspection`)
- `advisory` = informational, never blocks

When in doubt on severity, lean toward `flag` for plan-check items and `verify` for inspection items. Add a `notes` field explaining the call.

### Title field

Use the row title as it appears in the SKILL.md checklist table. Strip bold markers (`**...**`). If the row has a long descriptive name, use the first meaningful phrase (up to ~50 chars). The validator will warn if titles drift — that's intentional so renames get flagged in CI.

---

## Validator

Build at `scripts/validate-tags.ts` (TypeScript, runnable via `npx tsx` or `bun`). Purpose: detect drift between SKILL.md and tags.json, so future edits to either file surface mismatches in CI.

### What the validator does

For each `tags.json` under `skills/california/*/`:

1. Load and JSON.parse the tags file
2. Validate against the JSON schema (required fields, enum values)
3. Read the sibling `SKILL.md`
4. Parse all numbered checklist rows from SKILL.md (match rows like `| 1  | **Title** | ...` at the start of a line, tolerating whitespace)
5. Compare:
   - Every tag `id` must exist as a row in SKILL.md → **ERROR if missing**
   - Every numbered row in SKILL.md must have a tag → **WARN if missing** (so you can spot skills that need tagging)
   - Tag `title` should match the SKILL.md row title (case-insensitive, ignoring punctuation) → **WARN on mismatch**
6. Print a structured report per skill

### Output format

```
✓ california-reroof         17/17 rows tagged, 0 drift
✓ california-ev-charger     12/12 rows tagged, 0 drift
⚠ california-water-heater   8/9 rows tagged (row 7 "Drain Pan" untagged)
✗ california-solar          row id 14 in tags.json not found in SKILL.md

Summary: 21/22 skills clean, 1 warnings, 1 errors
```

Exit code 0 on clean (errors = 0). Exit 1 on errors.

### Parsing notes

The state SKILL.md files follow a consistent checklist table format:

```markdown
| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Scope: Tear-off or Overlay** | ... | CBC 1512.2 | ... |
| 2 | **Fire Classification** | ... | ... | ... |
```

Regex pattern to extract IDs + titles:

```
/^\|\s*(\d+)\s*\|\s*\*\*([^*]+)\*\*/gm
```

Group 1 = numeric ID. Group 2 = bold title.

Some skills may have slightly different formatting — handle gracefully. If a SKILL.md has no parseable checklist, report and skip (don't crash).

---

## Deliverables

1. **`scripts/schemas/tags.schema.json`** — JSON schema file.
2. **22 × `tags.json` files** — one per simple-permit state skill listed above.
3. **`scripts/validate-tags.ts`** — the validator.
4. **Clean validator run** — `npx tsx scripts/validate-tags.ts` exits 0 with the 22 skills all showing ✓ or ⚠ (no ✗).
5. **Summary report** — brief writeup at the end of the execution summarizing what was tagged, any judgment calls made, and any SKILL.md quirks encountered.

---

## Non-goals (do NOT do these in this pass)

- ❌ Modifying any SKILL.md file
- ❌ Modifying any existing CLAUDE.md or reference file
- ❌ Adding tags to city overlays (`skills/cities/*/*/tags.json`)
- ❌ Building the flatten script
- ❌ Building the open-source plugin shell
- ❌ Tagging complex permits (ADU, SFR, multi-unit, residential-addition, restaurant-TI, kitchen-bath)
- ❌ Tagging overlay-only skills (coastal-development, wildfire-wui)
- ❌ Touching `frontend/`, `server/`, `data/` — this work is purely in `skills/` and `scripts/`
- ❌ Running the batch onboarder or any long-running job
- ❌ Committing to git — leave changes uncommitted for review

---

## Execution approach

1. Read this plan doc in full first.
2. List the 22 target directories and verify each exists.
3. For each skill, read SKILL.md, classify every numbered checklist row, write `tags.json`.
4. Build the JSON schema file.
5. Build the validator script.
6. Run the validator — fix any errors (should be rare if titles are copied carefully).
7. Produce the summary report.

**Parallelization:** the 22 tagging tasks are independent. Spawn multiple sub-agents (one per skill, or batches of 3-5) to tag in parallel. Validator and schema can be built in parallel with the tagging work.

**Time estimate:** 2-3 hours if done sequentially. Under 1 hour with parallel sub-agents.

---

## Execution prompt

Paste this into a fresh Claude Code session at `~/projects/crossbeam`:

```
Execute the sidecar tagging plan at:
docs/plans/active/plan-sidecar-tags-0423.md

Read it in full first. Then build:
1. JSON schema at scripts/schemas/tags.schema.json
2. tags.json sidecars for the 22 state-level simple-permit skills listed in the plan
3. Validator at scripts/validate-tags.ts (TypeScript, runnable with `npx tsx`)
4. A clean validator run

Hard constraints (from the plan):
- DO NOT modify any SKILL.md, CLAUDE.md, or references/*.md files
- DO NOT tag city overlays, complex permits, or overlay-only skills
- DO NOT build the flatten script or plugin shell
- DO NOT commit to git — leave changes uncommitted
- DO use parallel sub-agents to tag skills concurrently (one agent per 3-5 skills)

Deliverables: the schema file, 22 tags.json files, the validator, and a short summary report describing what you tagged, any judgment calls made, and any SKILL.md parsing quirks you encountered.

Start by reading the plan doc in full.
```

---

*Filed mirror at `~/projects/crossbeam-simple-permits/PLAN-sidecar-tags.md`.*
