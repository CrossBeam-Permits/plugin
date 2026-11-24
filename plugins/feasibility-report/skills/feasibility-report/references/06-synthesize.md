# Step 6: Synthesize

## 1. Cross-check with Ask

After steps 2 to 5, call `crossbeam_ask` once with:

- `city` (and `permit_type` when known)
- `facts`: the program, the lot facts from step 2, and the rules you read in steps 3 to 5 with their citations
- `question`: "Here is a proposed <program> on this lot. Is it feasible, on what review path, and what limits, requirements or recent law changes apply that the facts above miss? Name anything above that is wrong."

Follow up with its `conversation_id` for anything it raises; never resend earlier turns. Keep its `conversation_url` for the sources list.

Use the answer this way:

- Its `citations` are lookups it actually read. Read any section it names that you have not read; a cited section not in its `citations` is unverified.
- Its `could_not_confirm` items go straight to the City questions.
- Its `not_found` items are gaps: name them in the report (for example "CrossBeam has no city code for <city>").
- If the answer labels each claim by source (law text, CrossBeam's notes, or its own reading), keep the label: law text becomes `CODE` once you have read the section, CrossBeam's notes become `CROSSBEAM`, its own reading becomes `INFERRED`.

## 2. Ask is a cross-check, not the source

An Ask answer can be wrong. CrossBeam's notes for a city can lag the law. Treat every Ask claim as a lead to confirm against the text you read, not as a finding.

## 3. When sources disagree

1. Law text you read beats Ask, CrossBeam's notes, summaries and memory.
2. A newer law beats an older one; a state law that preempts a local rule beats it (`03-city-code.md` section 3).
3. State the conflict once in the question it affects, tagged `INFERRED`: "One CrossBeam answer said <claim>. That conflicts with <section>, so this report does not rely on it. Confirm with <Building or Planning> at intake."
4. Leave the wrong claim out of the verdict and the summary.

Example: Ask said a new detached ADU needs fire sprinklers as a new dwelling. The state ADU statute says an ADU does not need sprinklers if the main house is not required to have them, and the city code said the same. The report said "not required", tagged both sections `CODE`, and noted the conflicting answer once.

## 4. Build the fit table

One row for each limit that governs this project (from the profile's questions): the limit with its source, what is proposed, and the margin. Use the numbers you read and the program's numbers, nothing else.

| Column | Holds |
|---|---|
| Limit | The rule in a few words and its value, e.g. "Height, detached unit: 16 ft" |
| Proposed | The program's value, e.g. "single story, about 14 ft"; "unknown" when the program does not say |
| Margin | Proposed against the limit, e.g. "100 sf under", "4 ft short", or "to confirm" |
| Status | Fits · Does not fit · To confirm |
| Source | The section (`CODE`), the layer (`CROSSBEAM`) or the visit (`FIELD`) |

A row whose proposed value is unknown, or whose limit you could not read, is "To confirm" and has a City or design question. Never mark a row "Fits" on an assumed value.

## 5. Rank the risks

List every open item that could change the design, the cost or the schedule: the "To confirm" rows, reports not yet ordered, unpermitted existing work, open permits or cases, easements, utility upgrades, hazard-zone requirements, law that changes on a date, and conflicts you set aside. Rank them by what they could cost if they go the wrong way, highest first. For each, give one line: what could happen, roughly how much it moves the cost or schedule in words ("adds a soils report and possibly a deeper foundation"; "a hearing adds months"), and the step that settles it. Never put a dollar figure on a risk without a source for it.

## 6. What would fit

When a row does not fit, or the verdict needs a discretionary approval, say the nearest version of the project that would fit by right (smaller, shorter, moved, a different unit type or path), from the limits you read. Tag it `INFERRED`. Skip this when everything fits.

## 7. Choose the verdict

Pick one (`07-report.md` section 2) from the fit table and the rules you read, not from Ask's summary:

| Verdict | When |
|---|---|
| Feasible by right | Every known limit is met, and the path is ministerial (no hearing) |
| Feasible with conditions | It fits, but one or more open items could change the design (soils, separation, an easement, a survey) |
| Needs a discretionary approval | It needs a variance, a use permit, design review with a hearing, or a coastal permit |
| Not feasible as proposed | A limit you read rules out the program; say what change would make it fit |
| Can't tell yet | A fact the answer turns on is missing (the zone, the parcel, the city code); say which and how to get it |

A verdict that rests on an `INFERRED` claim says so in the summary.
