"""Load project.json, validate it, resolve values and check the model.

Every dimensional number is a Value: {v | expr, status, source?, fv?, note?}.
An `expr` is plain arithmetic over other value keys. A tiny parser reads it.
The kit never calls eval().

Axes, stated once for the whole kit: x = east, y = north, z = up. Lengths are
real inches.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import re

from fractions import Fraction

from . import schema as _schema
from .units import UnitError, fmt_len, unit_info

UNVERIFIED = ("ASSUMED", "PLACEHOLDER")      # statuses that need a field-verify tag
#: The most ranged estimates one check combines (every low/high mix: 2**10 = 1,024).
MAX_RANGED = 10
TRUE_NORTH_KEY = "axes.true_north_deg"   # value key of a true_north_deg given as a Value
GEOMETRY_KINDS = ("levels", "walls", "openings", "rooms", "stairs", "guards", "fixtures")
# Integer fields in geometry items that are counts or ranks, not dimensions.
NON_DIMENSIONAL = {"rank", "delta", "qty"}

#: A value key as written in a note template or a "$key" reference. Item ids
#: may hold a hyphen, so an inline key such as openings.W-1.width is one name.
KEY = r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_-]+)*"
#: A value key inside an expression. A hyphen is allowed only in a middle
#: segment (an item id), so "a-b" and "openings.W-1.width-a" still subtract.
_EXPR_KEY = r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_-]+(?=\.))*(?:\.[A-Za-z0-9_]+)?"



class SourceFloat(float):
    """A number read from project.json that remembers how it was written.

    json turns 0.30 into 0.3; a sheet that prints a limit or a value should
    keep the source's decimals (0.30 U-FACTOR, as the energy table prints it).
    It is a float everywhere else: arithmetic returns plain floats and json
    writes it back as a float.
    """

    __slots__ = ("text",)

    def __new__(cls, text):
        obj = super().__new__(cls, text)
        obj.text = str(text)
        return obj

    def __reduce__(self):
        return (SourceFloat, (self.text,))


def source_places(x) -> int | None:
    """Decimal places a number was written with: 0.30 -> 2, 12 -> 0, 7.6 -> 1.
    None when x is not a number. A computed float gives its shortest repr's places."""
    import decimal
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    if isinstance(x, int):
        return 0
    text = getattr(x, "text", None) or repr(float(x))
    exp = decimal.Decimal(text).as_tuple().exponent
    return min(6, max(0, -exp)) if isinstance(exp, int) else 0

class ProjectError(ValueError):
    """project.json is not valid. `.errors` lists every problem."""

    def __init__(self, errors):
        self.errors = list(errors)
        super().__init__("project.json is not valid:\n  " + "\n  ".join(self.errors))


class ExprError(ValueError):
    pass


class RangeError(ValueError):
    """A check rests on more ranged estimates than MAX_RANGED."""


class PrintRefused(ValueError):
    """The kit refused to print a value or a note. The message says why."""


# ------------------------------------------------------------------ expressions

_TOKEN = re.compile(r"\s*(?:(\d+(?:\.\d*)?|\.\d+)|(" + _EXPR_KEY + r")|(.))")
_FUNCS = {"min": min, "max": max, "abs": abs, "sqrt": math.sqrt, "hypot": math.hypot}


def _tokens(src: str):
    out = []
    pos = 0
    src = src.strip()
    while pos < len(src):
        m = _TOKEN.match(src, pos)
        if not m:
            raise ExprError(f"cannot read {src[pos:]!r}")
        number, ident, op = m.groups()
        if number is not None:
            x = float(number)
            if not math.isfinite(x):
                raise ExprError(f"number {number[:20]}... is too large")
            out.append(("num", x))
        elif ident is not None:
            out.append(("id", ident))
        elif op in "+-*/(),":
            out.append(("op", op))
        elif op.strip():
            raise ExprError(f"character {op!r} is not allowed in an expression")
        pos = m.end()
    out.append(("end", None))
    return out


class _Parser:
    """Recursive descent: expr := term (+|- term)*, term := unary (*|/ unary)*."""

    def __init__(self, src: str):
        self.src = src
        self.toks = _tokens(src)
        self.i = 0

    def peek(self):
        return self.toks[self.i]

    def take(self, kind=None, val=None):
        t = self.toks[self.i]
        if (kind and t[0] != kind) or (val and t[1] != val):
            raise ExprError(f"expected {val or kind} in {self.src!r}, got {t[1]!r}")
        self.i += 1
        return t

    def parse(self):
        node = self.expr()
        self.take("end")
        return node

    def expr(self):
        node = self.term()
        while self.peek() in (("op", "+"), ("op", "-")):
            op = self.take()[1]
            node = ("bin", op, node, self.term())
        return node

    def term(self):
        node = self.unary()
        while self.peek() in (("op", "*"), ("op", "/")):
            op = self.take()[1]
            node = ("bin", op, node, self.unary())
        return node

    def unary(self):
        if self.peek() == ("op", "-"):
            self.take()
            return ("neg", self.unary())
        if self.peek() == ("op", "+"):
            self.take()
            return self.unary()
        return self.atom()

    def atom(self):
        kind, val = self.peek()
        if kind == "num":
            self.take()
            return ("num", val)
        if kind == "id":
            self.take()
            if self.peek() == ("op", "("):
                if val not in _FUNCS:
                    raise ExprError(f"unknown function {val!r}; allowed: {', '.join(_FUNCS)}")
                self.take("op", "(")
                args = [self.expr()]
                while self.peek() == ("op", ","):
                    self.take()
                    args.append(self.expr())
                self.take("op", ")")
                return ("call", val, args)
            return ("id", val)
        if (kind, val) == ("op", "("):
            self.take()
            node = self.expr()
            self.take("op", ")")
            return ("paren", node)
        raise ExprError(f"unexpected {val!r} in {self.src!r}")


def parse_expr(src: str):
    """Parse an expression into a small tree. Raises ExprError."""
    try:
        return _Parser(src).parse()
    except RecursionError:
        raise ExprError(f"expression nests too deeply: {src[:40]!r}...") from None


def expr_names(node) -> list[str]:
    """Value keys that an expression tree reads, in order of first use."""
    out: list[str] = []

    def walk(n):
        k = n[0]
        if k == "id" and n[1] not in out:
            out.append(n[1])
        elif k == "bin":
            walk(n[2])
            walk(n[3])
        elif k in ("neg", "paren"):
            walk(n[1])
        elif k == "call":
            for a in n[2]:
                walk(a)
    walk(node)
    return out


