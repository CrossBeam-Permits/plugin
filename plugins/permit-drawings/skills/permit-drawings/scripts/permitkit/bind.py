"""Write the bound set and one PDF per sheet.

External PDFs (manufacturer data, forms) are merged only when pypdf happens to
be importable. Otherwise the build reports them, in position, so they are
attached separately. The kit never needs pypdf to draw.
"""
from __future__ import annotations

import os

from .pdf import write_pdf


def write_set(pages, out_dir: str, set_name: str, title: str = "", attachments=(),
              base_dir: str = ".") -> dict:
    """Write <set_name>.pdf and sheets/<id>.pdf. Returns relative file names."""
    os.makedirs(os.path.join(out_dir, "sheets"), exist_ok=True)
    set_pdf = f"{set_name}.pdf"
    write_pdf(pages, os.path.join(out_dir, set_pdf), title=title)
    sheet_pdfs = {}
    for pg in pages:
        rel = os.path.join("sheets", f"{pg.sheet_id}.pdf")
        write_pdf([pg], os.path.join(out_dir, rel), title=f"{pg.sheet_id} {pg.title}".strip())
        sheet_pdfs[pg.sheet_id] = rel
    report = []
    if attachments:
        merged = _merge(pages, out_dir, set_name, attachments, base_dir, set_pdf)
        for a in attachments:
            report.append({"id": a["id"], "path": a["path"], "position": a["position"],
                           "merged_into": merged})
    return {"set_pdf": set_pdf, "sheet_pdfs": sheet_pdfs, "attachments": report}


def _merge(pages, out_dir, set_name, attachments, base_dir, set_pdf):
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        return None
    w = PdfWriter()
    drawn = PdfReader(os.path.join(out_dir, set_pdf))
    by_pos = {a["position"]: a for a in attachments}
    di = 0
    for pos in range(len(pages) + len(attachments)):
        start = len(w.pages)
        if pos in by_pos:
            a = by_pos[pos]
            w.append(PdfReader(os.path.join(base_dir, a["path"])), import_outline=False)
            w.set_page_label(start, len(w.pages) - 1, prefix=a["id"])
        else:
            w.add_page(drawn.pages[di])
            w.set_page_label(start, start, prefix=pages[di].sheet_id)
            di += 1
    name = f"{set_name}-with-attachments.pdf"
    with open(os.path.join(out_dir, name), "wb") as fh:
        w.write(fh)
    return name
