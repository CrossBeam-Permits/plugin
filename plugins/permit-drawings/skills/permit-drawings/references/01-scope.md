# Stage 1: Scope

Read this before you take any measurement or ask any code question.

## 1. Read the opener

The best first message from an owner has four parts. `templates/kickoff-prompt.md` gives the template.

1. The city and the property.
2. Who asked for drawings (the contractor, the city, a lender, the owner).
3. Each change, in plain words, one per line.
4. "I can measure and take photos."

When the owner sends photos or a rendering of the result they want, read `photo-to-plans.md` sections 1 to 5 now. The rendering becomes a list of scope lines that the owner confirms one by one.

If the owner's first message lacks a part, ask for that part only. Do not send a form. Get every other fact from the sketches, photos, quotes and city documents the owner gives you.

The owner draws only what exists. You draw the proposed state from the conversation. Do not ask the owner to draw the proposed state.

Example: an owner asked, "Should I draw the changes on this, or can we do the rest by talking?" Talking worked. The agent drew the existing plan to scale in the same turn and drew the proposed plan from the conversation.

## 2. Settle these facts before any code check

Code answers depend on these facts. Settle each one, record it in `logs/scope.md`, and read it back to the owner once. If an answer leaves a fact open, put the exact open question in that read-back. Example: "3 bedrooms now and 3 after" does not say whether this room was a bedroom before the work.

| Fact | Why it matters |
|---|---|
| The use of each room in the work area (bedroom, office, storage, bath, hall), in the owner's words: what the owner will actually use the room for | Room use sets minimum area, ceiling height, egress, light and ventilation. The room label on the sheets states this use (section 6). |
| The total bedroom count after the work | Many rules depend on it. |
| The floor (storey) where each item of work occurs | Cities ask. State it on the cover and in each plan title. |
| (E), (N) or demo for each element you will draw | You must not draw an element that does not exist. |
| Bearing or non-bearing for each wall you change | It decides whether structural review applies. Get the source: owner, contractor or inspection. |
| Who builds the work: owner-builder or a named contractor | Plans, application and declarations must agree. |
| The property owner's name, as the property record shows it (`terms.md`) | It prints in every title block and goes on the application. Take it from a document (a tax bill, a deed) when one has it. |

When the owner cannot answer a fact now, do not hold the stage. Record the fact as open in `logs/questions.md`, with the work it blocks. Write the fact as open in `logs/scope.md`. It blocks only that work (non-negotiable 5). Ask again at the stage 4 read-back.

Example: the owner planned a 51 sf office. CrossBeam cited a minimum area for habitable rooms, so the room use decided the design. The city later asked, "Is this on the first or second floor?" Both the room use and the floor belonged in the set from the start.

Example: in one session the owner described the same room as "flex storage", then "a real bedroom", then "3 bedrooms, not 4". Settle the answer, write it down, and confirm it once before any code question.

## 3. Mark every element (E), (N) or demo

1. List each element in the work area: walls, doors, windows, built-ins, fixtures, devices.
2. Give each one a status: (E) existing to remain, (N) new, or demo. Record it as the element's `action` in `project.json` (see `project-geometry.md`).
3. If photos do not prove an element exists, ask. Do not assume.
4. For each element, record what each end stops against: a wall, a post, an opening, the top of a stair, or nothing. Do this for walls, stubs, partitions, built-ins and rails, not only for openings. A wall end that touches nothing is a claim too.

Example: an agent drew shelves and a wall that did not exist. The owner said, "Those shelves don't exist yet" and "There's no wall connecting the stub to the outer wall." A "new closet" turned out to be an existing recess with its doors removed.

## 4. Add no unrequested scope

