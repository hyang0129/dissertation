# Dissertation v2 — Master Outline

**Title (working):** Information-Theoretic Approaches to Out-of-Distribution
Detection and Hallucination Detection
**Author:** Hong Yang

This is the plan for what the **final, defendable** dissertation should contain.
It carries over the completed v1 material, drops the proposal-only scaffolding,
and reserves two chapters for source papers that are still pending.

## Status legend

| Mark | Meaning |
|---|---|
| ✅ **carry-over** | Substantively complete in v1 — port and de-proposalise |
| ⬜ **blank (pending source)** | Leave a stub; fill when the source paper arrives |
| ✏️ **revise** | Exists in v1 but needs rewriting (remove proposal framing) |
| ❌ **drop** | In v1 but does not belong in a completed dissertation |

## The spine (thesis statement)

Information theory is the unifying lens: across three settings, *detection is
possible only when the learning objective preserves the mutual information
relevant to the thing being detected*, and it is **provably guaranteed to fail**
when that information is discarded.

1. **Unlabeled OOD detection** fails when the self-/unsupervised surrogate task
   is independent of label-relevant features (Label Blindness). — *done*
2. **Single-domain OOD detection** fails when domain-relevant features collapse
   during representation learning (Domain Feature Collapse). — *replacement paper pending*
3. **LLM hallucination** arises as a loss of mutual information between query and
   response in intermediate layers. — *MI-Hallucination paper pending*

Pillars 1–2 prove failure and offer evaluation/mitigation; pillar 3 turns the
same information-theoretic frame onto generative models.

---

## Chapter structure

### Chapter 1 — Introduction ✅ carry-over ✏️
- **Source:** [v1/Introduction.tex](../../v1/Introduction.tex), [v1 §1](../../v1/Sample_Thesis_main.tex)
- **Purpose:** Motivate the reliability problem (OOD + hallucination), state the
  information-theoretic spine, enumerate contributions, map the document.
- **Sections:**
  - 1.1 Problem Statement and Motivation
  - 1.2 Research Objectives and Contributions
  - 1.3 Methodology and Approach
  - 1.4 Dissertation Organization
  - 1.5 Significance *(rename from v1's "Expected Impact and Significance" — drop forward-looking "expected")*
- **Revise:** convert "we propose / will" → "we present / show". Contributions
  list should describe completed work, with pillar 3 framed as the chapter's
  scope honestly.

### Chapter 2 — Background and Definitions ✅ carry-over
- **Source:** [v1 §2](../../v1/Sample_Thesis_main.tex), [v1/Background.tex](../../v1/Background.tex)
- **Purpose:** Shared formal vocabulary used by all three pillars.
- **Sections:** 2.1 OOD Detection · 2.2 Anomaly Detection (scope, training
  assumptions, evaluation) · 2.3 Information Theory (entropy, mutual information)
  · 2.4 Information Bottleneck & Minimal Sufficient Statistic · 2.5 Dataset
  Domain (incl. Domain Features & Domain Feature Collapse) · 2.6 Unlabeled OOD
  Detection · 2.7 Large Language Models
- **Note:** 2.5/2.6 prime Chapters 4–5; 2.7 primes Chapter 6. Keep as-is.

### Chapter 3 — Literature Review ✅ carry-over
- **Source:** [v1 §3](../../v1/Sample_Thesis_main.tex)
- **Purpose:** Position all three pillars against prior work.
- **Sections:** 3.1 Information Theory in ML · 3.2 Representation Learning
  (unsupervised, self-supervised) · 3.3 OOD Detection (classical /
  self-supervised / benchmarking / single-domain / domain adaptation /
  ensembles) · 3.4 Hallucination Detection (taxonomy, info-theoretic,
  evaluation) · 3.5 Model Architectures (CNNs, Transformers, foundation models)
- **Decision needed:** keep Ch.2 and Ch.3 separate (v1 does) or merge into one
  "Background & Related Work" chapter. Recommendation: keep separate.

### Chapter 4 — Label Blindness in Unlabeled OOD Detection ✅ carry-over (strongest chapter)
- **Source:** [v1 §4](../../v1/Sample_Thesis_main.tex); paper source at
  [sources/iclr2025_label_blindness/](../sources/iclr2025_label_blindness) (ICLR 2025 camera-ready)
- **Status:** Complete, peer-reviewed (ICLR 2025). Port with light edits.
- **Sections:** 4.1 Introduction · 4.2 Preliminaries (labeled/unlabeled OOD;
  self-/unsupervised learning) · 4.3 Guaranteed OOD Failure → **Label Blindness
  Theorem** · 4.4 Benchmarking → **Adjacent OOD** (vs near/far OOD) · 4.5
  Experiments (supervised/SSL/unsupervised/zero-shot baselines; Faces/Cars/Food)
  · 4.6 Discussion · 4.7 Conclusion
- **Numbers/figures for the bib gate:** Table of AUROC/FPR95 across
  {Faces, Cars, Food} × {MSP, SimCLR-KNN/SSD, RotLoss-KNN/SSD, Diffusion
  LPIPS/MSE, CLIPN CTW/ATD/MSP} → `data/label_blindness_results.csv`
  (mean±std, 3 seeds). GradCAM/example figures → `figures_src/`.
- **Proofs:** Appendix A.

### Chapter 5 — Domain Feature Collapse in Single-Domain OOD Detection ⬜ blank (source located, not yet drafted)
- **Source:** ECCV 2026 paper *"Beyond the Class Subspace: Teacher-Guided
  Training for Reliable OOD Detection in Single-Domain Models"* (repo
  `hyang0129/eccv2026`). Copied to `sources/eccv2026_domain_feature_collapse/`;
  tracked, but the dissertation repo is **private** because this paper is under
  review — see `../sources/README.md` (keep the repo private until the paper is
  public). Do **not** port v1 §5 (that was the prior AAAI framing).
