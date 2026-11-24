# project.json: geometry, expressions, chains, measurements

Topic card for `project-file.md`. Read it when you write `walls`, `openings` or other geometry items, an `expr`, a `chains` entry, `axes.true_north_deg`, or a taped measurement.

## Geometry items and names

Geometry items (`walls`, `openings`, `rooms`, `stairs`, `guards`, `fixtures`, `levels`) hold Values inline or refer to a key with `"$key"`. The kit gives an inline Value a key from its path, for example `openings.W-1.height`. An inline Value is checked like any other: a status must be one of the six (`project-file.md`, "Status"), in capitals.

Names:

- A key in `values` uses letters, digits and underscores only, such as `win_w`.
- An item or chain `id` uses letters, digits, underscores and hyphens, such as `W-1`. It has no dot, because it becomes part of a key.
- A field name inside an item uses letters, digits and underscores, such as `sill`.
- A note writes an inline key in full, such as `{openings.W-1.width:in}`. A reference writes it as `"$openings.W-1.width"`.

## Walls and openings

- An item in `walls` has an `id`, an `action`, and the Values that describe it, for example `t` (thickness), `length` and `start`. Give each wall an `id` you can name on site, such as `N` or `hall-N`.
- An opening's `wall` is the `id` of the wall item it sits in. When `walls` is not empty, `validate` warns if no wall has that `id`.
- An opening's `type` is one of `door`, `window`, `slider`, `bifold`, `bypass`, `cased`, `dutch_door`, `pocket`, `overhead` (a garage door) and `skylight`. `symbols.opening_tag` (also `annot.opening_tag`) draws `window` and `skylight` as windows (hexagon) and the rest as doors (circle); `tag_shape` overrides. `Panel.opening_schedule` prints the tag, `desc` (or the action and `type`), `width`, `height`, `sill`, `head` and `note`.
- An existing opening whose door leaf was removed is `type: "cased"` with `action: "existing"`. Say in `note` that the leaf is gone.
- The sheet scripts draw the walls and openings. These lists record what the scripts draw, so a reader and `validate` can check the names.

Each geometry item may have an `action`:

| `action` | Meaning | Sheet mark |
|---|---|---|
| `existing` | Existing construction to remain. | (E) |
| `new` | New construction. | (N) |
| `demo` | Existing construction to remove. | demo |
| `relocate` | Existing equipment or construction moved to a new place. | (E), relocated |

Use `existing` for (E) existing to remain. There is no separate `remain` value.

## True north

Set `axes.true_north_deg` when true north differs from plan north (degrees clockwise from plan north). Write it as a Value with a status, like any other number: `{"v": 22, "unit": "deg", "status": "ASSUMED", "fv": "FV-4", "note": "phone compass"}`. `v` is one number, not a point, and `unit` (if given) is `deg`; anything else is a validation error. A plain number is still accepted, but it has no status. `p.true_north` returns it, and `annot.north_arrow(..., value=p.true_north)` prints an ASSUMED north with its FV tag (`kit-site.md`).

## Expressions

`expr` allows numbers, value keys, `+ - * /`, parentheses, and the functions `min`, `max`, `abs`, `sqrt`, `hypot`. A tiny parser reads it. Nothing is evaluated as Python. A circular reference, an unknown key, a failed function (such as `sqrt` of a negative number), division by zero and a result too large to hold are errors that `validate` reports.

Inside an expression, a hyphen belongs to a name only in the middle part of an inline key: `openings.W-1.width - 2` reads as the width minus 2. Write a space on each side of a minus sign that means subtraction.

`{key:explain}` prints the arithmetic. Constants in it print as whole numbers or fractions. Write a constant that is not an exact fraction as a division, for example `room_w * room_d / 144`.

## Dimension chains

A chain lists segments that must add up to a total:

```json
{"id": "N-wall", "total": "$room_w", "tol": 0.0625,
 "segments": [{"len": "$pier_w", "what": "wall"}, {"len": "$win_w", "what": "opening"}]}
```

Each segment's `what` is `wall`, `opening` or `other` (a setback, a separation, a room). An `opening` segment may name the opening's `id` in `opening`. Both are for the reader: QA checks only that the lengths add up. `tol` defaults to one unit of the drawing precision (1/16 in.). A chain that does not close is an error. Put any closure error in a wall segment, never in an opening, and record why in `note`.

## Recording a measurement

Write down five things for every taped number:

1. What it runs between. Name the surfaces: "finished face of W wall" is clear; "the wall" is not. Say if the tape touched trim instead of the wall.
2. Whether the tape followed the floor, a slope, or a level line (`along`).
3. The height it was held at, for horizontal tapes (`ref_level`).
4. The source: the sketch, photo or answer it came from.
5. For a sketch or photo source, which compass direction is up in the image (`orientation_note`).

Ask about a digit only when a chain fails to close. When a field value replaces an assumption, change the status to MEASURED, remove the `fv` tag, and rebuild. Every note and dimension that printed the old value follows, because they read the model.
