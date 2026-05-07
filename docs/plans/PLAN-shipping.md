# CrossBeam Simple Permits — Shipping Plan

**Date:** 2026-04-23
**Status:** Active — parallel workstreams in flight.
**Parent plans:**
- `plan-simple-permits-open-source-0422.md` — strategic frame
- `plan-sidecar-tags-0423.md` — state-level tagging (executed, clean)

**What this plan covers:** moving from "3 HB permits flatten and live-tested" to "shipped at Code with Claude with 22 permits × Tier 1 cities, open-source repo public, Anthropic marketplace listing."

---

## Current state (as of 2026-04-23 evening)

### Done
- ✅ 22 state-level simple permit skills tagged (487 items, stage + severity)
- ✅ State tags validated clean, semantic rules enforced (no plan-check/advisory, no doc/non-advisory, no inspection/non-verify)
- ✅ City tags schema + validator (extended to handle both state and city)
- ✅ HB city tags written for 3 pilot permits: reroof, ev-charger, water-heater
- ✅ Flatten script — reads state + city tags + narrative, produces single flattened SKILL.md per (city, permit)
- ✅ 3 HB permits flattened and placed in `.claude/skills/` for Claude Code testing
- ✅ **Live reviewer test passed** (reroof, 2026-04-23) — 50% fewer false-positive corrections vs yesterday's baseline; inspection items correctly bucketed; hard fails preserved; model supplies bonus expertise (CZ 6 exemption, valuation heuristic)

### Not done, needed to ship
- ❌ 19 other HB permits flattened (HB city tags + flatten run)
- ❌ Synthetic test fixture set at state level (for scale testing)
- ❌ Tier 1 cities beyond HB (Buena Park, Costa Mesa, Laguna Beach) — city tags + flatten
- ❌ Batch review command (`/batch-review <folder>`) — the demo centerpiece
- ❌ Demo dataset (30-50 mixed synthetic HB permits)
- ❌ `cb add <city>` shadcn-style installer
- ❌ Public GitHub repo + README + disclaimer/license
- ❌ Anthropic marketplace listing
- ❌ Tier 2 cities (~20-50) — automated flatten across onboarded cities
- ❌ Legal review (disclaimer, municipal code quoting, license choice)

---

## Launch target: Code with Claude demo + public release

**Demo arc (~6 minutes on stage):**

```
0:00  Context: cities spend $340K/yr on plan check consultants (BP verified).
      Simple permits = 80% of volume, 0% of value.

0:45  Install: one command, one plugin
      → `cb add huntington-beach`
      → "22 permit types live."

1:15  Single permit review (fast, legible):
      → drop one reroof PDF → 45 seconds → clean corrections output.
      → "This is what every line of the batch output means."

2:00  Batch review (the killer):
      → drop folder of 40 mixed HB permits (reroof/ev-charger/water-heater/solar/panel)
      → 3-5 minutes parallel processing
      → 28 auto-approve / 9 corrections-required / 3 human-review
      → CSV + draft correction letters ready to send

5:00  Punch: "This is a week of plan-checker work. It's 9:05 AM."
      → `github.com/onboard-dot-ai/crossbeam-simple-permits` — every CA city,
        every simple permit, shipped today, free.

5:30  Don't name competitors. Positioning speaks for itself.
```

**What must work for demo:**
1. Install story (CLI one-liner)
2. Single-permit reviewer output — visually tight (already works)
3. Batch review command — doesn't exist yet, demo-critical
4. Demo dataset with variety — needs generation
5. All 22 HB permits available — 3 done, 19 to go

---

## Workstreams (run in parallel)

### A. Content production — complete HB, extend to Tier 1

**A1. Finish HB's 22 permits.**
- Write HB city tags.json for the remaining 19 permits
  - Most will be small (2-6 additions each) — overlay + portal + fire agency + parcel checks
- Run flatten for all 22 HB (city, permit) pairs
- Spot-check each flattened output for obvious issues (5 minutes × 22 = ~2 hours)
- **Estimate:** 1 day

