#!/usr/bin/env python3
"""
build_G10_G14.py — Regenerate PhD NN-style analysis figures G10-G14
Run from repo root: python figures/icnp_graphs/build_G10_G14.py
Requires: pandas, plotly, kaleido
Data: GA-Work/Validated_Logs/Master_Dataset_EXP3.csv + Master_Dataset_CMABs.csv
"""
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

def hex_rgba(h, a=0.25):
    r,g,b = int(h[1:3],16),int(h[3:5],16),int(h[5:7],16)
    return f"rgba({r},{g},{b},{a})"

# Oracle-normalised efficiency % per model per scenario (from validated logs)
all_models = {
    "EXPNeuralUCB": [91.61, 86.69, 59.94, 85.53, 78.79],
    "GNeuralUCB":   [80.99, 74.87, 90.68, 90.93, 77.78],
    "EXPUCB":       [77.20, 69.26, 71.66, 72.45, 69.36],
    "CPursuit":     [95.87, 84.24, 89.95, 91.66, 82.81],
    "CEpsilonGreedy":[92.74,85.99, 86.90, 86.73, 79.95],
    "CThompson":    [67.33, 63.94, 63.49, 62.84, 62.92],
}
C = {
    "EXPNeuralUCB":"#FF6B35","GNeuralUCB":"#F7B731","EXPUCB":"#FC5C65",
    "CPursuit":"#2ECC71","CEpsilonGreedy":"#45AAF2","CThompson":"#A29BFE",
}
slabels = ["Baseline","Markov","Stochastic","Adaptive","OnlineAdap."]
mnames  = list(all_models.keys())

def save(fig, name, caption, description):
    path = os.path.join(OUT, name)
    fig.write_image(path)
    with open(path + ".meta.json", "w") as f:
        json.dump({"caption": caption, "description": description}, f)
    print(f"  {name} ({os.path.getsize(path)//1024} KB)")


def review_legend(x=0.5, y=0.02, orientation="h", xanchor="center", yanchor="bottom", font_size=9):
    return dict(
        orientation=orientation,
        x=x,
        y=y,
        xanchor=xanchor,
        yanchor=yanchor,
        bgcolor="rgba(255,255,255,0.80)",
        bordercolor="rgba(0,0,0,0.12)",
        borderwidth=1,
        font=dict(size=font_size),
    )


def annotate_box_means(fig):
    maxima = []
    for trace in fig.data:
        values = [float(value) for value in getattr(trace, "y", []) if value is not None]
        if not values:
            continue
        mean_value = sum(values) / len(values)
        trace_max = max(values)
        maxima.append(trace_max)
        fig.add_annotation(
            x=getattr(trace, "name", ""),
            y=trace_max + 1.4,
            xref="x",
            yref="y",
            text=f"avg {mean_value:.1f}%",
            showarrow=False,
            font=dict(size=8, color="#444444"),
            bgcolor="rgba(255,255,255,0.75)",
        )
    if maxima:
        fig.update_yaxes(range=[0, max(maxima) + 3.2])

# G10: Oracle Gap Box Plot
fig = go.Figure()
for m, ev in all_models.items():
    gaps = [100-v for v in ev]
    fig.add_trace(go.Box(y=gaps, name=m, boxpoints="all", jitter=0.4,
        marker_color=C[m], line_color=C[m], fillcolor=hex_rgba(C[m]),
        marker_size=8, showlegend=False))
fig.update_layout(
    title={"text":"Oracle Gap by Model (5 Threat Scenarios)<br>"
           "<span style='font-size:14px;font-weight:normal'>"
           "Lower = better. CPursuit tightest; EXPNeuralUCB collapses under Stochastic.</span>"},
    yaxis_title="Oracle Gap (%)", xaxis_title="Model")
