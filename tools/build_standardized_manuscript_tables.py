#!/usr/bin/env python3
"""Generate LaTeX tables for standardized external-testbed comparisons.

This script targets the manuscript tables in:
  main.tex

It recomputes the *same aggregation settings* as the manuscript's external testbed tables,
but using the standardized combined dataset:
  ../../../Validated_Logs/Master_Dataset_papers-4000_2000.csv

Outputs are printed to stdout so they can be pasted into LaTeX.

Usage
-----
From the QuantumFaultTolerant repo root:

    ../../.quantum/bin/python tools/build_standardized_manuscript_tables.py --runs 5

Or specify an explicit dataset path:

    ../../.quantum/bin/python tools/build_standardized_manuscript_tables.py --input /path/to/Master_Dataset_papers-4000_2000.csv

Notes
-----
- Efficiency/gap match the manuscript definition: average the per-row (eff_pct, gap_pct)
  percentages across configs (not ratio-of-means).
- Exp. Winner counts are computed at the config level using the dataset's `winner` field.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


CONFIG_COLS_ALL_ALLOCS = ["scenario", "allocator", "scale", "experiment"]
CONFIG_COLS_DEFAULT_ONLY = ["scenario", "scale", "experiment"]


PAPER_META = {
    # These labels mirror the manuscript's descriptive cells.
    "paper2": {
        "parbox": r"\parbox{2.2cm}{\textbf{Paper 2}\\ (\small 15N, 51E, 8P)\\ \small 4K/2K/5R\\ \small 4 allocs, $s\in\{1,1.5,2\}$, T}",
        "color": "findingBlue",
    },
    "paper7": {
        "parbox": r"\parbox{2.2cm}{\textbf{Paper 7}\\ (\small 50N, 141E, 15P)\\ \small 4K/2K/5R\\ \small 4 allocs, $s\in\{1,1.5,2\}$, T}",
        "color": "findingGreen",
    },
    "paper12": {
        "parbox": r"\parbox{2.2cm}{\textbf{Paper 12}\\ (\small 100N, 426E, 4P)\\ \small 4K/2K/5R\\ \small 4 allocs, $s\in\{1,1.5,2\}$, T}",
        "color": "findingOrange",
    },
    "paper8": {
        "parbox": r"\parbox{2.2cm}{\textbf{Paper 8}\\ (\small 20N, 19E, 8P)\\ \small 4K/2K/5R\\ \small 4 allocs, $s\in\{1,1.5,2\}$, T}",
        "color": "findingBlue",
    },
}


MODEL_DISPLAY = {
    "ORACLE": "ORACLE",
    "CPURSUITNEURALUCB": "CPursuitNeuralUCB",
    "GNEURALUCB": "GNeuralUCB",
    "ICPURSUITNEURALUCB": "iCPursuitNeuralUCB",
    "EXPNEURALUCB": "EXPNeuralUCB",
}

MODEL_ORDER = [
    "ORACLE",
    "CPURSUITNEURALUCB",
    "GNEURALUCB",
    "ICPURSUITNEURALUCB",
    "EXPNEURALUCB",
]

# The manuscript uses a slightly different per-testbed ordering.
PAPER_MODEL_ORDERS = {
    "paper2": ["ORACLE", "CPURSUITNEURALUCB", "GNEURALUCB", "ICPURSUITNEURALUCB", "EXPNEURALUCB"],
    "paper7": ["ORACLE", "ICPURSUITNEURALUCB", "EXPNEURALUCB", "CPURSUITNEURALUCB", "GNEURALUCB"],
    "paper12": ["ORACLE", "GNEURALUCB", "EXPNEURALUCB", "ICPURSUITNEURALUCB", "CPURSUITNEURALUCB"],
    "paper8": ["ORACLE", "ICPURSUITNEURALUCB", "EXPNEURALUCB", "GNEURALUCB", "CPURSUITNEURALUCB"],
}


@dataclass(frozen=True)
class ModelRowAllAllocs:
    model: str
    avg_reward: float
    regret: float
    eff_pct: float | None
    gap_pct: float | None
    wins: int | None


@dataclass(frozen=True)
class ModelRowDefaultOnly:
    model: str
    eff_pct: float
    gap_pct: float
    floor_pct: float
    wins: int


def _assert_has_columns(df: pd.DataFrame, cols: list[str]) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def _load_dataset(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = [
        "paper",
        "model",
        "winner",
        "scenario",
        "allocator",
        "scale",
        "experiment",
        "runs",
        "avg_reward",
        "regret",
        "eff_pct",
        "gap_pct",
    ]
    _assert_has_columns(df, required)

    df["paper"] = df["paper"].astype(str)
    df["model"] = df["model"].astype(str)
    df["winner"] = df["winner"].astype(str)
    return df


def _winner_counts_by_model(configs: pd.DataFrame) -> dict[str, int]:
    counts: dict[str, int] = {}
    vc = configs["winner"].astype(str).str.upper().value_counts()
    for model_code, cnt in vc.items():
        counts[str(model_code)] = int(cnt)
    return counts


def _format_bold(s: str, is_bold: bool) -> str:
    return f"\\textbf{{{s}}}" if is_bold else s


def _compute_all_allocs_rows(df_paper: pd.DataFrame, runs: int) -> tuple[int, list[ModelRowAllAllocs], list[str], list[str]]:
    df_paper = df_paper[df_paper["runs"] == runs]

    configs = df_paper.drop_duplicates(subset=CONFIG_COLS_ALL_ALLOCS)[CONFIG_COLS_ALL_ALLOCS + ["winner"]]
    denom = int(configs.shape[0])
    win_counts = _winner_counts_by_model(configs)

    rows: list[ModelRowAllAllocs] = []
    for model_code in MODEL_ORDER:
        sub = df_paper[df_paper["model"].str.upper() == model_code]
        if sub.empty:
            continue
        avg_reward = float(sub["avg_reward"].mean())
        regret = float(sub["regret"].mean())
        if model_code == "ORACLE":
            rows.append(ModelRowAllAllocs(model=model_code, avg_reward=avg_reward, regret=regret, eff_pct=None, gap_pct=None, wins=None))
        else:
            eff = float(sub["eff_pct"].mean())
            gap = float(sub["gap_pct"].mean())
            wins = int(win_counts.get(model_code, 0))
            rows.append(ModelRowAllAllocs(model=model_code, avg_reward=avg_reward, regret=regret, eff_pct=eff, gap_pct=gap, wins=wins))

    non_oracle = [r for r in rows if r.model != "ORACLE"]
    if not non_oracle:
        return denom, rows, [], []

    max_eff = max(r.eff_pct for r in non_oracle if r.eff_pct is not None)
    best_eff_models = [r.model for r in non_oracle if r.eff_pct is not None and abs(r.eff_pct - max_eff) < 1e-12]

    max_wins = max(int(r.wins or 0) for r in non_oracle)
    best_win_models = [r.model for r in non_oracle if int(r.wins or 0) == max_wins]

    return denom, rows, best_eff_models, best_win_models


def _compute_default_only_rows(df_paper: pd.DataFrame, runs: int) -> tuple[int, list[ModelRowDefaultOnly], list[str], list[str]]:
    df_paper = df_paper[(df_paper["runs"] == runs) & (df_paper["allocator"] == "Default")]

    configs = df_paper.drop_duplicates(subset=CONFIG_COLS_DEFAULT_ONLY)[CONFIG_COLS_DEFAULT_ONLY + ["winner"]]
    denom = int(configs.shape[0])
    win_counts = _winner_counts_by_model(configs)

    rows: list[ModelRowDefaultOnly] = []
    for model_code in [m for m in MODEL_ORDER if m != "ORACLE"]:
        sub = df_paper[df_paper["model"].str.upper() == model_code]
        if sub.empty:
            continue
        eff = float(sub["eff_pct"].mean())
        gap = float(100.0 - eff)
        floor = float(sub["eff_pct"].min())
        wins = int(win_counts.get(model_code, 0))
        rows.append(ModelRowDefaultOnly(model=model_code, eff_pct=eff, gap_pct=gap, floor_pct=floor, wins=wins))

    if not rows:
        return denom, rows, [], []

    max_eff = max(r.eff_pct for r in rows)
    best_eff_models = [r.model for r in rows if abs(r.eff_pct - max_eff) < 1e-12]

    max_wins = max(r.wins for r in rows)
    best_win_models = [r.model for r in rows if r.wins == max_wins]

    return denom, rows, best_eff_models, best_win_models


def render_table_cross_testbed_standardized(df: pd.DataFrame, runs: int) -> str:
    papers_order = ["paper2", "paper7", "paper12", "paper8"]

    lines: list[str] = []
    lines.append(r"% AUTO-GENERATED by tools/build_standardized_manuscript_tables.py")
    lines.append(r"% Source: Validated_Logs/Master_Dataset_papers-4000_2000.csv")
    lines.append(r"\begin{table*}[ht!]")
    lines.append(r"\centering")
    lines.append(
        r"\caption{Cross-testbed performance comparison under standardized 4K/2K/5R run configurations. Numeric columns are means across all five scenarios (\texttt{none}, \texttt{stochastic}, \texttt{markov}, \texttt{adaptive}, \texttt{onlineadaptive}), 4 allocators, and scales $s \in \{1.0,1.5,2.0\}$ (\texttt{cap\_type}=T), computed from the standardized corpus (config key \texttt{4000\_2000}). Exp.\ Winner counts are experiment-level win counts out of the available standardized configurations for each testbed.}")
    lines.append(r"\label{tab:testbed_comparison_standard_4000_2000}")
    lines.append(r"\small")
    lines.append(r"\begin{tabular}{l l c c c c l}")
    lines.append(r"\toprule")
    lines.append(
        r"\textbf{Testbed} & \textbf{Algorithm} & \textbf{Avg Reward} & \textbf{Regret} & \textbf{Efficiency (\%)} & \textbf{Gap (\%)} & \textbf{Exp. Winner} \\")
    lines.append(r"\midrule")

    for paper in papers_order:
        meta = PAPER_META[paper]
        denom, rows, best_eff_models, best_win_models = _compute_all_allocs_rows(df[df["paper"] == paper], runs=runs)

        desired_order = PAPER_MODEL_ORDERS.get(paper, MODEL_ORDER)
        row_by_model = {r.model: r for r in rows}
        ordered_rows = [row_by_model[m] for m in desired_order if m in row_by_model]

        lines.append(rf"\multirow{{7}}{{*}}{{{meta['parbox']}}}")

        for idx, r in enumerate(ordered_rows):
            algo = rf"\texttt{{{MODEL_DISPLAY.get(r.model, r.model)}}}"
            avg_reward = f"{r.avg_reward:.4f}"
            regret = f"{r.regret:.1f}"

            if r.model == "ORACLE":
                eff = "---"
                gap = "---"
                wins = "---"
            else:
                assert r.eff_pct is not None
                assert r.gap_pct is not None
                assert r.wins is not None
                eff = _format_bold(f"{r.eff_pct:.2f}", r.model in best_eff_models)
                gap = f"{r.gap_pct:.2f}"

                win_str = f"{r.wins}/{denom}"
                if r.model in best_win_models:
                    win_str = _format_bold(f"{r.wins}/{denom}$^\\star$", True)
                wins = win_str

            prefix = "&" if idx == 0 else "&"
            lines.append(rf"{prefix} {algo} & {avg_reward} & {regret} & {eff} & {gap} & {wins} \\")

        non_oracle = [rr for rr in ordered_rows if rr.model != "ORACLE" and rr.eff_pct is not None]
        if non_oracle:
            eff_min = min(rr.eff_pct for rr in non_oracle)  # type: ignore[arg-type]
            eff_max = max(rr.eff_pct for rr in non_oracle)  # type: ignore[arg-type]
            win_max = max(int(rr.wins or 0) for rr in non_oracle)
            win_models = [rr.model for rr in non_oracle if int(rr.wins or 0) == win_max]
            win_models_disp = " / ".join(MODEL_DISPLAY.get(m, m) for m in win_models)
            lines.append(r"\cline{2-7}")
            lines.append(
                rf"& \cellcolor{{{meta['color']}}}\textit{{Standardized 4K/2K slice}} & \multicolumn{{5}}{{l}}{{\cellcolor{{{meta['color']}}}\small {eff_min:.1f}--{eff_max:.1f}\% eff. $^\star$Exp.\ Winner: {win_models_disp} ({win_max}/{denom})}} \\")

        lines.append(r"\midrule")

    if lines and lines[-1] == r"\midrule":
        lines[-1] = r"\bottomrule"

    lines.append(r"\end{tabular}")
    lines.append(r"\end{table*}")

    return "\n".join(lines)


def render_table_external_default_standardized(df: pd.DataFrame, runs: int) -> str:
    papers_order = ["paper2", "paper7", "paper12", "paper8"]

    lines: list[str] = []
    lines.append(r"% AUTO-GENERATED by tools/build_standardized_manuscript_tables.py")
    lines.append(r"% Source: Validated_Logs/Master_Dataset_papers-4000_2000.csv")
    lines.append(r"\begin{table*}[ht!]")
    lines.append(r"\centering")
    lines.append(
        r"\caption{External testbed comparison under standardized 4K/2K/5R run configurations using the \texttt{Default} allocator (\texttt{cap\_type}=T). Columns match the external-testbed slice used in the model-family comparison: Avg Eff/Gaps are means across all five scenarios and scales $s \in \{1.0,1.5,2.0\}$; Floor is worst-case efficiency; Exp.\ Winner counts are out of the available standardized configurations.}")
    lines.append(r"\label{tab:external_default_standard_4000_2000}")
    lines.append(r"\small")
    lines.append(r"\begin{tabular}{l l c c c l}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Testbed} & \textbf{Algorithm} & \textbf{Avg Eff (\%)} & \textbf{Gap (\%)} & \textbf{Floor (\%)} & \textbf{Exp. Winner} \\")
    lines.append(r"\midrule")

    for paper in papers_order:
        meta = PAPER_META[paper]
        denom, rows, best_eff_models, best_win_models = _compute_default_only_rows(df[df["paper"] == paper], runs=runs)

        desired_order = ["ICPURSUITNEURALUCB", "CPURSUITNEURALUCB", "GNEURALUCB", "EXPNEURALUCB"]
        row_by_model = {r.model: r for r in rows}
        ordered_rows = [row_by_model[m] for m in desired_order if m in row_by_model]

        lines.append(rf"\multirow{{5}}{{*}}{{\parbox{{2cm}}{{\textbf{{{paper.replace('paper','Paper ')}}}\\ \small(Standard)\\ \small 4K/2K}}}}")

        for idx, r in enumerate(ordered_rows):
            algo = rf"\texttt{{{MODEL_DISPLAY.get(r.model, r.model)}}}"
            eff = _format_bold(f"{r.eff_pct:.2f}", r.model in best_eff_models)
            gap = f"{r.gap_pct:.2f}"
            floor = f"{r.floor_pct:.1f}"

            win_str = f"{r.wins}/{denom}"
            if r.model in best_win_models:
                win_str = _format_bold(f"{r.wins}/{denom}$^\\star$", True)

            lines.append(rf"& {algo} & {eff} & {gap} & {floor} & {win_str} \\")

        if ordered_rows:
            eff_vals = [r.eff_pct for r in ordered_rows]
            eff_min = min(eff_vals)
            eff_max = max(eff_vals)
            win_max = max(r.wins for r in ordered_rows)
            win_models = [r.model for r in ordered_rows if r.wins == win_max]
            win_models_disp = " / ".join(MODEL_DISPLAY.get(m, m) for m in win_models)

            lines.append(r"\cline{2-6}")
            lines.append(
                rf"& \cellcolor{{{meta['color']}}}\textit{{Standardized Default slice}} & \multicolumn{{4}}{{l}}{{\cellcolor{{{meta['color']}}}\small {eff_min:.1f}--{eff_max:.1f}\% eff. $^\star$Exp.\ Winner: {win_models_disp} ({win_max}/{denom})}} \\")

        lines.append(r"\midrule")

    if lines and lines[-1] == r"\midrule":
        lines[-1] = r"\bottomrule"

    lines.append(r"\end{tabular}")
    lines.append(r"\end{table*}")

    return "\n".join(lines)


def _default_input_path() -> Path:
    # tools/ -> QuantumFaultTolerant/ -> GA Papers/ -> GA-Work/
    ga_work_root = Path(__file__).resolve().parents[3]
    return ga_work_root / "Validated_Logs" / "Master_Dataset_papers-4000_2000.csv"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate LaTeX snippets for standardized external-testbed manuscript tables.")
    parser.add_argument("--input", type=Path, default=_default_input_path(), help="Path to Master_Dataset_papers-4000_2000.csv")
    parser.add_argument("--runs", type=int, default=5, help="Run-count slice to use (default: 5)")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input dataset not found: {args.input}. Pass --input explicitly.")

    df = _load_dataset(args.input)
    df = df[df["paper"].isin(PAPER_META.keys())].copy()

    print(render_table_cross_testbed_standardized(df, runs=args.runs))
    print("\n\n")
    print(render_table_external_default_standardized(df, runs=args.runs))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
