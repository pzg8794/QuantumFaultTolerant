#!/usr/bin/env python3
"""Build G8 and G9 advanced result figures for the ICNP paper.

G8 — 4-panel gap synthesis (family gap, capacity paradox, allocator, testbed)
G9 — 9-panel networking performance & gap analysis
     (fidelity decay, qubit budget, Oracle-gap bars, RQ1 tiers,
      threat escalation heatmap, capacity paradox lines,
      scenario penalties, allocator risk, cross-testbed violin)

All data sourced from validated main.tex tables:
  tab:rq1masterstochastic, tab:rq2_adversarial, fig:capacity_all,
  tab:rq3c_allocators, tab:external_default_standard_4000_2000,
  topology §IV-A (4-node diamond, 35-qubit budget)

Run from repo root:
  python figures/icnp-exported-assets/build_G8_G9.py
  python figures/icnp-exported-assets/build_G8_G9.py --only panel-h
"""
from __future__ import annotations
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_G8 = SCRIPT_DIR / "G8_advanced_4panel.png"
OUT_G9 = SCRIPT_DIR / "G9_network_gap_analysis.png"
OUT_PANEL_D = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-033_g9_network_gap_analysis_panel_d_rq1_algorithm_tier_separation_stochastic.png"
)
OUT_PANEL_C = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-032_g9_network_gap_analysis_panel_c_oracle_gap_context_vs_exp3_by_scenario_c.png"
)
OUT_PANEL_F = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-035_g9_network_gap_analysis_panel_f_capacity_paradox_all_6_replay_configs_sc.png"
)
OUT_PANEL_G = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-036_g9_network_gap_analysis_panel_g_scenario_penalty_vs_baseline_by_algorith.png"
)
OUT_PANEL_H = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-037_g9_network_gap_analysis_panel_h_allocator_risk_floor_mean_peak_icpursuit.png"
)
OUT_PANEL_I = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-038_g9_network_gap_analysis_panel_i_cross_testbed_efficiency_oracle_gap_std.png"
)
OUT_G8_PUBLIC = (
    SCRIPT_DIR.parent
    / "icnp"
    / "ICNP-CODE-024_g8_advanced_4panel_grouped_full_figure.png"
)

RNG = np.random.default_rng(42)

# ── palette (colour-blind safe) ────────────────────────────────────────────
C = dict(
    CMAB='#4c78a8', iCMAB='#72b7b2', EXP3='#f28e2b', HYBRID='#2ca02c',
    T='#2b6cb0', Tb='#e76f51', T15='#4da6ff', T2='#7b2cbf',
    FIXED='#457b9d', DUB='#2a9d8f', THOM='#7b2cbf', RAND='#e63946',
    P2='#4c78a8', P8='#59a14f', P7='#f28e2b', P12='#e15759',
    THRESH='#555555',
)
SCENARIOS = ['Baseline', 'Stochastic', 'Markov', 'Adaptive', 'OnlineAdaptive']

# ════════════════════════════════════════════════════════════════════════════
# DATA — all numbers traced to main.tex
# ════════════════════════════════════════════════════════════════════════════
FAMILY_EFF = {
    'CMAB':  [[99.8,94.7,93.0,92.8,81.5],[95.2,89.1,86.8,86.3,80.4],
              [97.1,91.3,88.2,87.5,78.9],[88.0,82.4,77.4,76.3,81.0]],
    'iCMAB': [[99.9,94.8,93.0,92.8,99.8],[93.2,88.1,86.5,87.7,86.5],
              [91.4,87.2,85.9,86.1,84.3],[86.8,85.0,81.0,83.0,86.0]],
    'EXP3':  [[83.6,76.3,73.8,74.7,76.4],[95.4,83.0,88.5,81.6,85.3],
              [89.9,81.4,80.6,77.2,82.5],[85.9,81.1,81.7,79.5,81.1]],
    'Hybrid':[[99.9,94.8,93.0,92.8,99.8],[99.8,94.7,93.0,92.8,81.5],
              [89.9,85.5,82.6,87.0,84.2],[95.4,83.0,88.5,81.6,85.3]],
}
GAP_DATA = {f:[100-v for row in rows for v in row] for f,rows in FAMILY_EFF.items()}

T_BOX  = [[3.1,0.4,1.3,2.1],[-0.6,-0.2,-0.8,0.5],[1.3,3.5,1.4,0.9],[7.4,7.5,7.8,2.3],[3.1,1.4,2.6,-0.4]]
TB_BOX = [[0.5,-0.4,0.7,-0.6],[1.1,-0.9,0.4,0.8],[-5.2,-3.5,-4.8,-2.1],[2.3,1.4,2.6,-0.4],[-2.4,-1.8,-3.1,-0.9]]

ALLOC_SCEN_EFF = {
    'Fixed':      [99.9,94.8,93.0,92.8,99.8],
    'DynamicUCB': [99.7,92.2,87.5,91.0,92.6],
    'Thompson':   [99.9,91.4,73.3,91.5,83.2],
    'Random':     [99.2,86.3,68.3,79.8,84.2],
}
ALLOC_AVG   = [92.7, 92.6, 87.8, 86.4]
ALLOC_FLOOR = [88.9, 87.9, 73.3, 68.3]
ALLOC_SPAN  = [7.8,   9.3, 26.4, 26.7]

TESTBED_EFF = {
    'Chaudhary et al.': [74.5,73.2,73.2,71.3],
    'Liu et al.': [78.0,70.8,70.8,69.6],
    'Clayton et al.': [44.1,43.8,43.7,42.5],
    'Jallow-Khan': [67.9,61.4,61.7,61.9],
}

# RQ1 stochastic tier data (tab:rq1masterstochastic)
RQ1_MODELS = ['CPursuit','iCEpsGreedy','CEpsGreedy','GNeuralUCB',
              'EXPNeuralUCB','EXPUCB','CEXP4','iCPursuit',
              'CThompson','iCThompson','CEpochGreedy','iCEpochGreedy','iCEXP4']
