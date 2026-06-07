# Chapter 6 — Information-Theoretic Hallucination Detection · port plan

Plan for porting the paper *"Detecting Hallucinations via Mutual Information
Analysis of Intermediate Layer Activations"* (HalluLens, EMNLP 2026 submission)
into Ch.6. Companion to [00_dissertation_outline.md](00_dissertation_outline.md)
(Ch.6 entry, lines 186–252) and [03_literature_review.md](03_literature_review.md)
(§4 RW scope). Source tree:
[`../sources/hallulens_mi_hallucination/`](../sources/hallulens_mi_hallucination).

**Status:** ⬜ not yet drafted (`chapters/06_hallucination_detection.tex` is a
7-line stub; `appendices/C_mi_proofs.tex` does **not** exist yet). All phases
below are pending — unlike Ch.5, **no** number-gate work is done.

**Not Ch.4, not Ch.5.** Ch.4 ported a *dissertation* chapter (matching keys, one
printed table). Ch.5 ported a *conference paper* with a foreign number system.
Ch.6 is the easiest mechanically but the trickiest editorially: its source
**already uses the v2 bib-gate build system** (v2's `build_numbers.py` /
`\result{}` macros were adapted from this paper's), so CSVs and macros drop in
almost directly — but the source content lives in **markdown drafts**
(`02_…md`–`06_…md`, ~195 KB), not finished `.tex`, and the chapter must be
**re-ordered method-first** from the paper's results-first layout.

## Decisions (2026-06-06)

- **Method-led, not results-led** (locked 2026-06-04, master outline). The method
  matches but does **not** statistically beat the best learned baseline (ACT-ViT),
  and ACT-ViT is *also* single-pass activation-space, so the compute-efficiency
  win is a *class-level* point, not a differentiator. The chapter's claim is
  **parity-from-an-information-theoretic-first-principle** (parity = evidence the
  lens is right) + the framework's **self-validation** (confirmed symmetric-SupCon
  prediction; 2×2 signal attribution). Promote Method + the info-theoretic
  argument; do not bury it after Results.
- **Verb is locked: "matches-or-outperforms (in the mean)."** Never "beats" /
  "state-of-the-art." Same verb in §1 contribution, abstract, and Ch.6 Results
  prose (cross-section consistency rule). **The two NQ losses are reported, not
  hidden.**
- **Honesty discipline carries over.** Bolding rule: bold a cell **only** when it
  beats the runner-up by **> max std**. The headline read is "wins 3 clearly
  (Llama-PopQA, Qwen-PopQA, Qwen-SciQ), ties ~3, loses ~4 (both NQ firm)" — verify
  the tally against the gated CSV once §6.5 prose locks.
- **`baseline_comparison.csv` is STALE — do NOT port.** Its header is
  `source_commit: placeholder`, it references `mmlu` / `natural_questions` /
  `icr_probe` (all dropped or renamed), and its numbers do not match
  `headline_results.csv`. The live headline table is `headline_results.csv`. MMLU
  was dropped from the paper 2026-05-21; ICR Probe and SEP-SE were **cut as
  baselines** (reproducibility failure / superseded by ACT-ViT — see source
  `inconsistencies.md` I-1/I-2). ICR Probe survives only as a **cite-only**
  touchstone in §6.2 RW.
- **Main-paper metric is AUROC ± std only** (across 5 seeds). AUPRC / ECE / FPR@95
  → supplementary / arXiv (source `inconsistencies.md` I-6). Do not gate them.
- **Method name = "Contrastive+Recon"** (full) / "contrastive probe" (short).
  **Never "ICR-probe"** — that is the cut *baseline* (Zhang et al.); the source's
  `sections/01_intro.tex` stub still says "ICR-probe" (stale, I-9) — do not carry.
