# Stage 7: CrossBeam check

Read this when the set passes kit QA and no row in `logs/required-documents.md` blocks a CrossBeam check (`02-path.md` section 3, step 8). Stage 8 resolves the document rows that stay open. Items that change the sheets resolve in this stage (section 8).

## 0. Open items the set carries

These items wait on the owner or on others, not on you:

- a row in `logs/required-documents.md` at `owner to supply` or `by others: not engaged`;
- a row at `by others (<who>)` whose file is not in hand;
- a code question at `waiting` (`05-code-questions.md` section 2).

The set can also carry items the owner already chose: each value the owner chose to draw with an FV tag (`06-draw.md` section 0), each decision the owner deferred (`01-scope.md` section 6), and each seek-relief choice (`01-scope.md` section 6).

Before the first CrossBeam round, send the owner one message that lists every such item. This message is the one place where the skill tells the owner what CrossBeam will likely flag. Other stages point here and do not repeat it.

"These items are still open: <list>. <For each missing document whose row has no date: About when could you get <document>?> I can start a CrossBeam check now. CrossBeam will likely flag each open item, and the city may too. Or we wait until <the missing documents> arrive. Which do you want?"

For a `waiting` code question, name the note that prints as an open item. Ask "about when" only for a row that has no date and no "no date". Write the answer in the row.

- If the owner approves a check with the open items, record the approval, the owner's words and the list in `logs/crossbeam-rounds.md`. Go on to section 1.
- If the owner wants to wait, or approves only "once it's in", record "Waiting on owner: <document>, by <date or "no date">" in `logs/release.md`. Keep the gate at REVIEW. Tell the owner what to send and what to say when it arrives. Do not write `Stage 7 done`.

The owner's answer stands for later CrossBeam rounds until the owner changes it or the item's status changes. Do not ask again about a carried item. Before a later round, ask only about an item that is new since the last message. The round summary (section 6) lists the carried items. It does not ask about them.

A CrossBeam check is a plan check of the set by CrossBeam. It is not a filing with the city. Each CrossBeam check of one version of the set is one CrossBeam round.

## 1. Set the gate READY TO SUBMIT

Do this once, before the first CrossBeam round.

1. Confirm the READY TO SUBMIT evidence in `10-release.md`.
2. Set `project.status_label` in `project.json` to the READY TO SUBMIT label.
3. Record the gate change in `logs/release.md`.

The label prints in every title block. A label change changes every file hash. So set the label before you build the files you submit.

## 2. Before each CrossBeam round

1. Run a full build: `python3 -m permitkit build project.json`. Never use `--no-determinism` for a build you submit.
2. Run the kit QA: `python3 -m permitkit qa build --out build/qa.json`. Do not submit a set that fails QA.
3. Choose the files to submit:
   - If the build merged the attachments, submit `<set_name>-with-attachments.pdf`. `attachments[].merged_into` in `build/build.json` names it.
   - Otherwise submit `<set_name>.pdf`, and each attachment the build reports as its own file.
   - Add each required document that is not in the set as its own file.
   - List as absent each document the owner approved leaving out, and each `by others (<who>)` row whose file is not in hand (section 0). Name these in the approval request (section 3), so the owner and you read the result knowing they are absent.
4. Record the CrossBeam round number, the file names and the file hashes in `logs/crossbeam-rounds.md`. The file hashes are the SHA-256 of each file you submit. `file_sha256` in `build/build.json` holds them for the set PDF and the sheet PDFs. Compute the others with `shasum -a 256`.

## 3. Submit

A CrossBeam check uses the owner's account and can use credits. The owner approves the price before each submit.

**If the submittal tools exist** (see the tool map in `logs/setup.md`):

1. Call `crossbeam_get_review_requirements` for this city and permit type. Confirm the required documents are in the package.
2. Open the draft for this CrossBeam round:
   - CrossBeam round 1: call `crossbeam_create_review_draft` with the project name (`project.title` in `project.json`) and the file manifest. Record the `project_id`.
   - CrossBeam round 2 and later: call `crossbeam_start_resubmittal` with the same `project_id`. It returns the draft for the new round. Do not create a new project.
