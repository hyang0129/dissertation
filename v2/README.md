# Dissertation v2 — Build System & Bib Gate

This is the v2 rewrite of the dissertation. The **document format is unchanged**
from v1 (RIT GCCIS one-column `book` class + `thesisfrontmatter.sty`). What is
new is the *engineering*, ported from the onlycodes paper build system
([`hyang0129/onlycodes/paper`](https://github.com/hyang0129/onlycodes/tree/main/paper)):

> Every number and every figure in the dissertation traces back to a single CSV
> cell. When an experiment re-runs and its CSV regenerates, `make paper` picks up
> new values automatically. **A stale value is a build failure, not a
> proofreading task.**

Macro namespace prefix is `ds@` (dissertation) instead of onlycodes' `oc@`;
otherwise the contracts are identical.

## Quick start

```bash
cd v2/
make deps         # first-time only: pip install pandas, numpy, scipy, matplotlib
make paper        # renders figures, builds values.tex, lints (BIB GATE), compiles PDF
make figures      # render figures_src/*.py only
make values       # build generated/values.tex from data/ + sidecar CSVs
make lint         # BIB GATE: check prose for bare digits outside citation macros
make clean        # remove generated/ and LaTeX byproducts
```

`latexmk` (already in this dev container) is required for `make paper`. All
other targets need only Python 3 and the packages in
[requirements.txt](requirements.txt). To use a repo-local venv instead of
system Python (recommended — keeps the repo venv-isolated per the workspace
rules):

```bash
python3 -m venv ../.venv && ../.venv/bin/python -m pip install -r requirements.txt
make PYTHON=../.venv/bin/python paper
```

## The bib gate (two halves)

### 1. Number gate — `make lint`

`lint.py` flags any bare digit in `chapters/*.tex`, `appendices/*.tex`, and
`main.tex` that is **not** inside an approved macro (`\result`, `\resdelta`,
`\resratio`, `\resultCI`, `\resultPM`, `\cite*`, `\ref`, `\eqref`, `\label`),
**not** a year (`19xx`/`20xx`), and **not** a whitelisted literal string. Math
mode is exempt. This makes every claimed number traceable: it either comes from
a CSV via a `\result`-family macro, or the build fails.

To allow a legitimate bare digit, add a literal string to `WHITELIST` in
`lint.py` and document it below.

### 2. Citation gate — human-gated `references.bib` + `make check-refs`

**Policy.** `references.bib` is human-gated: new citations are proposed in
`outlines/<chapter>.md` first, with enough detail to verify, and only then added
by a human. (The seed `references.bib` was copied from `../v1/Bibliography.bib`.)

**Enforcement.** A `PreToolUse` hook (`.claude/settings.json` →
`.claude/hooks/protect_references_bib.py`) intercepts every agent attempt to
*write* `references.bib` — via `Edit`/`Write`/`MultiEdit` **or** a `Bash` command
that writes it (redirects, `tee`, `sed -i`, `cp`/`mv`, or a script's `open(...,
'w')`) — and escalates to a user-approval prompt (`permissionDecision: "ask"`).
You approve a verified entry or reject it; reading the file is never blocked. The
hook fails open on parse errors and does not affect your own edits in the editor.

**Tooling — `check_refs.py` (`make check-refs`).** Offline, stdlib-only, fails
the build on:
- an **undefined citation** (`\cite` key with no entry),
- a **duplicate bibkey**,
- an **orphaned/malformed entry body** (field lines outside any `@entry` — the
  corruption that hid a broken `huang2021mos` entry in the seed bib).

It also summarizes two advisories (entries with no DOI/arXiv/url; entries not yet
cited — expected while chapters are stubs); list them with `--show-no-id` /
`--show-uncited`. `make check-refs ONLINE=1` additionally resolves each arXiv id /
DOI and **fails if the resolved title doesn't match the bib title** — the check
that catches an identifier pointing at the wrong paper (needs network; for CI /
pre-submission, not the default build).

**Periodic deep audit.** A full web re-verification of every entry (the
`reference-audit` multi-agent workflow) is re-runnable on demand; its last run is
in `reports/reference_audit.md`.

## Citation macros

Defined in `macros.tex`; values resolve at LaTeX build time from
`generated/values.tex` (produced by `build_numbers.py`).

| Macro | Renders |
|---|---|
| `\result{csv}{key}[p]` | one CSV cell, `p` decimal places |
| `\resdelta{csv}{a}{b}[p]` | `a - b` (computed at build time, explicit sign) |
| `\resratio{csv}{a}{b}[p]` | `a / b` |
| `\resultCI{csv}{mean,lo,hi}[p]` | `mean [lo, hi]` |
| `\resultPM{csv}{mean,err}[p]` | `mean ± err` |
| `\resp`, `\respp`, `\respct`, `\resdollar` | p-values, percentage-points, percentages, USD |

- `csv` is the stem of a file in `data/` (e.g. `example_metrics` for
  `data/example_metrics.csv`) or `fig.<name>` for a figure sidecar.
- `key` is a colon-joined coordinate per the CSV's `key_schema`, plus the
  column name (e.g. `example:auroc:value`).

## CSV provenance header

Every CSV in `data/` must start with this block (read by `build_numbers.py`):

```
# source_commit: <sha or 'placeholder'>
# generated: <ISO timestamp>
# generator: <script name or "hand-built — <reason>">
# key_schema: col1:col2          # colon-separated row-key columns
# default_precision: 3           # optional, falls back to 3
```

`build_numbers.py` checks `source_commit` is an ancestor of HEAD and warns if
not — catching CSVs generated off a stale branch. `placeholder`/`unknown` skip
the check.

## File map

| Path | Purpose |
|---|---|
| `main.tex` | LaTeX entry point — `book` class + `thesisfrontmatter` |
| `thesisfrontmatter.sty`, `math_commands.tex` | RIT frontmatter + math macros (from v1) |
| `frontmatter/*.tex` | Cover/abstract/acknowledgements/dedication stubs |
| `chapters/*.tex` | One file per chapter (compiled via `\input`) |
| `appendices/*.tex` | One file per appendix |
| `outlines/*.md` | Per-chapter planning docs + proposed citations (not compiled) |
| `macros.tex` | `\result`, `\resdelta`, ... macro definitions (namespace `ds@`) |
| `references.bib` | Bibliography — **human-gated**, seeded from v1 |
| `build_numbers.py` | CSV → `generated/values.tex` generator |
| `lint.py` | The number half of the bib gate |
| `Makefile` | Build orchestration |
| `data/*.csv` | Provenance-headed CSVs (single source of truth for numbers) |
| `figures_src/*.py` | Figure renderers; each emits a PDF + `*.numbers.csv` sidecar |
| `sources/` | Original paper source per chapter — **reference only**, not compiled or gated (see `sources/README.md`) |
| `generated/` | Build outputs (git-ignored): `values.tex`, `figures/*.pdf`, ... |

## Current whitelist (non-exhaustive)

Enumeration markers (`(1) `, ...), chapter/objective labels (`Chapter 4`,
`Objective 1`), cross-reference phrasings (`Figure~\ref`, `Table~\ref`, ...),
statistical phrases (`95% CI`), LaTeX table syntax (`\multicolumn{`,
`\cmidrule`), and version paths (`v1`, `v2`). Edit `WHITELIST` in `lint.py` to
extend.
