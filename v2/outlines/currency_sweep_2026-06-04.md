# Literature currency sweep — 2026-06-04

Recent (2023–25) methods a committee would expect, found via web search and
**confirmed absent** from `v2/references.bib` (190 keys). These are **gated
proposals** for positioning — *not added*. Verify each identifier on add (the
audit showed even published bibs err), then route through the bib gate. Scope:
positioning breadth, not exhaustive. Resolves the §6 currency TODO in
[03_literature_review.md](03_literature_review.md) / the master-outline TODO.

**Tiers:** ⭐ must-add (a reviewer will expect it — closest neighbor to our method)
· ➕ recommended · ◦ optional.

---

## Ch.6 — Hallucination detection (→ §3.4)

| Tier | Proposed key | Paper | Venue / id | Why it matters |
|---|---|---|---|---|
| ⭐ | `duan2024inside` *(name TBD)* | INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection (**EigenScore**) | ICLR 2024, arXiv:2402.03744 | **Closest neighbor to Ch.6** — eigen-analysis of internal-state covariance. Must be positioned against. |
| ➕ | `du2024haloscope` | HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection | NeurIPS 2024 (verify arXiv id) | unlabeled hallucination detection; a major 2024 method |
| ➕ | `chuang2024lookback` | Lookback Lens: Detecting/Mitigating Contextual Hallucinations Using Only Attention Maps | EMNLP 2024, arXiv:2407.07071 | the **attention-based** family Ch.6 should acknowledge |
| ◦ | `su2024mind` | Unsupervised Real-Time Hallucination Detection based on Internal States (**MIND** + HELM benchmark) | ACL 2024 (verify), arXiv:2403.06448 | unsupervised, internal-state; adjacent to the trainability framing |
| ◦ | `semantic_energy2025` | Semantic Energy: Detecting LLM Hallucination Beyond Entropy | 2025, arXiv:2508.14496 | recent SE follow-up; cite only if §3.4 has room |

Already present (good recency, no action): `barshalom2025actvit` (ACT-ViT),
`zhang2025icr` (ICR), `suresh2025clap` (CLAP), `kossen2024semantic` (SEP),
`farquhar2024detecting`, `manakul2023selfcheckgpt`.

## Ch.4 / Ch.5 — OOD detection (→ §3.3)

| Tier | Proposed key | Paper | Venue / id | Why it matters |
|---|---|---|---|---|
| ⭐ | `ammar2024neco` | NECO: NEural Collapse Based Out-of-distribution detection | ICLR 2024, arXiv:2310.06823 | **Closest neighbor to Ch.5's DSC** — neural-collapse geometry for OOD. Must position DSC against it. |
| ➕ | `xu2024scale` | Scaling for Training-Time and Post-hoc OOD Detection Enhancement (**SCALE**) | ICLR 2024, arXiv:2310.00227 | recent post-hoc scorer SOTA |
| ➕ | `liu2024fdbd` | Fast Decision Boundary based OOD Detector (**fDBD**) | ICML 2024 (verify arXiv id) | distance-to-decision-boundary scorer — relates to Ch.5's distance scorers |
| ◦ | `park2023nnguide` | Nearest Neighbor Guidance for OOD Detection (**NNGuide**) | NeurIPS 2023, arXiv:2309.14888 | kNN-guided scoring; near-/far-OOD |
| ◦ | `liu2023gen` | GEN: Pushing the Limits of Softmax-Based OOD Detection | CVPR 2023 | generalized-entropy logit scorer |

Already present (good recency, no action): `Wang2022vim` (ViM), `Sun2022dice`
(DICE), `sun2021react` (ReAct), `Haas2022ncood`, `Yang2025pskd`, the 2024 OOD set
(`du2024and`/`du2024does`/`guille2024cadet`/`ekim2024distribution`/`saadati2024out`).

---

## Recommendation
> **✅ The two ⭐ must-adds were applied to `references.bib` on 2026-06-04**
> (web-verified, ICLR 2024): `chen2024inside` (INSIDE/EigenScore, arXiv:2402.03744)
> and `BenAmmar2024neco` (NECO, arXiv:2310.06823). Bib: 190 → 192 entries. The ➕/◦
> sets remain proposals for §3.3/§3.4 draft time.

Add the **two ⭐ must-adds now** (INSIDE/EigenScore, NECO) — they are the
published methods nearest our two contributions and their absence is the kind of
gap a committee flags immediately. Add the ➕ set when §3.3/§3.4 are drafted; the
◦ set only if space allows. All proposed bibkeys above are **placeholders** —
confirm the exact key style, full author list, and identifier at add time.

> **✅ FULLY RESOLVED 2026-06-07** (with the Ch.3 draft). The ➕ and ◦ sets were
> all web-verified and added through the gate (bib 199→206):
> `du2024haloscope` (NeurIPS 2024, 2409.17504), `chuang2024lookback` (EMNLP 2024,
> 2407.07071), `su2024mind` (ACL Findings 2024, 2403.06448), `liu2024fdbd`
> (ICML 2024, 2312.11536), `park2023nnguide` (**ICCV 2023** — corrected from the
> NeurIPS guess above, 2309.14888), `liu2023gen` (CVPR 2023), `ma2025semantic`
> (arXiv 2508.14496). **SCALE was already present as `xuscaling`** — cited in Ch.3,
> no duplicate added. All seven are now cited in Ch.3 (§3.3/§3.4); build is clean.

## Side observation (not part of the sweep)
A search hit lists the Ch.5 ECCV paper at **arXiv:2603.11269** ("Beyond the Class
Subspace: Teacher-Guided Training…"). If that posting is live, the paper may now be
**public** — which would lift the "keep the repo private until public" constraint.
Worth confirming; does not change anything here.
