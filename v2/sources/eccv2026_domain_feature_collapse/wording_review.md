# Wording Review: Space-Saving Changes for main.tex

Each entry shows the **original** phrase and a **proposed** shorter version.
Entries are grouped by section. Accept, reject, or modify as needed.

---

## Abstract

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| A1 | `both distance-based and logit-based OOD scores` | `distance- and logit-based OOD scores` | hyphen-chain saves 2 words |
| A2 | `The teacher and auxiliary head are discarded at inference, adding no test-time overhead.` | `The teacher and auxiliary head are discarded after training, adding no inference overhead.` | minor rewording for clarity/consistency with method section |

---

## Introduction

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| I1 | `a detector must identify both (i) unseen classes within the same domain and (ii) samples from entirely different domains` | `a detector must identify both (i) unseen within-domain classes and (ii) samples from entirely different domains` | saves 3 words |
| I2 | `we project out class-discriminative teacher components and supervise the student to predict the remaining residual with an auxiliary domain head` | `we project out class-discriminative directions and supervise the student on the remaining residual via an auxiliary domain head` | saves 2 words |
| I3 | `while also improving in-domain OOD and maintaining classification accuracy` | `while improving in-domain OOD and maintaining classification accuracy` | drop "also" |
| I4 | `in both in and out-of-domain settings` (contributions bullet) | `in both in- and out-of-domain settings` | add hyphen (grammatically needed) |

---

## Related Work

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| R1 | `flags inputs whose score falls below a threshold as out-of-distribution` | `flags below-threshold inputs as out-of-distribution` | saves 5 words |
| R2 | `where in distribution training data spans rich visual diversity` | `where in-distribution training data spans rich visual diversity` | fix missing hyphen + saves nothing but is correct |
| R3 | `Preserving the rich pre-trained geometry during single-domain fine-tuning therefore requires an explicit training objective beyond cross-entropy.` | `Preserving pretrained geometry during single-domain fine-tuning therefore requires an explicit objective beyond cross-entropy.` | saves 3 words |

---

## Theory (Section 3)

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| T1 | `We state sufficient conditions under which OOD-score failure is quantifiable (\cref{...}), identify DSC as an inherent consequence of supervised single-domain training (\cref{...}), and validate the resulting predictions empirically (\cref{...}).` | `We state sufficient conditions for quantifiable OOD-score failure (\cref{...}), identify DSC as an inherent consequence of supervised single-domain training (\cref{...}), and validate predictions empirically (\cref{...}).` | saves 5 words |
| T2 | `a sensor, style, or semantic sub category` | `a sensor, style, or semantic subcategory` | merge to one word |
| T3 | `fine-grained sub-category identity` | `fine-grained subcategory identity` | merge to one word |
| T4 | `We quantify severity with two directly measurable diagnostics:` | `We quantify severity with two diagnostics:` | saves 2 words |
| T5 | `the geometry audits confirm the DSC severity landscape described in section \ref{sec:theory}` | `the geometry audits confirm the DSC severity landscape described in \cref{sec:theory}` | use `\cref` for consistency |
| T6 | `regardless of their discriminative value for ID-vs-OOD separation` | `regardless of their discriminative value` | redundant qualifier |

---

## Method (Section 4)

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| M1 | `so the student gains both signals without requiring the teacher at inference` | `so the student gains both signals without the teacher at inference` | saves 1 word |
| M2 | `The quantity $u_{\mathrm{dom}}(x)$ is computed from frozen teacher features as a training-time supervision target only.` | `$u_{\mathrm{dom}}(x)$ is computed from frozen teacher features as a training-time target only.` | saves 4 words |
| M3 | `no teacher forward pass, no auxiliary head, and no additional memory cost at test time` | `no teacher forward pass, no auxiliary head, and no additional test-time cost` | saves 2 words |

---

