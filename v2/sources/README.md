# sources/ — original paper material (reference only)

The papers that individual chapters are built from. This directory is **not
compiled and not gated**: `make paper`, `lint.py`, and `build_numbers.py` only
touch `main.tex`, `chapters/`, and `appendices/`, so nothing here affects the
build or the bib gate.

## Source → chapter map

| Directory | Feeds | Status |
|---|---|---|
| `iclr2025_label_blindness/` | Chapter 4 — Label Blindness in Unlabeled OOD Detection | ICLR 2025 camera-ready (`paper.tex`, `iclr2025_conference.bib`, figures). **Public** — committed. |
| `eccv2026_domain_feature_collapse/` | Chapter 5 — Domain Feature Collapse | ECCV 2026 paper *"Beyond the Class Subspace: Teacher-Guided Training…"* (`main.tex`, `main.bib`, `results_macros.tex`, `generated_*` tables, figures). Source: `hyang0129/eccv2026`. **Under review — tracked, but this whole repo is PRIVATE.** See note below. |
| `hallulens_mi_hallucination/` | Chapter 6 — Information-Theoretic Hallucination Detection | Paper *"Detecting Hallucinations via Mutual Information Analysis of Intermediate Layer Activations"* (`main.tex`, `sections/`, `data/*.csv`, `macros.tex`, `references.bib`). Source: `hyang0129/HalluLens` (`paper/`). **Already uses this exact bib-gate build system.** Public source. |

> ⚠️ **This source is under review; the dissertation repo is therefore PRIVATE.**
> The ECCV 2026 paper is unpublished (likely double-blind). It is committed here
> only because `hyang0129/dissertation` was switched to **private** to hold it.
> **Do not make the dissertation repo public again** until this paper is public
> (arXiv / camera-ready), or move/remove this source first.

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
