"""v2/voice_meter.py — the VOICE METER (prose-texture gate).

Companion to lint.py (the number gate). Where lint.py polices *content*
(every digit must resolve through a \\result/\\cite/\\ref macro), this tool
polices *texture* — the structural signature that separates the human-written
exemplar (Chapter 4, the ported ICLR paper) from machine-smoothed prose.

The machine register is not a set of banned phrases; it is LOW VARIANCE
(register leveling). So this meter measures the variance and the repetition,
not a wordlist:

  * burstiness        — sentence-length spread (SD and coefficient of variation),
                        plus presence of very short (<8w) and very long (>35w)
                        sentences. Human prose spikes; machine prose stays flat.
  * tricolons         — "A, B, and C" noun lists + runs of parallel \\paragraph
                        openers. Rule-of-three scaffolding is the dominant tell.
  * cross-chapter     — 6+ -grams that recur across the framing files. Catches
    repetition          a thesis sentence recited verbatim in abstract+intro+
                        conclusion, reused appositives, and reused example-triples.
  * closers           — last sentence of each section: short + balanced-clause
                        aphorism heuristic (warning only; human confirms).

WORKFLOW (regenerate, don't patch): the meter is the gate for the rewrite loop
documented in outlines/style_guide.md §6. Build the Ch.4 profile once, then
regenerate each framing section from bare claims conditioned on Ch.4 spans and
reject any section that fails the burstiness / tricolon / n-gram thresholds
*before* a human reads it. Voice (local stake, idiosyncrasy) stays human.

Usage:
    python voice_meter.py --profile chapters/04_label_blindness.tex
        # write the exemplar target to data/voice_profile_ch4.json

    python voice_meter.py
        # report framing files vs the profile (warning only, exit 0)

    python voice_meter.py --gate
        # same, but exit nonzero on a gateable failure (burstiness / tricolon
        # cap / cross-chapter n-gram). For wiring into `make paper` once the
        # framing chapters pass.

    python voice_meter.py --files chapters/07_conclusion.tex
        # restrict to specific files

Stdlib only (the repo runs no venv), mirroring lint.py.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Which files are the exemplar vs the prose under test.
# ---------------------------------------------------------------------------
DEFAULT_EXEMPLAR = "chapters/04_label_blindness.tex"
DEFAULT_FRAMING = [
    "frontmatter/Abstract.tex",
    "chapters/01_introduction.tex",
    "chapters/02_background.tex",
    "chapters/03_literature_review.tex",
    "chapters/07_conclusion.tex",
]
PROFILE_PATH = "data/voice_profile_ch4.json"

# ---------------------------------------------------------------------------
# Gate thresholds. Tuned against the Ch.4 profile at build time; a section that
# falls below the burstiness floor or above the tricolon/parallel caps reads as
# machine-leveled. Cross-chapter n-grams are an absolute repetition gate.
# ---------------------------------------------------------------------------
# Burstiness floor is expressed as a fraction of the Ch.4 exemplar's coefficient
# of variation (SD/mean), so it tracks the target rather than a magic constant.
BURSTINESS_CV_FRACTION = 0.85          # require CV >= 0.85 * exemplar CV
MIN_LONG_SENTENCE_WORDS = 35           # at least one sentence this long ...
MAX_SHORT_SENTENCE_WORDS = 8           # ... and at least one this short
TRICOLON_CAP_PER_1K = 2.5              # "A, B, and C" lists per 1k words
PARALLEL_PARAGRAPH_RUN_CAP = 2         # consecutive \paragraph w/ same opener
NGRAM_N = 6                            # cross-chapter repetition window
MIN_WORDS_FOR_STATS = 60              # skip tiny fragments

# Cross-chapter phrases that recur BY DESIGN and must not be flagged. Normalized
# (lowercased, punctuation-stripped) so they match the n-gram form. A 6-gram is
# exempted when it is a substring of any entry here.
#   1. the thesis bookend (style_guide.md §2.3 exception);
#   2. the Ch.6 parity verb, which the framing locks fix verbatim
#      ("matches-or-outperforms, in the mean" / "strongest engineered probe",
#      never "beats"/"SOTA") — see 00_dissertation_outline.md.
SANCTIONED_BOOKENDS = [
    "when the representation keeps it a detector can read it out",
    "matches-or-outperforms in the mean the strongest engineered probe",
]

# ---------------------------------------------------------------------------
# Prose extraction. The same extractor runs on every file, so any systematic
# stripping artifact cancels when comparing a file to the Ch.4 profile.
# ---------------------------------------------------------------------------
_COMMENT_RE = re.compile(r"(?<!\\)%.*")

# Whole environments that are not running prose (their bodies are data, math,
# or captions) — removed entirely.
_NONPROSE_ENVS = (
    "equation", "align", "gather", "multline", "eqnarray", "alignat",
    "tikzpicture", "tabular", "table", "figure", "algorithm", "algorithmic",
    "lstlisting", "verbatim", "wrapfigure", "subfigure",
)
_NONPROSE_ENV_RE = re.compile(
    r"\\begin\{(" + "|".join(_NONPROSE_ENVS) + r")\*?\}.*?\\end\{\1\*?\}",
    re.DOTALL,
)

_INLINE_MATH_RE = re.compile(r"\$[^$]*\$")
_DISPLAY_MATH_RE = re.compile(r"\\\[.*?\\\]", re.DOTALL)

# Section-structure commands: used as segment delimiters, text dropped.
_HEADING_RE = re.compile(
    r"\\(chapter|section|subsection|subsubsection)\*?\{[^}]*\}"
)
# \paragraph{Title.} — a lead-in we track for parallel-opener runs.
_PARAGRAPH_LEADIN_RE = re.compile(r"\\paragraph\*?\{([^}]*)\}")

# Citation / ref / label macros — parenthetical noise, dropped (with a leading
# ~ or space). \Cref/\ref act as a noun ("Chapter 4"), replaced by a token.
_REF_TOKEN_RE = re.compile(r"\\(?:[Cc]ref|autoref|ref|eqref)\{[^}]*\}")
_CITE_RE = re.compile(r"~?\\(?:cite[a-z]*|citep|citet|citealp|citealt)\{[^}]*\}")
_LABEL_RE = re.compile(r"\\label\{[^}]*\}")
# \result-family numeric macros -> a number placeholder.
_RESULT_RE = re.compile(
    r"\\(?:result|resdelta|resratio|resultCI|resultPM|respct|respp|resp)"
    r"\{[^}]*\}(?:\{[^}]*\})?(?:\[[^\]]*\])?"
)
# Font/emphasis wrappers -> keep inner content.
_UNWRAP_RE = re.compile(
    r"\\(?:emph|textbf|textit|texttt|textsc|underline|text)\{([^{}]*)\}"
)
# List item markers, spacing, and leftover backslash commands.
_ITEM_RE = re.compile(r"\\item\b")
_GENERIC_CMD_RE = re.compile(r"\\[a-zA-Z]+\*?")

_ABBREV = {
    "e.g", "i.e", "etc", "cf", "vs", "al", "fig", "eq", "no", "st",
    "mr", "ms", "dr", "ch", "sec", "approx", "resp",
}


def _strip_to_prose(text: str) -> str:
    text = _COMMENT_RE.sub("", text)
    text = _NONPROSE_ENV_RE.sub(" ", text)
    text = _DISPLAY_MATH_RE.sub(" ", text)
    text = _INLINE_MATH_RE.sub(" MATHX ", text)
    text = _RESULT_RE.sub(" NUM ", text)
    text = _REF_TOKEN_RE.sub(" REF ", text)
    text = _CITE_RE.sub("", text)
    text = _LABEL_RE.sub("", text)
    text = _PARAGRAPH_LEADIN_RE.sub(" ", text)   # title dropped; tracked separately
    text = _HEADING_RE.sub(" ", text)
    # Unwrap emphasis wrappers repeatedly (handles light nesting).
    for _ in range(3):
        text, n = _UNWRAP_RE.subn(r"\1", text)
        if not n:
            break
    text = _ITEM_RE.sub(" ", text)
    text = _GENERIC_CMD_RE.sub(" ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    text = text.replace("``", '"').replace("''", '"')
    text = re.sub(r"[ \t]+", " ", text)
    return text


def _split_sentences(prose: str) -> list[str]:
    # Collapse newlines to spaces but keep paragraph breaks as sentence ends.
    prose = re.sub(r"\n\s*\n", " . ", prose)
    prose = prose.replace("\n", " ")
    pieces = re.split(r"(?<=[.!?])\s+(?=[\"A-Z(])", prose)
    sentences: list[str] = []
    buf = ""
    for piece in pieces:
        cand = (buf + " " + piece).strip() if buf else piece.strip()
        # Re-join if the split landed right after a known abbreviation.
        last_word = re.findall(r"([A-Za-z.]+)\.$", cand)
        tail = cand.rstrip(".").split()[-1].lower() if cand.rstrip(".").split() else ""
        if tail in _ABBREV:
            buf = cand
            continue
        if cand:
            sentences.append(cand)
        buf = ""
    if buf:
        sentences.append(buf)
    # Keep only sentences with real word content.
    return [s for s in sentences if len(_words(s)) >= 1]


def _words(s: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z'\-]*", s)


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def _sd(xs: list[float]) -> float:
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


# ---------------------------------------------------------------------------
# Metric computation.
# ---------------------------------------------------------------------------
# Tricolon: "x, y, and z" / "x, y, or z" — three+ comma-separated items closing
# with a conjunction. Approximate, but consistent across files.
_TRICOLON_RE = re.compile(
    r"\b[\w\-]+(?:\s+[\w\-]+){0,3},\s+[\w\-]+(?:\s+[\w\-]+){0,3},"
    r"\s+(?:and|or)\s+[\w\-]+(?:\s+[\w\-]+){0,3}"
)


def _first_content_word(title: str) -> str:
    ws = _words(title)
    return ws[0].lower() if ws else ""


def measure(path: Path) -> dict:
    raw = path.read_text(errors="replace")
    prose = _strip_to_prose(raw)
    sentences = _split_sentences(prose)
    lengths = [len(_words(s)) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    total_words = sum(lengths)

    mean = _mean([float(n) for n in lengths])
    sd = _sd([float(n) for n in lengths])
    cv = sd / mean if mean else 0.0

    tricolons = len(_TRICOLON_RE.findall(prose))

    # Parallel \paragraph openers: longest run of consecutive \paragraph{...}
    # whose first content word repeats.
    titles = _PARAGRAPH_LEADIN_RE.findall(_COMMENT_RE.sub("", raw))
    openers = [_first_content_word(t) for t in titles]
    max_run = 1 if openers else 0
    run = 1
    for i in range(1, len(openers)):
        if openers[i] and openers[i] == openers[i - 1]:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 1

    return {
        "file": str(path),
        "n_sentences": len(lengths),
        "total_words": total_words,
        "mean_len": round(mean, 2),
        "sd_len": round(sd, 2),
        "cv": round(cv, 3),
        "min_len": min(lengths) if lengths else 0,
        "max_len": max(lengths) if lengths else 0,
        "n_short": sum(1 for n in lengths if n <= MAX_SHORT_SENTENCE_WORDS),
        "n_long": sum(1 for n in lengths if n >= MIN_LONG_SENTENCE_WORDS),
        "tricolons": tricolons,
        "tricolons_per_1k": round(1000 * tricolons / total_words, 2) if total_words else 0.0,
        "max_parallel_paragraph_run": max_run,
        "_sentences": sentences,  # retained for closer analysis; popped before JSON
    }


# ---------------------------------------------------------------------------
# Cross-chapter n-gram repetition.
# ---------------------------------------------------------------------------
def _normalized_tokens(path: Path) -> list[str]:
    prose = _strip_to_prose(path.read_text(errors="replace"))
    return [w.lower() for w in _words(prose)]


def _ngrams(tokens: list[str], n: int) -> set[str]:
    return {" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def _stitch(grams: set[tuple[str, ...]], n: int) -> list[tuple[str, ...]]:
    """Merge overlapping n-grams (sharing n-1 words) into maximal phrases, so a
    recited sentence shows up as one phrase instead of many shifted windows."""
    phrases = set(grams)
    k = n - 1
    merged = True
    while merged:
        merged = False
        for a in list(phrases):
            for b in list(phrases):
                if a == b:
                    continue
                if a[-k:] == b[:k]:
                    new = a + b[k:]
                    phrases.discard(a)
                    phrases.discard(b)
                    phrases.add(new)
                    merged = True
                    break
            if merged:
                break
    # Drop any phrase that is contained in a longer kept one.
    ordered = sorted(phrases, key=len, reverse=True)
    kept: list[tuple[str, ...]] = []
    for p in ordered:
        ps = " ".join(p)
        if not any(ps in " ".join(q) for q in kept):
            kept.append(p)
    return kept


def cross_chapter_repeats(paths: list[Path], n: int = NGRAM_N) -> list[tuple[str, list[str]]]:
    per_file: dict[str, set[str]] = {}
    for p in paths:
        per_file[str(p)] = _ngrams(_normalized_tokens(p), n)
    gram_to_files: dict[tuple[str, ...], frozenset[str]] = {}
    tmp: dict[str, set[str]] = {}
    for fname, grams in per_file.items():
        for g in grams:
            tmp.setdefault(g, set()).add(fname)
    # Group recurring grams by the exact set of files they appear in, then stitch
    # each group's windows into maximal phrases.
    by_fileset: dict[frozenset[str], set[tuple[str, ...]]] = {}
    for g, files in tmp.items():
        if len(files) >= 2 and not any(b in g or g in b for b in SANCTIONED_BOOKENDS):
            by_fileset.setdefault(frozenset(files), set()).add(tuple(g.split()))
    repeats: list[tuple[str, list[str]]] = []
    for fileset, grams in by_fileset.items():
        for phrase in _stitch(grams, n):
            repeats.append((" ".join(phrase), sorted(fileset)))
    repeats.sort(key=lambda gf: (-len(gf[1]), -len(gf[0].split())))
    return repeats


# ---------------------------------------------------------------------------
# Aphoristic-closer heuristic (warning only).
# ---------------------------------------------------------------------------
def aphoristic_closers(sentences: list[str]) -> list[str]:
    flagged = []
    for s in sentences[-1:] if sentences else []:
        ws = _words(s)
        # short + has a mid-sentence comma + no concrete REF/NUM token = likely flourish
        if 5 <= len(ws) <= 22 and "," in s and "REF" not in s and "NUM" not in s:
            flagged.append(s.strip())
    return flagged


# ---------------------------------------------------------------------------
# Profile + report.
# ---------------------------------------------------------------------------
def build_profile(exemplar: Path) -> dict:
    m = measure(exemplar)
    m.pop("_sentences", None)
    return {
        "exemplar": str(exemplar),
        "mean_len": m["mean_len"],
        "sd_len": m["sd_len"],
        "cv": m["cv"],
        "min_len": m["min_len"],
        "max_len": m["max_len"],
        "tricolons_per_1k": m["tricolons_per_1k"],
        "note": "Target texture from the human-written Ch.4 exemplar. "
                "Burstiness floor = BURSTINESS_CV_FRACTION * cv.",
    }


def _load_or_build_profile(paper_dir: Path) -> dict:
    pp = paper_dir / PROFILE_PATH
    if pp.exists():
        return json.loads(pp.read_text())
    return build_profile(paper_dir / DEFAULT_EXEMPLAR)


def report(paper_dir: Path, files: list[Path], gate: bool) -> int:
    profile = _load_or_build_profile(paper_dir)
    cv_floor = round(BURSTINESS_CV_FRACTION * profile["cv"], 3)

    print(f"voice_meter: exemplar={profile['exemplar']}  "
          f"target cv={profile['cv']} (floor {cv_floor}), "
          f"mean_len={profile['mean_len']}, sd_len={profile['sd_len']}, "
          f"tricolons/1k={profile['tricolons_per_1k']}")
    print("-" * 78)

    failures: list[str] = []
    measured = [measure(p) for p in files]

    for m in measured:
        sentences = m.pop("_sentences", [])
        if m["total_words"] < MIN_WORDS_FOR_STATS:
            print(f"{m['file']}: (skipped — {m['total_words']} words)")
            continue
        flags = []
        if m["cv"] < cv_floor:
            flags.append(f"FLAT cv={m['cv']}<{cv_floor}")
        if m["n_long"] == 0:
            flags.append("no long sentence(>=35w)")
        if m["n_short"] == 0:
            flags.append("no short sentence(<=8w)")
        if m["tricolons_per_1k"] > TRICOLON_CAP_PER_1K:
            flags.append(f"TRICOLONS {m['tricolons_per_1k']}/1k>{TRICOLON_CAP_PER_1K}")
        if m["max_parallel_paragraph_run"] > PARALLEL_PARAGRAPH_RUN_CAP:
            flags.append(f"PARALLEL paragraphs run={m['max_parallel_paragraph_run']}")

        status = "  ".join(flags) if flags else "ok"
        print(f"{m['file']}")
        print(f"    sentences={m['n_sentences']}  mean={m['mean_len']}  sd={m['sd_len']}  "
              f"cv={m['cv']}  range={m['min_len']}-{m['max_len']}  "
              f"short={m['n_short']} long={m['n_long']}  "
              f"tricolons={m['tricolons']}({m['tricolons_per_1k']}/1k)  "
              f"||para_run={m['max_parallel_paragraph_run']}")
        print(f"    -> {status}")

        # Gateable flags (burstiness + tricolon + parallel).
        gateable = [f for f in flags if f.split()[0] in
                    {"FLAT", "TRICOLONS", "PARALLEL"}]
        failures.extend(f"{m['file']}: {g}" for g in gateable)

    # Cross-chapter n-gram repetition (a repetition gate).
    print("-" * 78)
    repeats = cross_chapter_repeats(files, NGRAM_N)
    if repeats:
        print(f"cross-chapter {NGRAM_N}-grams recurring across files "
              f"(sanctioned bookend excluded):")
        for g, fs in repeats[:25]:
            short = [Path(f).name for f in fs]
            print(f"    «{g}»  in {short}")
            failures.append(f"cross-chapter repeat: «{g}» in {short}")
        if len(repeats) > 25:
            print(f"    ... and {len(repeats) - 25} more")
    else:
        print(f"cross-chapter {NGRAM_N}-grams: none recurring (good).")

    print("-" * 78)
    if failures:
        print(f"voice_meter: {len(failures)} gateable issue(s).")
        if gate:
            return 1
        print("(warning only — pass --gate to fail the build)")
        return 0
    print("voice_meter: OK — all measured files within texture thresholds.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Voice meter — prose-texture gate")
    ap.add_argument("--paper-dir", default=".", help="Path to v2/ (default: cwd)")
    ap.add_argument("--profile", metavar="TEXFILE",
                    help="Build the voice profile from this exemplar and write "
                         f"{PROFILE_PATH}")
    ap.add_argument("--files", nargs="*",
                    help="Specific .tex files to measure (default: framing set)")
    ap.add_argument("--gate", action="store_true",
                    help="Exit nonzero on a gateable failure")
    args = ap.parse_args(argv)
    paper_dir = Path(args.paper_dir)

    if args.profile:
        prof = build_profile(Path(args.profile))
        out = paper_dir / PROFILE_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(prof, indent=2) + "\n")
        print(f"voice_meter: wrote {out}")
        print(json.dumps(prof, indent=2))
        return 0

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = [paper_dir / f for f in DEFAULT_FRAMING]
    files = [f for f in files if f.exists()]
    if not files:
        print("voice_meter: no files to measure", file=sys.stderr)
        return 0

    return report(paper_dir, files, gate=args.gate)


if __name__ == "__main__":
    sys.exit(main())
