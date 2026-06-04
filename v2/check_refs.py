"""v2/check_refs.py — the citation half of the bib gate.

Companion to lint.py (the number half). Where lint.py stops fabricated *numbers*,
this stops fabricated / dangling *references*.

Offline checks (default; run by `make` — deterministic, no network):
  FAIL  undefined citation   — a \\cite key with no entry in references.bib
  FAIL  duplicate bibkey     — the same key defined twice
  FAIL  malformed/orphan body — a field line (title=/author=/...) living outside
                                any @entry (this is exactly the corruption that
                                hid a broken huang2021mos entry in the seed bib)
  WARN  no identifier        — an entry with no doi / arXiv id / url (can't be
                                machine-verified later; fine for books/datasets)
  WARN  uncited entry        — defined but never \\cite'd (dead weight)

Online check (opt-in: --online; needs network, for CI / pre-submission):
  FAIL  identifier mismatch  — an entry's arXiv id or DOI resolves to a paper
                              whose title does not match the bib title field.
                              This is the check that catches the two worst audit
                              findings (an arXiv id pointing at a *different*
                              paper). Skipped gracefully if the network is down.

Usage:
    python check_refs.py [--paper-dir <path>] [--online] [--strict-warn]

Exit 0 = clean. Non-zero = at least one FAIL (or any WARN under --strict-warn).
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

CITE_RE = re.compile(r"\\[Cc]ite[a-zA-Z]*(?:\[[^\]]*\])*\{([^}]*)\}")
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
FIELD_LINE_RE = re.compile(
    r"^\s*(title|author|booktitle|journal|year|pages|volume|number|publisher|"
    r"url|doi|eprint|note|editor|address|institution|howpublished)\s*=",
    re.IGNORECASE,
)
ARXIV_RE = re.compile(r"(?:arXiv:|abs/|/)?(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s}\"',]+")


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
def parse_entries(text: str) -> list[tuple[str, str, int, int]]:
    """Return [(entry_type, key, start, end)] with brace-matched bodies."""
    out = []
    for m in ENTRY_RE.finditer(text):
        start = m.start()
        brace = text.index("{", start)
        depth = 0
        for j in range(brace, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    out.append((m.group(1), m.group(2), start, j + 1))
                    break
    return out


def entry_field(body: str, field: str) -> str | None:
    m = re.search(field + r"\s*=\s*", body, re.IGNORECASE)
    if not m:
        return None
    i = m.end()
    if i < len(body) and body[i] in "{\"":
        close = "}" if body[i] == "{" else "\""
        depth = 0
        for j in range(i, len(body)):
            if body[j] == body[i] and body[i] == "{":
                depth += 1
            elif body[j] == close:
                depth -= 1
                if depth <= 0:
                    return body[i + 1 : j]
    # bare value up to comma/newline
    return body[i:].split(",")[0].split("\n")[0].strip()


def norm_title(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+", " ", s or "")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return " ".join(s.split())


# ---------------------------------------------------------------------------
# Online resolution
# ---------------------------------------------------------------------------
def _get(url: str, accept: str | None = None, timeout: int = 20) -> str | None:
    req = urllib.request.Request(url, headers={
        "User-Agent": "dissertation-check-refs/1.0 (mailto:hy3134@g.rit.edu)",
        **({"Accept": accept} if accept else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def arxiv_title(aid: str) -> str | None:
    body = _get(f"http://export.arxiv.org/api/query?id_list={aid}")
    if not body:
        return None
    m = re.search(r"<entry>.*?<title>(.*?)</title>", body, re.DOTALL)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def doi_title(doi: str) -> str | None:
    body = _get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    if not body:
        return None
    try:
        return (json.loads(body)["message"]["title"] or [None])[0]
    except (KeyError, ValueError, IndexError):
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Citation/reference integrity gate")
    ap.add_argument("--paper-dir", default=".")
    ap.add_argument("--online", action="store_true",
                    help="resolve arXiv/DOI identifiers and check titles match (needs network)")
    ap.add_argument("--show-uncited", action="store_true",
                    help="list entries never \\cite'd (expected while drafting; summarized by default)")
    ap.add_argument("--show-no-id", action="store_true",
                    help="list entries lacking a machine-verifiable identifier (summarized by default)")
    ap.add_argument("--strict-warn", action="store_true",
                    help="treat advisories as failures too")
    args = ap.parse_args(argv)
    pd = Path(args.paper_dir)

    bib_path = pd / "references.bib"
    if not bib_path.exists():
        print(f"check_refs: no references.bib under {pd}", file=sys.stderr)
        return 0
    text = bib_path.read_text(errors="replace")

    fails: list[str] = []

    # --- parse entries, detect duplicates ---
    entries = parse_entries(text)
    seen: dict[str, int] = {}
    for etype, key, _, _ in entries:
        seen[key] = seen.get(key, 0) + 1
    for key, n in seen.items():
        if n > 1:
            fails.append(f"duplicate bibkey '{key}' defined {n}x")
    defined = set(seen)
    bodies = {key: text[s:e] for etype, key, s, e in entries}

    # --- orphan/malformed: field lines outside any entry body ---
    covered = bytearray(len(text))
    for _, _, s, e in entries:
        for j in range(s, e):
            covered[j] = 1
    pos = 0
    for line in text.split("\n"):
        if FIELD_LINE_RE.match(line) and not covered[pos]:
            fails.append(f"orphan field line outside any @entry: «{line.strip()[:60]}»")
        pos += len(line) + 1

    # --- collect cited keys from prose ---
    cited: set[str] = set()
    scanned = 0
    targets = [pd / "main.tex"]
    for sub in ("chapters", "appendices"):
        d = pd / sub
        if d.exists():
            targets += sorted(d.glob("*.tex"))
    for t in targets:
        if not t.exists():
            continue
        scanned += 1
        body = re.sub(r"(?<!\\)%.*", "", t.read_text(errors="replace"))
        for m in CITE_RE.finditer(body):
            for k in m.group(1).split(","):
                k = k.strip()
                if k:
                    cited.add(k)

    # --- FAIL: undefined citations ---
    for k in sorted(cited - defined):
        fails.append(f"undefined citation \\cite{{{k}}} — no entry in references.bib")

    # --- advisory: entries with no identifier (not machine-verifiable) ---
    no_id = sorted(
        key for key in defined
        if not (DOI_RE.search(bodies[key])
                or re.search(r"\d{4}\.\d{4,5}", bodies[key])
                or ("url" in bodies[key].lower() and "http" in bodies[key].lower()))
    )
    # --- advisory: entries never cited (expected while chapters are stubs) ---
    uncited = sorted(defined - cited)

    # --- online identifier->title check ---
    if args.online:
        checked = skipped = 0
        for key in sorted(defined):
            b = bodies[key]
            bt = entry_field(b, "title")
            if not bt:
                continue
            dm = DOI_RE.search(entry_field(b, "doi") or "") or DOI_RE.search(b)
            am = (re.search(r"(\d{4}\.\d{4,5})", entry_field(b, "eprint") or "")
                  or re.search(r"arXiv:\s*(\d{4}\.\d{4,5})", b)
                  or re.search(r"(\d{4}\.\d{4,5})", b))
            real = doi_title(dm.group(0)) if dm else None
            if real is None and am:
                real = arxiv_title(am.group(1))
            if real is None:
                skipped += 1
                continue
            checked += 1
            a, c = norm_title(bt), norm_title(real)
            ratio = difflib.SequenceMatcher(None, a, c).ratio()
            if a not in c and c not in a and ratio < 0.75:
                fails.append(
                    f"identifier MISMATCH '{key}': bib title != resolved title\n"
                    f"      bib:      {bt[:80]}\n      resolved: {real[:80]}")
        print(f"check_refs(online): resolved {checked} identifiers, {skipped} unresolvable/no-id")

    # --- report ---
    if args.show_no_id:
        for k in no_id:
            print(f"ADVISORY  no machine-verifiable id: {k}", file=sys.stderr)
    if args.show_uncited:
        for k in uncited:
            print(f"ADVISORY  never \\cite'd: {k}", file=sys.stderr)
    for f in fails:
        print(f"FAIL  {f}", file=sys.stderr)

    n_advisory = len(no_id) + len(uncited)
    if fails or (args.strict_warn and n_advisory):
        print(f"\ncheck_refs: {len(fails)} integrity failure(s) "
              f"across {len(defined)} entries / {scanned} .tex files "
              f"({len(no_id)} no-id, {len(uncited)} uncited advisories).", file=sys.stderr)
        return 1
    print(f"check_refs: OK — {len(defined)} entries, {len(cited)} cited, "
          f"no integrity failures. "
          f"Advisories: {len(no_id)} without a machine-verifiable id, "
          f"{len(uncited)} not yet cited (run --show-no-id / --show-uncited to list).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
