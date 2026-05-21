#!/usr/bin/env python3
"""
QuantumFaultTolerant — ICNP Draft Result Graphs
All 6 figures: G1–G6
Requires: plotly, kaleido (pip install plotly kaleido)
Run: python icnp_graphs.py
Output: G1_capacity_paradox.png, G2_robustness_floor.png,
        G3_family_summary.png, G4_deployment_rules.png,
        G5_convergence.png, G6_heatmap.png
"""

import os, json
import numpy as np
import plotly.graph_objects as go

os.makedirs("icnp_graphs", exist_ok=True)
EXPORT_SCALE = int(os.environ.get("ICNP_PLOT_SCALE", "3"))


def save_plotly_figure(fig, output_path):
    # Increase raster resolution while preserving the layout's visual proportions.
    fig.write_image(output_path, scale=EXPORT_SCALE)


def in_figure_legend(font_size=10, y=0.02, x=0.5, orientation='h', xanchor='center', yanchor='bottom'):
    return dict(
        orientation=orientation,
        yanchor=yanchor,
        y=y,
        xanchor=xanchor,
        x=x,
        bgcolor='rgba(255,255,255,0.78)',
        bordercolor='rgba(0,0,0,0.10)',
        borderwidth=1,
        font=dict(size=font_size),
    )


def set_plotly_y_top(fig, top, bottom_padding=1.0):
    numeric_values = []
    for trace in fig.data:
        numeric_values.extend(float(value) for value in getattr(trace, 'y', []) if value is not None)
    bottom = max(min(numeric_values) - bottom_padding, 0.0) if numeric_values else 0.0
    fig.update_yaxes(range=[bottom, top])

# ── shared data ────────────────────────────────────────────────────────────────
SCENARIOS_5 = ['Stochastic', 'Markov', 'Adaptive', 'OnlineAdaptive', 'Baseline']

# ══════════════════════════════════════════════════════════════════════════════
# G1  CAPACITY PARADOX
#     Compact OnlineAdaptive stress slice used in the Figure 6A caption
#     Source: validated RQ3b ThompsonSampling / Tb / OnlineAdaptive slice
# ══════════════════════════════════════════════════════════════════════════════
capacity_scales = ['s=1', 's=1.5', 's=2']
onlineadaptive_tb_eff = [89.2, 84.9, 90.8]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    name='ThompsonSampling + Tb / OnlineAdaptive',
    x=capacity_scales,
    y=onlineadaptive_tb_eff,
    mode='lines+markers+text',
    line=dict(color='#7B2CBF', width=4),
    marker=dict(symbol='circle', size=16, color='#7B2CBF', line=dict(color='white', width=2)),
    text=[f"{value:.1f}%" for value in onlineadaptive_tb_eff],
    textposition=['top center', 'bottom center', 'top center'],
    textfont=dict(size=12, color='#1f2f4d'),
))
fig1.add_shape(type='rect', x0=0.75, x1=1.25, y0=84.2, y1=89.7,
               fillcolor='rgba(231,76,60,0.08)', line_width=0)
fig1.add_shape(type='rect', x0=1.75, x1=2.25, y0=84.2, y1=91.4,
               fillcolor='rgba(39,174,96,0.08)', line_width=0)
fig1.add_annotation(x='s=1.5', y=87.1, text='drop −4.4 pp',
                    showarrow=True, arrowhead=2, ax=-55, ay=-18,
                    font=dict(color='#e74c3c', size=11),
                    arrowcolor='#e74c3c',
                    bgcolor='rgba(255,255,255,0.80)')
fig1.add_annotation(x='s=2', y=88.0, text='recovery +6.0 pp',
                    showarrow=True, arrowhead=2, ax=-58, ay=35,
                    font=dict(color='#27ae60', size=11),
                    arrowcolor='#27ae60',
                    bgcolor='rgba(255,255,255,0.80)')
fig1.update_layout(
    margin=dict(t=8, r=12, b=44, l=60, pad=0),
    legend=in_figure_legend(font_size=9, y=0.99, yanchor='top'),
    showlegend=True,
)
fig1.update_xaxes(title_text="Replay-capacity scale")
fig1.update_yaxes(title_text="Oracle-Norm. Efficiency (%)", range=[83.5, 92.0])
save_plotly_figure(fig1, "icnp_graphs/G1_capacity_paradox.png")
print("✓ G1 saved")