3. Upload each file to the signed upload URL that the draft returns, for example with `curl -T <file> "<url>"`. Check each upload succeeded. If the draft returns no upload URL, use the web path below.
4. Call `crossbeam_validate_review_draft` with the `project_id`. This call is CrossBeam's preflight: it checks that a CrossBeam check can run on this package. It does not check city packaging. It returns `ready`, `validation_id`, `package_hash`, `price` and `findings[]`.
5. If `ready` is false, read each item in `findings[]`. Fix the file, or ask the owner one plain question. Then repeat section 2, upload the new files and validate again.
6. Show the owner the `price` and name the files. Submit only after the owner approves that price.
7. Write the `idempotency_key` in `logs/crossbeam-rounds.md` before the call. Use one key per `package_hash`.
8. Call `crossbeam_submit_review` with the `validation_id`, the `package_hash`, the approved price as `confirmed_price`, and the `idempotency_key`.
9. Save the receipt in `logs/crossbeam-rounds.md`: `project_id`, `review_id`, CrossBeam round, `package_hash`, time.
10. If the submit call times out, call `crossbeam_get_review_status` before you do anything else. If you must retry, reuse the same `idempotency_key`. Never submit the same package with a new key.

**If the submittal tools do not exist:**

The web app shows the price to the owner before the check starts. You cannot see it, so you do not approve a price. Your request names the files and who can see them.

1. Tell the owner the path of each file to submit, and the documents that are absent (section 2). Record the SHA-256 of each file in `logs/crossbeam-rounds.md`. This path returns no `package_hash`. Record `package_hash: none (web path)`.
2. Say who can see the files: the owner's CrossBeam account. Say that the web app shows the price before the check starts, and that the owner approves it there.
3. Ask the owner to upload the files in the CrossBeam web app and start the check. For CrossBeam round 2 and later, ask the owner to upload them as a resubmittal on the same project.
4. Ask the owner to tell you when the completion email arrives.

## 4. Wait for completion

- If the host receives task notifications, wait for the notification.
- If `crossbeam_get_review_status` exists, call it every 10 minutes. A check takes about an hour. Do not call it more often.
- Otherwise, wait for the owner to report the CrossBeam email.
- You cannot wake yourself. Before the session ends, tell the owner what to say to resume: "The CrossBeam check finished. Continue the permit drawings."

## 5. Read the results

`templates/crossbeam-findings-prompt.md` gives the owner's prompt for this step.

1. Call `crossbeam_list_projects` to find the project ID, if you do not have it.
2. Call `crossbeam_get_project_summary`. Record the counts by status and the `review_version`.
3. Read the `code_basis` block. If it differs from the code basis in `logs/code-decisions.md`, stop and reconcile.
4. Pull findings in this order with `crossbeam_get_findings`: FAIL, then CORRECTION, then FLAG. Then VERIFY and NEEDS_INFO.
5. For each finding, call `crossbeam_get_finding_detail`. Read the narrative, the code text, the required action and the pins.
6. Use the pins (sheet ID, page, grid cell, position) to find the exact spot on the sheet.
7. Call `crossbeam_get_sheet_annotations` once per CrossBeam round. Confirm that CrossBeam read each sheet as the sheet you meant. A wrong sheet index causes false findings.
8. Use `crossbeam_search_findings` for a topic that spans findings ("egress", "energy", "header").

## 6. Act on each finding

Write one line per finding in `logs/crossbeam-rounds.md`: finding ID, status, the decision, the change, the sheets.

