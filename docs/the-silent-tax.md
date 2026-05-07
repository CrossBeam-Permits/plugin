# The Silent Tax: How Simple Permits Clog California's Building Queue

**The pitch in one line:** California loses an estimated **$2.5–5 billion per year** in delayed economic activity because simple permits — water heaters, reroofs, EV chargers, solar — clog the same plan-check queue as the complex projects that actually move the housing needle.

## The situation

California issues roughly **4–5 million building permits per year** across ~600 jurisdictions. About **60–70% of those by count are "simple permits"** — checklist-driven replacements and small installations that don't require architects or blueprints:

- Water heaters (~700K/yr) · HVAC changeouts (~500K/yr) · Reroofs (~400K/yr)
- Rooftop solar (~180K/yr) · Battery storage (~100K/yr) · EV chargers (~100K/yr)
- Panel upgrades, windows, minor remodels, fences, pool equipment, sewer laterals, ADUs on pre-approved plans, and ~12 more similar categories

These simple permits consume an estimated **~1.1 million plan-check staff-hours per year** statewide — real work, but mechanical work. Every one of them is reviewed by the same humans who review single-family homes, ADUs, and commercial tenant improvements.

## Why this produces a queue crisis

California's plan-check system runs at roughly **85–95% utilization** — and in hot markets like LA, SF, San Jose, and San Diego, effectively pinned at 95%+. At that utilization, queueing theory is brutal:

| Utilization | Wait-time multiplier |
|---|---|
| 0.50 | 1× service time |
| 0.75 | 3× |
| 0.90 | 9× |
| 0.95 | **19×** |

A plan checker operating at 95% utilization produces wait times **19× longer** than one operating at 50%. This is why a complex project that needs 6 hours of actual review sits in the queue for 30+ days. The reviewer isn't slow — the *queue in front of them* is long, because every reroof and water heater in the city is waiting in the same line.

## What automating the simple 22 does

Open-sourcing AI-driven plan review for the simple permit categories pulls them out of the human queue entirely. Cities keep their existing plan-check headcount; those humans just stop reviewing checklists.

**The math:**

- Workload drops ~15–25% (simple permits are fast individually)
- **Queue depth drops ~60–70%** (they're most of the volume)
- **Utilization drops from ~0.90 → ~0.70**
- **Wait times for complex permits collapse from 30 days → ~8–10 days**

This isn't a linear improvement. It's the nonlinearity of queueing theory working in your favor: small utilization drops at the high end produce huge wait-time improvements.

## The economic impact

Every day a building permit sits in the queue is a day of delayed economic activity — construction financing accruing interest, contractors idle, tenants paying rent elsewhere, housing supply not reaching the market.

Conservative estimates of delay cost per category, if queue wait shrinks by ~20 days:

| Category | Annual volume | Carrying cost/day | Annual delay cost released |
|---|---|---|---|
| Single-family homes | ~100K | ~$500/day | **~$1.0B** |
| ADUs | ~28K | ~$200/day | ~$110M |
| Commercial tenant improvements | ~50–80K | ~$1,500–5,000/day | **~$1.5–3B** |
| Multifamily | ~500 projects | ~$15K/day | ~$150M |

**Total released annually: $2.5–5 billion in California.**

And that's just the mean. The bigger win is **variance collapse** — today wait times are wildly unpredictable (10 days for one project, 60 for the next), which inflates construction-loan risk premiums and kills pro-formas. Dropping utilization to 0.70 collapses both the mean and the variance, which feeds directly into lower housing-construction costs.

## Why open source

The 22 simple permit types are defined by state code — UPC, CEC, CRC, CalGreen. A jurisdiction in Fresno needs the same water-heater checklist as one in Chula Vista. There's no competitive moat here, and no reason every city should be building this in-house.

Open source means:
- Every one of California's ~600 jurisdictions can adopt it for free
- Code changes propagate once, not 600 times
- Cities audit the logic before trusting it (they should)
- No vendor lock-in, no recurring license fees pulling from already-strained building department budgets

Precedent: **SolarAPP+**, NREL's open-source solar permit automation, is already running in ~150 CA jurisdictions and saved ~15,400 staff-hours and ~150,000 business days of applicant delay in 2023 alone. It works. The simple-22 approach extends that model to the other 95% of routine permits.

## The ask

- **Legislators:** Back state funding or mandates that enable jurisdictions to adopt open-source simple-permit automation — the ROI to the state's housing production goals is ~30–60× the direct staff savings.
- **CalBO / building officials:** Pilot it. The humans in the loop stay in the loop for every complex permit. Simple permits become instant — which is what residents already expect.
- **YIMBY / housing advocates:** This is among the highest-leverage housing-production interventions available that doesn't require zoning changes, CEQA reform, or new state law. It's a pure throughput unlock on capacity that already exists.

---

### Sources and methodology notes

Volume estimates triangulated from US Census housing-unit data (14.88M CA housing units, 2024), equipment-lifespan replacement math, and the subset of CA cities that publish permit-type breakdowns. SolarAPP+ 2023 performance data from NREL (18,906 permits, 15,400 staff-hours saved, 14.5 median days off applicant timelines). EV charger data from CEC. Queueing analysis uses standard M/M/1 approximation; real plan-check queues deviate from this in ways that mostly make the story stronger (batching, business-hours constraints, multi-round review). Carrying cost estimates use blended construction-financing, contractor-mobilization, and opportunity-cost figures; swap in your own assumptions to taste.

No central statewide permit-type registry exists in California, so the 3.0M simple-permit figure has a ±25% uncertainty band. Even at the low end of that band, the queue-collapse story dominates.
