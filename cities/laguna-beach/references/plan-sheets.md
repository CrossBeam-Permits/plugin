# Plan sheets: when the applicant has no plan set, or must fix one

Read this when the filing route needs plans and the applicant has none, or when the plans need
fixing: a sheet is missing, the City found the set incomplete, or the City sent plan-check
corrections. Planning types 114 and 182 and Building types 183 and 214 all take a Plans upload
(`references/packaging-checklist.md`, Upload map).

This plugin does not draw permit sheets. It says what Laguna needs, and it can hand the drawing to
CrossBeam's permit-drawings skill when the applicant has the CrossBeam connector. The drawn set then
comes back here for the City forms, the packet and the portal filing.

## 1. Say what Laguna needs

1. Settle the stage and the scope first (`references/process-stage.md`). Which sheets the City wants
   depends on the project type and the review level. Decide both from the evidence, never from words
   in the request.
2. Read the Planning sheet matrix in `requirements/plan-sheet-matrix.*`. It is the City's own table
   of sheets per project type and review level, printed in the Design Review Application
   (document 26714, p. 23,
   https://www.lagunabeachcity.net/home/showpublisheddocument/26714/639216204685500000) and the Zone
   Clearance Application (document 26718, Exhibit C, p. 21,
   https://www.lagunabeachcity.net/home/showpublisheddocument/26718/639216211418770000). Read the
   Building lane's lists from the other files in `requirements/`. Name each sheet, what it shows, and
   whether it is required or depends on a trigger (for example "Grading & Drainage, when grading is
   more than 20 cubic yards"). A project type the matrix does not list has no City list: say so and
   ask the City. Do not borrow the nearest row.
3. If `requirements/` is missing from this install, say which list you could not read and give the
   City application's own link above. Do not write a list from memory.
4. Say once, with the citation, where the law or the City requires a licensed professional:
   - The topographic survey is "prepared, signed, and stamped by a licensed surveyor or civil
     engineer" (Zone Clearance Application, Section V, "Survey"; document 26718).
   - California lets a person who is not a licensed architect or engineer prepare plans for some
     wood-frame buildings, such as a single-family dwelling of not more than two stories and a
     basement. When any part departs from conventional wood-frame construction, the building
     official requires that part from a licensed architect or engineer (Business and Professions
     Code §5537,
     https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=5537,
     and §6737.1,
     https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6737.1).
   Say it once in one or two sentences, record in `permit-work/state/readiness.md` that you said it,
   and do not repeat it. Keep helping with everything else.
5. Offer the ways forward: a designer or architect the applicant hires, CrossBeam permit-drawings
   (section 2), or the applicant's own drawings within the law above. For a professional, write the
   precise sheet brief: each sheet, what it must show, and the source facts you already have.

Keep the sheet list in the drawing register `permit-work/state/drawing-register.md`
(`references/homeowner-journey.md`). When permit-drawings draws the set, its hand-off bundle is the
register. Do not keep a second one.

## 2. With the CrossBeam connector

1. Look for tools whose names start with `crossbeam_`. If there are none, CrossBeam is not connected.
   Say once that the applicant can add the CrossBeam connector to draw the set, and stay in
   section 1.
2. Call `crossbeam_get_skill` with `skill_id: "permit-drawings"`. It returns the skill's files, a
   SHA-256 digest for each, and a bundle version.
3. If `crossbeam_get_skill` is not in the tool list yet, or it says the account is not entitled, tell
   the applicant once: connect CrossBeam and use permit drawings from the CrossBeam app. Then stay in
   section 1. When the drawn set comes back as files, use them as an ordinary plan set.
4. Saving the skill writes outside the project folder. Ask once, naming the folder the host loads
   skills from, the bundle version and the number of files. Write only after a clear yes. Check each
   file against its digest. This approval covers that bundle version; permit-drawings does not ask
   again.
5. Start permit-drawings for this project with Laguna Beach as the city and this plugin as the filing
   step: "Draw the permit set for <address>, City of Laguna Beach, CA. The laguna-beach plugin files
   it." It works in the same `permit-work/` folder, in its own folders (`sources/`, `project.json`,
   `sheets/`, `build/`, `package/`, `history/`, `questions/`). Never write in its folders. It copies
   the originals in `permit-work/input/` into its `sources/`.
6. While it draws, keep working on what does not depend on the drawings: the filing route, contacts
   and the forms' identity fields. Do not answer its questions for the applicant.

## 3. Take the drawn set (hand-off in)

Permit-drawings stage 8 writes `permit-work/package/round-0/handoff/handoff.json` and stops before
anything goes to the City. A resubmittal comes as `package/round-<n>/handoff/handoff.json`.

1. Validate it:
   ```sh
   python3 scripts/validate-json.py --schema schemas/permit-drawings-handoff.schema.json \
     permit-work/package/round-0/handoff/handoff.json
   ```
2. Check, and stop that record on any failure:
   - `city.jurisdiction_id` is `laguna-beach-ca`, `gate` is `PERMIT REVIEW`, and `kind` is `drawn_set`;
   - every file in `files` exists in the bundle folder with its SHA-256 and size;
   - `plan_set.sha256` is one of the `files`, the plan PDF opens without a password and has
     `plan_set.pages` pages.
3. Copy the bundle's files unchanged to `permit-work/input/plans/permit-drawings/round-<n>/`, with
   `project.json` and `handoff.json`. Never edit them. A change goes back to permit-drawings.
4. Record each fact in `state/project-facts.json` with its provenance:
   - `source.kind`: `plan`. Receipt: `kind: file`, `file`: the copied `project.json` (or the log
     file the fact names), `field`: the fact's `source.pointer`, `sheet`: the first of `on_sheets`,
     `note`: "permit-drawings project.json, status <status>, handoff sha256 <hash>".
   - A `null` value stays `null`, with its `null_reason` in `notes`. Never fill it from elsewhere to
     complete a form.
   - An `ASSUMED` value keeps its FV tag in `notes` and a confidence below 1.
   - A fact marked `applicant_controlled` gets `confirmation.required: true`, `status: pending`. Show
     the applicant the value from the drawn set and ask them to confirm it in the normal batch
     (`references/applicant-confirmations.md`). Do not ask them to retype it.
   - A value that disagrees with a fact already in the file goes in `conflicts`. Stop the affected
     consumer and ask (`references/guided-intake.md`, Conflict protocol).
5. Map facts to this plugin's ids by what each fact means, not by its name:

   | Hand-off fact | This plugin's fact |
   |---|---|
   | `site.address` | `site.address` |
   | `owner.name`, `owner.mailing_address` | `owner.name`, `owner.mailing_address` |
   | `preparer.name` (a designer or architect) | `architect_designer.name` |
   | `project.scope_statement` | the source text for each `project.description.<record-id>` |
   | `area.<name>` | a scoped area fact such as `building.residential.addition_sqft`, only when the area measures what that field asks |
   | `contractor.*`, `builder.kind` | `contractor.*`, and the owner-builder question in the applicant batch |
   | `valuation.owner_stated` | a candidate for `project.valuation.<record-id>`; the applicant confirms each record's valuation |

   Never compute a valuation from areas. Laguna computes its own minimum and applies the higher figure.
6. Put `required_documents` rows and `open_items` into `permit-work/state/readiness.md`.
7. Go on with the usual stages: filing route, forms, packet, portal (`SKILL.md` steps 2 to 6).
   - Each record's description must read the same as the scope on the sheets. A difference stops the
     record and goes back to permit-drawings.
   - Upload one plan set for the whole project and reference it from every record that needs plans.
     Laguna breaks the permits off one shared set; separate sets per permit are a City correction.
   - Upload the plan PDF byte for byte. Do not merge, flatten or compress it. If a tool rewrites it,
     record both hashes in `logs/` and check the page count and the first and last page.
   - The 8.5 x 11 energy report may be its own upload. Full-size energy sheets are inside the plan set.
   - In the Gate P5 manifest, list each open item with `owner_decision.status: pending`, and say once
     that the City may reject or return the submittal for them. The Gate P6 question names them:
     "Submit these applications now, with these open items: ...?"
8. After filing, the receipt's `uploaded_files` (name, category, hash) is what permit-drawings mirrors
   on a resubmittal. Keep it.

## 4. City corrections (hand-off back)

After filing, the City may return corrections, an incomplete notice or an approval.

1. Use the applicant's signed-in, user-visible browser to open the existing record. Download each
   City document: the letter or comment list, any red-marked set, any resubmittal form, and the
   notice text. Reading and downloading are not transactions. Never submit, upload or pay here.
2. Save them unchanged in `permit-work/input/city/after-round-<n>/`, where `<n>` is the round the City
   answered (0 for the first filing). Hash each file.
3. Write `permit-work/input/city/after-round-<n>/city-documents.json` (`kind: city_documents`) and
   validate it with the same schema. Fill:
   - `outcome`: `corrections`, `approved` or `other_notice`, from what the City says;
   - `record`: this plugin's record id, the City record number, the portal type, and the status
     exactly as the portal shows it;
   - `city_round_marker`: a round marker the City put on file names, copied exactly, or `null`;
   - `instructions_seen`: each resubmittal instruction you saw, with where you saw it;
   - `original_submittal`: the drawn-set bundle path and the receipt's `uploaded_files`;
   - `due_date`: only a date the City states.
4. Hand it to permit-drawings stage 9: "The City sent corrections. Continue the permit drawings." Do
   not write a response of your own for drawing items.
5. Permit-drawings returns `package/round-<n+1>/handoff/handoff.json`. Validate and check it as in
   section 3. Then:
   - Upload only files with `upload: true`. Put each file that `replaces` an earlier upload into that
     same City category, with the portal's Resubmit action on the existing document, so it becomes a
     new version. A new standalone upload breaks the record's versioning.
   - Make each change in `comments_for_plugin` exactly as written. If you cannot, stop and hand it
     back to permit-drawings before anything goes to the City, so the response sheet stays true.
   - Resubmit into the existing record. Never open a new one. The usual signature and final-submit
     gates apply.
6. On `approved`, hand the bundle to permit-drawings too. It freezes the approved set. Issuance stays
   with this plugin (`references/homeowner-journey.md`).

## 5. Who asks the applicant for which approval

Ask each approval once, on one side.

| Approval | Asked by |
|---|---|
| Save the permit-drawings skill files | This plugin, when it fetched them (section 2) |
| CrossBeam check price, check with open items, items that change the sheets | permit-drawings |
| Signature on documents permit-drawings prepared (sheets, energy forms, response sheet) | permit-drawings |
| Filing route; applicant-controlled facts; valuation | This plugin |
| Signatures on City forms and the portal attestation | This plugin; the applicant signs personally |
| Send with open items, final submit, resubmit | This plugin, in one question at Gate P6 |
| Payment and appointments | This plugin, each one separately |

The contract both sides follow is `schemas/permit-drawings-handoff.schema.json`. It is a
byte-identical copy of the schema permit-drawings ships. Do not edit it here.
