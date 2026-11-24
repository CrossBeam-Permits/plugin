# 3D views on the sheets

This needs the kit's optional `3d` module. Run `python3 -m permitkit modules`; if it is not installed, fetch it as `00-connect.md` section 3 says (`crossbeam_get_skill` with `"module": "3d"`).

Read this when a sheet needs a 3D view: an exterior rendering for the title sheet, an interior perspective for a kitchen or bath, a cutaway or an axonometric with code callouts.

The kit draws 3D views itself (`scripts/permitkit/render3d.py`). A 3D view prints as vector polygons inside a view cell, like any other view, so it is sharp in the PDF and the SVG. It reads the same `project.json` values as the plans. It is not a separate model that can drift. For an orbit-around model the owner reviews on screen, see `3d-review.md`.

## 1. What reviewers and owners expect

- **Title sheet**: one exterior view of the whole building with the new work, usually from the side where the work is. An axonometric or a two-point perspective from eye height both work. It tells a plan checker where the work is before they open the plans.
- **Kitchen and bath remodels**: one interior perspective from the door, with callouts for the code items a reviewer checks there: receptacle spacing and height, GFCI, hood clearance, island receptacles, clearances at fixtures. Each callout reads from a rule or a value.
- **Additions**: the exterior view, plus a view that shows how the new roof meets the existing roof.
- A 3D view never replaces a plan, elevation or section. Say so in the view notes: "WHERE A VIEW AND A PLAN DIFFER, THE PLAN GOVERNS."

## 2. The model3d block

Add a `model3d` block to `project.json`. Each element names its geometry with `$key` refs or inline Values, exactly like the rest of the file. A bare number is refused, so the 3D view and the plans cannot disagree.

```json
"model3d": {
  "sun": {"azimuth": 215, "altitude": 50},
  "materials": {"stucco": {"rgb": "#e8dcc4", "label": "(E) AND (N) STUCCO, (N) TO MATCH (E)"}},
  "elements": [
    {"id": "N-REAR", "kind": "wall", "material": "stucco", "body": "N",
     "x0": "$x_w", "y0": "$y_s", "x1": "$x_e", "y1": "$y_s", "t": "$t_ext_n_in",
     "z": "$grade_z_in", "h": "$n_wall_h_in",
     "openings": [{"ref": "W-1", "style": "XO", "offset": "$w1_off_in", "sill": "$w1_sill_z"}]},
    {"id": "N-ROOF", "kind": "roof", "form": "gable", "ridge": "y", "x0": "$x_w", "y0": "$y_s",
     "x1": "$x_e", "y1": "$ridge_meet_in", "z": "$plate_h_in", "pitch": "$roof_rise_n_in",
     "overhang": "$eave_oh_in", "rake": "$rake_oh_in", "thick": "$rafter_d_in"}
  ],
  "cameras": [
    {"id": "yard", "type": "perspective", "eye": [-320, -390, "$eye_h"], "target": [-110, -50, "$eye_h"], "lens": 32},
    {"id": "sw", "type": "axon", "projection": "iso", "azimuth": 222, "fit": ["N-REAR", "N-ROOF"]}
  ]
}
```

Element kinds (all positions in the project axes, inches):

| kind | fields | notes |
|---|---|---|
| `wall` | `x0 y0 x1 y1` (the face line), `t`, `z`, `h`, `body` (N/S/E/W, left, right), `openings`, `inner` (material of the other face) | Openings are cut through with jambs, sill and head. `openings[].ref` names an `openings` item; `offset` runs from `x0,y0` along the face; `sill` is above the wall's `z`. `kind`: window, door, glass_door, opening; `style`: fixed, XO, pair. |
| `slab` | `x0 y0 x1 y1`, `z` (top), `t` | Floors, ceilings, patios, grade. |
| `box` | `x y z w d h`, `style`, `front` | Casework, appliances, fixtures, furniture. `style`: plain, base, upper, tall, range, fridge, hood, basin, panel draws schematic doors, drawers, burners or a bowl on the `front` face. |
| `roof` | `x0 y0 x1 y1` (wall outside faces), `z` (underside at the walls), `pitch` (rise per 12), `overhang`, `rake`, `thick`, `form` (gable, hip, shed, flat), `ridge` (x or y), `low` (shed) | Gable ends close with wall-material triangles; fascia and barge in `fascia_material`. |
| `member` | `x0 y0 z0 x1 y1 z1`, `w`, `d`, `count`, `step_x step_y step_z` | Posts, beams and rafters (a patio cover is a set of members). |
| `device` | `x y z`, `face` (N/S/E/W, U for a worktop) | Receptacles, switches. |

An element takes the worst status of the values it was built from. An ASSUMED or PLACEHOLDER element draws lighter with grey dashed edges, and each view prints its FV tag once, on the largest visible part. When a part's form is not measured at all (for example an existing roof nobody has looked at), add `"assumed": {"fv": "FV-4"}` to the element.

Geometry values the plans do not print (a cabinet depth, a camera eye height, a drawn slab thickness) are still Values: add them with a note such as "3D model only; prints nowhere". A drawing size used only to make a part look right (a window frame, a handle) is a kit constant and never prints.

