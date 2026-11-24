# Stage 8: Package

Read this when the CrossBeam check meets its stop rule (`07-crossbeam-check.md` section 8), and before anything goes to the city. This stage builds city round 0.

A package that does not follow the city's instructions can cost a full city round with no technical content.
Example: an owner sent one combined PDF. The city wanted separate files. The owner lost about two weeks.

## 0. Filing through a city plugin

Read `logs/setup.md`. When it names a city plugin (`00-connect.md` section 8), the plugin is the filing step, and this stage changes in these places:

- Section 2: the manifest lists the city's forms as the plugin's rows.
- Section 3: the plugin fills the city's application forms. You fill only the documents this skill prepares.
- Section 3, step 6: you do not ask the send question. The plugin asks it once, with the final submit.
- Section 4: you get signatures only on this skill's documents.
- Section 6 does not apply. Section 7 replaces it: write the hand-off bundle and stop before anything goes to the city.
- The exit condition is the plugin-mode one.

Everything else is the same: the packaging rules, the build at the city's sheet size, and the package check. `city-plugin-handoff.md` is the contract. The Laguna Beach plugin is the first one; any city plugin that follows the contract works the same way.

## 1. Get the city's submittal instructions

1. Ask CrossBeam for the city's submittal requirements for this permit type. Call `crossbeam_get_review_requirements` and read `packaging_rules`. If it says `coverage: none`, CrossBeam has no packaging rules for this city: go on to step 2. If the tool does not exist, ask `crossbeam_ask`. Some cities' `packaging_rules` include plan-set standards (sheets per scope, cover and title-block content, north arrows, legends, scales). Stage 2 put them in the Sheet content plan. Check here that the set meets each one.
2. If the host has web access, read the city's own submittal page. Record the URL and the date.
3. Read every instruction the city already sent: emails, checklists, intake notes.
4. If no source states a packaging rule, write `unknown: confirm with the city` in the manifest. Ask the owner to check the city's page or call the city. Give the owner the exact questions:
   - "Do you want one PDF or separate PDFs? Which documents go in which file?"
   - "What sheet size do you require?"
   - "How do I submit: portal, email or counter?"
   - "Which forms must be signed, and by whom?"
5. Record each answer and its source in `logs/city.md`.

## 2. Build the file manifest

Write the manifest for city round 0 in `package/round-0/manifest.md`. One row per file:

| # | File name | Contents (sheets or forms) | Order inside | Sheet size | Separate or combined | Rule source | Status |
|---|---|---|---|---|---|---|---|

Rules:

- Follow the city's file split exactly. Never combine files the city wants separate. Never split a file the city wants combined.
- Number and name files the way the city asks. If the city gives no rule, use `NN-<document>.pdf` so the order is clear.
- Use the sheet size the city asks for. Build at that size. Do not rely on a printer to rescale.
- Put product data where the city or the sheet note says (for example, "follows sheet A-5").
- For a resubmittal, add the response sheet and mirror the original file list (`09-city-corrections.md`).
- With a city plugin, add one row for each city application form and portal answer, with the status `by city plugin (<plugin>)`. Those files are not in this skill's package. The plugin's portal categories decide the upload slots; the city's rules still decide the file split you build.

## 3. Fill the forms

With a city plugin, skip steps 1 to 4 for the city's application forms. The plugin fills them from the city's current form. Do steps 1 to 4 for every other form this skill prepares.

1. Get each form's current version from the official source. If a direct download fails, use the host's browser tool, or give the owner the link.
2. Fill each field from `project.json`, `logs/scope.md` or a cited source. Every value must trace to a sheet or a source document.
3. Leave each field you cannot trace empty and list it for the owner.
4. Use the scope statement from `logs/scope.md` word for word where the form asks for a description.
   Title 24 energy forms (CF1R) are not filled by this skill: the T sheet's CF1R worksheet lists the entries, and the documentation author fills and signs the state form or the CBECC-Res report, registered with an ECC-Provider when the sheet says so (`energy-and-green.md` sections 1 and 5). Attach the signed CF1R in `sheets` with `attach`.
