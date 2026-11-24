# Stage 9: City corrections

Read this when the city sends plan-check comments, a correction letter, or a resubmittal request. Each pass through this stage is one city round. The first resubmittal is city round 1.

The city's documents can reach you two ways: from the owner, or from a city plugin that filed the set (`city-plugin-handoff.md` section 8). The Laguna Beach plugin is the first such plugin. When `logs/setup.md` names a city plugin, the plugin downloads the city's documents and resubmits; this stage answers the comments and hands the revised set back. Section 8 says how.

## 1. Read every city document

1. Save every document the city sent in `sources/city/round-<n>/`, where `<n>` is the city round: the comment list, the red-marked set, any resubmittal form, and the email body.

   When a city plugin sent them, read `permit-work/input/city/after-round-<m>/city-documents.json`, where `<m>` is the city round the city answered. This city round is `<m + 1>`. Check the bundle against `schemas/city-plugin-handoff.schema.json`. Check each file's SHA-256 against the bundle. Copy each file unchanged into `sources/city/round-<m + 1>/`. Record the bundle path, its `record` and its `outcome` in `logs/city.md`. If `outcome` is `approved`, go to `10-release.md` instead. If the bundle names files you cannot find, or a hash differs, stop and ask the owner to download the documents again through the plugin.
2. Read all of them. Instructions often sit in the email body, not in the comment list.
3. Log each comment in `logs/city.md`: comment number, the exact text, the sheet it names, and your reading of what it asks.
4. List every packaging instruction separately: response sheet format, bubbles or clouds, file split, returned red-marked set, editable full set. Add each item in the bundle's `instructions_seen`, with its source.
5. If a comment is unclear, write the question for the owner to ask the plan checker. Do not guess.
6. With a city plugin, decide for each comment whether it asks for a change to the drawings or this skill's documents, or to the filing: the application form, a portal answer, a fee or the record. Read the comment to decide; do not match words. Record the decision and the reason in `logs/city.md`. This stage answers the first kind. The second kind goes to the plugin in `comments_for_plugin` (section 8).

## 2. Change only what the comments ask

- Make the changes each comment asks for. Make no other change.
- If a comment needs a change on more than one sheet, change each sheet and list each one in the response.
- If you find a different problem during the city round, record it in `logs/decisions.md` and tell the owner. Fix it only if the owner decides to. A life-safety conflict needs the owner's deliberate decision.
- Do not renumber citations or rewrite notes the comments did not name.

Example: during a city round, an agent started to change numbers the city had not asked about. The owner said: "We should only focus on the two items the plan reviewer called out. Nothing else should be getting changed if not part of those two items."

## 3. Mark each change

This is the first stage that uses revision clouds. The city reviewed a set and now checks what changed, so every change it sees must be clouded and tagged. Earlier rounds, CrossBeam rounds included, were rebuilt clean (`07-crossbeam-check.md` section 7).


1. Add a revision entry to `revisions` in `project.json`: delta number, date, description, and the changed sheets.
2. In the script of each changed sheet, put `annot.revision_cloud` around each change. The kit draws the cloud and a delta tag with the revision number. Cloud administrative text changes too.
3. The kit prints every listed revision in the title block of every sheet. You add nothing to the title block by hand.
4. Rebuild the whole set.

## 4. Check that nothing else changed

Compare the rebuilt set with the set the city reviewed, page by page.
Every difference must sit inside a cloud. If a difference sits outside a cloud, cloud it and list it, or revert it.

## 5. Check the corrections with CrossBeam

Check against the comment list. Do not run a fresh full check. A fresh full check reviews the whole set again, so it re-reports items the city already accepted. After city comments, use a check scoped to the comment list.

