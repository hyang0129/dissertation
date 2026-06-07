"""figures_src/render_compute_matched.py

Renders the Ch.6 compute-matched figure (sec:hd:compute): per-dataset panels
showing AUROC vs forward-pass count K. The point is that our detector and the
other single-pass (K=1) probes operate at a fraction of the inference budget of
the K=10 sampling baselines, so any AUROC parity with sampling methods comes for
roughly 1/10th the compute. K is read directly from the data
(forward_pass_count): K=1 for activation/scalar probes, K=2 for P(true), K=10
for the sampling cluster.

HONESTY DISCIPLINE
------------------
This figure makes a *compute* argument, not a *dominance* argument. Our method
is one of several K=1 points; ACT-ViT (the strongest learned competitor) shares
the same K=1 column and is plotted in the same style, so the figure never
implies our method stands alone at low compute. No method is bolded or enlarged
beyond legibility. The NQ panel inherits the headline losses to ACT-ViT and they
remain visible as two overlapping K=1 points.

Outputs:
  generated/figures/hd_compute_matched.pdf
  generated/figures/hd_compute_matched.numbers.csv

Reads data/hallu_headline.csv only.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
import pandas as pd

FIGURE_NAME = "hd_compute_matched"
SOURCE_CSV = "hallu_headline.csv"

DATASETS_ORDER = ["hotpotqa", "nq", "popqa", "sciq", "searchqa"]
DATASET_LABELS = {
    "hotpotqa": "HotpotQA",
    "nq": "NQ",
    "popqa": "PopQA",
    "sciq": "SciQ",
    "searchqa": "SearchQA",
}

MODELS = [
    ("Llama-3.1-8B-Instruct", "Llama", "o"),
    ("Qwen3-8B",              "Qwen3", "s"),
]

# (method_id, display_label, color, marker_size). Our method and ACT-ViT both
# sit at K=1; sampling cluster (K=10) graded toward red. Our marker is slightly
# larger only so it is locatable, not to imply superiority.
METHODS = [
    ("contrastive_logprob_recon", "Contrastive+Recon (ours)", "#1a3c75", 55),
    ("act_vit",                   "ACT-ViT",                  "#5a86c4", 40),
    ("llmsknow_probe",            "LLMsKnow",                 "#6f9bc9", 32),
    ("linear_probe",              "Linear",                   "#9bb8d9", 32),
    ("saplma",                    "SAPLMA",                   "#bcd0e5", 32),
    ("p_true",                    "P(true)",                  "#b09abc", 32),
    ("se_length_normalized",      "SE (length-norm)",         "#e08214", 32),
    ("se_semantic_entropy",       "Semantic entropy",         "#d6604d", 32),
    ("selfcheck_nli",             "SelfCheck-NLI",            "#b2182b", 32),
]


def write_sidecar_header(fh, generator: str, source_data: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fh.write(f"# generator: {generator}\n")
    fh.write(f"# source_data: {source_data}\n")
    fh.write(f"# generated: {now}\n")


def cell(df: pd.DataFrame, model: str, dataset: str, method: str):
    row = df[(df["model"] == model) & (df["dataset"] == dataset) & (df["method"] == method)]
    if row.empty:
        return None, None, None
    return (
        float(row["auroc_mean"].iloc[0]),
        float(row["auroc_std"].iloc[0]),
        int(row["forward_pass_count"].iloc[0]),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", default=".")
    args = parser.parse_args(argv)

    paper_dir = Path(args.paper_dir)
    data_csv = paper_dir / "data" / SOURCE_CSV
    out_dir = paper_dir / "generated" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = out_dir / f"{FIGURE_NAME}.pdf"
    out_sidecar = out_dir / f"{FIGURE_NAME}.numbers.csv"

    if not data_csv.exists():
        print(f"ERROR: {data_csv} not found.", file=sys.stderr)
        return 1

    df = pd.read_csv(data_csv, comment="#")

    n_panels = len(DATASETS_ORDER)
    fig, axes = plt.subplots(1, n_panels, figsize=(8.5, 2.8), sharey=True)

    sidecar_rows: list[tuple[str, float, str]] = []

    for ax, ds in zip(axes, DATASETS_ORDER):
        for method_id, method_label, color, msize in METHODS:
            for model_id, model_short, marker in MODELS:
                mean, std, k = cell(df, model_id, ds, method_id)
                if mean is None:
                    continue
                ax.scatter(
                    k, mean,
                    s=msize, marker=marker, c=color,
                    edgecolors="white", linewidths=0.5,
                    zorder=3,
                )
                safe_method = method_id.replace("_", "")
                key_prefix = f"{ds}_{model_short.lower()}_{safe_method}"
                sidecar_rows.append((f"{key_prefix}_auroc", mean, "data"))
                sidecar_rows.append((f"{key_prefix}_k", float(k), "data"))
                if std and std > 0:
                    sidecar_rows.append((f"{key_prefix}_std", std, "data"))

        ax.set_xscale("log")
        ax.set_xticks([1, 2, 10])
        ax.set_xticklabels(["1", "2", "10"], fontsize=7)
        ax.set_xlim(0.7, 14.0)
        ax.set_xlabel("forward passes (K)", fontsize=7.5)
        ax.set_title(DATASET_LABELS[ds], fontsize=8, pad=2)
        ax.tick_params(axis="y", labelsize=7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(True, which="both", linestyle=":", linewidth=0.4, alpha=0.5)
        ax.set_axisbelow(True)

    axes[0].set_ylabel("AUROC", fontsize=9)
    axes[0].set_ylim(0.45, 0.95)

    # Aggregate compute-vs-AUROC deltas for the prose: mean(ours, K=1) vs the
    # mean of the two sampling baselines (K=10), per model and pooled. Reported
    # as the AUROC difference achieved at 1/10th the forward-pass budget.
    def mean_over(model_id, method_id):
        vals = []
        for ds in DATASETS_ORDER:
            m, _, _ = cell(df, model_id, ds, method_id)
            if m is not None:
                vals.append(m)
        return sum(vals) / len(vals) if vals else None

    all_o, all_se, all_sc = [], [], []
    for model_id, model_short, _ in MODELS:
        o = mean_over(model_id, "contrastive_logprob_recon")
        se = mean_over(model_id, "se_length_normalized")
        sc = mean_over(model_id, "selfcheck_nli")
        if o is not None and se is not None:
            sidecar_rows.append((f"{model_short.lower()}_mean_ours_vs_se_lengthnorm_delta", o - se, "annotation"))
        if o is not None and sc is not None:
            sidecar_rows.append((f"{model_short.lower()}_mean_ours_vs_selfchecknli_delta", o - sc, "annotation"))
        for ds in DATASETS_ORDER:
            mo, _, _ = cell(df, model_id, ds, "contrastive_logprob_recon")
            ms, _, _ = cell(df, model_id, ds, "se_length_normalized")
            mc, _, _ = cell(df, model_id, ds, "selfcheck_nli")
            if mo is not None: all_o.append(mo)
            if ms is not None: all_se.append(ms)
            if mc is not None: all_sc.append(mc)
    if all_o and all_se:
        sidecar_rows.append(("both_models_mean_ours_vs_se_lengthnorm_delta",
                             sum(all_o)/len(all_o) - sum(all_se)/len(all_se), "annotation"))
    if all_o and all_sc:
        sidecar_rows.append(("both_models_mean_ours_vs_selfchecknli_delta",
                             sum(all_o)/len(all_o) - sum(all_sc)/len(all_sc), "annotation"))

    method_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color,
                   markersize=6, label=label, markeredgecolor="white",
                   markeredgewidth=0.4)
        for _, label, color, _ in METHODS
    ]
    model_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#444",
                   markersize=6, label="Llama-3.1-8B", markeredgecolor="white",
                   markeredgewidth=0.4),
        plt.Line2D([0], [0], marker="s", color="w", markerfacecolor="#444",
                   markersize=6, label="Qwen3-8B", markeredgecolor="white",
                   markeredgewidth=0.4),
    ]
    leg1 = fig.legend(handles=method_handles, fontsize=6.2,
                      loc="lower center", bbox_to_anchor=(0.5, -0.10),
                      ncol=5, frameon=False, handlelength=1.0,
                      columnspacing=0.8)
    fig.add_artist(leg1)
    fig.legend(handles=model_handles, fontsize=6.2,
               loc="lower center", bbox_to_anchor=(0.5, -0.20),
               ncol=2, frameon=False, handlelength=1.0)

    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)
    print(f"  Written figure: {out_pdf}")

    sidecar_rows.append(("y_axis_min", 0.45, "axis"))
    sidecar_rows.append(("y_axis_max", 0.95, "axis"))
    sidecar_rows.append(("x_axis_min", 0.7, "axis"))
    sidecar_rows.append(("x_axis_max", 14.0, "axis"))

    with open(out_sidecar, "w") as fh:
        write_sidecar_header(
            fh,
            generator="figures_src/render_compute_matched.py",
            source_data=str(data_csv),
        )
        fh.write("label,value,role\n")
        for label, value, role in sidecar_rows:
            fh.write(f"{label},{value:.6g},{role}\n")
    print(f"  Written sidecar: {out_sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
