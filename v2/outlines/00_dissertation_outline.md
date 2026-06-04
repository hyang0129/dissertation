# Dissertation v2 — Master Outline

**Title (working):** What Representations Preserve: Information-Theoretic and
Geometric Conditions for Out-of-Distribution and Hallucination Detection
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

Information theory and representation geometry are the unifying lens: detection
is possible exactly when the learned representation preserves the structure that
distinguishes the shift. The dissertation runs that lens across three reliability
settings, moving from an impossibility result to a recovery method to a detector:

1. **Unlabeled OOD detection — a genuine failure result.** When the
   self-/unsupervised surrogate task is independent of label-relevant features,
   OOD detection is *provably guaranteed to fail* (Label Blindness). — *Ch.4, done*
2. **Single-domain OOD detection — diagnosis and recovery.** Single-domain
   supervised training induces *Domain-Sensitivity Collapse* (DSC): variance
   concentrates in a low-rank class subspace and domain-shift directions are
   suppressed, so distance- and logit-based OOD scores lose sensitivity. This is
   a *diagnostic* geometric account (explicitly **not** an impossibility claim —
   the paper's bounds are diagnostic, not guarantees); *Teacher-Guided Training*
   (TGT) **recovers** the lost sensitivity by distilling a frozen multi-domain
   teacher. — *Ch.5, source located*
3. **LLM hallucination — detection.** Hallucination is **detectable** from a
   model's intermediate-layer activations: a learned one-class contrastive probe
   over *cross-layer* activation pairs, motivated by an information-theoretic
   feasibility argument (cross-layer MI is positive by construction; the probe's
   trainability is the proof the label-relevant signal exists). The method reaches
   *parity* with the best engineered probe — parity being evidence the lens is
   right, not a leaderboard claim. — *Ch.6, source located*

The arc is failure → recovery → detection: Ch.4 proves when the representation
*cannot* support detection, Ch.5 *restores* the missing structure, Ch.6
*detects* the shift from the representation it leaves behind. The "guaranteed failure" claim is specific to Ch.4 (the Label
Blindness theorem); Ch.5 and Ch.6 are recovery- and detection-led, not
impossibility results.

---

## Chapter structure

### Chapter 1 — Introduction ✅ carry-over ✏️
- **Source:** [v1/Introduction.tex](../../v1/Introduction.tex), [v1 §1](../../v1/Sample_Thesis_main.tex)
- **Purpose:** Motivate the reliability problem (OOD + hallucination), state the
  representation-structure spine (information theory and geometry as its two
  lenses), enumerate contributions, map the document.
- **Sections:**
  - 1.1 Problem Statement and Motivation
  - 1.2 Research Objectives and Contributions
  - 1.3 Methodology and Approach
  - 1.4 Dissertation Organization
  - 1.5 Significance *(rename from v1's "Expected Impact and Significance" — drop forward-looking "expected")*
- **Revise:** convert "we propose / will" → "we present / show". Contributions
  list should describe completed work. **Pillar 3 verb is locked to Ch.6:**
  "matches-or-outperforms (in the mean)" — frame as *parity-from-an-information-
  theoretic-first-principle*, never "beats" / "state-of-the-art." §1 contribution,
  abstract, and Ch.6 results prose must all use this same verb (per the source's
  cross-section consistency rule).

### Chapter 2 — Background and Definitions ✅ carry-over ✏️
- **Source:** [v1 §2](../../v1/Sample_Thesis_main.tex), [v1/Background.tex](../../v1/Background.tex)
- **Purpose:** Shared formal vocabulary used by all three pillars.
- **Sections:** 2.1 OOD Detection · 2.2 Anomaly Detection (scope, training
  assumptions, evaluation) · 2.3 Information Theory (entropy, mutual information)
  · 2.4 Information Bottleneck & Minimal Sufficient Statistic · 2.5 Dataset
  Domain (incl. Domain Features & **Domain-Sensitivity Collapse, DSC** — renamed
  from v1's "Domain Feature Collapse") · 2.6 Unlabeled OOD Detection · 2.7 Large
  Language Models
- **Note:** 2.5/2.6 prime Chapters 4–5; 2.7 primes Chapter 6. ⚠️ **§2.5 needs a
  revise, not a clean carry-over:** v1's §2.5 defines "Domain Feature Collapse"
  under the old info-bottleneck framing; Ch.5/App.B now use **DSC** with a
  *geometric* account, so §2.5 must be renamed and reconciled to prime the DSC
  concept (variance in a low-rank class subspace, suppressed domain-shift
  directions), not the superseded DFC one. 2.6/2.7 carry over as-is.
- **Boundary with Ch.3:** §2.3 (Information Theory) and §2.4 (IB & Minimal
  Sufficient Statistic) own the **definitions/formalism**; Ch.3 §3.1 owns the
  **usage-literature** (info theory *in* ML). Definitions live here, the literature
  there — avoids the §2.3–2.4 ↔ §3.1 overlap.

### Chapter 3 — Literature Review ✅ carry-over ✏️
- **Source:** [v1 §3](../../v1/Sample_Thesis_main.tex)
- **Full plan:** [03_literature_review.md](03_literature_review.md) — RW
  architecture (division of labor with per-chapter RW), organizing principle, and
  per-section reference buckets (mapped to the 190-entry bib).
- **Purpose:** Position all three pillars against prior work under the
  representation-structure lens (info theory + geometry). Organize around the **two
  lenses** (§3.1–3.2 shared frame; §3.3–3.4 = two applications of one question;
  §3.5 substrate) so it reads as one review, not three.
- **Sections:** 3.1 Information Theory in ML · 3.2 **Representation Learning &
  Geometry** (self-/unsupervised + **neural collapse / alignment-uniformity /
  probes**) · 3.3 OOD Detection (scorers / benchmarking / unlabeled / single-domain
  + collapse / ensembles) · 3.4 Hallucination Detection (surveys / evaluation /
  sampling / **internal-state probing**) · 3.5 Architectures & Foundation Models
- **Status:** not a clean carry-over — §3.2 gains the geometry lens, §3.3 gets the
  single-domain/DSC reframe, §3.4 is largely rewritten for the real Ch.6 methods.
- **Architecture:** Ch.3 owns breadth + cross-pillar synthesis; per-chapter RW
  (Ch.4/5/6) owns depth + comparators and back-references §3.x (no duplication).

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
- **Related Work scope** (see [03_literature_review.md](03_literature_review.md) §4):
  unlabeled/SSL-OOD baselines tested (SimCLR-KNN/SSD, RotLoss, diffusion, CLIPN) +
  near/far/**adjacent**-OOD benchmarking. Defer sufficiency/MI → §3.1, SSL → §3.2.

### Chapter 5 — Domain-Sensitivity Collapse and Teacher-Guided Training for Single-Domain OOD Detection ⬜ blank (source located, not yet drafted)
- **Title decided (2026-06-03):** adopt the paper's **DSC / TGT** naming (was
  "Domain Feature Collapse"). Label remains `ch:domain-sensitivity-collapse`.
- **Source:** ECCV 2026 paper *"Beyond the Class Subspace: Teacher-Guided
  Training for Reliable OOD Detection in Single-Domain Models"* (repo
  `hyang0129/eccv2026`), at `sources/eccv2026_domain_feature_collapse/`. Tracked,
  but the repo is **private** (paper under review) — keep it private until the
  paper is public. Do **not** port v1 §5: the phenomenon was renamed (Domain
  Feature Collapse → **Domain-Sensitivity Collapse, DSC**) **and the solution
  changed** (v1's domain filtering / two-stage detector → **Teacher-Guided
  Training, TGT**). This is a rewrite, not a port.
- **Framing (per the paper, [main.tex:155](../sources/eccv2026_domain_feature_collapse/main.tex)):**
  DSC is a *geometric, diagnostic* account — single-domain supervised training
  drives features into a low-rank, class-aligned subspace, suppressing
  domain-shift directions, so distance-based (MDS, kNN, ViM) and logit-based
  (MSP, Energy) scorers lose sensitivity. The bounds are **diagnostic upper
  bounds, explicitly not guarantees**. So the chapter leads with *diagnosis +
  recovery (TGT)*, not an impossibility theorem.
- **Contributions (paper §1):** (1) formalize DSC as a root-cause failure mode
  with testable geometry predictions; (2) TGT — a training-time auxiliary loss
  (class-suppressed DINOv2 teacher residual) that restores domain-sensitive
  geometry with **no inference overhead**; (3) validation on 8 single-domain
  benchmarks (double-digit FPR@95 reductions for MDS/ViM/kNN).
- **Sections (from the paper):** Introduction · Related Work · Domain-Sensitivity
  Collapse (anisotropic geometry & distance failure; DSC induced by single-domain
  supervised training; empirical validation) · Method (class-suppressed teacher
  residuals; Teacher-Guided Training) · Experiments (8 benchmarks; TGT across
  scorers; why DINOv2 improves less; ablations) · Conclusion.
- **Numbers/figures:** the paper already uses `results_macros.tex` +
  `generated_*.tex/.csv` — port those CSVs into `data/` with provenance headers,
  re-express via `\result{}`; figures (effective-rank vs FPR@95, etc.) →
  `figures_src/`.
- **Related Work scope** (see [03_literature_review.md](03_literature_review.md) §4):
  single-domain OOD + the distance/logit scorers DSC degrades (MDS/kNN/ViM/MSP/
  Energy), neural collapse as the diagnosis's neighbor (§3.2 back-ref), the
  teacher-distillation lineage TGT builds on (CRD-style, DINOv2 teacher). Defer
  broad OOD → §3.3, geometry → §3.2.
- **Proofs → Appendix B** (changed; see below): Theorem 1 (distance failure under
  variance–discriminability mismatch) and Proposition 1 (MSP/Energy insensitivity).

### Chapter 6 — Information-Theoretic Hallucination Detection ⬜ blank (source located, not yet drafted)
- **Source:** paper *"Detecting Hallucinations via Mutual Information Analysis of
  Intermediate Layer Activations"* (repo `hyang0129/HalluLens`, `paper/`). Copied
  to `sources/hallulens_mi_hallucination/`. Do **not** port v1 §6 (that was a
  *proposal*, no results). Public source.
- **Big advantage:** this paper **already uses the same bib-gate build system**
  (the v2 system was itself adapted from it). Its `sections/*.tex`, `macros.tex`,
  `data/*.csv` (provenance headers), and `references.bib` port over almost
  directly — re-namespace its macros and fold its CSVs into `v2/data/`.
- **Framing decided (2026-06-04): methodology/theory-led, not results-led.** The
  empirical situation (see [`sources/.../05_results.md:27-36`](../sources/hallulens_mi_hallucination/05_results.md#L27-L36)):
  the method (`contrastive_logprob_recon`) **matches but does not statistically
  beat** the strongest learned baseline (ACT-ViT, `barshalom2025actvit`). Of 10
  cells it wins clearly on 3 (PopQA both models, SciQ-Qwen), ties on 3, loses on
  4 (firm losses on both NQ cells). The paper's own verb is
  **"matches-or-outperforms (in the mean)"** — do not escalate to "beats."
  Critically, the compute-efficiency result (single-pass beats K=10 sampling by
  +0.15–0.25 AUROC) is a **class-level** advantage of activation-reading over
  sampling — ACT-ViT is *also* single-pass activation-space, so it is **not** a
  differentiator against the actual competitor and cannot carry the chapter.
- **The chapter's claim (what the dissertation defends):** a hallucination
  detector derived from an *information-theoretic first principle* reaches
  **parity** with the best engineered probe — and the parity is itself evidence
  the lens is correct (a wrong principle would not land in the same performance
  band). The contribution is the **framework + mechanism + self-validation**, not
  a leaderboard win. This is the stronger spine fit: Ch.6 is the *detection*
  pillar under the information-theory lens (spine §3), so a principled,
  self-explaining method is more coherent than a benchmark-topping one would be.
- **Core contributions to foreground (from [`sources/.../03_method.md`](../sources/hallulens_mi_hallucination/03_method.md)):**
  1. **Feasibility-by-trainability argument.** Cross-layer MI is positive by
     construction (DPI on the residual stream); InfoNCE cannot descend below
     `−log K` if that MI were zero — so the loss descending *is* the empirical
     proof the signal exists. The probe's existence is the content of the theorem.
  2. **One-class contrastive over layer-pair views** with asymmetric
     `ignore_label` — the architectural novelty (views are *different layers* of
     one un-augmented forward pass, not augmentations; one class is the inlier
     anchor, the other only view-consistent).
  3. **A falsifiable prediction, confirmed.** Corollary A.1.1 predicts symmetric
     SupCon fails when one class lacks coherent latent structure; the Variant-4
     ablation drops ~10 AUROC points. Theory predicted, ablation confirmed — lead
     with this as the chapter's strongest empirical-of-theory moment.
  4. **2×2 signal attribution** (contrastive vs. logprob-recon channels) — the
     §3.4 menu; resolves *which* supervision carries the signal.
- **Section plan (re-ordered from the paper for a method-led chapter):**
  Introduction (state the parity-as-validation framing up front) · Related Work ·
  **Method + information-theoretic argument** (the conceptual core; promote, do
  not bury) · Experimental Setup · Results (read honestly: parity table + the NQ
  shortfall called out, *not* hidden) · Compute-matched comparison (present as
  motivation for the activation-reading *class*, with the ACT-ViT caveat stated) ·
  Ablations / attribution (the 2×2 + the confirmed symmetric-SupCon prediction) ·
  Domain Transfer · Limitations.
- **Proofs → Appendix C** (new; see Appendices below). Port the source paper's
  Proposition A.1 (asymmetric SupCon bounds label-conditioned MI on the inlier
  class), Corollaries A.1.1 / A.2.1, and Lemmas A.2 / A.3. **Renumber A.* → C.* on
  port** — the dissertation's Appendix A is Label Blindness, so the paper's
  `A.1 / A.2 / A.3` labels collide and must be re-namespaced (Proposition C.1, etc.).
- **Numbers/figures:** port `sources/hallulens_mi_hallucination/data/*.csv`
  (headline_results, baseline_comparison, transfer_*) into `v2/data/` and reuse
  `figures_src/` renderers. Honesty discipline from the source carries over: the
  bolding rule (bold a cell only when it beats the runner-up by > max std) and the
  two NQ losses must survive into the chapter prose.
- **Related Work scope** (see [03_literature_review.md](03_literature_review.md) §4):
  the three comparator families — output-space scalar (logprob/entropy/P(true)),
  activation probes (SAPLMA/LLMsKnow/**ACT-ViT**), sampling (SelfCheckGPT/semantic
  entropy) — + the contrastive-distillation precedent it extends (CRD/CoDIR/CDS,
  SEP). Defer info-theory → §3.1, contrastive → §3.2, taxonomy/eval → §3.4. Hosts
  the §2.3 novelty claim (layer-pair one-class contrastive vs CRD/CoDIR/CDS).

### Chapter 7 — Conclusion ✅ carry-over ✏️ (was v1 Ch.8)
- **Source:** [v1 §8](../../v1/Sample_Thesis_main.tex)
- **Purpose:** Synthesise the three pillars under the representation-structure
  spine (info theory + geometry as its two lenses); state limitations and genuine
  future work.
- **Sections:** 7.1 Summary of Contributions *(drop "Proposed")* · 7.2 Broader
  Implications (AI safety, information theory & representation geometry in ML,
  evaluation) · 7.3 Future
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
- **Appendix B — Geometric Proofs for Domain-Sensitivity Collapse** ⬜ blank
  (source located). **Changed from v1.** v1/AppendixB held information-bottleneck
  / mutual-information proofs for the old "domain feature collapse" — those do
  **not** carry over. The ECCV theory is *geometric*: port from
  `sources/eccv2026_domain_feature_collapse/supplementary.tex` (§Extended
  Proofs) — a linear-model illustration, **Theorem 1** (distance failure under
  variance–discriminability mismatch), and **Proposition 1** (MSP/Energy
  insensitivity). Label: `app:dsc-proofs`.
- **Appendix C — Information-Theoretic Proofs for Hallucination Detection** ⬜
  blank (source located). New in v2 (Ch.6 has no v1 counterpart). Port from
  `sources/hallulens_mi_hallucination/` Appendix A: **Proposition C.1** (asymmetric
  SupCon bounds label-conditioned MI on the inlier/truthful class), **Corollary
  C.1.1** (symmetric SupCon contraindicated when one class lacks coherent latent
  structure — the confirmed ≈−10-AUROC prediction), **Corollary C.2.1**
  (cross-layer/response co-information under downward determinism), **Lemma C.2**
  (DPI chain) and **Lemma C.3** (InfoNCE variational bound restated).
  **Renumber the source's A.* labels → C.*** to avoid colliding with Appendix A.
  Label: `app:mi-hallucination-proofs`.

---

## What changes from v1 (and why)

| v1 | v2 | Reason |
|---|---|---|
| Spine = universal "guaranteed failure" | failure (Ch.4) → diagnosis+recovery (Ch.5) → detection (Ch.6) | ECCV paper walked the guarantee back to *diagnostic bounds*; Ch.5 leads with recovery (TGT), Ch.6 with detection |
| Ch.5 Domain Feature Collapse (AAAI; domain-filtering solution) | Ch.5 **Domain-Sensitivity Collapse + TGT** (ECCV) | New paper: phenomenon renamed (DFC→DSC), **new method** (domain filtering → Teacher-Guided Training), diagnostic-geometric framing |
| Ch.6 Hallucinations (**proposed**) | Ch.6 MI hallucination detection (HalluLens) | v1 was a proposal with no results; now a real paper |
| App.B info-bottleneck / MI proofs for DFC | App.B **geometric** proofs (distance-failure Thm 1; MSP/Energy insensitivity Prop 1) | Follows the new DSC theory; v1 proofs superseded |
| *(no Ch.6 proofs — v1 Ch.6 was a proposal)* | **App.C** info-theoretic proofs for MI hallucination detection (Prop C.1 + corollaries/lemmas) | Ch.6 is now a real results chapter with a theoretical core; needs an appendix home |
| **Ch.7 Research Timeline** (Gantt, "Months 1–12", milestones, risk) | ❌ **dropped** | Proposal-only; never appears in a final dissertation |
| Ch.8 Conclusion ("Proposed Contributions", "Expected Outcomes") | Ch.7 Conclusion ✏️ | De-proposalise to accomplished work |
| Numbers hard-coded in prose | `\result{}` macros ← `data/*.csv` | The v2 bib gate |
| `references.bib` edited freely | human-gated; propose in `outlines/` | Bib gate |

## Publications & out-of-scope work

A "Publications During Candidacy" page lives in
`frontmatter/Publications.tex` (front matter, not a chapter; not gated), split
into two groups:

- **Forming this dissertation** — the three papers behind Chapters 4–6.
- **Other publications during candidacy** (acknowledged only, not chapters):
  - **onlycodes** — *"When Does Code-Execution Beat IDE Tools for Coding
    Agents?"* (KDD 2026 SE 3.0 workshop, non-archival). Software-engineering
    research, no information-theoretic tie to the spine.
  - **AAAI 2022** — *"Predictive Maintenance for General Aviation Using
    Convolutional Transformers"* (Yang, LaBella, Desell). Off-spine (time-series
    predictive maintenance); no source materials available, so not portable as a
    chapter regardless.

Decision (2026-06-03): both are **acknowledged only, not chapters** — including
off-spine work would weaken the unifying thesis. ~~TODO: fill author lists / exact
statuses.~~ **Done 2026-06-04** — all five entries have authors + venue/status in
`frontmatter/Publications.tex` (Ch.6 paper marked *In preparation, 2026*; Ch.5
paper *Under review, 2026*).

## Decisions locked (2026-06-03)

- **Title (revised 2026-06-04):** *"What Representations Preserve:
  Information-Theoretic and Geometric Conditions for Out-of-Distribution and
  Hallucination Detection."* Revised from the 2026-06-03 lock ("Information-Theoretic
  Approaches to…"): Ch.5 (DSC/TGT) is *geometric*, not information-theoretic, so the
  old umbrella mis-framed a third of the work. The **representation-structure**
  framing is the true unifying lens — both information theory (Ch.4, Ch.6) and
  geometry (Ch.5) are tools for asking what the representation preserves — and it
  covers all three chapters honestly. Subtitle retains both lenses + both task
  keywords for discoverability.
- **Spine:** failure → recovery → detection (above); "guaranteed failure" is
  Ch.4-specific.
- **Chapter order:** 4 Label Blindness → 5 DSC/TGT → 6 MI Hallucination → 7
  Conclusion (two OOD chapters adjacent, hallucination last).
- **Ch.5 title:** adopt the DSC / TGT naming.
- **onlycodes / AAAI 2022:** acknowledged in front matter, not chapters.

### Added 2026-06-04

- **Ch.6 framing: methodology/theory-led, not results-led.** The method matches
  but does not statistically beat the best learned baseline (ACT-ViT), and since
  ACT-ViT is *also* single-pass activation-space, the compute-efficiency result
  is a class-level point, not a differentiator. The chapter's claim is
  *parity-from-an-information-theoretic-first-principle* (parity = evidence the
  lens is right) plus the framework's self-validation (the confirmed
  symmetric-SupCon prediction; the 2×2 signal attribution). Verb stays
  **"matches-or-outperforms (in the mean)"**; the two NQ losses are reported, not
  hidden. See the Ch.6 entry above.
- **Appendix C confirmed — separate appendix, not folded.** Ch.6's
  information-theoretic proofs (Proposition C.1 + corollaries/lemmas, renumbered
  from the source paper's A.*) live in a dedicated **Appendix C**, parallel to
  App.A (Label Blindness) and App.B (DSC) — not folded into the Ch.6 body. See the
  Appendices section.
- **Ch.2 / Ch.3 kept separate.** Background & Definitions (Ch.2) and Literature
  Review (Ch.3) remain two distinct chapters, as in v1 (resolves Open Question 1).
- **Spine umbrella = representation structure.** The unifying lens is *what the
  representation preserves*; information theory (Ch.4, Ch.6) and geometry (Ch.5)
  are its two tools. Ch.1 §1.3 and the abstract must lead with this, not an
  info-theory-only umbrella.

## Open questions for you

1. ~~**Keep Ch.2 Background and Ch.3 Literature Review separate**, or merge into one
   "Background & Related Work" chapter?~~ **Resolved 2026-06-04: keep them split** —
   Ch.2 Background & Definitions and Ch.3 Literature Review stay as two separate
   chapters, as in v1.
2. ~~For the **two pending chapters**, keep the tentative section skeletons above as
   outline placeholders, or leave them empty until each chapter is drafted?~~
   **Resolved 2026-06-04: keep the skeletons** as placeholders / drafting checklist for now.
3. ~~**Title vs. spine coherence.**~~ **Resolved 2026-06-04: adopted option (c),
   the representation-structure umbrella** — new title *"What Representations
   Preserve: Information-Theoretic and Geometric Conditions for Out-of-Distribution
   and Hallucination Detection."* See the revised Title entry under Decisions
   locked. **Follow-ups:** (i) ✅ done — LaTeX `\degreetitle{}` updated in
   [`frontmatter/CoverPage.tex`](../frontmatter/CoverPage.tex) (propagates to all
   title-page variants via `\@degreetitle`); (ii) **still open** — §1.3
   (Methodology) and the abstract must lead with the representation-structure
   framing (both info theory and geometry as tools for "what the representation
   preserves"), not an info-theory-only umbrella.

## TODO — research tasks

- 🔜 **Literature currency sweep (before §3.3/§3.4 freeze).** The bib was seeded
  from v1 + the three source papers, so concurrent **2024–25** work may be
  under-covered. Find the 3–5 recent methods *per pillar* a committee would expect
  and that the bib lacks — hallucination (e.g. EigenScore/INSIDE, Lookback Lens,
  Haloscope, semantic-entropy follow-ups), OOD (e.g. GEN, NNGuide, fDBD). Scope:
  positioning only, not exhaustive; route any additions through the bib gate
  (propose → verify → apply). See [03_literature_review.md](03_literature_review.md) §6.
