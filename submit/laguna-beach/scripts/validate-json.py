#!/usr/bin/env python3
"""Validate a canonical artifact without third-party schema dependencies."""

from __future__ import annotations

import argparse

from _lib import load_json
from _schema import validate_instance


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", required=True)
    parser.add_argument("document")
    args = parser.parse_args()
    schema = load_json(args.schema)
    document = load_json(args.document)
    errors = validate_instance(document, schema)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Valid: {args.document}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
