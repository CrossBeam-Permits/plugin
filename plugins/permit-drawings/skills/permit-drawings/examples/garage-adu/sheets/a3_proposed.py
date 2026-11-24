"""A-3 - PROPOSED FLOOR PLAN. Every dimension comes from project.json.
Fixture and device positions are schematic layout unless dimensioned."""
import common
from permitkit import annot, arch, fixtures

def build(kit):
    p = kit.project
    sh = kit.sheet("A-3")
    W, D, te, ti = p.v("int_w"), p.v("int_d"), p.v("t_ext"), p.v("t_int")
    v = sh.view("PROPOSED FLOOR PLAN", common.PLAN, extents=common.plan_extents(p), cell=(0, 3.4, 17.0, 19.0))

    s = common.shell(v, p)
    # S wall: (E) garage door opening infilled; new entry door and window
    s.S.infill(p.v("gd_off"), p.v("ed_off") - p.v("gd_off"))
    s.S.door(p.v("ed_off"), p["ed_w"], swing="N", hinge="start")
    s.S.infill(p.v("ed_off") + p.v("ed_w"), p.v("lw_off") - p.v("ed_off") - p.v("ed_w"))
    s.S.window(p.v("lw_off"), p["lw_w"])
    s.S.infill(p.v("lw_off") + p.v("lw_w"), p.v("gd_off") + p.v("gd_w") - p.v("lw_off") - p.v("lw_w"))
    s.W.door(p.v("sd_off"), p["sd_w"], swing="E", hinge="start")
    bs, bw = p.v("bed_s"), p.v("bath_w")
    s.E.slider(bs + ti + p.v("egw_off"), p["egw_w"])
    s.N.window(p.v("btw_off"), p["btw_w"])

    # (N) partitions
    p1 = arch.Wall(v, (0, bs), "E", W, p["t_int"], "N", action="new")
    p1.door(p.v("btd_off"), p["btd_w"], swing="N", hinge="start")
    p1.door(bw + ti + p.v("bd_off"), p["bd_w"], swing="N", hinge="end")
    arch.Wall(v, (bw, bs + ti), "N", p.v("bath_d"), p["t_int"], "E", action="new")
    # closet in the bedroom NE corner
    cw, cd = p.v("clo_w"), p.v("clo_d")
    clo = arch.Wall(v, (W - cw, D - cd - ti), "E", cw, p["t_int"], "N", action="new", draw=False)
    clo.draw()
    clo.bypass(4, cw - 8)
    arch.Wall(v, (W - cw - ti, D - cd - ti), "N", cd + ti, p["t_int"], "E", action="new")

    # bath: tub across the N end, toilet and vanity on the W wall
    fixtures.tub(v, 0, D - 30, bw, D, drain="W")
    fixtures.toilet(v, (0, D - 30 - 24), "E")
    fixtures.vanity(v, (0, bs + ti + 24), "E", w=30, d=21)
    # kitchenette on the E wall of the living room
    y0, kl, cdp, rw = p.v("kit_y0"), p.v("kit_len"), p.v("ctr_d"), p.v("ref_w")
    fixtures.counter(v, W - cdp, y0, W, y0 + kl, uppers=(W - 13, y0, W, y0 + kl))
    fixtures.range_(v, (W, y0 + 18), "W", w=30, d=24)
    fixtures.kitchen_sink(v, (W, y0 + 60), "W", w=30, d=22, bowls=1)
    fixtures.refrigerator(v, (W, y0 + kl + rw / 2), "W", w=rw, d=30)

    # room tags
    annot.room_tag(v, (bw / 2 + 10, bs + ti + 30), "BATH", [kit.text("{bath_w:ftin} x {bath_d:ftin}")], size=9)
    annot.room_tag(v, ((bw + ti + W - cw) / 2 + 6, bs + 66), "BEDROOM",
                   [kit.text("{bed_w:ftin} x {bed_d:ftin}"), kit.text("{bed_area:sf}")])
    annot.room_tag(v, (W / 2 - 22, bs / 2 + 8), "LIVING / KITCHEN",
                   [kit.text("{int_w:ftin} x {liv_d:ftin}"), kit.text("{liv_area:sf}")])
    v.text(W - cw / 2, D - cd / 2, "CLOSET", size=6.5, bold=True, anchor="middle", dy=-2)

    # tags at openings, keyed to the schedule
    annot.opening_tag(v, (p.v("ed_off") + p.v("ed_w") / 2, -te - 14), "D-1")
    annot.opening_tag(v, (-te - 16, p.v("sd_off") + p.v("sd_w") / 2), "D-2")
    annot.opening_tag(v, (bw + ti + p.v("bd_off") + p.v("bd_w") / 2, bs - 14), "D-3")
    annot.opening_tag(v, (p.v("btd_off") + p.v("btd_w") / 2, bs - 14), "D-4")
    annot.opening_tag(v, (p.v("lw_off") + p.v("lw_w") / 2, -te - 14), "W-1")
    annot.opening_tag(v, (W + te + 16, bs + ti + p.v("egw_off") + p.v("egw_w") / 2), "W-2")
    annot.opening_tag(v, (p.v("btw_off") + p.v("btw_w") / 2, D + te + 14), "W-3")
    annot.north_arrow(v, (W + te + 40, D + te + 40))

    # dimensions last
    annot.dim_chain(v, [p["gd_off"], p["inf_a"], p["ed_w"], p["inf_b"], p["lw_w"], p["inf_c"], p["gd_e"]],
                    start=0, at=-te - 34, axis="x", ext_from=-te, side=-1)
    annot.dim_chain(v, [p["ext_w"]], start=-te, at=-te - 52, axis="x", ext_from=-te, side=-1)
    annot.dim_chain(v, [p["bath_w"], p["t_int"], p["bed_w"]], start=0, at=D + te + 34, axis="x",
                    ext_from=D + te)
    annot.dim_chain(v, [p["liv_d"], p["t_int"], p["egw_off"], p["egw_w"], p["egw_n"]], start=0,
                    at=W + te + 40, axis="y", ext_from=W + te, side=-1)
    annot.dim_chain(v, [p["ext_d"]], start=-te, at=-te - 44, axis="y", ext_from=-te)

    leg = sh.panel((0, 0, 7.6, 3.2), "LEGEND")
    leg.legend([("poche_e", "(E) WALL TO REMAIN"), ("poche_n", "(N) 2x4 WALL @ 16\" O.C."),
                ("demo", "WALL OR ITEM REMOVED")])
    sched = sh.panel((17.4, 3.4, 9.0, 19.0), "DOOR AND WINDOW SCHEDULE")
    sched.opening_schedule(types=("door", "overhead"))
    sched.space(10)
    sched.opening_schedule(types=("window",))
    sh.notes([
        "ALL DIMENSIONS ARE TO FACE OF STUD OR FINISH AS SHOWN; FIELD-VERIFY BEFORE FRAMING.",
        "FIXTURE AND APPLIANCE OUTLINES ARE SCHEMATIC; SEE MANUFACTURER DATA.",
        kit.text("CONDITIONED FLOOR AREA: {floor_area:sf} (EXTERIOR FACES)."),
    ])
    return sh