**A2. Tier 1 cities — Buena Park, Costa Mesa, Laguna Beach.**
- Each city already has city SKILL.md overlays from batch-onboard
- For each: write per-permit city tags.json, run flatten across all 22 permits
- Hand QA each city's 22 flattened outputs
- **Estimate:** 2-3 days per city (most of which is judgment on city-specific additions, not new work)

**A3. Tier 2 cities — automated across all 275 onboarded.**
- Script: for each city in `skills/cities/*/`, if `meta.json` lists a permit as OTC, run flatten
- Accept that Tier 2 outputs ship without hand QA — label "community-reviewed pending"
- **Estimate:** 1 day (mostly script work, then bulk run)

### B. Test infrastructure — scale QA without hand-testing 8,000 outputs

**B1. Synthetic fixtures at state level (not per-city).**
- Use existing `synthetic-permit-tests` skill to generate 3 fixtures per state permit (PASS/FAIL/EDGE) × 22 = 66 fixtures
- Each fixture: realistic form-field JSON + expected reviewer output (pass/fail/flag per checklist item)
- Store at `skills/california/{permit}/fixtures/{case}.json` (new directory)
- **Estimate:** 1-2 days

**B2. Automated review harness.**
- `scripts/test-skill.ts <city> <permit>` — takes flattened skill + fixtures, runs reviewer mode via Agent SDK, compares output to expected
- Produces a matrix: per-fixture pass/fail with diff
- Run across all Tier 1 (city × permit × fixture) = 4 cities × 22 permits × 3 fixtures = 264 automated reviews
- **Estimate:** 2-3 days (Agent SDK + scoring logic is the real work)

**B3. Real-world spot-check for HB.**
- Fetch 10-20 real HB permits from Accela public records
- Run reviewer mode, hand-check outputs for false positives / missed issues
- Highest-fidelity test — calibrates what "good" looks like for the anchor city
- **Estimate:** 1 day (mostly scraping + reading)

**B4. Regression harness for post-launch.**
- Any code amendment (CBC update, city local amendment change) should trigger a re-run of fixtures
- Deferred until post-launch — not on critical path for demo

### C. Demo prep

**C1. Batch review command.**
- `/batch-review <folder>` — identifies each PDF's permit type, routes to appropriate skill, runs reviewer mode, aggregates
- Output: auto-approve / corrections / human-review triage, CSV summary, draft correction emails
- Parallelism via Agent SDK sub-agents
- **Estimate:** 2-3 days (similar to existing city-review demo skill but multi-type routing)

**C2. Demo dataset.**
- Generate 40-50 synthetic HB permits mixing all 22 types in realistic proportions (lots of reroofs + EV chargers + water heaters, fewer fireworks/fence/retaining)
- Mix PASS / FAIL / EDGE cases so batch output shows variety
- Blend into single drop-in folder
- **Estimate:** 1-2 days (leveraging synthetic-permit-tests)

**C3. Install story (`cb add <city>`).**
- Shadcn-style CLI — fetches skill dir from GitHub monorepo, writes to user's `.claude/skills/`
- Npm package: `@onboard-dot-ai/crossbeam-simple-permits`
- Commands: `add`, `remove`, `list`, `update`
- Also publish as Claude Code plugin on Anthropic marketplace (same commands)
- **Estimate:** 3-4 days

**C4. Demo polish.**
- Practice runs — validate timing (6 min target), eliminate dead air during batch processing
- Failsafe: canned video of batch run in case live fails
- Slide deck / minimal viz around the plan checker output
- **Estimate:** 2-3 days, closer to event

### D. Distribution + launch materials

**D1. Public GitHub repo.**
- `onboard-dot-ai/crossbeam-simple-permits`
- Structure: `skills/{city}-{permit}/` (flat — one dir per pair), `tests/`, `.github/workflows/` for CI
- Clear CONTRIBUTING.md so cities / contractors can submit corrections
- **Estimate:** 1 day

