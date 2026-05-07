# CrossBeam Simple Permits — Flatten & Distribute Plan

**Date:** 2026-05-06
**Status:** Ready to execute. Supersedes the `cb add` CLI workstream from `PLAN-shipping.md`.
**Parent plans:** `PLAN.md` (strategy), `PLAN-shipping.md` (shipping), `PLAN-sidecar-tags.md` (tags layer).

---

## Goal

Open-source the 22 simple-permit skills × every California city as a Claude Code plugin. A plan reviewer in any CA city installs their city's plugin and gets all 22 simple-permit skills, each tailored with that city's portal, fire agency, code prefix, and (where applicable) local amendments.

---

## The model

**22 state-level simple-permit skills are the baseline.** Every California city issues all 22 permit types — state law preempts, cities can amend but not opt out.

For each (city, permit) pair, we **flatten**:

```
state SKILL.md + state tags.json
+ city CITY.md (portal, fire agency, contacts)
+ city meta.json (code prefix, overlays)
+ city {permit}/SKILL.md (IF a meaningful local delta exists — optional)
→ one open-source SKILL.md
```

**Output is uniform: 22 skills per city × 485 cities = ~10,670 flattened skills.** Where the city has no local delta, the flattened skill is still city-specific (different portal URL, fire agency, code prefix tag) — just no rule overrides.

### The 22 simple permits

| # | Permit | # | Permit |
|---|---|---|---|
| 1 | block-wall | 12 | repipe |
| 2 | cleanout | 13 | reroof |
| 3 | deck-patio-repair | 14 | retaining-wall |
| 4 | ev-charger | 15 | rewire |
| 5 | fence | 16 | siding-replacement |
| 6 | fireworks-temp-use | 17 | sign |
| 7 | hvac | 18 | solar |
| 8 | ltia-demolition | 19 | swimming-pool |
| 9 | panel-upgrade | 20 | temporary-power |
| 10 | patio-cover | 21 | water-heater |
| 11 | pool-demolition | 22 | window-replacement |

---

## Distribution architecture

**One GitHub monorepo, one marketplace, per-city sub-plugins.**

```
crossbeam-simple-permits/
├── .claude-plugin/
│   └── marketplace.json                  ← lists all 485 cities as discrete plugins
├── cities/
│   ├── huntington-beach/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── README.md
│   │   ├── meta.json                     ← portal, fire, code prefix, overlays, tier
│   │   └── skills/
│   │       ├── reroof/SKILL.md
│   │       ├── ev-charger/SKILL.md
│   │       ├── ... (all 22)
│   ├── costa-mesa/...
│   └── ... (485 cities)
├── commands/
│   └── batch-review.md                   ← /cb:batch-review <folder>
├── scripts/
│   ├── flatten-skill.ts                  ← existing, needs 2 edits
│   ├── flatten-all.ts                    ← new driver
│   ├── generate-plugin-manifest.ts       ← new
│   └── generate-marketplace.ts           ← new
├── docs/disclaimer.md
├── LICENSE                               ← Apache-2.0 + NOTICE
└── README.md
```

**Install UX (native Claude Code, no custom flow):**

```
/plugin marketplace add CrossBeam-Permits/plugin
/plugin                                    ← opens Discover menu
(search "huntington beach")
Install
```

**GitHub home:** https://github.com/CrossBeam-Permits — repo `plugin` hosts the marketplace monorepo.

The reviewer now has 22 HB simple-permit skills available. Lazy-loaded by description.

---

## Required script changes

### 1. `flatten-skill.ts` — two edits

- **Make city per-permit `SKILL.md` optional.** Currently throws if missing (line 287–288). Change: if missing, render with state checklist + state tags + city universal info (portal/fire/code prefix from CITY.md + meta.json), with empty deltas summary. Skill still produces.
- **Parse city `SKILL.md` delta tables when present.** Currently the prose is read and discarded. Add parsers for the two structured tables onboard-city emits:
  - `## Overrides` table → state-check# | city rule | code | notes
  - `## City-Specific Additions` table → # | check | requirement | code

### 2. `flatten-all.ts` — new driver

```
for city in skills/cities/*:
  for permit in [22 simple permits]:
    flatten(city, permit)  →  cities/{city}/skills/{permit}/SKILL.md
```

Output path changes from current `~/projects/crossbeam-simple-permits/.claude/skills/{city}-{permit}/` to `cities/{city}/skills/{permit}/`.

### 3. `generate-plugin-manifest.ts` — new

For each city directory under `cities/`, emit `.claude-plugin/plugin.json` from `meta.json`. ~10 lines per file.

### 4. `generate-marketplace.ts` — new

Walk `cities/`, emit root `.claude-plugin/marketplace.json` listing all 485 plugins with name, description, source path, keywords (city, county, region).

---

## Tier labeling

Same 22 skills per city, but each plugin's metadata reflects how much hand-curation has gone in:

- **Tier 1** — hand-reviewed deltas + tagged plan-check vs inspection (HB, BP, Costa Mesa, Laguna)
- **Tier 2** — onboarder-generated deltas, spot-checked
- **Tier 3** — onboarder-generated deltas only, not yet human-reviewed
- **State-only** — no detectable deltas; output is state baseline + portal/fire info

Honest, no fake gaps. All 485 ship Day 0; tier label tells reviewers what's been QA'd.

---

## What stays out of v1

- `cb add <city>` shadcn-style CLI — replaced by native `/plugin marketplace add`
- 23rd permit for professional pyrotechnic display — defer
- MCP "connector" with server-side skills — that's the paid product, separate repo or boundary
- Plan extraction, Artemis vision, pinning, Bluebeam XFDF — all stay in CrossBeam paid (moat)
- Complex permits (ADU, SFR, multi-unit, residential-addition, restaurant-TI, kitchen-bath) — paid product

---

## Sequenced execution

1. **Flatten parser fix** — make city per-permit skill optional, parse delta tables. (½ day)
2. **`flatten-all.ts` driver + manifest generators** — bulk-flatten 485 × 22, write plugin manifests + marketplace.json. (1 day)
3. **Tier 1 hand polish** — HB (finish 19 remaining), BP, Costa Mesa, Laguna deltas hand-reviewed. (3 days, parallelizable)
4. **`/cb:batch-review` slash command** — folder-of-PDFs → triage queue + draft corrections. The demo anchor. (2-3 days)
5. **Synthetic test fixtures + automated review harness** at state level (66 fixtures = 22 × 3). (2-3 days)
6. **Repo public** — README, disclaimer, Apache-2.0 + NOTICE, contributor guide. (1 day)
7. **Anthropic marketplace listing** — week behind public to let Tier 1 settle.

**Critical path:** 1 → 2 → 4 → 6. Tier 1 polish parallelizes.

---

## Open decisions for you

1. ~~**Repo location**~~ — ✅ `github.com/CrossBeam-Permits/plugin`
2. **License** — Apache-2.0 + NOTICE working assumption pending legal?
3. **Day 0 scope** — all 485 cities with honest tier labels (recommended) or only Tier 1?
4. **Attribution in flattened output** — "via CrossBeam Simple Permits — onboard.ai" footer?
5. **Paid MCP connector** — same repo with license boundary, or separate repo?

---

*Filed at `~/projects/crossbeam-simple-permits/PLAN-flatten-and-distribute.md`.*
