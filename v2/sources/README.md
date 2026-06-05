# sources/ — original paper material (reference only)

The papers that individual chapters are built from. This directory is **not
compiled and not gated**: `make paper`, `lint.py`, and `build_numbers.py` only
touch `main.tex`, `chapters/`, and `appendices/`, so nothing here affects the
build or the bib gate.

## Source → chapter map

| Directory | Feeds | Status |
|---|---|---|
| `iclr2025_label_blindness/` | Chapter 4 — Label Blindness in Unlabeled OOD Detection | ICLR 2025 camera-ready (`paper.tex`, `iclr2025_conference.bib`, figures). **Public** — committed. |
| `eccv2026_domain_feature_collapse/` | Chapter 5 — Domain Feature Collapse | ECCV 2026 paper *"Beyond the Class Subspace: Teacher-Guided Training…"* (`main.tex`, `main.bib`, `results_macros.tex`, `generated_*` tables, figures). Source: `hyang0129/eccv2026`. **Public as of 2026-06-05** — arXiv:2603.11269 (submitted 2026-03-11); under review at venue but preprint is public. |
| `hallulens_mi_hallucination/` | Chapter 6 — Information-Theoretic Hallucination Detection | Paper *"Detecting Hallucinations via Mutual Information Analysis of Intermediate Layer Activations"* (`main.tex`, `sections/`, `data/*.csv`, `macros.tex`, `references.bib`). Source: `hyang0129/HalluLens` (`paper/`). **Already uses this exact bib-gate build system.** Public source. |

> ℹ️ **Embargo lifted 2026-06-05.** The ECCV 2026 paper is now a public arXiv
> preprint (arXiv:2603.11269, submitted 2026-03-11), so vendoring its source here
> no longer requires the dissertation repo to stay private. The repo had been
> switched to private on 2026-06-03 solely to hold this source; that constraint no
> longer applies and the repo may be made public again at the author's discretion.

## Rules (so source material can't defeat the v2 design)

1. **Never `\input` a file from `sources/` into a chapter.** Doing so would
   smuggle the paper's hard-coded numbers past the number gate. Reuse is
   *copy-and-macroise*: lift the prose/figure into `chapters/`, then route every
   number through a `\result{}` macro backed by a CSV in `data/`.
2. **Citations are still human-gated.** A paper's `.bib` here is a convenient
   donor, but entries reach `references.bib` only after a human vets them
   (propose in `outlines/` first — see `../outlines/README.md`).
3. **Figures:** prefer re-rendering via `figures_src/*.py` (single source of
   truth). If you reuse a baked figure from a source tree, copy it into the
   build and note its origin.

Add one subdirectory per source paper, lowercase-slug named after the chapter it
feeds, and add a row to the table above.