- **Framing shift to confirm:** the paper renames the phenomenon
  **Domain-Sensitivity Collapse (DSC)** (supervised training compresses features
  into a low-rank class subspace, suppressing domain-shift directions) and adds a
  method, **Teacher-Guided Training (TGT)** — distilling class-suppressed
  residual structure from a frozen DINOv2 teacher (discarded at inference).
  → Decide the chapter title: keep "Domain Feature Collapse", or adopt
  "Domain-Sensitivity Collapse / Teacher-Guided Training".
- **Tentative sections (from the ECCV paper, to confirm):** Introduction ·
  Problem setup (single-domain regime) · Theory: DSC / class-subspace collapse ·
  Method: Teacher-Guided Training · Experiments (8 single-domain benchmarks;
  MDS/ViM/kNN far-OOD FPR@95) · Ablations (λ) · Limitations · Conclusion
- **Numbers/figures:** the paper already uses a `results_macros.tex` +
  `generated_*.tex/.csv` pipeline (close to our bib gate) — port those CSVs into
  `data/` with provenance headers and re-express via `\result{}`.
- **Proofs:** Appendix B (pending — tied to this chapter's DSC theory).

### Chapter 6 — Information-Theoretic Hallucination Detection ⬜ blank (source located, not yet drafted)
- **Source:** paper *"Detecting Hallucinations via Mutual Information Analysis of
  Intermediate Layer Activations"* (repo `hyang0129/HalluLens`, `paper/`). Copied
  to `sources/hallulens_mi_hallucination/`. Do **not** port v1 §6 (that was a
  *proposal*, no results). Public source.
- **Big advantage:** this paper **already uses the same bib-gate build system**
  (the v2 system was itself adapted from it). Its `sections/*.tex`, `macros.tex`,
  `data/*.csv` (provenance headers), and `references.bib` port over almost
  directly — re-namespace its macros and fold its CSVs into `v2/data/`.
- **Tentative sections (from the paper, to confirm):** Introduction · Related
  Work · Method (MI between query/response across intermediate layers;
  contrastive MI estimation) · Experimental Setup · Results · Domain Transfer ·
  Limitations.
- **Numbers/figures:** port `sources/hallulens_mi_hallucination/data/*.csv`
  (headline_results, baseline_comparison, transfer_*) into `v2/data/` and reuse
  `figures_src/` renderers.

### Chapter 7 — Conclusion ✅ carry-over ✏️ (was v1 Ch.8)
- **Source:** [v1 §8](../../v1/Sample_Thesis_main.tex)
- **Purpose:** Synthesise the three pillars under the information-theoretic
  spine; state limitations and genuine future work.
- **Sections:** 7.1 Summary of Contributions *(drop "Proposed")* · 7.2 Broader
  Implications (AI safety, information theory in ML, evaluation) · 7.3 Future
  Directions · 7.4 Concluding Remarks
- **Revise:** delete v1's "Research Timeline and Feasibility" and "Expected
  Outcomes / Success Metrics" sections — proposal artefacts.

---

## Appendices

- **Appendix A — Theoretical Proofs for Label Blindness** ✅ carry-over.
  Source: [v1/AppendixA.tex](../../v1/AppendixA.tex). MI/entropy properties;
  sufficiency; strict label blindness in the minimal sufficient statistic;
  independence of filtered distributions; guaranteed OOD failure; unavoidable
  risk of overlapping OOD.
- **Appendix B — Theoretical Proofs for Domain Feature Collapse** ⬜ blank
  (pending). Tied to Chapter 5's replacement paper; do not port v1/AppendixB.tex
  until the new paper's theory is fixed.

---

## What changes from v1 (and why)

| v1 | v2 | Reason |
|---|---|---|
| Ch.5 Domain Feature Collapse (AAAI) | ⬜ blank, new source pending | Being replaced by a different paper |
| Ch.6 Hallucinations (**proposed**) | ⬜ blank, MI paper pending | v1 is a proposal with no results |
| **Ch.7 Research Timeline** (Gantt, "Months 1–12", milestones, risk) | ❌ **dropped** | Proposal-only; never appears in a final dissertation |
| Ch.8 Conclusion ("Proposed Contributions", "Expected Outcomes") | Ch.7 Conclusion ✏️ | De-proposalise to accomplished work |
| Numbers hard-coded in prose | `\result{}` macros ← `data/*.csv` | The v2 bib gate |
| `references.bib` edited freely | human-gated; propose in `outlines/` | Bib gate |

## Open questions for you

1. **Keep Ch.2 Background and Ch.3 Literature Review separate**, or merge?
   (Recommend: separate, as v1.)
2. **Chapter order** — is OOD-then-hallucination (4→5→6) the intended narrative,
   or should the two OOD chapters (Label Blindness, Domain Feature Collapse) be
   adjacent with hallucination last? (Current plan already does this: 4, 5 = OOD;
   6 = hallucination.)
3. For the **two pending chapters**, do you want me to keep the tentative section
   skeletons above as outline placeholders, or leave them fully empty until the
   papers land?
