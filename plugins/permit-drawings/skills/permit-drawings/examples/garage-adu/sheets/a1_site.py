"""A-1 - SITE PLAN. Site coordinates: real inches from the SW lot corner, x east, y north."""
from permitkit import annot, site

def build(kit):
    p = kit.project
    sh = kit.sheet("A-1")
    LW, LD = p.v("lot_w"), p.v("lot_d")
    v = sh.view("SITE PLAN", '1" = 10\'-0"', extents=(-300, -260, LW + 300, LD + 140), cell=(0, 0, 14.0, 22.4))
    site.property_line(v, [(0, 0), (LW, 0), (LW, LD), (0, LD)], lengths=[p["lot_w"], p["lot_d"], p["lot_w"], p["lot_d"]])
    hx, hy, hw, hd = p.v("house_x"), p.v("house_y"), p.v("house_w"), p.v("house_d")
    site.footprint(v, [(hx, hy), (hx + hw, hy), (hx + hw, hy + hd), (hx, hy + hd)], "existing",
                   "(E) RESIDENCE", ["1 STORY", "NOT IN SCOPE"])
    ax, ay, aw, ad = p.v("adu_x"), p.v("adu_y"), p.v("ext_w"), p.v("ext_d")
    site.footprint(v, [(ax, ay), (ax + aw, ay), (ax + aw, ay + ad), (ax, ay + ad)], "new",
                   "(E) GARAGE TO ADU", [kit.text("{floor_area:sf}")])
    site.paving(v, [(hx + hw + 24, 0), (ax + aw - 12, 0), (ax + aw - 12, ay), (hx + hw + 24, ay)], "(E) DRIVEWAY")
    site.centerline(v, (-280, -200), (LW + 280, -200))
    site.street_label(v, (LW / 2, -170), "EXAMPLE AVENUE")
    site.utility(v, (hx + hw - 40, hy - 10), "(E) ELEC. METER", side="S")
    site.utility(v, (ax - 10, ay + 40), "(N) SUBPANEL", side="W")
    annot.north_arrow(v, (LW + 140, LD - 40), r=16)
    # setbacks and separation
    annot.dim_chain(v, [p["adu_x"], p["ext_w"], p["set_side"]], start=0, at=LD + 60, axis="x", ext_from=LD)
    annot.dim_chain(v, [p["adu_y"], p["ext_d"], p["set_rear"]], start=0, at=LW + 70, axis="y", ext_from=LW, side=-1)
    annot.dim_chain(v, [p["house_y"], p["house_d"], {"value": p["sep"], "suffix": "SEPARATION"}], start=0,
                    at=-90, axis="y", ext_from=0)
    annot.dim_chain(v, [p["house_x"], p["house_w"]], start=0, at=hy - 60, axis="x", ext_from=hy)
    pan = sh.panel((14.4, 12.0, 12.0, 10.4), "PROJECT DATA")
    pan.table([("ITEM", 2.4), ("VALUE", None, "wrap")], [
        ["ADDRESS", p.meta["address"]],
        ["LOT SIZE", kit.text("{lot_w:ftin} x {lot_d:ftin}")],
        ["ADU FLOOR AREA", kit.text("{floor_area:sf} (CONVERSION OF (E) GARAGE)")],
        ["SETBACKS (EXISTING)", kit.text("SIDE {set_side:ftin}, REAR {set_rear:ftin}")],
        ["BUILDING SEPARATION", kit.text("{sep:ftin}")],
    ])
    leg = sh.panel((14.4, 6.0, 12.0, 5.6), "LEGEND")
    leg.legend([("poche_e", "(E) STRUCTURE"), ("hatch", "AREA OF WORK"), ("assumed", "SETBACK / NOT TAPED")])
    sh.notes(["PROPERTY LINES FROM THE ASSESSOR MAP; NO SURVEY.", "NO CHANGE TO SITE GRADING OR DRAINAGE."])
    return sh