# ══════════════════════════════════════════════════════════════════════════════
# G2  ROBUSTNESS FLOOR
#     Horizontal dot-range: floor / mean / peak per algorithm
#     Source: fig:floor in main.tex
# ══════════════════════════════════════════════════════════════════════════════
algos   = ['iCEpsGreedy', 'iCPursuit', 'CPursuit', 'EXPNeuralUCB', 'EXPUCB']
peak_v  = [88.5, 72.7, 96.2, 94.0, 90.7]
mean_v  = [86.1, 69.5, 77.3, 86.2, 76.0]
floor_v = [83.3, 66.5, 37.2, 59.9, 69.3]

fig2 = go.Figure()
for i, algo in enumerate(algos):
    fig2.add_shape(type='line',
                   x0=floor_v[i], x1=peak_v[i], y0=algo, y1=algo,
                   line=dict(color='rgba(160,160,160,0.4)', width=10))

fig2.add_trace(go.Scatter(
    x=floor_v, y=algos, mode='markers', name='Floor',
    marker=dict(symbol='square', size=14, color='#e74c3c'),
    hovertemplate="%{y}: Floor %{x}%<extra></extra>",
))
fig2.add_trace(go.Scatter(
    x=mean_v, y=algos, mode='markers', name='Mean',
    marker=dict(symbol='circle', size=14, color='#f39c12'),
    hovertemplate="%{y}: Mean %{x}%<extra></extra>",
))
fig2.add_trace(go.Scatter(
    x=peak_v, y=algos, mode='markers', name='Peak',
    marker=dict(symbol='diamond', size=14, color='#27ae60'),
    hovertemplate="%{y}: Peak %{x}%<extra></extra>",
))

for i, algo in enumerate(algos):
    label_specs = [
        (floor_v[i], f"floor {floor_v[i]:.1f}%", '#e74c3c', -24, 'right'),
        (mean_v[i], f"mean {mean_v[i]:.1f}%", '#f39c12', 10, 'left'),
        (peak_v[i], f"peak {peak_v[i]:.1f}%", '#27ae60', 10, 'left'),
    ]
    for x_value, label, color, xshift, xanchor in label_specs:
        fig2.add_annotation(
            x=x_value,
            y=algo,
            text=label,
            showarrow=False,
            xanchor=xanchor,
            xshift=xshift,
            yshift=-9 if label.startswith('mean') else 10 if label.startswith('peak') else 0,
            font=dict(size=9, color=color),
            bgcolor='rgba(255,255,255,0.72)',
            bordercolor='rgba(0,0,0,0.08)',
            borderwidth=1,
        )

fig2.add_shape(type='line', x0=85, x1=85, y0=-0.5, y1=4.5,
               line=dict(color='#3498db', width=1.5, dash='dash'))
fig2.add_annotation(x=86.5, y=0.2, text="85% deploy threshold",
                    showarrow=False, font=dict(color='#3498db', size=10),
                    xanchor='left')
fig2.add_annotation(x=0.02, y=0.98, xref='paper', yref='paper',
                    text="Scope: Markov + Adaptive + OnlineAdaptive",
                    showarrow=False, xanchor='left', yanchor='top',
                    font=dict(color='#1f2f4d', size=10),
                    bgcolor='rgba(255,255,255,0.78)',
                    bordercolor='rgba(0,0,0,0.12)',
                    borderwidth=1)

fig2.update_layout(
    margin=dict(t=8, r=12, b=44, l=66, pad=0),
    legend=in_figure_legend(),
    xaxis_range=[25, 110],
)
fig2.update_xaxes(title_text="Oracle-Norm. Efficiency (%)")
fig2.update_yaxes(title_text="")
save_plotly_figure(fig2, "icnp_graphs/G2_robustness_floor.png")
print("✓ G2 saved")


# ══════════════════════════════════════════════════════════════════════════════
# G3  MAIN CLAIM SUMMARY
#     Bar: best-in-family efficiency per model family
#     Source: tab:model_family_comparison + RQ summary in main.tex
# ══════════════════════════════════════════════════════════════════════════════
families  = ['Classical\nMABs', 'EXP3-based', 'CMAB\nBaselines',
             'iCMAB\nBaselines', 'Hybrid\nNeural']
best_effs = [77.0, 85.37, 89.90, 88.56, 90.86]
colors_fam = ['#95a5a6', '#e67e22', '#2980b9', '#8e44ad', '#27ae60']

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=families, y=best_effs,
    marker_color=colors_fam,
    text=[f"{v:.1f}%" for v in best_effs],
    textposition='outside', width=0.6,
))