def eval_expr(node, lookup) -> float:
    """Evaluate a tree. Every failure, and every non-finite result, is an ExprError."""
    try:
        x = _eval(node, lookup)
    except RecursionError:
        raise ExprError("expression nests too deeply") from None
    if not math.isfinite(x):
        raise ExprError(f"expression gives a non-finite result ({x})")
    return x


def _eval(node, lookup) -> float:
    k = node[0]
    if k == "num":
        return node[1]
    if k == "id":
        return lookup(node[1])
    if k == "neg":
        return -_eval(node[1], lookup)
    if k == "paren":
        return _eval(node[1], lookup)
    if k == "call":
        args = [_eval(a, lookup) for a in node[2]]
        try:
            out = float(_FUNCS[node[1]](*args))
        except (ValueError, TypeError, OverflowError) as exc:
            raise ExprError(f"{node[1]}({', '.join(_plain(a) for a in args)}) fails: {exc}") from None
        return _finite(out, node[1])
    a, b = _eval(node[2], lookup), _eval(node[3], lookup)
    op = node[1]
    if op == "+":
        return _finite(a + b, op)
    if op == "-":
        return _finite(a - b, op)
    if op == "*":
        return _finite(a * b, op)
    if b == 0:
        raise ExprError("division by zero")
    return _finite(a / b, op)


def _finite(x: float, what: str) -> float:
    if not math.isfinite(x):
        raise ExprError(f"'{what}' gives a non-finite result")
    return x


# ------------------------------------------------------------------ field-verify tags

#: A tag after its "FV-": up to three letters that group it (H for the hall), a
#: number, and an optional letter: 3, 2A, H11. Mirrors the Tag pattern in project.schema.json.
_FV_BODY = r"[A-Z]{0,3}\d+[A-Z]?"
_FV_TAG = re.compile(r"FV-([A-Z]{0,3})(\d+)([A-Z]?)")
#: A printed tag or a run of them: FV-3, or FV-1,8,H11 (FV-1, FV-8 and FV-H11).
FV_PRINTED = re.compile(r"\bFV-(" + _FV_BODY + r"(?:," + _FV_BODY + r")*)\b")


def fv_key(tag: str):
    """Natural order for FV tags: FV-1 < FV-2 < FV-2A < FV-10 < FV-H2 < FV-H11.

    Tags with no letter prefix come first, then each prefix in turn."""
    m = _FV_TAG.fullmatch(str(tag))
    return (0, m.group(1), int(m.group(2)), m.group(3)) if m else (1, "", 0, str(tag))


def fv_sorted(tags) -> list:
    """Tags once each, in natural order."""
    return sorted(dict.fromkeys(tags), key=fv_key)


def fv_text(tags) -> str:
    """The printed form of a value's FV tags: '' for none, FV-3 for one, and
    one run for several, FV-1,8,10 or FV-2,H11, in natural order. QA reads a run as every
    tag in it (fv_parse), so a compact run still proves each tag printed."""
    tags = fv_sorted(tags)
    if not tags:
        return ""
    return "FV-" + ",".join(t[3:] if t.startswith("FV-") else t for t in tags)


def fv_parse(text: str) -> list:
    """Every FV tag printed in a text, runs expanded: 'FV-1,8 FV-H3' -> [FV-1, FV-8, FV-H3]."""
    out = []
    for m in FV_PRINTED.finditer(str(text)):
        out += ["FV-" + n for n in m.group(1).split(",")]
    return fv_sorted(out)


#: Unit dimensions that only scale a product: 3 x a stud spacing is a length.
#: Alone in a sum they are kinds of their own (a count added to a length).
_SCALARS = ("count", "percent")


class _UnknownDims(Exception):
    pass


def _dims_of_unit(unit) -> dict:
    if unit is None:
        raise _UnknownDims
    try:
        dim, _f = unit_info(unit)
    except UnitError:
        raise _UnknownDims from None
    if dim == "length":
        return {"length": 1}
    if dim == "area":
        return {"length": 2}
    return {dim: 1}


def _dims_mul(a: dict, b: dict, sign: int) -> dict:
    out: dict = {}
    for d, side in ((a, 1), (b, sign)):
        for k, e in d.items():
            if k in _SCALARS:
                continue
            out[k] = out.get(k, 0) + e * side
    return {k: e for k, e in out.items() if e}


def dims_name(d: dict) -> str:
    """A unit kind in words: length, area, in/ft, count, length x in/ft."""
    if not d:
        return "a plain number"
    if d == {"length": 2}:
        return "area"
    parts = []
    for k, e in sorted(d.items()):
        base = k.split(", ")[-1]
        parts += [base] * e if e > 0 else [f"1/{base}"] * -e
    return " x ".join(parts)