**D2. README / landing page.**
- Lead with batch review use case, not single-permit
- Tier labels explicit and honest (Tier 1 = vetted, Tier 2 = spot-checked, Tier 3 = community)
- Install one-liner, 3-minute quickstart
- Partner city logos / endorsements (if BP / Laguna signs off pre-launch)
- **Estimate:** 2 days

**D3. Announcement arc.**
- Blog post — the "why free, why now" essay
- Tweet thread with demo video
- DM preview to BP / HB city staff 48 hours before public (social proof, no surprise)
- Anthropic marketplace listing live Day 0
- **Estimate:** 2-3 days

### E. Legal + license

**E1. License choice.**
- Options: MIT (simple) vs Apache-2.0 (patent clause + NOTICE) vs custom "informational-use" license
- Needs attorney input
- **Estimate:** 1 week to decide (mostly waiting on legal review)

**E2. Disclaimer language.**
- Prominent in every SKILL.md frontmatter + README
- "Informational use, not legal advice, jurisdiction controls"
- Reviewed by counsel
- **Estimate:** embedded in E1

**E3. Municipal code reuse audit.**
- Ensure no skill reproduces copyrighted municipal code — paraphrase + cite only
- Spot-check ecode360 and ICC-quoted content
- **Estimate:** 1 day (mostly mechanical pass)

---

## Testing strategy at 8,000-skill scale

The question: how do we QA an 8,000-skill repo without manual review at scale?

**Answer: trust the pyramid, test at the base.**

```
            ┌──────────────────────────┐
            │  Flattened city skills   │  ← derived, test by sampling
            │  (8,000 outputs)          │
            └──────────────────────────┘
                        │ flatten script (deterministic)
                        ▼
            ┌──────────────────────────┐
            │  State tags + city tags  │  ← validated clean
            │  (487 + ~2000 items)      │
            └──────────────────────────┘
                        │
                        ▼
            ┌──────────────────────────┐
            │  22 state SKILL.md       │  ← hand-written, peer-reviewed,
            │  (the source of truth)   │     synthetic fixtures catch bugs
            └──────────────────────────┘
```

**Test effort concentrated at the base:**
- 22 state skills × 3 synthetic fixtures = **66 test cases** that validate the core checklist logic
- Flatten script is deterministic — no additional test needed beyond "does it run clean on every input"
- City overlays are small (6-8 items per permit) and mostly overlay/portal/fire-agency variations

**Per-tier validation effort:**

| Tier | Cities | QA effort | Approach |
|---|---|---|---|
| Tier 1 | 4 (HB, BP, CM, LB) | Full hand QA on 22 × 4 = 88 outputs | Each reviewed by a human, optionally real-permit spot-check |
| Tier 2 | ~20-50 | Synthetic fixtures + 3 random permit types spot-checked per city | Automated harness catches regressions |
| Tier 3 | remainder (~200+) | Ship with "community-reviewed pending" label | Flatten + validator clean only; real QA via community |

