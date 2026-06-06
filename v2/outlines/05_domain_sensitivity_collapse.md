# Chapter 5 — Domain-Sensitivity Collapse & Teacher-Guided Training · port plan

Plan for porting the ECCV 2026 paper *"Beyond the Class Subspace: Teacher-Guided
Training for Reliable OOD Detection in Single-Domain Models"* (arXiv:2603.11269,
public) into Ch.5. Companion to [00_dissertation_outline.md](00_dissertation_outline.md)
(Ch.5 entry) and [03_literature_review.md](03_literature_review.md) (§4 RW scope).
Source tree: [`../sources/eccv2026_domain_feature_collapse/`](../sources/eccv2026_domain_feature_collapse).

**Status:** ⬜ not yet drafted (`chapters/05_domain_sensitivity_collapse.tex` is a
stub). This is a **rewrite from the paper**, not a port of v1 §5 (phenomenon
renamed DFC→DSC *and* method changed domain-filtering→TGT).

**Not Ch.4.** Ch.4 ported a *dissertation* chapter (matching cite keys, one printed
table). Ch.5 ports a *conference paper*: its own number system (50 macros + ~10
generated tables), mismatched cite keys, and a 608-line supplementary to triage.

## Decisions (2026-06-06)

- **Supplementary triage: LEAN.** App.B = proofs only (linear illustration + Thm 1
  + Prop 1). Deep supplementary (geometry-audit internals, teacher-only oracle,
  extended per-dataset tables, implementation details) stays in the source/arXiv —
  cite it, don't vendor it.
- **Table scope: CORE set.** Main text carries: dual-metric near+far OOD (headline),
  the DSC geometry/effective-rank table (diagnostic evidence), and the EuroSAT
  λ-ablation. Defer pr95 variants, within-class-variance, teacher-oracle, accuracy,
  and per-dataset breakdowns (→ arXiv).
- **DSC is defined here**, not in Ch.2 (Ch.2 only primes geometry — see
  [02_background.md](02_background.md) §2.8). Same primitives-vs-contributions rule
  as Ch.4/Ch.6.

---

## 1. Section map (source main.tex → Ch.5)

| Source §  | → | Ch.5 § | Action |
|---|---|---|---|
| Introduction | | 5.1 Introduction | port; lead with diagnosis+recovery framing (not impossibility) |
| Related Work (OOD; geometry/NC/rank; KD; fine-tuning) | | 5.2 Related Work | **tighten to ~0.5–1pg**; back-ref Ch.3 §3.2 (geometry/NC), §3.3 (OOD scorers), distillation thread; position vs direct comparators only |
| Domain-Sensitivity Collapse (anisotropic geometry & distance failure; DSC from single-domain training; empirical validation) | | 5.3 Domain-Sensitivity Collapse | **defines DSC**; geometry/rank table lands here; Thm 1 / Prop 1 stated, proofs → App.B |
| Method (class-suppressed teacher residuals; TGT) | | 5.4 Method | port |
| Experiments (datasets/setup; TGT improves across scorers; why DINOv2 less; ablations) | | 5.5 Experiments | core tables only |
| Conclusion | | 5.6 Conclusion | port; de-conference |
| supplementary §Extended Proofs | | **Appendix B** (`app:dsc-proofs`) | linear illustration + Thm 1 + Prop 1 |

## 2. Number-gate port inventory (the dominant work item)