5. Resolve every row in the Documents table of `logs/required-documents.md` that is `owner to supply`, `owner to sign`, `by others (<who>)` without the file in hand, `by others: not engaged` or `unknown: confirm with the city`. Each one becomes `done`, `by others (<who>)` with the file in hand, or `not required (source)`. For the "Preparer statement" row, the city's written instruction (an email, a checklist or a counter note, cited by source and date) is a source that closes the row (`02-path.md` section 2, step 6). This stage resolves only documents that are not drawing sheets. Sheet content plan rows and deferred decisions change the sheets, so they resolved in stage 7 (`07-crossbeam-check.md` section 8). A row at `by city plugin (<plugin>)` stays as it is. The plugin closes it.
6. Some items can stay open: a row from step 5 the owner cannot close, an `unknown: confirm with the city` in the manifest or in `logs/scope.md`, each item the owner chose to send open in stage 7 (`07-crossbeam-check.md` section 8), each `connections` entry still `open` (`kit-elevations-sections.md`), and each number the sheets print unmeasured. A city approves measured numbers, so before you call the set ready to file, run `python3 -m permitkit measure project.json --out questions/measure-list.md` on the city build and put its rows in the message as one "measure these" list, first rows first: they are the numbers a code rule rests on. Offer a site visit before sending; the owner may measure some, all or none. The owner decides whether to send with the rest. Send the owner one message that lists each open item. Say once that the city may reject the submittal or return it for these items. Ask: "Send to the city with these items open?" Record the answer, the owner's words and the list in `logs/decisions.md`. If the owner says yes, go on. If not, record "Waiting on owner: <item>" in `logs/release.md` and stop until the item arrives.

   With a city plugin, do not send this message. Put each open item in the bundle's `open_items` (`city-plugin-handoff.md` section 5). Items that change the sheets already carry the owner's stage 7 decision. The plugin names the rest in its one submit question, and says once that the city may reject or return the submittal for them.

Check these before you finish. With a city plugin, check them for this skill's documents, and the plugin checks its forms against the same scope statement and sheets:

- **Scope match**: every item on the form appears on the sheets, and every item on the sheets appears on the form. Example: an application still listed dimmers and receptacles after the sheets dropped them.
- **Sheet index match**: every sheet in `logs/sheet-index.md` is in the package, or its row says `by others (<who>)` with the file in hand or `not required (source)`. A structural, energy or green sheet that dropped out without a source goes back to stage 6.
- **Fee lines**: each fee line matches a sheet note. Example: an agent chose a "new branch circuit" fee line while the panel note said "no new branch circuits." The owner asked, "Tell me where in the plan this is true?" It was not true.
- **Builder match**: the plans, the application and every declaration name the same builder. If the owner is the owner-builder, no sheet names a contractor as the builder. Example: the plans named a contractor while the forms said owner-builder. The agent had to explain it in the email.
- **Valuation**: use the owner's value and its source. Never invent one.

## 4. Signatures

- The owner signs every owner signature and every declaration.
- With a city plugin, this section covers only the documents this skill prepared. Get each signature before the file's hash goes in the bundle. The plugin handles the signatures on the city's forms and the portal attestation.
- You may place an image of the owner's signature only when the owner gives explicit consent for that one document. Ask again for each document.
- Never reuse a signature from one document on another without consent.
- Record each consent in `logs/decisions.md`: document, date, the owner's words.

## 5. Check the package

No CrossBeam tool checks city packaging. `crossbeam_validate_review_draft` checks only that a CrossBeam check can run. This section is the packaging check.