1. If the submittal tools exist, call `crossbeam_start_resubmittal` with the `project_id` from `logs/crossbeam-rounds.md`. It opens a new CrossBeam round on the same project. Upload the revised set and the city's comment list to the draft it returns. Then validate and submit as in `07-crossbeam-check.md` section 3, with the owner's approval of the price.
2. Submit only if the draft offers a check scoped to the comments. If it offers only a full check, do not submit it. Use step 3.
3. Without a scoped check, use `crossbeam_ask`. Ask one question per comment, in one conversation: give the comment, the change and the revised sheet. Ask whether the change answers the comment. Record each answer as in `05-code-questions.md` section 3.
4. If the owner uses the web app, ask the owner to start a corrections check with the city's letter, not a new plan check.
5. After a corrections check finishes, call `crossbeam_get_corrections_letter` with the `project_id`. It returns the response letter that CrossBeam drafted. Use it as a draft for the response sheet in section 6. Check every sentence against `project.json` and the sheets.
6. Record each result in `logs/crossbeam-rounds.md`.

Example: the city cut its comments to two and accepted the rest of the set. A fresh full CrossBeam check then reported 21 corrections across the whole set. A check scoped to the two comments was the right tool.

## 6. Write the response sheet

Use `templates/response-sheet.md` and follow its rules.

Example: a response said "this is the only new opening." The set also enlarged a bedroom window. The owner caught it before it went to the city.

Example: an owner's first resubmittal bounced once because the response sheet was not in the city's format. Read the format rule before you write.

## 7. Mirror the original submittal

1. Open `package/round-0/manifest.md` and the files in `package/round-0/sent/`. With a city plugin, also read `original_submittal.uploaded_files` in the city-documents bundle. It names the city's upload category for each file. A revised file goes back into the same category, as a new version of the same document.
2. Build the resubmittal manifest in `package/round-<n>/manifest.md` with the same file split, names and order.
3. Replace only the files that changed. Add the response sheet and any file the city asked for.
4. If the city asked for the original attachments again, include them unchanged.

Example: a city's comment asked that the attachments match the original submission. The owner asked the agent to find the original submittal and match it file for file.

## 8. Package and send

Without a city plugin: follow `08-package.md` sections 5 and 6. Get fresh approval before you send. Record the send in `logs/city.md`.

With a city plugin: follow `08-package.md` section 5, then hand the set back. Do not send anything to the city.

1. Create `package/round-<n>/handoff/` and copy in the revised files, the response sheet, any file the city asked for, and `project.json`.
2. Write `handoff.json` as `08-package.md` section 7 says, with `city_round: <n>`. For each revised file, set `replaces` to the earlier city round, the earlier file and its city category. Set `corrections_answered` to the city round answered, the path of the city-documents bundle and the response sheet. Always include the current plan set. Set `upload: false` on a file that did not change and that the city did not ask for again. Set `upload: true` on every revised file, the response sheet and each file the city asked for.
3. Put each comment that goes to the plugin (section 1, step 6) in `comments_for_plugin`: its number, its exact text, and the change the plugin will make. The response sheet answers it with that change. The plugin makes exactly that change before it resubmits. If it cannot, it comes back here, and you revise the response line before anything goes to the city.
4. Check the bundle against the schema and record the hand-off in `logs/city.md`. The plugin asks the owner for the resubmit approval. You do not ask it.

## 9. Follow-up city rounds

Each city round repeats this stage. Keep each city round's documents, manifest and sent files in their own folders. Never edit an earlier city round's files.

When the city approves the set, read `10-release.md` and set the gate APPROVED.

## Exit condition

- Every comment has a numbered response that matches a clouded change, or a cited reason.
- No change sits outside a cloud.
- The resubmittal file list mirrors the original, plus the response sheet and any file the city asked for.
- Without a city plugin: the owner approved the send, and `logs/city.md` records it. `logs/release.md` has the line `Stage 9 done — city round <n> sent`.
- With a city plugin: `package/round-<n>/handoff/handoff.json` passes the schema, each comment for the plugin is in `comments_for_plugin`, and `logs/city.md` records the hand-off. `logs/release.md` has the line `Stage 9 done — city round <n> handed to <plugin>`.
