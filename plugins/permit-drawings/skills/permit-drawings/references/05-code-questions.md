# Stage 5: Code questions

Read this before you fix any dimension, note or detail that a code rule controls. Come back each time a new one appears.

## 0. Start with `crossbeam_rules` for drawing values

`crossbeam_rules` returns the rules that apply to the things you draw, at one city. Ask it about the thing, not about a code section: "bedroom emergency escape window", not "R310". Use it first for every number a sheet must meet (sizes, heights, clearances, areas, counts). Keep `crossbeam_ask` for open questions (section 1).

1. List the elements on the sheets. Take them from `logs/scope.md`, the Sheet content plan in `logs/required-documents.md`, and the (N) and changed items in `project.json`. Write each one in plain words with the use that selects its rule: "office ceiling height (habitable room)", "new bathroom exhaust fan", "new interior door to bedroom", "stair from garage to kitchen". Write the room use the owner stated, never a use you guessed.
2. Make one call per city with every element: `city`, `address`, `permit_type` (the ID from `logs/scope.md`) or `scope` (the scope statement) when there is no ID, `elements` (up to 12 per call; make a second call for more), and `site` with the site facts you have: `zone`, `lot_width_ft`, `lot_depth_ft`, `coastal` (true or false; leave it out when unknown), `fire_zone`, and `notes` for anything else (year built, stories, slope, corner lot). Do not call once per element.
3. Read each rule: `requirement`, `values` (each with its comparator, unit and `applies_when`), `exceptions`, `source` (`from`, `citation`, `edition`, `quote`), `confidence`, `quote_has_values` and `kit_checks`. One element can come back as several rules, one per quote; read each one.
4. Record each rule as an entry in `logs/code-decisions.md` (section 3). Write "Asked through: crossbeam_rules", the call date, the element, the `confidence` and the `quote_has_values`. Grade it with the citation levels in section 3:
   - `quote_has_values` is `true` and `confidence` is `high`: the rule is `quoted`. CrossBeam checked that the quote is word for word in the cited source and that it writes each number in `values`. Copy `source.quote` word for word into the entry's Citations line (a ` … ` in it marks source text CrossBeam skipped between two verbatim pieces; keep it) with `source.citation` and `source.edition` (or the response's `code_basis` when the source gives no edition). Each value in `values` may print as a limit, with its citation and its `applies_when` condition (section 6).
   - anything else (`quote_has_values` is `false`, `confidence` is `medium` or `low`, no quote, or no citation): the rule is `unquoted`. Its limits do not print until you get the quote: ask `crossbeam_ask` to quote the section, or read the primary text (section 4). The response `notes` say what the check found.
   - A `false` on a quote that looks right: read the section with `crossbeam_lookup_code` (section 4) before you ask again. Older indexed text sometimes ran a mixed fraction together (`73/4` for 7-3/4, `11/2` for 1-1/2), so the value check missed a correct number. If the primary text gives the limit, and its metric value agrees when it gives one (`7-3/4 inches (196 mm)`), record the entry as `primary-read`; the limit may print.
   A limit you print is always one that the recorded quote writes. Never print a number from `requirement`, `notes` or your memory.
