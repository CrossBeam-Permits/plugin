#!/usr/bin/env python3
"""Inspect both the canonical AcroForm tree and page widgets."""

from __future__ import annotations

import argparse
from pathlib import Path

from _lib import (
    field_tree,
    field_tree_sha256,
    require_pypdf,
    sha256_file,
    utc_now,
    widget_inventory,
    write_json,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    pypdf = require_pypdf()
    source = Path(args.pdf)
    reader = pypdf.PdfReader(str(source))
    fields = field_tree(reader)
    widgets = widget_inventory(reader)
    write_json(
        args.output,
        {
            "schema_version": "1.0.0",
            "generated_at": utc_now(),
            "source": str(source.resolve()),
            "sha256": sha256_file(source),
            "bytes": source.stat().st_size,
            "pages": len(reader.pages),
            "canonical_field_count": len(fields),
            "widget_count": len(widgets),
            "field_tree_sha256": field_tree_sha256(reader),
            "fields": fields,
            "widgets": widgets,
        },
    )
    print(f"{len(fields)} canonical fields; {len(widgets)} widgets -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