fig.add_hline(y=15, line_color="#555555", line_dash="dash", line_width=1.2)
fig.add_annotation(x=0.98, y=0.42, xref="paper", yref="paper", text="15% gap target<br>Lower is better", showarrow=False, xanchor="right", font=dict(size=9, color="#555555"), bgcolor="rgba(255,255,255,0.72)")
annotate_box_means(fig)
save(fig, "G10_gap_box.png",
     "G10: Oracle-Gap Box Plot — CPursuit tightest; EXPNeuralUCB highest variance",
     "Box plot of oracle gap across 5 threat scenarios per routing model")

# G11: Efficiency Heatmap
eff_mat = np.array([all_models[m] for m in mnames])
fig11 = go.Figure(go.Heatmap(
    z=eff_mat, x=slabels, y=mnames,
    colorscale="RdYlGn", zmin=55, zmax=97,
    text=np.round(eff_mat,1), texttemplate="%{text}%",
    textfont={"size":12}, colorbar=dict(title="Eff %"),
))
fig11.update_layout(
    title={"text":"Efficiency Heatmap: Model x Threat Scenario<br>"
           "<span style='font-size:14px;font-weight:normal'>"
           "Green = high efficiency. CMAB Pursuit leads; Thompson lags.</span>"},
    xaxis_title="Threat Scenario", yaxis_title="Routing Model")
save(fig11, "G11_heatmap.png",
     "G11: Efficiency Heatmap — CPursuit green; CThompson red across all scenarios",
     "Heatmap of Oracle-normalised efficiency across routing models and threat scenarios")

# G12: 4-Panel Gap Analysis
fig4 = make_subplots(rows=2, cols=2, vertical_spacing=0.22, horizontal_spacing=0.16,
    subplot_titles=["A. Efficiency by Scenario","B. Stochastic vs Adaptive Gap",
                    "C. Mean Oracle Gap +/- Std","D. Overall Model Ranking"])
top4 = ["CPursuit","CEpsilonGreedy","GNeuralUCB","EXPNeuralUCB"]
for m in top4:
    fig4.add_trace(go.Bar(x=["BL","MK","ST","AD","OA"], y=all_models[m],
        name=m, marker_color=C[m], showlegend=True), row=1, col=1)
fig4.update_yaxes(range=[50,100], title_text="Eff %", row=1, col=1)
fig4.update_xaxes(title_text="Scenario", row=1, col=1)
x_s = [100-all_models[m][2] for m in mnames]
y_a = [100-all_models[m][3] for m in mnames]
fig4.add_trace(go.Scatter(x=x_s, y=y_a, mode="markers",
    marker=dict(size=18, color=[C[m] for m in mnames], opacity=0.9),
    showlegend=False, text=mnames, hoverinfo="text+x+y"), row=1, col=2)
fig4.update_xaxes(title_text="Stochastic Gap %", row=1, col=2)
fig4.update_yaxes(title_text="Adaptive Gap %", row=1, col=2)
mean_g = [np.mean([100-v for v in all_models[m]]) for m in mnames]
std_g  = [np.std([100-v for v in all_models[m]]) for m in mnames]
sn = ["ExpNe","GNeur","ExpUC","CPurs","CEps","CTh"]
fig4.add_trace(go.Bar(x=sn, y=mean_g,
    error_y=dict(type="data", array=std_g, visible=True),
    marker_color=[C[m] for m in mnames], showlegend=False), row=2, col=1)
fig4.update_yaxes(title_text="Mean Gap %", row=2, col=1)
avg_eff = {m: np.mean(all_models[m]) for m in mnames}
sm = sorted(avg_eff, key=lambda model: avg_eff[model])
sm_s = ["CThom","ExpUCB","GNeur","CEps","ExpNe","CPurs"]
fig4.add_trace(go.Bar(x=[avg_eff[m] for m in sm], y=sm_s, orientation="h",
    marker_color=[C[m] for m in sm], showlegend=False), row=2, col=2)
