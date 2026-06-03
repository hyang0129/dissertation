"""paper/figures_src/render_compute_matched.py

Renders the §5.3 compute-matched figure: per-dataset panels showing AUROC vs
forward-pass count for K=1 activation/scalar baselines, K=2 P(true), and
K=10 sampling baselines.

Outputs:
  paper/generated/figures/compute_matched.pdf
  paper/generated/figures/compute_matched.numbers.csv

The sidecar lists every plotted point (method × dataset × model × AUROC × K)
plus the headline gap annotations. Figure captions cite via:

    \\result{fig.compute_matched}{popqa_llama_ours_vs_selfchecknli_delta}[3]

Reads paper/data/headline_results.csv only.
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

FIGURE_NAME = "compute_matched"
SOURCE_CSV = "headline_results.csv"

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

# (method_id, display_label, color, marker_size)
# Ours sits at K=1 and is highlighted. Sampling cluster (K=10) is red-ish.
METHODS = [
    ("contrastive_logprob_recon", "Ours",            "#1a3c75", 60),
    ("llmsknow_probe",            "LLMsKnow",        "#5a86c4", 38),
    ("linear_probe",              "Linear",          "#7ba4cc", 38),
    ("saplma",                    "SAPLMA",          "#9bb8d9", 38),
    ("act_vit",                   "ACT-ViT",         "#bcd0e5", 38),
    ("p_true",                    "P(true)",         "#b09abc", 38),
    ("se_length_normalized",      "SE (length-norm)", "#d6604d", 38),
    ("selfcheck_nli",             "SelfCheck-NLI",   "#b2182b", 38),
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
    parser.add_argument("--paper-dir", default="paper")
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
    fig, axes = plt.subplots(1, n_panels, figsize=(8.5, 2.6), sharey=True)

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
                if std > 0:
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

    # PopQA panel: annotate ours and best-K=10 marker (per §5.3 outline,
    # PopQA is the worst-case dataset where sampling baselines score highest).
    popqa_idx = DATASETS_ORDER.index("popqa")
    panel = axes[popqa_idx]
    for model_id, model_short, _ in MODELS:
        ours_mean, _, _ = cell(df, model_id, "popqa", "contrastive_logprob_recon")
        sc_mean, _, _ = cell(df, model_id, "popqa", "selfcheck_nli")
        if ours_mean is None or sc_mean is None:
            continue
        delta = ours_mean - sc_mean
        safe = f"popqa_{model_short.lower()}"
        sidecar_rows.append((f"{safe}_ours_vs_selfchecknli_delta", delta, "annotation"))
        # Single label per model on the panel: "Ours K=1: X.XX" near the ours dot.
        panel.annotate(
            f"{model_short}: {ours_mean:.3f}",
            xy=(1, ours_mean),
            xytext=(1.05, ours_mean + 0.012),
            fontsize=5.5,
            ha="left",
            color="#1a3c75",
        )
        panel.annotate(
            f"{sc_mean:.3f}",
            xy=(10, sc_mean),
            xytext=(7.5, sc_mean - 0.025),
            fontsize=5.5,
            ha="left",
            color="#b2182b",
        )

    # Aggregate-summary numbers for the §5.3 paragraph: mean ours K=1 vs mean
    # K=10 sampling, averaged across the five datasets.
    for model_id, model_short, _ in MODELS:
        ours_vals, se_vals, sc_vals = [], [], []
        for ds in DATASETS_ORDER:
            o, _, _ = cell(df, model_id, ds, "contrastive_logprob_recon")
            s, _, _ = cell(df, model_id, ds, "se_length_normalized")
            c, _, _ = cell(df, model_id, ds, "selfcheck_nli")
            if o is not None: ours_vals.append(o)
            if s is not None: se_vals.append(s)
            if c is not None: sc_vals.append(c)
        if ours_vals and se_vals:
            sidecar_rows.append(
                (f"{model_short.lower()}_mean_ours_vs_se_lengthnorm_delta",
                 (sum(ours_vals)/len(ours_vals)) - (sum(se_vals)/len(se_vals)),
                 "annotation"))
        if ours_vals and sc_vals:
            sidecar_rows.append(
                (f"{model_short.lower()}_mean_ours_vs_selfchecknli_delta",
                 (sum(ours_vals)/len(ours_vals)) - (sum(sc_vals)/len(sc_vals)),
                 "annotation"))

    # Both-models headline mean: averaging both models' deltas vs SE-length-norm.
    all_o, all_se, all_sc = [], [], []
    for model_id, _, _ in MODELS:
        for ds in DATASETS_ORDER:
            o, _, _ = cell(df, model_id, ds, "contrastive_logprob_recon")
            s, _, _ = cell(df, model_id, ds, "se_length_normalized")
            c, _, _ = cell(df, model_id, ds, "selfcheck_nli")
            if o is not None: all_o.append(o)
            if s is not None: all_se.append(s)
            if c is not None: all_sc.append(c)
    if all_o and all_se:
        sidecar_rows.append(
            ("both_models_mean_ours_vs_se_lengthnorm_delta",
             (sum(all_o)/len(all_o)) - (sum(all_se)/len(all_se)),
             "annotation"))
    if all_o and all_sc:
        sidecar_rows.append(
            ("both_models_mean_ours_vs_selfchecknli_delta",
             (sum(all_o)/len(all_o)) - (sum(all_sc)/len(all_sc)),
             "annotation"))

    # Legend (single, below all panels). Methods row + models row.
    method_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color,
                   markersize=6, label=label, markeredgecolor="white",
                   markeredgewidth=0.4)
        for _, label, color, _ in METHODS
    ]
    model_handles = [
        plt.Line2D([0], [0], marker=marker, color="w", markerfacecolor="#444",
                   markersize=6, label=label, markeredgecolor="white",
                   markeredgewidth=0.4)
        for _, label, marker in [(MODELS[0][0], "Llama", "o"),
                                  (MODELS[1][0], "Qwen3", "s")]
    ]
    leg1 = fig.legend(handles=method_handles, fontsize=6.5,
                      loc="lower center", bbox_to_anchor=(0.5, -0.08),
                      ncol=8, frameon=False, handlelength=1.0,
                      columnspacing=0.8)
    fig.add_artist(leg1)
    fig.legend(handles=model_handles, fontsize=6.5,
               loc="lower center", bbox_to_anchor=(0.5, -0.16),
               ncol=2, frameon=False, handlelength=1.0)

    fig.tight_layout(rect=(0, 0.04, 1, 1))
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
            generator="paper/figures_src/render_compute_matched.py",
            source_data=str(data_csv),
        )
        fh.write("label,value,role\n")
        for label, value, role in sidecar_rows:
            fh.write(f"{label},{value:.6g},{role}\n")
    print(f"  Written sidecar: {out_sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
