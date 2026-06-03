# Paper Outline — EMNLP 2026 Submission

**Working title (provisional, 2026-05-20).** *Detecting Hallucinations with Contrastive Large Language Model Representations (CLLMR)*. Task-first framing puts "Detecting Hallucinations" in the first three words (mean-margin headline lead — Open Question 6 below; not the compute-efficiency lead, which is shared with ACT-ViT at K=1 and therefore non-differentiating). Method-name backronym `CLLMR` = *Contrastive Large Language Model Representations*, structurally echoing SimCLR (`chen2020simclr`).

**⚠ Naming-collision flag for CLLMR.** Web search 2026-05-20 surfaced [arXiv:2409.20052](https://arxiv.org/html/2409.20052) (Liu et al., updated April 2025) — "CLLMR" already in use as *Counterfactual Large Language Model Recommendation* in the recsys/causal-inference literature. Different subfield (recsys vs. hallucination detection), so reviewer-flag risk is low, but the cite-graph collision is permanent. Near-collision: [CLLMRec](https://arxiv.org/abs/2511.17041) (recsys, also 2025). Open Question 7 below tracks the *keep-CLLMR-anyway vs. switch* decision. Title and method-name are both **provisional until that resolves**; do not propagate `CLLMR` into prose, bib entries, or figure captions until the open question closes. Candidate alternatives if a switch is preferred: **LPCR** (Layer-Pair Contrastive Representations) and **CL²R** (Cross-Layer Contrastive Representations) — both encode the layer-pair structure that `CLLMR` does not; neither yet checked for collisions.

---

**🛑 Scope decision (2026-05-21) — MMLU is fully cut from the paper (treatment: silent omission).**

MMLU is **not** a dataset of this paper. The treatment is **silent omission in §4.2**: do not even mention MMLU in the dataset list. The writing agent must not:
- include MMLU in the §4.2 dataset list, the §5 main table, the §6 transfer table, the §5.3 compute-matched figure, or the §8 discussion;
- cite MMLU (Hendrycks et al. 2021) in §2 related work or anywhere else (do not add `hendrycks2021mmlu` to `references.bib`);
- import MMLU AUROC / transfer numbers from `paper/data/*.csv` via `\result` / `\resultPM` macros even if those CSVs contain MMLU columns or rows. The `build_numbers.py` aggregator must filter out MMLU rows so the macro paths stay MMLU-free;
- repeat the "MMLU-as-format-outlier" / "ViT-on-letter-token-activations" mechanism story from earlier drafts — those framings did not match the actual task implementation, and the cleaner reason is that **substring-match labeling degenerates on single-letter MCQ answer tokens** (the gold "A"/"B"/"C"/"D" matches anywhere in free-form responses, silently flipping labels). Rebuttal-ready analysis lives in [`appendix_candidates/mmlu_rebuttal.md`](appendix_candidates/mmlu_rebuttal.md) (not compiled into the PDF). If a reviewer asks "why no MMLU?", the human responds via rebuttal from that stash.

**Scope after the cut:** five datasets — **HotpotQA, NQ, PopQA, SciQ, SearchQA** — all free-form factual QA with substring-match labeling. The paper's framing becomes uniform on "free-form short-form factual QA" with no multi-choice cell. The §5.3 "MMLU shows K=1 only" caveat goes away; the §6.4 MMLU-exception paragraph goes away.

**Concurrent scope decisions (2026-05-21).**
- **ICR Probe descoped from §5.** Memmap coverage is only 3/6 datasets per model and the reproduction (0.49–0.76) is below the paper's headline (~0.80) due to a labeling-pipeline mismatch (not an architectural defeat). Treatment: **removed from §4.3 baseline list and §5.1 table**; **kept in §2 related work** as a methodology touchstone for the labeling-convention footnote.
- **SelfCheckGPT-BERT descoped from §5.** No results. Treatment: **removed from §4.3 sampling baselines and §5.1 supplementary-variants mention**. SelfCheckGPT-NLI (headline) and SelfCheckGPT-ngram (supplementary) stay; the `manakul2023selfcheckgpt` citation stays.

**Method inventory post-descope (10 methods, 2 model families, 5 datasets — the new grid is 2 × 5 × 10):**
- Output-space scalar (K=1, 3 methods): LogProb (seq), Token Entropy, P(true).
- Activation-space (K=1, 5 methods): Linear Probe, LLMsKnow Probe, SAPLMA, ACT-ViT, Contrastive+Recon (ours).
- Sampling (K=10, 4 methods): SE-length-norm (headline), SE-semantic (supp), SelfCheckGPT-NLI (headline), SelfCheckGPT-ngram (supp).

**Propagation.** This decision invalidates MMLU-bearing prose in [`04_experimental_setup.md`](04_experimental_setup.md) §4.2 / §4.3 / pending-approval list, [`05_results.md`](05_results.md) §5.1 / §5.2 / §5.3 / Open Q1+Q6, [`06_domain_transfer.md`](06_domain_transfer.md) §6.1–§6.4 / Open Q8 / cross-check #12, [`figures_outline.md`](figures_outline.md) Figure 5.3, and [`plan_taxonomy_sidestep.md`](plan_taxonomy_sidestep.md). The audit at the bottom of this file enumerates every line that must be edited. Sections §04 / §05 / §06 outlines have been swept on 2026-05-21 to drop MMLU + ICR + BERT references; remaining files (figures_outline, plan_taxonomy_sidestep) are flagged but not yet swept.

Target: 8-page long paper (Main or Findings). References + appendix unlimited.

Structural skeleton only. Each section lists what the prose will cover, not the prose itself. `[bracketed]` items mark spots where the author decides whether to import from planning docs.

**Reference coverage note.** The per-section outlines (`02_related_work.md`, `03_method.md`, `04_experimental_setup.md`) are the authoritative reference lists for their sections and may contain additional citations not enumerated here. This file summarizes structure and key anchors only — absence of a citation from this outline is not an inconsistency.

---

## Abstract (~180 words)

- One-sentence framing of the problem (LLM hallucination detection in a white-box single-pass regime against gold-reference labels).
- One-sentence statement of the method (learned contrastive compression of intermediate-layer activations with a logprob-recon auxiliary loss).
- One-sentence statement of the comparison classes (output-space scalar baselines, single-layer linear probe, MLP probe, sampling-based methods).
- One-sentence headline result naming the AUROC delta and the scope (two model families, five datasets, five seeds).
- One-sentence claim about transfer + layer-pair concentration (the cross-layer-coherence prediction).
- **Do not finalize until §6 numbers freeze** (week 3 of writing plan).

---

## 1. Introduction (~1 page)

- **The phenomenon.** LLMs hallucinate; the cost is asymmetric — wrong answers presented with high fluency are downstream-damaging.
- **The detection axis we work in.** White-box, single forward pass. Distinguish from: retrieval-augmented checking, multi-sample consistency methods, prompt-based self-evaluation.
- **What's already known about activations and hallucination.** A single layer carries some signal (linear-probe literature), but it's not clear which layer or what structure to extract.
- **Our contribution (3 bullets, paper-claim-aligned).**
  1. A learned contrastive compression of intermediate activations is competitive with or outperforms the strongest learned-activation baselines (single-layer linear probe, SAPLMA, LLMsKnow, ACT-ViT) and clearly outperforms sampling-based methods at matched compute. Exact verb (*beats* vs. *matches-or-outperforms*) and headline-cell selection finalize against the 2026-05-21 refreshed `draft_headline_table.md` — see Open Question 6.
  2. The signal is consistent across two model families, five datasets, and five training seeds, and transfers across datasets without retraining.
  3. The effective signal concentrates in mid-to-late residual-stream layer pairs, matching a cross-layer-coherence prediction.
- **Roadmap of the paper.** One paragraph.

---

## 2. Related Work (~0.75 page)

Detailed outline in [02_related_work.md](02_related_work.md). Summary structure (three subsections, ~3–4 references each):

- **2.1 Activation probing for LLM behavior.** Linear probes (Alain & Bengio), SAPLMA single-layer MLP (Azaria & Mitchell), ICR Probe per-layer-scalar MLP (Zhang et al. 2025), CLAP cross-layer attention (Suresh et al. 2025), ACT-ViT full-tensor ViT (Bar-Shalom et al. 2025), plus residual-stream truth-direction evidence (ITI, Marks & Tegmark). Sets our method up as a *learned* extension of probing rather than a replacement.
- **2.2 Hallucination detection.** Output-space scalars (Kadavath), multi-sample consistency (semantic entropy — Farquhar; SelfCheckGPT — Manakul), retrieval-augmented checking scoped out (FActScore — Min). Add one-sentence footnote: SEP (Kossen et al. 2024) trains a linear probe to predict SE; since we report both direct SE and linear probes on the same activations, SEP is covered by their union — not run as a standalone experiment.
- **2.3 Contrastive representation learning.** SimCLR (Chen et al.), InfoNCE (van den Oord et al.), SimCSE (Gao et al.); broad-novelty claim ships hedged with a footnote crediting CRD/CoDIR/CDS as adjacent machinery in different problem settings. Views here are layer pairs, not data augmentations or different networks.

End the section with one sentence positioning our work relative to the three threads.

---

## 3. Method (~2 pages)

Detailed outline in [03_method.md](03_method.md), which supersedes `methods_outline.md` and `theory_outline.md`. Summary structure:

- 3.1 Problem setup + notation
- 3.2 Why a learned cross-layer compression can carry the signal — the information-theoretic argument (folded in, not a standalone theory section)
- 3.3 What we built — supervised contrastive over layer pairs with logprob reconstruction (`ProgressiveCompressor`, layer-pair views, asymmetric `ignore_label` SupCon, logprob-recon auxiliary, KNN/cosine/Mahalanobis scorers, implementation summary)
- 3.4 What the method predicts — the 2×2 attribution table (SupCon-asymm × recon) with four pre-committed outcome-conditional framings

**Theoretical framing** is §3.2 (~half the section), with the full information-bound derivation in Appendix A. Budget is slightly above the original 1.5–2 page target because the theory is absorbed in-section; if the page budget binds, §3.4 collapses first into a single paragraph forwarding to §7.1.

---

## 4. Experimental Setup (~0.5–0.75 page)

- **Models.** Llama-3.1-8B-Instruct, Qwen3-8B. State why these two (open weights, two distinct training pipelines, 8B-scale).
- **Datasets.** HotpotQA, NQ, PopQA, SciQ, SearchQA. State per-dataset: task type, train/test sizes, evaluator used to label hallucinations, class imbalance ratio. (Movies excluded — no train split. MMLU silently omitted — see scope-decision flag at top of file.)
- **Baselines.** Three classes (10 methods total after the 2026-05-21 descope of ICR Probe and SelfCheckGPT-BERT):
  1. Output-space scalar (3): logprob, token entropy, P(true).
  2. Activation-space probes (5): single-layer linear probe (the "obvious" baseline), SAPLMA (~11M-param MLP, established literature baseline), LLMsKnow (Slobodkin et al. 2023, layer-wise probing baseline), ACT-ViT (Bar-Shalom et al. 2025, full-tensor ViT on activations), Contrastive+Recon (ours).
  3. Sampling-based (4): SE (length-normalized headline + semantic supplementary), SelfCheckGPT (NLI headline + n-gram supplementary).
  - **[TODO: one-sentence parry needed here]** Naive multi-layer concat is excluded from the baseline list; ACT-ViT is the principled learned multi-layer comparison and LLMsKnow covers layer-wise probing — add one sentence justifying the omission on compute/design grounds so reviewers don't flag it as an oversight.
- **Training procedure.** One paragraph: five seeds, cached activations reused across all methods, single 80 GB GPU per cell. Do not reproduce hyperparameters in prose — forward readers to the codebase on GitHub for full implementation details.
- **Metrics.** AUROC ± std across 5 seeds (main paper only). AUPRC, ECE, FPR@95 in supplementary tables.
- **Compute budget summary** (1–2 sentences; full breakdown in appendix).

---

## 5. Main Results (~1.5 pages)

- **5.1 Headline table.** AUROC ± std (across 5 seeds) for every (model, dataset, method) cell. State which cells the contrastive method wins, by how much, and where it does not.
- **5.2 Headline figure.** Per-dataset AUROC bars, both models, baseline cluster vs. ours.
- **5.3 Compute-matched comparison.** AUROC vs. forward-pass count. K=1 cluster: ours, linear probe, SAPLMA, P(true). K=10 cluster: SE (length-normalized), SelfCheckGPT-NLI. One panel per dataset for the five free-form datasets (HotpotQA, NQ, PopQA, SciQ, SearchQA).
- **5.4 Calibration.** Reliability diagrams for one dataset per model. ECE in supplementary.

Numbers freeze before this section is written. Until then, table/figure slots are reserved but blank.

---

## 6. Cross-Dataset Transfer (~0.5 page)

- **Procedure.** Train on dataset A, evaluate on dataset B's test split. No retraining, no fine-tuning. Both models. All ordered pairs.
- **Headline table.** 6×6 source→target AUROC heatmap per model. Off-diagonal mean + worst case in the body.
- **One paragraph of interpretation.** Where transfer breaks down and why.

---

## 7. Ablations (~1 page)

- **7.1 Loss decomposition.** SimCLR-only (AUROC ≈ 0.5, our negative result — this is itself a contribution) vs. logprob-recon-only vs. full loss. On 2 representative datasets, 5 seeds. The SimCLR-only cell coincides with **Variant 1** of §7.3 — one run, two ablations.
- **7.2 Layer-pair sensitivity.** Sweep early/mid/late layer pairs on 1–2 datasets. Connects directly to the theoretical framing in §3.3.
- **7.3 Contrastive variant — which side gets labeled.** Holds the recon auxiliary, architecture, layer pair, and scorer fixed; varies only how labels enter the contrastive loss. Four variants, on 2 representative datasets, 5 seeds:
  1. **Unsupervised contrastive (SimCLR over layer pairs).** `use_labels: false`. No label information — layer-pair views are the only positive-pair signal. **Early result: ~0.6 AUROC** — above chance but well below headline, confirming label information is necessary but not sufficient.
  2. **Hallucinations as outliers — truthful labeled, hallucinated unlabeled** *(headline; `use_labels: true, ignore_label: 1`)*. Truthful class is the coherent inlier cluster; hallucinated instances are required only to be view-consistent with themselves. This is the §3.3 / §5 configuration. **Early result: ~0.8 AUROC.**
  3. **Inverse — hallucinated labeled, truthful unlabeled** *(`use_labels: true, ignore_label: 0`)*. Hallucinated class treated as the coherent cluster; truthful instances ignored. **Early result: ≈ Variant 2 ±1 AUROC point** — varies by dataset/model but tracks the headline within noise. Implication: the *direction* of the one-class anchor does not strongly matter; what matters is that one class is unlabeled as the outlier role. The §3.3 "hallucinations are not a coherent class" framing needs revision — see §3.3 update below.
  4. **Symmetric SupCon — both classes labeled** *(`use_labels: true`, no `ignore_label`)*. Both classes pulled into their own coherent clusters; standard SupCon (`khosla2020supcon`). **Early result: drops ~10 AUROC points vs. Variant 2** (i.e., ≈ 0.7 AUROC) — worse than the one-class variants but still above unlabeled. This is a confirmed prediction of Corollary A.1.1: forcing `I(Z; C=1)` to be positive when class 1 lacks coherent latent structure adds gradient noise that actively fights the class-0 term. See [`03_method.md`](03_method.md) Theorems section.
  - **Preliminary ordering (early results, 2026-05-20): {2 ≈ 3} >> {4} > {1}.** Confirmed framing: **Variant 2 ≈ Variant 3 > Variant 4 > Variant 1.** Maps to the third pre-committed framing below — now effectively resolved pending final 5-seed runs.
  - **What this resolves.** Removes the §3.3 hedge ("we have not run and do not commit to running [symmetric SupCon]") and the symmetric-equivalent question raised in [`03_method.md`](03_method.md) Open Question 4. Pre-committed framings (for reference; early data points to the third):
    - **Variant 2 > {3, 4} ≈ Variant 1:** asymmetric `ignore_label=1` is doing the work; both the label-asymmetry *and* the choice of which side to anchor matter. Cleanest support for the current §3.3 prose. *Not supported by early results.*
    - **Variant 2 ≈ Variant 4 > {3, 1}:** any supervised contrastive over layer pairs works; the asymmetry is decorative. *Not supported — Variant 4 drops 10 points.*
    - **Variant 2 ≈ Variant 3 > Variant 4 > Variant 1:** *(early results point here)* the *asymmetry* helps but the *direction* doesn't; either class can serve as the one-class anchor. What is contraindicated is labeling *both* classes. §3.3 "hallucinations are not a coherent class" → revise to "labeling both classes simultaneously forces an incoherent second cluster that actively hurts." Variant 4's drop is a confirmed prediction of Corollary A.1.1, not just an empirical surprise.
    - **All four tied:** label structure of the contrastive loss is irrelevant; recon does all the work. *Not supported — large gaps between variants.*
- **7.4 Scorer choice.** Cosine vs. Mahalanobis vs. KNN. Justifies the KNN headline.
- **7.5 Alternative Augmetnations.** see https://github.com/hyang0129/HalluLens/issues/109
---

## 8. Discussion (~0.5 page)

- **Where the method works.** Mid-to-late layers, both model families, short-form free-form factual QA across all five evaluated datasets.
- **Where it doesn't.** Whatever the data shows — call it out honestly. Live candidates from the 2026-05-20 draft headline pass: NQ on both models (ACT-ViT modestly above ours, ~0.013–0.018 AUROC), several near-ties on HotpotQA / SciQ / SearchQA. Original risk-register candidates (Qwen weaker than Llama, SAPLMA parity) appear *not* to fire on current numbers but stay in the watch list until 5/5 seeds complete. Update this section after numbers freeze.
- **What the layer-pair concentration result means.** Brief — full theoretical argument in the appendix.

---

## 9. Limitations (~0.25 page)

- Two model families, 8B scale only. No 70B, no closed models.
- Short-form QA only. Long-form (FactScore-style) is out of scope.
- White-box. The method does not apply to API-only models.
- Single language (English). Multilingual is future work.

---

## 10. Conclusion (~0.25 page)

Three sentences, mirroring the abstract's claim. Do not finalize until the abstract is finalized.

---

## Appendix

- **A. Full theoretical derivation.** Cross-layer-coherence argument in full. Imported from `THEORETICAL_JUSTIFICATION.md` *only with explicit author sign-off per the paper-writing rule*.
- **B. Full hyperparameter table.** Every config in `configs/experiments/baseline_comparison_*.json`.
- **C. Full results tables.** Every (model, dataset, method, seed) cell, AUROC + AUPRC + ECE + FPR@95.
- **D. Dataset details.** Per-dataset evaluator prompts, class imbalance, split sizes, exact preprocessing.
- **E. Compute breakdown.** GPU-hours per phase per model.
- **F. Reproducibility checklist.** EMNLP-mandated artifact.

---

## File map for `paper/`

Each section below should eventually have its own file. Naming convention: `NN_section_name.md`.

| File | Status | Owner |
|---|---|---|
| `outline.md` | ✅ this file | — |
| `methods_outline.md` | ⚠️ superseded by `03_method.md` (delete after final review) | — |
| `theory_outline.md` | ⚠️ superseded by `03_method.md` §3.2 (delete after final review) | — |
| `00_abstract.md` | pending | freeze last |
| `01_introduction.md` | pending | week 1 |
| `02_related_work.md` | ✅ outline materialized (prose pending) | week 2 |
| `03_method.md` | ✅ outline materialized (prose pending; depends on §3.2 pending bib + Figure 1 source) | week 2 |
| `04_experimental_setup.md` | pending | week 2 |
| `05_results.md` | pending | week 3 (after numbers freeze) |
| `06_transfer.md` | pending | week 3 |
| `07_ablations.md` | pending | week 3 |
| `08_discussion.md` | pending | week 3 |
| `09_limitations.md` | pending | week 4 |
| `10_conclusion.md` | pending | week 4 |
| `appendix/` | pending | rolling |

---

## Open structural questions

1. ~~**Theory as §3 subsection vs. its own section.**~~ **Resolved 2026-05-19** — folded into §3 as §3.2 (information-theoretic argument), not promoted to a standalone Theory section. Rationale: the load-bearing theoretical move is short, structurally inseparable from the architecture, and the 8-page EMNLP main paper does not have room for a dedicated theory section. Full information-bound derivation lives in Appendix A. See [`03_method.md`](03_method.md) structural-decision header. Soft commit revisable post-internal-review.
2. ~~**Where does SEP-binary / SEP-SE land in §5?**~~ **Removed** — SEP-binary was a confabulation; SEP-SE cut 2026-05-20. Both upper-bounded by max(SE, linear probe), already reported. Defused with a one-sentence footnote in §2.2.
3. **Headline framing across model families.** Preliminary numbers (2026-05-20 draft headline table) suggest Qwen tracks slightly *above* Llama on most cells (mean ours: Qwen ≈ 0.85, Llama ≈ 0.81 — `[TEMP — re-verify from headline_results.csv over the five paper datasets, MMLU excluded]`), inverting the original "what if Qwen is materially weaker" worry. The opposite framing question is now live — whether the abstract leads with Qwen, leads with Llama, or treats both symmetrically. Don't pre-commit; revisit once `headline_results.csv` lands (MMLU-filtered).
4. **§2.3 novelty-claim level — broad / medium / narrow.** Resolved 2026-05-19 to **broad with hedging** (see `02_related_work.md` §2.3 framing-level decision). Reviewer-rebuttal fallback to medium then narrow is documented there. Abstract and §1 contribution claims must be drafted to the broad level once §3 / §5 freeze.
5. **§3.4 attribution headline — locked when #66 (SupCon-asymm only) and #67 (SAPLMA + recon) land.** Until then, §3.4 prose is the *menu* of four outcome-conditional framings. The headline framing of §3 and the abstract cannot finalize until these resolve. See [`03_method.md`](03_method.md) §3.4. **Related:** the §7.3 contrastive-variant ablation (added 2026-05-20) now also bears on §3.3's load-bearing "asymmetric `ignore_label`" claim — Variant 4 (symmetric SupCon) is the run §3.3 previously declined to commit to. §3.3 prose stays hedged until Variants 2/3/4 land.
6. **ACT-ViT as the primary learned competitor.** Per the 2026-05-21 draft headline pass ([`../results/draft_headline_table.md`](../results/draft_headline_table.md), all ACT-ViT cells now 5/5 seeds), ACT-ViT is materially closer than the original outline implied. Mean across both models on the five retained datasets: ours ≈ 0.83 vs. ACT-ViT ≈ 0.79. Win pattern concentrates in PopQA (~+0.09 both models) and SciQ (Qwen large, Llama close). On HotpotQA / SearchQA the two methods sit within ±0.03; on NQ ACT-ViT is modestly ahead on both models. **Lead-framing decision (2026-05-21):** of the two remaining live framings — mean-margin / parameter-or-compute-efficiency-at-matched-AUROC — the working choice is **mean-margin**, because (a) theory is the slim half of §3 and cannot anchor the headline, and (b) compute-efficiency is shared with ACT-ViT (also K=1 activation-space) and therefore non-differentiating against the strongest learned competitor. The third framing previously on the menu ("PopQA-and-MMLU-headline-cells") is **dropped** with the MMLU cut; the new headline-cells anchor is **PopQA + SciQ** (clean wins on both models). ACT-ViT 5/5 seed sweep resolved (was outstanding on 2026-05-20 draft; closed on 2026-05-21 per refreshed `results/draft_headline_table.md`). Implications: (a) the §1 contribution verb against learned baselines can now lock against final numbers; (b) the §1 / §8 / abstract framing all assume the mean-margin lead; (c) an interpretation question remains open: ACT-ViT-vs-ours wins concentrate on already-high-AUROC datasets (PopQA is the highest-AUROC cell on the table), not on the hardest-to-detect ones (NQ) — does our method *push the ceiling* or *recover the floor*? Decide in §8 after numbers freeze.

7. **CLLMR naming collision — keep or switch.** Working title (top of outline) uses `CLLMR` = *Contrastive Large Language Model Representations* as the method-name backronym, echoing SimCLR (`chen2020simclr`). 2026-05-20 web search surfaced a permanent cite-graph collision with Liu et al., [arXiv:2409.20052](https://arxiv.org/html/2409.20052) (recsys / causal inference), and a near-collision with [arXiv:2511.17041 CLLMRec](https://arxiv.org/abs/2511.17041). Subfield distance makes reviewer-flag risk low but Google Scholar / arXiv search confusion permanent. Options: (a) **keep CLLMR** (status quo; brand-first, ties cleanly to SimCLR, accepts cross-subfield search collision); (b) **switch to LPCR** = *Layer-Pair Contrastive Representations* (additionally encodes the layer-pair-view structure that §3.3 makes load-bearing; collision-check pending); (c) **switch to CL²R** = *Cross-Layer Contrastive Representations* (most distinctive visually, but the superscript reads awkwardly in plain-text contexts including BibTeX keys and grep). Decision blocker: human needs to weigh cite-graph search-uniqueness vs. SimCLR-shape brand recognition. Until resolved, do **not** propagate `CLLMR` into prose, bib entries, or figure captions; references in this outline and in [`05_results.md`](05_results.md) carry the provisional flag.

---

## Bibliography state (as of 2026-05-19)

All §2 anchor citations and §3 load-bearing citations are in [`references.bib`](references.bib). Most recent additions: `khosla2020supcon`, `poole2019variational`, `wang2021understanding`, `tishby2015deep`, `hjelm2019deepinfomax` (all five for §3.2/§3.3, human-approved 2026-05-19 from the verification pass in [`03_method.md`](03_method.md) pending-approval section). The only candidates that are *not* in `references.bib` are the four §2 optionals (Hewitt & Manning, Tenney et al., Ji et al., Lewis et al. RAG) — verified 2026-05-19, defer insertion until a draft surfaces a gap.

MMLU citation (`hendrycks2021mmlu`) — **do not add to `references.bib`** per the 2026-05-21 scope-decision flag at the top of this file. The candidate entry in [`04_experimental_setup.md`](04_experimental_setup.md) §4 References (`Hendrycks et al., ICLR 2021, arXiv:2009.03300`) should be removed when §4.2 is cleaned.

---

## Audit — MMLU mentions in `paper/` (as of 2026-05-21 scope decision)

Every line below mentions MMLU and must be removed or rewritten when its section is next edited. Lines are grouped by file; the column **action** records the resolution sketch.

**Phase-1 sweep status (2026-05-21):**
- ✅ `outline.md` — cleaned (this file).
- ✅ `04_experimental_setup.md` — cleaned: dataset bullet deleted, framing rewritten, pending-approval entry removed, ICR Probe + SelfCheckGPT-BERT also descoped per concurrent decisions.
- ✅ `05_results.md` — cleaned: column dropped, ICR Probe row treatment removed, MMLU footnote struck, BERTScore mention dropped, ACT-ViT 5/5 banner updated, clean-wins reframed to PopQA + SciQ.
- ✅ `06_domain_transfer.md` — cleaned: rows/columns dropped, MMLU narrative struck, transfer count re-tallied (8/0/0 reportable wins post-MMLU), Open Q8 deleted.
- ⏳ `figures_outline.md`, `plan_taxonomy_sidestep.md` — NOT yet swept; the audit rows below remain authoritative for those two files.
- ⏳ `sections/01_intro.tex`, `templates/tab_baseline.tex.template`, `figures_src/render_transfer.py` — NOT yet swept; these still flow into the rendered PDF and are the priority for Phase-2 cleanup.

### `04_experimental_setup.md` (six hits)

| Line | Context | Action |
|---|---|---|
| 34 | §4.2 framing sentence — "Six short-form QA / reasoning benchmarks … broad multi-domain multiple-choice (MMLU)" | Rewrite as "Five short-form QA benchmarks spanning open-domain factoid (NQ, PopQA, HotpotQA, SearchQA) and science multiple-choice (SciQ)." Drop the "multi-domain multiple-choice (MMLU)" clause. |
| 40 | §4.2 full MMLU bullet ("Multi-domain multiple-choice (57 subjects, four options). Exact-match evaluator …") | Delete the entire bullet. |
| 47 | §4.2 wrap-up — "knowing exactly *what* the six datasets are and *why* MMLU is the one cell missing from the §5.3 sampling-baselines comparison" | Rewrite — five datasets, no missing cell story. |
| 73 | §4.3 SE bullet — "Five free-form datasets only (MMLU excluded — NLI clustering degenerates on single-letter answer tokens)" | Rewrite — SE runs on all five datasets; drop the parenthetical exclusion clause. |
| 135 | Open-questions §4 list — "Nine pending-approval citations … six dataset citations (HotpotQA, NQ, MMLU, PopQA, SciQ, SearchQA)" | Adjust counts: now five dataset citations, eight pending overall. |
| 230, 232 | Pending-approval candidates — Hendrycks et al. 2021 MMLU entry, "Would buy. The §4.2 MMLU bullet." | Delete both lines (the entry and its consumer). |

### `05_results.md` (eleven hits)

| Line | Context | Action |
|---|---|---|
| 27 | §5.1 table layout — column order "HotpotQA, NQ, MMLU, PopQA, SciQ, SearchQA" | Drop MMLU column; reorder to five datasets. |
| 29 | Reporting unit — "five such cells (all ACT-ViT: Llama MMLU 2/5, …, Qwen MMLU 2/5, Qwen SearchQA 2/5)" | Remove the two MMLU cells; three outstanding (Llama-SearchQA, Qwen-HotpotQA, Qwen-SearchQA). |
| 34 | Per-cell honesty — "ours wins clearly … on PopQA and MMLU on both models" | Drop MMLU from the clean-win list. |
| 36 | Cell-by-cell narrative template — "two clean wins (PopQA / MMLU, both models … `+0.005 to +0.010` over LLMsKnow on MMLU)" | Reduce to one clean-win cluster (PopQA) or rewrite around it. |
| 38 | MMLU footnote — "ACT-ViT under-performs every other activation-space probe on MMLU … ViT-on-letter-token-activations limitation" | Delete the entire MMLU-footnote bullet. |
| 40 | ICR Probe row treatment — "the cells we have (NQ, MMLU, PopQA on both models …)" | Remove MMLU from the cells-we-have list. |
| 42 | Supplementary cells — "LogProb-seq and Token-Entropy have Llama-MMLU 1/5 seeds and nothing else" | Reframe — without MMLU, LogProb-seq/Token-Entropy have *no* reportable cells; either drop these rows from the supplementary table or note that data is unavailable. |
| 58 | Annotation arrows — "MMLU-Llama ours-vs-LLMsKnow `+0.010`" | Drop the MMLU-Llama annotation. |
| 74 | §5.3 figure type — "5 panels: HotpotQA, NQ, PopQA, SciQ, SearchQA — MMLU excluded per §4.3 sampling-baseline scope decision" | Drop the parenthetical exclusion clause; the five-panel layout stays. |
| 117 | Open Q1 — "Llama MMLU 2/5, Llama SearchQA 3/5, Qwen HotpotQA 3/5, Qwen MMLU 2/5, Qwen SearchQA 2/5" | Drop both MMLU entries; three outstanding. |
| 127 | Open Q6 (headline-framing menu) — "(ii) PopQA/MMLU-headline-cells story … PopQA / MMLU per-cell margins are too small to lead with" | Drop framing (ii) entirely; menu reduces to (i) mean-margin and (iii) compute-efficiency. (`outline.md` Open Q6 already cleaned in this commit.) |

### `06_domain_transfer.md` (twelve hits)

| Line | Context | Action |
|---|---|---|
| 59 | §6.2 table layout — row ordering "HotpotQA, NQ, MMLU, PopQA, SciQ, SearchQA" | Drop MMLU row; reorder to five sources. |
| 69, 80 | Table cells — "MMLU 0.671 0.675 ACT-ViT −0.003 (tied)" and "MMLU 0.648 0.663 ACT-ViT −0.016 (loss)" | Delete both rows. |
| 86 | Claim 1 — "Across the 10 (model × source) cells … ours wins **8**, ties **1** (Llama-MMLU within ±0.005), and loses **1** (Qwen-MMLU, −0.016)" | Recount: with MMLU gone, the cells re-tally to **8 cells, ours wins 8 (or 7 + NQ pending)**. Rewrite the headline sentence. Both non-wins were MMLU; removing them eliminates the only ties/losses on this axis, which strengthens claim 1 — verify the count once `06_domain_transfer.md` §6.2 is edited. |
| 87 | Claim 2 — "the strongest baseline is ACT-ViT on HotpotQA, MMLU, SciQ-Llama, PopQA-Qwen" | Drop MMLU from the ACT-ViT list. |
| 88 | Claim 3 — "MMLU as source is a structural exception, not a counterexample" | Delete the entire claim-3 bullet. (Without MMLU non-wins, no exception to explain.) |
| 90 | Cell-by-cell narrative — "name MMLU as the one source where transfer is flat for every method" | Drop step (3) from the template; renumber. |
| 94 | §6.2 wrap-up — "The §8 discussion's lead into the MMLU-as-format-outlier story" | Drop the MMLU-format-outlier forward; §6.2 no longer feeds anything into §8 on this axis. |
| 137 | §6.4 MMLU exception bullet — "The MMLU format (multiple-choice, single-letter completion) produces an activation pattern that none of the four methods transfers out of" | Delete the entire bullet. |
| 143 | §6 wrap-up — "The §8 NQ-shortfall + MMLU-format-outlier discussion picks up §6.4" | Drop "+ MMLU-format-outlier". |
| 189 | Open Q8 — "MMLU-as-source interpretation (cross-section consistency) … §5.1's MMLU footnote characterizes ACT-ViT's MMLU performance as a ViT-on-letter-token-activations limitation" | Delete the entire Open Q8 entry; renumber. |
| 209 | §6 cross-section forwards — "§6.4 forwards the MMLU-as-format-outlier and NQ-as-target shortfall stories to §8" | Drop "MMLU-as-format-outlier"; keep NQ. |
| 255 | Cross-check #12 — "Cross-check §6.4 MMLU framing against §5.1 MMLU footnote and §8 MMLU discussion" | Delete the entire cross-check #12; renumber. |

### `plan_taxonomy_sidestep.md` (three hits)

| Line | Context | Action |
|---|---|---|
| 22 | Framework — "Closed-book QA against gold references (HotpotQA, NQ, PopQA, SciQ, SearchQA, MMLU)" | Remove MMLU from the list (five datasets). |
| 138 | Per-dataset stance — "[04_experimental_setup.md, all six datasets (HotpotQA, NQ, PopQA, SciQ, SearchQA, MMLU)]" | Adjust to "all five datasets" and drop MMLU. |
| 177 | Note 2 — "The MMLU footnote (§5.1 line 38) notes ACT-ViT limitation neutrally" | Delete the entire note 2; renumber. |

### `figures_outline.md` (one hit)

| Line | Context | Action |
|---|---|---|
| 21 | Figure 5.3 content — "One panel per free-form dataset (HotpotQA, NQ, PopQA, SciQ, SearchQA). MMLU shows K=1 cluster only." | Delete the trailing "MMLU shows K=1 cluster only" sentence; figure already correctly enumerates the five free-form panels. |

### Live LaTeX / figure-rendering sources (three hits — these compile into the actual PDF)

These are **higher priority** than the planning-markdown hits above because they currently produce paper output. The intro section currently asserts an MMLU AUROC number; the baseline table template currently emits an MMLU row; the transfer figure currently plots an MMLU bar. None of these can survive the cut.

| File | Lines | Context | Action |
|---|---|---|---|
| [`sections/01_intro.tex`](sections/01_intro.tex) | 22–27 | "trained on HotpotQA and evaluated on **five additional datasets** without re-training, achieving a mean AUROC of `\result{baseline_comparison}{mmlu:icr_probe:auroc:mean}[3]` **on MMLU** and …" | Drop the MMLU clause and the `\result{...mmlu...}` macro call. The "five additional datasets" count becomes **four** if HotpotQA is the source. Re-verify the count after the prose is edited — the intro also says "six LLMsKnow tasks" at line 35, which becomes **five** post-cut. |
| [`sections/01_intro.tex`](sections/01_intro.tex) | 35 | Contribution (2): "A reproducible benchmark suite covering **six LLMsKnow tasks**." | Change "six" → "five". |
| [`templates/tab_baseline.tex.template`](templates/tab_baseline.tex.template) | 12–14 | Generated baseline table row: `MMLU & \result{baseline_comparison}{mmlu:icr_probe:auroc:mean}[3] & \result{baseline_comparison}{mmlu:selfcheck:auroc:mean}[3]` | Delete the three-line MMLU block. Table reduces to five rows (HotpotQA, NatQ, PopQA, SciQ, SearchQA). Re-run `make values` after edit to regenerate `generated/tab_baseline.tex` without the MMLU row. |
| [`figures_src/render_transfer.py`](figures_src/render_transfer.py) | 39, 47 | `DATASETS_ORDER` includes `"mmlu"`; `DATASET_LABELS["mmlu"] = "MMLU"` | Remove `"mmlu"` from `DATASETS_ORDER` (line 39) and the `"mmlu": "MMLU"` entry from `DATASET_LABELS` (line 47). Re-run the figure build to regenerate the PDF and sidecar without the MMLU bar. Verify no downstream caption text in the consuming `.tex` references the MMLU bar by name. |

### `data/` and `generated/` — leave the CSVs alone, just don't dereference

| Path | Status | Action |
|---|---|---|
| [`data/baseline_comparison.csv`](data/baseline_comparison.csv) | Contains MMLU rows (the CSV is the source of truth for whatever numbers the macros consume) | **No edit.** Per [`paper/CLAUDE.md`](CLAUDE.md), `data/*.csv` is the single source of truth for cited numbers; we do not surgically delete CSV rows. The contract is that no surviving `\result{...mmlu...}` macro call exists in the rendered paper after the audit above is cleared. The MMLU CSV rows become orphaned but harmless. |
| `generated/figures/*.numbers.csv` | Auto-generated sidecars may list MMLU values | Auto-regenerate by running the figure pipeline after the `render_transfer.py` edit. |

### Files with **no** MMLU mentions (no edits needed)

- [`02_related_work.md`](02_related_work.md) — no MMLU references; the §2 anchor citations are already MMLU-free.
- [`03_method.md`](03_method.md) — no MMLU references.
- [`inconsistencies.md`](inconsistencies.md) — no MMLU references after the 2026-05-21 revert.
- [`main.tex`](main.tex), [`macros.tex`](macros.tex), [`Makefile`](Makefile), [`build_numbers.py`](build_numbers.py), [`lint.py`](lint.py), [`references.bib`](references.bib), [`README.md`](README.md) — no MMLU references on the 2026-05-21 grep pass.

**Total touch points after `outline.md` itself:** 33 lines across five planning-markdown files + four blocks across three live-source files (intro tex, table template, transfer figure renderer). The live-source hits are the priority because they currently flow into the rendered PDF.
