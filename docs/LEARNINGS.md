# LEARNINGS — Building CrossBeam Permits

Design decisions, gotchas, and non-obvious choices from the v0.1–v0.3 build (May 2026). Captured for future contributors and future-you.

For day-to-day operations on this product, see the **`simple-permit-stats-ops`** skill in the parent CrossBeam repo (`~/projects/crossbeam/.claude/skills/simple-permit-stats-ops/SKILL.md`). It covers the release workflow, marketplace schema, common operations, and quick-reference commands.

This doc is the **why**; the skill is the **how**.

---

## Architectural decisions

### Per-city sub-plugins, not one mega-plugin

We considered shipping the entire 482-city × 22-permit corpus as a single monolithic plugin. Rejected because:

- Claude Code loads every skill's frontmatter `description` into context at session start (~250 tokens per skill).
- 10,604 skills × 250 tokens ≈ **2.5M tokens** of skill descriptions before the user types anything.
- That blows past every reasonable context budget regardless of model.

The correct shape: one **marketplace** listing 482 **discrete plugins** (one per city). Users install only the city they need. A reviewer in Huntington Beach gets 22 skills loaded; the other 481 cities never touch their machine.

This also matches the user mental model ("install Huntington Beach permits") rather than fighting it.

### Monorepo, not 482 separate repos

We considered one GitHub repo per city. Rejected because:

- 482 repos to maintain, version, and document
- Contributors fragmented across hundreds of repos
- No single "marketplace.json" — discovery would require manual aggregation

A single monorepo with `metadata.pluginRoot: "./cities"` lets each plugin entry use a bare slug source (`"source": "huntington-beach"`) and resolves cleanly. One issue tracker, one PR queue, one place for contributors to land.

### Generated output committed to git

The `cities/` tree (~73K files, ~10,604 SKILL.md files + references) is committed to the public repo, not gitignored.

Tradeoff: large repo size (a few hundred MB), large diffs on regeneration. Win: the public repo is readable, forkable, and contributor-friendly without anyone needing to run the build pipeline. People can browse `cities/sacramento/skills/reroof/SKILL.md` directly on GitHub.

If repo size becomes a problem in the future, the build pipeline could move to a CI step that publishes a `dist` branch — but for v0, committed-output is the right call.

### Source-of-truth lives in the private repo, not the public one

The state skills (`skills/california/`) and city overlays (`skills/cities/`) live in the private CrossBeam repo. The public repo only contains **generated output**.

Why: those source files power both the open-source simple-permits product AND the paid CrossBeam product (which uses them for plan-set review on complex permits). Open-sourcing the source files would expose the paid product's underlying knowledge base and undermine the moat.

Anti-extraction is preserved by:
- Flattening obscures the layered structure (state baseline + 482 different city overlays)
- A competitor scraping the public repo can copy the 22 simple-permit knowledge but has no path to the complex-permit pipeline (extraction, Artemis vision, pinning, plan-sheet review)

---

## Schema gotchas (Claude Code plugin marketplace)

### Source field for in-repo sub-plugins

```json
"source": "./cities/huntington-beach"  // explicit
"source": "huntington-beach"           // works with metadata.pluginRoot
```

The relative-path source must start with `./` or be relative to `metadata.pluginRoot`. Don't use `../` (rejected by validator). Bare strings like `"huntington-beach"` only work when `pluginRoot` is set.

### Plugin name must be kebab-case

Claude Code accepts other forms (lower-cased input, etc.) but the **Claude.ai marketplace sync rejects** non-kebab-case names. Always use `huntington-beach`, never `huntington_beach`, `HuntingtonBeach`, or `Huntington Beach`.

This means natural-language search (`"huntington beach"`) requires keyword enrichment to work — the slug itself can't carry spaces.

### Skill name comes from folder, not frontmatter

For plugin skills, the folder name under `skills/{permit}/` drives the skill's identifier. The plugin's `name` field becomes the namespace prefix.

Example: `cities/huntington-beach/skills/reroof/SKILL.md` → `/huntington-beach:reroof`