RQ1_EFF    = [89.9,88.3,87.8,86.3,81.5,77.6,70.1,67.4,67.5,67.5,37.6,37.5,37.4]
RQ1_TIERS  = ['Tier1']*4 + ['Tier2']*6 + ['Tier3']*3

SCEN_ORDER = ['Stochastic','Markov','Adaptive','OnlineAdaptive','Baseline']
CTX_T  = [89.9, 85.9, 86.8, 88.8, 93.2]
CTX_TB = [88.1, 86.1, 87.7, 86.5, 93.3]
EXP_T  = [81.4, 80.6, 77.2, 82.5, 90.5]
EXP_TB = [81.1, 81.7, 79.5, 81.1, 85.9]

PEN_ALGOS = ['EXPUCB','EXPNeuralUCB','iCEpsGreedy','CPursuit']
PEN_STOCH = [7.3,12.4,4.9,3.2]; PEN_MARK=[9.8,6.9,7.0,7.6]
PEN_ADAP  = [8.9,13.8,6.1,6.3]; PEN_OA  =[7.2,10.1,5.8,4.5]

CAP_DATA = {
    'T':   [81.5,86.5,88.9,83.2,90.3], '1.5T':[82.3,80.5,83.7,90.3,88.0],
    '2T':  [84.8,85.9,90.2,90.6,93.4], 'Tb':  [80.6,83.2,84.8,86.6,87.9],
    '1.5Tb':[81.0,80.7,87.7,85.2,87.0],'2Tb': [81.7,78.0,87.1,84.2,91.0],
}

PATH_NAMES  = ['P1 (S→B→D)','P2 (S→C→D)','P3 (S→B→C→D)','P4 (S→C→B→D)']
PATH_HOPS   = [2, 2, 3, 3]
PATH_QUBITS = [8, 10, 8, 9]

HEAT_ALGOS = ['iCPursuitNeural','CPursuitNeural','CPursuit','iCEpsGreedy',
              'EXPNeuralUCB','EXPUCB','GNeuralUCB','CEpsGreedy']
HEAT_MAT = np.array([
    [99.9,94.8,93.0,92.8,99.8],[99.8,94.7,93.0,92.8,81.5],
    [96.2,90.0,88.2,85.6,81.5],[93.2,88.3,86.5,87.7,86.5],
    [95.4,81.5,88.5,81.6,85.3],[83.6,77.6,73.8,74.7,76.4],
    [89.9,86.3,80.6,77.2,82.5],[93.0,87.8,86.8,86.3,80.4],
])

def path_p(hops, total_q, pe=1.5e-4):
    q_per_link = total_q / hops
    return (1-(1-pe)**q_per_link)**hops


def panel_label(ax, letter, title, fs=11):
    ax.text(-0.10,1.07,letter,transform=ax.transAxes,fontsize=14,fontweight='bold',va='top')


def panel_subtitle(ax, title):
    ax.set_title(title, fontsize=10.4, fontweight='bold', pad=8)


def label_box_medians(ax, positions, datasets, colors, *, dy=0.6):
    for pos, values, color in zip(positions, datasets, colors):
        median = float(np.median(values))
        if median >= 0:
            y = median + dy
            va = 'bottom'
        else:
            y = median - dy
            va = 'top'
        ax.text(
            pos,
            y,
            f'{median:+.1f}pp',
            ha='center',
            va=va,
            fontsize=7.8,
            color=color,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.18', facecolor='white', alpha=0.82, edgecolor='none'),
            zorder=8,
        )


def label_bar_values_inside(ax, bars, *, suffix='%', text_color='white', y_padding=1.0):
    for bar in bars:
        height = bar.get_height()
        if height <= 0:
            continue
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            max(height - y_padding, height * 0.55),
            f'{height:.1f}{suffix}',
            ha='center',
            va='top',
            fontsize=6.8,
            color=text_color,
            fontweight='bold',
            zorder=7,
        )


def annotate_point_value(ax, x, y, text, color, xytext, *, ha='left'):
    ax.annotate(
        text,
        xy=(x, y),
        xytext=xytext,
        textcoords='offset points',
        ha=ha,
        va='center',
        fontsize=8.2,
        color=color,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.18', facecolor='white', alpha=0.84, edgecolor='none'),
        arrowprops=dict(arrowstyle='-', color=color, lw=0.8, alpha=0.75),
        zorder=9,
        clip_on=False,
    )


def draw_allocator_risk_panel(ax, *, include_panel_label=True):
    alloc_names_h = ['Fixed', 'DynamicUCB', 'Thompson', 'Random']
    alloc_cols_h = [C['FIXED'], C['DUB'], C['THOM'], C['RAND']]
    alloc_peak_h = [min(100.0, f + s) for f, s in zip(ALLOC_FLOOR, ALLOC_SPAN)]
    label_offsets = {
        'Fixed': dict(peak=(19, 14), mean=(20, 0), floor=(19, -28), ha='left'),
        'DynamicUCB': dict(peak=(19, 18), mean=(19, 0), floor=(19, -22), ha='left'),
        'Thompson': dict(peak=(19, 16), mean=(19, 0), floor=(19, -28), ha='left'),
        'Random': dict(peak=(24, 16), mean=(24, 0), floor=(24, -12), ha='left'),
    }
    for i, (an, ac) in enumerate(zip(alloc_names_h, alloc_cols_h)):
        fl = ALLOC_FLOOR[i]
        avg = ALLOC_AVG[i]
        pk = alloc_peak_h[i]
        ax.plot([i, i], [fl, pk], color=ac, lw=8, alpha=0.28, solid_capstyle='round')
        ax.plot([i, i], [fl, pk], color=ac, lw=1.5, alpha=0.9)
        ax.scatter(i, avg, s=90, color=ac, zorder=6, edgecolors='white', lw=1.5)
        ax.scatter(i, fl, s=50, marker='v', color=ac, zorder=6, edgecolors='white', lw=1)
        ax.scatter(i, pk, s=50, marker='^', color=ac, zorder=6, edgecolors='white', lw=1)
        offsets = label_offsets[an]
        annotate_point_value(ax, i, pk, f'peak {pk:.1f}%\nspan {ALLOC_SPAN[i]:.1f}pp', ac, offsets['peak'], ha=offsets['ha'])
        annotate_point_value(ax, i, avg, f'mean {avg:.1f}%', ac, offsets['mean'], ha=offsets['ha'])
        annotate_point_value(ax, i, fl, f'floor {fl:.1f}%', ac, offsets['floor'], ha=offsets['ha'])
    ax.axhline(85, color=C['THRESH'], ls='--', lw=1.2, alpha=0.7)
    ax.text(-0.1, 85.45, '85% target', ha='left', va='bottom', fontsize=8.0, color=C['THRESH'])
    ax.set_xticks(range(4))
    ax.set_xticklabels(alloc_names_h)
    ax.set_xlim(-0.15, 3.85)
    ax.set_ylim(65, 105)
    ax.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax.set_facecolor('#f9f9f9')
    ax.scatter([], [], s=80, color='#555', label='Mean')
    ax.scatter([], [], s=45, color='#555', marker='v', label='Floor')
    ax.scatter([], [], s=45, color='#555', marker='^', label='Peak')
    ax.legend(fontsize=7.5, loc='lower left', ncol=3, frameon=True, framealpha=0.88)
    if include_panel_label:
        panel_label(ax, 'H', 'Allocator Risk: Floor / Mean / Peak (iCPursuitNeural)')


