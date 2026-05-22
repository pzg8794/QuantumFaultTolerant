
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
import json, os

os.makedirs("output", exist_ok=True)
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


FIGURE_COLORS = {
    'CPursuit': '#2ECC71',
    'GNeuralUCB': '#F7B731',
    'EXPNeuralUCB': '#FF6B35',
    'iCEpsGreedy': '#8E44AD',
    'CEpsGreedy': '#45AAF2',
    'iCPursuit': '#1B9CFC',
    'EXP3': '#FC5C65',
}

THREAT_COLORS = {
    'Stochastic': '#4DA6FF',
    'Markov': '#2B6CB0',
    'Adaptive': '#E63946',
    'Online': '#F28E2B',
    'Baseline': '#2ECC71',
}

CAPACITY_LINE_COLORS = {
    'T': '#2B6CB0',
    '1.5T': '#4DA6FF',
    '2T': '#7B2CBF',
    'Tb': '#E76F51',
    '1.5Tb': '#D4730A',
    '2Tb': '#8B2500',
}


def add_last_point_value_labels(fig, y_offsets=None):
    offsets = y_offsets or [10, 2, 14, -6, -14, 6, -10, 0]
    for index, trace in enumerate(fig.data):
        y_values = list(getattr(trace, 'y', []) or [])
        if not y_values:
            continue
        color = (
            getattr(getattr(trace, 'line', None), 'color', None)
            or getattr(getattr(trace, 'marker', None), 'color', None)
            or '#444444'
        )
        fig.add_annotation(
            x=1.01,
            y=float(y_values[-1]),
            xref='paper',
            yref='y',
            text=f"{float(y_values[-1]):.1f}%",
            showarrow=False,
            xanchor='left',
            yshift=offsets[index % len(offsets)],
            font=dict(size=8, color=color),
            bgcolor='rgba(255,255,255,0.72)',
            bordercolor='rgba(0,0,0,0.10)',
            borderwidth=1,
        )


def set_plotly_y_top(fig, top, bottom_padding=1.0):
    numeric_values = []
    for trace in fig.data:
        numeric_values.extend(float(value) for value in getattr(trace, 'y', []) if value is not None)
    bottom = max(min(numeric_values) - bottom_padding, 0.0) if numeric_values else 0.0
    fig.update_yaxes(range=[bottom, top])

# ============================================================
# AUDIT DATA FROM main.tex
# All data are directly extracted from the LaTeX source
# ============================================================

# --- Fig 2 (fig:context_exp3_capacity): Line chart, 4 series ---
scenarios_5 = ['Stochastic','Markov','Adaptive','OnlineAdap','Baseline']
ctx_T   = [89.9, 85.9, 86.8, 88.8, 93.2]
ctx_Tb  = [88.1, 86.1, 87.7, 86.5, 93.3]
exp_T   = [81.4, 80.6, 77.2, 82.5, 90.5]
exp_Tb  = [81.1, 81.7, 79.5, 81.1, 85.9]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=scenarios_5, y=ctx_T,  mode='lines+markers', name='Context (T)',  line=dict(width=3)))
fig2.add_trace(go.Scatter(x=scenarios_5, y=ctx_Tb, mode='lines+markers', name='Context (Tb)', line=dict(width=3)))
fig2.add_trace(go.Scatter(x=scenarios_5, y=exp_T,  mode='lines+markers', name='EXP3 (T)',     line=dict(width=3, dash='dash')))
fig2.add_trace(go.Scatter(x=scenarios_5, y=exp_Tb, mode='lines+markers', name='EXP3 (Tb)',    line=dict(width=3, dash='dash')))
fig2.update_layout(
    margin=dict(t=8, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=9)
)
fig2.update_xaxes(title_text="Scenario")
fig2.update_yaxes(title_text="Efficiency (%)", range=[74, 96])
save_plotly_figure(fig2, "output/fig2_context_exp3.png")
with open("output/fig2_context_exp3.png.meta.json","w") as f:
    json.dump({"caption":"Fig 2 – Context vs EXP3 Oracle Efficiency (current pgfplots)","description":"Line chart showing Context T/Tb vs EXP3 T/Tb across 5 scenarios. Current range 74-96 compresses differences."}, f)

