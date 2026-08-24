#!/usr/bin/env python3
"""Fail closed when an official form differs from its pinned source receipt."""

from __future__ import annotations

import argparse
import shutil
import urllib.error
import urllib.request
from pathlib import Path

from _lib import field_tree_sha256, load_json, require_pypdf, sha256_file, widget_inventory


def locate(directory: Path, form: dict) -> Path | None:
    for name in (form["cache_name"], form["download_name"]):
        candidate = directory / name
        if candidate.is_file():
            return candidate
    return None


def fetch(form: dict, directory: Path) -> Path:
    destination = directory / form["cache_name"]
    directory.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(form["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output)
    except (urllib.error.HTTPError, urllib.error.URLError) as exc:
        destination.unlink(missing_ok=True)
        raise RuntimeError(
            f"official download failed ({exc}); use the official source page in a visible browser, "
            f"download {form['official_name']}, and rerun with --forms-dir"
        ) from exc
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--forms-dir", required=True)
    parser.add_argument(
        "--form-id",
        "--only",
        dest="form_id",
        action="append",
        help="Verify one form id; repeat for more. --only is the concise alias.",
    )
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()

    pypdf = require_pypdf()
    manifest = load_json(args.manifest)
    forms_dir = Path(args.forms_dir)
    selected = set(args.form_id or [])
    failures: list[str] = []
    checked = 0

    for form in manifest["forms"]:
        if selected and form["id"] not in selected:
            continue
        try:
            path = locate(forms_dir, form)
            if path is None and args.fetch:
                path = fetch(form, forms_dir)
            if path is None:
                raise FileNotFoundError(
                    f"missing {form['cache_name']} or {form['download_name']} in {forms_dir}"
                )
            reader = pypdf.PdfReader(str(path))
            actual = {
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
                "pages": len(reader.pages),
                "canonical_fields": len(reader.get_fields() or {}),
                "widgets": len(widget_inventory(reader)),
                "field_tree_sha256": field_tree_sha256(reader),
            }
            differences = [
                f"{key}: expected {form[key]!r}, got {value!r}"
                for key, value in actual.items()
                if value != form[key]
            ]
            if differences:
                raise ValueError("; ".join(differences))
            checked += 1
            print(f"OK {form['id']}: {actual['sha256']}")
        except Exception as exc:
            failures.append(f"{form['id']}: {exc}")

    if selected - {item["id"] for item in manifest["forms"]}:
        failures.append(f"unknown form ids: {sorted(selected - {item['id'] for item in manifest['forms']})}")
    if failures:
        for failure in failures:
            print(f"ERROR {failure}")
        return 1
    print(f"Verified {checked} current official forms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