**Why this is defensible:**
- The model supplies expertise on top of the skill (verified in today's HB reroof review — reviewer added CZ 6 exemption, valuation heuristic, OB declaration nuance *without prompting from the skill*). The skill provides scaffolding, not perfection.
- Each flattened output is a deterministic function of state + city inputs. Bugs surface at the source, not in the 8,000 derivatives.
- The disclaimer + license establish informational-only stance, protecting both us and cities.
- Community QA replaces exhaustive internal QA for Tier 3.

**Red lines — things we will NOT ship past:**
- Any state skill that fails its synthetic fixtures
- Any Tier 1 city with a hand-QA failure that isn't resolved
- Any skill citing repealed code or flagging-as-fail something that shouldn't fail (false positive = trust-destroying)

---

## Sequencing (what blocks what)

```
WEEK 1 (this week — Apr 23-27)
  A1: HB finish (19 permits remaining)  ─────┐
  B1: Synthetic fixtures at state level      ├─→  both needed before B2/B3
  C1: Batch review command (start)           ─┘

WEEK 2 (Apr 28 - May 4)
  B2: Automated review harness             ─┐
  A2: Tier 1 cities (BP, CM, LB)           │
  C2: Demo dataset                         ├─→  demo-critical set
  C1: Batch review command (finish)        │
  D1: GitHub repo public structure         ─┘

WEEK 3 (May 5-11)
  A3: Tier 2 automation (mass flatten)
  B3: HB real-permit spot-check
  C3: `cb add <city>` CLI
  D2: README + landing page
  E1/E3: Legal review + code audit

WEEK 4+ (pre-demo polish)
  C4: Demo practice runs
  D3: Announcement arc
  Final Tier 1 QA pass
  Dry runs with real demo hardware
```

**Critical path:** A1 → C1 → C2 → C3 (demo path). Batch review + demo dataset + install one-liner are load-bearing for stage.

**Nice-to-have cuts if crunched:** Tier 2 / Tier 3 city scaling can ship post-event. Demo only needs Tier 1 + HB's 22 permits. The repo goes public with Tier 1 cities populated and a "more cities coming" note.

---

## Open questions

1. **Who owns each workstream?** Currently Mike + multiple Claude Code agents. Do we need named humans on critical-path items, or is the agent-driven model OK? (Today's work showed the agent-driven model works well with clear execution prompts.)

2. **Which Tier 1 cities actually greenlight using their name pre-launch?** HB and BP are partners. Costa Mesa and Laguna are plausible — but we should get quick verbal ok before naming them publicly.

3. **Marketplace timing — live Day 0 or after first wave of GitHub traction?** If Anthropic features us Day 0, discoverability skyrockets but failures get amplified. Safer to ship GitHub first, marketplace a week later once Tier 1 is battle-tested.

4. **Kitchen-bath triage skill — include in v1 or defer?** Case for inclusion: it's the highest-traffic homeowner permit type and a natural funnel back to paid CrossBeam. Case for defer: we haven't designed it yet, adds scope. I'd defer.

5. **Pricing ask on stage?** If we're giving away simple permits, is there any ask at all for cities that want complex permits too? Or is the demo purely "look what you get for free" and leave the conversation open? My instinct: no ask on stage — positioning alone drives inbound.

6. **Real-world HB permit fetch — legally OK?** Accela records are public. Pulling them for synthetic-test-calibration is almost certainly fine but worth 10 minutes of legal review.

---

## Go/no-go criteria for demo day

Must all be true on demo day:

- [ ] All 22 HB permits flattened and hand-QA'd
- [ ] Batch review command works end-to-end on a 40-permit folder
- [ ] `cb add huntington-beach` installs cleanly in a fresh Claude Code session
- [ ] 3-5 Tier 1 cities (including HB) flattened, hand-QA'd, and publicly labeled
- [ ] Public GitHub repo with readable README and clear tier labels
- [ ] Disclaimer / license attached
- [ ] Batch demo runs in ≤5 minutes on Wi-Fi with audience watching
- [ ] Failsafe canned video ready
- [ ] Announcement tweet drafted + partner cities notified

If any of these fail 48 hours out, demo the working subset and announce the rest as "coming soon."

---

## What this plan does NOT cover

- **Complex permit skills** (ADU, SFR, multi-unit, residential addition, restaurant TI, kitchen-bath remodel) — stay in CrossBeam paid product. Not being open-sourced. Not being tagged with sidecars in this wave.
- **Corrections letter polish / Bluebeam XFDF round-trip** — CrossBeam paid product only. Open-source output is plain text.
- **Plan-sheet extraction pipeline** — CrossBeam paid. Self-enforcing moat.
- **Portal automation via Computer Use** — optional feature, not headline. If it works great, if not, the skill still has value.
- **MCP server for live plan-check data** — distinct project (Alex Vernaghi). Related but separate roadmap.

---

*Filed mirror at `~/projects/crossbeam-simple-permits/PLAN-shipping.md`.*
