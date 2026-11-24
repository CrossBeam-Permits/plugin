"""Elevation and section symbols: roof profiles, roof pitch and siding, plus
short aliases for grade, level datums and section materials (drawn by hatch
and symbols).

Elevation and section axes: x along the view as seen, y up, real inches.
y = 0 is usually finished floor; say what it is in the view title or a note.

Every printed number comes from a model Value. A roof pitch is a Value with
`unit: "in/ft"`: inches of rise per foot of run, so a 4:12 roof is 4. That is
the slope unit the QA `rules` check compares, so a roof-slope rule from
crossbeam_rules checks the same value the elevations draw.
"""
from __future__ import annotations

from . import hatch, symbols
from .annot import dim_label
from .display import DIM, INK, LIGHT, WHITE, View, poly_segments
from .model import Value

# ---- aliases. The section materials and the level datum are drawn by hatch
# and symbols, the kit's one pattern set and one symbol library; these names
# keep older sheet scripts working with the defaults they were written for.


def grade(v: View, x0, x1, y=0.0, depth_pt: float = 7.0, label: str | None = "GRADE"):
    """Finished grade: alias of hatch.grade with a thin earth band and a GRADE label."""
    return hatch.grade(v, x0, x1, y, depth_pt=depth_pt, label=label)


def earth(v: View, pts):
    """Earth under a footing or slab: alias of hatch.fill(v, pts, "earth")."""
    hatch.fill(v, pts, "earth")


def concrete(v: View, pts, outline: bool = True):
    """Concrete cut in section: alias of hatch.fill(v, pts, "concrete") with a
    white ground and a cut outline (outline=False: the stipple only)."""
    hatch.fill(v, pts, "concrete", outline="cut_med" if outline else None, tint=WHITE if outline else None)


def wood_cut(v: View, x0, y0, x1, y1):
    """A framing member cut in section (a plate, a header, a joist end): alias
    of hatch.rect(..., "wood"), a box with an X."""
    hatch.rect(v, x0, y0, x1, y1, "wood", outline="cut_med", tint=WHITE)


def insulation(v: View, x0, y0, x1, y1):
    """Batt insulation in a box: alias of hatch.rect(..., "batt"). The loops run
    along the long side and stay between the box's two faces."""
    hatch.rect(v, x0, y0, x1, y1, "batt")


def level_marker(v: View, x, y, label: str, value=None, side: str = "right", reach_pt: float = 40.0):
    """A level datum set off the building's face: alias of symbols.level_marker
    with a dashed leader `reach_pt` long and the height in feet-inches.
    Example: level_marker(v, W + 12, p.v("plate"), "T.O. PLATE", p["plate"]).
    """
    return symbols.level_marker(v, x, y, label, value, side, size=6.5, line=False, reach_pt=reach_pt,
                                style="ftin")


PITCH_UNIT = "in/ft"


def _rise(pitch) -> float:
    """Inches of rise per foot of run, from a pitch Value in in/ft."""
    if not isinstance(pitch, Value):
        raise TypeError('roof pitch must be a model Value with unit "in/ft" (rise per 12), so its status prints')
    if pitch.unit != PITCH_UNIT:
        raise ValueError(f'roof pitch {pitch.key} has unit {pitch.unit!r}; give it unit "in/ft" (inches of rise '
                         "per foot of run, 4 for a 4:12 roof), the slope unit the rules check uses")
    return float(pitch)


def pitch_symbol(v: View, at, pitch, side: int = 1, run_pt: float = 18.0):
    """The roof-slope triangle: '<rise>' over a 12 run, from a model Value.
    side +1 slopes up to the right, -1 up to the left."""
    rise = _rise(pitch)
    lab, keys, tags = dim_label(v, pitch, "n")
    px, py = v.P(*at)
    h = run_pt * rise / 12.0
    x2 = px + side * run_pt
    v.paper_path(poly_segments([(px, py), (x2, py), (x2, py + h)]), stroke=INK, width=0.6, layer="annot")
    v.paper_path([("M", px - side * 4, py - h * 4 / run_pt), ("L", x2 + side * 4, py + h + h * 4 / run_pt)],
                 stroke=INK, width=0.6, layer="annot")
    recs = [v.paper_text(px + side * run_pt / 2, py - 7.5, "12", size=6.5, anchor="middle", role="pitch")]
    recs.append(v.paper_text(x2 + side * 3, py + h / 2 - 2.5, lab, size=6.5, anchor="start" if side > 0 else "end",
                             role="pitch", keys=keys, fv=tags, color=DIM if tags else INK))
    return recs


