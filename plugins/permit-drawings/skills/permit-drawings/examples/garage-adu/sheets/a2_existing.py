"""A-2 - EXISTING / DEMOLITION PLAN."""
import common
from permitkit import annot

def build(kit):
    p = kit.project
    sh = kit.sheet("A-2")
    W, D, te = p.v("int_w"), p.v("int_d"), p.v("t_ext")
    v = sh.view("EXISTING / DEMOLITION PLAN", common.PLAN, extents=common.plan_extents(p), cell=(0, 3.4, 17.0, 19.0))
    s = common.shell(v, p)
    s.S.overhead(p.v("gd_off"), p["gd_w"], action="demo")
    s.W.door(p.v("sd_off"), p["sd_w"], swing="E", hinge="start")
    annot.room_tag(v, (W / 2, D / 2 + 30), "(E) GARAGE", [kit.text("{int_w:ftin} x {int_d:ftin}")])
    annot.keynote(v, (W / 2 + 40, 40), 1, leader_to=(W / 2, -2))
    annot.keynote(v, (40, 60), 2, leader_to=(0, p.v("sd_off") + p.v("sd_w") / 2))
    annot.opening_tag(v, (p.v("gd_off") + p.v("gd_w") / 2, -te - 14), "GD-1")
    annot.opening_tag(v, (-te - 16, p.v("sd_off") + p.v("sd_w") / 2), "D-2")
    annot.north_arrow(v, (W + te + 40, D + te + 40))
    annot.dim_chain(v, [p["gd_off"], p["gd_w"], p["gd_e"]], start=0, at=-te - 34, axis="x", ext_from=-te, side=-1)
    annot.dim_chain(v, [p["ext_w"]], start=-te, at=-te - 52, axis="x", ext_from=-te, side=-1)
    annot.dim_chain(v, [p["sd_off"], p["sd_w"], p["sd_n"]], start=0, at=-te - 34, axis="y", ext_from=-te)
    annot.dim_chain(v, [p["ext_d"]], start=-te, at=-te - 52, axis="y", ext_from=-te)
    k = sh.panel((17.4, 12.0, 9.0, 10.4), "DEMOLITION KEYNOTES")
    k.numbered([kit.text("REMOVE (E) {gd_w:ftin} WIDE OVERHEAD DOOR, TRACK AND OPENER. KEEP THE (E) HEADER."),
                "(E) SIDE DOOR TO REMAIN."])
    leg = sh.panel((0, 0, 7.6, 3.2), "LEGEND")
    leg.legend([("poche_e", "(E) WALL TO REMAIN"), ("demo", "ITEM TO BE REMOVED")])
    return sh
