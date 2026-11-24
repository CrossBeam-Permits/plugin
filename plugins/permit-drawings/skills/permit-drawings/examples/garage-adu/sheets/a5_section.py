"""A-5 - BUILDING SECTION A, cut E-W through the living room, looking north."""
from permitkit import annot, pens, section

def build(kit):
    p = kit.project
    sh = kit.sheet("A-5")
    EW, H, te = p.v("ext_w"), p.v("plate"), p.v("t_ext")
    pitch = p["roof_pitch"]
    v = sh.view("BUILDING SECTION A", "fit", extents=(-70, -50, EW + 110, 200), cell=(0, 0, 26.4, 22.4))
    # slab and footings
    section.concrete(v, [(-6, -4), (EW + 6, -4), (EW + 6, 0), (-6, 0)])
    for x0 in (-6, EW - 12):
        section.concrete(v, [(x0, -24), (x0 + 18, -24), (x0 + 18, -4), (x0, -4)])
    section.earth(v, [(-40, -34), (EW + 40, -34), (EW + 40, -24), (-40, -24)])
    section.grade(v, -40, EW + 40, y=-2, label="FINISH GRADE")
    # walls cut
    for x0 in (0, EW - te):
        v.rect(x0, 0, x0 + te, H, **pens.kw("cut", fill="#ffffff"))
        section.insulation(v, x0 + 1, 3, x0 + te - 1.5, H - 6)
        section.wood_cut(v, x0, H - 3, x0 + te, H)
    # ceiling joists and insulation
    v.line(te, H, EW - te, H, **pens.kw("cut_med"))
    section.insulation(v, te, H, EW - te, H + 10)
    section.roof_profile(v, 0, EW, H, pitch, overhang=p.v("overhang"))
    section.pitch_symbol(v, (EW * 0.25, H + 46), pitch)
    section.level_marker(v, EW + 12, H, "T.O. PLATE", p["plate"])
    section.level_marker(v, EW + 12, 0, "F.F. / T.O. SLAB")
    annot.dim_chain(v, [p["plate"]], start=0, at=-30, axis="y", ext_from=0)
    annot.dim_chain(v, [p["ext_w"]], start=0, at=-44, axis="x", ext_from=-24, side=-1)
    annot.leader(v, (EW / 2, H + 5), "(N) R-38 BATT INSULATION AT CEILING", dx=40, dy=-40)
    annot.leader(v, (te / 2, H / 2), ["(E) 2x4 STUDS @ 16\" O.C.", "(N) R-13 BATT INSULATION"], dx=50, dy=30)
    annot.leader(v, (EW / 2, -2), "(E) CONCRETE SLAB ON GRADE", dx=50, dy=-30)
    sh.notes(["INSULATION VALUES ARE PLACEHOLDERS PENDING THE ENERGY COMPLIANCE REPORT."])
    # every hatched material is named in a legend (QA "hatching")
    sh.side_panel("LEGEND").legend([("hatch:concrete", "CONCRETE"), ("hatch:earth", "EARTH"),
                                    ("hatch:batt", "BATT INSULATION"), ("hatch:wood", "WOOD, CUT")])
    return sh
