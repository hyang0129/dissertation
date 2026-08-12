# Dissertation Defense Slides — v1-Based Upgrade Plan

**Source deck:** `v1/dissertation_proposal_slides.tex`
**Defense source:** `v2/defense_slides.tex`
**Target:** 36 numbered main slides, approximately 40–45 minutes
**Backup:** 10 technical slides plus references, excluded from the main count

## 1. Base-deck decision

The final defense uses the v1 proposal deck as its presentation base. It retains:

- 16:9 Beamer with the Madrid theme and default color theme;
- the original title-page hierarchy;
- the two-part section/status and frame-count footer;
- the proposal's Introduction → Research Overview → three deep dives → Conclusion rhythm;
- bold-led `itemize` lists, centered equations, image/text columns, and full-width result figures;
- blue, green, and red as navigational accents for the three contributions.

The page count increases from 30 proposal-content slides to 36 defense-content
slides because Chapters 5 and 6 now contain completed methods, results, ablations,
and limitations that did not exist in the proposal.

## 2. Scientific upgrade

The talk defends one thesis:

> A detector can use only the distinctions available in its representation. When
> the relevant structure is absent, detection has a principled limit; when it is
> suppressed, training can restore it; when it is retained, a readout can expose it.

The three studies provide different kinds of evidence:

| Study | Role | Defensible claim |
|---|---|---|
| Label Blindness | Failure | Under independence and minimal sufficiency, the learned representation contains no information about the required OOD label. |
| DSC and TGT | Diagnosis and recovery | DSC identifies a geometric sensitivity failure; TGT restores useful directions and improves the evaluated scorers. |
| Hallucination detection | Detection | Cross-layer activations support a principled one-class readout that reaches parity with the strongest engineered activation probe. |

Only Label Blindness is an impossibility result. DSC provides diagnostic bounds,
and the hallucination chapter provides a feasibility argument plus empirical
evidence.

## 3. Main-deck sequence

### Introduction and overview — slides 1–7

1. **Title** — final dissertation title, defense type, author, RIT, August 5, 2026.
2. **Why confidence can be misleading** — explain unfamiliar inputs and unsupported answers before introducing specialist terminology.
3. **Two lenses tell us what a detector can recover** — define a representation, then introduce information theory as presence and geometry as accessibility.
4. **Presentation Roadmap** — failure → recovery → detection, followed by synthesis.
5. **Contribution 1: Label Blindness** — conditional theorem, Adjacent OOD, and headline evidence.
6. **Contribution 2: DSC and recovery** — low-rank geometry, TGT, and the diagnostic claim boundary.
7. **Contribution 3: cross-layer hallucination detection** — one-class method, parity result, and access regime.

### Label Blindness — slides 8–14

8. **Motivating Example: When Features Mislead** — reuse the v1 GradCAM figure with a bounded interpretation.
9. **Formal Problem Definition** — surrogate target, target label, independent feature components, and minimal sufficiency.
10. **Information-Theoretic Analysis** — minimality removes the unused component; therefore the target label is independent of the representation.
11. **Adjacent OOD Evaluation Paradigm** — contrast far, near, and adjacent OOD; state the actual three-split protocol.
12. **Empirical Validation Results** — data-backed Faces/Cars/Food AUROC plot.
13. **What the Result Establishes** — explicit established/not-established comparison replacing the proposal's unsupported hybrid method.
14. **Key Takeaways** — theorem, benchmark, practical implication, and ICLR 2025 status.

### DSC and TGT — slides 15–22

15. **Motivating Question: What Do We Really Learn?** — reuse the v1 butterfly image and broaden the question from class to domain sensitivity.
16. **Mathematical Formalization** — covariance decomposition, class subspace, DSC, and effective rank.
17. **Theoretical Analysis of Collapse** — diagnostic distance and logit-score bounds with an explicit scope statement.
18. **Empirical Demonstration of DSC** — CE versus TGT effective-rank figure over eight datasets.
19. **Teacher-Guided Training Methodology** — frozen teacher, class-suppressed residual, cosine objective, and student-only inference.
20. **Implementation and Validation** — out-of-domain FPR@95 across eight scorers.
21. **Recovered Geometry Tracks Lower OOD Error** — effective-rank gains versus FPR@95 reductions.
22. **Key Takeaways** — diagnostic contribution, method contribution, limitations, and under-review status.

### Hallucination detection — slides 23–31

