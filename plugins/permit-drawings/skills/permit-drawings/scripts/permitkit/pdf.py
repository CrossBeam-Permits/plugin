"""A PDF writer from scratch, standard library only.

Fonts: the base-14 Helvetica and Helvetica-Bold with WinAnsiEncoding. They are
not embedded, so there is nothing to license.

Output is deterministic: no timestamps unless the caller passes one, fixed
number formatting, a document ID made from the content hash.

The MediaBox is the true sheet size in points (ARCH D = 2592 x 1728). No page
content uses a scaling transform, so a placed view prints at its stated scale.
"""
from __future__ import annotations

import hashlib
import math
import re
import zlib

from . import textmetrics as tm
from .display import run_start
from .units import num

PRODUCER = "permitkit"


def _esc(s: str) -> bytes:
    raw = s.encode("cp1252")
    out = bytearray()
    for b in raw:
        if b in (0x28, 0x29, 0x5C):          # ( ) \
            out += b"\\" + bytes([b])
        elif b < 32 or b > 126:
            out += f"\\{b:03o}".encode()
        else:
            out.append(b)
    return bytes(out)


def _pdf_str(s: str) -> bytes:
    """A string in a content stream or a page label: WinAnsi bytes."""
    return b"(" + _esc(s) + b")"


def _text_str(s: str) -> bytes:
    """A PDF text string (Info /Title, outline /Title): UTF-16BE with a byte
    order mark, written as hex. Readers decode a plain text string as
    PDFDocEncoding, which differs from WinAnsi for dashes, quotes and others."""
    return b"<FEFF" + tm.clean(s).encode("utf-16-be").hex().upper().encode() + b">"


def _color(c, stroke: bool) -> str:
    r, g, b = c
    if abs(r - g) < 1e-9 and abs(g - b) < 1e-9:
        return f"{num(r, 4)} {'G' if stroke else 'g'}"
    return f"{num(r, 4)} {num(g, 4)} {num(b, 4)} {'RG' if stroke else 'rg'}"


def _segs(segs) -> list[str]:
    out = []
    for s in segs:
        if s[0] == "M":
            out.append(f"{num(s[1])} {num(s[2])} m")
        elif s[0] == "L":
            out.append(f"{num(s[1])} {num(s[2])} l")
        elif s[0] == "C":
            out.append(" ".join(num(v) for v in s[1:]) + " c")
        elif s[0] == "Z":
            out.append("h")
    return out


def image_block(name: str, op) -> list[str]:
    """The operators that draw one placed image: clip to its box, map the unit
    square onto the placed image, paint. QA accepts a 'cm' only in this exact form."""
    x0, y0, x1, y1 = op["clip"]
    return ["q", f"{num(x0)} {num(y0)} {num(x1 - x0)} {num(y1 - y0)} re W n",
            " ".join(num(v, 4) for v in op["matrix"]) + " cm", f"/{name} Do", "Q"]


def image_names(pages) -> dict:
    """sha256 of each distinct image -> its XObject name, in first-use order."""
    names: dict = {}
    for pg in pages:
        for op in pg.sorted_ops():
            if op["k"] == "image" and op["raster"].sha256 not in names:
                names[op["raster"].sha256] = f"Im{len(names) + 1}"
    return names


def content_stream(page, names=None) -> bytes:
    """Turn a Page display list into PDF content operators."""
    names = names if names is not None else image_names([page])
    lines: list[str] = []
    for op in page.sorted_ops():
        if op["k"] == "image":
            lines += image_block(names[op["raster"].sha256], op)
        elif op["k"] == "path":
            lines.append("q")
            if op["clip"]:
                lines += _segs(op["clip"])
                lines.append("W* n" if op["evenodd"] else "W n")
            lines.append(f"{num(op['lw'])} w {op['cap']} J {op['join']} j")
            if op["dash"]:
                lines.append("[" + " ".join(num(d) for d in op["dash"]) + "] 0 d")
            if op["stroke"]:
                lines.append(_color(op["stroke"], True))
            if op["fill"]:
                lines.append(_color(op["fill"], False))
            lines += _segs(op["segs"])
            star = "*" if op["evenodd"] else ""
            if op["fill"] and op["stroke"]:
                lines.append("B" + star)
            elif op["fill"]:
                lines.append("f" + star)
            elif op["stroke"]:
                lines.append("S")
            else:
                lines.append("n")
            lines.append("Q")
        elif op["k"] == "text":
            x, y = run_start(op)
            a = math.radians(op["rot"])
            ca, sa = math.cos(a), math.sin(a)
            font = "/F2" if op["bold"] else "/F1"
            # Tc is graphics state and outlives ET, so set it on every run.
            tc = f" {num(op['tracking'])} Tc"
            lines.append(f"BT {font} {num(op['size'])} Tf{tc} {_color(op['color'], False)} "
                         f"{num(ca, 5)} {num(sa, 5)} {num(-sa, 5)} {num(ca, 5)} {num(x)} {num(y)} Tm")
            lines.append(_pdf_str(op["s"]).decode("latin-1") + " Tj ET")
    return ("\n".join(lines) + "\n").encode("latin-1")


