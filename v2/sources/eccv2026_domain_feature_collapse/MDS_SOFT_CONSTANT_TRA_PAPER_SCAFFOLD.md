# MDS + Soft Constant-RA Score via Teacher-Guided Training: Paper Scaffold

## Terminology

- **RA Score**: Residual Agreement Score (legacy code/doc name: **TRA**, "Teacher Residual Agreement").
- **RA Score — Variant A (post-hoc)**: fits a ridge regression mapping $W$ from student features to class-suppressed teacher residuals on the training set; no training changes required. Teacher needed at inference.
- **RA Score — Variant B (TGT)**: uses a student domain head trained end-to-end via TGT to predict teacher residuals; the trained head is used directly at evaluation time. Teacher-free at inference.
- **TGT**: Teacher-Guided Training — training a student network with an auxiliary domain head that predicts class-suppressed teacher residuals.
- **Constant-RA (Constant TRA)**: RA Score variant where the reference teacher residual is replaced by its training-set mean $\mu_\text{const}$; no per-sample teacher at inference.
- **Soft scoring**: disagreement-based penalty blended into the base score via $\gamma$-weighted excess above a percentile threshold; no hard rejection masking.
- **MDS Soft Constant-RA**: the full method — Mahalanobis Distance Score (MDS) as base detector, fused softly with Constant-RA disagreement computed from TGT-trained student domain head.
- **DSC**: Domain-Sensitivity Collapse — the low-rank, class-aligned geometry induced by single-domain supervised training that renders standard OOD scores insensitive to domain shift.

---

## Working Premise

Single-domain supervised training induces **Domain-Sensitivity Collapse (DSC)**: features concentrate in a class-aligned, low-rank subspace (neural-collapse-adjacent geometry), making standard OOD scores (KNN, MDS/Mahalanobis, MSP, Energy) systematically insensitive to domain shift.

**Teacher-Guided Training (TGT)** counteracts DSC by injecting multi-domain structure from a frozen DinoV2 teacher into the supervised student's representation. After TGT, the student retains class-discriminative power *and* domain-shift sensitivity, so that even vanilla MDS in the student space achieves near-zero FPR@95 on out-of-domain OOD.

**Key result (to be finalized with locked numbers):** MDS Soft Constant-RA applied to a TGT-trained student achieves **up to 90% reduction in FPR@95** compared to plain MDS on a standard CE-trained student, and outperforms all other evaluated methods including KNN, MSP, Energy, and VIM variants  on both far-OOD (domain-shift) and near-OOD (adjacent class) benchmarks.

---

## 0. Title, Abstract, Contributions

### Candidate Titles

1. *Teacher-Guided Training Eliminates Domain-Sensitivity Collapse: MDS + Soft Constant Residual Agreement for Single-Domain OOD Detection*
2. *From Collapse to Sensitivity: MDS Soft Constant-RA via TGT Closes the Single-Domain OOD Gap*
3. *MDS Soft Constant-RA: 90% FPR@95 Reduction Through Teacher-Guided Representation Recovery*

### Abstract Draft (placeholder; fill with final numbers)

Standard OOD detectors (KNN, Mahalanobis/MDS, MSP, Energy) perform well on multi-domain benchmarks but collapse on single-domain datasets  trained on medical images, satellite imagery, or specialized sensors, they routinely fail to flag even trivially different domains as out-of-distribution. We identify **Domain-Sensitivity Collapse (DSC)** as the root cause: supervised single-domain optimization drives features into a low-rank, class-aligned subspace (a neural-collapse-adjacent geometry), after which domain shifts produce negligible change in standard distance or logit-based scores.

