# Laguna Beach — Current Commercial TI Planning Route (Ord. 1732)

**Law as of:** 2026-10-10

**Authority:** LBMC §§25.05.040 and 25.05.045 as replaced/added by Urgency Ordinance No. 1732

## Default inversion

Do not send a commercial TI to discretionary Design Review merely because it has exterior work. Match the current closed lists: 16 Design Review categories, 28 Zone Clearance categories, and 17 Administrative Design Review categories.

When Design Review is required for non-residential development, apply §25.05.040(F)(1)(ii)'s Planning Commission jurisdiction (also for any project in the Downtown Specific Plan area and any project where the Planning Commission decides another permit, such as a CUP). Jurisdiction does not itself create a Design Review trigger.

## Common TI matches

| Scope | Current route |
|---|---|
| Interior modification with no exterior modification | Zone Clearance, (B)(2)(d) |
| Other non-major alteration/addition and improvement no more than 15 ft | Ordinarily Zone Clearance, (B)(2)(a)-(b), absent another trigger |
| New building | Design Review, (B)(1)(b) |
| Improvement over 15 ft | Design Review, (B)(1)(c) |
| Development in an ESA | Design Review, (B)(1)(e), absent the enacted peer-reviewed professional determination |
| Commercial/industrial parking or loading area | Design Review, (B)(1)(l) |
| New/widened vehicular access described by the ordinance | Design Review, (B)(1)(k) |
| Trash storage/enclosure | Design Review, (B)(1)(n), except screened side-yard storage `(B)(2)(q)` or qualifying screened front-yard storage ADR `(B)(3)(a)(xv)` |
| Mechanical equipment satisfying §7.25.130(C) | Zone Clearance, (B)(2)(v) |
| Mechanical equipment failing §7.25.130(C) | Administrative Design Review, (B)(3)(a)(v) |
| White/light or potentially glaring reroof | Administrative Design Review, (B)(3)(a)(ix) |
| Roof dimension/SF/pitch change | Administrative Design Review, (B)(3)(a)(x) |

**Precedence between rows.** A specific row governs its subject over the general "Improvement over 15 ft" and "non-major alteration" rows. Rooftop mechanical equipment is routed by the two equipment rows (a roof unit is not ground-mounted, so ADR under (B)(3)(a)(v)), not by (B)(1)(c), even on a building over 15 ft. A true in-kind replacement of an existing roof unit is (B)(2)(c), cleared at the counter. New floor area, a new building or a raised roof is a separate piece that keeps (B)(1)(b) or (c). Method: a CrossBeam reference that is not included in this plugin Step 4d; HVAC detail: `../../hvac/SKILL.md`.

Storefronts, awnings, facade finishes, exterior lights, signs, and visible hood components are not categorical triggers by name in the new lists. Classify their actual improvement/height/ESA and related scope. If no closed-list category matches, return `needs_source`; do not revive the former exterior-change default.

For signs, the current lists have no sign item. A sign permit is decided under §25.54.018 as amended by Ord. 1732: Director for eligible signs (master-program signs, replacements of permitted signs, conforming signs with letters 14 in or less), Planning Commission for all others. Load the `sign` skill. Current `(B)(1)(d)` is historic-resource work, not signs.

## Historic resources

Current routing is based on the historic action, not a blanket reversal of the interior-only provision:

- qualifying minor historic-resource alteration → ADR under (B)(3)(a)(iv), after Heritage Committee review; hearing waiver unavailable;
- major modification/alteration/action pertaining to a historic resource → Design Review under (B)(1)(d), after Heritage Committee review.

Use current §25.45.010 for the detailed procedure.

## Administrative hearing waiver and timing

Except for elevated decks/patios and minor historic-resource work, an ADR hearing may be waived only when no other entitlement is required and the 15-working-day mailed/published notice-and-comment procedure produces no timely hearing request.

- Public-hearing site/public-place posting: at least 10 calendar days before hearing.
- Mailed public-hearing notice: at least 21 calendar days for Design Review and 14 calendar days for ADR.
- DR/ADR staking, when applicable: 21/14 calendar days before hearing.
- Appeal/effective-date period: 14 calendar days.

For these two tracks, the 21/14-day values govern mailed hearing notice and independently govern applicable staking.

## Output

```text
Route: Design Review | Zone Clearance | Administrative Design Review | needs_source
Matched current category: §25.05.040(B)(...)
Planning Commission jurisdiction if DR: yes | no | unknown
ESA override: applies | cleared | not applicable | unknown
Historic route: major DR | minor ADR | not applicable | unknown
ADR hearing waiver: potentially available | unavailable | not applicable
CDP/CUP: separately required | separately exempt | determination needed
Appeal period: 14 calendar days
```