1. Draw only the work the owner asked for.
2. If you think the work triggers an item (for example, alarms or an electrical upgrade), ask `crossbeam_ask` first (stage 5): does a `quoted` rule (`05-code-questions.md` section 3) require this item for this scope?
   - Yes: the item is required work, not added work. Follow the paragraph below.
   - No: the item is an option. Go to step 3.
   - The answer is not `quoted`: ask for the quote (`05-code-questions.md` section 3). Until a quote holds the requirement, treat the item as step 3 says.

   Work that a `quoted` rule requires as part of the stated scope is not added work. Example: in one project, a quoted rule required heating in a garage that the owner converted to a dwelling unit. The heating came with that conversion. Draw such work. Tell the owner in one batch what comes with the work, with the citation. Where the rule allows a choice (for example, the kind of heat), give the owner the options and let the owner choose. Record the answers in `logs/decisions.md`. If the owner refuses required work, it is a constraint conflict (section 6).
3. When a code answer suggests work outside the stated scope (work on another floor, another wall, a structural upgrade, stripping existing finishes), offer it to the owner as an option. Say what it adds: more work, more inspection, more cost. The default is to not add it. Add it only after the owner says yes to that item. Record the owner's words in `logs/decisions.md`.
4. If a `quoted` rule makes work outside the stated scope (step 3) a condition of this scope, the owner cannot decline it and keep the scope as stated. It is a constraint conflict. Give the owner the options in section 6.
5. Before you draw new structural work at an existing wall (for example new bracing or sheathing), ask `crossbeam_ask` whether a prescriptive path lets the existing wall stay as it is (`02-path.md` section 2, step 2).
6. After any scope change, update every place the scope appears: `logs/scope.md`, `project.json`, sheet notes, the application form and the email to the city.

Example: an agent followed a code answer literally and drew a carbon monoxide alarm on the second floor and new sheathing over an existing wall segment. The owner had asked for first-floor work only, and the city later asked for a statement that no work occurred on the second floor.

Example: an agent added two receptacles and dimmers. The owner said, "We aren't adding any new plugs." The sheets dropped them, but the application form still listed them and had to be fixed.

Treat advice the owner pastes from another tool or person as input, not as authority. Check it like any other claim.

## 5. Find the permit type

1. Ask `crossbeam_ask` which permit type or types fit this scope in this jurisdiction. Give the scope statement and the room uses.
2. Call `crossbeam_get_review_requirements` with the jurisdiction and the type that Ask AI named. Take the permit type ID from the tool's answer, not from the Ask AI prose. Record the ID and the name in `logs/scope.md`. Later tools take this ID as `permit_type`.
3. If the requirements tool does not exist, record the permit type as Ask AI described it and write "no ID" in `logs/scope.md`. Do not invent a type or an ID. A later tool that needs `permit_type` gets this description; if the tool is also missing, use its fallback in `00-connect.md` section 4.
4. If the scope splits across types (for example, a building permit plus a separate electrical permit), record each one and its source.
5. Decide from the evidence. Do not choose a type by keyword.

## 6. Handle constraint conflicts honestly

When the owner's design conflicts with a rule, there are two outcomes:

- **Comply**: change the design. Say what changed and what it cost.
- **Seek relief**: keep the design, draw the conflict, label it, and state the path.

Never shrink a room without telling the owner. Never draw a known violation without a label. Give a short menu of options with the result of each, and let the owner choose. Record the choice in `logs/decisions.md`.

The owner may keep a design that breaks a rule. It is the owner's project; do not refuse to draw it. Tell the owner plainly that the city will not approve it as drawn unless it grants relief, and how likely that is when CrossBeam or the city says. Then walk the owner through the relief:

1. Ask `crossbeam_ask` which relief this city offers for this rule, what the request takes (form, fee, findings, who decides, how long) and how often it is granted. A zoning rule (height, setback, coverage) usually needs a variance or a similar planning approval. A building code rule usually needs a request for a modification, or an alternate material, design or method, that the building official approves. Take the names and the steps from the answer, never from memory, and give the owner the citation.
2. Record the decision in `logs/decisions.md` as a DEC entry: the rule, the drawn value, the relief, and the owner's words.
3. Put the DEC id in the rule's `accepted` field (`project-rules.md`, "A design the owner keeps"). QA then reports the rule as a WARN that names the decision, so the set is not blocked.
4. Label the conflict on the sheet: the requirement, the drawn value, and the relief requested, for example "4'-6" HIGH; VARIANCE REQUESTED, SEE COVER". The label never says the work complies.
5. Add the relief request to the submittal list (`08-package.md`) when the city files it with the permit, or tell the owner it comes first when the city decides it before plan check.