def draw_rq1_tier_panel(ax, *, include_panel_label=True):
    y=np.arange(len(RQ1_MODELS))[::-1]
    tier_cols={'Tier1':'#2ca02c','Tier2':'#f28e2b','Tier3':'#e63946'}
    tier_labels={'Tier1':'Viable (≥85%)','Tier2':'Degraded','Tier3':'Collapsed'}
    for yi,model,eff,tier in zip(y,RQ1_MODELS,RQ1_EFF,RQ1_TIERS):
        col=tier_cols[tier]
        ax.hlines(yi,20,eff,color=col,lw=1.9,alpha=0.55)
        ax.scatter(eff,yi,s=55,color=col,edgecolors='white',lw=0.8,zorder=4)
        ax.text(eff+0.6,yi,f'{eff:.1f}',va='center',fontsize=7.6,color=col)
    ax.axvline(85,color='#777',ls='--',lw=1.2)
    ax.text(85.8, len(RQ1_MODELS)-1.15, '85% target', ha='left', va='top',
            fontsize=8.0, color='#555',
            bbox=dict(boxstyle='round,pad=0.18', facecolor='white', alpha=0.82, edgecolor='none'))
    ax.set_yticks(y); ax.set_yticklabels(RQ1_MODELS,fontsize=8.8)
    ax.set_xlim(20,103); ax.set_ylim(-0.6,len(RQ1_MODELS)-0.4)
    ax.set_xlabel('Oracle-Norm. Efficiency % (Stochastic)')
    ax.set_facecolor('#f9f9f9')
    for tier,col in tier_cols.items():
        ax.scatter([],[],color=col,s=50,label=tier_labels[tier])
    ax.legend(fontsize=7.2,loc='lower right',ncol=3,frameon=True,framealpha=0.88,columnspacing=0.8,handlelength=1.1)
    if include_panel_label:
        panel_label(ax,'D','RQ1: Algorithm Tier Separation (Stochastic Decoherence)')


def draw_capacity_all_configs_panel(ax, *, include_panel_label=True):
    cap_styles={'T':('-',C['T'],'o',2.2),'1.5T':('--',C['T15'],'s',1.8),
                '2T':('-',C['T2'],'^',2.2),'Tb':('-',C['Tb'],'o',2.2),
                '1.5Tb':('--','#d4730a','s',1.8),'2Tb':('-','#8b2500','^',2.2)}
    online_label_offsets = {
        'T': (-18, -18), '1.5T': (-10, 18), '2T': (0, 18),
        'Tb': (22, 0), '1.5Tb': (-24, -18), '2Tb': (24, 16),
    }
    x6=np.arange(5)
    cap_scens=['Stochastic','Markov','Adaptive','Online\nAdaptive','Baseline']
    for cname,(ls,col,mk,lw) in cap_styles.items():
        ax.plot(x6,CAP_DATA[cname],ls=ls,color=col,marker=mk,lw=lw,ms=6,label=cname,alpha=0.88)
        dx, dy = online_label_offsets[cname]
        ax.annotate(f'{CAP_DATA[cname][3]:.1f}', xy=(3, CAP_DATA[cname][3]), xytext=(dx, dy),
                    textcoords='offset points', ha='center', va='center', fontsize=7.4,
                    color=col, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.12', facecolor='white', alpha=0.84, edgecolor='none'),
                    zorder=8, clip_on=False)
    ax.axhline(85,color=C['THRESH'],ls=':',lw=1.1,alpha=0.7)
    ax.text(4.95,85.2,'85% target',ha='right',va='bottom',fontsize=7.3,color=C['THRESH'])
    ax.set_xticks(x6); ax.set_xticklabels(cap_scens,fontsize=9,rotation=10,ha='right')
    ax.set_ylim(76.8,94.5); ax.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax.legend(fontsize=6.5,ncol=6,frameon=True,framealpha=0.90,loc='upper center',
              bbox_to_anchor=(0.5,0.995),columnspacing=0.7,handlelength=1.0)
    ax.set_facecolor('#f9f9f9')
    ax.annotate('OnlineAdaptive T span: 83.2--90.6%',
                xy=(3,CAP_DATA['2T'][3]),xytext=(2.35,92.9),fontsize=7.6,color=C['T2'],
                arrowprops=dict(arrowstyle='->',color=C['T2'],lw=0.9),
                bbox=dict(boxstyle='round,pad=0.18', facecolor='white', alpha=0.86, edgecolor='none'))
    ax.annotate(r'OnlineAdaptive $T_b$ span: 84.2--86.6%',
                xy=(3,CAP_DATA['Tb'][3]),xytext=(2.0,78.0),fontsize=7.6,color=C['Tb'],
                arrowprops=dict(arrowstyle='->',color=C['Tb'],lw=0.9),
                bbox=dict(boxstyle='round,pad=0.18', facecolor='white', alpha=0.86, edgecolor='none'))
    if include_panel_label:
        panel_label(ax,'F','Capacity Paradox: All 6 Replay Configs × Scenario')


