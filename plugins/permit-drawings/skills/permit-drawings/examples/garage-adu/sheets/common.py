"""Plan geometry shared by the existing and proposed plans."""
from permitkit import arch

PLAN = '1/2" = 1\'-0"'


def shell(v, p, action="existing"):
    t = {k: p["t_ext"] for k in "NSEW"}
    return arch.Shell(v, 0, 0, p.v("int_w"), p.v("int_d"), t, action=action)


def plan_extents(p, pad_x=60, pad_y=66):
    te = p.v("t_ext")
    return (-te - pad_x, -te - pad_y, p.v("int_w") + te + pad_x, p.v("int_d") + te + pad_y)