The paper bakes numbers two ways, both incompatible with the v2 gate
(`\result{stem}{key}` ← `data/*.csv`). **Never `\input` a source tabular**
(sources/README rule #1); rebuild each table with `\result` per cell (as in Ch.4).

### 2a. Headline scalars — `results_macros.tex` (50 `\newcommand`s)
→ `data/dsc_narrative.csv`. ⚠️ Heterogeneous: clean decimals (e.g. `59.07%`,
effective-rank `5.2`) port directly; **non-decimal constants need per-type
handling** — split counts like `38/40` → two cells (num/den) rendered
`\result/\result`; percentages → store bare number, render with literal `\%`;
ranges (`0.80`–`0.95`) → two cells. Each macro's provenance comment carries over
into the CSV header/notes.

### 2b. Core results tables → CSVs + hand-built `\result` tabulars
| Source tabular | → CSV stem | key_schema | value cols |
|---|---|---|---|
| `generated_dual_metric_nearood_tabular.tex` | `dsc_main_nearood` | `scorer` | `{dino,tgdino,resnet,tgresnet,supcon}_{fpr95,auroc}` |
| `generated_dual_metric_farood_tabular.tex` | `dsc_main_farood` | `scorer` | same |
| `generated_geometry_table.tex` / `generated_rank_table.tex` | `dsc_geometry` | `dataset:variant` (base/TGT) | `eff_rank`, … |
| `generated_eurosat_lambda_ablation.csv` (shipped, **no provenance header**) | `dsc_eurosat_lambda` | `lambda:scorer` | `fpr95,auroc,aupr_in,aupr_out,fpr98` |

- Scorers (rows): EBO, MDS, MSP, kNN, NCI, ReAct, SCALE, ViM (+ "MDS Teacher Only").
  Missing cells (`-`) → omit the row/col or store `NaN` (build_numbers skips NaN).
- Bolding: source bolds the TGT columns. Keep as static `\textbf{\result{…}}` (the
  win is structural — TGT vs base — not a per-run significance claim).
- **Deferred (→ arXiv, not gated):** `generated_pr95_*`, `within_class_var`,
  `teacher_oracle`, `training_weight_accuracy`, extended per-dataset tables.

## 3. Citation reconciliation — VERIFIED CLEAN (2026-06-06)

All **32** paper keys resolve to existing gated entries: **20 direct** key matches
+ **12 remaps** (same paper, different key — verified by title, not key name).
**Zero new bib entries needed; no bib-gate additions.** Drafting just substitutes
the paper's key for the gated key.

### Remap table (paper key → existing gated key) — all confirmed by title
| ECCV key | gated key | | ECCV key | gated key |
|---|---|---|---|---|
| `Hendrycks2017msp` | `hendrycks2016baseline` | | `Fort2021pretrained` | `fort2021exploring` |
| `Lee2018maha` | `lee2018simple` | | `Yang2024survey` | `yang2021generalized` |
| `Liang2018odin` | `liang2017enhancing` | | `Liu2023nci` | `liu2025detecting` |
| `Sun2022knn` | `sun2022out` | | `Xu2024scale` | `xuscaling` |
| `Khosla2020supcon` | `khosla2020supervised` | | `Cao2020medood` | `cao2020benchmark` |
| `Oquab2024dinov2` | `oquab2023dinov2` | | `Hinton2015kd` | `hinton2015distilling` |

The other 20 keys (e.g. `Wang2022vim`, `Sun2021react`, `Yang2022openood`,
`Papyan2020nc`, `Caron2021dino`, `Sehwag2021ssd`, `Tack2020csi`, …) match the gated
key directly. Earlier scoping wrongly flagged NCI/SCALE/Cao-medical as new — they
were present under `liu2025detecting` / `xuscaling` / `cao2020benchmark`.
*Minor:* `yang2021generalized` is the arXiv-2021 record; the paper cited the
IJCV-2024 version of the same survey — remap is fine; optionally refresh that entry.

## 4. Proofs → Appendix B (`app:dsc-proofs`)

Port from `supplementary.tex` §Extended Proofs (lines ~130–240):
- Linear-Model Illustration (main-text companion)
- **Theorem 1** (distance failure under variance–discriminability mismatch) — `thm:supp:dist-fail`
- **Proposition 1** (MSP/Energy insensitivity)

Keep proof statements in §5.3 with `\ref{app:...}` pointers (mirrors Ch.4 → App.A).
App.B `B_dsc_proofs.tex` already exists as a stub.

## 5. Transform checklist (mirrors Ch.4's)

1. 🔴 **Number gate** — §2 inventory: build `dsc_narrative`, `dsc_main_nearood/farood`,
   `dsc_geometry`, `dsc_eurosat_lambda` CSVs (provenance headers); rebuild tables
   with `\result`. *Largest item — ~10× Ch.4's single table.*
2. **Cite remap** — apply §3 remap table in prose (mechanical key substitution).
   No bib-gate additions: all 32 keys already resolve.
3. **De-conference** — strip ECCV two-column/`llncs`/`\vspace` cruft; drop the
   anonymized/rebuttal scaffolding; expand page-limited prose where natural.
4. **RW tighten** — §5.2 back-refs Ch.3; no re-survey (see 03 §4 Ch.5 scope).
5. **Proofs → App.B** — §4 above.
6. **Figures** — effective-rank-vs-FPR@95 etc. → re-render via `figures_src/` if data
   is available, else copy baked PNGs into `figures/` with provenance (as Ch.4 did).

## 6. Drafting order (phased)

Dependency logic: the number port gates the prose (prose cites `\result` keys);
proofs and figures are independent; gates/build run last.

**Phase A — Number foundation (do first; the bulk).**
- A1. `dsc_main_nearood.csv` + `dsc_main_farood.csv` ← `generated_dual_metric_*_tabular.tex`
  (clean decimals; headline + most-referenced). Build + verify keys.
- A2. `dsc_geometry.csv` ← `generated_geometry_table.tex` / `generated_rank_table.tex`
  (use the source's columns now; reconcile with Ch.2 §2.8 later).
- A3. `dsc_eurosat_lambda.csv` ← shipped `generated_eurosat_lambda_ablation.csv`
  (just add the v2 provenance header + rename). Easy.
- A4. `dsc_narrative.csv` ← the 50 `results_macros.tex` scalars (last — needs the
  non-decimal convention call: 38/40 → num/den cells, % → bare + literal `\%`,
  ranges → two cells). Then `build_numbers` → confirm all keys resolve.

**Phase B — Prose port (body before front).**
- B1. §5.3 Domain-Sensitivity Collapse (core; defines DSC; geometry table + Thm/Prop statements).
- B2. §5.4 Method (TGT).
- B3. §5.5 Experiments (main tables + EuroSAT ablation).
- B4. §5.1 Introduction (write after results settle, so headline claims match).
- B5. §5.2 Related Work (tighten, back-ref Ch.3 — see 03 §4).
- B6. §5.6 Conclusion.
  Throughout: swap numbers→`\result`, paper-keys→gated-keys (§3), de-conference.

**Phase C — Proofs → Appendix B.** Port linear illustration + Thm 1 + Prop 1 into
`appendices/B_dsc_proofs.tex`; wire `\ref{app:...}` from §5.3.

**Phase D — Figures.** Check if the source ships figure data (→ `figures_src/`
renderer) or only baked PDFs (→ `figures/` copy-with-provenance, as Ch.4).

**Phase E — Gates & build.** `make lint` (whitelist dataset/scorer/arch tokens:
EuroSAT, ResNet50, DINOv2, MedMNIST, ViM, DINOv2…) → `build_numbers` → `latexmk`
(App.B now resolves the proof refs) → `check_refs`.

### Open items
- ✅ References verified clean (§3) — no bib work needed.
- 🔜 `dsc_geometry` exact columns — finalize with §5.3's table (and Ch.2 §2.8).
- 🔜 Non-decimal narrative-macro render convention — settle at A4.
- 🔜 Figures: source ships data vs baked PDFs only? — determines D.