def _font_dict(name: str, bold: bool) -> bytes:
    """Base-14 font, not embedded. /Widths makes a viewer that substitutes another
    font still advance each glyph by Helvetica metrics, so layout holds."""
    widths = []
    for code in range(32, 256):
        try:
            ch = bytes([code]).decode("cp1252")
        except UnicodeDecodeError:
            ch = " "
        widths.append(str(round(tm.text_width(ch, 1000.0, bold))))
    return (f"<< /Type /Font /Subtype /Type1 /BaseFont /{name} /Encoding /WinAnsiEncoding "
            f"/FirstChar 32 /LastChar 255 /Widths [{' '.join(widths)}] >>").encode()


class _Writer:
    def __init__(self):
        self.objs: list[bytes | None] = []

    def reserve(self) -> int:
        self.objs.append(None)
        return len(self.objs)

    def set(self, n: int, body: bytes) -> None:
        self.objs[n - 1] = body

    def add(self, body: bytes) -> int:
        self.objs.append(body)
        return len(self.objs)

    def stream(self, data: bytes, compress: bool) -> int:
        if compress:
            data = zlib.compress(data, 9)
            head = f"<< /Length {len(data)} /Filter /FlateDecode >>".encode()
        else:
            head = f"<< /Length {len(data)} >>".encode()
        return self.add(head + b"\nstream\n" + data + b"\nendstream")

    def image(self, r) -> int:
        """An image XObject, with its soft mask, palette and PNG predictor."""
        smask = self.image(r.smask) if r.smask is not None else None
        space = r.colorspace
        if isinstance(space, tuple):                    # ("Indexed", palette bytes)
            pal = self.add(f"<< /Length {len(space[1])} >>".encode() + b"\nstream\n" + space[1]
                           + b"\nendstream")
            space = f"[/Indexed /DeviceRGB {len(space[1]) // 3 - 1} {pal} 0 R]"
        else:
            space = "/" + space
        head = (f"<< /Length {len(r.data)} /Type /XObject /Subtype /Image /Width {r.width} "
                f"/Height {r.height} /ColorSpace {space} /BitsPerComponent {r.bpc} /Filter /{r.filter}")
        if r.predictor:
            colors, bpc, cols = r.predictor
            head += f" /DecodeParms << /Predictor 15 /Colors {colors} /BitsPerComponent {bpc} /Columns {cols} >>"
        if r.decode:
            head += " /Decode [" + " ".join(str(v) for v in r.decode) + "]"
        if smask is not None:
            head += f" /SMask {smask} 0 R"
        return self.add((head + " >>").encode() + b"\nstream\n" + r.data + b"\nendstream")

    def render(self, root: int, info: int) -> bytes:
        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for i, body in enumerate(self.objs, start=1):
            offsets.append(len(out))
            out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
        doc_id = hashlib.md5(bytes(out)).hexdigest()
        xref = len(out)
        out += f"xref\n0 {len(self.objs) + 1}\n0000000000 65535 f \n".encode()
        for off in offsets:
            out += f"{off:010d} 00000 n \n".encode()
        out += (f"trailer\n<< /Size {len(self.objs) + 1} /Root {root} 0 R /Info {info} 0 R "
                f"/ID [<{doc_id}> <{doc_id}>] >>\nstartxref\n{xref}\n%%EOF\n").encode()
        return bytes(out)


