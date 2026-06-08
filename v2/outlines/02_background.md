# Chapter 2 — Background and Definitions · outline & primitive inventory

Plan for the dissertation's **shared formal vocabulary**. Companion to
[00_dissertation_outline.md](00_dissertation_outline.md) (Ch.2 entry, which holds
the prose rationale + the 2026-06-05 reframe) and
[03_literature_review.md](03_literature_review.md) (the §2↔§3 handoff). This file
is the *spec sheet*: per-section, what definitions go in, where they come from, and
which chapter consumes them.

**Status:** ✅ **drafted 2026-06-07** (`chapters/02_background.tex`, 8 sections,
11 numbered definitions/methods; builds clean). Blocks 1 ported from v1 §2 with
edits (DFC definition deleted → DSC forward-pointer); Block 2 is the new work
(§2.8 representation geometry; DPI added to §2.6; InfoNCE + SupCon/SimCLR to §2.7).
Labels are `bg:`-namespaced (`def:bg:ood`, `def:bg:mss`, `def:bg:ib`,
`def:bg:dpi`, `method:bg:infonce`, `def:bg:anisotropy`, `def:bg:neuralcollapse`, …).

---

## 1. The two boundaries Ch.2 lives inside

1. **Primitives-only (Ch.2 vs Ch.4–6).** Ch.2 holds only vocabulary reused by more
   than one chapter. Named phenomena/methods are defined *where contributed*:
   Label-Blindness theorem (Ch.4), **DSC + TGT** (Ch.5), the one-class layer-pair
   probe (Ch.6). → v1's "Domain Feature Collapse" definition is **deleted** from
   Background.
2. **Definitions vs literature (Ch.2 vs Ch.3).** Ch.2 *defines* the primitive
   (§2.6–2.8 = formalism); Ch.3 §3.1–3.2 *survey its use* in ML. Ch.2 ends on the
   two lenses in the order Ch.3 opens with them: §2.6/2.7→§3.1, §2.8→§3.2.

Net handoff, one beat per primitive: **Ch.2 defines → Ch.3 surveys → Ch.4–6 deploy.**

---

## 2. Section inventory

Provenance key: **port** = lift from v1 §2 (light edits) · **port-src** = pull from
a source paper's preliminaries · **new** = write from scratch.

### Block 1 — settings / tasks (mostly carry-over)

| § | Section | Primitives it defines | Provenance | Consumer |
|---|---|---|---|---|
| 2.1 | OOD Detection | OOD detection def (`defineood`); MSP method (`methodmsp`); training-agnostic vs -aware; epistemic vs aleatoric | port — [v1 §2.1](../../v1/Sample_Thesis_main.tex#L165-L196) | Ch.4, Ch.5 |
| 2.2 | Anomaly Detection | scope/training-assumptions/eval contrast vs OOD (one-class framing) | port, **compress** — [v1 §2.2](../../v1/Sample_Thesis_main.tex#L199-L219) | Ch.4 (one-class), Ch.6 (one-class probe) |
| 2.3 | Unlabeled OOD Detection | unlabeled OOD def (`Train({x_i})`, no labels); pretrained-as-unlabeled | port, **moved up** to sit with OOD — [v1 §2.6](../../v1/Sample_Thesis_main.tex#L397-L421) | Ch.4 |
| 2.4 | Dataset Domain & Single-Domain Setting | domain labelling fn `f_d`; domain vs class features (`I(x_d:x_y)=0`); single-domain dataset def (`def:singledomain`) | port — [v1 §2.5](../../v1/Sample_Thesis_main.tex#L324-L368); **DELETE `def:domainfeaturecollapse`** ([v1 L390-393](../../v1/Sample_Thesis_main.tex#L390-L393)); add 1-line forward-pointer → DSC (Ch.5) | Ch.4, Ch.5 |
| 2.5 | LLMs & Hallucination | LLM def (autoregressive `f_θ`); hallucination def; extrinsic vs intrinsic (focus: extrinsic); **+ residual stream / intermediate-layer activations as a defined object** | port [v1 §2.7](../../v1/Sample_Thesis_main.tex#L423-L472) + **new** (residual stream) | Ch.6 |

### Block 2 — the two lenses (the new work)

| § | Section | Primitives it defines | Provenance | Consumer |
|---|---|---|---|---|
| 2.6 | Information Theory | entropy, conditional entropy, MI, KL, chain rules (`def:entropy`…`def:chain_rule_mi`); **+ Data Processing Inequality** | port [v1 §2.3](../../v1/Sample_Thesis_main.tex#L221-L283) + **new** (DPI) | Ch.4, **Ch.6** (DPI = "cross-layer MI positive by construction") |
| 2.7 | Information Bottleneck, Sufficiency & MI Estimation | minimal sufficient statistic (`def:mss`); information bottleneck (`def:ib`); **+ variational MI lower bound / InfoNCE as the canonical estimator** | port [v1 §2.4](../../v1/Sample_Thesis_main.tex#L285-L322) + **port-src** (InfoNCE bound ← hallulens [03_method.md](../sources/hallulens_mi_hallucination/03_method.md)) | Ch.4 (sufficiency engine), **Ch.6** (InfoNCE = feasibility-by-trainability) |
| 2.8 | **Representation Geometry** (NEW) | feature/representation space; covariance spectrum & anisotropy; effective rank / low-rank subspace; class subspace vs domain-shift directions; distance- vs logit-based scores *as geometric objects*; **bare neural-collapse definition** | **new** + **port-src** ← eccv2026 [main.tex](../sources/eccv2026_domain_feature_collapse/main.tex) + [supplementary.tex](../sources/eccv2026_domain_feature_collapse/supplementary.tex) (geometry preliminaries only — **not** Thm 1 / Prop 1, which live in App.B) | **Ch.5** (DSC), Ch.6 (layer-pair geometry) |

---

## 3. Drafting cautions

- **Don't restate appendix theorems in Ch.2.** §2.8 gives the geometric *primitives*
  only; the distance-failure Theorem 1 and MSP/Energy Proposition 1 stay in
  **Appendix B**. Likewise §2.7 states the InfoNCE *bound as a primitive*; the
  Ch.6 propositions/corollaries stay in **Appendix C**.
- **Don't name DSC in §2.4.** Forward-pointer only ("the geometric failure mode
  single-domain training induces — Domain-Sensitivity Collapse — is the subject of
  Ch.5"). DSC is Ch.5's contribution, not a background primitive.
- **Notation reconciliation.** v1 §2 uses the `math_commands.tex` macros
  (`\rvx`, `\sY_{in}`, etc.); new §2.8 geometry + §2.7 InfoNCE must adopt the same
  macro set so symbols are consistent across the eccv/hallulens ports.
- **Citations are sparse here by design** — Ch.2 defines, Ch.3 cites the
  literature. Only foundational attributions belong in Ch.2 (`shannon1948mathematical`
  for entropy, `tishby2000information` for IB, `oord2018representation` for InfoNCE,
  `Papyan2020nc` for neural collapse). Everything else → §3.1/§3.2.

## 4. Open items

- 🔜 Confirm the exact geometry primitives to lift from the eccv supplementary
  (effective rank vs participation ratio; which anisotropy measure) when §2.8 is
  drafted — match whatever Ch.5 actually uses so the prime is exact.
- 🔜 Decide whether "residual stream" gets its own short subsection in §2.5 or a
  paragraph — depends on how much Ch.6 leans on it vs. defines it itself.