We propose **Teacher-Guided Training (TGT)**, a lightweight auxiliary loss that supervises the student's domain head using class-suppressed residuals from a frozen multi-domain teacher (DinoV2 ViT-S/14). TGT restores domain sensitivity to the student representation without degrading classification accuracy. For settings where training changes are infeasible, we additionally present **RA Score Variant A**: a post-hoc ridge regression mapping fit from student features to teacher residuals that requires no retraining. At inference, the full method uses **Mahalanobis Distance Score with Soft Constant Residual Agreement (MDS Soft Constant-RA)**  a soft blend of MDS with a disagreement signal derived from the student's domain head and a constant reference residual calibrated on the training set, requiring no teacher at test time.

Across [N] single-domain benchmarks (Colon pathology, EuroSAT satellite, Food, Yoga, Plant), MDS Soft Constant-RA achieves up to **90% reduction in FPR@95** compared to standard MDS, and consistently surpasses all competing methods including KNN, VIM, MSP, and Energy  for both far-OOD (domain-shift) and near-OOD (adjacent class) detection.

### Contributions

1. **Theory**: Formal characterization of DSC  a neural-collapse-adjacent, anisotropic geometry that provably renders distance-based and logit-based OOD scores insensitive to domain shift under mild assumptions, supported by empirical validations (Section 3).
2. **Method — RA Score Variant A**: A post-hoc detector that fits a ridge regression from student features to class-suppressed teacher residuals; no training changes required (Section 4).
3. **Method — TGT + MDS Soft Constant-RA**: Teacher-Guided Training that injects multi-domain structure via an auxiliary domain head loss, combined with a soft Constant-RA fusion score requiring only the student model at test time (Sections 45).
4. **Empirics**: Up to 90% FPR@95 reduction vs. all baselines across five single-domain benchmarks, with ablations tracing gains to representation geometry recovery (Section 6).

---

## 1. Introduction

### Problem Statement

Modern OOD detection methods excel on multi-domain benchmarks (CIFAR-10/100, ImageNet), yet catastrophically fail when models are trained on single-domain data  a setting ubiquitous in high-stakes deployments (medical imaging, earth observation, industrial inspection). In these settings, FPR@95 can exceed 50% even for extreme domain shifts (e.g., X-rays presented to a model trained on colon histopathology), a failure not predicted by standard benchmarks.

> **Paragraph to write**: Open with 23 concrete failure examples (FPR@95 numbers for CE-ResNet on Colon, EuroSAT, Plant). State the gap and why it matters.

### Why Existing Methods Fail

