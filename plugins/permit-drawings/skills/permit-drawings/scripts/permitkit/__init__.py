"""permitkit: a drafting kit for permit drawing sets. Python standard library only.

Axes for every model value: x = east, y = north, z = up. Lengths are real inches.
Paper is laid out in inches or points from the lower-left, x right, y up.

See references/drawing-kit.md (and its task cards) and references/project-file.md in the skill.
"""
__version__ = "0.9.10"


def __getattr__(name):
    # `from permitkit import energy` on an install without the optional energy
    # module says how to fetch it, instead of a bare "cannot import name".
    if name.startswith("_") or name == "optional":
        raise AttributeError(f"module 'permitkit' has no attribute {name!r}")
    import importlib
    optional = importlib.import_module(__name__ + ".optional")
    for mod, m in optional.manifest().items():
        if f"scripts/permitkit/{name}.py" in m["files"]:
            optional.require(mod, f"permitkit.{name}")
    raise AttributeError(f"module 'permitkit' has no attribute {name!r}")
