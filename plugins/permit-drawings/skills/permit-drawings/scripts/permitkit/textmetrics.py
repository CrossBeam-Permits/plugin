"""Helvetica and Helvetica-Bold advance widths, and WinAnsi text encoding.

The widths come from the standard Adobe AFM metrics for Helvetica and
Helvetica-Bold, including the WinAnsi characters that permit sheets use
(section sign, degree, dashes and so on).

The PDF writer uses the base-14 fonts Helvetica and Helvetica-Bold. They are
not embedded, so every viewer uses Helvetica metrics and these widths are exact.
"""
from __future__ import annotations

_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "<": 584, "=": 584, ">": 584,
    "?": 556, "@": 1015, "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556,
    "`": 333, "{": 334, "|": 260, "}": 334, "~": 584,
    "A": 667, "B": 667, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778,
    "H": 722, "I": 278, "J": 500, "K": 667, "L": 556, "M": 833, "N": 722,
    "O": 778, "P": 667, "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722,
    "V": 667, "W": 944, "X": 667, "Y": 667, "Z": 611,
    "a": 556, "b": 556, "c": 500, "d": 556, "e": 556, "f": 278, "g": 556,
    "h": 556, "i": 222, "j": 222, "k": 500, "l": 222, "m": 833, "n": 556,
    "o": 556, "p": 556, "q": 556, "r": 333, "s": 500, "t": 278, "u": 556,
    "v": 500, "w": 722, "x": 500, "y": 500, "z": 500,
    # WinAnsi additions (Helvetica AFM).
    "§": 556, "°": 400, "±": 584, "×": 584, "¼": 834,
    "½": 834, "¾": 834, "–": 556, "—": 1000, "‘": 222,
    "’": 222, "“": 333, "”": 333, "•": 350, "·": 278,
    "…": 1000, "²": 333, "³": 333, "®": 737, "©": 737,
}
_B = {
    " ": 278, "!": 333, '"': 474, "#": 556, "$": 556, "%": 889, "&": 722,
    "'": 238, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 333, ";": 333, "<": 584, "=": 584, ">": 584,
    "?": 611, "@": 975, "[": 333, "\\": 278, "]": 333, "^": 584, "_": 556,
    "`": 333, "{": 389, "|": 280, "}": 389, "~": 584,
    "A": 722, "B": 722, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778,
    "H": 722, "I": 278, "J": 556, "K": 722, "L": 611, "M": 833, "N": 722,
    "O": 778, "P": 667, "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722,
    "V": 667, "W": 944, "X": 667, "Y": 667, "Z": 611,
    "a": 556, "b": 611, "c": 556, "d": 611, "e": 556, "f": 333, "g": 611,
    "h": 611, "i": 278, "j": 278, "k": 556, "l": 278, "m": 889, "n": 611,
    "o": 611, "p": 611, "q": 611, "r": 389, "s": 556, "t": 333, "u": 611,
    "v": 556, "w": 778, "x": 556, "y": 556, "z": 500,
    "§": 556, "°": 400, "±": 584, "×": 584, "¼": 834,
    "½": 834, "¾": 834, "–": 556, "—": 1000, "‘": 278,
    "’": 278, "“": 500, "”": 500, "•": 350, "·": 278,
    "…": 1000, "²": 333, "³": 333, "®": 737, "©": 737,
}
for _d in (_W, _B):
    for _c in "0123456789":
        _d[_c] = 556

_FALLBACK = 556

# Characters Helvetica/WinAnsi cannot show. The kit swaps them for plain text.
# Anything else outside cp1252 raises, so no glyph is silently lost.
SUBSTITUTE = {
    "≤": "<=", "≥": ">=", "→": "->", "←": "<-", "≈": "~",
    "′": "'", "″": '"', "Δ": "DELTA ", "−": "-", " ": " ",
}

ASCENT = 0.718     # cap height of Helvetica, per em
DESCENT = 0.207    # descender depth, per em


def clean(text: str) -> str:
    """Apply SUBSTITUTE and confirm every character encodes in WinAnsi."""
    out = "".join(SUBSTITUTE.get(ch, ch) for ch in str(text))
    try:
        out.encode("cp1252")
    except UnicodeEncodeError as exc:
        bad = out[exc.start:exc.end]
        raise ValueError(f"character {bad!r} in {text!r} has no Helvetica glyph; "
                         "write it in plain text") from None
    return out


def text_width(s: str, size: float, bold: bool = False, tracking: float = 0.0) -> float:
    """Advance width of `s` in points at `size` points."""
    table = _B if bold else _W
    total = sum(table.get(ch, _FALLBACK) for ch in s)
    w = total * size / 1000.0
    if tracking and len(s) > 1:
        w += tracking * (len(s) - 1)
    return w


def wrap(text: str, max_width: float, size: float, bold: bool = False) -> list[str]:
    """Greedy wrap on measured width. A word longer than the line gets its own line."""
    words = str(text).split()
    lines: list[str] = []
    cur = ""
    for wd in words:
        trial = f"{cur} {wd}" if cur else wd
        if cur and text_width(trial, size, bold) > max_width:
            lines.append(cur)
            cur = wd
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines or [""]