# Bracket: classical → hybrid gap
fig3.add_shape(type='line', x0=-0.35, x1=-0.35, y0=77.0,  y1=90.86,
               line=dict(color='#e74c3c', width=2))
fig3.add_shape(type='line', x0=-0.35, x1=-0.25, y0=77.0,  y1=77.0,
               line=dict(color='#e74c3c', width=2))
fig3.add_shape(type='line', x0=-0.35, x1=-0.25, y0=90.86, y1=90.86,
               line=dict(color='#e74c3c', width=2))
fig3.add_annotation(x=-0.48, y=83.9, text="+13.9pp",
                    showarrow=False, font=dict(color='#e74c3c', size=12),
                    textangle=-90)

# 85% threshold
fig3.add_shape(type='line', x0=-0.5, x1=4.5, y0=85, y1=85,
               line=dict(color='#005BBB', width=3, dash='dash'))
fig3.add_annotation(x=4.45, y=85.65, text="85% threshold",
                    showarrow=False, font=dict(color='#3498db', size=10),
                    xanchor='right',
                    bgcolor='rgba(255,255,255,0.80)',
                    bordercolor='rgba(0,91,187,0.30)',
                    borderwidth=1)

fig3.update_layout(
    margin=dict(t=8, r=12, b=34, l=56, pad=0),
    showlegend=False,
    xaxis_range=[-0.6, 4.6],
)
fig3.update_xaxes(title_text="Model Family")
fig3.update_yaxes(title_text="Oracle-Norm. Efficiency (%)", range=[60, 95])
save_plotly_figure(fig3, "icnp_graphs/G3_family_summary.png")
print("✓ G3 saved")


# ══════════════════════════════════════════════════════════════════════════════
# G4  DEPLOYMENT LOLLIPOP
#     Scenario → threat-tuned config vs. static default
#     Source: RQ3d deployment rules in main.tex
# ══════════════════════════════════════════════════════════════════════════════
scenarios_d    = ['Baseline', 'Stochastic', 'Markov', 'Adaptive', 'OnlineAdaptive']
effs_d         = [99.9, 95.4, 93.2, 95.7, 99.8]
static_default = [96.0, 94.8, 93.0, 92.8, 99.8]

fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    x=static_default, y=scenarios_d, mode='lines+markers',
    name='Static default',
    line=dict(color='#95a5a6', width=2, dash='dot'),
    marker=dict(symbol='square', size=12, color='#95a5a6'),
))
for i in range(len(scenarios_d)):
    fig4.add_shape(type='line',
                   x0=static_default[i], x1=effs_d[i],
                   y0=scenarios_d[i], y1=scenarios_d[i],
                   line=dict(color='#27ae60', width=3))

fig4.add_trace(go.Scatter(
    x=effs_d, y=scenarios_d, mode='markers+text',
    name='Threat-tuned optimum',
    marker=dict(symbol='circle', size=18, color='#27ae60'),
    text=[f"{v}%" for v in effs_d],
    textposition='middle right',
    textfont=dict(size=12),
))

gains = [round(effs_d[i] - static_default[i], 1) for i in range(len(scenarios_d))]
for i in range(len(scenarios_d)):
    if gains[i] > 0:
        mid = (static_default[i] + effs_d[i]) / 2
        fig4.add_annotation(x=mid, y=scenarios_d[i],
                            text=f"+{gains[i]}pp",
                            showarrow=False, yshift=-14,
                            font=dict(size=9, color='#27ae60'),
                            xanchor='center')

fig4.add_annotation(
    x=95.7,
    y='Adaptive',
    text="ThompsonSampling + Tb, s=1.5",
    showarrow=True,
    arrowhead=2,
    ax=74,
    ay=-44,
    font=dict(size=9, color='#1f2f4d'),
    arrowcolor='#27ae60',
    bgcolor='rgba(255,255,255,0.82)',
    bordercolor='rgba(39,174,96,0.35)',
    borderwidth=1,
)

fig4.update_layout(
    margin=dict(t=8, r=12, b=44, l=72, pad=0),
    legend=in_figure_legend(font_size=8, x=0.02, y=0.98, orientation='v', xanchor='left', yanchor='top'),
    xaxis_range=[88, 103],
)
fig4.update_xaxes(title_text="Oracle-Norm. Efficiency (%)")
fig4.update_yaxes(title_text="Threat Scenario")
save_plotly_figure(fig4, "icnp_graphs/G4_deployment_rules.png")
print("✓ G4 saved")