If you put `name: huntington-beach-reroof` in the SKILL.md frontmatter, the skill becomes `/huntington-beach:huntington-beach-reroof` (double-prefixed). The flatten script intentionally strips the `name:` field from frontmatter for this reason.

### Reserved marketplace names

Names like `claude-code-marketplace`, `claude-code-plugins`, `anthropic-marketplace`, etc. are reserved. Names that *impersonate* official marketplaces (e.g., `official-claude-plugins`) are also blocked. `crossbeam-permits` is fine — domain-specific, no impersonation.

---

## Build pipeline learnings

### `require.main === module` guard for tsx scripts

When `flatten-skill.ts` exports `flattenSkill` for `flatten-all.ts` to import, the unconditional `main()` call at the bottom auto-runs on import — printing the usage message and exiting. Cost us ~5 minutes diagnosing why the driver script "did nothing."

Pattern that works:

```typescript
const isDirectInvocation =
  typeof require !== "undefined" && require.main === module;
if (isDirectInvocation) {
  main();
}
```

Apply to **every** tsx script that's both runnable directly AND imported by another script.

### 9-second sequential build for 10,604 skills

We considered parallelizing the flatten loop (Promise.all, batches of 8 cities). Tried it briefly. Then ran the sequential version — **9 seconds for 10,604 file writes on SSD.** The complexity of parallelism wasn't worth a 5x speedup of a 9-second job.

Lesson: **profile before parallelizing.** Modern SSDs + sync Node fs are very fast at this scale.

### Counties don't issue simple permits

10 county dirs (`la-county`, `orange-county`, etc.) live in `skills/cities/` because counties matter for the paid CrossBeam product (unincorporated SFR/ADU work). For simple permits, counties don't issue them — incorporated cities do.

The `flatten-all.ts` driver filters with `dir.name.endsWith("-county")` to skip them. **Don't remove the filter.** Tested 482 cities × 22 permits = ~10,604 outputs, matches expectations.

### City per-permit SKILL.md is OPTIONAL

Originally `flatten-skill.ts` threw if `cities/{city}/{permit}/SKILL.md` was missing. We changed this to make the file optional — many cities don't have meaningful local amendments for every permit type, and forcing the onboarder to write empty overlays is wasted work.

When the file is missing, flatten produces:
- State checklist + state tags (always present)
- City portal/fire/code-prefix from `CITY.md` + `meta.json`
- Empty deltas summary

Result: every city ships 22 skills uniformly, even if some are "state baseline + city portal info" only.

### Parse city SKILL.md amendment tables, don't rely on tags.json

The first version of the flatten parser only inlined deltas from city `tags.json` files (severity-routing layer). Cities without `tags.json` would produce flattened output identical to the state baseline (except portal info) — losing all the local amendment content the onboarder had captured in the city's `## Overrides` and `## City-Specific Additions` markdown tables.

The fix: parse those tables in `flatten-skill.ts`. When `tags.json` is also present, it wins for severity routing (curated layer); the SKILL.md tables provide the prose content.

This was the unlock that made shipping all 482 cities Day 0 viable. Without it, we'd have needed to hand-write 482 × 22 = ~10K `tags.json` files.

---

## Distribution learnings

### `/plugin` Discover ranks by install count

This surprised us during testing. Searching `"san"` in Discover returned `laravel-boost` (17.3K installs, claude-plugins-official marketplace) before any San Francisco / San Diego / etc. (0 installs each).

Implications:
- Generic searches will be dominated by popular cross-marketplace plugins
- Specific searches (`"san francisco"`, `"huntington beach"`) work fine because keyword enrichment puts those exact strings in our plugin keywords
- For partial / generic terms, users may need to scroll past popular results

We can't change ranking — that's Claude Code's behavior. We can only make sure specific searches always hit by enriching keywords.

### Marketplace cache is local; pushing to GitHub doesn't auto-propagate

Adding `CrossBeam-Permits/plugin` as a marketplace pulls the catalog *once*. Subsequent pushes to GitHub don't propagate until users run `/plugin marketplace update crossbeam-permits`. Document this prominently in user-facing docs.

