# figures/ — baked / external figures (reference only)

For figures that **cannot be re-rendered from data** by a `figures_src/*.py`
script (e.g. GradCAM heatmaps that need a trained model). Distinct from
`figures_src/` (renderers → `generated/figures/`) and from `generated/figures/`
(build output).

Per `../sources/README.md`: a baked figure reused from a source tree is copied
into the build with its origin noted here.

| File | Origin | Used in |
|---|---|---|
| `gradcam_example_faces.png` | `sources/iclr2025_label_blindness/gradcam_example_faces.png` (ICLR 2025 camera-ready) | Ch.4 (Label Blindness), Fig. `fig:grad` |
| `dsc_rank_vs_fpr95_gains.png` | `sources/eccv2026_domain_feature_collapse/figures/effective_rank_tgt_improvement_rank_vs_fpr95_horizontal.png` (ECCV 2026 submission); baked copy, not re-rendered | Ch.5 (DSC/TGT), Fig. `fig:dsc:rank-fpr-gains` |
| `dsc_eurosat_lambda_ablation.png` | `sources/eccv2026_domain_feature_collapse/figures/eurosat_lambda_ablation_farood_fpr95.png` (ECCV 2026 submission); baked copy, not re-rendered | Ch.5 (DSC/TGT), Fig. `fig:dsc:eurosat-lambda` |
| `dsc_teacher_compare.jpg` | `sources/eccv2026_domain_feature_collapse/figures/teachercompare.jpg` (ECCV 2026 submission; commented-out conceptual schematic in source); baked copy, not re-rendered | Ch.5 (DSC/TGT), Fig. `fig:dsc:teacher-compare` |