# ══════════════════════════════════════════════════════════════════════════════
# G5  CONVERGENCE
#     Running efficiency vs. frames (line, y-axis zoomed 0–100)
#     Source: fig:convergence_hybrid in main.tex
#     ⚠ GNeuralUCB series (8–24%) is likely a placeholder — verify before submit
# ══════════════════════════════════════════════════════════════════════════════
frame_labels = ['1K','2K','3K','4K','5K','6K','7K','8K']
iCP_c = [65, 74, 82, 86, 88,   88.5, 88.8, 88.9]
CP_c  = [63, 70, 76, 82, 85,   87,   87.5, 87.7]
EXP_c = [45, 52, 58, 61, 62.5, 63,   63.2, 63.0]
GNU_c = [8,  12, 16, 19, 21,   22,   23,   24  ]  # ⚠ verify

fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=frame_labels, y=iCP_c, mode='lines+markers',
    name='iCPursuitNeuralUCB', line=dict(width=3), marker=dict(size=7)))
fig5.add_trace(go.Scatter(x=frame_labels, y=CP_c, mode='lines+markers',
    name='CPursuitNeuralUCB',  line=dict(width=3), marker=dict(size=7)))
fig5.add_trace(go.Scatter(x=frame_labels, y=EXP_c, mode='lines+markers',
    name='EXPNeuralUCB', line=dict(width=2, dash='dash'), marker=dict(size=7)))
fig5.add_trace(go.Scatter(x=frame_labels, y=GNU_c, mode='lines+markers',
    name='GNeuralUCB (verify data)', line=dict(width=2, dash='dot'), marker=dict(size=7)))

fig5.add_shape(type='line', x0=0, x1=7, y0=85, y1=85,
               line=dict(color='#3498db', width=1.5, dash='dash'))
fig5.add_annotation(x='8K', y=86.5, text="85% threshold",
                    showarrow=False, font=dict(color='#3498db', size=10),
                    xanchor='right')

fig5.update_layout(
    margin=dict(t=8, r=12, b=46, l=60, pad=0),
    legend=in_figure_legend(font_size=8, x=0.12, y=0.22, orientation='v', xanchor='left', yanchor='bottom'),
)
fig5.update_xaxes(title_text="Frames (thousands)", range=[-0.2, 7.5])
fig5.update_yaxes(title_text="Running Efficiency (%)")
set_plotly_y_top(fig5, top=90)
save_plotly_figure(fig5, "icnp_graphs/G5_convergence.png")
print("✓ G5 saved")


# ══════════════════════════════════════════════════════════════════════════════
# G6  TRUE HEATMAP — CPursuitNeuralUCB
#     Allocator × Scenario efficiency matrix
#     Source: fig:heatmap in main.tex
# ══════════════════════════════════════════════════════════════════════════════
allocators  = ['Fixed', 'DynamicUCB', 'Thompson']
scenarios_h = ['Stochastic', 'Markov', 'Adaptive', 'OnlineAdaptive', 'Baseline']

# rows = scenarios (top=lowest threat, bottom=highest)
z = np.array([
    [94.0, 68.2, 65.1],   # Stochastic
    [89.6, 71.2, 66.8],   # Markov
    [89.9, 70.6, 65.9],   # Adaptive
    [90.0, 68.8, 65.0],   # OnlineAdaptive
    [99.7, 69.2, 69.9],   # Baseline
])
text_vals = [[f"{v:.1f}%" for v in row] for row in z]

fig6 = go.Figure(go.Heatmap(
    z=z, x=allocators, y=scenarios_h,
    text=text_vals, texttemplate="%{text}",
    textfont=dict(size=13),
    colorscale='RdYlGn', zmin=60, zmax=100,
    colorbar=dict(title="Efficiency (%)", thickness=15),
))
fig6.update_layout(
    margin=dict(t=8, r=12, b=34, l=60, pad=0),
)
fig6.update_xaxes(title_text="Allocator Strategy", side='bottom')
fig6.update_yaxes(title_text="Threat Scenario")
save_plotly_figure(fig6, "icnp_graphs/G6_heatmap.png")
print("✓ G6 saved")

print("\nAll 6 graphs saved to ./icnp_graphs/")