fig4.update_xaxes(range=[60,97], title_text="Avg Eff %", row=2, col=2)
fig4.update_layout(
    title={"text":"G12: 4-Panel Gap Analysis — Neural vs CMAB Routing"},
    legend=dict(orientation="v", y=0.98, x=1.01, font_size=9), height=680)
save(fig4, "G12_4panel.png",
     "G12: 4-Panel Gap Analysis — CPursuit leads; EXPNeuralUCB stochastic collapse",
     "4-panel: A=efficiency bars, B=gap scatter, C=mean gap error bars, D=overall ranking")

# G13: Capacity Paradox
cap_labels = ["4k (1x)", "6k (1.5x)", "8k (2x)"]
cap_data = {
    "Baseline": [80.99, 83.84, 91.64],
    "Stochastic": [90.68, 91.51, 79.23],
    "Adaptive":   [90.93, 92.97, 84.46],
    "Markov":     [74.87, 85.43, 89.45],
}
cap_c = {"Baseline":"#2ECC71","Stochastic":"#FC5C65","Adaptive":"#FF6B35","Markov":"#45AAF2"}
fig13 = go.Figure()
for threat, vals in cap_data.items():
    fig13.add_trace(go.Scatter(x=cap_labels, y=vals, mode="lines+markers",
        name=threat, line=dict(color=cap_c[threat], width=3), marker=dict(size=12)))
fig13.add_vrect(x0=1.5, x1=2.5, fillcolor="rgba(255,80,80,0.08)",
    annotation_text="Paradox Zone", annotation_position="top right", line_width=0)
fig13.update_layout(
    title={"text":"G13: Capacity Paradox — More Capacity Hurts Under Adversarial Threats"},
    xaxis_title="Capacity Level", yaxis_title="Oracle-Norm. Efficiency %",
    yaxis_range=[70,97], legend=review_legend(x=0.5, y=0.05))
fig13.add_hline(y=95, line_color="#3498db", line_dash="dash", line_width=1.2)
save(fig13, "G13_capacity_paradox.png",
     "G13: Capacity Paradox — extra capacity hurts Stochastic/Adaptive",
     "Line chart of efficiency vs capacity level per threat type")

# G14: Regret Trajectory
regret_data = {
    "CPursuit":       [0.060, 0.103, 0.088, 0.100],
    "CEpsilonGreedy": [0.073, 0.116, 0.100, 0.116],
    "EXPNeuralUCB":   [0.084, 0.133, 0.095, 0.133],
    "GNeuralUCB":     [0.093, 0.145, 0.207, 0.107],
    "EXPUCB":         [0.123, 0.254, 0.254, 0.239],
    "CThompson":      [0.327, 0.345, 0.365, 0.370],
}
regret_labels = {
    "CPursuit": "CPursuit",
    "CEpsilonGreedy": "CEpsGreedy",
    "EXPNeuralUCB": "EXPNeural",
    "GNeuralUCB": "GNeural",
    "EXPUCB": "EXPUCB",
    "CThompson": "CThompson",
}
frames = [1000, 2000, 3000, 4000]
fig14 = go.Figure()
for model, vals in regret_data.items():
    fig14.add_trace(go.Scatter(x=frames, y=vals, mode="lines+markers",
        name=regret_labels[model], line=dict(color=C[model], width=2.5), marker=dict(size=9)))
fig14.update_layout(
    title={"text":"G14: Normalized Regret Trajectory Across Capacity Levels"},
    xaxis_title="Frames (Capacity Steps)", yaxis_title="Normalized Regret",
    width=920,
    margin=dict(l=60, r=24, t=72, b=48, pad=0),
    legend=review_legend(x=0.5, y=0.99, font_size=7, yanchor="top"))
save(fig14, "G14_regret.png",
     "G14: Regret Trajectory — CPursuit tightest; Thompson Sampling diverges",
     "Line chart of normalized regret across capacity steps per routing model")

print("\nAll G10-G14 figures written to", OUT)
