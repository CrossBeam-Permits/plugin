#!/usr/bin/env python3
"""Render every PDF page to PNG for mandatory visual QA."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from _lib import sha256_file, utc_now, write_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dpi", type=int, default=150)
    args = parser.parse_args()

    executable = shutil.which("pdftoppm")
    if not executable:
        raise SystemExit("pdftoppm is required (install Poppler)")
    source = Path(args.pdf)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = output_dir / "page"
    subprocess.run(
        [executable, "-png", "-r", str(args.dpi), str(source), str(prefix)],
        check=True,
    )
    pages = sorted(path.name for path in output_dir.glob("page-*.png"))
    if not pages:
        raise SystemExit("render produced no PNG pages")
    write_json(
        output_dir / "render-manifest.json",
        {
            "schema_version": "1.0.0",
            "rendered_at": utc_now(),
            "source_pdf": str(source.resolve()),
            "source_sha256": sha256_file(source),
            "dpi": args.dpi,
            "pages": pages,
            "visual_status": "manual_review_required",
        },
    )
    print(f"Rendered {len(pages)} pages -> {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