def draw_scenario_penalty_panel(ax, *, include_panel_label=True):
    x=np.arange(4); w=0.18
    pen_data=[('Stochastic',PEN_STOCH,'#4da6ff'),('Markov',PEN_MARK,'#2b6cb0'),
              ('Adaptive',PEN_ADAP,'#e63946'),('OnlineAdaptive',PEN_OA,'#f28e2b')]
    for (lbl,vals,col),off in zip(pen_data,[-1.5,-0.5,0.5,1.5]):
        container=ax.bar(x+off*w,vals,width=w*0.88,color=col,alpha=0.88,label=lbl,edgecolor='white',lw=0.6)
        ax.bar_label(container,fmt='%.1f',padding=1,fontsize=7.0)
    ax.set_xticks(x); ax.set_xticklabels(PEN_ALGOS,fontsize=9.0)
    ax.set_ylabel('Penalty vs Baseline (pp)')
    ax.set_ylim(0, 14.7)
    ax.legend(fontsize=8,ncol=4,frameon=True,framealpha=0.90,loc='upper center',
              bbox_to_anchor=(0.5,0.995),columnspacing=0.9,handlelength=1.1)
    ax.set_facecolor('#f9f9f9')
    if include_panel_label:
        panel_label(ax,'G','Scenario Penalty vs Baseline by Algorithm & Threat')