def write_pdf(pages, path: str | None = None, title: str = "", compress: bool = True,
              creation_date: str | None = None, outlines: bool = True) -> bytes:
    """Write pages (display.Page) to one PDF. Page labels are the sheet ids.

    creation_date: an optional PDF date string such as 'D:20260930000000Z'. It is
    left out by default so the output stays byte-identical across builds.
    """
    w = _Writer()
    catalog = w.reserve()
    pages_obj = w.reserve()
    f1 = w.add(_font_dict("Helvetica", False))
    f2 = w.add(_font_dict("Helvetica-Bold", True))
    names = image_names(pages)
    rasters = {op["raster"].sha256: op["raster"] for pg in pages for op in pg.ops if op["k"] == "image"}
    xobj = {sha: w.image(rasters[sha]) for sha in names}      # one object per distinct image
    kids = []
    for pg in pages:
        content = w.stream(content_stream(pg, names), compress)
        used = sorted({op["raster"].sha256 for op in pg.ops if op["k"] == "image"},
                      key=lambda sha: int(names[sha][2:]))
        xres = ""
        if used:
            xres = " /XObject << " + " ".join(f"/{names[sha]} {xobj[sha]} 0 R" for sha in used) + " >>"
        page_obj = w.add(
            (f"<< /Type /Page /Parent {pages_obj} 0 R "
             f"/MediaBox [0 0 {num(pg.width)} {num(pg.height)}] "
             f"/Resources << /Font << /F1 {f1} 0 R /F2 {f2} 0 R >>{xres} >> "
             f"/Contents {content} 0 R >>").encode())
        kids.append(page_obj)
    w.set(pages_obj, (f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] "
                      f"/Count {len(kids)} >>").encode())
    nums = b" ".join(f"{i} << /P ".encode() + _pdf_str(pg.sheet_id) + b" >>"
                     for i, pg in enumerate(pages))
    cat = b"<< /Type /Catalog /Pages " + f"{pages_obj} 0 R".encode()
    cat += b" /PageLabels << /Nums [" + nums + b"] >>"
    if outlines and pages:
        root_ol = w.reserve()
        items = [w.reserve() for _ in pages]
        for i, (pg, n) in enumerate(zip(pages, items)):
            label = pg.sheet_id + (" - " + pg.title if pg.title else "")
            body = b"<< /Title " + _text_str(label) + f" /Parent {root_ol} 0 R".encode()
            if i > 0:
                body += f" /Prev {items[i - 1]} 0 R".encode()
            if i < len(items) - 1:
                body += f" /Next {items[i + 1]} 0 R".encode()
            body += f" /Dest [{kids[i]} 0 R /Fit] >>".encode()
            w.set(n, body)
        w.set(root_ol, f"<< /Type /Outlines /First {items[0]} 0 R /Last {items[-1]} 0 R "
                       f"/Count {len(items)} >>".encode())
        cat += f" /Outlines {root_ol} 0 R /PageMode /UseOutlines".encode()
    cat += b" >>"
    w.set(catalog, cat)
    info = b"<< /Producer " + _pdf_str(PRODUCER)
    if title:
        info += b" /Title " + _text_str(title)
    if creation_date:
        info += b" /CreationDate " + _pdf_str(creation_date)
    info += b" >>"
    info_obj = w.add(info)
    data = w.render(catalog, info_obj)
    if path:
        with open(path, "wb") as fh:
            fh.write(data)
    return data


# ------------------------------------------------------------------ reading

def _objects(data: bytes) -> dict:
    """Object number -> body bytes, located through the xref table."""
    start = int(re.search(rb"startxref\s+(\d+)", data[-64:]).group(1))
    m = re.match(rb"xref\s+0 (\d+)\s+", data[start:])
    count = int(m.group(1))
    pos = start + m.end()
    objs = {}
    for i in range(count):
        entry = data[pos + 20 * i: pos + 20 * i + 20]
        off, _, kind = entry.split()[:3]
        if kind != b"n":
            continue
        off = int(off)
        hm = re.match(rb"(\d+) 0 obj\n", data[off:])
        body_start = off + hm.end()
        lm = re.match(rb"<< /Length (\d+)", data[body_start:])
        head_end = data.find(b">>\nstream\n", body_start)
        nl = data.find(b"\n", body_start)
        if lm and head_end != -1 and nl == head_end + 2:     # this writer's stream headers hold no newline
            end = head_end + len(b">>\nstream\n") + int(lm.group(1)) + len(b"\nendstream")
        else:
            end = data.index(b"\nendobj", body_start)
        objs[int(hm.group(1))] = data[body_start:end]
    return objs