# --- Fig 3 (fig:floor): Grouped bar, peak/mean/floor ---
algos_5 = ['iCEpsGreedy','iCPursuit','CPursuit','EXPNeuralUCB','EXPUCB']
peak  = [88.5, 72.7, 96.2, 94.0, 90.7]
mean_ = [86.1, 69.5, 77.3, 86.2, 76.0]
floor_= [83.3, 66.5, 37.2, 59.9, 69.3]

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    name='Peak',
    x=algos_5,
    y=peak,
    opacity=0.9,
    text=[f'{value:.1f}%' for value in peak],
    textposition='outside',
    cliponaxis=False,
))
fig3.add_trace(go.Bar(
    name='Mean',
    x=algos_5,
    y=mean_,
    opacity=0.9,
    text=[f'{value:.1f}%' for value in mean_],
    textposition='outside',
    cliponaxis=False,
))
fig3.add_trace(go.Bar(
    name='Floor',
    x=algos_5,
    y=floor_,
    opacity=0.9,
    text=[f'{value:.1f}%' for value in floor_],
    textposition='outside',
    cliponaxis=False,
))
fig3.update_layout(
    barmode='group',
    margin=dict(t=8, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=9, x=0.99, y=0.99, xanchor='right', yanchor='top')
)
fig3.update_xaxes(title_text="Algorithm")
fig3.update_yaxes(title_text="Efficiency (%)", range=[0, 104])
save_plotly_figure(fig3, "output/fig3_floor.png")
with open("output/fig3_floor.png.meta.json","w") as f:
    json.dump({"caption":"Fig 3 – Peak/Mean/Floor at default 2T–2Tb budget","description":"Grouped bar showing peak, mean and worst-case floor for 5 algorithms."}, f)

# --- Fig 5 (fig:global_win_share): Single bar ---
algos_wins = ['CPursuit','GNeuralUCB','EXPNeuralUCB','iCEpsGreedy','CEpsGreedy']
wins = [27.8, 11.9, 11.6, 37.5, 9.7]
fig5 = go.Figure()
for algo, win_share in zip(algos_wins, wins):
    fig5.add_trace(go.Bar(
        x=[algo],
        y=[win_share],
        name=algo,
        marker_color=FIGURE_COLORS.get(algo, '#4C78A8'),
        text=[f'{win_share:.1f}%'],
        textposition='outside',
    ))
fig5.update_layout(
    margin=dict(t=10, r=12, b=34, l=52, pad=0),
    barmode='group',
    legend=in_figure_legend(font_size=8, y=0.90),
)
fig5.update_xaxes(title_text="Algorithm")
fig5.update_yaxes(title_text="Win Share (%)", range=[0,45])
save_plotly_figure(fig5, "output/fig5_win_share.png")
with open("output/fig5_win_share.png.meta.json","w") as f:
    json.dump({"caption":"Fig 5 – Win dominance under default allocator","description":"Bar chart: top-5 win dominance percentages."}, f)

