# Asking the owner

Read this before you ask the owner any question, at any stage.

Most owners are not builders. One owner said: "Ask me this in more detail, simpler English, I'm not a builder. Use screenshots of drawings if needed." Questions in jargon got no answer. A picture with two marked spots got both answers in about a minute.

## 1. Before you ask

1. Search the record: `project.json`, `logs/questions.md`, the sources and earlier sessions. Never ask again for a number the owner gave.
2. Ask only what no source holds.
3. Decide what the answer changes. If the answer changes nothing, do not ask.

## 2. Parts of a good question

Each question names:

- **a physical spot** the owner can see and touch ("the step outside the back door");
- **where the tape starts and ends** ("from the floor to the top of the rail");
- **the decision it changes** ("this decides whether the rail must be taller").

Show it as a picture when words could confuse. Draw the spot on your own draft or on the owner's photo. Mark each spot with a number or a colored dot.

How to make the picture from the kit:

1. Mark each spot on a draft sheet with `annot.keynote` (a numbered circle). Keep the marks out of the permit sheets: use a draft sheet, or remove the marks after the answer.
2. Build, then render only that sheet into `questions/`, at 150 dpi or more so the owner can read it: `python3 -m permitkit preview build --sheet A-1 --dpi 150 --out questions --prefix Q-012-`. This writes `questions/Q-012-A-1.png`.
3. If the host can crop an image, crop to the area the question is about. A whole ARCH D sheet is too small to read on a phone.
4. Log the path in `logs/questions.md`.

Keep every picture you send in `questions/`. The build deletes everything in `build/png/`, so a picture there is gone after the next build. `preview` never overwrites a file in `questions/`; use a new prefix for a new picture.

Example that worked: a picture with "Spot 1, the flat part: put your tape on the floor. Spot 2, the sloped part: put your tape on the front edge of that step (the green dot)." The owner answered "Spot 2 is 36 inches" and the next height a minute later.

## 3. Plain words

- Use words the owner uses. Name walls and rooms the way the owner names them.
- Explain any term you must use, in one short clause.
- Do not send a list of technical items. One owner replied to a list with: "What's not resolved? What do you need me to measure?"
- Use the owner's meaning of a word. If you are not sure, ask. Example: an owner said a landing "must be 36 inches" and meant 36 inches all around the step outside the door.

## 4. Question patterns that worked

- **Endpoints**: "Your wall number is 161 inches. Does the tape run from the corner to the top step, or from the corner to the far wall?"
- **Close the chain, with both options**: "Either the wall is 161 and the railing stops 14 inches short of the end, or the railing reaches the end and the wall is 146. Which is it?"
- **Identity**: "Is there another wall in this room with a similar window? What is under the window on this wall?"
- **What it stops against**: "At the far end, what does the railing stop against: a post, a wall, or the top of the stairs?"
- **Numbered readings**: "I can read 'invert' three ways: 1, 2 or 3. Say which one, or mark up the sheet and send it back."
- **One deciding number**: "The one number I need is the stone thickness. It decides whether the seat stays at 18 inches."
- **Default, then confirm**: "I drew it at 18 inches and put the other option on the sheet. Say the word and I will move it."
- **Options with a recommendation**: give two or three options, what each one costs, and which one you would pick for the owner's goal.

## 5. Patterns that failed

- A technical distinction built on a wrong reading. Example: "Was that to the top of the stool or to the bottom of the glass?" asked about the wrong wall. The owner answered, "That's just furniture under that window sill."
- The same open question asked many times with no options. An owner never answered "What are you actually changing here?" after four tries. Give options or draw the choices.
- A question about a number you just received, built into a theory. Confirm a surprising number first.

## 6. Batches

- Group a few related questions. Do not send more than five at once.
- If the host has a structured-question tool, use it for batches. Owners asked for it by name: "Use the question tool." Give multiple-choice options where you can. Include a small diagram if the tool allows it.
- Record each answer in `logs/questions.md` at once. Answers given through a question tool may not appear in the saved transcript.

## 7. Markup

Invite the owner to correct you with a screenshot of your own drawing, a circle, and one short line. Tell the owner this once, early. Treat each markup as an instruction for that spot only.

Example lines: "This door should swing outward to the right." "The railing goes all the way to the wall." "Those stairs need to be rotated 90 degrees."

## 8. Replies to the owner

- Lead with what changed and what you need next.
- Keep background work out of the reply unless it changes something for the owner.
- Say plainly when you were wrong: "That was my drawing error, not the design."
- When you made a design choice the owner did not ask for, name it as a choice and ask.

## 9. The question log

Use `templates/question-log.md`. Each entry has: ID, date, the question, the picture (path), what it decides, the answer, the value updated in `project.json`, and the status (`open`, `answered`, `superseded`).

## Exit condition

- The question is in `logs/questions.md` with a picture path if a picture was sent.
- Each answer is recorded and applied to `project.json` before you ask the next batch.
