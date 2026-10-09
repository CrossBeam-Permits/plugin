#!/usr/bin/env python3
"""Mechanical helpers for checking an applicant-signed form.

These helpers only measure pixels. They never decide that a document is signed;
the agent still looks at the rendered crops and the applicant confirms.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any


def pdftoppm() -> str:
    executable = shutil.which("pdftoppm")
    if not executable:
        raise SystemExit("pdftoppm is required (install Poppler)")
    return executable


def page_sizes(reader: Any) -> list[tuple[float, float, int]]:
    sizes = []
    for page in reader.pages:
        box = page.mediabox
        sizes.append((float(box.width), float(box.height), int(page.get("/Rotate", 0) or 0)))
    return sizes


def scaled_rect(
    rect: list[float],
    source_size: tuple[float, float],
    target_size: tuple[float, float],
) -> list[float]:
    """Scale a rectangle from the unsigned page size to the signed page size."""

    sx = target_size[0] / source_size[0]
    sy = target_size[1] / source_size[1]
    return [rect[0] * sx, rect[1] * sy, rect[2] * sx, rect[3] * sy]


def crop_arguments(rect: list[float], page_height: float, dpi: int) -> list[str]:
    scale = dpi / 72.0
    x = int(round(rect[0] * scale))
    y = int(round((page_height - rect[3]) * scale))
    width = max(1, int(round((rect[2] - rect[0]) * scale)))
    height = max(1, int(round((rect[3] - rect[1]) * scale)))
    return ["-x", str(x), "-y", str(y), "-W", str(width), "-H", str(height)]


def render_crop(
    pdf: Path,
    page: int,
    rect: list[float],
    page_height: float,
    destination_prefix: Path,
    *,
    dpi: int = 150,
    gray: bool = False,
) -> Path:
    destination_prefix.parent.mkdir(parents=True, exist_ok=True)
    command = [pdftoppm(), "-f", str(page), "-l", str(page), "-r", str(dpi), "-singlefile"]
    command += crop_arguments(rect, page_height, dpi)
    command += ["-gray"] if gray else ["-png"]
    command += [str(pdf), str(destination_prefix)]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    suffix = ".pgm" if gray else ".png"
    output = destination_prefix.with_name(destination_prefix.name + suffix)
    if not output.is_file():
        raise RuntimeError(f"pdftoppm produced no crop for page {page}")
    return output


def read_pgm(path: Path) -> tuple[int, int, bytes]:
    data = path.read_bytes()
    tokens: list[bytes] = []
    index = 0
    while len(tokens) < 4:
        while data[index : index + 1].isspace():
            index += 1
        if data[index : index + 1] == b"#":
            while data[index : index + 1] not in (b"\n", b""):
                index += 1
            continue
        start = index
        while not data[index : index + 1].isspace():
            index += 1
        tokens.append(data[start:index])
    index += 1
    if tokens[0] != b"P5":
        raise ValueError(f"unsupported PGM format: {tokens[0]!r}")
    width, height, maximum = int(tokens[1]), int(tokens[2]), int(tokens[3])
    if maximum > 255:
        raise ValueError("16-bit PGM is not supported")
    return width, height, data[index : index + width * height]


def dark_fraction(pgm: Path, threshold: int = 128) -> float:
    width, height, pixels = read_pgm(pgm)
    if not pixels:
        return 0.0
    dark = sum(1 for value in pixels if value < threshold)
    return dark / float(width * height)


def signature_crops(
    pdf: Path,
    blocks: list[dict[str, Any]],
    sizes: list[tuple[float, float, int]],
    reference_sizes: list[tuple[float, float, int]] | None,
    output_dir: Path,
    *,
    dpi: int = 200,
) -> list[dict[str, Any]]:
    """Render each signature block as a PNG for visual review and measure its ink."""

    results = []
    for block in blocks:
        page = int(block["page"])
        if page > len(sizes):
            results.append({"id": block["id"], "error": f"page {page} is missing"})
            continue
        width, height, rotation = sizes[page - 1]
        rect = [float(item) for item in block["rect"]]
        if reference_sizes is not None:
            reference_width, reference_height, _ = reference_sizes[page - 1]
            rect = scaled_rect(rect, (reference_width, reference_height), (width, height))
        stem = output_dir / f"{block['id']}"
        png = render_crop(pdf, page, rect, height, stem, dpi=dpi)
        pgm = render_crop(pdf, page, rect, height, stem, dpi=dpi, gray=True)
        fraction = dark_fraction(pgm)
        pgm.unlink(missing_ok=True)
        results.append(
            {
                "id": block["id"],
                "kind": block.get("kind"),
                "page": page,
                "rect": rect,
                "rotation": rotation,
                "crop_png": str(png.resolve()),
                "dark_fraction": round(fraction, 5),
            }
        )
    return results
