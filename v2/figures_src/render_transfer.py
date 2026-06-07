"""figures_src/render_transfer.py

Renders the Ch.6 cross-dataset transfer figure (sec:hd:transfer): for each
model, a grouped bar chart of in-domain vs out-of-domain AUROC per detector.
Out-of-domain means trained on one source dataset and evaluated on the four
held-out targets, averaged. The figure shows that the learned axis transfers
(out-of-domain AUROC stays well above chance) and that our Contrastive+Recon
detector tracks the strongest learned competitor, ACT-ViT, under transfer.

HONESTY DISCIPLINE
------------------
ACT-ViT is plotted directly beside our method in every group so transfer parity
is read directly, not implied. The claim is "matches-or-outperforms in the
mean": where our out-of-domain mean is within the error bars of ACT-ViT's, the
two are treated as tied (annotated "tie"); a directional delta is annotated only
when the gap exceeds the larger seed std. Error bars are the seed-to-seed std
straight from the data, so the reader can see how thin the margins are.

Outputs:
  generated/figures/hd_transfer.pdf
  generated/figures/hd_transfer.numbers.csv

Reads data/hallu_transfer_summary.csv (primary) with schema:
  model,method,scope,auroc_mean,auroc_std,n_seeds,n_cells_used,n_cells_total
scope in {in_domain, out_of_domain}.
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

FIGURE_NAME = "hd_transfer"
SOURCE_CSV = "hallu_transfer_summary.csv"

MODELS = [
    ("Llama-3.1-8B-Instruct", "Llama-3.1-8B"),
    ("Qwen3-8B", "Qwen3-8B"),
]

# (method_id, display_label). Our method first, ACT-ViT (strongest learned
# competitor) directly adjacent for a fair parity read.
METHODS = [
    ("contrastive_logprob_recon", "Contrastive+Recon (ours)"),
    ("act_vit",                   "ACT-ViT"),
    ("llmsknow_probe",            "LLMsKnow"),
    ("saplma",                    "SAPLMA"),
]

# Two scopes, lighter shade for out-of-domain.
SCOPES = [
    ("in_domain", "in-domain", 1.00),
    ("out_of_domain", "out-of-domain (transfer)", 0.55),
]

METHOD_COLORS = {
    "contrastive_logprob_recon": "#1a3c75",
    "act_vit":                   "#5a86c4",
    "llmsknow_probe":            "#9bb8d9",
    "saplma":                    "#c2cfe0",
}


def write_sidecar_header(fh, generator: str, source_data: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fh.write(f"# generator: {generator}\n")
    fh.write(f"# source_data: {source_data}\n")
    fh.write(f"# generated: {now}\n")


def cell(df: pd.DataFrame, model: str, method: str, scope: str):
    row = df[(df["model"] == model) & (df["method"] == method) & (df["scope"] == scope)]
    if row.empty:
        return None, None
    return float(row["auroc_mean"].iloc[0]), float(row["auroc_std"].iloc[0])


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

    fig, axes = plt.subplots(1, len(MODELS), figsize=(7.4, 3.2), sharey=True)

    sidecar_rows: list[tuple[str, float, str]] = []

    n_methods = len(METHODS)
    n_scopes = len(SCOPES)
    bar_w = 0.34
    group_gap = 0.5
    group_w = n_scopes * bar_w
    # x positions: one group per method.
    group_centers = [i * (group_w + group_gap) + group_w / 2 for i in range(n_methods)]

    for ax, (model_id, model_label) in zip(axes, MODELS):
        for mi, (method_id, method_label) in enumerate(METHODS):
            base = mi * (group_w + group_gap)
            color = METHOD_COLORS[method_id]
            for si, (scope_id, scope_label, alpha) in enumerate(SCOPES):
                mean, std = cell(df, model_id, method_id, scope_id)
                if mean is None:
                    continue
                x = base + si * bar_w + bar_w / 2
                ax.bar(
                    x, mean,
                    width=bar_w * 0.9,
                    color=color,
                    alpha=alpha,
                    edgecolor="white",
                    linewidth=0.4,
                    yerr=std if std and std > 0 else None,
                    error_kw={"elinewidth": 0.6, "capsize": 1.4, "ecolor": "#222"},
                )
                safe_m = method_id.replace("_", "")
                key = f"{model_label.lower().replace('-', '').replace('.', '')}_{safe_m}_{scope_id}"
                sidecar_rows.append((f"{key}_auroc", mean, "data"))
                if std and std > 0:
                    sidecar_rows.append((f"{key}_std", std, "data"))

        # Parity annotation: ours vs ACT-ViT on the out-of-domain (transfer)
        # scope, the one this figure is about. Tie unless |delta| > larger std.
        ours_mean, ours_std = cell(df, model_id, "contrastive_logprob_recon", "out_of_domain")
        act_mean, act_std = cell(df, model_id, "act_vit", "out_of_domain")
        if ours_mean is not None and act_mean is not None:
            delta = ours_mean - act_mean
            band = max(ours_std or 0.0, act_std or 0.0)
            decisive = abs(delta) > band
            mtag = model_label.lower().replace("-", "").replace(".", "")
            sidecar_rows.append((f"{mtag}_ood_ours_vs_actvit_delta", delta, "annotation"))
            sidecar_rows.append((f"{mtag}_ood_ours_vs_actvit_decisive", 1.0 if decisive else 0.0, "annotation"))
            label = (f"{delta:+.3f}" if decisive else "tie")
            txt_color = "#222" if delta >= 0 else "#8a1f1f"
            ymax = max(ours_mean + (ours_std or 0.0), act_mean + (act_std or 0.0))
            ax.annotate(
                f"ours vs ACT-ViT\n(transfer): {label}",
                xy=(group_w / 2, ymax + 0.02),
                fontsize=5.6, ha="center", va="bottom",
                color=txt_color,
            )

        ax.set_xticks(group_centers)
        ax.set_xticklabels([m[1] for m in METHODS], fontsize=6.0, rotation=20, ha="right")
        ax.set_title(model_label, fontsize=8.5, pad=2)
        ax.axhline(0.5, color="#888", linestyle="--", linewidth=0.6, alpha=0.7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", linestyle=":", linewidth=0.4, alpha=0.6)
        ax.set_axisbelow(True)

    axes[0].set_ylabel("AUROC", fontsize=9)
    axes[0].set_ylim(0.45, 0.92)
    axes[0].set_yticks([0.5, 0.6, 0.7, 0.8, 0.9])
    axes[0].tick_params(axis="y", labelsize=7)

    # Scope legend (shade encodes in vs out of domain).
    scope_handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor="#5a6b85", alpha=alpha, label=label)
        for _, label, alpha in SCOPES
    ]
    fig.legend(handles=scope_handles, fontsize=6.8, loc="upper center",
               bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=False,
               handlelength=1.2, columnspacing=1.0)

    # chance reference annotation on the left panel
    axes[0].annotate("chance (0.5)", xy=(group_centers[-1], 0.5),
                     fontsize=5.5, color="#666", va="bottom", ha="right")

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)
    print(f"  Written figure: {out_pdf}")

    sidecar_rows.append(("y_axis_min", 0.45, "axis"))
    sidecar_rows.append(("y_axis_max", 0.92, "axis"))
    sidecar_rows.append(("chance_line", 0.5, "axis"))

    with open(out_sidecar, "w") as fh:
        write_sidecar_header(
            fh,
            generator="figures_src/render_transfer.py",
            source_data=str(data_csv),
        )
        fh.write("label,value,role\n")
        for label, value, role in sidecar_rows:
            fh.write(f"{label},{value:.6g},{role}\n")
    print(f"  Written sidecar: {out_sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