- **DSC/Ch.2 boundary unchanged:** Ch.6 owns the one-class layer-pair construction
  and the cross-layer-MI argument; Ch.2 §2.6/§2.7 own DPI + the InfoNCE/variational
  bound primitives (back-ref, don't re-derive).

---

## 1. Section map (source markdown → Ch.6, RE-ORDERED method-first)

The paper's markdown is numbered RW→Method→Setup→Results→Transfer. The chapter
**promotes Method ahead of Results** per the method-led decision.

| Source md | → | Ch.6 § | Action |
|---|---|---|---|
| `01_intro` stub + master-outline framing | | 6.1 Introduction | write fresh; **state parity-as-validation up front**; fix the "ICR-probe"→"Contrastive+Recon" name |
| `02_related_work.md` (§2.1 activation probing · §2.2 hallucination detection · §2.3 contrastive repr.) | | 6.2 Related Work | **tighten**; back-ref Ch.3 §3.1 (info theory), §3.2 (contrastive), §3.4 (taxonomy/eval). Host the §2.3 novelty claim (layer-pair one-class vs CRD/CoDIR/CDS). ICR Probe cite-only. |
| `03_method.md` (§3.1 setup · §3.2 info-theoretic argument · §3.3 the method · §3.4 the 2×2) | | 6.3 Method + Information-Theoretic Argument | **the conceptual core — promote, do not bury.** Feasibility-by-trainability; one-class asymmetric `ignore_label`; the 2×2 menu. Thm/Prop **statements** here; proofs → App.C. |
| `04_experimental_setup.md` (§4.1 models · §4.2 datasets · §4.3 baselines · §4.4 training · §4.5 metrics) | | 6.4 Experimental Setup | port; 2 models × 5 datasets × 12 methods; AUROC±std only main; one-paragraph training (forward to GitHub for hyperparams, I-7) |
| `05_results.md` (§5.1 headline · §5.3 compute-matched · §5.4 calibration) | | 6.5 Results | parity table read **honestly** (NQ shortfall named); bolding rule |
| `05_results.md` §5.3 | | 6.6 Compute-Matched Comparison | present as motivation for the activation-reading **class**, with the **ACT-ViT caveat** stated (not a differentiator vs the real competitor) |
| `03_method.md` §3.4 + §7.3 ablation (Variant 1–4) | | 6.7 Ablations / Signal Attribution | lead with the **confirmed symmetric-SupCon prediction** (Variant 4 ≈ −10 AUROC) — the strongest empirical-of-theory moment; then the 2×2 contrastive-vs-logprob-recon attribution |
| `06_domain_transfer.md` (§6.2 per-source · §6.3 in/out aggregate · §6.4 interp) | | 6.8 Domain Transfer | per-source transfer table (main) + in/out-domain aggregate (supporting) |
| `99_limitations` stub + master outline | | 6.9 Limitations | NQ shortfall; parity-not-dominance; ICR/ECE/FPR95 scoped out |
| `03_method.md` "Theorems to be added" | | **Appendix C** (`app:mi-hallucination-proofs`) | renumber A.* → C.* (see §4) |

## 2. Number-gate port inventory

The source already speaks the v2 gate (`\result{stem}{key}` ← `data/*.csv`).
**Re-namespace each CSV stem with a `hallu_` prefix** to avoid colliding with the
DSC/label-blindness CSVs already in `data/`, fold into `v2/data/`, preserve the
provenance header, then rebuild the `\result` tabulars per cell (never `\input`
a source tabular — sources/README rule #1).

| Source CSV | → v2 stem | key_schema | value cols | port? |
|---|---|---|---|---|
| `headline_results.csv` | `hallu_headline` | `model:dataset:method` | `auroc_mean,auroc_std,n_seeds,forward_pass_count` | **YES — the headline table (120 cells: 2 models × 5 datasets × 12 methods)** |
| `transfer_per_source.csv` | `hallu_transfer_per_source` | `model:method:source` | `auroc_mean,auroc_std` | YES — §6.8 main (Option E) |
| `transfer_summary.csv` | `hallu_transfer_summary` | `model:method:scope` (`in_domain`/`out_of_domain`) | `auroc_mean,auroc_std` | YES — §6.8 supporting (Option B) |
| `transfer_matrix.csv` | `hallu_transfer_matrix` | `model:method:source:target` (5×5) | `auroc_mean,auroc_std` | OPTIONAL — full matrix; supplementary/arXiv unless §6.8 wants the heatmap |
| `datasets.csv` | `hallu_datasets` | `dataset` | sizes/%-hallucinated **all empty** | LOW — port only if §6.4 needs a dataset table; values are TBD/blank now |
| `baseline_comparison.csv` | — | — | — | **NO — STALE (see Decisions); delete from consideration** |

- **Methods (12):** output-space scalar — `logprob_baseline`, `token_entropy`,
  `p_true`; activation probes — `linear_probe`, `saplma`, `llmsknow_probe`,
  `act_vit`, **`contrastive_logprob_recon`** (ours); sampling —
  `se_length_normalized`, `se_semantic_entropy`, `selfcheck_nli`,
  `selfcheck_ngram`. `forward_pass_count` column drives the compute-matched §6.6
  argument (ours/ACT-ViT = 1; p_true = 2; sampling = 10).
- **Models (2):** `Llama-3.1-8B-Instruct`, `Qwen3-8B`. **Datasets (5):** hotpotqa,
  nq, popqa, sciq, searchqa.
- **Headline read to preserve (verify against gated CSV):** ours vs ACT-ViT per
  (model×dataset) — clear wins PopQA (both) + SciQ-Qwen; firm losses NQ (both);
  rest ties. → "matches-or-outperforms (in the mean)."
- **Deltas/ratios** for §6.6 compute prose → `\resdelta{hallu_headline}{…sampling key}{…ours key}`.

## 3. Citation reconciliation

Source `references.bib` has **26 keys**; the §4 setup adds dataset/model/baseline
candidates. Three buckets:

### 3a. Already in the gated bib — direct match (21)
`alain2017understanding, azaria2023internal, bang2025hallulens,
barshalom2025actvit, belinkov2019analysis, chen2020simclr, gao2021simcse,
ji2022survey, kadavath2022language, kossen2024semantic, li2023iti,
manakul2023selfcheckgpt, marks2024geometry, min2023factscore,
poole2019variational, sun2020codir, suresh2025clap, tian2020crd, tishby2015deep,
wang2021understanding, zhang2022cds, zhang2025icr` — substitute as-is. (Note
ACT-ViT/CLAP/ICR + CRD/CoDIR/CDS adjacent-machinery are **all already present** —
no gate work for the novelty footnote.)

### 3b. Remap — same paper, different gated key (5; confirmed by title)
| Source key | gated key |
|---|---|
| `khosla2020supcon` | `khosla2020supervised` |
| `oord2018cpc` | `oord2018representation` |
| `hjelm2019deepinfomax` | `hjelm2019learning` |
| `farquhar2024semantic` | `farquhar2024detecting` |
| `kwiatkowski2019nq` | `kwiatkowski2019natural` |

### 3c. Genuinely missing — **bib-gate additions needed** (7; propose in `outlines/`, human-approve before insert)
All are standard dataset/model/baseline papers (verify arXiv/venue, then gate):
| Proposed key | Paper |
|---|---|
| `grattafiori2024llama3` | Grattafiori et al., *The Llama 3 Herd of Models*, arXiv:2407.21783 |
| `yang2025qwen3` | Yang et al., *Qwen3 Technical Report*, 2025 (verify preprint/venue) |
| `yang2018hotpotqa` | Yang et al., *HotpotQA*, EMNLP 2018, arXiv:1809.09600 |
| `mallen2023popqa` | Mallen et al., *When Not to Trust LMs* (PopQA), ACL 2023 |
| `welbl2017sciq` | Welbl et al., *Crowdsourcing Multiple Choice Science Questions* (SciQ), W-NUT 2017, arXiv:1707.06209 |
| `dunn2017searchqa` | Dunn et al., *SearchQA*, arXiv:1704.05179 |
| `orgad2024llmsknow` | LLMsKnow baseline — **Orgad et al.**, *LLMs Know More Than They Show*, ICLR 2025, arXiv:2410.02707 (repo `technion-cs-nlp/LLMsKnow`). ✅ verified 2026-06-06; corrects the source's wrong "Slobodkin et al." guess (I-5). |

NQ is **not** a new entry — it remaps to `kwiatkowski2019natural` (3b). So the gate
list is exactly these 7. **✅ All 7 applied to `references.bib` 2026-06-06
(192→199); web-verified; staging at
[bib_staging_ch6_2026-06-06.md](bib_staging_ch6_2026-06-06.md).**

## 4. Proofs → Appendix C (`app:mi-hallucination-proofs`)

Port `03_method.md` "Theorems to be added". **Renumber A.* → C.*** (Appendix A is
Label Blindness — the paper's `A.1/A.2/A.3` collide). Drafting order **lemmas
first** (C.2 → C.3 → C.1), per the source's own recommendation:

- **Lemma C.2** (was A.2) — DPI chain in our notation (~3 lines).
- **Lemma C.3** (was A.3) — InfoNCE variational bound restated (Poole-tightened);
  cites `oord2018representation` + `poole2019variational`. Plugs into C.1.
- **Proposition C.1** (was A.1) — **the only non-off-the-shelf result.** Asymmetric
  SupCon bounds label-conditioned MI on the inlier/truthful class. Combines the
  SupCon→MI bound (`khosla2020supervised`) with the `ignore_label=1` asymmetry.
  Proof starts from Lemma C.3.
- **Corollary C.1.1** (was A.1.1) — symmetric SupCon contraindicated when one class
  lacks coherent latent structure. **The confirmed ≈−10-AUROC prediction**
  (Variant 4). ~2 paragraphs off the C.1 decomposition.
- **Corollary C.2.1** (was A.2.1) — cross-layer/response co-information under
  downward determinism: `I(h_a;h_b;y)=I(h_b;y)>0`. Follows from Lemma C.2.

Keep statements in §6.3 with `\ref{app:mi-hallucination-proofs}` pointers (mirrors
Ch.4→App.A, Ch.5→App.B). **Create `appendices/C_mi_proofs.tex`** and wire it into
`main.tex` (App.A/B are already wired; C is new). Budget ≤ 1 page.

## 5. Transform checklist (mirrors Ch.4/Ch.5)

1. **Number gate (CSVs)** — copy + `hallu_`-namespace `headline_results`,
   `transfer_per_source`, `transfer_summary` (+ optional `transfer_matrix`,
   `datasets`) into `v2/data/` with provenance headers; rebuild `\result`
   tabulars. **Drop `baseline_comparison.csv` (stale).**
2. **Cite remap + gate** — apply §3b remaps; propose the §3c 7 new entries through
   the bib gate (human sign-off) before drafting `.bib`-dependent prose.
3. **Re-order method-first** — §1 map; promote Method ahead of Results.
4. **RW tighten** — §6.2 back-refs Ch.3 §3.1/§3.2/§3.4; no re-survey (03 §4 Ch.6 scope).
5. **Proofs → App.C** — §4 above; new file + `main.tex` wiring + renumber A.*→C.*.
6. **Figures** — headline AUROC figure + transfer heatmap: re-render via
   `figures_src/` if the source ships figure data (`sources/.../figures_src/`,
   `figures_outline.md`), else copy baked PDFs into `figures/` with provenance.
7. **Honesty sweep** — verb "matches-or-outperforms (in the mean)"; NQ losses
   named; bolding only when > max std; method name "Contrastive+Recon" (not
   "ICR-probe").

## 6. Drafting order (phased)

Dependency: numbers gate prose; proofs + figures independent; gates/build last.

**Phase A — Number foundation (do first).**
- A1. `hallu_headline.csv` ← `headline_results.csv` (namespace + header). Build,
  confirm all 120 keys resolve. Settle the bolding (per-cell, > max-std rule).
- A2. `hallu_transfer_per_source.csv` + `hallu_transfer_summary.csv` (+ optional
  `hallu_transfer_matrix`). Build + verify.
- A3. (optional) `hallu_datasets.csv` only if §6.4 wants a dataset table (values
  currently blank/TBD).

**Phase B — Bib gate (parallel to A; blocks prose).** Propose the §3c 7 entries;
get human approval; insert; apply §3b remaps. Until then, hedge dataset/model
wording (source's standing instruction).

**Phase C — Prose port. ✅ ALL DONE 2026-06-06. Chapter compiles clean (latexmk
EXIT 0, lint OK, every `\result`/`\resultPM`/`\resdelta` resolves, no undefined
Ch.6 refs/cites).** Nine sections drafted:
- C1. ✅ §6.3 Method + Info-Theoretic Argument (lead). Prop `prop:hd:supcon-mi` in
  body, proof → App.C.
- C2. ✅ §6.4 Experimental Setup. Source-verified: Qwen3-8B non-thinking mode,
  HotpotQA distractor / SearchQA closed-book (the two flagged claims checked OK).
- C3. ✅ §6.5 Results (headline 2×12×5 table, both models; bolding computed per
  >max-std rule — verified) + §6.6 Compute-Matched (ACT-ViT caveat stated).
- C4. ✅ §6.7 Ablations — QUALITATIVE (no ablation CSV): leads with the confirmed
  symmetric-SupCon prediction (`cor:hd:symcon`, "roughly ten points"); 2×2 framed
  but per-cell numbers explicitly deferred; SimCLR-near-chance + scorer choice
  qualitative.
- C5. ✅ §6.8 Domain Transfer (per-source + in/out aggregate tables; recomputed
  from CSVs — ours leads 2 clean / 3 in-mean of 10 cells; NQ weakest, named).
- C6. ✅ §6.1 Introduction (parity-as-validation; "Contrastive+Recon" introduced;
  spine tie-in; contributions list; chapter map).
- C7. ✅ §6.9 Limitations (parity-not-dominance, NQ shortfall, evaluator noise,
  taxonomy deferred, scope, attribution gap, AUPRC/ECE/FPR95 supplementary).

**Build/gate notes for the record:**
- Lint whitelist gained `Claim`, `Variant`, `Llama-3.1-8B-Instruct`, `Qwen3-8B`
  (enumerated-label + model proper-noun digits).
- **`\resultPM` self-emits `$\pm$`** — call it BARE, never inside `$...$` (the
  subagents wrapped prose calls in `$...$`; fixed via regex strip of 12 instances).
  `\result`/`\resdelta` emit bare `\num` and are fine inside or outside math.
- `\midrule` must not appear in `\caption{}` text (cascading `\noalign` errors) —
  one §6.5 caption hit this; fixed to "a horizontal rule between groups".
- Subagents were told to return LaTeX fragments but **edited the chapter file
  directly**; they hit non-adjacent stubs so no corruption, but next time enforce
  return-only or use worktree isolation.

(Original per-section briefs retained below for reference.)
- C3. §6.5 Results (honest parity read) + §6.6 Compute-Matched (ACT-ViT caveat).
- C4. §6.7 Ablations / signal attribution (lead with confirmed Variant-4 prediction).
- C5. §6.8 Domain Transfer.
- C6. §6.1 Introduction (write after results settle, so headline claims match).
- C7. §6.2 Related Work (tighten, back-ref Ch.3) + §6.9 Limitations.
  Throughout: numbers→`\result`, keys→gated (§3), name→"Contrastive+Recon".

**Phase D — Proofs → Appendix C. ✅ DONE 2026-06-06.** `appendices/C_mi_proofs.tex`
created and wired into `main.tex`: Lemma DPI (`lem:hd:dpi`), Lemma InfoNCE
(`lem:hd:infonce`), Corollary co-information (`cor:hd:coinfo`), Proposition
(`prop:hd:supcon-mi`, proof here / statement in §6.3), Corollary symmetric-SupCon
(`cor:hd:symcon`). Source A.* renumbered to App.C; single-line display eqns for the
lint gate. Builds clean.

**Phase E — Figures.** Determine source ships figure data vs baked PDFs.

**Phase F — Gates & build.** `make lint` (whitelist tokens: Llama-3.1-8B,
Qwen3-8B, HotpotQA, PopQA, SciQ, SearchQA, SAPLMA, ACT-ViT, LLMsKnow, SelfCheckGPT,
InfoNCE, SupCon, DPI) → `build_numbers` → `latexmk` (App.C now resolves proof refs)
→ `check_refs`.

### Open items
- ✅ **Bib gate (§3c): DONE 2026-06-06.** All 7 entries web-verified and applied
  (references.bib 192→199). Phase B complete.
- ✅ **LLMsKnow identity (I-5): RESOLVED.** = `orgad2024llmsknow` (Orgad et al.,
  ICLR 2025, arXiv:2410.02707) — source's "Slobodkin" guess was wrong.
- ✅ **Phase A (numbers): DONE 2026-06-06.** `hallu_headline` (481 cells),
  `hallu_transfer_per_source` (161), `hallu_transfer_summary` (81) built and
  resolve via `build_numbers`. `baseline_comparison.csv` dropped (stale).
- 🔜 **`transfer_matrix` / `datasets`:** port or defer — decide when §6.4/§6.8 lock.
- 🔜 **Figures:** does `sources/.../figures_src/` ship data or only baked PDFs? →
  Phase E.
- ✅ **Source numbers already speak the v2 gate** — no foreign macro system to
  translate (unlike Ch.5).