5. Copy the `kit_checks` into `rules` in `project.json` (`project-rules.md`, "Rules"). For each item, decide which drawn value it checks, and write one entry per value: `kit_key` = the item's `key`, `check.value` = the `$key` of the drawn value, `op` = `op`, `limit` = `value`, `unit` = `unit`. Copy `citation` and `source_from` from `source`, and `cd` from the entry. When the drawn value does not exist yet, add it to `project.json` (PLACEHOLDER until someone measures it). An `unquoted` rule may still go into `rules`: the check prints nothing. It only tells you early that the drawing misses.
6. A value with `applies_when` is a rule with conditions. Decide from the evidence which branch applies, write the branch in the entry, and follow section 6. A rule with `exceptions` is a code decision only when you rely on the exception (section 7).
7. Ask `crossbeam_ask` (section 2) for:
   - each element in `misses` (CrossBeam had no rule for it). A miss does not mean no rule applies;
   - a rule with `confidence: low`, or one whose `applies_when` turns on a fact you cannot settle;
   - a rule whose `quote_has_values` is `false` or whose `confidence` is `medium`, when you need to print its limit: "Quote the section and the text that gives <the limit> for <the element> in <edition>.";
   - a value with no `kit_checks` item (text, or a unit the kit does not compare, such as kW or Btu/h): record it in the entry and print it as section 6 says. Amps, cfm, gpm, gpf, psf, psi, lb, mph, degF, U-factor, slope in in/ft and a flame spread or smoke-developed index do get kit checks; they compare only against a drawn value in the same unit. Hours and days (a fire rating, a cure time) get kit checks too;
   - every question that is not a drawing value: whether a permit is needed, who may prepare, whether the work triggers an upgrade, whether an exception applies.
8. After QA, read the `rules` check (`qa-reference.md`, "The QA gate"). A FAIL is a design problem. Tell the owner and give the options in `01-scope.md` section 6. When the owner keeps the design, the rule gets `accepted` and QA reports it as a WARN (`project-rules.md`, "A design the owner keeps"). A WARN on an ASSUMED value that "WOULD FAIL", or that fails at one end of its range, goes first on the site-visit list (`06-draw.md` section 0). When you know how far an estimate can be off, give it a `range` (`project-file.md`, "Ranges"), so QA can tell a sure failure from a maybe.

Errors. `rules_rate_limited`: the daily allowance is used up. Use `crossbeam_ask` for the most important elements, or wait, and record the rules as `waiting`. A knowledge-base or model error (503, 502): try once more, then use `crossbeam_ask`. An unknown `permit_type` error lists the valid types: pick the one that fits the scope (`01-scope.md` section 5) and call again.

When the tool is missing, ask `crossbeam_ask` the same element list in one numbered question: "For each element, give the requirement, each limit with its unit and conditions, and the section, edition and verbatim text." Or the owner asks it in the CrossBeam web app (section 2). Then write the `rules` entries yourself from each `quoted` limit.

When a fact changes (a room use, a permit type, the city), call `crossbeam_rules` again for the elements it touches and update `rules`.

## 1. When to ask `crossbeam_ask`

Ask before you put any of these on a sheet. For a drawing value, ask `crossbeam_rules` first (section 0) and use `crossbeam_ask` for its misses, its low-confidence rules and the rules whose quote does not hold the limit (`quote_has_values: false`):

- a minimum or maximum dimension (room area, ceiling height, egress opening, stair riser and tread, guard and handrail height, landing size, clearances);
- a product requirement (safety glazing, fire rating, energy values). For Title 24 energy limits, start with `permitkit energy` (`energy-and-green.md`): it reads the 2025 CEnC limits from sourced data and lists what it cannot read for you to ask;
- a statement that something is required, not required, exempt or compliant;
- a citation;
- an answer to "do I need a permit", "may I prepare this" or "does this trigger an upgrade";
- a claim that an exception applies ("exempt", "limits do not apply", "not required"). See section 7;
- which minimums (size, ceiling height, egress, light, ventilation) apply to each room's stated use. Ask the question in `01-scope.md` section 6.

Example: in one session nobody asked Ask AI about a railing. The agent's code memory was wrong six times. It mixed up guards and handrails, quoted a state history that it later reversed, and presented a drafting default as a code limit.

## 2. How to ask

Use `crossbeam_ask` (see `00-connect.md`). Write a plain question. Include:

- the jurisdiction and the state;
- the code basis you recorded, or a request to state it;
- the scope and the room use;
- the existing condition and the proposed change;
- the measurements that matter, with their status;
- what you want back: the rule, the section, the edition, any local amendment, and the facts still needed.

Example question: "In <jurisdiction>, for an existing two-storey dwelling, the owner will add a built-in bench next to an 18-inch level change. The drop is MEASURED. Is a guard required at this edge? Which section applies in the current edition? What other facts do you need?"