| Finding says | What you do |
|---|---|
| A dimension or note is wrong | Check the citation (stage 5). Change `project.json` or the sheet script. Never patch the PDF. |
| A document is missing | If the owner approved leaving it out (section 0), the finding is owner-accepted (section 8). If its row is `by others (<who>)` or `by others: not engaged`, do not prepare the document yourself. You may prepare the preparer's inputs (`02-path.md` section 4). If the owner may prepare it, prepare it (`02-path.md` section 4), add it to the list, and do not only report it. |
| A value is unclear | Find the value's status. If ASSUMED, ask the owner for a tape (stage 3). |
| A room use or scope fails a rule | Give the owner the options with their results (`01-scope.md` section 6). |
| You believe the finding is wrong | Read the primary text. Record the evidence in `logs/disputes.md`. Tell the owner, and ask whether the owner accepts the dispute. Record the answer in the entry. |
| The finding is advice, not a defect | Record a decision with a reason. Change nothing unless the owner agrees. |

A change can affect other sheets. After each change, check every sheet that uses the same value.

After each round, give the owner a round summary: the counts by status, the changes you made, the owner-accepted findings (section 8), and the carried items (section 0). List the carried items. Do not ask about them again.

## 7. Next CrossBeam round

1. Rebuild the whole set without clouds. Changes made for a CrossBeam finding are not revisions: add no `revisions` entry, no revision cloud and no delta. Clouds start with the first city round (`09-city-corrections.md` section 3). Run the kit QA, the vision pass (`06-draw.md` section 5) and the text audit (`06-draw-checks.md` section 3).
2. Repeat sections 2 and 3. Section 3 step 2 opens the new CrossBeam round with `crossbeam_start_resubmittal`.
3. Compare the new summary with the last one. Confirm that each fixed finding is gone. Look for new findings caused by the changes.

## 8. Stop rule

Stop the loop when both of these are true:

- Every FAIL and CORRECTION is fixed or owner-accepted.
- Every FLAG, VERIFY and NEEDS_INFO has a recorded decision with a reason.

A FAIL or CORRECTION is owner-accepted when it reports a condition that the owner knowingly chose. These choices count:

- a document the owner approved leaving out (section 0);
- a value the owner chose to draw with an FV tag (`06-draw.md` section 0);
- a decision the owner deferred, or a code question at `waiting` that the owner approved checking with (section 0);
- a seek-relief choice (`01-scope.md` section 6);
- a dispute the owner accepted (`logs/disputes.md`).

Record each owner-accepted finding once in `logs/crossbeam-rounds.md`: the finding ID, "owner-accepted", the item (document, FV tag, question ID, decision or dispute ID), and the owner's words. When the owner's words are already in a log, cite that entry. Do not ask the owner again. In a later round, the same finding on the same item stays owner-accepted. It reopens only when the owner changes the choice or the item's status changes.

### Items that change the sheets

Stage 8 changes no sheets (`08-package.md` section 5). So items that change the sheets resolve before the last CrossBeam round. These items are a Sheet content plan row at `open (<what is missing>)` in `logs/required-documents.md`, and a decision the owner deferred (`01-scope.md` section 6).

1. When each remaining FAIL and CORRECTION is fixed or owner-accepted, list these items.
2. Send the owner one message. For each item, the owner chooses: resolve it now, or send it to the city open. Say that a resolved item changes the sheets and needs one more CrossBeam round. Skip an item whose choice `logs/decisions.md` already records.
3. Record each answer in `logs/decisions.md`.
4. Draw each item the owner resolved. Run the next round (section 7).
5. An item the owner sends open stays printed as an open item. Its finding is owner-accepted. Stage 8 lists it in the send approval (`08-package.md` section 3, step 6).

Typical shape: a first CrossBeam round of 9 FAIL, 18 FLAG and 5 PASS, then a set with no FAIL by the third or fourth round.

Do not run a fresh full check after the city sends comments. Use `09-city-corrections.md`.

## Exit condition

- The stop rule in section 8 is met, and the owner chose for each item that changes the sheets (section 8).
- `logs/crossbeam-rounds.md` lists every CrossBeam round with its counts and every finding with its decision.
- `logs/release.md` records the passing CrossBeam round, its `package_hash` (or `none (web path)`) and its file hashes, and has the line `Stage 7 done`.