def draw_oracle_gap_panel(ax, *, include_panel_label=True):
    x3=np.arange(len(SCEN_ORDER)); w3=0.18
    gap_pairs=[('Context(T)',[100-v for v in CTX_T],C['T']),
               ('Context(Tb)',[100-v for v in CTX_TB],'#72b7b2'),
               ('EXP3(T)',[100-v for v in EXP_T],C['EXP3']),
               ('EXP3(Tb)',[100-v for v in EXP_TB],'#d4730a')]
    for (lbl,gaps,col),off in zip(gap_pairs,[-1.5,-0.5,0.5,1.5]):
        bars = ax.bar(x3+off*w3,gaps,width=w3*0.88,color=col,alpha=0.85,label=lbl,edgecolor='white',lw=0.6)
        for bar, gap in zip(bars, gaps):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                gap + 0.35,
                f'{gap:.1f}',
                ha='center',
                va='bottom',
                fontsize=6.6,
                color='#111111',
                fontweight='bold',
                zorder=7,
                bbox=dict(boxstyle='round,pad=0.08', facecolor='white', alpha=0.74, edgecolor='none'),
            )
    ax.axhline(15,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    ax.set_xticks(x3); ax.set_xticklabels(SCEN_ORDER,fontsize=9,rotation=10,ha='right')
    ax.set_ylabel('Oracle Gap (pp)')
    ax.legend(fontsize=6.8,ncol=2,frameon=True,framealpha=0.88,loc='upper right',bbox_to_anchor=(0.98,0.92),columnspacing=0.9,handlelength=1.1)
    ax.set_facecolor('#f9f9f9')
    ax.text(0.02,0.82,'Context(T) cuts the Stochastic gap by 8.5 vs EXP3(T)',transform=ax.transAxes,ha='left',va='top',fontsize=8,color='#555',bbox=dict(boxstyle='round,pad=0.25',facecolor='white',alpha=0.75,edgecolor='none'))
    ax.text(0.98,0.92,'Lower is better',transform=ax.transAxes,ha='right',va='top',fontsize=8,color='#555',bbox=dict(boxstyle='round,pad=0.25',facecolor='white',alpha=0.75,edgecolor='none'))
    if include_panel_label:
        panel_label(ax,'C','Oracle Gap: Context vs EXP3 by Scenario & Capacity')


def draw_cross_testbed_panel(ax, *, include_panel_label=True):
    tl=list(TESTBED_EFF.keys()); tv=list(TESTBED_EFF.values())
    tc9=[C['P2'],C['P7'],C['P12'],C['P8']]
    amk9=['o','s','^','D']
    aln9=['iCPursuitNeural','CPursuitNeural','GNeuralUCB','EXPNeuralUCB']
    vd=[np.repeat(v,20)+RNG.normal(0,0.18,len(v)*20) for v in tv]
    vp=ax.violinplot(vd,positions=range(4),widths=0.62,showmedians=False,showextrema=False)
    for body,col in zip(vp['bodies'],tc9):
        body.set_facecolor(col); body.set_alpha(0.35)
    bp=ax.boxplot(tv,positions=range(4),widths=0.20,patch_artist=True,
        medianprops=dict(color='white',lw=2.2),
        whiskerprops=dict(lw=1.3,color='#666'),capprops=dict(lw=1.3,color='#666'),
        flierprops=dict(marker='o',ms=3,alpha=0.4))
    for p,col in zip(bp['boxes'],tc9):
        p.set_facecolor(col); p.set_alpha(0.88)
    for ji,(vals,col) in enumerate(zip(tv,tc9)):
        for ki,v in enumerate(vals):
            ax.scatter(ji+RNG.uniform(-0.07,0.07),v,s=52,color=col,marker=amk9[ki],
                       zorder=6,alpha=0.95,edgecolors='white',lw=0.9)
            if v == max(vals):
                ax.text(ji, v + 1.05, f'best {v:.1f}%', ha='center',
                        fontsize=8.0, color=col, fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.16', facecolor='white', alpha=0.82, edgecolor='none'))
        ax.text(ji,max(vals)+2.65,f'gap {100-max(vals):.1f}pp',ha='center',
                fontsize=7.8,color=col,fontweight='bold')
    ax.axhline(85,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    ax.text(3.45,85.45,'85% internal target',ha='right',va='bottom',fontsize=7.4,color=C['THRESH'])
    ax.set_xticks(range(4)); ax.set_xticklabels(tl,fontsize=7.8)
    ax.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax.set_ylim(39,88)
    ax.set_facecolor('#f9f9f9')
    for mk,mn in zip(amk9,aln9):
        ax.scatter([],[],marker=mk,color='#555',s=42,label=mn[:12])
    ax.legend(loc='lower left',ncol=2,frameon=True,framealpha=0.88,fontsize=7.0)
    if include_panel_label:
        panel_label(ax,'I','Cross-Testbed Efficiency & Oracle Gap (Std. 4K/2K/5R)')


def draw_context_capacity_panel(ax):
    x=np.arange(len(SCEN_ORDER))
    lines=[
        ('Context T', CTX_T, C['T'], '-', 'o'),
        (r'Context $T_b$', CTX_TB, '#72b7b2', '-', 's'),
        ('EXP3 T', EXP_T, C['EXP3'], '--', '^'),
        (r'EXP3 $T_b$', EXP_TB, '#d4730a', '--', 'D'),
    ]
    for label, values, color, linestyle, marker in lines:
        ax.plot(x, values, color=color, linestyle=linestyle, marker=marker,
                lw=2.1, ms=5.5, label=label, alpha=0.92)
        ax.text(x[-1] + 0.04, values[-1], f'{values[-1]:.1f}', ha='left',
                va='center', fontsize=7.2, color=color, fontweight='bold')
    ax.axhline(85,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    ax.text(0.04,85.45,'85% target',ha='left',va='bottom',fontsize=8.0,color=C['THRESH'])
    ax.set_xticks(x); ax.set_xticklabels(SCEN_ORDER,fontsize=8.7,rotation=10,ha='right')
    ax.set_xlim(-0.15, len(SCEN_ORDER)-0.45)
    ax.set_ylim(74,95)
    ax.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax.set_facecolor('#f9f9f9')
    ax.legend(fontsize=7.2,ncol=2,loc='lower left',frameon=True,framealpha=0.88,
              columnspacing=0.8,handlelength=1.2)
    ax.text(0.02,0.94,'Context lines stay above EXP3 under most threats',
            transform=ax.transAxes,ha='left',va='top',fontsize=7.6,color='#555',
            bbox=dict(boxstyle='round,pad=0.22',facecolor='white',alpha=0.80,edgecolor='none'))
    panel_label(ax,'D','Context-Capacity Efficiency by Threat')


def base_style():
    plt.rcParams.update({
        'font.family':'DejaVu Sans','font.size':11.5,
        'axes.titlesize':12,'axes.titleweight':'bold',
        'axes.labelsize':10.5,'xtick.labelsize':9.5,'ytick.labelsize':9.5,
        'legend.fontsize':9,'axes.spines.top':False,'axes.spines.right':False,
        'axes.grid':True,'grid.alpha':0.20,'grid.linewidth':0.6,
    })


# ════════════════════════════════════════════════════════════════════════════
def build_G8():
    base_style()
    fig = plt.figure(figsize=(16,12)); fig.patch.set_facecolor('white')
    gs  = gridspec.GridSpec(2,2,figure=fig,hspace=0.52,wspace=0.42)
    axA = fig.add_subplot(gs[0,0]); axB = fig.add_subplot(gs[0,1])
    axC = fig.add_subplot(gs[1,0]); axD = fig.add_subplot(gs[1,1])

    # A — notched box + strip: Oracle-gap by family
    fams=['CMAB','iCMAB','EXP3','Hybrid']; fc=[C['CMAB'],C['iCMAB'],C['EXP3'],C['HYBRID']]
    dA=[GAP_DATA[f] for f in fams]
    bp=axA.boxplot(dA,patch_artist=True,notch=True,
        medianprops=dict(color='white',linewidth=2.5),
        whiskerprops=dict(linewidth=1.4,linestyle='--'),capprops=dict(linewidth=1.8),
        flierprops=dict(marker='D',markersize=3.5,alpha=0.45,linestyle='none'))
    for p,col in zip(bp['boxes'],fc): p.set_facecolor(col); p.set_alpha(0.82)
    for i,(d,col) in enumerate(zip(dA,fc),1):
        jit=RNG.uniform(-0.22,0.22,len(d))
        axA.scatter(np.full(len(d),i)+jit,d,s=24,color=col,alpha=0.38,zorder=3,linewidths=0)
    label_box_medians(axA, range(1, 5), dA, fc, dy=0.8)
    axA.axhline(15,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    axA.text(4.42,16.8,'85% eff.',ha='right',va='bottom',fontsize=9,color=C['THRESH'])
    axA.set_xticks(range(1,5)); axA.set_xticklabels(fams,fontsize=10.5)
    axA.set_ylabel('Oracle Gap (pp)'); axA.set_facecolor('#f9f9f9')
    fam_handles=[mpatches.Patch(color=col,alpha=0.82,label=fam) for fam,col in zip(fams,fc)]
    axA.legend(handles=fam_handles,loc='upper right',ncol=2,frameon=True,framealpha=0.88,fontsize=8,title='Family')
    panel_label(axA,'A','Oracle-Gap Distribution by Model Family')
    panel_subtitle(axA, 'Oracle-gap distribution')

    # B — grouped box: capacity paradox
    n=5; pos_T=[i*2.6+0.45 for i in range(n)]; pos_Tb=[i*2.6+1.15 for i in range(n)]
    def dboxes(ax,dl,pos,col,lbl):
        b=ax.boxplot(dl,positions=pos,widths=0.52,patch_artist=True,
            medianprops=dict(color='white',linewidth=2.2),
            whiskerprops=dict(linewidth=1.3),capprops=dict(linewidth=1.3),
            flierprops=dict(marker='o',markersize=3,alpha=0.38))
        for p in b['boxes']: p.set_facecolor(col); p.set_alpha(0.82)
        return mpatches.Patch(color=col,alpha=0.82,label=lbl)
    phT=dboxes(axB,T_BOX,pos_T,C['T'],'T-type')
    phTb=dboxes(axB,TB_BOX,pos_Tb,C['Tb'],'Tb-type')
    label_box_medians(axB, pos_T, T_BOX, [C['T']] * len(T_BOX), dy=0.45)
    label_box_medians(axB, pos_Tb, TB_BOX, [C['Tb']] * len(TB_BOX), dy=0.45)
    axB.axhline(0,color='black',lw=1.3)
    axB.fill_betweenx([-18,0],[-0.4,-0.4],[n*2.6-0.3,n*2.6-0.3],color='red',alpha=0.05,zorder=0)
    axB.fill_betweenx([0,18],[-0.4,-0.4],[n*2.6-0.3,n*2.6-0.3],color='green',alpha=0.05,zorder=0)
    axB.text(0.4,-2.2,'hurts ↓',fontsize=9,color='#c0392b')
    axB.text(0.4,0.8,'helps ↑',fontsize=9,color='#27ae60')
    tp=[(pos_T[i]+pos_Tb[i])/2 for i in range(n)]
    axB.set_xticks(tp); axB.set_xticklabels(SCENARIOS,rotation=12,ha='right',fontsize=9.5)
    axB.set_xlim(-0.4,n*2.6-0.3); axB.set_ylim(-6,10); axB.set_yticks([-5,0,5,10]); axB.set_ylabel('Δ Efficiency (pp)  s: 1→1.5')
    axB.legend(handles=[phT,phTb],loc='lower left',bbox_to_anchor=(0.01,0.02),ncol=2,frameon=True,framealpha=0.88,columnspacing=0.8,handlelength=1.1)
    axB.set_facecolor('#f9f9f9')
    panel_label(axB,'B','Capacity Paradox: Replay Scaling Δ by Scenario & Semantic')
    panel_subtitle(axB, 'Replay drop/recovery')

    # C — grouped bar: allocator × scenario
    anames=['Fixed','DynamicUCB','Thompson','Random']
    acols=[C['FIXED'],C['DUB'],C['THOM'],C['RAND']]
    x=np.arange(5); w=0.18; offs=np.array([-1.5,-0.5,0.5,1.5])*w
    for ai,(an,ac) in enumerate(zip(anames,acols)):
        axC.bar(x+offs[ai],ALLOC_SCEN_EFF[an],width=w*0.88,color=ac,alpha=0.85,
                label=an,edgecolor='white',lw=0.6)
    axC.axhline(85,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    axC.set_xticks(x); axC.set_xticklabels(SCENARIOS,fontsize=9.5)
    axC.set_ylim(55,105); axC.set_ylabel('Oracle-Norm. Efficiency (%)')
    axC.legend(loc='upper center',bbox_to_anchor=(0.5,0.995),ncol=4,frameon=True,framealpha=0.90,fontsize=7.2,columnspacing=0.8,handlelength=1.0)
    axC.text(0.02,0.82,'Default stays above 92%; Random drops to 68.3% in Markov',
             transform=axC.transAxes,ha='left',va='top',fontsize=7.6,color='#555',
             bbox=dict(boxstyle='round,pad=0.22',facecolor='white',alpha=0.78,edgecolor='none'))
    axC.set_facecolor('#f9f9f9')
    panel_label(axC,'C','Allocator Efficiency per Scenario (iCPursuitNeuralUCB)')
    panel_subtitle(axC, 'Allocator efficiency')

    # D — context-capacity detail replacing duplicate cross-testbed content
    draw_context_capacity_panel(axD)
    panel_subtitle(axD, 'Context-capacity effects')

    fig.subplots_adjust(top=0.96)
    fig.text(0.5,-0.008,
        'Sources: tab:model_family_comparison, tab:rq3b, tab:rq3c, '
        'tab:external_default_standard_4000_2000, fig:capacity_all',
        ha='center',fontsize=8.5,color='#666')
    fig.savefig(OUT_G8,dpi=220,bbox_inches='tight',facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_G8}")


# ════════════════════════════════════════════════════════════════════════════
def build_G9():
    base_style()
    fig = plt.figure(figsize=(18,14)); fig.patch.set_facecolor('white')
    gs  = gridspec.GridSpec(3,3,figure=fig,hspace=0.58,wspace=0.42)
    ax1=fig.add_subplot(gs[0,0]); ax2=fig.add_subplot(gs[0,1]); ax3=fig.add_subplot(gs[0,2])
    ax4=fig.add_subplot(gs[1,0]); ax5=fig.add_subplot(gs[1,1]); ax6=fig.add_subplot(gs[1,2])
    ax7=fig.add_subplot(gs[2,0]); ax8=fig.add_subplot(gs[2,1]); ax9=fig.add_subplot(gs[2,2])

    # A: fidelity decay log-scale
    q_rng=np.linspace(3,20,200)
    cp=['#2b6cb0','#e76f51','#2ca02c','#f28e2b']; lsp=['-','-','--','--']
    for nm,hp,col,ls in zip(PATH_NAMES,PATH_HOPS,cp,lsp):
        ys=[path_p(hp,q)*1e6 for q in q_rng]
        ax1.plot(q_rng,ys,color=col,lw=2.2,ls=ls,label=f'{nm} ({hp}-hop)')
    ax1.set_yscale('log')
    for nm,hp,q,col in zip(PATH_NAMES,PATH_HOPS,PATH_QUBITS,cp):
        yp=path_p(hp,q)*1e6
        ax1.scatter(q,yp,s=70,color=col,zorder=6,edgecolors='white',lw=1.2)
    ax1.scatter([],[],s=70,facecolor='white',edgecolor='#555',lw=1.2,label='Default marker')
    ax1.set_xlabel('Qubit Budget per Path'); ax1.set_ylabel('Success Prob. (×10⁻⁶)')
    ax1.legend(fontsize=6.3,ncol=2,loc='lower left',bbox_to_anchor=(0.02,0.42),bbox_transform=ax1.transAxes,frameon=True,framealpha=0.88,columnspacing=0.8,handlelength=1.4)
    ax1.set_facecolor('#f9f9f9')
    ax1.text(0.97,0.05,'3-hop paths 1000×\nworse than 2-hop',
             transform=ax1.transAxes,ha='right',va='bottom',fontsize=8,color='#c0392b',
             style='italic',bbox=dict(boxstyle='round,pad=0.3',facecolor='#fff3f3',alpha=0.8))
    ax1.text(0.02,0.05,'Markers show the default\nqubit-budget operating point',transform=ax1.transAxes,ha='left',va='bottom',fontsize=7.5,color='#555',bbox=dict(boxstyle='round,pad=0.25',facecolor='white',alpha=0.75,edgecolor='none'))
    panel_label(ax1,'A','Fidelity Decay: 2-hop vs 3-hop Paths')

    # B: qubit allocation heatmap
    alloc_budgets={'Fixed':[8,10,8,9],'Thompson':[9,9,9,8],'DynamicUCB':[8,11,7,9],'Random':[9,9,9,8]}
    path_short=['P1\n2-hop','P2\n2-hop','P3\n3-hop','P4\n3-hop']
    alloc_mat=np.array([alloc_budgets[a] for a in ['Fixed','Thompson','DynamicUCB','Random']])
    im=ax2.imshow(alloc_mat,cmap='YlOrRd',aspect='auto',vmin=5,vmax=13)
    ax2.set_xticks(range(4)); ax2.set_xticklabels(path_short,fontsize=9)
    ax2.set_yticks(range(4)); ax2.set_yticklabels(['Fixed','Thompson','DynamicUCB','Random'],fontsize=9)
    for i in range(4):
        for j in range(4):
            ax2.text(j,i,str(alloc_mat[i,j]),ha='center',va='center',fontsize=10,fontweight='bold',
                     color='white' if alloc_mat[i,j]>10 else '#333')
    plt.colorbar(im,ax=ax2,shrink=0.85,label='Qubits'); ax2.grid(False)
    panel_label(ax2,'B','Qubit Budget per Path × Allocator (Total=35)')

    # C: Oracle-gap bars
    draw_oracle_gap_panel(ax3)

    # D: RQ1 lollipop
    tier_colors={'Tier1':'#2ca02c','Tier2':'#f28e2b','Tier3':'#e63946'}
    tier_labels={'Tier1':'Viable (≥85%)','Tier2':'Degraded','Tier3':'Collapsed'}
    for i,(m,eff,tier) in enumerate(zip(RQ1_MODELS,RQ1_EFF,RQ1_TIERS)):
        col=tier_colors[tier]
        ax4.hlines(i,0,eff,colors=col,lw=1.8,alpha=0.6)
        ax4.scatter(eff,i,s=65,color=col,zorder=5,edgecolors='white',lw=1.0)
        ax4.text(eff+0.5,i,f'{eff:.1f}',va='center',fontsize=8,color=col)
    ax4.axvline(85,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    ax4.set_yticks(range(len(RQ1_MODELS))); ax4.set_yticklabels(RQ1_MODELS,fontsize=8.5)
    ax4.set_xlim(20,103); ax4.set_xlabel('Oracle-Norm. Efficiency % (Stochastic)')
    ax4.axhline(3.5,color='#bbb',lw=0.8,ls=':'); ax4.axhline(9.5,color='#bbb',lw=0.8,ls=':')
    ax4.set_facecolor('#f9f9f9')
    for tier,col in tier_colors.items():
        ax4.scatter([],[],color=col,s=50,label=tier_labels[tier])
    ax4.legend(fontsize=7.2,loc='upper right',ncol=3,frameon=True,framealpha=0.88,columnspacing=0.8,handlelength=1.1)
    ax4.text(0.98,0.04,'85% target line separates\nviable from degraded tiers',transform=ax4.transAxes,ha='right',va='bottom',fontsize=7.5,color='#555',bbox=dict(boxstyle='round,pad=0.25',facecolor='white',alpha=0.75,edgecolor='none'))
    panel_label(ax4,'D','RQ1: Algorithm Tier Separation (Stochastic Decoherence)')

    # E: threat heatmap
    im5=ax5.imshow(HEAT_MAT,cmap='RdYlGn',aspect='auto',vmin=60,vmax=100)
    ax5.set_xticks(range(5)); ax5.set_xticklabels(SCENARIOS,fontsize=8.5,rotation=10,ha='right')
    ax5.set_yticks(range(len(HEAT_ALGOS))); ax5.set_yticklabels(HEAT_ALGOS,fontsize=8.5)
    for i in range(len(HEAT_ALGOS)):
        for j in range(5):
            v=HEAT_MAT[i,j]
            ax5.text(j,i,f'{v:.0f}',ha='center',va='center',fontsize=8,fontweight='bold',
                     color='white' if v<75 else '#1a1a1a')
    plt.colorbar(im5,ax=ax5,shrink=0.85,label='Eff. %'); ax5.grid(False)
    panel_label(ax5,'E','Threat Escalation Heatmap: Algo × Scenario')

    # F: capacity paradox lines
    cap_styles={'T':('-',C['T'],'o',2.2),'1.5T':('--',C['T15'],'s',1.8),
                '2T':('-',C['T2'],'^',2.2),'Tb':('-',C['Tb'],'o',2.2),
                '1.5Tb':('--','#d4730a','s',1.8),'2Tb':('-','#8b2500','^',2.2)}
    x6=np.arange(5)
    cap_scens=['Stochastic','Markov','Adaptive','Online\nAdaptive','Baseline']
    for cname,(ls,col,mk,lw) in cap_styles.items():
        ax6.plot(x6,CAP_DATA[cname],ls=ls,color=col,marker=mk,lw=lw,ms=6,label=cname,alpha=0.88)
    ax6.axhline(85,color=C['THRESH'],ls=':',lw=1.1,alpha=0.7)
    ax6.set_xticks(x6); ax6.set_xticklabels(cap_scens,fontsize=9,rotation=10,ha='right')
    ax6.set_ylim(77,94); ax6.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax6.legend(fontsize=6.2,ncol=6,frameon=True,framealpha=0.88,loc='upper center',bbox_to_anchor=(0.5,0.99),columnspacing=0.7,handlelength=1.0)
    ax6.set_facecolor('#f9f9f9')
    ax6.annotate('Paradox:\n2Tb<Tb\nin Markov',
                 xy=(1,CAP_DATA['2Tb'][1]),xytext=(1.4,77.5),fontsize=7.5,color='#8b2500',
                 arrowprops=dict(arrowstyle='->',color='#8b2500',lw=0.9))
    panel_label(ax6,'F','Capacity Paradox: All 6 Replay Configs × Scenario')

    # G: scenario penalty bars
    draw_scenario_penalty_panel(ax7)

    # H: allocator risk profile
    draw_allocator_risk_panel(ax8)

    # I: cross-testbed violin
    tl=list(TESTBED_EFF.keys()); tv=list(TESTBED_EFF.values())
    tc9=[C['P2'],C['P7'],C['P12'],C['P8']]; amk9=['o','s','^','D']
    aln9=['iCPursuitNeural','CPursuitNeural','GNeuralUCB','EXPNeuralUCB']
    vd=[np.repeat(v,20)+RNG.normal(0,0.18,len(v)*20) for v in tv]
    vp=ax9.violinplot(vd,positions=range(4),widths=0.62,showmedians=False,showextrema=False)
    for body,col in zip(vp['bodies'],tc9): body.set_facecolor(col); body.set_alpha(0.35)
    bpI=ax9.boxplot(tv,positions=range(4),widths=0.20,patch_artist=True,
        medianprops=dict(color='white',lw=2.2),
        whiskerprops=dict(lw=1.3,color='#666'),capprops=dict(lw=1.3,color='#666'),
        flierprops=dict(marker='o',ms=3,alpha=0.4))
    for p,col in zip(bpI['boxes'],tc9): p.set_facecolor(col); p.set_alpha(0.88)
    for ji,(vals,col) in enumerate(zip(tv,tc9)):
        for ki,v in enumerate(vals):
            ax9.scatter(ji+RNG.uniform(-0.07,0.07),v,s=52,color=col,marker=amk9[ki],
                        zorder=6,alpha=0.95,edgecolors='white',lw=0.9)
        ax9.text(ji,max(vals)+0.8,f'gap:{100-max(vals):.1f}pp',ha='center',
                 fontsize=8,color=col,fontweight='bold')
    ax9.axhline(85,color=C['THRESH'],ls='--',lw=1.2,alpha=0.7)
    ax9.set_xticks(range(4)); ax9.set_xticklabels(tl,fontsize=8.4)
    ax9.set_ylabel('Oracle-Norm. Efficiency (%)')
    ax9.set_facecolor('#f9f9f9')
    for mk,mn in zip(amk9,aln9): ax9.scatter([],[],marker=mk,color='#555',s=42,label=mn[:12])
    ax9.legend(loc='lower left',ncol=2,frameon=True,framealpha=0.88,fontsize=7.2)
    panel_label(ax9,'I','Cross-Testbed Efficiency & Oracle Gap (Std. 4K/2K/5R)')

    fig.subplots_adjust(top=0.97)
    fig.text(0.5,-0.005,
        'Sources: §IV-A topology, tab:rq1masterstochastic, tab:rq2_adversarial, fig:capacity_all, '
        'tab:rq3c_allocators, tab:external_default_standard_4000_2000',
        ha='center',fontsize=8,color='#666')
    fig.savefig(OUT_G9,dpi=200,bbox_inches='tight',facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_G9}")


def build_allocator_risk_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.625, 4.59), dpi=200)
    fig.patch.set_facecolor('white')
    draw_allocator_risk_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.97, bottom=0.13)
    fig.savefig(OUT_PANEL_H, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_H}")


def build_rq1_tier_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.64, 4.58), dpi=200)
    fig.patch.set_facecolor('white')
    draw_rq1_tier_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.17, right=0.98, top=0.98, bottom=0.14)
    fig.savefig(OUT_PANEL_D, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_D}")


def build_oracle_gap_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.64, 4.58), dpi=200)
    fig.patch.set_facecolor('white')
    draw_oracle_gap_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.08, right=0.985, top=0.97, bottom=0.16)
    fig.savefig(OUT_PANEL_C, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_C}")