# --- Fig 6 (fig:context_capacity_effects): 4-series line ---
ctx_T2   = [89.9, 85.9, 86.8, 88.8, 93.2]
ctx_Tb2  = [88.1, 86.1, 87.7, 86.5, 93.3]
nctx_T   = [81.4, 80.6, 77.2, 82.5, 90.5]
nctx_Tb  = [81.1, 81.7, 79.5, 81.1, 85.9]
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=scenarios_5, y=ctx_T2,  mode='lines+markers', name='Context T',      line=dict(width=3)))
fig6.add_trace(go.Scatter(x=scenarios_5, y=ctx_Tb2, mode='lines+markers', name='Context Tb',     line=dict(width=3)))
fig6.add_trace(go.Scatter(x=scenarios_5, y=nctx_T,  mode='lines+markers', name='Non-Context T',  line=dict(width=3, dash='dash')))
fig6.add_trace(go.Scatter(x=scenarios_5, y=nctx_Tb, mode='lines+markers', name='Non-Context Tb', line=dict(width=3, dash='dash')))
fig6.update_layout(
    margin=dict(t=8, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=9)
)
fig6.update_xaxes(title_text="Scenario")
fig6.update_yaxes(title_text="Efficiency (%)", range=[74, 95])
save_plotly_figure(fig6, "output/fig6_context_capacity.png")
with open("output/fig6_context_capacity.png.meta.json","w") as f:
    json.dump({"caption":"Fig 6 – Context vs Non-Context efficiency (T and Tb)","description":"Near-duplicate of Fig 2 — same data, essentially identical chart."}, f)

# --- Fig 7 (fig:scenario_penalties): grouped bar, 4 series ---
algos_pen = ['EXPUCB','EXPNeural','iCEpsGreedy','CPursuit']
stoch_pen = [7.3,  12.4, 4.9, 3.2]
markov_pen= [9.8,   6.9, 7.0, 7.6]
adapt_pen = [8.9,  13.8, 6.1, 6.3]
online_pen= [7.2,  10.1, 5.8, 4.5]
fig7 = go.Figure()
fig7.add_trace(go.Bar(name='Stochastic', x=algos_pen, y=stoch_pen, marker_color=THREAT_COLORS['Stochastic']))
fig7.add_trace(go.Bar(name='Markov',     x=algos_pen, y=markov_pen, marker_color=THREAT_COLORS['Markov']))
fig7.add_trace(go.Bar(name='Adaptive',   x=algos_pen, y=adapt_pen, marker_color=THREAT_COLORS['Adaptive']))
fig7.add_trace(go.Bar(name='Online',     x=algos_pen, y=online_pen, marker_color=THREAT_COLORS['Online']))
fig7.update_layout(
    barmode='group',
    margin=dict(t=10, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=8, x=0.99, y=0.98, orientation='v', xanchor='right', yanchor='top')
)
fig7.update_xaxes(title_text="Algorithm")
fig7.update_yaxes(title_text="Penalty (pp vs Baseline)", range=[0, 14])
save_plotly_figure(fig7, "output/fig7_penalties.png")
with open("output/fig7_penalties.png.meta.json","w") as f:
    json.dump({"caption":"Fig 7 – Scenario penalties (pp drop vs Baseline) per algorithm","description":"Grouped bar: 4 algorithms × 4 threat penalties. EXPNeuralUCB shows highest penalty."}, f)

