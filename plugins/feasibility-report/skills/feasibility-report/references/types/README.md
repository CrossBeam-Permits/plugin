# Project-type profiles

The core steps (`SKILL.md`) are the same for every project. A profile adds what one kind of project always raises: the intake facts it needs, the questions it always asks, the tools to call for them, and the question cards the report carries.

## Pick the profile

Decide from the program the person described, after reading it (never by matching words in it). If the program spans two (an addition plus a new ADU; a restaurant tenant improvement that also adds a patio), load both and merge their cards. If none fits, use `general.md`.

| Profile | Program |
|---|---|
| `new-unit.md` | ADU, JADU, garage or accessory-building conversion, a guest house used as a dwelling |
| `new-house.md` | New single-family house, including a rebuild after demolition |
| `addition-remodel.md` | Addition, second story, remodel or alteration of an existing house |
| `multi-unit.md` | SB 9 unit or urban lot split, duplex, triplex, small apartment or townhome project |
| `commercial-ti.md` | Commercial tenant improvement, change of use or occupancy, restaurant or food use, small commercial addition |
| `general.md` | Anything else that needs a building permit (pool, retaining wall, deck, sign, solar, demolition, industrial) |

Record the profile you picked, and why in one line, at the top of your working notes. Say in the report's header kicker which project type it is.

## What every profile holds

1. **Intake:** the facts the core intake (`../01-intake.md`) must also collect for this type.
2. **Questions:** the topics to settle, each with where to look. A profile names topics and tools, never a value: every limit still comes from the law you read.
3. **Extra checks:** tools beyond the core steps.
4. **Cards:** the question cards for the report, in order. Drop a card that does not apply; add one the client raised.
5. **Intake checklist additions:** what the permit filing usually needs for this type, to confirm against the City's own list.

## Permit type ids

`crossbeam_get_review_requirements` and `crossbeam_fees` take a CrossBeam permit type id. Each profile suggests one; a wrong id returns the valid list, so pick from that list rather than guessing.
