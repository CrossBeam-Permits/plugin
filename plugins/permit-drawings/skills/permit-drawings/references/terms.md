# Terms

The words this skill uses in a fixed sense. `SKILL.md` and every reference use them this way.

- **Owner**: the user. The owner is a homeowner, an owner-builder or a builder. The owner decides scope and signs.
- **Property owner**: the person or entity on the property record. The property owner's name prints in every title block and goes on the application. The property owner can be someone other than the owner, for example a builder's client.
- **City**: the agency that issues the permit. It can be a city or a county.
- **Set**: the drawing sheets plus the documents the city requires.
- **Kit**: the drafting kit in `scripts/permitkit/`. `references/drawing-kit.md` tells you how to use it.
- **project.json**: the one source file for every value in the set. `references/project-file.md` gives its schema.
- **CrossBeam check**: a CrossBeam plan check of the set. It is not a filing with the city.
- **CrossBeam round**: one CrossBeam check of one version of the set (stage 7).
- **City round**: one city plan-check cycle: one submittal to the city and the city's answer (stages 8 and 9). City rounds are numbered from 0.
- **Ask AI**: CrossBeam's open-question chat. The web app labels it **Chat** in the top nav (it was called Ask AI there before November 2026). It answers code and permit questions. Its tool is `crossbeam_ask`. "Ask `crossbeam_ask`" means: send the question with that tool, or, when the tool is missing, through the owner in the CrossBeam web app (`references/00-connect.md` section 4).
- **Rules tool**: `crossbeam_rules`. It returns the rules that apply to the things you draw at one city, each with its limits, its source and `kit_checks` that the kit QA can run. Ask it about the thing ("bedroom emergency escape window"), not a code section. `references/05-code-questions.md` section 0 says how to use it.
- **Rules**: the `rules` list in `project.json`. Each entry checks one drawn value against one limit. The kit QA check `rules` fails a verified value that breaks its limit (`references/project-rules.md`, "Rules").
- **`quoted`**: a citation level. The answer gives the section, the edition and the verbatim text of the section, and that text holds the limit you print. A `crossbeam_rules` rule with `quote_has_values: true` and `confidence: high` is `quoted`. A paraphrase or a summary is `unquoted`. `references/05-code-questions.md` section 3 defines every level.
- **`primary-read`**: a citation level. You read the primary code text of the section in the adopted edition yourself, and recorded the source and the edition (`references/05-code-questions.md` sections 3 and 4).
- **`waiting`**: a citation level. The code question has no answer yet, because the turn failed, the answer was empty, or Ask AI is `rate_limited`. Nothing from it prints (`references/05-code-questions.md` section 2).
- **`owner to supply`**, **`by others: not engaged`**, **`unknown: confirm with the city`**: statuses of a row in `logs/required-documents.md`. `references/02-path.md` section 3, step 6 defines every status. Step 8 says which statuses block a CrossBeam check. `unknown: confirm with the city` can also appear in two other places: the file manifest (`08-package.md` section 2), and `logs/scope.md` for a fact nobody could find, such as earlier permits (`02-path.md` section 1, step 5). Before the city submittal, the owner confirms each one with the city, or approves sending without it (stage 8).
- **Owner-accepted**: the status of a CrossBeam finding that reports a condition the owner knowingly chose, such as an absent document or a value drawn with an FV tag. It closes the finding for the stop rule (`07-crossbeam-check.md` section 8).
- **FV tag**: a field-verify tag, such as `FV-3`. It marks a value that someone must measure on site before construction. The field-verify schedule (`field_verify` in `project.json`) lists each FV tag.
- **Gate**: the release status of the set. `references/10-release.md` defines the five gates. The gate label prints in every title block. Only these five are gates. The site-visit list (stage 6) is not a gate.
