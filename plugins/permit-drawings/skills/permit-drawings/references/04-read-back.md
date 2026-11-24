# Stage 4: Read back

Read this when the first measurements are in, and before you draw any permit sheet.

## 1. Draw your reading to scale first

Do not describe your reading in words only. Draw it.

1. Build a quick draft plan from `project.json` with the kit. Use true scale.
2. Letter every opening: A, B, C. Letter doors, windows, cased openings and closets.
3. Label every element (E), (N) or demo.
4. Draw each unknown extent as `03-measure.md` section 8 says: ASSUMED with an FV tag when a source gives a number, PLACEHOLDER with an FV tag when none does.
5. Send the draft with a short numbered list of the claims you want confirmed.
6. Add each fact that stage 1 left open, such as the property owner's name or the bedroom count (`01-scope.md` section 2). Ask it once more, in plain words.

Example claims:

1. "The stair goes down toward the street side of the house."
2. "Opening C is a closet. Opening D is the bathroom door."
3. "The wall between the hall and the stair is 5 inches thick."
4. "I assumed the far end of the railing stops at a wall. I tagged it FV-2 so it gets measured."

The owner then answers in short form: "A is the bathroom. G, F and E are closets."

Example: an agent read a hallway sketch, drew it, and lettered every opening A to J. The owner answered with short lines such as "H and I are entryway doors."

## 2. Invite markup

Tell the owner how to correct you: "Take a screenshot of any part that is wrong, circle it, and add one short line." One fix per message is fine.

This was the main correction loop in every successful project. Examples of the owner's lines:

- "This door should swing outward to the right."
- "The railing here goes all the way to the wall."
- "Stairs are on the other side."
- "This should be a wall along the stairs going down."

Apply each correction to `project.json` first. Then rebuild. Then reply with what changed in one or two lines.

## 3. Check orientation and identity

- Test the draft against one feature that is not symmetric (a door near one corner, a stair going one way). Ask the owner to confirm it. A mirrored plan looks correct until you check a feature like this.
- When two elements look alike (two walls with similar windows), confirm which one you drew by a feature the owner can see: "What is under the window on this wall?"
- Ask what each end of each element stops against, for every element that `01-scope.md` section 3, step 4 lists.

Example: an agent drew the wrong wall for an hour. The two walls each had one window. The deciding fact was that one window had a kitchen sink under it and the other had furniture.

Example: an agent "corrected" the compass to explain a measurement that did not fit. The real cause was that it was reading the wrong wall. Never change orientation to make numbers fit.

## 4. Run a refute-first check

For each critical reading, run a second check whose only job is to prove the reading wrong.

Critical readings include:

- stair direction and the side of each rail;
- which wall each opening is on;
- the orientation of each sketch;
- the endpoints of each chain dimension;
- riser count and level changes;
- the (E), (N) or demo status of each element.

How to run it:

1. Re-read the source image for that one reading. Do not read your own draft.
2. Give the checker the owner's answers about that reading from `logs/questions.md`, as evidence.
3. Write the strongest case that the reading is wrong.
4. Every number in the check declares MEASURED, DERIVED or ASSUMED.
5. If the host can run parallel agents, give each critical reading to its own checker.
6. A checker may flag a conflict between the owner's answer and a source. A checker never overturns the owner's answer (section 5).
7. Put each overturned reading and each flagged conflict to the owner once, as a question, not as a fact.

Example: a refute-first pass overturned eight readings, including an invented landing and a riser count off by one. The same pass then claimed a hallway chain closed at a value that the owner later disproved. The owner's on-site answer decided it.

## 5. The owner outranks every agent

- An owner's on-site answer replaces any agent's reading.
- If the owner's answer conflicts with a strong reading, show both with the evidence and ask once. Then accept the answer. This includes a conflict with the owner's own sketch.
- When the owner reports an error that is not there, check before you redraw. Example: an owner said "looks like you missed a window", then confirmed there was only one window. The agent searched first and did not redraw.

## 6. Label inferences

- State each inference as an inference: "I think this is a closet because it is 24 inches deep."
- Use three states for a hazard or an element: confirmed, absent, not observed. Do not call an edge "unguarded" when nobody looked at it.
- Record a reading the owner has not confirmed in `logs/questions.md` as open.
- A label with "or" in it (for example "CASEMENT OR FIXED") is an open question, not a reading. Record it in `logs/questions.md` and ask it. When the owner answers, change the label everywhere it prints (`06-draw-checks.md` section 3).

## Exit condition

- The owner confirmed the draft plan, or each open reading is in `logs/questions.md` with an FV tag.
- The refute-first check ran on every critical reading. The results are in `logs/decisions.md`.
- Every element in the work area shows (E), (N) or demo on the draft.
- Values that are still ASSUMED or PLACEHOLDER go on the site-visit list at the start of stage 6 (`06-draw.md` section 0).
- `logs/release.md` has the line `Stage 4 done`.
