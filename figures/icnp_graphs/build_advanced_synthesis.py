#!/usr/bin/env python3
"""Build the ICNP advanced synthesis figure from validated master datasets.

Outputs:
- G7_advanced_synthesis.png
- G7_advanced_synthesis_summary.csv
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd
import seaborn as sns

SCRIPT_DIR = Path(__file__).resolve().parent
GA_WORK_ROOT = SCRIPT_DIR.parents[3]
VALIDATED_LOGS = GA_WORK_ROOT / "Validated_Logs"
OUT_PNG = SCRIPT_DIR / "G7_advanced_synthesis.png"
OUT_SUMMARY = SCRIPT_DIR / "G7_advanced_synthesis_summary.csv"

INTERNAL_FAMILY_FILES = {
    "CMAB": "Master_Dataset_CMABs.csv",
    "iCMAB": "Master_Dataset_iCMABs.csv",
    "EXP3": "Master_Dataset_EXP3.csv",
    "Hybrid": "Master_Dataset_Hybrid.csv",
}
FAMILY_ORDER = ["CMAB", "iCMAB", "EXP3", "Hybrid"]
SCENARIO_ORDER = ["NONE", "STOCHASTIC", "MARKOV", "ADAPTIVE", "ONLINEADAPTIVE"]
SCENARIO_LABELS = ["Baseline", "Stochastic", "Markov", "Adaptive", "OnlineAdaptive"]
ALLOCATOR_ORDER = ["Default", "Dynamic", "ThompsonSampling", "Random"]
PAPER_ORDER = ["paper2", "paper8", "paper7", "paper12"]
PAPER_LABELS = ["Paper2\n15N", "Paper8\n20N", "Paper7\n50N", "Paper12\n100N"]


def require_file(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(path)
    return path


def read_validated_csv(relative_path: str) -> pd.DataFrame:
    path = require_file(VALIDATED_LOGS / relative_path)
    frame = pd.read_csv(path)
    frame["source_dataset"] = str(path.relative_to(GA_WORK_ROOT))
    return frame


def normalized_non_oracle(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame[frame["model"].ne("ORACLE")].copy()
    out["efficiency_gap_pp"] = 100.0 - out["eff_pct"]
    return out


def build_panel_a() -> pd.DataFrame:
    parts = []
    for family, csv_name in INTERNAL_FAMILY_FILES.items():
        frame = normalized_non_oracle(read_validated_csv(csv_name))
        slice_frame = frame[
            frame["base_frames"].eq(4000)
            & frame["runs"].eq(5)
            & frame["allocator"].eq("Default")
            & frame["cap_type"].eq("Tb")
        ].copy()
        slice_frame["family"] = family
        parts.append(slice_frame)
    out = pd.concat(parts, ignore_index=True)
    if out.empty:
        raise ValueError("Panel A source slice is empty")
    return out


def build_panel_b() -> pd.DataFrame:
    hybrid = normalized_non_oracle(read_validated_csv("Master_Dataset_Hybrid.csv"))
    hybrid = hybrid[
        hybrid["base_frames"].eq(4000)
        & hybrid["runs"].eq(5)
        & hybrid["model"].isin(["GNEURALUCB", "EXPNEURALUCB", "CPURSUITNEURALUCB", "ICPURSUITNEURALUCB"])
    ].copy()
    grouped = hybrid.groupby(
        ["model", "allocator", "scenario", "cap_type", "scale"], as_index=False
    )["eff_pct"].mean()
    pivot = grouped.pivot_table(
        index=["model", "allocator", "scenario", "cap_type"], columns="scale", values="eff_pct"
    ).dropna(subset=[1.0, 2.0])
    pivot["delta_eff_pp"] = pivot[2.0] - pivot[1.0]
    out = pivot.reset_index()
    if out.empty:
        raise ValueError("Panel B source slice is empty")
    return out


def build_panel_c() -> pd.DataFrame:
    hybrid = normalized_non_oracle(read_validated_csv("Master_Dataset_Hybrid.csv"))
    out = hybrid[
        hybrid["base_frames"].eq(4000)
        & hybrid["runs"].eq(5)
        & hybrid["model"].isin(["CPURSUITNEURALUCB", "ICPURSUITNEURALUCB", "EXPNEURALUCB", "GNEURALUCB"])
    ].copy()
    if out.empty:
        raise ValueError("Panel C source slice is empty")
    return out


def build_panel_d() -> pd.DataFrame:
    standardized = normalized_non_oracle(
        read_validated_csv("standardized/Master_Dataset_papers-4000_2000.csv")
    )
    out = standardized[standardized["runs"].eq(5)].copy()
    if out.empty:
        raise ValueError("Panel D source slice is empty")
    return out


def summarize(frame: pd.DataFrame, panel: str, group_cols: list[str], metric: str) -> pd.DataFrame:
    q1 = frame.groupby(group_cols)[metric].quantile(0.25).rename("q1")
    q3 = frame.groupby(group_cols)[metric].quantile(0.75).rename("q3")
    desc = frame.groupby(group_cols)[metric].agg(["count", "mean", "median", "min", "max"])
    out = desc.join([q1, q3]).reset_index()
    out.insert(0, "panel", panel)
    out.insert(1, "metric", metric)
    return out


def add_panel_label(ax: Axes, label: str, title: str) -> None:
    ax.text(-0.09, 1.08, label, transform=ax.transAxes, fontsize=15, fontweight="bold")


def main() -> None:
    panel_a = build_panel_a()
    panel_b = build_panel_b()
    panel_c = build_panel_c()
    panel_d = build_panel_d()

    summary = pd.concat(
        [
            summarize(panel_a, "A_family_gap", ["family"], "efficiency_gap_pp"),
            summarize(panel_b, "B_capacity_delta", ["scenario", "cap_type"], "delta_eff_pp"),
            summarize(panel_c, "C_allocator_gap", ["allocator"], "gap_pct"),
            summarize(panel_d, "D_standardized_testbed", ["paper"], "eff_pct"),
        ],
        ignore_index=True,
    )
    summary.to_csv(OUT_SUMMARY, index=False)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.12)
    palette_family = {"CMAB": "#8fb3ff", "iCMAB": "#b99aff", "EXP3": "#f4a261", "Hybrid": "#2a9d8f"}
    palette_cap = {"T": "#2b6cb0", "Tb": "#e76f51"}
    palette_alloc = {
        "Default": "#457b9d",
        "Dynamic": "#2a9d8f",
        "ThompsonSampling": "#7b2cbf",
        "Random": "#e63946",
    }
    palette_paper = {"paper2": "#4c78a8", "paper8": "#59a14f", "paper7": "#f28e2b", "paper12": "#e15759"}

    fig, axes = plt.subplots(2, 2, figsize=(14.5, 10.5), constrained_layout=True)

    ax = axes[0, 0]
    sns.boxplot(
        data=panel_a,
        x="family",
        y="efficiency_gap_pp",
        hue="family",
        order=FAMILY_ORDER,
        hue_order=FAMILY_ORDER,
        palette=palette_family,
        linewidth=1.1,
        fliersize=2.2,
        legend=False,
        ax=ax,
    )
    sns.stripplot(
        data=panel_a.sample(min(len(panel_a), 420), random_state=7),
        x="family",
        y="efficiency_gap_pp",
        order=FAMILY_ORDER,
        color="0.18",
        alpha=0.18,
        size=2.2,
        jitter=0.25,
        ax=ax,
    )
    add_panel_label(ax, "A", "All-policy Oracle-gap distribution by family")
    ax.set_xlabel("")
    ax.set_ylabel("Oracle gap (percentage points)")
    ax.axhline(15, color="#555", linestyle="--", linewidth=1, alpha=0.55)
    ax.text(3.45, 15.8, "85% efficiency line", ha="right", va="bottom", fontsize=9, color="#555")
    family_handles = [mpatches.Patch(color=palette_family[family], label=family) for family in FAMILY_ORDER]
    ax.legend(handles=family_handles, ncol=4, loc="upper left", bbox_to_anchor=(0.01, 0.99), frameon=True, fontsize=8.1, columnspacing=0.9, handlelength=1.1)

    ax = axes[0, 1]
    sns.boxplot(
        data=panel_b,
        x="scenario",
        y="delta_eff_pp",
        hue="cap_type",
        order=SCENARIO_ORDER,
        palette=palette_cap,
        linewidth=1.1,
        fliersize=2.4,
        ax=ax,
    )
    ax.axhline(0, color="black", linewidth=1.1)
    add_panel_label(ax, "B", "Capacity paradox as paired $s=2$ vs. $s=1$ delta")
    ax.set_xlabel("")
    ax.set_ylabel("Δ efficiency from replay scaling (pp)")
    ax.set_xticks(range(len(SCENARIO_LABELS)))
    ax.set_xticklabels(SCENARIO_LABELS, rotation=18, ha="right")
    ax.legend(frameon=True, fontsize=8.4, loc="upper left", bbox_to_anchor=(0.01, 0.99), ncol=2, columnspacing=0.9, handlelength=1.2)
    ax.text(0.98, 0.04, "Positive = replay scaling helps", transform=ax.transAxes, ha="right", va="bottom", fontsize=8.5, color="#555", bbox=dict(boxstyle="round,pad=0.25", facecolor="white", alpha=0.78, edgecolor="none"))

    ax = axes[1, 0]
    sns.boxplot(
        data=panel_c,
        x="allocator",
        y="gap_pct",
        hue="allocator",
        order=ALLOCATOR_ORDER,
        hue_order=ALLOCATOR_ORDER,
        palette=palette_alloc,
        linewidth=1.1,
        fliersize=2.2,
        legend=False,
        ax=ax,
    )
    add_panel_label(ax, "C", "Allocator-induced tail risk for hybrid policies")
    ax.set_xlabel("")
    ax.set_ylabel("Oracle gap (percentage points)")
    ax.set_xticks(range(4))
    ax.set_xticklabels(["Default", "DynamicUCB", "Thompson", "Random"], rotation=12, ha="right")
    ax.axhline(15, color="#555", linestyle="--", linewidth=1, alpha=0.55)
    ax.text(3.45, 15.8, "85% efficiency line", ha="right", va="bottom", fontsize=9, color="#555")
    alloc_handles = [
        mpatches.Patch(color=palette_alloc[allocator], label=label)
        for allocator, label in zip(ALLOCATOR_ORDER, ["Default", "DynamicUCB", "Thompson", "Random"])
    ]
    ax.legend(handles=alloc_handles, ncol=4, loc="upper left", bbox_to_anchor=(0.01, 0.99), frameon=True, fontsize=8.0, columnspacing=0.9, handlelength=1.1)

    ax = axes[1, 1]
    sns.boxplot(
        data=panel_d,
        x="paper",
        y="eff_pct",
        hue="paper",
        order=PAPER_ORDER,
        hue_order=PAPER_ORDER,
        palette=palette_paper,
        linewidth=1.1,
        fliersize=2.2,
        legend=False,
        ax=ax,
    )
    add_panel_label(ax, "D", "Standardized external-testbed efficiency spread")
    ax.set_xlabel("")
    ax.set_ylabel("Oracle-normalized efficiency (%)")
    ax.set_xticks(range(len(PAPER_LABELS)))
    ax.set_xticklabels(PAPER_LABELS)
    ax.axhline(85, color="#555", linestyle="--", linewidth=1, alpha=0.55)
    ax.text(3.45, 86.5, "85% deployment target", ha="right", va="bottom", fontsize=9, color="#555")
    paper_handles = [
        mpatches.Patch(color=palette_paper[paper], label=label.replace("\n", " "))
        for paper, label in zip(PAPER_ORDER, PAPER_LABELS)
    ]
    ax.legend(handles=paper_handles, ncol=4, loc="upper left", bbox_to_anchor=(0.01, 0.99), frameon=True, fontsize=8.0, columnspacing=0.9, handlelength=1.1)

    fig.subplots_adjust(top=0.97)
    fig.text(
        0.5,
        -0.01,
        "Source-backed from Validated_Logs master datasets: internal CMAB/iCMAB/EXP3/Hybrid corpora and standardized 4000_2000 external-testbed family.",
        ha="center",
        fontsize=10,
        color="#333",
    )
    fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Wrote {OUT_PNG}")
    print(f"Wrote {OUT_SUMMARY}")
    print("Panel source rows:", {
        "A": len(panel_a),
        "B": len(panel_b),
        "C": len(panel_c),
        "D": len(panel_d),
    })


if __name__ == "__main__":
    main()
