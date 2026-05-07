# CrossBeam Permits

> Open-source plan-check skills for every California city. 22 simple permit types per city — free for cities, builders, and homeowners.

A Claude Code plugin marketplace. A plan reviewer in any California city installs their city's plugin and gets ready-to-use permit-review skills tailored to that city's portal, fire agency, code amendments, and overlays.

## Install

In Claude Code:

```
/plugin marketplace add CrossBeam-Permits/plugin
/plugin
# search your city, install
```

## What you get per city

Skills for the 22 simple permit types every California city issues:

reroof · ev-charger · solar · water-heater · hvac · window-replacement · panel-upgrade · temporary-power · repipe · siding-replacement · fence · block-wall · retaining-wall · patio-cover · deck-patio-repair · pool-demolition · ltia-demolition · cleanout · sign · fireworks-temp-use · swimming-pool · rewire

Each skill works in two modes:

- **Builder / Homeowner** — intake → compliance check → submission guide for the city's portal
- **City Reviewer** — runs the plan-check checklist against a submittal, produces tight corrections output

## Status

**This is the v0.1 scaffold.** Currently shipping:

- ✅ **Huntington Beach** (Tier 1, vetted) — reroof, EV charger, water heater
- 🔜 Buena Park, Costa Mesa, Laguna Beach (Tier 1)
- 🔜 ~480 more California cities (Tier 2/3)
- 🔜 All 22 permit types per city

The full ~485-city × 22-permit run lands shortly. Watch this repo for releases.

## Tier labels

- **Tier 1** — hand-reviewed, vetted end-to-end (HB, BP, Costa Mesa, Laguna Beach)
- **Tier 2** — onboarder-generated, spot-checked
- **Tier 3** — onboarder-generated, not yet human-reviewed

Each city's plugin metadata declares its tier honestly.

## Contributing

Cities, contractors, plan reviewers, and developers welcome. CONTRIBUTING.md coming with the full release.

## Disclaimer

Informational use only. Not legal advice. The jurisdiction issuing the permit governs all final decisions. See [NOTICE](NOTICE) for full disclaimer.

## License

[Apache-2.0](LICENSE)

CrossBeam Permits is a brand of [Onboard Dot AI LLC](https://crossbeam-permits.com). The CrossBeam paid product handles complex permits (ADUs, single-family, multi-unit, residential additions, restaurant TI) with proprietary plan-extraction and review tools — see https://crossbeam-permits.com.
