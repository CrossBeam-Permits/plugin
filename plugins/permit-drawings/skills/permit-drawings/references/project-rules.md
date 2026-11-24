# project.json: rules and code notes

Topic card for `project-file.md`. Read it when you copy `kit_checks` into `rules` (stage 5, `05-code-questions.md` section 0), record a code decision whose quote has conditions, or read the `rules` check in the QA report.

## Rules

`rules` lists the code rules that drawn values must meet. Each entry checks one drawn value against one limit. You usually copy them from the `kit_checks` of a `crossbeam_rules` answer (`05-code-questions.md` section 0). The field is optional.

```json
"rules": [
  {"id": "R-1", "element": "habitable room ceiling height", "citation": "<CODE> <EDITION> <SECTION>",
   "source_from": "state", "cd": "CD-004", "kit_key": "ceiling_height",
   "check": {"value": "$office_ceiling_h", "op": ">=", "limit": 7, "unit": "ft"},
   "note": "office is habitable (logs/scope.md)"},
  {"id": "R-2-D1", "element": "door clear width", "citation": "<CODE> <SECTION>",
   "check": {"value": "$openings.D-1.width", "op": ">=", "limit": 32, "unit": "in"}}
]
```

| Field | Meaning |
|---|---|
| `id` | Your rule id, unique in the file. Letters, digits, `_` and `-`. When one rule applies to several drawn values (every door), write one entry per value: `R-2-D1`, `R-2-D2`. |
| `element` | What the rule is about, in the words `crossbeam_rules` used. |
| `citation` | Code, edition and section, from the rule's `source`. |
| `source_from` | `city`, `state` or `code`, from `source.from`. |
| `cd` | The `logs/code-decisions.md` entry that records the rule. |
| `kit_key` | The `key` of the `kit_checks` item you copied, kept for tracing. |
| `accepted` | Only when the owner keeps a design that breaks this rule: the `logs/decisions.md` entry that records it, such as `DEC-007`. See "A design the owner keeps" below. |
| `check.spread` | In place of `check.value`: two or more drawn values whose spread, the largest minus the smallest, the rule limits. See "Spread rules" below. |
| `check.value` | The drawn value, as a reference: `"$key"`, or an item field such as `"$openings.D-1.width"`. An item field works whether it holds an inline Value or a `"$key"` reference; QA follows the reference and reports the key it reached as `resolved_key`. |
| `check.op` | `>=` (at least), `<=` (at most) or `==` (exactly). |
| `check.limit` | The limit, a number. |
| `check.close` | Optional: how near the limit, in the rule's unit, an unverified value counts as close. Default 10 % of the limit. See "Estimates near the limit" below. |
| `check.unit` | The unit of `limit`: `in`, `ft`, `sf` (also `sq ft`), `sq in`, `pct` (also `%`), `ratio`, `deg`, `count`, `hr` or `days`; or a same-unit-only unit: `cfm`, `gpm`, `gpf`, `A`, `psf`, `psi`, `lb`, `mph`, `degF`, `u-factor`, `R-value`, `in/ft` or `index` (a flame spread or smoke-developed index). |
| `note` | Why the rule applies to this value, such as the room use that selects it. |

Which value a rule applies to is your judgment. A ceiling-height rule for habitable rooms applies to the rooms whose stated use is habitable (`logs/scope.md`), not to every room with "ceiling" in a key. Write the reason in `note`.

QA converts the drawn value to the rule's unit before it compares: an 84-inch value meets a 7 ft limit, and a value with `unit: sf` meets a limit in `sq ft`. The same-unit-only units never convert: a 50 `cfm` limit checks a drawn value whose `unit` is `cfm`, and a 1.28 `gpf` limit a value in `gpf`. Write the drawn value in the rule's unit, for example `"bath_fan_flow": {"v": 80, "unit": "cfm", "status": "MANUFACTURER", "source": "S4"}`. A slope in `in/ft` compares only with a value in `in/ft`, not with `pct` or `ratio`. `validate` refuses a unit the kit does not know, a unit of another kind than the value (an area limit on a length, a `cfm` limit on a value in `gpm` or `in`), a point value and a duplicate `id`, and QA fails such a rule. It warns when `check.value` names no value yet. `qa-reference.md`, "The QA gate", says what the `rules` check reports.

### Spread rules

Some limits are on the difference between values, not on one value: the tallest riser of a flight may exceed the shortest by no more than 3/8 inch. Write one rule with `check.spread` listing the values instead of one rule per value:

```json
{"id": "R-7", "element": "riser height variation", "citation": "<CODE> <SECTION>", "cd": "CD-009",
 "check": {"spread": ["$riser_1", "$riser_2", "$riser_3", "$riser_4"], "op": "<=", "limit": 0.375, "unit": "in"}}
```

QA reports the spread and names the largest and the smallest value. Each listed value follows the same checks as `check.value` (it must exist, be a number and be the limit's kind). `{rule.value}` in `rule_note` and `rule=` on a 3D dimension refuse a spread rule, since it has no one drawn value.

### Ranges in the rules check

An ASSUMED value with a `range` (`project-file.md`, "Ranges"), or a value DERIVED from one, is tested at every estimate: each mix of the low and high ends of the ranges behind it.

- It breaks the limit at every estimate: the rule **fails**, and so does QA. No measurement inside the estimates could make it pass, so change the design (or, if an estimate is wrong, correct the range and say why in the note). When the owner keeps the design, see "A design the owner keeps". This holds only when every ASSUMED value behind it has a range, its formulas use no `abs`, `hypot`, `min` or `max` over an estimate, and (for a spread) the smallest spread is one of those estimates. Otherwise the rule warns "WOULD FAIL at every estimate" and says why it cannot be sure. A spread of straight lines on one estimate is also checked where two of them are equal, so a stair that is over the limit at every thickness fails.
- It meets the limit at every estimate: the rule passes when every estimate is clear of the limit, and warns when one comes close ("Estimates near the limit" below). A formula that uses `abs`, `hypot`, `min` or `max` warns instead of passing on the ends alone, because a number between them could fail.
- It meets the limit at some estimates: the rule warns and names the end that fails.

An ASSUMED value without a `range` is one estimate. Its rule never fails, because a measurement could still land on either side: it warns "WOULD FAIL", warns "would pass" when the estimate is close to the limit, and passes when the estimate is clear of it. Give it a range when you know how far off it can be.

### Estimates near the limit

An unverified value that meets its limit passes only when it is clear of the limit: at least `check.close` inside it at every estimate, by default 10 % of the limit. A riser estimated at 5 to 5 1/2 in. under a 7 3/4 in. maximum passes; one estimated at 7 1/2 in. warns, and so does a 20 ft height under a 21 ft maximum. Either way its FV tag still prints and it stays on the field-verify list, and no note may claim compliance on it (`kit.claim`). Set `close` yourself when a guess can be far off (a dimension read off an old plan, a load nobody has checked): the farther off it can be, the larger. A rule that `structure` makes keeps warning on any unverified input.

### A design the owner keeps

When the owner keeps a design that breaks a rule and will ask the city for relief (`01-scope.md` section 6), record the decision and put its id in the rule: `"accepted": "DEC-007"`. QA then reports the rule's FAIL as a WARN that starts `ACCEPTED BY OWNER (DEC-007)` and says the city must grant relief, so the set can pass QA and go to CrossBeam and the city with the conflict labeled. A rule that cannot be compared (a point value, a unit of another kind) still fails. If the design changes and the rule passes, QA says so; take `accepted` off. Never use `accepted` without the owner's decision, and never change a limit instead.

### Printed lengths near a limit

A length that a rule caps (`<=`) prints rounded up to the drawing precision, and one with a minimum (`>=`) rounded down, so the printed number never reads better than the value: a 3.711 in. baluster gap under a 4 in. maximum prints 3 3/4", not 3 11/16". A value with both a maximum and a minimum, or with no rule, prints to the nearest 1/16 in. A plain number that a rule caps rounds up the same way.

A rule entry prints nothing itself. It lets QA check the drawing and sets which way the value it names rounds. A note that prints the limit still follows `05-code-questions.md` section 6: its entry must be `quoted` or `primary-read`.

## Code notes

`code_notes` lists the entries in `logs/code-decisions.md` whose quoted rule has conditions (`05-code-questions.md` section 6). Each entry has a `cd` (the entry ID, such as `CD-014`), `conditions` (`true` when the quote has conditions) and an optional `note` (the conditions in a few words). Add an entry when you record the "Conditions in the quote" line of a code decision. The field is optional.

Every note that prints a code limit passes its entry ID with `cd=`, for example `kit.text("...", cd="CD-014")` (`05-code-questions.md` section 6). The ID is recorded in `build.json` and never prints. QA lists each printed note whose `cd=` ID has `conditions: true` in `advisory.conditional_code_notes` (`qa-reference.md`, "Advisory list"). The list never fails QA. You read each note and judge it.
