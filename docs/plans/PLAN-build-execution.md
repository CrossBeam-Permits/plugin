# CrossBeam Simple Permits — Build Execution Spec

**Date:** 2026-05-06
**Status:** Ready to execute in a fresh Claude Code session at `~/projects/crossbeam`.
**Parent plans:**
- `PLAN.md` — strategy
- `PLAN-flatten-and-distribute.md` — architecture (per-city sub-plugins in monorepo)
- `PLAN-sidecar-tags.md` — state-level tags layer (already executed, clean)

**GitHub destination:** `https://github.com/CrossBeam-Permits/plugin` (empty repo, ready to receive first push)

**Local working dir:** `~/projects/crossbeam-simple-permits/` — becomes the local clone of `CrossBeam-Permits/plugin` after this spec runs.

---

## Goal

Bulk-flatten all 22 California simple-permit skills × ~485 cities into a Claude Code marketplace monorepo. First push to `CrossBeam-Permits/plugin` lands a working public marketplace with city sub-plugins.

**Math:** 22 permits × ~485 cities = ~10,670 flattened `SKILL.md` files. Plus 495 `plugin.json` manifests, 1 `marketplace.json`, 1 LICENSE, README, disclaimer.

---

## The 22 simple permits (canonical list)

```ts
const SIMPLE_PERMITS = [
  "block-wall", "cleanout", "deck-patio-repair", "ev-charger", "fence",
  "fireworks-temp-use", "hvac", "ltia-demolition", "panel-upgrade", "patio-cover",
  "pool-demolition", "repipe", "reroof", "retaining-wall", "rewire",
  "siding-replacement", "sign", "solar", "swimming-pool", "temporary-power",
  "water-heater", "window-replacement",
];
```

These match `skills/california/{permit}/` directories (all 22 confirmed present and tagged).

---

## Workstream A — Modify `scripts/flatten-skill.ts`

Two surgical edits to the existing script at `~/projects/crossbeam/scripts/flatten-skill.ts`.

### A1. Make city per-permit `SKILL.md` optional

**Current (lines 287–288):**
```ts
const citySkill = readFileOpt(path.join(cityDir, "SKILL.md"));
if (citySkill === null) throw new Error(`city SKILL.md missing: ${cityDir}`);
```

**Change to:**
```ts
const citySkill = readFileOpt(path.join(cityDir, "SKILL.md")); // may be null
```

Then guard all downstream uses of `citySkill`/`cityBody` so the script renders cleanly when only `CITY.md` + `meta.json` exist (no per-permit overlay).

**Behavior when city skill is missing:**
- State checklist + state tags inlined as the baseline
- City universal info (portal URL, fire agency, code prefix, building dept phone, overlays from CITY.md + meta.json) in the `## City Info` block
- Empty `## Key {City} deltas vs state baseline` section — omit the section header entirely if no deltas
- All severity/stage routing inherits from state tags

### A2. Parse city `SKILL.md` delta tables when present

The city per-permit SKILL.md (when present) has two structured tables we currently ignore:

**Table 1 — `## Overrides`** (modifies a state checklist item):
```markdown
| State Checklist Item | City Rule | Code Reference | Notes |
|---|---|---|---|
| Roof fire classification (Check #2) | **Class B minimum**... | HBMC Ch. 17.04 | ... |
```
Extract the state check # from the first column (regex: `Check #(\d+[a-z]?)`), then the city rule prose, code, and notes.

**Table 2 — `## City-Specific Additions`** (new check not in state):
```markdown
| # | Check | Requirement | Code Reference |
|---|---|---|---|
| 1 | Class B minimum — explicit confirmation | Verify... | HBMC Ch. 17.04 |
```
Extract id, title, requirement (becomes `whatToVerify`), code.

**Stage/severity defaults when parsed from SKILL.md tables (no city tags.json):**
- Overrides: inherit state's stage/severity (override is *content*, not severity tier)
- Additions: default `stage: plan-check, severity: flag` (conservative — needs reviewer judgment, not an auto-fail)

