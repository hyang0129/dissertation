# Chapter 3 — Literature Review · outline & related-work architecture

Plan for the dissertation's cross-cutting related work, and how it divides labor
with the per-chapter Related Work sections (Ch.4/5/6). Companion to
[00_dissertation_outline.md](00_dissertation_outline.md) (Ch.3 entry) and
[bib_staging.md](bib_staging.md). Reference keys below are confirmed present in
`v2/references.bib` (190 entries, audited + verified 2026-06-04).

**Status:** ✅ carry-over from v1 §3, but ✏️ **revise** — §3.2 gains the geometry
lens, §3.3 gets the single-domain/DSC reframe, §3.4 is largely rewritten for the
real Ch.6 methods. Not a clean port.

---

## 1. Architecture — who owns what

The failure mode of a three-paper dissertation is saying everything twice (big
Ch.3 + each chapter's RW) or letting the two contradict. Division of labor:

| | **Ch.3 Literature Review** | **Per-chapter Related Work (4/5/6)** |
|---|---|---|
| Owns | breadth + cross-pillar synthesis under the representation lens | depth + comparators — only the methods in *that chapter's* tables |
| Length | substantial (the review) | tight, ~0.5–1 pg each |
| Job | establish the two lenses & shared vocabulary **once**; bridge vision-OOD and LLM-hallucination | position the chapter's contribution against its direct baselines |
| A work is… | **introduced and defined** here | **cited-and-positioned** as a comparator, with "(see §3.x)" |

**No-duplication rule:** a paper appears in Ch.3 for *thematic placement* and in a
chapter only when it is a *direct baseline* — cited once on first mention with a
§3.x back-ref, never re-surveyed. If a chapter RW starts *explaining* a method, it
belongs in Ch.3 instead.

## 2. Organizing principle

Ch.3 spans two disjoint literatures (vision OOD; LLM hallucination). Organized by
pillar it reads as three stapled mini-reviews. Instead, organize around the **two
lenses** (domain-agnostic), so the chapter enacts the title:

> §3.1–3.2 establish the shared frame — information theory + representation
> geometry as two ways to ask *"does the representation preserve the structure
> that distinguishes the shift?"* §3.3–3.4 are then **two applications of the same
> question** (OOD, hallucination), not two separate reviews. §3.5 is the substrate.

Open with a framing paragraph stating the thesis + two lenses; end each section
with a one-sentence tie back to the spine.

**Bridge the two lenses (else it's two topics, not one thesis).** §3.1→§3.2 must
explicitly link information-theoretic and geometric views as *two measurements of
the same representational structure* — e.g. `achille2018emergence` (invariance/
sufficiency ↔ geometry), `wang2021understanding` (a contrastive loss read
geometrically), `shwartz2023compress` / IB ↔ neural-collapse compression. Without
this connective tissue §3.1 and §3.2 read as unrelated surveys.

---

## 3. Section structure

### 3.1 Information theory in ML  ✅ carry-over
- **Owns (lens A):** entropy/MI; information bottleneck & minimal sufficiency; MI
  estimation; info-theoretic generalization. Primes Ch.4 (sufficiency / label
  blindness) and Ch.6 (cross-layer MI feasibility).
- **Refs:** `shannon1948mathematical` `cover1999elements` `tishby2000information`
  `tishby2015deep` `shwartz2017opening` `shwartz2023compress` `saxe2019information`
  `achille2018emergence` `alemi2017deep` `federici2020learning`
  `oord2018representation` `poole2019variational` `belghazi2018mutual`
  `hjelm2019learning` `mcallester1999pac` `xu2017information` `robert1952fano`
  `linsker1988self`
- **Boundary with Ch.2 (no duplication):** Ch.2 §2.6–2.7 own the **definitions/
  formalism** (what entropy, MI, DPI, the information bottleneck, minimal
  sufficiency, and the variational/InfoNCE MI bound *are*). §3.1 owns **how these
  have been used in ML** — the literature, not the definitions. §3.1 assumes
  §2.6–2.7 and cites forward sparingly.
- **Spine tie:** the formal language for "what a representation preserves about the
  label/shift."

### 3.2 Representation learning & geometry  ✏️ revise (geometry is new)
- **Owns (lens B + how representations form):** self-/unsupervised & supervised
  contrastive learning; latent-variable/generative representations; **and the
  geometric structure of learned features (neural collapse, dimensional collapse,
  alignment/uniformity, linear probes)** — the new co-lens that makes Ch.5's
  geometric DSC account and Ch.6's layer-pair views legible. **Builds on Ch.2 §2.8
  (Representation Geometry):** §2.8 *defines* the geometric primitives (spectrum,
  effective rank, subspaces, the bare neural-collapse definition); §3.2 surveys how
  the field has *used* them. Same definitions-vs-literature boundary as §3.1↔§2.6–2.7.
- **Self-/unsup + contrastive:** `chen2020simclr` `chen2020simple` `he2020momentum`
  `gidaris2018unsupervised` `Caron2021dino` `he2022masked` `chen2021exploring`
  `khosla2020supervised` `gao2021simcse` `oquab2023dinov2`
- **Classical lineage (compress to ~2 sentences — context only):** pre-deep
  representation learning — PCA/ICA/factor analysis + autoencoders:
  `pearson1901liii` `hyvarinen2000independent` `tipping1999probabilistic`
  `bartholomew1987latent` `hinton2006reducing` `vincent2008extracting`
  `baldi2012autoencoders`.
  - **Pruned from Ch.3** (v1 baggage; generative modeling is not the thesis — keep
    in the bib, omit from the review): `goodfellow2014generative` `kingma2014auto`
    `higgins2017beta` `chen2016infogan` `rezende2014stochastic`
    `dumoulin2016adversarially` `donahue2016adversarial` `creswell2018generative`
    `locatello2019challenging` `rifai2011contractive` `ng2011sparse`. Diffusion
    (`ho2020denoising` `song2020score` `karras2017progressive`) appears only as a
    **Ch.4 OOD baseline**, not here.
- **Geometry (new emphasis):** `Papyan2020nc` `Zhu2021nc` `Galanti2022collapse`
  `Haas2022ncood` `Jing2022rank` `wang2021understanding`. (Linear probing as a
  geometry tool is introduced in §3.5; back-reference it here.)
- **Distillation — cross-cutting thread (introduce here):** `hinton2015distilling`
  `tian2020crd` `sun2020codir` `zhang2022cds`. **Load-bearing for two chapters** —
  Ch.5 (TGT *is* teacher distillation) and Ch.6 (positions its layer-pair method
  *against* contrastive distillation). Flag explicitly so it isn't under-weighted.
- **Spine tie:** the second lens — *geometry* of what the representation keeps.

### 3.3 OOD detection  ✏️ revise (single-domain / DSC reframe)
- **Owns:** classical scorers, benchmarking, unlabeled/SSL OOD, single-domain +
  neural-collapse link, domain adaptation, ensembles. Positions Ch.4 & Ch.5.
- **Scorers:** `hendrycks2016baseline` `liang2017enhancing` `liu2020energy`
  `lee2018simple` `sun2021react` `Wang2022vim` `Sun2022dice` `huang2021mos`
  `sehwag2021ssd`
- **Benchmarks / surveys:** `yang2021generalized` `yang2022openood`
  `zhang2023openood` `drummond2006open`
- **Unlabeled / SSL / zero-shot OOD:** `tack2020csi` `hendrycks2019using`
  `mohseni2020self` `xiao2020likelihood` `liu2023unsupervised` `esmaeilpour2022zero`
  `wang2023clipn` `du2024and` `du2024does`
- **Single-domain + collapse / fine-tuning:** `Haas2022ncood` `Kumar2022lp`
  `Winkens2020contrastive` `Berger2021medood` `zhou2022rethinking`
- **Ensembles / DA theory:** `lakshminarayanan2017simple` `daxberger2019bayesian`
  `pmlr-v235-xu24ae` `ben2010theory` `katz2022training` `vyas2018out`
- **Spine tie:** detection succeeds/fails by whether the representation kept the
  shift-distinguishing directions.

### 3.4 Hallucination detection  ✏️ revise heavily (v1 was proposal-era)
- **Owns:** surveys/taxonomy, evaluation, sampling/consistency methods,
  internal-state probing, info-theoretic framing. Positions Ch.6.
- **Surveys / taxonomy:** `ji2022survey` `bang2025hallulens`
- **Evaluation / benchmarks:** `min2023factscore` `li2023halueval`
  `lin2021truthfulqa` `lin2022truthfulqa` `thorne2018fever` `peng2023check`
  `chern2023factool`
- **Sampling / consistency:** `manakul2023selfcheckgpt` `farquhar2024detecting`
  `kossen2024semantic`
- **Internal-state probing (the family Ch.6 lives in):** `azaria2023internal`
  `li2023iti` `marks2024geometry` `kadavath2022language` `burns2023discovering`
  `zhang2025icr` `suresh2025clap` `barshalom2025actvit` — *applies* the probing
  paradigm introduced in §3.5 (back-ref, don't re-introduce).
- **Spine tie:** hallucination as loss of label-relevant structure across layers.

### 3.5 Architectures & foundation models  ✅ carry-over (+ LLMs)
- **Owns:** the shared substrate all three pillars run on.
- **CNNs:** `he2016deep` `krizhevsky2012imagenet` `lecun1998gradient`
- **Transformers / ViT:** `vaswani2017attention` `dosovitskiy2020image`
  `Touvron2021deit`
- **Foundation models:** `radford2021learning` `oquab2023dinov2` `devlin2018bert`
  `brown2020language` `raffel2020exploring` `radford2018improving`
- **Interpretability / probing of internals (HOME of the probing paradigm):**
  `alain2017understanding` `belinkov2019analysis` `tenney2019bert`
  `hewitt2019structural` `voita2019analyzing` `voita2019information`
  `kim2018interpretability` `olah2020zoom` `selvaraju2017grad`. Introduce probing
  *here*; §3.2 (geometry) and §3.4 (hallucination) apply it with a back-ref.
- **Spine tie:** the substrate whose internal representations §3.3/§3.4 probe.

> **Dataset / benchmark cites are NOT in Ch.3.** Keys like `cifar10` `food`
> `fashion` `plant` `bossard14` `netzer2011reading` `cimpoi2014describing`
> `yu2015lsun` `deng2009imagenet` `helber2019eurosat` `yang2023medmnist`
> `zhou2017places` `card_data` `rock_data` `yoga_data` `kwiatkowski2019natural`
> `joshi2017triviaqa` `berant2013semantic` `single2023realwaste` `ritrc` etc. belong
> in each chapter's **Experimental Setup**, not the literature review.

---

## 4. Per-chapter Related Work scope

Each results chapter keeps a tight RW (~0.5–1 pg), back-referencing Ch.3.

- **Ch.4 (Label Blindness):** unlabeled/SSL-OOD baselines it tests (SimCLR-KNN/SSD,
  RotLoss, diffusion, CLIPN) + near/far/**adjacent**-OOD benchmarking. Defers
  sufficiency/MI → §3.1, SSL → §3.2.
- **Ch.5 (DSC/TGT):** single-domain OOD + the **distance/logit scorers DSC
  degrades** (MDS/kNN/`Wang2022vim`/MSP/Energy), neural collapse as the diagnosis's
  neighbor (§3.2 back-ref), the **teacher-distillation lineage TGT builds on**
  (`tian2020crd`-style, DINOv2 teacher). Defers broad OOD → §3.3, geometry → §3.2.
- **Ch.6 (MI Hallucination):** the **three comparator families** — output-space
  scalar (logprob/entropy/`kadavath2022language` P(true)); activation probes
  (`azaria2023internal`/LLMsKnow/`barshalom2025actvit`); sampling
  (`manakul2023selfcheckgpt`/semantic entropy) — + the **contrastive-distillation
  precedent it extends** (`tian2020crd`/`sun2020codir`/`zhang2022cds`,
  `kossen2024semantic` SEP). Defers info-theory → §3.1, contrastive learning →
  §3.2, taxonomy/eval → §3.4. Hosts the **§2.3 novelty claim** (one-class
  contrastive over *layer-pair* views vs. CRD/CoDIR/CDS).

## 5. The reviewer-risk to settle now
`tian2020crd` / `sun2020codir` / `zhang2022cds` appear in **both** §3.2 (as
representation-MI / distillation methods) and Ch.6 RW (as the precedent the novelty
distinguishes from). Convention: **§3.2 introduces and defines them; Ch.6 positions
against them with a back-ref.** Don't let both carry the novelty argument.

## 6. Open items

**Resolved 2026-06-04** (review of the plan):
- ✅ **§3.2 pruned** — generative/latent-variable v1 baggage cut to a brief
  classical-lineage sentence; GANs/VAEs/disentanglement omitted from the review;
  diffusion demoted to Ch.4 OOD baseline.
- ✅ **Ch.2 ↔ Ch.3 boundary** stated (§3.1): Ch.2 = definitions/formalism, §3.1 =
  usage-literature.
- ✅ **Two-lens bridge** added (§2): explicit info-theoretic↔geometric linking refs.
- ✅ **Distillation** elevated to a flagged cross-cutting thread (§3.2).
- ✅ **Probing** consolidated — introduced in §3.5; §3.2/§3.4 apply with back-ref.

**Resolved 2026-06-07** (Ch.3 drafted):
- ✅ **Currency sweep applied.** The ⭐ must-adds (`chen2024inside` INSIDE/EigenScore,
  `BenAmmar2024neco` NECO) landed 06-04; the ➕/◦ sets landed with the Ch.3 draft
  (bib 199→206): `du2024haloscope`, `chuang2024lookback`, `su2024mind` (§3.4);
  `liu2024fdbd`, `park2023nnguide`, `liu2023gen` (§3.3); `ma2025semantic` (§3.4).
  All web-verified 06-07 (title/authors/venue/arXiv id). SCALE was already present
  as `xuscaling` — cited, no duplicate added. NNGuide corrected to ICCV 2023.
- ✅ **§3.3/§3.4 drafted** citing the above; all keys resolve, build clean.
- Confirm a few unbucketed keys at draft time: `liu2025detecting`,
  `chen2020simple` vs `chen2020simclr` (possible overlap), `guille2024cadet`,
  `ekim2024distribution`, domain-specific OOD apps (`kafunah2023out`/`kim2021wafer`/
  `narayanaswamy2023exploring`).