`crossbeam_ask` can return `status: answering` with a conversation ID. Then call `crossbeam_get_conversation` with that ID until the turn is `done` or `failed`. Wait a few seconds between calls. A `failed` turn is an error. An empty answer is a failed turn too. Never treat either as "no rule applies."

Errors `crossbeam_ask` can return. Each is an error result whose `error` field names it:

- `rate_limited`: the owner's Ask AI allowance is used up. The result gives `resets_at`, the time the allowance resets, and `message`. Stop asking. Tell the owner the `resets_at` time.
- `turn_in_progress`: the conversation is still answering an earlier question. One conversation answers one turn at a time. The result gives the `conversation_id` and the `turn_id` of the turn in progress. Call `crossbeam_get_conversation` with that `conversation_id` until that turn is `done` or `failed`. Then ask.

When a turn fails, ask the same question once more. If it fails again, or the result is `rate_limited`, Ask AI is unavailable for now. Then:

1. Record each unanswered question in `logs/code-decisions.md` as an entry with the level `waiting` and the reason (failed turn, empty answer, or `rate_limited` until `resets_at`).
2. Tell the owner once, in one or two sentences, which questions wait and when you will ask again.
3. Keep working on everything that does not need an answer: measurements, drawing, documents, other questions after the reset.
4. Never print a value, a limit, an exemption or a citation that waits on an answer. Print the requirement as an open item instead, for example "<TOPIC>: TO BE CONFIRMED (CODE QUESTION OPEN)". The printed text says what is open. Pass the entry ID with `cd=` (`drawing-kit.md`); it never prints. Never fill the gap from memory.
5. Ask each waiting question again at each stage exit, when a session resumes (`resume.md`), and before the gate READY TO SUBMIT. After `rate_limited`, wait until `resets_at`. Ask once at each of these points. Do not ask in a loop. A failed turn or an empty answer gets the same retries.
6. At the gate READY TO SUBMIT, list each entry still `waiting` for the owner. The owner decides whether to start a CrossBeam check with those items open (`07-crossbeam-check.md` section 0).

To ask several questions at once, either put them in one numbered question, or start a separate conversation for each (call `crossbeam_ask` without a `conversation_id`). Batch related questions; each answer uses part of the owner's Ask AI allowance.

Keep the conversation ID. Ask follow-ups in the same conversation. If a fact changes, ask again in the same conversation and say what changed.

If Ask AI is not available as a tool, write the question for the owner. The owner asks it on the **Chat** page of the CrossBeam web app and pastes the answer and the conversation link to you. A pasted answer gets a level by the same rules as a tool answer (the levels below).

## 3. Record every answer

Add one entry to `logs/code-decisions.md` for each question. Use `templates/code-decision-log.md`. Each entry has:

