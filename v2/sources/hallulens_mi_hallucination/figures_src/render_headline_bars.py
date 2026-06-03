"""paper/figures_src/render_headline_bars.py

Renders the §5.2 headline figure: grouped bar chart comparing four methods
(ours, ACT-ViT, Linear probe, SelfCheckGPT-NLI) across five datasets, both
models shown side-by-side within each dataset cluster.

Outputs:
  paper/generated/figures/headline_bars.pdf
  paper/generated/figures/headline_bars.numbers.csv

The sidecar lists every bar height, error-bar half-width, and decisive-cell
annotation delta. Figure captions cite via:

    \\result{fig.headline_bars}{popqa_llama_ours_auroc}[3]
    \\result{fig.headline_bars}{popqa_llama_ours_vs_actvit_delta}[3]

Pure pandas + matplotlib; reads paper/data/headline_results.csv only.
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

FIGURE_NAME = "headline_bars"
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
    ("Llama-3.1-8B-Instruct", "Llama"),
    ("Qwen3-8B", "Qwen3"),
]

# (method_id, display_label, color). Ours is highlighted; baselines are
# graded by class (activation-space probes blue-ish, sampling red).
METHODS = [
    ("contrastive_logprob_recon", "Ours (Contrastive+Recon)", "#1a3c75"),
    ("act_vit",                   "ACT-ViT",                  "#5a86c4"),
    ("linear_probe",              "Linear probe",             "#9bb8d9"),
    ("selfcheck_nli",             "SelfCheckGPT-NLI (K=10)",  "#d6604d"),
]


def write_sidecar_header(fh, generator: str, source_data: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fh.write(f"# generator: {generator}\n")
    fh.write(f"# source_data: {source_data}\n")
    fh.write(f"# generated: {now}\n")


def load_grid(data_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(data_csv, comment="#")
    method_ids = [m[0] for m in METHODS]
    model_ids = [m[0] for m in MODELS]
    df = df[
        df["dataset"].isin(DATASETS_ORDER)
        & df["model"].isin(model_ids)
        & df["method"].isin(method_ids)
    ].copy()
    return df


def cell(df: pd.DataFrame, model: str, dataset: str, method: str) -> tuple[float | None, float | None]:
    row = df[(df["model"] == model) & (df["dataset"] == dataset) & (df["method"] == method)]
    if row.empty:
        return None, None
    return float(row["auroc_mean"].iloc[0]), float(row["auroc_std"].iloc[0])


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

    df = load_grid(data_csv)

    # --- Layout: dataset clusters along x; within each, Llama-block then
    # Qwen-block, each with 4 method bars side-by-side. Small gap between
    # model blocks within a cluster, larger gap between dataset clusters.
    n_methods = len(METHODS)
    n_models = len(MODELS)
    bar_w = 0.10
    intra_model_gap = 0.0          # bars within a model block touch
    inter_model_gap = 0.08         # gap between Llama and Qwen blocks within one dataset
    inter_dataset_gap = 0.40       # gap between dataset clusters
    block_w = n_methods * bar_w + (n_methods - 1) * intra_model_gap
    cluster_w = n_models * block_w + (n_models - 1) * inter_model_gap

    # x-coordinate of each individual bar
    bar_x: dict[tuple[str, str, str], float] = {}  # (dataset, model, method) -> x
    cluster_centers: dict[str, float] = {}
    x_cursor = 0.0
    for ds in DATASETS_ORDER:
        cluster_start = x_cursor
        for mi, (model_id, _) in enumerate(MODELS):
            block_start = cluster_start + mi * (block_w + inter_model_gap)
            for mj, (method_id, _, _) in enumerate(METHODS):
                bar_x[(ds, model_id, method_id)] = block_start + mj * (bar_w + intra_model_gap) + bar_w / 2
        cluster_centers[ds] = cluster_start + cluster_w / 2
        x_cursor = cluster_start + cluster_w + inter_dataset_gap

    fig, ax = plt.subplots(figsize=(7.2, 3.2))

    sidecar_rows: list[tuple[str, float, str]] = []

    # Draw bars
    for ds in DATASETS_ORDER:
        for model_id, model_short in MODELS:
            for method_id, method_label, color in METHODS:
                mean, std = cell(df, model_id, ds, method_id)
                if mean is None:
                    continue
                x = bar_x[(ds, model_id, method_id)]
                # Llama bars solid, Qwen hatched, so the model is readable
                # without legend hunting.
                hatch = "" if model_short == "Llama" else "////"
                ax.bar(
                    x, mean,
                    width=bar_w * 0.95,
                    color=color,
                    edgecolor="white",
                    linewidth=0.4,
                    hatch=hatch,
                    yerr=std if std > 0 else None,
                    error_kw={"elinewidth": 0.6, "capsize": 1.2, "ecolor": "#222"},
                )
                # Sidecar: bar height + std as half-width
                safe_method = method_id.replace("_", "")
                key_prefix = f"{ds}_{model_short.lower()}_{safe_method}"
                sidecar_rows.append((f"{key_prefix}_auroc", mean, "data"))
                if std > 0:
                    sidecar_rows.append((f"{key_prefix}_std", std, "data"))

    # Decisive-cell annotations: ours vs best_competitor where |delta| > std_sum.
    # We highlight cells where ours WINS clearly or LOSES clearly to ACT-ViT.
    for ds in DATASETS_ORDER:
        for model_id, model_short in MODELS:
            ours_mean, ours_std = cell(df, model_id, ds, "contrastive_logprob_recon")
            actvit_mean, actvit_std = cell(df, model_id, ds, "act_vit")
            if ours_mean is None or actvit_mean is None:
                continue
            delta = ours_mean - actvit_mean
            band = max(ours_std, actvit_std)
            decisive = abs(delta) > band
            safe = f"{ds}_{model_short.lower()}"
            sidecar_rows.append((f"{safe}_ours_vs_actvit_delta", delta, "annotation"))
            if decisive:
                # Place a small arrow above the ours bar pointing to the
                # ACT-ViT bar to communicate direction visually.
                x_ours = bar_x[(ds, model_id, "contrastive_logprob_recon")]
                x_act = bar_x[(ds, model_id, "act_vit")]
                y = max(ours_mean, actvit_mean) + 0.025
                ax.annotate(
                    f"{delta:+.3f}",
                    xy=(x_act, y),
                    xytext=(x_ours, y + 0.015),
                    fontsize=5.5,
                    ha="center",
                    color="#222",
                    arrowprops=dict(arrowstyle="-|>", color="#222", lw=0.5,
                                     shrinkA=0.5, shrinkB=0.5),
                )

    # X tick labels at cluster centers
    ax.set_xticks([cluster_centers[d] for d in DATASETS_ORDER])
    ax.set_xticklabels([DATASET_LABELS[d] for d in DATASETS_ORDER], fontsize=8)
    ax.set_ylabel("AUROC", fontsize=9)
    ax.set_ylim(0.45, 0.95)
    ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9])
    ax.tick_params(axis="y", labelsize=7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle=":", linewidth=0.4, alpha=0.6)
    ax.set_axisbelow(True)

    # Combined legend: methods (color) + models (hatch). Two columns.
    method_handles = [
        plt.Rectangle((0, 0), 1, 1, color=color, label=label)
        for _, label, color in METHODS
    ]
    model_handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor="#888", hatch="", label="Llama-3.1-8B"),
        plt.Rectangle((0, 0), 1, 1, facecolor="#888", hatch="////", label="Qwen3-8B"),
    ]
    leg1 = ax.legend(handles=method_handles, fontsize=6.5, loc="upper left",
                     bbox_to_anchor=(0.0, 1.02), ncol=2, frameon=False,
                     handlelength=1.2, columnspacing=0.8)
    ax.add_artist(leg1)
    ax.legend(handles=model_handles, fontsize=6.5, loc="upper right",
              bbox_to_anchor=(1.0, 1.02), ncol=2, frameon=False,
              handlelength=1.2, columnspacing=0.8)

    fig.tight_layout()
    fig.savefig(out_pdf)
    plt.close(fig)
    print(f"  Written figure: {out_pdf}")

    # Sidecar
    sidecar_rows.append(("y_axis_min", 0.45, "axis"))
    sidecar_rows.append(("y_axis_max", 0.95, "axis"))
    with open(out_sidecar, "w") as fh:
        write_sidecar_header(
            fh,
            generator="paper/figures_src/render_headline_bars.py",
            source_data=str(data_csv),
        )
        fh.write("label,value,role\n")
        for label, value, role in sidecar_rows:
            fh.write(f"{label},{value:.6g},{role}\n")
    print(f"  Written sidecar: {out_sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
