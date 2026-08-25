#!/usr/bin/env python3
"""Inventory task files without extracting or transmitting their contents."""

from __future__ import annotations

import argparse
import mimetypes
from pathlib import Path

from _lib import sha256_file, utc_now, write_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.directory).resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    files = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        files.append(
            {
                "path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "media_type": mimetypes.guess_type(path.name)[0] or "application/octet-stream",
            }
        )

    write_json(
        args.output,
        {
            "schema_version": "1.0.0",
            "root": str(root),
            "generated_at": utc_now(),
            "files": files,
        },
    )
    print(f"Inventoried {len(files)} files -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
