# 3D review (optional)

Read this when the owner wants a 3D model, or when a design question depends on a view the sheets cannot show (built-ins, stairs, level changes, clearances).

The 3D model is a review aid. It is not a gate and not a source. CrossBeam does not supply a 3D engine for an on-screen model. You build that model yourself in the owner's session.

For 3D views printed on the sheets (an exterior view, an interior perspective with code callouts), use the kit's `render3d` views and the `model3d` block instead; see `3d-views.md`. They follow the same rules as this page: built from `project.json`, labels computed from values, unverified parts drawn in a distinct style with their FV tags. A screenshot of a kit view is also a good thing to show the owner in the review loop below (section 5).

## 1. Why build one

In one project, an owner looked at a simple 3D model of a built-in bench and found eight errors that the 2D sheets did not show:

- chairs placed on the bench, because a plan angle had the wrong sign;
- a ramp drawn backwards;
- a pinched wedge at a corner;
- a seat with no back where the table still reached it;
- a cushion that stopped at a vertical cut;
- chairs placed on fixed angles that crowded one side;
- a stair flight rotated 90 degrees;
- a walkway to the stair that was too narrow with the larger table.

The owner also made three design changes while looking at the model. Every catch came from the owner looking at a screenshot, not from a number check.

## 2. Build it from project.json

- Generate the model data from `project.json` with a script. Write it to `build/model.json`. If the project already has a `model3d` block for its sheets, generate `model.json` from that block, so the sheets and the on-screen model share one source.
- The viewer reads `model.json`. The viewer never declares a dimension of its own.
- Compute every label in the model from the value it measures. Never type a label.
- Carry each element's status into the model. Show ASSUMED and PLACEHOLDER parts in a distinct style.
- Keep placeholder furniture in a separate file. It never enters the drawings or a cut list.

Example: an early model declared five dimensions again by hand. The paper set and the model then drifted apart. The paper set still printed five places on the bench after the model showed that three places on the curve were too tight.

## 3. Recipe: a single-file viewer

Write one HTML file, for example `build/model-viewer.html`.

1. Load three.js from a public CDN. Load OrbitControls with it.
2. Load `model.json`. If the host blocks local file reads, embed the JSON in the HTML at build time.
3. State the axis mapping once, at the top of the script. Example: if `project.json` uses x east, y north, z up, map each point to three.js as `(x, z, -y)`.
4. Build walls as boxes along their face lines, with openings cut where the openings are. Use one opening list for both faces of each wall.
5. Build stairs as real treads: riser count times riser height must equal the level change. A label is not a stair.
6. Add buttons for views that match the sheets: plan, and each elevation by name. Then the owner can compare a view with a sheet without turning the model.
7. Add layer switches: existing, new, demo, furniture, dimensions.
8. Add dimension labels that face the viewer. Hide them by default if the owner asks.
9. Add a few eye-height viewpoints: standing, and seated where seating matters.
10. Give every mesh a name. Then you can check the model with scene queries, not only by eye.

By default, give the owner the local path of the viewer file. Owners forget where a model lives, so record the path in `logs/decisions.md`.

If the host can publish a web page, you may offer to publish the viewer. Publishing puts the model outside the project folder, so ask first:

1. Say what the page shows: the layout of the rooms, their dimensions, and any label in the model.
2. Say who can see it, as the host states it: only the owner, or anyone with the link.
3. Leave the address, the property owner's name and the parcel number out of the model before you publish.
4. Publish only after a clear yes. Record the link and who can see it in `logs/decisions.md`.

## 4. Check it before you show it

1. Render a screenshot yourself before you send the link. Look for a camera inside the geometry, oversized labels and missing parts.
2. Test handedness on one asymmetric feature. Compare it with the plan. A mirrored model is a serious error for a builder.
3. Confirm each opening reads as an opening from both sides of its wall.
4. Confirm the stair connects the two floors.
5. Your own look is a claim. The owner's look is the check.

## 5. The review loop

1. Ask the owner to look around and send screenshots with one short line each, the same way as `04-read-back.md`.
2. Put each finding into `project.json` first. Never fix only the model.
3. Rebuild the sheets and the model together.
4. Record each finding in `logs/decisions.md` with the sheets it changed.

## 6. What it cannot prove

Tell the owner these limits once, when you first share the model:

- It does not prove code compliance, accessibility, structural capacity or fabrication fit.
- Seated and standing views are approximate. They do not prove comfort or fit for a person.
- Positions marked as indicative were never taped. Example: "The three risers carry measured heights, but their position along the rail is indicative."
- Moving parts show nominal travel. Hardware limits are not verified.

Code questions that the model raises go to stage 5.

## Exit condition

- Every model finding is in `project.json` and `logs/decisions.md`.
- The sheets and the model come from the same build.
