# Stage 3: Measure

Read this before you ask the owner to measure, and each time a new measurement arrives.
Read `project-file.md` for the exact fields, and `project-geometry.md` for walls, openings and recording a measurement. Read `asking-the-owner.md` before you send the checklist.

## 1. Read what you already have

1. Look at every sketch, photo, quote and product sheet in `sources/` before you ask for anything.
2. Rotate each sketch upright. Record which way each sketch faces in the source's `orientation_note`: which compass direction is at the top of the paper, and how you checked it.
3. Enter every number you can read as a value in `project.json`, with its status and source.
4. Search the record before you ask for a number. Never ask the owner to measure a value the owner already gave.

Example: an owner's sketches faced east, not north. The agent did not record this. The main stair stayed drawn 90 degrees wrong for weeks.

Example: an agent told the owner to field-verify two numbers. A later search found that the owner had given both numbers earlier.

## 2. Send a ranked tape checklist

Rank each measurement by how many unknowns one tape closes. Put the highest first.

Example: "Count the risers on the main stair. This one closes four things at once." The riser count fixes total rise, floor-to-floor height, riser height and the stair's length. Add the field tip: "Include the very top and the very bottom step."

For each item on the checklist, say:

- the physical spot, named the way the owner sees it ("the wall with the window over the couch");
- where the tape starts and where it ends ("from the finished wall corner to the edge of the window trim");
- along the floor, or along a slope;
- which floor the height is measured from, if floors differ;
- the decision the number changes.

Ask for 1/4-inch precision. A rough sketch is fine. Show a picture for any item that words alone could confuse. Save each picture you send in `questions/` (`asking-the-owner.md` section 2).

Before the owner goes to measure, send this briefing: "Say which floor each height is measured from. Name each wall the way you think of it, not the way I labeled it."

## 3. Register rules

Every value in `project.json` has these facts:

- the number and the unit;
- the status: MEASURED, DERIVED, ASSUMED, PROPOSED, MANUFACTURER or PLACEHOLDER;
- the source: which sketch, photo, answer or document, and the date;
- what it measures and which object it belongs to (wall A, not "the window wall");
- its two endpoints, and which surface each endpoint touched (finished wall, trim, framing);
- along the floor or along a slope;
- the reference level, for heights.

The Status table in `project-file.md` says when to use each status and how the kit draws it.

An unknown value is PLACEHOLDER, or ASSUMED with an FV tag. Never leave an unknown value out, and never invent one.

- ASSUMED with an FV tag: a value that has one of the sources below. It prints with its FV tag.
- PLACEHOLDER: a value that has no source below. Its number never prints; the kit refuses it. Section 8 says when a sheet may use one to place geometry.

An ASSUMED number needs a source. It is not invented when its `source` and `note` name where it came from:

- a CrossBeam answer (cite the entry in `logs/code-decisions.md`);
- the contractor's quote or a product data sheet in `sources/`;
- the owner's estimate, in the owner's words;
- a nominal size from one of these sources, for example a wall thickness that the contractor's quote states.

A CrossBeam answer can give a number that is not a code fact. This applies only to an existing-condition value that someone could measure on site, such as the thickness of an existing wall. Record it as ASSUMED with an FV tag. Its source is the answer, saved as `05-code-questions.md` section 3 says. It needs no citation level, because it prints as a dimension with its FV tag and never as a code limit. If the answer says the number is unverified, write that in `note`. A value that a code table or a code rule governs (for example a header size, a span or a fastener spacing) is a code fact. It needs a citation level (`05-code-questions.md` section 3) before it prints.

Sometimes the drawing needs a value and no source above gives it. Then do this:

1. Propose a draft value to the owner. Say what it is based on (for example, a scaled sketch or a photo) and say that it is not a measurement.
2. Ask the owner to accept it or to give another number.
3. When the owner accepts it, record it as ASSUMED with an FV tag. The source is the owner's estimate. Put the owner's words and your draft in `note`.
4. Until the owner answers, the value blocks only the work that depends on it.

Your draft alone is never a source. Do not record a number from your memory of typical construction as a source.

An owner's estimate is not a tape value. "About 50" or "pretty sure it's 216" is ASSUMED with an FV tag, with the owner's words in `note`, until the owner tapes it. Draw the number the owner gave.

If the owner cannot measure now, do not wait. Use ASSUMED (with its source and an FV tag) for each value that has a source, PLACEHOLDER for each value that has none (section 8), and ask again in the next batch. Stage 6 section 0 gives the owner one site-visit list before the permit sheets are drawn.