**Layering rule:** if `city tags.json` ALSO exists, it wins on stage/severity (it's the curated layer). The SKILL.md table parser is the fallback that gives every city deltas without requiring hand-tagging.

**Robustness:** table headers vary slightly across batch-onboarded cities. Be tolerant — if a table can't be parsed, log a warning and skip *that table* (not the whole skill). The goal is graceful degradation across 495 cities.

### A3. Change output path

**Current:**
```ts
const OUTPUT_BASE = path.join(os.homedir(), "projects", "crossbeam-simple-permits", ".claude", "skills");
// outputs: ~/projects/crossbeam-simple-permits/.claude/skills/{city}-{permit}/SKILL.md
```

**Change to:**
```ts
const OUTPUT_BASE = path.join(os.homedir(), "projects", "crossbeam-simple-permits", "cities");
// outputs: ~/projects/crossbeam-simple-permits/cities/{city}/skills/{permit}/SKILL.md
```

Adjust `outDir` construction in `flattenSkill()` accordingly. References dir likewise moves to `cities/{city}/skills/{permit}/references/`.

Keep the skill `name` frontmatter as `{city}-{permit}` so installed skills are uniquely namespaced when a reviewer installs multiple cities.

---

## Workstream B — `scripts/flatten-all.ts` (NEW)

Driver script that runs flatten across the matrix.

```ts
#!/usr/bin/env -S npx tsx

import * as fs from "node:fs";
import * as path from "node:path";

const SIMPLE_PERMITS = [/* see canonical list above */];
const CITIES_DIR = path.resolve(__dirname, "..", "skills", "cities");

const cities = fs.readdirSync(CITIES_DIR, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .filter(d => !d.name.endsWith("-county"))   // counties don't issue simple permits — exclude
  .map(d => d.name);

let success = 0, failed = 0, skipped = 0;
const errors: string[] = [];

for (const city of cities) {
  for (const permit of SIMPLE_PERMITS) {
    try {
      // call flatten function directly (refactor flatten-skill.ts to export)
      flattenSkill(city, permit);
      success++;
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      errors.push(`${city}/${permit}: ${msg}`);
      failed++;
    }
  }
}

console.log(`\n${success} flattened, ${failed} failed, ${skipped} skipped`);
if (errors.length) console.log(errors.slice(0, 20).join("\n"));
```

**Key changes to flatten-skill.ts to support this driver:**
- Export `flattenSkill(citySlug, permitSlug)` from the module instead of only running via `main()`
- Keep the CLI entry point intact for one-off testing

**Expected output:** ~10,670 successful flattens. Any failures surface in the error log for triage.

**Performance:** This is sequential, file-IO bound. ~10K writes ≈ 60–120 seconds total. No need to parallelize.

---

## Workstream C — `scripts/generate-plugin-manifest.ts` (NEW)

For each city directory under `~/projects/crossbeam-simple-permits/cities/`, emit `.claude-plugin/plugin.json`.

```ts
{
  "name": "{city-slug}",
  "version": "1.0.0",
  "description": "Plan-check skills for {City Display Name}, CA. 22 simple permit types ({list a few}) with {codePrefix} local amendments. Tier {N}.",
  "author": {
    "name": "Onboard Dot AI LLC",
    "url": "https://github.com/CrossBeam-Permits"
  },
  "homepage": "https://github.com/CrossBeam-Permits/plugin/tree/main/cities/{city-slug}",
  "keywords": ["california", "{city-slug}", "{county-slug if known}", "plan-check", "permits", "{codePrefix}"]
}
```

**Inputs:** `skills/cities/{city}/meta.json` (displayName, codePrefix, fireAgency).

**Tier derivation (initial):** Tier 1 = `huntington-beach`, `buena-park`, `costa-mesa`, `laguna-beach` (hardcoded list). All others = Tier 3. Refine post-launch.

**County enrichment (optional, best-effort):** check if there's a city→county mapping in `data/` or `frontend/`; if found, include in keywords. If not, skip — not blocking.

---

## Workstream D — `scripts/generate-marketplace.ts` (NEW)

Walks `~/projects/crossbeam-simple-permits/cities/`, emits root `.claude-plugin/marketplace.json` listing every city as a discrete plugin.

```ts
{
  "name": "crossbeam-permits",
  "owner": {
    "name": "Onboard Dot AI LLC",
    "url": "https://github.com/CrossBeam-Permits"
  },
  "metadata": {
    "version": "1.0.0",
    "description": "Open-source plan-check skills for every California city. 22 simple permit types × 495 cities."
  },
  "plugins": [
    {
      "name": "huntington-beach",
      "source": { "source": "github", "type": "path", "path": "cities/huntington-beach" },
      "description": "Huntington Beach, CA — 22 simple permit types. Tier 1 (vetted).",
      "keywords": ["california", "huntington-beach", "orange-county"]
    }
    // ... 494 more entries
  ]
}
```

**IMPORTANT:** Verify the exact `source` schema for path-based sub-plugins by reading current Claude Code plugin marketplace docs (https://code.claude.com/docs/en/plugin-marketplaces.md). The above is best-guess — adjust to match the canonical schema before push.

---

## Workstream E — Repo bootstrap

Restructure `~/projects/crossbeam-simple-permits/` to become the local clone of `CrossBeam-Permits/plugin`.

### E1. Clean up legacy artifacts
- Delete `.claude/skills/huntington-beach-reroof/`, `.claude/skills/huntington-beach-ev-charger/`, `.claude/skills/huntington-beach-water-heater/` (old flatten output paths — superseded by new `cities/{city}/skills/{permit}/` location)
- Move `PLAN*.md` files to `docs/plans/` (keep them in repo as design history)
- Keep `README.md`, `HB_ReRoof_Application_MikeBrown.pdf` etc. — clean up later

### E2. Add repo scaffolding
- `.gitignore` — node_modules, .DS_Store, .env*, *.log
- `LICENSE` — Apache-2.0 (working assumption pending legal — flag in README that final license TBD)
- `NOTICE` — "CrossBeam Simple Permits — © 2026 Onboard Dot AI LLC. Informational use only; not legal advice. Jurisdiction governs."
- `README.md` — see template below
- `docs/disclaimer.md` — full disclaimer language
- `.claude-plugin/marketplace.json` — generated by Workstream D
- `cities/` — generated by Workstream B

### E3. README.md template

```markdown
# CrossBeam Simple Permits

Open-source plan-check skills for every California city. 22 simple permit types × 495 cities. Free for cities, builders, and homeowners.

## Install

```
/plugin marketplace add CrossBeam-Permits/plugin
/plugin
# search for your city, install
```

## What you get

Per-city plugins with skills for: reroof, EV charger, water heater, HVAC, solar, panel upgrade, fence, patio cover, window replacement, repipe, deck/patio repair, retaining wall, block wall, siding, sign, swimming pool, pool demolition, LTIA demolition, cleanout, fireworks (temp use), rewire, temporary power.

Each skill works in two modes: **Builder/Homeowner** (intake → compliance check → submission guide) and **City Reviewer** (run plan-check checklist against a submittal → tight corrections output).

## Tier labels

- **Tier 1** — hand-reviewed, vetted end-to-end (HB, BP, Costa Mesa, Laguna Beach)
- **Tier 2** — onboarder-generated, spot-checked
- **Tier 3** — onboarder-generated, not yet human-reviewed

## Contributing

Cities, contractors, and reviewers welcome. See CONTRIBUTING.md.

## Disclaimer

Informational use only. Not legal advice. Jurisdiction governs. See docs/disclaimer.md.

## License

Apache-2.0 (working assumption — final license pending legal review)
```

### E4. Git init + first push

```bash
cd ~/projects/crossbeam-simple-permits
git init -b main
git remote add origin https://github.com/CrossBeam-Permits/plugin.git
git add -A
git commit -m "Initial public release: 495 California city plugins, 22 simple permits each"
git push -u origin main
```

---

## Sequencing

```
PARALLEL (can run simultaneously):
  A: Modify flatten-skill.ts (parser fix + output path)
  B: Write flatten-all.ts driver
  C: Write generate-plugin-manifest.ts
  D: Write generate-marketplace.ts

SEQUENTIAL (gated by all of A–D):
  1. Run flatten-all.ts                → produces cities/{city}/skills/{permit}/...
  2. Run generate-plugin-manifest.ts   → adds .claude-plugin/plugin.json per city
  3. Run generate-marketplace.ts       → adds root marketplace.json
  4. Validate: spot-check Tier 1 cities (HB, BP, CM, LB) — read 3-5 random skills, sanity check
  5. Validate: confirm 22 skills in HB plugin (hand check)
  6. Bootstrap repo (E1, E2, E3)
  7. Git init + push (E4)
```

---

## Validation gates (must pass before push)

- [ ] `flatten-all.ts` runs to completion. Failures < 5% of total (i.e., < ~545). Failed pairs logged with reason.
- [ ] `cities/huntington-beach/skills/` contains all 22 permit skill dirs
- [ ] `cities/huntington-beach/skills/reroof/SKILL.md` includes the HB Class B / 50% / Coastal / Methane deltas (parsed from city SKILL.md tables — proves parser works)
- [ ] `cities/costa-mesa/skills/reroof/SKILL.md` exists, has Costa Mesa portal/fire info, no HB deltas (proves city isolation)
- [ ] `cities/sacramento/skills/reroof/SKILL.md` exists with state baseline + Sacramento universal info (proves "no city skill" path works)
- [ ] `marketplace.json` lists ≥ 480 city plugins (counties excluded — only incorporated cities)
- [ ] Each city has `.claude-plugin/plugin.json` with valid name + description
- [ ] Local install test: `cd ~/test-claude && claude` → `/plugin marketplace add ~/projects/crossbeam-simple-permits` → `/plugin` shows the menu → install `huntington-beach` → restart → verify HB skills available

---

## Non-goals (do NOT do in this pass)

- ❌ Do NOT modify any `skills/california/` or `skills/cities/` source content (they're CrossBeam paid-product source-of-truth — read-only here)
- ❌ Do NOT write hand-curated city `tags.json` files (Tier 1 polish is a separate workstream)
- ❌ Do NOT build the `/cb:batch-review` slash command (that's the next workstream)
- ❌ Do NOT build synthetic test fixtures or automated review harness (separate workstream)
- ❌ Do NOT submit to Anthropic marketplace (week behind public push)
- ❌ Do NOT push to `main` until all validation gates pass

---

## Locked decisions

- **Company:** Onboard Dot AI LLC
- **Brand:** CrossBeam Permits
- **Domain:** crossbeam-permits.com
- **License:** Apache-2.0 (text in `LICENSE`, attribution paragraph in `NOTICE`)
- **Per-skill footer in flattened SKILL.md (replace existing footer):**
  ```
  *Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
  *Informational use only; not legal advice; jurisdiction governs.*
  ```
- **MODE B reviewer output template — add as last line of the example block:**
  ```
  —
  Generated by CrossBeam Permits · crossbeam-permits.com
  ```
- **NOTICE file content:**
  ```
  CrossBeam Permits
  Copyright 2026 Onboard Dot AI LLC

  This product is brand "CrossBeam Permits" (crossbeam-permits.com), a product of Onboard Dot AI LLC.

  Licensed under the Apache License, Version 2.0 (the "License").
  See LICENSE file for the full text.

  This is informational software. It is not legal advice. The jurisdiction issuing
  the permit governs all final decisions. Verify all output against the city's
  current municipal code and the California Building Standards Code.
  ```

## Open questions for the executor

1. **County mapping** — if a `city → county` lookup is found in the codebase, enrich plugin manifests + marketplace keywords. Else, skip.
2. **`marketplace.json` schema** — verify the exact `source` shape for path-based sub-plugins against current Claude Code docs before generating.

---

## Estimated time

- Workstreams A, B, C, D in parallel: ~2–4 hours by 4 sub-agents
- Run + validate: ~30 min
- Repo bootstrap + push: ~30 min
- **Total: half a day**

---

## Execution prompt

Paste this into a fresh Claude Code session at `~/projects/crossbeam`:

```
Execute the build spec at:
~/projects/crossbeam-simple-permits/PLAN-build-execution.md

Read it in full first. Then run the four parallel workstreams (A–D), gate on
their completion, then run the sequential steps (1–7).

Hard constraints:
- DO NOT modify skills/california/ or skills/cities/ source content
- DO NOT push to main until all validation gates pass
- DO use parallel sub-agents for workstreams A, B, C, D
- Local working dir: ~/projects/crossbeam-simple-permits/
- Output target: github.com/CrossBeam-Permits/plugin (empty repo, ready)

Deliverables: passing flatten run for ~10,670 city × permit pairs, repo bootstrapped
with marketplace.json + 495 city plugins, first commit pushed to main, summary
report listing flatten failures (if any) for triage.

Start by reading the spec doc in full.
```

---

*Filed at `~/projects/crossbeam-simple-permits/PLAN-build-execution.md`.*