def build_capacity_all_configs_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.64, 4.585), dpi=200)
    fig.patch.set_facecolor('white')
    draw_capacity_all_configs_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.18)
    fig.savefig(OUT_PANEL_F, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_F}")


def build_scenario_penalty_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.64, 4.58), dpi=200)
    fig.patch.set_facecolor('white')
    draw_scenario_penalty_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.08, right=0.985, top=0.98, bottom=0.14)
    fig.savefig(OUT_PANEL_G, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_G}")


def build_cross_testbed_panel():
    base_style()
    fig, ax = plt.subplots(figsize=(7.64, 4.545), dpi=200)
    fig.patch.set_facecolor('white')
    draw_cross_testbed_panel(ax, include_panel_label=False)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.97, bottom=0.22)
    fig.savefig(OUT_PANEL_I, dpi=200, facecolor='white')
    plt.close(fig)
    print(f"Wrote {OUT_PANEL_I}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build ICNP G8/G9 result figures.")
    parser.add_argument(
        "--only",
        choices=["all", "panel-c", "panel-d", "panel-f", "panel-g", "panel-h", "panel-i"],
        default="all",
        help="Build all figures or only one manuscript-facing labeled panel.",
    )
    args = parser.parse_args()
    if args.only == "panel-c":
        build_oracle_gap_panel()
    elif args.only == "panel-d":
        build_rq1_tier_panel()
    elif args.only == "panel-f":
        build_capacity_all_configs_panel()
    elif args.only == "panel-g":
        build_scenario_penalty_panel()
    elif args.only == "panel-h":
        build_allocator_risk_panel()
    elif args.only == "panel-i":
        build_cross_testbed_panel()
    else:
        build_G8()
        build_G9()
        build_oracle_gap_panel()
        build_rq1_tier_panel()
        build_capacity_all_configs_panel()
        build_scenario_penalty_panel()
        build_allocator_risk_panel()
        build_cross_testbed_panel()
        OUT_G8_PUBLIC.write_bytes(OUT_G8.read_bytes())
        print(f"Wrote {OUT_G8_PUBLIC}")
        print("All done.")