1. Set the gate PERMIT REVIEW. Confirm its evidence in `10-release.md`. Set `project.status_label` in `project.json` to the PERMIT REVIEW label, or to the city's required designation. Record the gate change in `logs/release.md`.
2. Change nothing else on the sheets since the passing CrossBeam round, except these: the label, the city's sheet size, replacing `OWNER NAME PENDING` with the property owner's name (`project.owner`), and setting or removing the preparer statement (`project.preparer.statement`) when step 5 of section 3 resolves the "Preparer statement" row. If anything else must change, go back to stage 7.
3. Run a full build at the city's sheet size: `python3 -m permitkit build project.json`. Run the kit QA.
4. Assemble each file in the manifest.
5. Do a vision pass on every page of every file. Look for clipping, overlap and signature dates that run into the city stamp area.
6. Compare the assembled files with the manifest: file count, names, order, page counts, page sizes.
7. Check each file's size against the sending channel. With a city plugin, the channel is the plugin's portal upload. Leave the file as it is unless the city's rules give a size limit. Email tools can fail on large attachments. If a file is too large, offer the city's portal or a browser upload. Compress only if the city accepts it and the scale stays true.
8. Record the file hashes (the SHA-256 of each file) in `logs/city.md`.

## 6. Prepare the send

Skip this section when a city plugin is the filing step. Go to section 7.

1. Draft the email or portal entries: recipient, subject, body, attachments in manifest order.
2. Keep the body short: address, permit type, scope statement, list of attached files, the owner's contact.
3. Show the owner the draft and the manifest.
4. Ask for fresh approval: "Send these <n> files to <recipient> now?" Name each file.
5. Send only after a clear yes. If the owner sends it, record that.
6. Record the send in `logs/city.md`: date, channel, recipient, files, hashes.
7. Copy the sent files to `package/round-0/sent/`. Never change them.

## 7. Hand off to the city plugin

Do this only when a city plugin is the filing step. Never send anything to the city from this skill in this mode.

1. Create `package/round-0/handoff/`. Copy into it the plan set, every other file in the manifest that this skill prepared, and `project.json`. Keep the names from the manifest.
2. Write `handoff.json` with `kind: drawn_set` and `city_round: 0`. In city round 0 every file has `upload: true` and `replaces: null`. `city-plugin-handoff.md` sections 3 to 6 say what each field holds. Fill `facts` from `project.json` and the logs, with each source. Keep unknowns `null` with a reason. Mark applicant-controlled facts. Never put a computed valuation in it.
3. Check the bundle against `schemas/city-plugin-handoff.schema.json`. Check that each file's SHA-256 matches `logs/city.md` and that the plan set's hash is one of the `files`. Fix the bundle, not the schema.
4. Record the hand-off in `logs/city.md`: date, plugin, bundle path, the SHA-256 of `handoff.json`, and each file hash.
5. Tell the owner in three lines or fewer: the set is ready for the <city> plugin, where the bundle is, and that the plugin will ask about the filing route, the city forms, any open items and the final submit.
6. Stop. Do not copy files to `package/round-0/sent/` yet. When the plugin reports the filing (its receipt names the record and the uploaded files with their hashes), copy the uploaded files from the bundle to `package/round-0/sent/`, and record the record number and the date in `logs/city.md`. A file whose uploaded hash differs from the bundle hash is a question for the plugin. Record it in `logs/disputes.md` and tell the owner.

## Exit condition

Without a city plugin:

- The manifest has a rule source or an `unknown: confirm with the city` answer for every row. The owner resolved each unknown, or approved sending without it (section 3, step 6).
- Every form value traces to a sheet or a source.
- Plans, forms and declarations agree on scope and builder.
- Each item still open is in the owner's send approval in `logs/decisions.md` (section 3, step 6).
- The owner approved the send, and `logs/city.md` records it.
- `logs/release.md` shows the gate `PERMIT REVIEW` (see `10-release.md`) and has the line `Stage 8 done`.

With a city plugin:

- The manifest has a rule source or an `unknown: confirm with the city` answer for every row, and a `by city plugin (<plugin>)` row for each city form.
- Every value in this skill's documents traces to a sheet or a source.
- The owner signed what the owner must sign on this skill's documents.
- `package/round-0/handoff/handoff.json` passes the schema, its file hashes match, and `logs/city.md` records the hand-off.
- `logs/release.md` shows the gate `PERMIT REVIEW` and has the line `Stage 8 done — handed to <plugin>`.
