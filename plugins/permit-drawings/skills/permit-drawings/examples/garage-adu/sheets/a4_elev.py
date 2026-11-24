"""A-4 - EXTERIOR ELEVATIONS. x along the wall as seen, y up from slab."""
from permitkit import annot, arch, pens, section

ELEV = '3/8" = 1\'-0"'

def build(kit):
    p = kit.project
    sh = kit.sheet("A-4")
    EW, ED, H = p.v("ext_w"), p.v("ext_d"), p.v("plate")
    pitch = p["roof_pitch"]
    # SOUTH: gable end faces you
    v = sh.view("SOUTH ELEVATION", ELEV, extents=(-50, -40, EW + 80, 200), cell=(0, 11.4, 13.0, 11.0))
    section.siding(v, 0, 0, EW, H, "stucco")
    v.rect(0, 0, EW, H, **pens.kw("profile"))
    section.roof_profile(v, 0, EW, H, pitch, overhang=p.v("overhang"))
    te = p.v("t_ext")
    arch.elev_door(v, te + p.v("ed_off"), p.v("ed_w"), p.v("ed_h"))
    arch.elev_window(v, te + p.v("lw_off"), p.v("lw_sill"), p.v("lw_w"), p.v("lw_h"))
    section.grade(v, -40, EW + 40)
    section.pitch_symbol(v, (EW * 0.78, H + EW * 0.2), pitch, side=-1)
    section.level_marker(v, EW, H, "T.O. PLATE", p["plate"])
    section.level_marker(v, EW, 0, "F.F. / SLAB")
    annot.opening_tag(v, (te + p.v("ed_off") + p.v("ed_w") / 2, p.v("ed_h") / 2), "D-1")
    annot.opening_tag(v, (te + p.v("lw_off") + p.v("lw_w") / 2, p.v("lw_sill") - 12), "W-1")
    annot.dim_chain(v, [p["ext_w"]], start=0, at=-30, axis="x", ext_from=0, side=-1)
    # EAST: eave side
    v2 = sh.view("EAST ELEVATION", ELEV, extents=(-50, -40, ED + 80, 200), cell=(13.4, 11.4, 13.0, 11.0))
    section.siding(v2, 0, 0, ED, H, "stucco")
    v2.rect(0, 0, ED, H, **pens.kw("profile"))
    section.roof_eave(v2, 0, ED, H, pitch, EW, overhang=p.v("overhang"))
    y = te + p.v("ped") + p.v("egw_off")
    arch.elev_window(v2, y, p.v("egw_sill"), p.v("egw_w"), p.v("egw_h"))
    section.grade(v2, -40, ED + 40)
    section.level_marker(v2, ED, H, "T.O. PLATE", p["plate"])
    annot.opening_tag(v2, (y + p.v("egw_w") / 2, p.v("egw_sill") - 12), "W-2")
    annot.dim_chain(v2, [p["ext_d"]], start=0, at=-30, axis="x", ext_from=0, side=-1)
    annot.dim_chain(v2, [p["egw_sill"], p["egw_h"]], start=0, at=y - 14, axis="y", ext_from=y)
    v3 = sh.view("NORTH ELEVATION", ELEV, extents=(-50, -40, EW + 80, 200), cell=(0, 0, 13.0, 11.0))
    section.siding(v3, 0, 0, EW, H, "stucco")
    v3.rect(0, 0, EW, H, **pens.kw("profile"))
    section.roof_profile(v3, 0, EW, H, pitch, overhang=p.v("overhang"))
    xw = EW - te - p.v("btw_off") - p.v("btw_w")
    arch.elev_window(v3, xw, p.v("btw_sill"), p.v("btw_w"), p.v("btw_h"), kind="casement")
    section.grade(v3, -40, EW + 40)
    annot.opening_tag(v3, (xw + p.v("btw_w") / 2, p.v("btw_sill") - 12), "W-3")
    v4 = sh.view("WEST ELEVATION", ELEV, extents=(-50, -40, ED + 80, 200), cell=(13.4, 0, 13.0, 11.0))
    section.siding(v4, 0, 0, ED, H, "stucco")
    v4.rect(0, 0, ED, H, **pens.kw("profile"))
    section.roof_eave(v4, 0, ED, H, pitch, EW, overhang=p.v("overhang"))
    xd = ED - te - p.v("sd_off") - p.v("sd_w")
    arch.elev_door(v4, xd, p.v("sd_w"), p.v("ed_h"))
    section.grade(v4, -40, ED + 40)
    annot.opening_tag(v4, (xd + p.v("sd_w") / 2, p.v("ed_h") / 2), "D-2")
    sh.notes(["(E) STUCCO TO REMAIN; PATCH TO MATCH AT INFILL.", "(E) ROOF TO REMAIN."])
    return sh
