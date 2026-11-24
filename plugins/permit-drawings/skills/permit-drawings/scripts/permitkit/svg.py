"""Optional SVG preview of a Page, with physical units on the root.

The root says width="36in" height="24in" with a viewBox in points. A root
without units is how a past set printed at 75 percent. PDF is the deliverable;
SVG is for previews and web display only.
"""
from __future__ import annotations

import base64

from .display import run_start
from .units import num


def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def _hex(c) -> str:
    if c is None:
        return "none"
    return "#" + "".join(f"{int(round(v * 255)):02x}" for v in c)


def to_svg(page) -> str:
    H = page.height

    def d(segs):
        out = []
        for s in segs:
            if s[0] in ("M", "L"):
                out.append(f"{s[0]}{num(s[1])} {num(H - s[2])}")
            elif s[0] == "C":
                out.append("C" + " ".join(f"{num(s[i])} {num(H - s[i + 1])}" for i in (1, 3, 5)))
            else:
                out.append("Z")
        return " ".join(out)

    body = [f'<rect width="{num(page.width)}" height="{num(H)}" fill="#ffffff"/>']
    clip_n = 0
    defs = []
    uris: dict = {}
    for op in page.sorted_ops():
        if op["k"] == "image":
            # The file goes in as a data URI. The PDF matrix maps the unit square
            # (y up) to the page; the SVG image's unit box runs y down.
            r = op["raster"]
            if r.sha256 not in uris:
                uris[r.sha256] = f"data:{r.mime};base64," + base64.b64encode(r.original).decode("ascii")
            a, b, c, dd, e, f = op["matrix"]
            x0, y0, x1, y1 = op["clip"]
            clip_n += 1
            defs.append(f'<clipPath id="c{clip_n}"><rect x="{num(x0)}" y="{num(H - y1)}" '
                        f'width="{num(x1 - x0)}" height="{num(y1 - y0)}"/></clipPath>')
            m = " ".join(num(v, 4) for v in (a, -b, -c, dd, c + e, H - dd - f))
            body.append(f'<g clip-path="url(#c{clip_n})"><image width="1" height="1" '
                        f'preserveAspectRatio="none" style="image-orientation:none" '
                        f'transform="matrix({m})" href="{uris[r.sha256]}"/></g>')
        elif op["k"] == "path":
            attrs = [f'd="{d(op["segs"])}"', f'fill="{_hex(op["fill"])}"', f'stroke="{_hex(op["stroke"])}"',
                     f'stroke-width="{num(op["lw"])}"', 'stroke-linecap="round"', 'stroke-linejoin="round"']
            if op["evenodd"]:
                attrs.append('fill-rule="evenodd"')
            if op["dash"]:
                attrs.append(f'stroke-dasharray="{",".join(num(x) for x in op["dash"])}"')
            if op["clip"]:
                clip_n += 1
                defs.append(f'<clipPath id="c{clip_n}"><path d="{d(op["clip"])}"/></clipPath>')
                attrs.append(f'clip-path="url(#c{clip_n})"')
            body.append("<path " + " ".join(attrs) + "/>")
        else:
            x, y = run_start(op)
            weight = ' font-weight="bold"' if op["bold"] else ""
            rot = f' transform="rotate({num(-op["rot"])} {num(x)} {num(H - y)})"' if op["rot"] else ""
            ls = f' letter-spacing="{num(op["tracking"])}"' if op["tracking"] else ""
            body.append(f'<text x="{num(x)}" y="{num(H - y)}" font-family="Helvetica, Arial, sans-serif" '
                        f'font-size="{num(op["size"])}" fill="{_hex(op["color"])}"{weight}{ls}{rot}>'
                        f'{_esc(op["s"])}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{num(page.width / 72)}in" '
            f'height="{num(H / 72)}in" viewBox="0 0 {num(page.width)} {num(H)}">'
            f'<defs>{"".join(defs)}</defs>' + "".join(body) + "</svg>\n")


def write_svg(page, path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(to_svg(page))