Single-domain supervised training produces **Domain-Sensitivity Collapse (DSC)**: the feature geometry concentrates variance along a low-rank, class-aligned subspace $\mathcal{S}_\text{cls}$. Both ID and OOD samples are aggressively mapped into $\mathcal{S}_\text{cls}$ by $f_\theta$, making domain-shift differences invisible to Euclidean or Mahalanobis distance (see `docs_theory/anisotropy_ood_detection_theory.md`, Section 2; `docs_theory/theory_distance_failure_and_TRA_success.md`, Theorem 1'). The same class-aligned geometry suppresses MSP and Energy via head subspace insensitivity. Fine-tuning even a rich pretrained model on single-domain data reintroduces DSC via progressive rank collapse.

> **Paragraph to write**: Key diagnostic  participation ratio / effective rank of supervised features. Cite the fine-tuning trajectory experiment showing rank collapse co-varies with FPR@95 rise.

### Our Approach

We present two complementary methods, both leveraging a frozen DinoV2 teacher to supply class-suppressed domain residuals as a reference signal:

- **RA Score Variant A (post-hoc)**: fits a ridge regression $W$ from student features to teacher residuals on the training set. No training changes required. At inference, disagreement between student-predicted and teacher residuals serves as an OOD signal, fused softly with MDS.
- **TGT (Variant B / trained)**: adds an auxiliary domain head loss during training, permanently shaping the student representation to retain domain-shift sensitivity. After TGT, no teacher is needed at inference; vanilla MDS in the student space already achieves near-zero far-OOD FPR@95, and MDS Soft Constant-RA further improves both far- and near-OOD detection.

Both variants require the teacher only during setup / training, and deploy teacher-free at inference (Variant A requires the teacher at inference to compute $u_\text{dom}(x)$; Variant B / TGT is fully teacher-free at deployment).

---

## 2. Related Work

### 2.1 Single-Domain OOD Detection Failures
- Prior empirical observations of catastrophic OOD failure on medical/satellite/specialized-sensor data.
- Contrast with multi-domain benchmarks (CIFAR-10/100, ImageNet) where modern detectors succeed.
- Supervised fine-tuning of pretrained models reintroduces geometric collapse via catastrophic forgetting, even from a strong multi-domain initialization.

### 2.2 Distance-Based OOD Detectors
- KNN (Sun et al., 2022), Mahalanobis/MDS (Lee et al., 2018), VIM (Wang et al., 2022), SSD+.
- React (Sun et al., 2021), DICE: logit-truncation interventions; do not address underlying feature geometry.
- These methods succeed on multi-domain benchmarks where feature geometry is isotropic; they degrade precisely when DSC is present.

### 2.3 Representation Distillation and Teacher-Student Methods
- Knowledge Distillation (Hinton et al., 2015), DeiT, DINO.
- TGT is distinct: the teacher is used for *domain representation recovery*, not accuracy transfer. Teacher is needed only at training time; inference is teacher-free.
- Feature alignment via Contrastive methods (SimCLR, SupCon): retain some domain structure, but still subject to DSC under single-domain fine-tuning.

### 2.4 Neural Collapse
- Papyan et al. (2020): ETF geometry at training convergence  within-class variance vanishes, class means form an equiangular tight frame (ETF simplex) in $C-1$ dimensions.
- DSC generalizes this: ETF geometry is optimal for classification but catastrophic for OOD detection, explicitly placing domain-shift directions in the null space.

---

## 3. Theory: Domain-Sensitivity Collapse

### 3.1 Anisotropic Geometry and Distance Failure

> **Subsection to write** (from `docs_theory/anisotropy_ood_detection_theory.md`, `docs_theory/theory_distance_failure_and_TRA_success.md`):

The covariance $\Sigma = \Sigma_\text{between} + \Sigma_\text{within}$ of a single-domain supervised model concentrates variance in the class-discriminative subspace $\mathcal{S}_\text{cls}$ (at most rank $C-1$). Relevant geometry metrics:

$$
\text{PR}(\Sigma) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}, \quad r_\text{eff}(\Sigma) = \exp\!\left(-\sum_i \hat\lambda_i \log \hat\lambda_i\right)
$$

