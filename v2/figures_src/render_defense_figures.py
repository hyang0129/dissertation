"""Render simplified, presentation-scale figures for the dissertation defense.

The dissertation figures prioritize paper-level completeness. These versions
prioritize projector legibility and show only the comparisons used in the spoken
defense claims. Every figure is generated from the provenance-headed v2 CSVs and
emits a ``*.numbers.csv`` sidecar for the existing number/provenance pipeline.

Outputs under ``generated/figures``:

* defense_label_blindness_auroc.pdf
* defense_dsc_geometry.pdf
* defense_dsc_fpr95.pdf
* defense_hallu_attribution.pdf
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BLUE = "#2459A6"
LIGHT_BLUE = "#7FA6D9"
GREEN = "#2E8B57"
RED = "#C44E52"
AMBER = "#D28E28"
GREY = "#8D99A6"
DARK = "#20242A"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, comment="#")


def write_sidecar(
    path: Path,
    generator: str,
    source_data: str,
    rows: list[tuple[str, float, str]],
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with path.open("w") as fh:
        fh.write(f"# generator: {generator}\n")
        fh.write(f"# source_data: {source_data}\n")
        fh.write(f"# generated: {now}\n")
        fh.write("label,value,role\n")
        for label, value, role in rows:
            fh.write(f"{label},{value:.8g},{role}\n")


def clean_axes(ax: plt.Axes, grid_axis: str = "y") -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis=grid_axis, linestyle=":", linewidth=0.7, alpha=0.55)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=11)


def render_label_blindness(data_dir: Path, out_dir: Path) -> None:
    source = data_dir / "label_blindness_results.csv"
    df = read_csv(source)
    datasets = ["faces", "cars", "food"]
    dataset_labels = ["Faces", "Cars", "Food"]
    methods = [
        ("supervised_msp", "Supervised MSP", BLUE),
        ("simclr_knn", "SimCLR-KNN", LIGHT_BLUE),
        ("rotloss_knn", "RotLoss-KNN", AMBER),
        ("diffusion_lpips", "Diffusion-LPIPS", GREY),
    ]

    x = np.arange(len(datasets))
    width = 0.19
    fig, ax = plt.subplots(figsize=(9.8, 4.4))
    rows: list[tuple[str, float, str]] = []

    for idx, (method, label, color) in enumerate(methods):
        means, stds = [], []
        for dataset in datasets:
            row = df[(df["dataset"] == dataset) & (df["method"] == method)].iloc[0]
            mean = float(row["auroc_mean"])
            std = float(row["auroc_std"])
            means.append(mean)
            stds.append(std)
            rows.extend(
                [
                    (f"{dataset}_{method}_auroc", mean, "data"),
                    (f"{dataset}_{method}_std", std, "data"),
                ]
            )
        offset = (idx - (len(methods) - 1) / 2) * width
        ax.bar(
            x + offset,
            means,
            width * 0.92,
            yerr=stds,
            capsize=3,
            color=color,
            edgecolor="white",
            linewidth=0.8,
            label=label,
        )

    ax.axhline(50, color=RED, linewidth=1.3, linestyle="--")
    ax.text(2.48, 50.8, "chance", color=RED, fontsize=10, ha="right")
    ax.set_ylabel("Adjacent-OOD AUROC (%)", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(dataset_labels, fontsize=13)
    ax.set_ylim(40, 86)
    ax.legend(frameon=False, ncol=2, fontsize=10.5, loc="upper left")
    clean_axes(ax)
    fig.tight_layout()

    name = "defense_label_blindness_auroc"
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    rows.extend([("chance_auroc", 50.0, "annotation"), ("y_axis_max", 86.0, "axis")])
    write_sidecar(
        out_dir / f"{name}.numbers.csv",
        "figures_src/render_defense_figures.py",
        str(source),
        rows,
    )


def render_dsc_geometry(data_dir: Path, out_dir: Path) -> None:
    source = data_dir / "dsc_geometry.csv"
    df = read_csv(source)
    datasets = ["colon", "tissue", "eurosat", "fashion", "food", "yoga", "rock", "garbage"]
    labels = ["Colon", "Tissue", "EuroSAT", "Fashion", "Food", "Yoga", "Rock", "Garbage"]

    ce, tgt = [], []
    rows: list[tuple[str, float, str]] = []
    for dataset in datasets:
        ce_val = float(df[(df["dataset"] == dataset) & (df["variant"] == "ce")]["r_eff"].iloc[0])
        tgt_val = float(df[(df["dataset"] == dataset) & (df["variant"] == "tgt")]["r_eff"].iloc[0])
        ce.append(ce_val)
        tgt.append(tgt_val)
        rows.extend(
            [
                (f"{dataset}_ce_effective_rank", ce_val, "data"),
                (f"{dataset}_tgt_effective_rank", tgt_val, "data"),
                (f"{dataset}_rank_delta", tgt_val - ce_val, "annotation"),
            ]
        )

    x = np.arange(len(datasets))
    width = 0.36
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    ax.bar(x - width / 2, ce, width, color=GREY, label="Cross-entropy")
    ax.bar(x + width / 2, tgt, width, color=GREEN, label="Teacher-Guided Training")
    ax.set_yscale("log")
    ax.set_ylabel("Effective rank (log scale)", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, rotation=18, ha="right")
    ax.legend(frameon=False, fontsize=11, ncol=2, loc="upper left")
    ax.text(
        2.5,
        265,
        "severe DSC",
        color=RED,
        fontsize=11,
        ha="center",
        bbox={"boxstyle": "round,pad=0.25", "fc": "white", "ec": RED, "alpha": 0.9},
    )
    ax.text(
        6.5,
        265,
        "high-diversity controls",
        color=BLUE,
        fontsize=11,
        ha="center",
        bbox={"boxstyle": "round,pad=0.25", "fc": "white", "ec": BLUE, "alpha": 0.9},
    )
    clean_axes(ax)
    fig.tight_layout()

    name = "defense_dsc_geometry"
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    write_sidecar(
        out_dir / f"{name}.numbers.csv",
        "figures_src/render_defense_figures.py",
        str(source),
        rows,
    )


def render_dsc_fpr95(data_dir: Path, out_dir: Path) -> None:
    source = data_dir / "dsc_main_farood.csv"
    df = read_csv(source)
    scorers = ["mds", "vim", "knn", "nci", "react", "ebo", "msp", "scale"]
    labels = ["MDS", "ViM", "kNN", "NCI", "ReAct", "Energy", "MSP", "SCALE"]
    ce, tgt = [], []
    rows: list[tuple[str, float, str]] = []
    for scorer in scorers:
        row = df[df["scorer"] == scorer].iloc[0]
        ce_val = float(row["resnet_fpr95"])
        tgt_val = float(row["tgresnet_fpr95"])
        ce.append(ce_val)
        tgt.append(tgt_val)
        rows.extend(
            [
                (f"{scorer}_ce_fpr95", ce_val, "data"),
                (f"{scorer}_tgt_fpr95", tgt_val, "data"),
                (f"{scorer}_fpr95_reduction", ce_val - tgt_val, "annotation"),
            ]
        )

    x = np.arange(len(scorers))
    width = 0.36
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    ax.bar(x - width / 2, ce, width, color=GREY, label="Cross-entropy ResNet-50")
    ax.bar(x + width / 2, tgt, width, color=GREEN, label="TG ResNet-50")
    for idx in [0, 1, 2]:
        reduction = ce[idx] - tgt[idx]
        ax.text(x[idx] + width / 2, tgt[idx] + 1.1, f"−{reduction:.1f}", ha="center", fontsize=10, color=DARK)
    ax.set_ylabel("Out-of-domain FPR@95 (%) ↓", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, rotation=18, ha="right")
    ax.set_ylim(0, 61)
    ax.legend(frameon=False, fontsize=11, ncol=2, loc="upper left")
    clean_axes(ax)
    fig.tight_layout()

    name = "defense_dsc_fpr95"
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    rows.append(("y_axis_max", 61.0, "axis"))
    write_sidecar(
        out_dir / f"{name}.numbers.csv",
        "figures_src/render_defense_figures.py",
        str(source),
        rows,
    )


def render_hallu_attribution(data_dir: Path, out_dir: Path) -> None:
    source = data_dir / "hallu_ablation.csv"
    df = read_csv(source)
    cells = [
        ("Llama-3.1-8B-Instruct", "hotpotqa", "Llama · HotpotQA"),
        ("Llama-3.1-8B-Instruct", "popqa", "Llama · PopQA"),
        ("Qwen3-8B", "hotpotqa", "Qwen · HotpotQA"),
        ("Qwen3-8B", "popqa", "Qwen · PopQA"),
    ]
    methods = [
        ("saplma_logprob_recon", "Reconstruction only", GREY),
        ("contrastive", "One-class contrastive", LIGHT_BLUE),
        ("contrastive_logprob_recon", "Both (full method)", BLUE),
    ]

    x = np.arange(len(cells))
    width = 0.24
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    rows: list[tuple[str, float, str]] = []

    for idx, (method, label, color) in enumerate(methods):
        deltas = []
        for model, dataset, _ in cells:
            base = float(
                df[(df["model"] == model) & (df["dataset"] == dataset) & (df["method"] == "saplma")][
                    "auroc_mean"
                ].iloc[0]
            )
            value = float(
                df[(df["model"] == model) & (df["dataset"] == dataset) & (df["method"] == method)][
                    "auroc_mean"
                ].iloc[0]
            )
            delta_pp = 100.0 * (value - base)
            deltas.append(delta_pp)
            safe_model = "llama" if model.startswith("Llama") else "qwen"
            rows.append((f"{safe_model}_{dataset}_{method}_gain_pp", delta_pp, "data"))
        offset = (idx - 1) * width
        ax.bar(x + offset, deltas, width * 0.92, color=color, label=label)

    ax.axhline(0, color=DARK, linewidth=0.8)
    ax.set_ylabel("AUROC gain over SAPLMA (points)", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels([cell[2] for cell in cells], fontsize=11)
    ax.set_ylim(-2, 20)
    ax.legend(frameon=False, fontsize=10.5, ncol=3, loc="upper right")
    clean_axes(ax)
    fig.tight_layout()

    name = "defense_hallu_attribution"
    fig.savefig(out_dir / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)
    rows.extend([("y_axis_min", -2.0, "axis"), ("y_axis_max", 20.0, "axis")])
    write_sidecar(
        out_dir / f"{name}.numbers.csv",
        "figures_src/render_defense_figures.py",
        str(source),
        rows,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", default=".")
    args = parser.parse_args(argv)
    paper_dir = Path(args.paper_dir)
    data_dir = paper_dir / "data"
    out_dir = paper_dir / "generated" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        render_label_blindness(data_dir, out_dir)
        render_dsc_geometry(data_dir, out_dir)
        render_dsc_fpr95(data_dir, out_dir)
        render_hallu_attribution(data_dir, out_dir)
    except (FileNotFoundError, IndexError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for name in [
        "defense_label_blindness_auroc",
        "defense_dsc_geometry",
        "defense_dsc_fpr95",
        "defense_hallu_attribution",
    ]:
        print(f"  Written figure: {out_dir / (name + '.pdf')}")
        print(f"  Written sidecar: {out_dir / (name + '.numbers.csv')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