## Experiments (Section 5)

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| E1 | `We evaluate on eight single-domain classification benchmarks spanning diverse visual modalities.` | `We evaluate on eight single-domain benchmarks spanning diverse visual modalities.` | saves 1 word |
| E2 | `the harder and more practically relevant regime` | `the harder, practically relevant regime` | saves 2 words |
| E4 | `To evaluate an alternative training strategy that can reduce DSC, we also include a \textbf{ResNet-50 trained with supervised contrastive learning}~\cite{Khosla2020supcon}, referred to as \textbf{SupCon}.` | `To evaluate an alternative DSC-mitigation strategy, we include \textbf{ResNet-50 with supervised contrastive learning}~\cite{Khosla2020supcon} (\textbf{SupCon}).` | saves ~7 words |
| E5 | `We use a shared trade-off weight $\lambda_{\mathrm{TGT}} = 1.0$ for both ResNet-50 and DINOv2 runs.` | `We use $\lambda_{\mathrm{TGT}} = 1.0$ for both ResNet-50 and DINOv2.` | saves 5 words |
| E6 | `We evaluate eight post-hoc OOD scoring methods on each trained backbone without modification:` | `We apply eight post-hoc OOD scorers to each backbone without modification:` | saves 3 words |
| E7 | `We additionally report a \emph{MDS Teacher Only} oracle (MDS applied to frozen DINOv2 features without a student) as a reference upper bound for out-of-domain sensitivity.` | `We additionally report a \emph{Teacher-Only MDS} oracle (MDS on frozen DINOv2 features, no student) as an upper bound on out-of-domain sensitivity.` | saves 5 words |
| E8 | `On \textbf{ResNet-50}, swapping the CE backbone for a TGT backbone improves all eight scorers on average across the 8 benchmarks:` | `On \textbf{ResNet-50}, TGT improves all eight scorers on average:` | saves 9 words |
| E9 | `Compared to the non-TGT plain MDS baseline, adding TGT lowers FPR@95 from \FaroodMDSStdResNet{} to \FaroodMDSTGTResNet{} on ResNet-50` | `TGT lowers MDS FPR@95 from \FaroodMDSStdResNet{} to \FaroodMDSTGTResNet{} on ResNet-50` | saves 7 words |
| E10 | `TGT is the only evaluated approach that improves both regimes simultaneously, though individual dataset--scorer combinations may show small regressions (particularly logit-based scores and tissue/rock datasets), and improvements on DINOv2 are less consistent than on ResNet-50.` | `TGT is the only evaluated approach that improves both regimes simultaneously, though individual dataset--scorer combinations may regress (particularly logit-based scores and tissue/rock datasets), and DINOv2 gains are less consistent.` | saves ~10 words |
| E11 | `On out-of-domain OOD, SupCon underperforms the CE ResNet-50 baseline on both reported distance-based scorers (MDS: 32.02 vs. 25.55 FPR@95; kNN: 44.39 vs. 34.98), which is inconsistent with recovering domain-sensitive structure.` | `SupCon underperforms the CE baseline on both distance-based scorers (MDS: 32.02 vs. 25.55; kNN: 44.39 vs. 34.98), inconsistent with recovering domain-sensitive structure.` | saves ~8 words |
| E12 | `Overall, SupCon may improve class-level compactness, but it does not consistently restore the domain-sensitive directions suppressed by DSC.` | `SupCon may improve class compactness but does not consistently restore domain-sensitive directions.` | saves 8 words |

---

## DINOv2 Analysis (Section 5.3)

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| D1 | `In this setting, the teacher is frozen DINOv2 and the student is also DINOv2 fine-tuned from the same pre-training initialization.` | `Both teacher and student are DINOv2, sharing architecture and pre-training initialization.` | saves 9 words |
| D2 | `Because architecture and pre-training weights are shared, teacher residual targets can be highly aligned with the student's existing representation, reducing the novelty of the auxiliary supervision.` | `Because of this shared initialization, teacher residual targets can be highly aligned with the student's representation, reducing the novelty of the auxiliary supervision.` | saves 4 words |
| D3 | `instead of adding new geometric information, the teacher objective may mainly reinforce the student's current feature structure and constrain adaptation` | `the teacher objective may mainly reinforce existing structure rather than inject new geometric information` | saves 5 words |
| D4 | `where the student has a different architecture and different optimization trajectory, so distilling from DINOv2 injects genuinely complementary structure` | `where a different architecture and optimization trajectory make DINOv2 distillation genuinely complementary` | saves 5 words |

---

## Conclusion

| # | Original | Proposed | Notes |
|---|----------|----------|-------|
| C1 | `most reliably for distance-based scorers in both out-of-domain and in-domain settings` | `most reliably for distance-based scorers in both settings` | saves 4 words (reader knows the two settings) |
| C2 | `Future work includes extending DSC analysis to other architectures and modalities, designing adaptive teacher residual targets, and studying when additional supervision can further improve difficult fine-grained in-domain OOD scenarios.` | `Future work includes extending DSC to other architectures and modalities, designing adaptive teacher residual targets, and studying when additional supervision improves difficult fine-grained in-domain OOD scenarios.` | saves 4 words |

---

## Summary

| Section | Changes | Est. words saved |
|---------|---------|-----------------|
| Abstract | 2 | ~3 |
| Introduction | 4 | ~8 |
| Related Work | 3 | ~6 |
| Theory | 6 | ~10 |
| Method | 3 | ~7 |
| Experiments | 12 | ~70 |
| DINOv2 Analysis | 4 | ~23 |
| Conclusion | 2 | ~8 |
| **Total** | **36** | **~135** |

> Highest-impact single change: **E3** (OpenOOD protocol sentence, ~10 words) and **E8** (ResNet-50 results intro, ~9 words).