def roof_profile(v: View, x0, x1, plate, pitch, overhang=12.0, fascia=6.0, kind: str = "gable",
                 thickness=None, status: str | None = None):
    """The roof as seen in an elevation or cut in a section.

    x0, x1     outside faces of the walls that carry the roof, real inches.
    plate      top of wall plate height (a number or Value).
    pitch      rise per 12, a Value with unit "in/ft".
    kind       'gable'  the gable end faces you: two slopes meet at a ridge.
               'shed'   one slope, rising from x0 to x1.
               For the eave side of a gable roof use roof_eave().
    thickness  roof assembly depth measured plumb (default: fascia).
    Returns {'ridge': y, 'eave': y}, bare numbers in real inches, for placing
    a dimension or a level marker. 'ridge' is the top of the roof at its high
    point. A gable's high point is the peak between the walls:
    plate + (x1 - x0) / 2 / 12 x pitch + thickness. A shed's is the high
    fascia, past x1 by the overhang: plate + (x1 - x0 + overhang) / 12 x pitch
    + thickness. 'eave' is the underside at the low fascia.

    A bare number never prints. To print a ridge height, give it a DERIVED
    value in project.json, converting the slope in a value of its own so no
    expr adds inches to in/ft (validate warns on that):
        "roof_rise": {"expr": "ext_w / 2 / 12 * roof_pitch", "status": "DERIVED"},
        "ridge_h":   {"expr": "plate + roof_rise + roof_t", "status": "DERIVED"}
    (roof_rise has the default unit, in; roof_t is the thickness you pass).
    Then level_marker(v, x, p.v("ridge_h"), "T.O. RIDGE", p["ridge_h"]); QA
    checks the printed text against the value.
    """
    rise = _rise(pitch) / 12.0
    plate, oh, fa = float(plate), float(overhang), float(fascia)
    th = float(thickness) if thickness is not None else fa
    kw = {"stroke": INK, "width": 1.2}
    if status:
        kw["status"] = status
    eave_y = plate - oh * rise          # underside of rafter tail at the fascia line, approx.
    if kind == "gable":
        mid = (x0 + x1) / 2
        ridge = plate + (mid - x0) * rise
        top = [(x0 - oh, eave_y + th), (mid, ridge + th), (x1 + oh, eave_y + th)]
        bot = [(x0 - oh, eave_y), (mid, ridge), (x1 + oh, eave_y)]
        v.polyline(top, **kw)
        v.polyline(bot, **dict(kw, width=0.7))
        v.line(*top[0], *bot[0], **kw)
        v.line(*top[-1], *bot[-1], **kw)
        return {"ridge": ridge + th, "eave": eave_y}
    if kind == "shed":
        hi = plate + (x1 - x0) * rise
        top = [(x0 - oh, eave_y + th), (x1 + oh, hi + oh * rise + th)]
        bot = [(x0 - oh, eave_y), (x1 + oh, hi + oh * rise)]
        v.polyline(top, **kw)
        v.polyline(bot, **dict(kw, width=0.7))
        v.line(*top[0], *bot[0], **kw)
        v.line(*top[1], *bot[1], **kw)
        return {"ridge": hi + oh * rise + th, "eave": eave_y}
    raise ValueError("kind must be 'gable' or 'shed'; for the eave side use roof_eave()")


def roof_eave(v: View, x0, x1, plate, pitch, depth, overhang=12.0, fascia=6.0, rake=None, status=None):
    """The eave side of a gable roof seen in elevation: fascia band at the
    bottom, ridge line at the top, rake overhangs at both ends.

    depth  the building dimension across the ridge (outside wall to outside wall).
    """
    rise = _rise(pitch) / 12.0
    plate, oh, fa = float(plate), float(overhang), float(fascia)
    rk = float(rake) if rake is not None else oh
    kw = {"stroke": INK, "width": 1.2}
    if status:
        kw["status"] = status
    eave_y = plate - oh * rise
    ridge = plate + float(depth) / 2 * rise + fa
    a, b = x0 - rk, x1 + rk
    v.rect(a, eave_y, b, eave_y + fa, **kw)                     # fascia
    v.polygon([(a, eave_y + fa), (b, eave_y + fa), (b, ridge), (a, ridge)], **dict(kw, width=0.9))
    v.line(a, ridge, b, ridge, **dict(kw, width=1.4))
    # roofing courses, light
    n = int((ridge - eave_y - fa) / 10)
    for i in range(1, n):
        y = eave_y + fa + i * (ridge - eave_y - fa) / n
        v.line(a, y, b, y, stroke=LIGHT, width=0.3, layer="back")
    return {"ridge": ridge, "eave": eave_y}


SIDING_KINDS = ("lap", "board", "stucco", "plain")


def siding(v: View, x0, y0, x1, y1, kind: str = "lap", exposure=None):
    """A light surface texture on an elevation wall. Draw it before openings;
    openings fill white over it.

    kind  'lap'     horizontal courses every `exposure` (default 7")
          'board'   board and batten: vertical battens every `exposure` (default 12")
          'stucco'  a light stipple
          'plain'   no texture: the material is unknown, or one the kit does not
                    draw (shingle, panel, masonry). Name it in a keynote or note.
    """
    if kind not in SIDING_KINDS:
        raise ValueError(f"siding kind must be one of {SIDING_KINDS}, not {kind!r}")
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    if kind in ("lap", "board"):
        step = float(exposure if exposure is not None else (7.0 if kind == "lap" else 12.0))
        if step <= 0:
            raise ValueError("siding exposure must be more than 0")
        segs = []
        if kind == "lap":
            y = float(y0) + step
            while y < y1:
                segs += [("M", x0, y), ("L", x1, y)]
                y += step
        else:
            x = float(x0) + step
            while x < x1:
                segs += [("M", x, y0), ("L", x, y1)]
                x += step
        if segs:
            v.path(segs, stroke=LIGHT, width=0.3, layer="back")
    elif kind == "stucco":
        v.hatch(pts, angle=35, spacing_pt=6.0, stroke=LIGHT, width=0.3, dash=(0.5, 5.0), layer="back")
