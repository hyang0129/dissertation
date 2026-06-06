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