def _hex_text(h: bytes) -> str:
    raw = bytes.fromhex(h.decode())
    return raw[2:].decode("utf-16-be") if raw[:2] == b"\xfe\xff" else raw.decode("latin-1")


def read_pdf(path_or_bytes) -> dict:
    """Minimal reader for PDFs this kit wrote: pages, MediaBoxes, labels, content.

    Mechanical parsing of a known format. It is not a general PDF parser.
    """
    data = path_or_bytes
    if isinstance(path_or_bytes, str):
        with open(path_or_bytes, "rb") as fh:
            data = fh.read()
    objs = _objects(data)
    pages_obj = next(b for b in objs.values() if b.startswith(b"<< /Type /Pages"))
    kids = [int(k) for k in re.findall(rb"(\d+) 0 R", pages_obj.split(b"/Kids", 1)[1].split(b"]")[0])]
    pages = []
    for k in kids:
        body = objs[k]
        mb = [float(v) for v in re.search(rb"/MediaBox \[([^\]]*)\]", body).group(1).split()]
        cnum = int(re.search(rb"/Contents (\d+) 0 R", body).group(1))
        sbody = objs[cnum]
        length = int(re.match(rb"<< /Length (\d+)", sbody).group(1))
        head, rest = sbody.split(b"\nstream\n", 1)
        raw = rest[:length]
        if b"/FlateDecode" in head:
            raw = zlib.decompress(raw)
        pages.append({"mediabox": mb, "content": raw})
    cat = next(b for b in objs.values() if b.startswith(b"<< /Type /Catalog"))
    labels = []
    m = re.search(rb"/PageLabels << /Nums \[(.*?)\] >>", cat, re.S)
    if m:
        for idx, lab in re.findall(rb"(\d+) << /P \(((?:\\.|[^\\)])*)\) >>", m.group(1)):
            labels.append((int(idx), re.sub(rb"\\(.)", rb"\1", lab).decode("cp1252")))
    title = None
    info = next((b for b in objs.values() if b.startswith(b"<< /Producer")), b"")
    m = re.search(rb"/Title <([0-9A-Fa-f]*)>", info)
    if m:
        title = _hex_text(m.group(1))
    outlines = [_hex_text(h) for h in re.findall(rb"<< /Title <([0-9A-Fa-f]*)> /Parent", data)]
    return {"page_count": len(pages), "pages": pages, "page_labels": labels,
            "header": data[:8].decode("latin-1"), "title": title, "outlines": outlines}


_RUN = re.compile(rb"BT /F([12]) (\S+) Tf (\S+) Tc [^\n]*? (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) Tm\n"
                  rb"\(((?:\\.|[^\\)])*)\) Tj ET")


def _unescape(b: bytes) -> str:
    out = bytearray()
    i = 0
    while i < len(b):
        if b[i] == 0x5C:
            if b[i + 1:i + 2].isdigit():
                out.append(int(b[i + 1:i + 4], 8))     # this writer always uses 3 digits
                i += 4
            else:
                out.append(b[i + 1])
                i += 2
        else:
            out.append(b[i])
            i += 1
    return bytes(out).decode("cp1252")


def text_runs(content: bytes) -> list[dict]:
    """Every text run in a content stream this kit wrote, as it appears in the PDF.

    Each run: s, bold, size, tracking, and x, y (start of the run on its
    baseline) and the rotation matrix a b c d. Mechanical parsing of the
    kit's own operator layout; it is not a general content-stream parser.
    """
    runs = []
    for m in _RUN.finditer(content):
        a, b, c, d, x, y = (float(m.group(i)) for i in range(4, 10))
        runs.append({"s": _unescape(m.group(10)), "bold": m.group(1) == b"2",
                     "size": float(m.group(2)), "tracking": float(m.group(3)),
                     "matrix": [a, b, c, d], "x": x, "y": y})
    return runs
