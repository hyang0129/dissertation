"""v2/lint.py

Lint rule: every digit in prose must be inside an approved citation macro,
or covered by the whitelist.

Approved contexts (digits inside these are allowed):
  result, resdelta, resratio, resultCI, resultPM macros
  ref, cite, citep, citet, eqref, label arguments

Math mode ($ $, display math, equation/align environments) is stripped before
scanning -- digits in math are allowed unconditionally.

Year literals matching the pattern (19|20)XX are allowed everywhere.

Whitelist entries are literal strings (not regexes). A digit is OK if the
surrounding text contains a whitelist string that overlaps the digit position.

Usage:
    python lint.py [--paper-dir <path>]   # run from the v2/ directory

Exit code 0 = clean. Non-zero = violations found.

Ported from the onlycodes paper lint; whitelist slimmed for dissertation prose.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Approved macro patterns — digits inside these are safe.
# ---------------------------------------------------------------------------
_CITATION_MACROS = r"(?:result|resdelta|resratio|resultCI|resultPM|respct|respp|resp|ref|cref|Cref|autoref|cite|citep|citet|citealp|citealt|citeauthor|citeyear|citenum|eqref|label)"

_APPROVED_RE = re.compile(
    r"\\"
    + _CITATION_MACROS
    + r"(?:\{[^}]*\}){1,3}"
    + r"(?:\[[^\]]*\])?"
)

# ---------------------------------------------------------------------------
# LaTeX structural commands — not prose, digits inside are ignored.
# ---------------------------------------------------------------------------
_STRUCTURAL_CMDS = r"(?:documentclass|usepackage|geometry|input|include|inputenc|fontenc|bibliographystyle|bibliography|includegraphics|setlength|setcounter|vspace|hspace|textwidth|columnwidth|linewidth|acmConference|acmYear|copyrightyear|acmISBN|acmDOI|settopmatter)"

_STRUCTURAL_RE = re.compile(
    r"\\"
    + _STRUCTURAL_CMDS
    + r"(?:\[[^\]]*\])?"
    + r"(?:\{[^}]*\}){1,2}"
)

# ---------------------------------------------------------------------------
# Math mode patterns — stripped before digit scanning.
# ---------------------------------------------------------------------------
_INLINE_MATH_RE = re.compile(r"\$[^$]*\$")
_DISPLAY_MATH_RE = re.compile(r"\\\[.*?\\\]", re.DOTALL)
_ENV_MATH_RE = re.compile(
    r"\\begin\{(?:equation|equation\*|align|align\*|gather|gather\*|multline|multline\*)\}.*?\\end\{(?:equation|equation\*|align|align\*|gather|gather\*|multline|multline\*)\}",
    re.DOTALL,
)
# TikZ pictures hold coordinates and dimensions (e.g. at (5,0), text width=3.3cm),
# never result numbers — strip the whole environment before digit scanning, the
# same way math environments are stripped. Spans multiple lines, so masked at the
# block level in lint_file alongside block math.
_ENV_TIKZ_RE = re.compile(
    r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
    re.DOTALL,
)

# ---------------------------------------------------------------------------
# Year pattern — allowed everywhere.
# ---------------------------------------------------------------------------
_YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")

# ---------------------------------------------------------------------------
# Digit detector
# ---------------------------------------------------------------------------
_DIGIT_RE = re.compile(r"\d")

# ---------------------------------------------------------------------------
# Whitelist — literal strings; a digit is OK if its context contains one.
# To add an entry, append a string here and document it in README.md.
# ---------------------------------------------------------------------------
WHITELIST: list[str] = [
    # --- Enumerated contributions / objectives in intro & conclusion ---
    "(1) ",
    "(2) ",
    "(3) ",
    "(4) ",
    "(5) ",
    "Objective 1",
    "Objective 2",
    "Objective 3",
    "Chapter 1",
    "Chapter 2",
    "Chapter 3",
    "Chapter 4",
    "Chapter 5",
    "Chapter 6",
    "Chapter 7",
    "Chapter 8",
    # --- Cross-reference macros (defensive; also covered by _CITATION_MACROS) ---
    "Figure~\\ref",
    "Table~\\ref",
    "Section~\\ref",
    "Chapter~\\ref",
    "Appendix~\\ref",
    "Theorem~\\ref",
    "Lemma~\\ref",
    "Equation~\\ref",
    "\\S\\ref",
    # --- Statistical phrases ---
    "95\\% CI",
    "95\\%",
    "p < 0",
    "p > 0",
    # --- LaTeX table syntax — \multicolumn{N}{...}, \cmidrule(lr){A-B} ---
    "\\multicolumn{",
    "\\cmidrule",
    "\\multirow",
    # --- Footnote markers ---
    "\\footnote{",
    # --- Repository / version structure paths sometimes appearing inline ---
    "v1",
    "v2",
    # --- Dataset / architecture / metric proper nouns (digit is part of a
    #     name, not a quantity; recur across results chapters). Added for Ch.4. ---
    "CIFAR10",      # also covers CIFAR100 (substring) within the ±60 context
    "CIFAR100",
    "CIFAR-10",     # hyphenated form; also covers CIFAR-10/100 and CIFAR-100
    "ResNet50",
    "ResNet-50",
    "CC3M",
    "Food 101",
    "Food-101",     # Ch.5: dataset proper noun ("Food-101, 101 categories")
    "BMW M3",
    "FPR95",        # metric label in tables/captions
    "FPR@95",
    # --- Ch.5 (DSC/TGT) proper nouns, metrics, and prediction labels ---
    "Sentinel-2",       # EuroSAT sensor proper noun
    "precision-at-95",  # deferred-metric name (pr@95)
    "P1",               # DSC prediction labels (description list + prose refs)
    "P2",
    "P3",
    # --- Ch.6 (MI hallucination) enumerated-claim labels ---
    "Claim",            # "Claim 1/2/3", "Claim~2", "Claims~1--3" in §6.3 argument
    "Variant",          # "Variant 4" ablation labels (§6.7)
    # --- Ch.6 LLM model proper nouns (digit is part of the name) ---
    "Llama-3.1-8B-Instruct",
    "Qwen3-8B",
    # NOTE: This whitelist intentionally starts small. Add a literal string
    # here (and document it in README.md) when a legitimate digit in prose
    # cannot be expressed via a \result{}/\cite{}/\ref{} macro.
]


def _mask_spans(text: str, spans: list[tuple[int, int]]) -> str:
    text_list = list(text)
    for start, end in spans:
        for i in range(start, end):
            # Preserve newlines so callers can mask multi-line spans (e.g. a
            # display-math block) without collapsing line numbering.
            if i < len(text_list) and text_list[i] != "\n":
                text_list[i] = " "
    return "".join(text_list)


def strip_math_and_approved(text: str) -> tuple[str, list[tuple[int, int]]]:
    masked_spans: list[tuple[int, int]] = []

    for m in _ENV_MATH_RE.finditer(text):
        masked_spans.append((m.start(), m.end()))
    for m in _DISPLAY_MATH_RE.finditer(text):
        masked_spans.append((m.start(), m.end()))
    for m in _INLINE_MATH_RE.finditer(text):
        masked_spans.append((m.start(), m.end()))
    for m in _APPROVED_RE.finditer(text):
        masked_spans.append((m.start(), m.end()))
    for m in _STRUCTURAL_RE.finditer(text):
        masked_spans.append((m.start(), m.end()))

    stripped = _mask_spans(text, masked_spans)
    return stripped, masked_spans


def _context_window(text: str, pos: int, width: int = 40) -> str:
    start = max(0, pos - width)
    end = min(len(text), pos + width + 1)
    return text[start:end].replace("\n", " ")


def lint_file(path: Path) -> list[str]:
    text = path.read_text(errors="replace")
    violations: list[str] = []

    text_no_comments = re.sub(r"(?<!\\)%.*", "", text)

    # Block-level math (equation/align/gather/multline and display \[ \]) may
    # span multiple lines, so mask it across the FULL text before splitting
    # into lines. The per-line strip below only catches single-line $...$.
    # _mask_spans preserves newlines, so line numbering stays aligned.
    block_spans: list[tuple[int, int]] = []
    for m in _ENV_MATH_RE.finditer(text_no_comments):
        block_spans.append((m.start(), m.end()))
    for m in _DISPLAY_MATH_RE.finditer(text_no_comments):
        block_spans.append((m.start(), m.end()))
    for m in _ENV_TIKZ_RE.finditer(text_no_comments):
        block_spans.append((m.start(), m.end()))
    text_no_comments = _mask_spans(text_no_comments, block_spans)

    lines_original = text_no_comments.splitlines()

    for lineno, line in enumerate(lines_original, 1):
        stripped, _ = strip_math_and_approved(line)

        for digit_match in _DIGIT_RE.finditer(stripped):
            pos = digit_match.start()

            if _YEAR_RE.search(line[max(0, pos - 4) : pos + 4]):
                continue

            context_start = max(0, pos - 60)
            context_end = min(len(line), pos + 60)
            context = line[context_start:context_end]
            # \allowbreak is a pure line-break hint with no semantic content;
            # drop it so it can't split a whitelisted token (e.g. an instance
            # ID) and defeat the substring match below.
            context = context.replace("\\allowbreak", "")
            if any(entry in context for entry in WHITELIST):
                continue

            snippet = _context_window(stripped, pos, width=30)
            violations.append(
                f"{path}:{lineno}: bare digit '{digit_match.group()}' "
                f"outside approved context — «{snippet.strip()}»"
            )

    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint .tex prose for bare digits")
    parser.add_argument(
        "--paper-dir",
        default=".",
        help="Path to the v2/ directory (default: current dir)",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        help="Specific .tex files to lint (overrides default scan)",
    )
    args = parser.parse_args(argv)

    paper_dir = Path(args.paper_dir)

    if args.files:
        tex_files = [Path(f) for f in args.files]
    else:
        tex_files = []
        main_tex = paper_dir / "main.tex"
        if main_tex.exists():
            tex_files.append(main_tex)
        for sub in ("chapters", "appendices"):
            sub_dir = paper_dir / sub
            if sub_dir.exists():
                tex_files.extend(sorted(sub_dir.glob("*.tex")))

    if not tex_files:
        print(f"No .tex files found under {paper_dir}", file=sys.stderr)
        return 0

    all_violations: list[str] = []
    for tex_path in tex_files:
        violations = lint_file(tex_path)
        all_violations.extend(violations)

    if all_violations:
        for v in all_violations:
            print(v, file=sys.stderr)
        print(
            f"\nlint: {len(all_violations)} violation(s) found. "
            "Add to WHITELIST in lint.py or use \\result{...} macros.",
            file=sys.stderr,
        )
        return 1

    print(f"lint: OK — {len(tex_files)} file(s) scanned, no bare digits found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