# --- Fig 9 (fig:capacity_all): 6-series line, T/1.5T/2T/Tb/1.5Tb/2Tb ---
T_     = [81.5, 86.5, 88.9, 83.2, 90.3]
T15    = [82.3, 80.5, 83.7, 90.3, 88.0]
T2_    = [84.8, 85.9, 90.2, 90.6, 93.4]
Tb_    = [80.6, 83.2, 84.8, 86.6, 87.9]
Tb15   = [81.0, 80.7, 87.7, 85.2, 87.0]
Tb2_   = [81.7, 78.0, 87.1, 84.2, 91.0]
fig9 = go.Figure()
fig9.add_trace(go.Scatter(x=scenarios_5, y=T_,   mode='lines+markers', name='T',    line=dict(width=2, color=CAPACITY_LINE_COLORS['T'])))
fig9.add_trace(go.Scatter(x=scenarios_5, y=T15,  mode='lines+markers', name='1.5T', line=dict(width=2, color=CAPACITY_LINE_COLORS['1.5T'])))
fig9.add_trace(go.Scatter(x=scenarios_5, y=T2_,  mode='lines+markers', name='2T',   line=dict(width=2, color=CAPACITY_LINE_COLORS['2T'])))
fig9.add_trace(go.Scatter(x=scenarios_5, y=Tb_,  mode='lines+markers', name='Tb',   line=dict(width=2, dash='dot', color=CAPACITY_LINE_COLORS['Tb'])))
fig9.add_trace(go.Scatter(x=scenarios_5, y=Tb15, mode='lines+markers', name='1.5Tb',line=dict(width=2, dash='dot', color=CAPACITY_LINE_COLORS['1.5Tb'])))
fig9.add_trace(go.Scatter(x=scenarios_5, y=Tb2_, mode='lines+markers', name='2Tb',  line=dict(width=2, dash='dot', color=CAPACITY_LINE_COLORS['2Tb'])))
fig9.update_layout(
    margin=dict(t=8, r=116, b=42, l=60, pad=0),
    legend=in_figure_legend(font_size=8, x=0.99, y=0.99, xanchor='right', yanchor='top')
)
fig9.update_xaxes(title_text="Scenario")
fig9.update_yaxes(title_text="Efficiency (%)", range=[78, 94])
add_last_point_value_labels(fig9)
save_plotly_figure(fig9, "output/fig9_capacity.png")
with open("output/fig9_capacity.png.meta.json","w") as f:
    json.dump({"caption":"Fig 9 – Capacity paradox: T vs Tb at 3 scales","description":"6-line chart showing capacity paradox. Zoomed y-axis to 76-96 to reveal crossovers."}, f)

# --- Fig 10 (fig:threat_rules): 4-series line ---
scenarios_4 = ['Stochastic','Markov','Adaptive','OnlineAdaptive']
thompson   = [86.7, 89.2, 91.0, 90.3]
dynucb     = [85.7, 86.1, 91.0, 90.9]
random_    = [69.1, 69.3, 79.3, 77.5]
noalloc    = [89.5, 88.9, 90.2, 89.9]
fig10 = go.Figure()
fig10.add_trace(go.Scatter(x=scenarios_4, y=thompson, mode='lines+markers', name='Thompson',  line=dict(width=3)))
fig10.add_trace(go.Scatter(x=scenarios_4, y=dynucb,   mode='lines+markers', name='DynamicUCB',line=dict(width=3)))
fig10.add_trace(go.Scatter(x=scenarios_4, y=noalloc,  mode='lines+markers', name='No-alloc',  line=dict(width=3, dash='dot')))
fig10.add_trace(go.Scatter(x=scenarios_4, y=random_,  mode='lines+markers', name='Random',    line=dict(width=2, dash='dash')))
fig10.update_layout(
    margin=dict(t=8, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=8, x=0.02, y=0.99, orientation='h', xanchor='left', yanchor='top')
)
fig10.add_hline(y=85, line_color='#555555', line_dash='dash', line_width=1.2)
fig10.add_annotation(
    x=0.98,
    y=0.08,
    xref='paper',
    yref='paper',
    text='85% target; Random trails under threat',
    showarrow=False,
    xanchor='right',
    font=dict(size=8, color='#555555'),
    bgcolor='rgba(255,255,255,0.72)',
)
fig10.update_xaxes(title_text="Threat Regime")
fig10.update_yaxes(title_text="Efficiency (%)", range=[65, 95])
save_plotly_figure(fig10, "output/fig10_threat_rules.png")
with open("output/fig10_threat_rules.png.meta.json","w") as f:
    json.dump({"caption":"Fig 10 – Allocator efficiency by threat regime","description":"Line chart: Thompson/DynamicUCB/No-alloc/Random across 4 threat scenarios."}, f)

