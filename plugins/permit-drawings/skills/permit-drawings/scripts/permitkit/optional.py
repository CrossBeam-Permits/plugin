"""Optional kit modules: energy, structural and 3D.

A core install of the skill leaves these files out, so an owner who never
draws a T sheet, a framing check or a 3D view never downloads them.
`modules.json` beside this file lists each module's files; the MCP server's
bundler reads the same file. A project block that needs a missing module
fails with the exact call that fetches it.
"""
from __future__ import annotations

import functools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(os.path.dirname(HERE))


class ModuleMissing(ImportError):
    """An optional module this work needs is not installed."""


@functools.lru_cache(maxsize=1)
def manifest() -> dict:
    with open(os.path.join(HERE, "modules.json"), encoding="utf-8") as fh:
        return json.load(fh)["modules"]


def missing_files(name: str) -> list[str]:
    return [f for f in manifest()[name]["files"] if not os.path.isfile(os.path.join(SKILL_ROOT, f))]


def installed(name: str) -> bool:
    return not missing_files(name)


def fetch_hint(name: str) -> str:
    return (f'Fetch it with crossbeam_get_skill {{"skill_id": "permit-drawings", "module": "{name}"}} and run its '
            "archive.install in the folder that holds the permit-drawings skill folder (references/00-connect.md "
            "section 3). Ask the owner first, as for any skill update.")


def message(name: str, why: str = "") -> str:
    """What to tell the agent when the module is missing: what it is and the call that fetches it."""
    need = f" for {why}" if why else ""
    return f"The optional {name} module ({manifest()[name]['title']}) is not installed{need}. {fetch_hint(name)}"


def require(name: str, why: str = "") -> None:
    """Raise ModuleMissing, naming the call that fetches the module, when it is not installed."""
    if not installed(name):
        raise ModuleMissing(message(name, why))


def for_blocks(data: dict) -> None:
    """Require every module whose project.json block is present and non-empty."""
    for name, m in manifest().items():
        present = [b for b in m["blocks"] if data.get(b)]
        if present:
            require(name, "the " + " and ".join(present) + " block in project.json")


def report() -> dict:
    """What `permitkit modules` prints."""
    out = {}
    for name, m in manifest().items():
        miss = missing_files(name)
        out[name] = {"installed": not miss, "title": m["title"], "when": m["when"], "reference": m["reference"]}
        if miss:
            out[name]["fetch"] = fetch_hint(name)
    return out