A DERIVED value records its arithmetic. Never derive a length by subtracting two lengths measured along different axes.

If the owner gives a rounded value ("about 33 inches"), draw that value. Do not replace it with a value that looks more buildable. If you need another value, mark it ASSUMED and ask.

## 4. Close every chain before you draw

1. Sum each chain of dimensions along a wall. Compare it with the overall dimension.
2. If the chain closes, record it.
3. If it does not close, look for the cause: a misread digit, a missing segment, a different endpoint. Ask about a digit only when the chain fails to close.
4. When the owner accepts a small closure error, put it in a wall segment. Never put it in an opening. Record the choice in `logs/decisions.md`.

Example: one sketch digit could be read 31 or 38. The wall segments summed to the overall 215 only if it was 31. The agent used the closure to read the digit and did not need to ask.

Example: an owner said a room was most likely 18 feet, not his reading one inch short. The agent set the room to 216 inches and put the extra inch in the last wall segment, so every opening size stayed exact.

## 5. When a new value replaces an old one

1. Change the value in `project.json` and its status.
2. Search for the old number everywhere: `project.json`, every sheet script, every note, every form, every log summary, every model file.
3. Fix each dependent value. Re-derive DERIVED values.
4. Rebuild the whole set.
5. Record the change in `logs/decisions.md`: old value, new value, source, every place that changed.

Example: an agent assumed a standard 80-inch door head. The owner then taped 78 inches. The old 80 survived in four places, and a window sill note disagreed with the sheet.

## 6. Scans and photos

- A picture is never a dimension. `photo-to-plans.md` sections 3 and 4 say what a photo gives, what it cannot give, and what to tape.
- A phone scan value is ASSUMED until a tape confirms it.
- Methods are independent only if their inputs are independent. Four scan methods agreed on a wrong window sill because all four read the same view blocked by furniture.
- Read the photos before you analyze scan numbers. A photo often answers the question at once.
- Ask what furniture and objects are in the room before you read low geometry. Furniture is not a wall.
- Never change the orientation or the datum to make numbers fit. If a fit needs a flip, suspect your reading instead.
- Do not build a theory on a number you just received. Confirm a surprising number first.

## 7. Existing devices where the work touches

When walls are added, moved or opened, or a room's use changes, record what is already on those walls and in that room:

- lights and their switches;
- receptacles;
- smoke and carbon monoxide alarms;
- heating and cooling units, registers and thermostats.

1. Record each device as an element with an `action` (`existing`, `relocate` or `demo`) and its position. A position nobody taped is ASSUMED with an FV tag.
2. The owner's counts and descriptions are evidence. Ask for positions with a picture of your draft (`asking-the-owner.md`).
3. Do not add a new device the owner did not ask for (`01-scope.md` section 4).

`06-draw-checks.md` section 2 uses this list to decide which plan sheets to draw.

## 8. Unknown extents

An unknown extent is a length or a position that nobody measured, such as where a wall piece ends or where a door sits in a wall. The drawing needs it to place the element.

1. If a source in section 3 gives a number, record it as ASSUMED with an FV tag.
2. If no source gives one, propose a draft value to the owner (section 3). When the owner accepts it, it is ASSUMED with an FV tag.
3. If the owner cannot give or accept a number yet, record it as PLACEHOLDER with an FV tag. A sheet script may use it only to place the element. The kit draws it grey with a dash-dot line and refuses to print its number. Print the FV tag beside the element. Add it to the field-verify schedule. `06-draw.md` section 0 puts it on the site-visit list.
4. Never draw an element that no source shows. A landing or a wall that nobody measured can change other values without warning.

## 9. The field-verify schedule

Each ASSUMED value that prints gets an FV tag and a row in the field-verify schedule (`field_verify` in `project.json`): tag, what to measure, why it matters, rank. The kit prints the schedule on a sheet. A row closes only when a tape value replaces the assumption. Record who closed it and when in the row's `signed_off` entry.

## Exit condition

- Every value the set needs is in `project.json` with a status and a source.
- When the work touches walls or changes a room's use, the existing devices there are recorded (section 7).
- Every chain closes, or its closure error sits in a recorded wall segment.
- Every sketch has a recorded orientation.
- The field-verify schedule is ranked.
- `logs/release.md` has the line `Stage 3 done`.