# --- Fig 13 (fig:convergence_hybrid): 4-series convergence ---
frames = ['1K','2K','3K','4K','5K','6K','7K','8K']
iCP = [65,74,82,86,88,88.5,88.8,88.9]
CP  = [63,70,76,82,85,87,87.5,87.7]
EXP = [45,52,58,61,62.5,63,63.2,63.0]
GNU = [8,12,16,19,21,22,23,24]
fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=frames, y=iCP, mode='lines+markers', name='iCPursuitNeuralUCB', line=dict(width=3)))
fig13.add_trace(go.Scatter(x=frames, y=CP,  mode='lines+markers', name='CPursuitNeuralUCB',  line=dict(width=3)))
fig13.add_trace(go.Scatter(x=frames, y=EXP, mode='lines+markers', name='EXPNeuralUCB',       line=dict(width=2, dash='dash')))
fig13.add_trace(go.Scatter(x=frames, y=GNU, mode='lines+markers', name='GNeuralUCB',          line=dict(width=2, dash='dash')))
fig13.update_layout(
    margin=dict(t=8, r=12, b=42, l=54, pad=0),
    legend=in_figure_legend(font_size=9)
)
fig13.update_xaxes(title_text="Frames")
fig13.update_yaxes(title_text="Efficiency (%)")
set_plotly_y_top(fig13, top=90)
save_plotly_figure(fig13, "output/fig13_convergence.png")
with open("output/fig13_convergence.png.meta.json","w") as f:
    json.dump({"caption":"Fig 13 – Convergence: running efficiency by algorithm","description":"4-line convergence plot. GNeuralUCB data appears wrong (8-24%) — likely placeholder."}, f)

# --- Fig 14 (fig:context_hybrid): grouped bar, 5 scenarios × 5 algos ---
algos_h = ['iCPursuit','CPursuit','EXPNeuralUCB','GNeuralUCB','EXP3']
stoch_h  = [67.4, 89.9, 80.6, 85.5, 77.0]
markov_h = [68.1, 85.8, 84.6, 82.6, 75.1]
adapt_h  = [70.0, 89.4, 76.1, 87.0, 76.8]
online_h = [67.3, 89.1, 86.4, 84.2, 77.1]
base_h   = [72.0, 95.3, 88.0, 89.9, 81.9]
fig14 = go.Figure()
fig14.add_trace(go.Bar(name='Stochastic',    x=algos_h, y=stoch_h))
fig14.add_trace(go.Bar(name='Markov',        x=algos_h, y=markov_h))
fig14.add_trace(go.Bar(name='Adaptive',      x=algos_h, y=adapt_h))
fig14.add_trace(go.Bar(name='OnlineAdaptive',x=algos_h, y=online_h))
fig14.add_trace(go.Bar(name='Baseline',      x=algos_h, y=base_h))
fig14.add_shape(
    type='line',
    x0=-0.5,
    x1=len(algos_h) - 0.5,
    y0=95,
    y1=95,
    line=dict(color='#3498db', width=1.2, dash='dash'),
)
fig14.update_layout(
    barmode='group',
    margin=dict(t=8, r=116, b=42, l=60, pad=0),
    legend=in_figure_legend(font_size=8, x=0.99, y=0.90, orientation='v', xanchor='right', yanchor='top')
)
add_last_point_value_labels(fig14)
fig14.add_annotation(
    x=0.02,
    y=0.92,
    xref='paper',
    yref='paper',
    text='95% threshold',
    showarrow=False,
    font=dict(size=9, color='#3498db'),
    bgcolor='rgba(255,255,255,0.70)',
)
fig14.add_annotation(
    x=0.02,
    y=0.06,
    xref='paper',
    yref='paper',
    text='CPursuit clears 85% in every threat; EXP3 trails by 8-18pp',
    showarrow=False,
    xanchor='left',
    font=dict(size=8, color='#555555'),
    bgcolor='rgba(255,255,255,0.72)',
)
fig14.update_xaxes(title_text="Algorithm")
fig14.update_yaxes(title_text="Efficiency (%)", range=[55, 100])
save_plotly_figure(fig14, "output/fig14_context_hybrid.png")
with open("output/fig14_context_hybrid.png.meta.json","w") as f:
    json.dump({"caption":"Fig 14 – Hybrid efficiency across algorithms and threats","description":"5-group bar chart. iCPursuit data looks like paper-baseline not hybrid. CPursuit leads."}, f)

print("All 8 charts rendered.")