**Theorem (VarianceDiscriminability Mismatch; Theorem 1' in `theory_distance_failure_and_TRA_success.md`):** Under anisotropic ID geometry (assumption A1) and dominant-subspace OOD projection (A2), the KNN and Mahalanobis score distributions on ID and OOD samples converge:

$$
W_1\!\left(S_\text{KNN}(Z_\text{ID}),\, S_\text{KNN}(Z_\text{OOD})\right) \le c_1 \varepsilon + c_2 \tau^2
$$

Analogous results hold for MSP and Energy under head subspace insensitivity (small $\|WP_\perp\|_\text{op}$).

> Paragraph: Connection to Neural Collapse  ETF geometry is optimal for classification but catastrophic for OOD; maps all inputs into a $(C-1)$-simplex leaving domain-shift directions in the null space with near-zero variance.

### 3.2 DSC is Induced by Single-Domain Supervised Training

> **Subsection to write**: Show that the supervised objective on single-domain data is the direct cause of DSC.
> - Define domain features $x_d$ and class features $x_y$; domain features carry zero classification gain on a single-domain training set.
> - Supervised objective concentrates variance in class-predictive directions; domain directions are compressed out.
> - Connect to empirical diagnostics: fine-tuning a rich pretrained model monotonically collapses $r_\text{eff}(\Sigma)$ while FPR@95 rises.

### 3.3 Empirical Validation of DSC Predictions

> These experiments are direct, quantitative tests of the theoretical claims above.

| Prediction | Experiment | Expected Result |
|---|---|---|
| Single-domain training collapses $r_\text{eff}(\Sigma)$ | Fine-tuning trajectory: measure effective rank and FPR@95 jointly over training epochs | Rank drops monotonically; FPR@95 rises |
| DSC causes distance-metric failure (not class confusion) | Measure $\|P_\perp z\|$ (nullspace energy) for ID vs OOD samples | OOD has negligible null-space energy, confirming full suppression |
| Head insensitivity to domain directions | Measure $\|WP_\perp\|_\text{op}$ for CE-trained student | Near-zero: head is blind to $\mathcal{S}_\text{cls}^\perp$ |
| TGT reverses DSC | Measure $r_\text{eff}(\Sigma)$ pre/post TGT; correlate with FPR@95 trajectory | Rank recovers; FPR drops; monotone relationship |
| TGT gain is not explained by extra compute | Train CE for matched epochs; compare FPR@95 | No improvement; gain is TGT-specific |

---

## 4. Method: RA Score and Teacher-Guided Training

### 4.1 Class-Suppressed Teacher Residuals

Given frozen teacher $u(x) = T(x) \in \mathbb{R}^m$ (DinoV2 ViT-S/14) and training class means $\mu_c$, define:

$$
U = [\mu_1 - \mu, \ldots, \mu_C - \mu] \in \mathbb{R}^{m \times C}, \quad P_\text{cls} = U(U^\top U + \epsilon I)^{-1} U^\top
$$

$$
u_\text{dom}(x) = (I - P_\text{cls})(u(x) - \mu)
$$

This projects out between-class teacher directions, leaving a residual that emphasizes within-class variation (domain/style/acquisition cues), while requiring no class label at test time (see `docs_theory/TEACHER_RESIDUAL_AGREEMENT.md`, Section 2).

### 4.2 Variant A: Post-Hoc Ridge Regression (No Training Changes)

For settings where retraining is not feasible, a linear mapping $W \in \mathbb{R}^{d \times m}$ is fit by ridge regression on the training set:

$$
W = (V^\top V + \alpha I)^{-1} V^\top U_\text{dom}
$$

where $V \in \mathbb{R}^{N \times d}$ is the student feature matrix and $U_\text{dom} \in \mathbb{R}^{N \times m}$ is the matrix of class-suppressed teacher residuals. The predicted residual at inference is $\hat u_\text{dom}(x) = v(x) W$.

The RA disagreement score is then:

$$
s_\text{agree}(x) = \left\| \hat u_\text{dom}(x) - u_\text{dom}(x) \right\|_2
$$

On in-distribution data, $W$ fits well $\to$ low $s_\text{agree}$. On domain-shifted OOD data, the student's off-support features break the fit $\to$ high $s_\text{agree}$. This disagreement score serves as a soft domain penalty fused with MDS.

> **Note**: Variant A requires the teacher at inference (to compute $u_\text{dom}(x)$). It is most useful as a strong post-hoc baseline and as a diagnostic for whether teacher domain residuals are informative before committing to TGT.

### 4.3 Variant B: Teacher-Guided Training (TGT)

The student $S$ is augmented with a domain head $h$ (linear or shallow MLP) predicting $u_\text{dom}$. The combined loss is:

$$
\mathcal{L}_\text{TGT} = \mathcal{L}_\text{CE} + \lambda_\text{TGT} \cdot \mathcal{L}_\text{domain}, \quad \mathcal{L}_\text{domain} = \mathbb{E}_x \left\| h(v(x)) - u_\text{dom}(x) \right\|_2^2
$$

where $v(x) = S_\text{feat}(x)$ is the student feature vector.

> **Key effects of TGT on representation geometry** (from `docs/PLANT_TRA_PERFORMANCE_INVESTIGATION.md`, `docs_theory/summary_experiments_theory.md`):
> - Increases effective rank $r_\text{eff}(\Sigma_\text{student})$.
> - Redistributes variance from class-aligned subspace into domain-relevant directions.
> - After TGT, plain MDS in student space achieves near-zero FPR@95 on out-of-domain OOD.
> - Class accuracy preserved; near-OOD detection preserved or improved.

### 4.4 Teacher Feature Caching for Efficiency

Because the teacher is frozen, its residuals are deterministic per sample. Pre-computing a canonical teacher feature cache before training eliminates all teacher forward passes during training (see `docs/TEACHER_FEATURE_CACHE_TRAINING.md`):

- Memory: $N \times d_\text{teacher} \times 2\ \text{bytes}$ (float16); ~73 MB for 100k samples at $d=384$.
- Latency: one extra data pass at startup; zero teacher cost thereafter.
- Augmentation note: canonical center-crop features are used; student receives full random augmentation.

---

## 5. Method: MDS Soft Constant-RA Score

### 5.1 Core Idea

After TGT, the student's domain head outputs $\hat u_\text{dom}(x) = h(v(x))$. The **Constant-RA** variant replaces the per-sample teacher residual with its training-set mean:

$$
\mu_\text{const} = \mathbb{E}_\text{train}[\hat u_\text{dom}(x)]
$$

The disagreement signal then measures how far the domain head prediction deviates from this constant reference:

$$
d_\text{const}(x) = \sqrt{(r(x) - \mu_\text{const})^\top \Sigma_\text{const}^{-1} (r(x) - \mu_\text{const})}, \quad r(x) = \hat u_\text{dom}(x)
$$

**Why constant reference works:** Experiments on Colon and EuroSAT show the constant-teacher ablation achieves nearly identical AUROC to full per-sample RA Score (~0.978 vs ~0.978 on Colon; ~0.950 vs ~0.950 on EuroSAT). The student retains *dataset-specific statistical signatures* from training; the constant reference simply tests whether the domain head output drifts from the in-distribution cluster  no per-sample teacher evaluation is needed at inference (see `docs_theory/summary_experiments_theory.md`, Constant-Teacher Ablation).

### 5.2 Soft Fusion Scoring

All scores are z-normalized using training-set statistics, then blended:

**Training-set statistics:**
- Base: $\mu_\text{base},\, \sigma_\text{base}$ from MDS scores on training data.
- Domain: $\mu_d,\, \sigma_d$ from $d_\text{const}$ on training data.
- Threshold: $\tau_\text{norm} = \text{percentile}_p\!\left(\frac{d_\text{const} - \mu_d}{\sigma_d}\right)$ at percentile $p$ (e.g., 85th95th).

**Inference scoring** (for each sample $x$):

$$
s_\text{base} = \frac{-\text{MDS}(x) - \mu_\text{base}}{\sigma_\text{base}}, \quad s_d = \frac{d_\text{const}(x) - \mu_d}{\sigma_d}
$$

$$
\text{score}(x) = s_\text{base} - \gamma \cdot \max(0,\; s_d - \tau_\text{norm})
$$

Higher score $\to$ more ID-like. The soft excess term penalizes domain-atypical samples progressively, without hard masking (see `OpenOOD-main/CONSTANT_TRA_SOFT_BASE_SPEC.md`).

**Hyperparameters** (swept via `postprocessor_sweep`):
- $\gamma \in \{1, 5, 10\}$: blending strength; typical effective range $\gamma \approx 10$ for normalized scores.
- $p \in \{75, 85, 90, 95\}$: domain-atypicality threshold percentile.

### 5.3 Relationship to Other Constant-RA Variants

MDS Soft Constant-RA is one instance of the `ConstantTRASoftBasePostprocessor` architecture (see `OpenOOD-main/CONSTANT_TRA_SOFT_BASE_SPEC.md`). Identical soft-fusion logic applies to:
- **KNN Soft Constant-RA**: FAISS KNN as base score.
- **VIM Soft Constant-RA**: Virtual Logit Matching as base score.
- **MSP Soft Constant-RA**: Maximum Softmax Probability as base score.

MDS is the primary proposed base because it captures both class-conditional mean shift and covariance structure, and because TGT restores MDS sensitivity.

---

## 6. Experiments

### 6.1 Datasets

> **Fill in final dataset list.**



### 6.2 Main Results

> **Placeholder table  fill with locked numbers. Target claim: up to 90% FPR@95 reduction.**


> *Up to 90% FPR@95 reduction vs. CE + MDS on far-OOD. Insert final numbers.*

### 6.3 Ablations

#### A — Representation Recovery via TGT

# NOTE THIS IS NO LONGER RELEVANT SINCE WE ARE NOT INCLUDING REFINING ANYMORE 

| | Effective Rank | FPR@95 Far-OOD | FPR@95 Near-OOD |
|---|---|---|---|
| CE baseline | low (~3060) | high | moderate |
| + TGT (full) | recovered (~80150) | near-zero | preserved/improved |
| + extra CE epochs (control) | unchanged | unchanged | unchanged |

> Tests: DSC reversal is caused by TGT, not training compute; effective rank tracks domain sensitivity recovery.

#### B — Variant A vs Variant B vs Scoring Components

| Scoring | Far-OOD FPR | Near-OOD FPR | Notes |
|---|---|---|---|
| CE + RA Score Variant A (post-hoc ridge) | moderate | moderate | teacher needed at inference |
| TGT + MDS ($\gamma$=0; base only) | very low | preserved | teacher-free inference |
| TGT + MDS Soft Constant-RA ($\gamma$>0) | lowest | preserved/improved | teacher-free inference |
| TGT + MDS Hard Constant-RA | good far-OOD | may regress near-OOD |  |
| CE + MDS Soft Constant-RA (no TGT) | marginal | marginal | representation not recovered |

> Variant A provides a meaningful baseline without retraining; TGT is the primary representation fix; soft Constant-RA scoring adds calibrated improvement on top.

#### C — Constant-RA vs Full Per-Sample RA

| Teacher Reference | Far-OOD AUROC | Near-OOD FPR |
|---|---|---|
| Full RA Variant A (per-sample teacher) | ~0.978 (Colon) | comparable |
| Constant-RA (mean reference) | ~0.978 (Colon) | comparable |

> Constant-RA matches full per-sample RA, confirming inference-time teacher-free deployment.

#### D — $\gamma$ / Percentile Sweep

> Include heatmap figure of FPR@95 as a function of $\gamma \in \{1, 5, 10\}$ and $p \in \{75, 85, 90, 95\}$.
> Stable performance across a broad region; chosen operating point cited in main table.

#### E — Plant Dataset (Failure Case and Theory Boundary Condition)

On PlantVillage, TGT training *degrades* near-OOD MDS performance relative to CE baseline (FPR@95: 34.11 vs 14.83). Far-OOD remains strong (~1.81). Root cause: PlantVillage has low within-class domain diversity; the teacher residual is near-constant for all plant images, making the TGT domain objective uninformative. The soft Constant-RA signal provides no recovery. This failure is predicted by the DSC theory as a boundary condition: when teacher residual variance is near zero, $\mathcal{L}_\text{domain}$ gradients act as a variance-suppressing regularizer with no domain benefit. See `docs/PLANT_TRA_PERFORMANCE_INVESTIGATION.md` for detailed hypotheses and diagnostic experiments.

> **Include as an honest limitations example.** Diagnostic: compute teacher residual variance and R of ridge regression (Variant A) before applying TGT; low R signals an uninformative domain objective.

---

## 7. Conclusion

Teacher-Guided Training (TGT) with MDS Soft Constant-RA resolves the single-domain OOD detection problem by attacking its root cause  Domain-Sensitivity Collapse — at the representation level. By distilling class-suppressed domain residuals from a frozen multi-domain teacher into the supervised student during training, TGT restores the isotropic, domain-sensitive geometry needed for distance-based OOD scores to function. For settings where retraining is not feasible, RA Score Variant A (post-hoc ridge regression) provides a meaningful improvement without any training changes. The full TGT method:

- Requires **no teacher at inference**.
- Adds modest training overhead (optional caching further reduces cost; see `docs/TEACHER_FEATURE_CACHE_TRAINING.md`).
- Achieves up to **90% FPR@95 reduction** vs. standard MDS across multiple single-domain benchmarks.
- Degrades gracefully when teacher domain residual is uninformative (Plant; a predicted predicted boundary condition of DSC theory).

Future work: extend to settings with multi-source single-domain training; investigate data-efficient TGT schedules; analyze teacher domain diversity requirements for guaranteed DSC recovery.

---

## Checklist

### Theory
- [ ] Finalize DSC theorem (distance failure conditions; Theorem 1' in `theory_distance_failure_and_TRA_success.md`)
- [ ] Finalize logit-based (MSP/Energy) failure theorem under head subspace insensitivity
- [ ] Write DSC  Neural Collapse subsection (ETF  hostile to domain shift) in Section 3.1
- [ ] State 35 testable predictions in Section 3.3 linking $r_\text{eff}$, nullspace energy, $\|WP_\perp\|$ to OOD metrics
- [ ] Run fine-tuning trajectory experiment (effective rank vs FPR@95 vs training epoch)
- [ ] Run nullspace energy experiment ($\|P_\perp z\|$ for ID vs OOD)
- [ ] Run head insensitivity measurement ($\|WP_\perp\|$) pre/post TGT

### Method
- [ ] Confirm TGT training recipe (loss weight $\lambda_\text{TGT}$, schedule, domain head architecture) in Section 4.3
- [ ] Confirm ridge regression hyperparameter $\alpha$ and feature normalization for Variant A in Section 4.2
- [ ] Lock constant-RA scoring formula (soft fusion; `CONSTANT_TRA_SOFT_BASE_SPEC.md`) in Section 5
- [ ] Specify teacher caching strategy used in reported experiments (`TEACHER_FEATURE_CACHE_TRAINING.md`)

### Experiments
- [ ] Lock final FPR@95 / AUROC numbers for all datasets and methods
- [ ] Run extra-CE-epochs control experiment (confirm gains not explained by compute)
- [ ] Run effective rank / participation ratio trajectory during TGT training
- [ ] Run Plant diagnostic (teacher residual variance + R analysis using Variant A ridge fit)
- [ ] Run $\gamma$ / percentile sweep heatmap for MDS Soft Constant-RA

### Writing & Figures
- [ ] Pipeline figure: TGT training diagram + MDS Soft Constant-RA inference scoring
- [ ] Geometry figure: spectra / participation ratio (CE vs TGT)
- [ ] Score distribution figure: FPR@95 histograms / ROC curves for key dataset pairs
- [ ] Main results table (all methods  all datasets  near/far OOD)
- [ ] Ablation table (Variant A vs TGT, scoring components)
- [ ] Limitations section (Plant failure; Variant A teacher requirement; adjacent-OOD edge cases)
- [ ] Reproducibility checklist: seeds, dataset splits, teacher model ID, compute budget

---

## References (to add)

- DinoV2 (Oquab et al., 2023)  teacher model
- Neural Collapse (Papyan et al., 2020)  ETF geometry motivation for DSC
- Mahalanobis OOD Detection (Lee et al., 2018)  MDS base score
- KNN OOD (Sun et al., 2022)  comparison baseline
- VIM (Wang et al., 2022)  comparison baseline
- OpenOOD benchmark framework  evaluation setup
- Knowledge Distillation (Hinton et al., 2015)  related training paradigm
- SupCon (Khosla et al., 2020)  supervised contrastive baseline
- ReAct (Sun et al., 2021)  logit-based baseline
- Ridge Regression / Tikhonov regularization  Variant A fitting