Also note: the marketplace catalog is small (~200 KB for 482 plugins), but plugin content (skills + references) is fetched per-plugin only when installed. So updating the marketplace is fast even if the underlying catalog grows.

### Keyword enrichment for natural-language search

Plugin slug `san-francisco` does NOT match the search term `"san francisco"` (with space) — the slug has a hyphen. Adding `"san francisco"` (with space) as an explicit keyword is what makes natural-language search work.

Pattern in `scripts/generate-plugin-manifest.ts`:

```typescript
if (citySlug.includes("-")) {
  kws.add(citySlug.replace(/-/g, " "));    // space-form
  for (const part of citySlug.split("-")) {
    if (part.length > 1) kws.add(part);    // individual words
  }
}
```

Applied automatically to all multi-word city slugs. Plus county-tag enrichment when `meta.county` exists.

---

## Tier system, honest labeling

### "Tier 3" doesn't mean "not human-reviewed"

Initial framing was: Tier 1 = hand-reviewed, Tier 3 = machine-generated, not yet human-reviewed. **Wrong.** Every city has been through the `onboard-city` 11-phase pipeline, which includes:

- Phase 6: validation (skill schema, citation correctness)
- Phase 8: synthetic test generation
- Phase 9: blind skill testing with fix-retest cycle
- Phase 10: end-to-end testing
- Phase 11: human checkpoint before promote-to-production

Costa Mesa hit 99.7%, Laguna Beach 99.6% accuracy on those tests. That's rigorous human-in-the-loop review.

The actual differential between Tier 1 and Tier 3 is much smaller: **whether a city has hand-written `tags.json` files for its 22 simple permits** (severity routing layer specific to plan-check-vs-inspection bucketing in reviewer-mode output).

That's a polish gap, not a quality gap. Future framing should reflect that.

### We considered dropping tiers entirely

Pro: cleaner UX, no implied hierarchy that doesn't exist.
Con: removes a real quality signal for cities looking at adoption.

Decision: **kept tiers** for v0.3 but clarified what they actually mean. Revisit when v1 launches publicly.

---

## What we deferred

- **`/cb:batch-review` slash command** — the demo anchor (folder of mixed PDFs → triage queue + draft corrections). Designed in PLAN-shipping but not built. Highest-impact unbuilt feature.
- **City→county lookup** — `meta.json` doesn't always carry `county`, so search-by-county doesn't always work. Fix is a hardcoded CA city→county map in the manifest generator.
- **2-letter abbreviations as keywords** — `"sf"` → SF, `"la"` → LA, `"hb"` → HB. Considered, deferred. Risks overmatching (`"la"` matches La Mirada, La Habra, La Quinta, etc.) — useful but slightly fuzzy.
- **Tier 1 hand polish on BP / Costa Mesa / Laguna** — write `tags.json` files for the 22 simple permits each. Same level as HB.
- **Synthetic test fixtures at state level** — 22 × 3 = 66 PASS/FAIL/EDGE fixtures for regression testing when state skills change.
- **Anthropic marketplace submission** — listed in PLAN-shipping. Defer until 1–2 weeks after public push to let the repo settle.

---

## Open questions

1. **Should we ship a top-level `crossbeam-permits` plugin** (with the `/cb:batch-review` command) that's installed independently of any city? Currently every command lives inside a city plugin's namespace. A top-level plugin would let cross-city operations (batch review of mixed-city folders) work without forcing the user to install one specific city.

2. **Auto-update cadence** — should the public repo auto-rebuild on a cron when `skills/` source changes? Or stay manually triggered? Current state: manual.

3. **MCP server for live data** — the paid product's MCP server (queryable plan-check status, parcel lookup, batch routing) was discussed as a "Connector" model that lives in the same repo with a license boundary. Not built; design pending.

4. **Cities-edit-their-own-skills contributor model** — aspirational. Design the contribution flow when the first real partner city wants to author updates.

---

*Filed at `docs/LEARNINGS.md` in the public CrossBeam Permits repo. Updated as the build evolves.*