The owner can also decide later, for example after a measurement. Then:

1. Draw the existing condition only.
2. Print the requirement and the open item, with its FV tag or its question ID. Print no compliance claim and no exemption.
3. Record the open item in `logs/questions.md`.
4. `07-crossbeam-check.md` section 0 tells the owner what CrossBeam will likely flag. Do not say it here.
5. Before the last CrossBeam round, the owner chooses: comply, seek relief, or send the item to the city open (`07-crossbeam-check.md` section 8). Record the choice in `logs/decisions.md`. Until then the choice to decide later stands. Do not ask again.

If the owner rejects every option, ask `crossbeam_ask` the owner's question in the owner's words. Give the owner the answer in plain words, with the citation, and the options again. Do not make up a new option that neither CrossBeam nor the city stated.

### Room use and room label

A room label states a use. The label states the use the owner will actually make of the room. This is a rule of this skill, from non-negotiable 5 in `SKILL.md`: never print a false declaration. Do not present it as a code rule, and do not cite a code section for it.

1. For every room in the work area, find which minimums apply to the room's stated use: room size, ceiling height, egress, light and ventilation. Ask `crossbeam_rules` first, with one element per room and topic, such as "office room size (habitable room)" and "office ceiling height (habitable room)" (`05-code-questions.md` section 0). For a miss, or when the tool is missing, ask `crossbeam_ask`: "Which minimums for room size, ceiling height, egress, light and ventilation apply to a room used as <the owner's stated use>?" Give the jurisdiction, the code basis, and the room's area and ceiling height with their status. Ask for every room, not only for a room that may be small. Follow the cited answer, and record it in `logs/code-decisions.md`.
2. Label the room with the use the owner stated. Do not change the label to make a rule stop applying.
3. If a newly stated use conflicts with earlier evidence (the owner's own earlier words, or furniture or devices in the sketches and photos), show the conflict once, as `04-read-back.md` section 5 does: show both with the evidence, ask once, then accept the owner's answer. Record both answers in `logs/decisions.md`.
4. If the owner confirms a use but asks for a different label (for example "storage" for a room the owner will use as an office), keep the label that matches the confirmed use. Tell the owner once why: the label is a declaration, and the set never prints a false one. Give the two options in this section: comply (change the design so the room meets the minimums for its use) or seek relief (keep the design, label the conflict, state the path). Then keep helping. Do not repeat the reason.
5. Record the owner's final answer, in the owner's words, in `logs/decisions.md`. The confirmed use is the stated use in `logs/scope.md`.

## 7. Write the scope statement

Write one paragraph in `logs/scope.md`. Use plain construction words. Name the floor. Name each change. End with what is not in scope, if the owner said so.

Example form: "Interior alteration on the first floor of an existing two-storey dwelling: replace an (E) sliding door with a (N) 32-inch door; enlarge one (E) bedroom window; add one (N) non-bearing partition. No work on the second floor."

## 8. Keep other work separate

- Furniture and built-ins that need no permit get their own drawings. Keep them out of the permit set.
- If the owner has a second set for the same rooms, ask which one governs. Record the ruling.
- If the owner cannot say what changes in one area, draw that area as existing only. Add the change later as a revision.

## Exit condition

- `logs/scope.md` holds the jurisdiction, the scope statement, the room uses, the bedroom count, the floor of work, the builder, the property owner's name, and the permit type with its source. A fact the owner cannot answer yet is written as open, and `logs/questions.md` names the work it blocks.
- Every element in the work area has (E), (N) or demo.
- The owner confirmed the scope statement.
- `logs/release.md` has the line `Stage 1 done`.