- ID, date, the question as sent;
- the conversation ID or link. When the channel gives neither, save the full answer text, word for word, as `sources/askai/AI-<nnn>.md` and use that path;
- the answer in one or two sentences;
- each citation in the answer: code, edition, section, jurisdiction, verbatim quote, link. A tool answer gives them in `citations[]`, which CrossBeam builds from its own code lookups. A pasted answer gives them in its text;
- the `jurisdiction_used` and `edition_used` the answer states. If they differ from the code basis in `logs/code-decisions.md`, ask again with the right city and date. `jurisdiction_used.city_rules: "none"` means no city rule file loaded (normal for a city that runs on its state's code), and `municipal_code: "not_read"` means the answer did not open the city's own code: take local amendments from the code basis, or read them with `crossbeam_municipal_code` (section 4). An answer that gives `city: null` although you passed `city` (servers before November 2026 did) did not say which city it used: record that once in `logs/setup.md`, check that the citations are the code your code basis names, and treat it the same way. Neither one alone is a reason to ask again;
- every unquoted claim (see the levels below);
- whether you read the primary text, and where;
- the facts the answer assumed, with their status;
- the sheets and `project.json` values it affects;
- the sheet note it produces, with each code limit in it;
- a level for each citation and each code limit the note prints.

### Citation levels

Each citation and each code limit (a number such as a minimum area or a maximum riser) has one level:

| Level | Meaning | May it print on a sheet? |
|---|---|---|
| `quoted` | The answer gives the section, the edition and the verbatim text of the section, the edition is the adopted edition, and the quote holds the limit you print. | Yes. |
| `primary-read` | You read the primary code text of that section in the adopted edition (from a tool, the host's browser, or a document the owner gave), and the text holds the limit you print. You recorded the source URL or document and the edition. | Yes. |
| `unquoted` | Anything else: a section number or a limit that appears only in the answer prose, a paraphrase or a summary of a section, any item in the answer's `unverified[]` list, or a quote from another edition. | No. |
| `disputed` | The primary text you read disagrees (section 5). | No, until the dispute is settled. |
| `waiting` | The question has no answer yet: a failed turn, an empty answer, or `rate_limited` (section 2). | No. Print the requirement as an open item. |

The level depends on what the answer contains, not on how it reached you. A `crossbeam_ask` answer and an answer the owner pasted from the web app follow the same rules. A paraphrase or a summary stays `unquoted`, whatever the channel.

A `crossbeam_rules` rule is `quoted` when its `quote_has_values` is `true` and its `confidence` is `high` (section 0, step 4). Then its quote is verbatim text from the cited source and writes each limit in `values`. Any other `crossbeam_rules` rule is `unquoted` until you get the quote.

How to grade an answer that has no `citations[]` list, such as a pasted answer or prose with links:

- A citation is `quoted` only when the text gives the section, the edition, and the section's own words marked as a quote (in quotation marks or a quote block), and those words hold the limit you print.
- A link, a section number or a summary next to a link is `unquoted`. A link is a place to read the primary text (section 4). It is not a quote.
- A table the answer reproduces is `quoted` only for the cells it presents as the table's own text, with the table number and the edition. A number that CrossBeam worked out from a table (by interpolation, a sum, or a choice between rows) is `unquoted`. Ask for the table rows themselves, then print the rows you use, or do the arithmetic in `project.json` as a DERIVED value.

`primary-read` usually adds to `quoted`. It stands alone when CrossBeam does not cover the jurisdiction (`00-connect.md` section 5, step 4) and you read the adopted primary text yourself. Record the source URL and the edition in the entry. Then the entry may print.

These levels are about citations. ASSUMED and the FV tags are about measured values. Do not mix the two words.

To move an `unquoted` item up, ask `crossbeam_ask` in the same conversation: "Quote the section and the text that gives <the limit> for <the topic> in <edition>." Record the answer as a new entry that names the old one.

## 4. Read the primary text when you can

For each answer that changes a dimension or a note, read the cited section in the stated edition if any source gives it to you. `crossbeam_lookup_code` returns a code section, statute or regulation from CrossBeam's indexed text, and `crossbeam_municipal_code` a city's own code by chapter; record the tool, the section and the date as the source. Confirm three things:

1. The jurisdiction and the edition match the project.
2. The conditions in the section match the project (room use, occupancy, height, scope).
3. The number on the sheet matches the number in the text.

Then record the entry as `primary-read`.

If no tool returns the primary text and the host cannot reach it, a `quoted` entry is enough. Check the same three things against the quote. Record "primary text not available" once, with the reason, in the code basis at the top of `logs/code-decisions.md`. Do not repeat it in each entry, and do not treat it as a block.

## 5. Both sides verify

CrossBeam can be wrong. Your memory can be wrong. Neither wins by default.

- If your memory disagrees with CrossBeam, follow the "prove it to yourself" rule in `00-connect.md`.
- If the primary text disagrees with CrossBeam, record it in `logs/disputes.md`. Quote the text. Tell the owner in two sentences. Ask `crossbeam_ask` again, in the same conversation, with the quote.
- Offer to write a short note the owner can send to CrossBeam about the error.

Example: an agent challenged a CrossBeam finding that whole-dwelling ventilation was required. The challenge held, and the approved set carried a note that it was not required, with the citation. In another CrossBeam round, CrossBeam cited an electrical section where a structural section applied. The owner asked, "Are those the right codes? Are you using CrossBeam to make sure it's right?"

## 6. Write the threshold into the note

A note that states the limit survives a wrong section number. Write the rule, the limit and the citation together.

Pattern: `<ELEMENT>: <LIMIT TYPE> <LIMIT VALUE> PER <CODE> <SECTION>`.
Example pattern (values come from CrossBeam): `(N) STEPS: MAX RISER <limit>, MIN TREAD <limit>, PER <code> <section>`.

Where each number in a note comes from:

- A design or measured dimension comes only from `project.json`. Print it with `kit.text` or `kit.claim` (`drawing-kit.md`). Never type it.
- A code limit quoted in a note must match an entry in `logs/code-decisions.md` whose level is `quoted` or `primary-read`, and the limit must appear in that entry's quote. A number from the answer prose alone is `unquoted` and does not print. The note carries the entry's citation. Pass the entry ID with `cd=`, for example `kit.text("...", cd="CD-014")`, so QA can find the note. The ID is metadata and never prints. You may type the limit in the note text.
- `06-draw.md` section 1 gives the same rules for sheet scripts.

Print the arithmetic for each check the reviewer will do: net clear opening area, light and ventilation percentages, total rise divided by riser count. Use the kit's format codes: `{key:sf}` for an area and `{key:explain}` for the arithmetic of a DERIVED value. Do not round a number by hand.

### A rule with conditions

Many quoted rules have conditions. A limit can apply only to one room use. A shorter distance can be allowed only when a stated condition holds. A requirement can depend on a fact such as a fuel type. When the quote that a note prints from has conditions:

1. The note prints the condition with the limit. Or the note states which branch applies and the fact that selects it, with the fact's source (a `project.json` key, a question ID or a document).
2. Never print the limit of one branch without its condition. A reader takes a bare limit as the general rule.
3. If the fact that selects the branch is not known, print the general requirement, or the open question.
4. Record the conditions and the branch you chose in the entry's "Sheet note" line in `logs/code-decisions.md`.
5. Add the entry to `code_notes` in `project.json` with `conditions: true` (`project-rules.md`, "Code notes"). The kit QA then lists each note that passes the entry ID with `cd=` in `advisory.conditional_code_notes`. Read each listed note and check items 1 to 3.

Example: a set printed the shortest alarm distance from a cooktop that a quoted section allows. The section allows that distance only under a stated condition. The note dropped the condition, and the plan did not show the condition was met. A longer distance, the section's general rule, was available on the plan.

## 7. An exception is a code decision

A claim that an exception applies ("<n> SQ FT OR LESS ADDED, LIMITS DO NOT APPLY", "EXEMPT", "NOT REQUIRED") is a code decision like any other.

1. It needs a `quoted` citation for the exception and for each condition of the exception.
2. The sheet prints the arithmetic that shows each condition is met. Print it from `project.json` with `{key:explain}`. Do not type the result.
3. If CrossBeam says a condition is unverified or unclear (for example, whether a window counts as added or as replaced), do not print the conclusion. Print the requirement and the open question. Record the question for the owner or the city.
4. Each fact the exception depends on is MEASURED in `project.json`, or confirmed by the owner's answer or by a document (cite the question ID or the source). If any such fact is ASSUMED, PLACEHOLDER or unknown, do not print the exception. Print the requirement, or the open question with its FV tag or question ID.
5. A "not required" note addresses every trigger the answer named. If the answer names more than one trigger (for example, a fuel-burning appliance and an attached garage), the note shows that each one is absent, each with its fact and source. If any trigger is not settled, do not print the note. Print the requirement. Record each trigger and its fact in the entry, and add the entry to `code_notes` with `conditions: true` (section 6).

Example: a set printed that one kind of alarm was not required because the unit had no fuel-burning appliance. The unit took its hot water from an existing water heater whose fuel and location nobody had recorded. The exception rested on an unknown fact. The note should have printed the requirement, or the open question.

Example: a set printed "TOTAL-AREA LIMITS DO NOT APPLY" for added glass, although CrossBeam had said twice that it was unverified whether one window counted as added. Counted as added, the area was over the limit.

## 8. Answers that suggest added work

A code answer can describe work outside the stated scope: work on another floor, on another wall, a structural upgrade, or stripping existing finishes.

1. Do not draw it yet. Ask `crossbeam_ask` whether the rule requires that work for this scope, or whether it is one option among others.
2. For a structural change to an existing wall, ask the prescriptive-path question in `02-path.md` section 2, step 2. Ask it before you draw new bracing.
3. Give the owner the options as `01-scope.md` section 4 says.

Work that a `quoted` rule requires for the stated scope itself comes with the work. It is not added work. Handle it as `01-scope.md` section 4, step 2 says. If the owner wants to decide an item later, follow `01-scope.md` section 6.

## 9. Never print COMPLIES on an assumed value

- If any input to a check is ASSUMED, do not print COMPLIES, OK, or a check mark.
- Print the requirement and the FV tag instead.
- A compliance claim the inspector disproves is worse than a plain (E) note.

Example: an agent first wrote "(E) solid wood, self-closing, complies" for a garage door it had never seen measured. It later removed the claim and added an FV tag.

## 10. Keep citations consistent across the set

- Use one section number for one topic on every sheet.
- When the edition renumbers a section, update every sheet, every form and every log summary.
- Before each CrossBeam check, read the citation list in the kit's QA report (`qa-reference.md`, "The QA gate") and run the text audit in `06-draw-checks.md` section 3. The kit only extracts citations. You judge whether they agree.

Example: an approved set cited smoke and carbon monoxide alarms under two different section families on two sheets. One family was from the previous edition. The city did not catch it. The next reviewer might.

## 11. Licensed professionals

If an answer says a part of the work needs a licensed professional, first check `logs/decisions.md`. If stage 2 already told the owner about that part, do not say it again. Otherwise follow `02-path.md` section 2: say it once, with the citation, record it in `logs/decisions.md`, and keep helping.

## 12. Rules of thumb are not code

Comfort and design figures (seat depth, place-setting width, walkway comfort) are not code. Label them "design guideline" on any sheet or in any reply. Do not cite a law that does not govern the space.

## 13. Existing conditions

When a drawing shows an existing condition that conflicts with a rule or with a note on an approved set, record it in `logs/decisions.md`. Tell the owner once. Note which declaration the project depends on (for example, the stated use of a room). A declaration states what the owner will actually do (`01-scope.md` section 6). Do not change an approved set to hide it.

## Exit condition

- Every code-controlled dimension and note in the set has an entry in `logs/code-decisions.md`.
- `crossbeam_rules` was called for the elements on the sheets, or its fallback recorded (section 0). Each `kit_checks` item is in `rules` in `project.json` for each drawn value it applies to, and each `misses` element has an Ask AI entry.
- Every code citation and code limit that a sheet prints is `quoted` or `primary-read`.
- `primary-read` is recorded where you read the primary text. If the primary text was not available, that is recorded once in the code basis. It does not block this stage.
- Every exception a sheet relies on has a `quoted` citation and printed arithmetic, and each fact it depends on is MEASURED or confirmed (section 7).
- Every printed limit from a rule with conditions carries its condition, or names its branch and the fact that selects it (section 6).
- No sheet prints a value, limit or exemption from a `waiting` entry (section 2).
- No added work is drawn without the owner's yes (section 8).
- No sheet prints a compliance claim on an ASSUMED value.
- `logs/release.md` has the line `Stage 5 done`. Later code questions come back to this stage without a new stage line. After such a return, run the full text audit again (`06-draw-checks.md` section 3).