A sheet script can also build elements from geometry it already drew: `scene.wall_from_plan(id, arch_wall, z, h, openings=...)` makes a 3D wall from an `arch.Wall`.

## 3. A 3D sheet

```python
from permitkit import render3d as r3

def build(kit):
    p = kit.project
    sh = kit.sheet("A-0.2")
    sc = r3.Scene.from_project(p)
    v = r3.View3D(sh, sc, "kitchen", "KITCHEN — INTERIOR PERSPECTIVE", cell=(0, 9, 26, 13),
                  margins=(0.24, 0.02, 0.24, 0.02), subtitle="LOOKING EAST FROM THE HALL DOOR")
    v.dim((hx, hy, p.v("counter_h")), (hx, hy, p.v("hood_bot")), p["hood_h"], rule="R-10")
    v.callouts([
        (sc["HOOD"].at(0.3, 0.0, 0.06), [
            kit.text("(N) DUCTED CANOPY HOOD, BOTTOM {hood_h} ABOVE THE COOKING SURFACE."),
            v.rule_text("R-10", "COOKTOP TO COMBUSTIBLES {rule.limit} {rule.op} ({rule.citation}).")], "left"),
        (sc["RCP-N2"].at(0.5, 0.5, 0.5), [
            v.rule_text("R-4", "NO POINT ALONG A COUNTER MORE THAN {rule.limit} FROM A RECEPTACLE.")], "left"),
    ])
    m = sh.panel((12, 0, 6.6, 9), "COLORS AND MATERIALS")
    r3.material_legend(m, sc, v.materials_used())
    r3.status_legend(m)
    return sh
```

- `View3D(sheet, scene, camera_id, title, cell, margins, subtitle)`: the picture is fitted N.T.S. into the cell. `margins` (left, bottom, right, top, as a share of the picture) leave room for callout text.
- `v.callouts([(point, lines, side), ...])`: leaders from 3D points to notes stacked beside the picture. Lay out all of a view's callouts in one call so they never cross. Each line is a `kit.text`, `v.rule_text` or plain words; a plain string with a digit is refused.
- `v.rule_text(rule_id, template)`: `{rule.limit}`, `{rule.op}` (MIN., MAX., EXACTLY), `{rule.citation}`, `{rule.element}`, `{rule.value}` and any `{value_key}` come from `project.json`.
- `v.dim(a, b, value, rule=None, offset=...)`: a dimension between two 3D points. The distance must equal the value, or the build stops. With a rule it prints `2'-6" (MIN. 2'-0")`, the limit in the same house style as `tables.limit_text` and refuses a verified value that breaks the rule.
- `el.at(fx, fy, fz)` is a point by bounding-box fractions; `el.top(fx, fy)` is the top surface over a plan point (a roof slope, a counter top). A leader whose point the camera cannot see, or that falls outside a framed picture, is a QA layout fail.

## 4. Cameras

- `axon`: `projection` iso, dimetric, plan_oblique (`rotate`, `vscale`) or custom (`azimuth`, `elevation`). `azimuth` is the compass bearing from the building to the viewer: 225 looks from the south-west. Check one asymmetric feature against the plan before you show it.
- `perspective`: `eye`, `target`, `lens` (35 mm terms: 18-24 wide for interiors, 28-35 for exteriors), `near`, `shift`. Keep `target` at eye height for an exterior: verticals stay plumb (two-point perspective). `shift` moves the picture up or down without tilting the camera.
- `hide`: element ids the camera leaves out. For an interior perspective, stand outside the room and hide the wall behind you (and its doors). A wall that is too close shows as a slab; hide it rather than moving into it.
- `cut_z`: a horizontal section; cut walls get a dark cap. Use it for a cutaway that shows a room's layout and its devices.
- `fit` (axon): frame the picture on a few elements and clip the rest at the frame, for a close view of the new work.
- `light`: `sun` (default for axons) or `interior` (default for perspectives, so ceilings read light).

Camera tips:

1. Exterior on the title sheet: an iso from the side of the new work, or a perspective from the yard at standing eye height.
2. Kitchen: stand in the doorway, look along the longest counter, lens 20-24. The range wall and the sink wall should both show.
3. Bath: from the door, lens 18-20, hide the door wall.
4. Build, look at the preview, move the camera, repeat. Look for slabs too close to the eye, callout leaders crossing parts, and tags on top of each other.

## 5. Checks the kit makes

- Every number printed in a 3D view is a Value with its FV tag, or comes from a rule.
- `model3d` is validated with the project: duplicate ids, unknown materials, missing fields, bad opening refs and unknown `fit` ids are errors; an unknown `hide` id is a warning.
- Builds are byte-for-byte deterministic.
- A callout point the camera cannot see is a layout fail; fix the point or the camera. A callout point outside the picture (or behind the camera) stops the build with `LayoutError`; it is never dropped.

## 6. Limits

- Faces are flat and convex; curved parts are approximated by the elements you give.
- Cabinet doors, handles, appliance fronts and window frames are schematic.
- No textures, cast shadows or reflections. Colors show the intended finishes; samples come from the owner.
- A section cap is drawn only for walls, boxes and slabs (solid prisms).
- Existing parts nobody surveyed are not shown, or are shown with an FV tag. Say which in the view notes.