def expr_unit_mixes(node, unit_of) -> list[tuple[dict, dict]]:
    """Every + or - (and min/max/hypot) in an expression whose two sides are
    values of different unit kinds: [(left kind, right kind)].

    A value's kind comes from its unit (unit_of(name)): a length, an area
    (length x length), a slope in/ft, a count and so on. A constant takes the
    kind of whatever it meets, and a count or percent only scales a product.
    An expression that reads a unit the kit does not know is not judged.
    """
    mixes: list[tuple[dict, dict]] = []

    def same(a, b):
        if a is None:
            return b
        if b is not None and a != b:
            mixes.append((a, b))
        return a

    def walk(n):
        k = n[0]
        if k == "num":
            return None
        if k == "id":
            return _dims_of_unit(unit_of(n[1]))
        if k in ("neg", "paren"):
            return walk(n[1])
        if k == "call":
            got = [walk(a) for a in n[2]]
            if n[1] == "sqrt":
                d = got[0]
                if d is None:
                    return None
                if any(e % 2 for e in d.values()):
                    raise _UnknownDims
                return {key: e // 2 for key, e in d.items()}
            out = None
            for g in got:
                out = same(out, g)
            return out
        a, b = walk(n[2]), walk(n[3])
        op = n[1]
        if op in "+-":
            return same(a, b)
        if b is None:
            return a
        if a is None:
            return _dims_mul({}, b, -1) if op == "/" else b
        return _dims_mul(a, b, 1 if op == "*" else -1)

    try:
        walk(node)
    except _UnknownDims:
        return []
    return mixes


def const_text(v: float) -> str:
    """A constant as a whole number or an exact fraction, never a decimal.

    Raises PrintRefused when the constant is not a fraction with a power-of-two
    denominator up to 64; write such a constant as a division (x / 144).
    """
    f = Fraction(v).limit_denominator(64)
    if abs(float(f) - v) > 1e-9 or f.denominator not in (1, 2, 4, 8, 16, 32, 64):
        raise PrintRefused(f"constant {v!r} cannot print as a fraction; write it as a "
                           "division such as x / 144, or make it a named value")
    sign = "-" if f < 0 else ""
    f = abs(f)
    whole, rest = divmod(f.numerator, f.denominator)
    if not rest:
        return f"{sign}{whole}"
    frac = f"{rest}/{f.denominator}"
    return f"{sign}{whole} {frac}" if whole else f"{sign}{frac}"


def render_expr(node, fmt_name, fmt_const=None, additive: bool = True) -> str:
    """Print an expression tree with each name replaced by fmt_name(name).

    fmt_const(v, additive) prints a constant. `additive` is True when the
    constant is added to or subtracted from other terms (so it has the unit of
    the result), and False when it multiplies or divides. The default prints
    whole numbers and exact fractions, never decimals.
    """
    fmt_const = fmt_const or (lambda v, _add: const_text(v))
    k = node[0]
    if k == "num":
        return fmt_const(node[1], additive)
    if k == "id":
        return fmt_name(node[1])
    if k == "neg":
        return "-" + render_expr(node[1], fmt_name, fmt_const, additive)
    if k == "paren":
        return "(" + render_expr(node[1], fmt_name, fmt_const, additive) + ")"
    if k == "call":
        inner = additive and node[1] != "sqrt"
        return node[1].upper() + "(" + ", ".join(
            render_expr(a, fmt_name, fmt_const, inner) for a in node[2]) + ")"
    op = node[1]
    side = op in "+-"
    sym = {"*": "x", "/": "/"}.get(op, op)
    return (f"{render_expr(node[2], fmt_name, fmt_const, side)} {sym} "
            f"{render_expr(node[3], fmt_name, fmt_const, side)}")


# ------------------------------------------------------------------ values


class Value:
    """A resolved dimensional value. Lengths are inches unless `unit` says otherwise."""

    __slots__ = ("key", "v", "status", "fv", "source", "note", "expr", "unit",
                 "deps", "unverified_inputs", "fv_tags", "raw")

    def __init__(self, key, v, status, fv=None, source=None, note=None, expr=None,
                 unit="in", deps=(), unverified_inputs=(), fv_tags=(), raw=None):
        self.key = key
        self.v = v
        self.status = status
        self.fv = fv
        self.source = source
        self.note = note
        self.expr = expr
        self.unit = unit
        self.deps = tuple(deps)
        self.unverified_inputs = tuple(unverified_inputs)
        self.fv_tags = tuple(fv_sorted(fv_tags))
        self.raw = raw or {}

    def __float__(self):
        if isinstance(self.v, (list, tuple)):
            raise TypeError(f"{self.key} is a point, not a number")
        return float(self.v)

    @property
    def unverified(self) -> bool:
        """True when this value is ASSUMED or PLACEHOLDER, or derives from one."""
        return bool(self.unverified_inputs)

    def __repr__(self):
        return f"Value({self.key}={self.v!r} {self.status})"


def inside_dir(path: str, folder: str) -> bool:
    """True when path, after resolving links, is folder or something inside it."""
    path, folder = os.path.realpath(path), os.path.realpath(folder)
    return os.path.commonpath([path, folder]) == folder


# ------------------------------------------------------------------ project


class Project:
    """A loaded project file. Use Project.load(path)."""

    def __init__(self, data: dict, path: str | None = None):
        self.data = data
        self.path = os.path.abspath(path) if path else None
        self.dir = os.path.dirname(self.path) if self.path else os.getcwd()
        self.issues: list[dict] = []
        self.values: dict[str, Value] = {}
        self._trees: dict[str, tuple] = {}
        self._toward: dict[str, str] | None = None
        self.fv = {e["tag"]: e for e in data.get("field_verify", [])}
        self.sources = {s["id"]: s for s in data.get("sources", [])}
        self.meta = data.get("project", {})
        self.axes = data.get("axes", {})
        drawing = data.get("drawing", {})
        self.denom = int(drawing.get("precision_denominator", 16))
        self.dim_style = drawing.get("dim_style", "ftin")
        self.sheet_size = drawing.get("sheet_size", "ARCH_D")
        self.orientation = drawing.get("orientation", "landscape")
        self.set_name = drawing.get("set_name", "permit-set")
        self.sheets = list(data.get("sheets", []))
        self.revisions = list(data.get("revisions", []))
        self._inline: dict[str, dict] = {}
        self.struct = None
        # A block that needs an optional module (energy, structural, 3D) that this
        # install left out fails here, naming the call that fetches it (optional.py).
        from . import optional
        try:
            optional.for_blocks(data)
        except optional.ModuleMissing as exc:
            raise ProjectError([str(exc)]) from None
        self._resolve_all()
        # ---- structure block (struct.py): derived code checks join `rules` before _check.
        # An empty object is schema-valid and is not a block (optional.for_blocks).
        if data.get("structure"):
            from .struct import attach
            self.data = attach(self)
        self._check()

    # ---- loading

    @classmethod
    def load(cls, path: str) -> "Project":
        """Read, schema-check and resolve a project file. Raises ProjectError on schema errors."""
        with open(path, "rb") as fh:
            raw = fh.read()
        try:
            data = json.loads(raw.decode("utf-8"), parse_float=SourceFloat)
        except json.JSONDecodeError as exc:
            raise ProjectError([f"$: not valid JSON: {exc}"]) from None
        errs = _validate(data)
        if errs:
            raise ProjectError(errs)
        p = cls(data, path)
        p.sha256 = hashlib.sha256(raw).hexdigest()
        return p

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        errs = _validate(data)
        if errs:
            raise ProjectError(errs)
        p = cls(data)
        p.sha256 = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
        return p

    def issue(self, severity: str, code: str, where: str, msg: str) -> None:
        self.issues.append({"severity": severity, "code": code, "where": where, "msg": msg})

    @property
    def errors(self) -> list[dict]:
        return [i for i in self.issues if i["severity"] == "error"]

    # ---- resolution

    def _resolve_all(self) -> None:
        raw_values = dict(self.data.get("values", {}))
        # Inline Values in geometry and chains get a key from their path.
        for kind in GEOMETRY_KINDS:
            for item in self.data.get(kind, []):
                for field, val in item.items():
                    if isinstance(val, dict) and "status" in val:
                        key = f"{kind}.{item['id']}.{field}"
                        raw_values[key] = val
                        self._inline[key] = val
        for chain in self.data.get("chains", []):
            for i, seg in enumerate(chain["segments"]):
                if isinstance(seg["len"], dict):
                    raw_values[f"chains.{chain['id']}.{i}"] = seg["len"]
                    self._inline[f"chains.{chain['id']}.{i}"] = seg["len"]
            if isinstance(chain["total"], dict):
                raw_values[f"chains.{chain['id']}.total"] = chain["total"]
                self._inline[f"chains.{chain['id']}.total"] = chain["total"]
        for key, val in model3d_inline(self.data):
            raw_values[key] = val
            self._inline[key] = val
        tn = self.axes.get("true_north_deg")
        if isinstance(tn, dict):
            raw = dict(tn)
            raw.setdefault("unit", "deg")
            raw_values[TRUE_NORTH_KEY] = raw
            self._inline[TRUE_NORTH_KEY] = tn
        # ---- structure block (struct.py): its inline Values get keys like structure.members.J-1.span
        if self.data.get("structure"):
            from .struct import inline_values
            for key, raw in inline_values(self.data["structure"]).items():
                raw_values[key] = raw
                self._inline[key] = raw
        self._raw = raw_values
        visiting: set[str] = set()
        for key in raw_values:
            try:
                self._resolve(key, visiting)
            except ExprError as exc:
                self.issue("error", "expr", key, str(exc))
            except RecursionError:
                self.issue("error", "expr", key, "expressions refer to each other too deeply")

    def _resolve(self, key: str, visiting: set) -> Value:
        if key in self.values:
            return self.values[key]
        if key not in self._raw:
            raise ExprError(f"unknown value key {key!r}")
        if key in visiting:
            raise ExprError(f"circular expression through {key!r}")
        visiting.add(key)
        try:
            return self._resolve_body(key, visiting)
        finally:
            visiting.discard(key)

    def _resolve_body(self, key: str, visiting: set) -> Value:
        r = self._raw[key]
        status = r["status"]
        deps: list[str] = []
        unverified: list[str] = [key] if status in UNVERIFIED else []
        if "expr" in r:
            tree = parse_expr(r["expr"])
            self._trees[key] = tree
            deps = expr_names(tree)

            def look(name):
                dv = self._resolve(name, visiting)
                if isinstance(dv.v, (list, tuple)):
                    raise ExprError(f"{name} is a point and cannot be used in arithmetic")
                return float(dv.v)
            v = eval_expr(tree, look)
            for d in deps:
                for u in self.values[d].unverified_inputs:
                    if u not in unverified:
                        unverified.append(u)
        else:
            v = r["v"]
            nums = v if isinstance(v, list) else [v]
            if not all(math.isfinite(float(x)) for x in nums):
                raise ExprError(f"{key} has a non-finite number {v!r}")
            if isinstance(v, list):
                v = tuple(v)
        tags = fv_sorted(self._raw[u]["fv"] for u in unverified if self._raw[u].get("fv"))
        val = Value(key, v, status, fv=r.get("fv"), source=r.get("source"), note=r.get("note"),
                    expr=r.get("expr"), unit=r.get("unit", "in"), deps=deps,
                    unverified_inputs=unverified, fv_tags=tags, raw=r)
        self.values[key] = val
        return val

    # ---- access

    def value(self, key: str) -> Value:
        """The Value for a key. A leading '$' is allowed."""
        k = key[1:] if key.startswith("$") else key
        if k not in self.values:
            raise KeyError(f"no value {k!r} in project.json")
        return self.values[k]

    __getitem__ = value

    def lookup(self, key: str) -> Value:
        """The Value for a key, also through an item field that holds a reference.

        `$openings.D-2.width` names the field `width` of opening D-2. The field
        may hold an inline Value (then it is a value key of its own) or a
        reference such as "$bed_door_w" (then this follows it). Raises KeyError.
        """
        k = key[1:] if key.startswith("$") else key
        if k in self.values:
            return self.values[k]
        kind, _, rest = k.partition(".")
        ident, _, field = rest.rpartition(".")
        if kind in GEOMETRY_KINDS and ident and field:
            try:
                ref = self.item(kind, ident).get(field)
            except KeyError:
                ref = None
            if isinstance(ref, str) and ref.startswith("$"):
                return self.value(ref)
        raise KeyError(f"no value {k!r} in project.json")

    def v(self, key: str) -> float:
        """The number for a key."""
        return float(self.value(key))

    def pt(self, key: str) -> tuple:
        """A point value [x, y] for a key."""
        val = self.value(key)
        if not isinstance(val.v, tuple):
            raise TypeError(f"{key} is not a point")
        return val.v

    def dim(self, ref) -> Value:
        """Resolve a Dim: a '$key' string, a key, or an inline Value already loaded."""
        if isinstance(ref, Value):
            return ref
        if isinstance(ref, str):
            return self.value(ref)
        for key, raw in self._inline.items():
            if raw is ref:
                return self.values[key]
        raise TypeError(f"cannot resolve {ref!r} to a value")

    @property
    def true_north(self) -> Value | None:
        """Clockwise angle from plan north to true north, as a Value, or None.

        `axes.true_north_deg` may be a Value with a status (an ASSUMED north
        carries its FV tag) or, in older files, a plain number. A plain number
        has no status; it comes back as a Value with status None and draws as
        it did before.
        """
        tn = self.axes.get("true_north_deg")
        if tn is None:
            return None
        if isinstance(tn, dict):
            return self.values[TRUE_NORTH_KEY]
        return Value(TRUE_NORTH_KEY, float(tn), None, unit="deg")

    def items(self, kind: str) -> list[dict]:
        return list(self.data.get(kind, []))

    def item(self, kind: str, ident: str) -> dict:
        for it in self.data.get(kind, []):
            if it["id"] == ident:
                return it
        raise KeyError(f"no {kind} item {ident!r}")

    def field(self, kind: str, ident: str, name: str) -> Value:
        """The Value of one field of a geometry item, e.g. field('openings', 'W-1', 'width')."""
        return self.dim(self.item(kind, ident)[name])

    def fmt(self, key_or_value, style: str | None = None):
        """A length in fractions, followed by the FV tag of every unverified input.

        Returns a notes.Txt that remembers the value key and its tags. Refuses a
        value that rests on a PLACEHOLDER, or on an unverified value with no
        FV tag. Prefer kit.text("{key}") in notes: concatenating this result
        with other text keeps the printed tags but loses the recorded key.
        """
        from .notes import Txt, tags_for
        val = key_or_value if isinstance(key_or_value, Value) else self.value(key_or_value)
        if val.unit != "in":
            raise PrintRefused(f"{val.key} has unit {val.unit}; fmt() prints lengths only. "
                               "Use kit.text with a format code")
        tags = tags_for(self, val)
        style = style or self.dim_style
        rng, toward = self.range_of(val.key), self.round_toward(val.key)
        text = fmt_len(float(val), style, self.denom, toward) if rng is None else \
            range_text(*(fmt_len(e, style, self.denom, toward) for e in rng))
        if tags:
            text += " " + fv_text(tags)
        return Txt(text, keys=[val.key], fv=tags)

    def explain(self, key: str, style: str = "in") -> str:
        """The arithmetic behind a DERIVED value, e.g. '216" - 104" = 112"'.

        Untagged: a caller that prints it adds the FV tags (kit.text does).
        Constants print as whole numbers or fractions, with an inch mark when
        they add to or subtract from a length.
        """
        from .notes import value_text
        val = self.value(key)
        if self.range_of(val.key):
            raise PrintRefused(f"{val.key} rests on a range of estimates {self.ranged_inputs([val.key])}; "
                               "its arithmetic has no one answer. Print the value itself, which prints its range")

        def text(v):
            return value_text(self, v, style if v.unit == "in" else None)
        if val.key not in self._trees:
            return text(val)
        tree = self._trees[val.key]

        def const(c, additive):
            if additive and val.unit == "in":
                const_text(c)            # refuses a constant that is not an exact fraction
                if (Fraction(c) * self.denom).denominator != 1:
                    raise PrintRefused(f"constant {c!r} in {val.key} is finer than 1/{self.denom} in.")
                return fmt_len(c, style, self.denom)
            return const_text(c)
        return f"{render_expr(tree, lambda n: text(self.values[n]), const)} = {text(val)}"

    def unverified_in(self, keys) -> list[str]:
        """Every ASSUMED or PLACEHOLDER input behind the given keys."""
        out: list[str] = []
        for k in keys:
            for u in self.value(k).unverified_inputs:
                if u not in out:
                    out.append(u)
        return out

    # ---- ranges: an ASSUMED number with its low and high estimate

    def own_range(self, key: str) -> tuple | None:
        """The (low, high) that a value's own `range` states, or None.

        Only an ASSUMED value with a number `v` inside a low-to-high range has
        one; _check reports any other `range` as an error, and it counts for nothing.
        """
        r = self._raw.get(key[1:] if key.startswith("$") else key) or {}
        if "range" not in r or _range_problem(r):
            return None
        return float(r["range"][0]), float(r["range"][1])

    def ranged_inputs(self, keys) -> list[str]:
        """Every ranged ASSUMED input behind the given keys, in order of first use."""
        out: list[str] = []
        for k in keys:
            for u in self.value(k).unverified_inputs:
                if u not in out and self.own_range(u):
                    out.append(u)
        return out

    def estimates(self, keys) -> list[list[float]]:
        """The numbers of `keys` at every mix of the low and high ends of the
        ranged estimates behind them: one list per mix, in key order.

        A key that rests on no range has its one number in every list; with no
        range at all there is one list. Values that share an estimate move
        together, so a difference of two of them is never wider than it can be.
        Raises RangeError past MAX_RANGED estimates, ExprError when a mix
        breaks an expression (a division by zero).
        """
        keys = [self.value(k).key for k in keys]
        roots = self.ranged_inputs(keys)
        if len(roots) > MAX_RANGED:
            raise RangeError(f"rests on {len(roots)} ranged estimates ({', '.join(roots)}); "
                             f"the kit combines at most {MAX_RANGED}")
        out = []
        for ends in itertools.product(*(self.own_range(u) for u in roots)):
            at = dict(zip(roots, ends))
            out.append([self._value_at(k, at) for k in keys])
        return out

    def _value_at(self, key: str, at: dict) -> float:
        """A value's number with the estimates in `at` set to the given ends."""
        if key in at:
            return at[key]
        val = self.values[key]
        if key not in self._trees or not any(u in at for u in val.unverified_inputs):
            return float(val)
        return eval_expr(self._trees[key], lambda n: self._value_at(n, at))

    def monotone(self, keys) -> bool:
        """False when a formula behind the keys uses abs, hypot, min or max over
        a ranged estimate: such a number can fail at both ends and pass between
        them, or pass at both ends and fail between them, so the ends alone
        cannot prove a failure or a pass."""
        seen: set = set()

        def walk(key):
            if key in seen:
                return True
            seen.add(key)
            tree = self._trees.get(key)
            if tree is None or not self.ranged_inputs([key]):
                return True
            if _calls(tree) & {"abs", "hypot", "min", "max"}:
                return False
            return all(walk(d) for d in self.values[key].deps)
        return all(walk(self.value(k).key) for k in keys)

    def round_toward(self, key: str) -> str | None:
        """How a length prints off the 1/denom grid: "up" for a value a rule caps
        (op <=), "down" for one a rule sets a minimum on (>=), so the printed number
        never reads better than the value (3.711 in. under a 4 in. cap prints
        3 3/4", not 3 11/16"). None (nearest) for a value with no such rule, or with both."""
        if self._toward is None:
            ops: dict[str, set] = {}
            for r in self.data.get("rules", []):
                chk = r.get("check") or {}
                if "value" not in chk or chk.get("op") not in ("<=", ">="):
                    continue
                try:
                    k = self.lookup(chk["value"]).key
                except (KeyError, TypeError, ValueError):
                    continue
                ops.setdefault(k, set()).add(chk["op"])
            self._toward = {k: "up" if o == {"<="} else "down" for k, o in ops.items() if len(o) == 1}
        return self._toward.get(key)

    def range_of(self, key: str) -> tuple | None:
        """(low, high) of a number over the ranged estimates behind it, or None
        when it rests on none. A DERIVED value from a ranged input has a range too.
        The drawn number is included, so the printed span cannot leave it out.
        Raises PrintRefused when the estimates cannot be combined."""
        val = self.values.get(key[1:] if key.startswith("$") else key)
        if val is None or not self.ranged_inputs([val.key]):
            return None
        try:
            xs = [e[0] for e in self.estimates([val.key])]
        except (ExprError, RangeError) as exc:
            raise PrintRefused(f"{val.key}: its range of estimates cannot be worked out: {exc}") from None
        # The drawn number sits in the printed span. A bend (max, abs) can put
        # it outside the corner mixes, and the sheet must not show a number the
        # project value is not.
        if not isinstance(val.v, (list, tuple)):
            xs.append(float(val))
        return min(xs), max(xs)

    def check_claim(self, text: str, depends_on) -> None:
        """Refuse a compliance note that rests on an unverified value.

        The author states which value keys the note depends on. If any of them is
        ASSUMED or PLACEHOLDER, or derives from one, raise PrintRefused.
        """
        bad = self.unverified_in(depends_on)
        if bad:
            tags = sorted({self._raw[b].get("fv") or "NO TAG" for b in bad})
            raise PrintRefused(
                f"note claims compliance but depends on unverified values {bad} "
                f"({', '.join(tags)}): {text!r}. Measure them first, or rewrite the note "
                "so it states the requirement and the field-verify tag instead of a claim.")

    # ---- checks

    def _check(self) -> None:
        for key, val in self.values.items():
            r = val.raw
            if val.status == "ASSUMED" and not val.fv:
                self.issue("warning", "assumed-without-tag", key,
                           "ASSUMED value has no fv tag; the kit will refuse to print it")
            elif val.status == "PLACEHOLDER" and not val.fv:
                self.issue("warning", "placeholder-without-tag", key,
                           "PLACEHOLDER value holds a place only; the kit refuses to print it "
                           "and anything derived from it. This is expected until a value replaces it")
            if "range" in r:
                why = _range_problem(r)
                if why:
                    self.issue("error", "range", key, why)
            try:
                self.range_of(key)
            except PrintRefused as exc:
                self.issue("error", "range", key, str(exc))
            if r.get("fv") and r["fv"] not in self.fv:
                self.issue("error", "unknown-fv", key, f"fv tag {r['fv']} is not in field_verify")
            if r.get("source") and r["source"] not in self.sources:
                self.issue("error", "unknown-source", key, f"source {r['source']!r} is not in sources")
            if "expr" in r and val.status == "MEASURED":
                self.issue("error", "computed-measured", key,
                           "a value computed from an expr cannot be MEASURED; use DERIVED")
            if val.status == "DERIVED" and "expr" not in r and not r.get("source"):
                self.issue("warning", "derived-without-expr", key,
                           "DERIVED value has no expr, so its arithmetic cannot be shown; a value read "
                           "from a table names the table in source")
            if val.status == "MEASURED" and not r.get("source"):
                self.issue("warning", "measured-without-source", key,
                           "MEASURED value has no source; record where the number came from")
        for tag, entry in self.fv.items():
            for k in entry.get("values", []):
                if k not in self.values:
                    self.issue("error", "fv-unknown-value", tag, f"lists unknown value {k!r}")
        seen_cd: set = set()
        for entry in self.data.get("code_notes", []):
            if entry["cd"] in seen_cd:
                self.issue("error", "code-note-duplicate", entry["cd"], "listed twice in code_notes")
            seen_cd.add(entry["cd"])
        used = {v.fv for v in self.values.values() if v.fv}
        # --- structure block (struct.py): design values carry FV tags but are not kit Values
        if self.data.get("structure"):
            from .struct import fv_tags
            used |= fv_tags(self.data["structure"])
        # ---
        for tag in self.fv:
            if tag not in used and not self.fv[tag].get("values"):
                self.issue("warning", "fv-unused", tag, "no value carries this tag")
        for src in self.sources.values():
            if src["kind"] in ("sketch", "photo", "scan") and not src.get("orientation_note"):
                self.issue("error", "no-orientation", src["id"],
                           "record which compass direction is up in this image")
        self._check_true_north()
        self._check_expr_units()
        self._check_bare_numbers()
        self._check_opening_walls()
        self._check_refs()
        self._check_paths()
        self._check_chains()
        self._check_rules()
        self._check_images_finishes()
        self._check_connections()
        # ---- energy and green blocks (energy.py, greensheets.py: the optional energy module)
        if self.data.get("energy") or self.data.get("green"):
            from . import energy, greensheets
            energy.validate(self)
            greensheets.validate(self)
        # ----
        self._check_model3d()
        ids = [s["id"] for s in self.sheets]
        if not ids:
            self.issue("warning", "no-sheets", "sheets",
                       "no sheets listed yet; fine while measuring, but build needs at least one")
        for sid in sorted({i for i in ids if ids.count(i) > 1}):
            self.issue("error", "duplicate-sheet", sid, "sheet id appears more than once")
        deltas = [r["delta"] for r in self.revisions]
        for d in sorted({d for d in deltas if deltas.count(d) > 1}):
            self.issue("error", "duplicate-revision", str(d), "revision delta appears more than once")

    def _check_true_north(self) -> None:
        """axes.true_north_deg must resolve to one angle in degrees."""
        val = self.values.get(TRUE_NORTH_KEY)
        if val is None:
            return
        if isinstance(val.v, (list, tuple)):
            self.issue("error", "true-north-not-angle", TRUE_NORTH_KEY,
                       "true_north_deg is a point; it must be one angle in degrees")
        if val.unit != "deg":
            self.issue("error", "true-north-not-angle", TRUE_NORTH_KEY,
                       f"true_north_deg has unit {val.unit!r}; it must be deg")

    def _check_expr_units(self) -> None:
        """Warn when an expr adds or subtracts values of different unit kinds.

        plate + ext_w / 2 * roof_pitch / 12 adds a length to a length x in/ft
        term: the arithmetic may be right, but nothing says the /12 turns the
        slope into a rise. Compute the conversion in its own value with the
        result's unit (roof_rise: ext_w / 2 * roof_pitch / 12, unit in) and add
        that. A warning, not an error, so an existing file still builds.
        """
        for key, tree in self._trees.items():
            if key not in self.values:
                continue

            def unit_of(name):
                v = self.values.get(name)
                return v.unit if v is not None else None
            for a, b in expr_unit_mixes(tree, unit_of):
                self.issue("warning", "expr-unit-mix", key,
                           f"expr {self.values[key].expr!r} adds or compares {dims_name(a)} with "
                           f"{dims_name(b)}. Put the converted term in a value of its own whose unit says what the "
                           "term is (a rise from a pitch: roof_rise = run / 12 * roof_pitch, unit in), then add that")

    def _check_bare_numbers(self) -> None:
        def walk(node, where):
            if isinstance(node, bool) or node is None:
                return
            if isinstance(node, (int, float)):
                self.issue("error", "bare-number", where,
                           "dimensional numbers must be a Value {v, status} or a '$key' reference")
            elif isinstance(node, dict):
                if "status" in node and ("v" in node or "expr" in node):
                    return
                for k, v in node.items():
                    if k not in NON_DIMENSIONAL:
                        walk(v, f"{where}.{k}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, f"{where}[{i}]")
        for kind in GEOMETRY_KINDS:
            for item in self.data.get(kind, []):
                walk({k: v for k, v in item.items() if k != "id"}, f"{kind}.{item['id']}")
        for item in (self.data.get("model3d") or {}).get("elements", []):
            walk({k: v for k, v in item.items() if k != "id"}, f"model3d.{item['id']}")

    def _check_opening_walls(self) -> None:
        """An opening's `wall` should name an item in `walls` when the file lists walls.

        A warning, not an error: a sheet script draws the walls, and a file may
        list only some of them.
        """
        wall_ids = [w["id"] for w in self.data.get("walls", [])]
        if not wall_ids:
            return
        for op in self.data.get("openings", []):
            wall = op.get("wall")
            if wall is not None and wall not in wall_ids:
                self.issue("warning", "opening-wall-unknown", f"openings.{op['id']}",
                           f"wall {wall!r} is not an id in walls ({', '.join(wall_ids)}). "
                           "Name the wall item the opening sits in, or add that wall to walls")

    def _check_refs(self) -> None:
        def walk(node, where):
            if isinstance(node, str) and re.fullmatch(r"\$" + KEY, node):
                if node[1:] not in self.values:
                    self.issue("error", "unknown-ref", where, f"{node} is not a value key")
            elif isinstance(node, dict):
                for k, v in node.items():
                    walk(v, f"{where}.{k}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, f"{where}[{i}]")
        for kind in GEOMETRY_KINDS + ("chains",):
            walk(self.data.get(kind, []), kind)
        walk(self.data.get("structure", {}), "structure")   # struct.py block
        m3 = self.data.get("model3d") or {}
        walk(m3.get("elements", []), "model3d.elements")
        walk(m3.get("cameras", []), "model3d.cameras")

    def resolve_path(self, rel: str) -> str:
        """Absolute path of a file named in project.json. Raises ValueError if it
        leaves the project folder (after following links)."""
        root = os.path.realpath(self.dir)
        full = os.path.realpath(os.path.join(root, rel))
        if os.path.isabs(rel) or not inside_dir(full, root):
            raise ValueError(f"{rel!r} is outside the project folder {root}")
        return full

    def _check_paths(self) -> None:
        for s in self.sheets:
            for field in ("script", "attach"):
                if s.get(field):
                    try:
                        self.resolve_path(s[field])
                    except ValueError as exc:
                        self.issue("error", "path-outside-project", f"sheets.{s['id']}.{field}", str(exc))
            if not s.get("script") and not s.get("attach"):
                self.issue("error", "sheet-without-source", f"sheets.{s['id']}",
                           "needs a script or an attach path")
            if s.get("script") and s.get("attach"):
                self.issue("error", "sheet-two-sources", f"sheets.{s['id']}",
                           "give a script or an attach path, not both")

    # ---- connections (references/kit-elevations-sections.md, "Connections that carry a load")

    def _check_connections(self) -> None:
        """Ids are unique; a printed load names its code decision; a settled basis
        says what settles it."""
        seen = set()
        for c in self.data.get("connections", []):
            where = f"connections.{c['id']}"
            if c["id"] in seen:
                self.issue("error", "connection-duplicate", where, "connection id appears more than once")
            seen.add(c["id"])
            if c.get("load") and not c.get("cd"):
                self.issue("error", "connection-load-no-cd", where,
                           "a load prints on the sheet only with the logs/code-decisions.md entry it comes from (cd)")
            if c["basis"] != "open" and not c.get("evidence"):
                self.issue("error", "connection-no-evidence", where,
                           f"basis {c['basis']} needs evidence: the maker's report and rated load, or the "
                           "engineer and the calculation")

    # ---- images and finishes (references/images-and-finishes.md)

    def _check_images_finishes(self) -> None:
        """Image files exist inside the project folder; ids are unique; a finish has
        a color unless it is TBD; a finish's image is an images entry."""
        images = {}
        for im in self.data.get("images", []):
            where = f"images.{im['id']}"
            if im["id"] in images:
                self.issue("error", "image-duplicate", where, "image id appears more than once")
            images[im["id"]] = im
            try:
                full = self.resolve_path(im["path"])
            except ValueError as exc:
                self.issue("error", "path-outside-project", where, str(exc))
                continue
            if not os.path.isfile(full):
                self.issue("error", "image-missing", where, f"no file at {im['path']!r}")
            if im.get("source_id") and im["source_id"] not in self.sources:
                self.issue("error", "unknown-source", where, f"source_id {im['source_id']!r} is not in sources")
            if im["kind"] != "aerial" and ("north_deg" in im or "site_px" in im):
                self.issue("warning", "image-not-aerial", where,
                           "north_deg and site_px are read only for an aerial image")
        seen = set()
        for f in self.data.get("finishes", []):
            where = f"finishes.{f['id']}"
            if f["id"] in seen:
                self.issue("error", "finish-duplicate", where, "finish id appears more than once")
            seen.add(f["id"])
            if f["status"] != "TBD" and not f.get("rgb"):
                self.issue("error", "finish-no-color", where,
                           "a SELECTED or PROPOSED finish needs rgb; use status TBD until the owner picks one")
            if f.get("image") and f["image"] not in images:
                self.issue("error", "finish-unknown-image", where, f"image {f['image']!r} is not in images")
            elif f.get("image") and images[f["image"]]["kind"] not in ("product", "photo"):
                self.issue("error", "finish-image-kind", where,
                           "a finish shows a product or photo image, never a concept rendering or an aerial")

    def _check_rules(self) -> None:
        """Each rule names a value (or, for `check.spread`, values) that exists, in a
        unit the kit can convert to.

        A rule whose value is missing is a warning here and in QA (the value may
        not be drawn yet). A unit the kit does not know, a unit of another kind
        than the value (a length limit on an area), a point value or a duplicate
        id is an error: the check could never run.
        """
        seen: set = set()
        for r in self.data.get("rules", []):
            where = f"rules.{r['id']}"
            if r["id"] in seen:
                self.issue("error", "rule-duplicate", where, "rule id appears more than once")
            seen.add(r["id"])
            chk = r["check"]
            if not math.isfinite(float(chk["limit"])):
                self.issue("error", "rule-limit", where, f"limit {chk['limit']!r} is not a finite number")
            try:
                dim_limit = unit_info(chk["unit"])[0]
            except UnitError as exc:
                self.issue("error", "rule-unit-unknown", where, str(exc))
                continue
            for ref in rule_refs(chk):
                self._check_rule_ref(where, ref, chk["unit"], dim_limit)

    def _check_rule_ref(self, where: str, ref: str, unit: str, dim_limit: str) -> None:
        """One value a rule checks: it exists, is a number and is the limit's kind."""
        try:
            val = self.lookup(ref)
        except KeyError:
            self.issue("warning", "rule-value-unknown", where,
                       f"{ref} is not a value key; QA warns until the value exists")
            return
        if isinstance(val.v, (list, tuple)):
            self.issue("error", "rule-value-point", where, f"{ref} is a point, not a number")
            return
        try:
            dim_value = unit_info(val.unit)[0]
        except UnitError as exc:
            self.issue("error", "rule-unit-unknown", where, str(exc))
            return
        if dim_value != dim_limit:
            self.issue("error", "rule-unit-mismatch", where,
                       f"{ref} is in {val.unit} ({dim_value}) but the limit is in "
                       f"{unit} ({dim_limit}); point the rule at a value of the same kind")

    # ---- model3d (3D views, render3d.py)

    def _check_model3d(self) -> None:
        if not self.data.get("model3d"):
            return
        from .render3d import model3d_issues
        for sev, code, where, msg in model3d_issues(self):
            self.issue(sev, code, where, msg)

    def chain_report(self) -> list[dict]:
        """Closure of every dimension chain: segment sum against the stated total."""
        out = []
        for ch in self.data.get("chains", []):
            try:
                segs = [self.dim(s["len"]) for s in ch["segments"]]
                total = self.dim(ch["total"])
            except (KeyError, TypeError) as exc:
                out.append({"id": ch["id"], "ok": False, "error": str(exc)})
                continue
            s = sum(float(x) for x in segs)
            tol = float(ch.get("tol", 1.0 / self.denom))
            diff = s - float(total)
            out.append({"id": ch["id"], "sum": s, "total": float(total), "diff": diff,
                        "tol": tol, "ok": abs(diff) <= tol + 1e-9,
                        "segments": [x.key for x in segs], "total_key": total.key})
        return out

    def _check_chains(self) -> None:
        for r in self.chain_report():
            if not r["ok"]:
                msg = r.get("error") or (
                    f"segments sum to {_plain(r['sum'])} in. but the total is {_plain(r['total'])} in. "
                    f"(off by {_plain(r['diff'])} in.). Ask about the reading, or put the closure "
                    "error in a wall segment, never in an opening")
                self.issue("error", "chain-not-closed", r["id"], msg)


def _validate(data) -> list[str]:
    """Schema errors, plus every inline Value in geometry checked against the
    Value definition (the geometry item schemas are open, so the schema alone
    would accept "status": "assumed")."""
    schema = _schema.load_schema()
    errs = _schema.validate(data, schema)
    if errs or not isinstance(data, dict):
        return errs
    value_schema = {"$ref": "#/$defs/Value"}

    def walk(node, where):
        if isinstance(node, dict):
            if any(k in node for k in ("status", "v", "expr")):
                errs.extend(_schema.validate_against(node, value_schema, schema, where))
                return
            for k, v in node.items():
                walk(v, f"{where}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{where}[{i}]")
    for kind in GEOMETRY_KINDS:
        for i, item in enumerate(data.get(kind, [])):
            for k, v in item.items():
                walk(v, f"$.{kind}[{i}].{k}")
    for i, item in enumerate((data.get("model3d") or {}).get("elements", [])):
        for k, v in item.items():
            if k not in ("assumed",):
                walk(v, f"$.model3d.elements[{i}].{k}")
    return errs


def model3d_inline(data) -> list:
    """Inline Values in model3d elements, keyed model3d.<element>.<field>; an opening's
    field is model3d.<element>.<opening>.<field>."""
    out = []
    for item in (data.get("model3d") or {}).get("elements", []):
        for field, val in item.items():
            if isinstance(val, dict) and "status" in val:
                out.append((f"model3d.{item['id']}.{field}", val))
        for op in item.get("openings", []) or []:
            oid = op.get("ref") or op.get("id")
            for field, val in op.items():
                if isinstance(val, dict) and "status" in val:
                    out.append((f"model3d.{item['id']}.{oid}.{field}", val))
    return out


def rule_refs(check: dict) -> list[str]:
    """The value references a rule check reads: its `value`, or every entry of `spread`."""
    return [check["value"]] if "value" in check else list(check["spread"])


def _calls(node) -> set:
    """Function names an expression tree calls."""
    k = node[0]
    if k == "call":
        return {node[1]}.union(*(_calls(a) for a in node[2]))
    if k == "bin":
        return _calls(node[2]) | _calls(node[3])
    if k in ("neg", "paren"):
        return _calls(node[1])
    return set()


def range_text(lo: str, hi: str) -> str:
    """How a range prints: 9/16" TO 5/8", or one number when both ends print alike."""
    return lo if lo == hi else f"{lo} TO {hi}"


def _range_problem(r: dict) -> str | None:
    """Why a raw value's `range` is invalid, or None."""
    if not isinstance(r.get("v"), (int, float)):
        return "a range goes with a number v (the value drawn), not with an expr or a point"
    if r["status"] != "ASSUMED":
        return (f"only an ASSUMED value has a range of estimates; a {r['status']} value is one number. "
                "Mark it ASSUMED with an fv tag until it is measured")
    lo, hi = float(r["range"][0]), float(r["range"][1])
    if not (math.isfinite(lo) and math.isfinite(hi)):
        return f"range {r['range']} has a number that is not finite"
    if not lo < hi:
        return f"range {r['range']} must run low to high"
    if not lo <= float(r["v"]) <= hi:
        return f"v {r['v']} is outside its range {r['range']}; draw a number within the estimates"
    return None


def _plain(x: float) -> str:
    return f"{x:.4f}".rstrip("0").rstrip(".")