23. **Information-Theoretic Framework** — cross-layer dependence, InfoNCE floor, and the separation between architectural dependence and label relevance.
24. **One-Class Contrastive Learning** — layer-pair views, truthful positives, hallucination instance consistency, and symmetric-supervision prediction.
25. **System Architecture Details** — activation sequences, progressive compressor, two loss channels, and KNN truthful bank.
26. **Experimental Design and Datasets** — two models, five datasets, three signal families, five seeds, and the operational label.
27. **Results and Performance Analysis** — parity with ACT-ViT, stated without leaderboard escalation.
28. **Single-Pass Readers versus Ten-Sample Methods** — compute comparison and the caveat that ACT-ViT shares the same advantage.
29. **Ablations Identify the Supervision That Matters** — 2×2 channel attribution and qualitative symmetric-SupCon failure; exact symmetric values remain gated.
30. **Cross-Dataset Transfer** — competitive transfer with the Natural Questions limitation visible.
31. **Key Takeaways** — feasibility, method, empirical conclusion, and study scope.

### Synthesis and close — slides 32–36

32. **Three States of the Signal** — absent, suppressed, and retained; failure → recovery → detection.
33. **Different Contribution Types and Claim Strengths** — theorem, diagnostic intervention, and feasibility/readout evidence.
34. **Limitations Define the Next Experiments** — one concrete limitation and next step for each study.
35. **Start with the Representation** — practical intervention order and final thesis sentence.
36. **Questions and Discussion** — preserve the minimal v1 closing layout.

## 4. Proposal material retained, replaced, and retired

| v1 material | Defense decision |
|---|---|
| Madrid theme, title structure, footer, and section rhythm | Retain directly. |
| Reliability motivation | Rewrite for a non-specialist audience. |
| Information Theory Foundations | Expand to information theory plus representation geometry. |
| Three contribution previews | Retain, but convert predictions into completed claims and evidence. |
| Label Blindness GradCAM, problem setup, Adjacent OOD, and results | Retain structurally; correct theorem assumptions, protocol, and numbers. |
| Proposal AUC guarantee and universal compression language | Replace with the actual minimal-sufficiency and independence result. |
| Hybrid OOD solution | Retire; replace with theorem scope. |
| Domain Feature Collapse and information-bottleneck theorem | Retire; replace with geometric DSC. |
| Domain filtering and two-stage detector | Retire; replace with TGT. |
| Query–response MI threshold | Retire; replace with cross-layer feasibility and trainability. |
| Projected hallucination models, latency, and AUROC targets | Retire; replace with measured experiments. |
| Research timeline and expected impact | Retire; replace with synthesis, limitations, and intervention order. |

## 5. Figures and number discipline

Main result figures are generated from v2 CSV sources:

- `defense_label_blindness_auroc.pdf`;
- `defense_dsc_geometry.pdf`;
- `defense_dsc_fpr95.pdf`;
- `hd_headline.pdf`;
- `hd_compute_matched.pdf`;
- `defense_hallu_attribution.pdf`;
- `hd_transfer.pdf`.

The mechanism figure `dsc_rank_vs_fpr95_gains.png` and the v1 GradCAM and
butterfly figures are reused. Displayed numeric results resolve through
`macros.tex` and `generated/values.tex`; new charts carry `.numbers.csv`
sidecars.

## 6. Backup bank

1. OOD metrics: AUROC and FPR@95.
2. Label Blindness proof chain.
3. Selected Adjacent-OOD table.
4. DSC diagnostic bounds.
5. Out-of-domain versus in-domain TGT table.
6. TGT objective and inference path.
7. Teacher-guidance-strength ablation.
8. Formal hallucination feasibility argument.
9. Hallucination evaluation grid.
10. Hallucination-study scope and unresolved Natural Questions result.
11. References generated from `references.bib`.

## 7. Timing and cut path

| Block | Slides | Target time |
|---|---:|---:|
| Introduction and overview | 1–7 | 7 min |
| Label Blindness | 8–14 | 8 min |
| DSC and TGT | 15–22 | 10 min |
| Hallucination detection | 23–31 | 12 min |
| Synthesis and close | 32–35 | 5 min |
| Questions | 36 | — |

For a shorter talk, cut slides 7, 13, 17, 21, 26, 28, and 30 before compressing
the remaining explanations.

## 8. Build

From `v2/`:

```bash
make PYTHON=../.venv/bin/python slides
```

The number pipeline currently emits one harmless unresolved-macro warning because
it scans a `\resultPM{...}` example inside a comment at the top of
`chapters/04_label_blindness.tex`. It is not an unresolved value used by the deck.
