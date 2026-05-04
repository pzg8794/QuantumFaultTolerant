# Study Design Time Horizons and Configuration Summary Reduction Audit

This document records the validated reduction for the Study Design `Time horizons` paragraph and `tab:config_summary` table.

## Process requirements applied

The block was audited using the project paragraph/table workflow: show the original content, identify short topic/idea subtitles, check each topic against already-audited sections, check venue requirements, reduce each topic, recombine the paragraph/table, and then run a final reduction. Repeated content was handled through concise table entries and cross-consistency with the already-audited Study Design staging file.

The overlap check was performed against the already-audited Abstract, Introduction, Background, Related Work, System Model, Study Design Research Questions, Experimental Design opening, and Network configuration. The table is kept because the opening paragraph and Network configuration already reference `tab:config_summary`.

## Original content being audited

```tex
\noindent\textit{Time horizons.}
We evaluate 3 horizons---\small\texttt{4K,6K,8K} frames---to capture short-, mid-, and long-episode learning dynamics. Unless otherwise noted, primary results use 6K, with 4K vs.\ 8K comparisons in \textbf{RQ3a} to assess sample efficiency.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Experimental design matrix linking configuration dimensions to the research questions.\shee{The last column (RQ(s)) has inconsistent subscripts and superscripts}}
\label{tab:config_summary}
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.32\linewidth} >{\raggedright\arraybackslash}X >{\centering\arraybackslash}c}
\toprule
\textbf{Configuration Dimension} & \textbf{Options Tested} & \textbf{RQ(s)} \\
\midrule
Network topology   & 4-node, 4-path (2+3-hop)      & All \\
\small\texttt{Time horizons} & \textit{4K, 6K, 8K frames} & $RQ3_a$ \\
Qubit capacity     & 35 total (fixed) qubits       & All \\
\midrule
\small\texttt{Allocators} & \textit{Fixed, Thompson,}     & $RQ3_c$ \\
                    & \multicolumn{1}{l}{\textit{DynamicUCB, Random}} & \\
Replay capacity     & $T_b=sF_b,\;T=sF_c$ & $RQ3_b$ \\
\small\texttt{Threat models} & \textit{None, Stochastic, Markov,} & \RQOneText \& \\
                    & \multicolumn{1}{l}{\textit{Adaptive, OnlineAdaptive}} & \RQTwoText \\
Forecasting         & None, ARIMA ($n=50$),         & $RQ3_a$ \\
                    & \multicolumn{1}{l}{ARIMA ($n=100$)} & \\
\midrule
Algorithm families  & Classical (4), Predictive (1) & \RQOneText \& \\
                    & Adversarial (3), Context (6) & \RQTwoText \\
\midrule
\textit{Evaluation phases} & & \\
\quad Ph 1 (MAB baseline)         & 12 conditions   & $RQ_1$ \\
\quad \textit{Ph 2 (CMAB / iCMAB)}  & \textit{180 conditions / family} & $RQ2_(a-b)$ \\
\quad Ph 3 (Dynamic allocation)   & 240 conditions  & $RQ3_c$ \\
\quad \textit{Ph 4 (Capacity ablation)} & \textit{120 conditions} & $RQ3_b$ \\
\bottomrule
\end{tabularx}
\end{table}
```

## Paragraph 1 original

```tex
We evaluate 3 horizons---\small\texttt{4K,6K,8K} frames---to capture short-, mid-, and long-episode learning dynamics. Unless otherwise noted, primary results use 6K, with 4K vs.\ 8K comparisons in \textbf{RQ3a} to assess sample efficiency.
```

## Paragraph 1 topics / ideas

1. Horizon range
2. Primary horizon and sample-efficiency comparison

## Topic/Idea 1 -- Horizon range

Original sentence:

```tex
We evaluate 3 horizons---\small\texttt{4K,6K,8K} frames---to capture short-, mid-, and long-episode learning dynamics.
```

Overlap check:

- Abstract: none.
- Introduction: none.
- Background: low -- repeated decision-making is introduced, but not horizon settings.
- Related Work: none.
- System Model: medium -- frames are defined, but horizon choices are not.
- Research Questions: medium -- horizon comparisons support deployment sensitivity under RQ3.
- Experimental Design opening: high -- this is one of the configuration axes summarized by `\Cref{tab:config_summary}`.
- Network configuration: low -- topology/capacity are already staged, not horizons.

Venue check:

Keep. This is concrete experimental-design information. Clean up formatting: use `three` instead of `3`, and avoid `\small` inside prose.

Decision:

Reduce lightly.

Validated reduction:

```tex
We evaluate \texttt{4K}, \texttt{6K}, and \texttt{8K}-frame horizons to capture short-, mid-, and long-episode learning dynamics.
```

## Topic/Idea 2 -- Primary horizon and sample-efficiency comparison

Original sentence:

```tex
Unless otherwise noted, primary results use 6K, with 4K vs.\ 8K comparisons in \textbf{RQ3a} to assess sample efficiency.
```

Overlap check:

- Abstract: none.
- Introduction: low.
- Background: low.
- Related Work: none.
- System Model: medium -- uses frame/horizon structure but does not set default.
- Research Questions: high -- current audited venue RQs use only RQ1/RQ2/RQ3, not RQ3a.
- Experimental Design opening: high -- table maps design options to RQs.
- Network configuration: none.

Venue check:

Keep the 6K default and 4K/8K comparison, but remove `RQ3a` because the audited RQ section does not preserve sub-RQ labels. Use plain RQ3.

Decision:

Reduce and align with audited RQ structure.

Validated reduction:

```tex
Primary results use \texttt{6K} unless noted; \texttt{4K}/\texttt{8K} comparisons support the RQ3 sample-efficiency analysis.
```

## Paragraph 1 further reduced paragraph

Validated for staging:

```tex
\noindent\textit{Time horizons.}
We evaluate \texttt{4K}, \texttt{6K}, and \texttt{8K}-frame horizons to capture short-, mid-, and long-episode learning dynamics. Primary results use \texttt{6K} unless noted; \texttt{4K}/\texttt{8K} comparisons support the RQ3 sample-efficiency analysis.
```

## Table topics / ideas

1. Design-to-RQ mapping
2. Configuration dimensions
3. RQ notation consistency
4. Consistency with already-staged topology/capacity
5. Evaluation phase summary

## Table decision

The table is kept. The caption is reduced, internal author comments are removed, RQ notation is normalized to RQ1/RQ2/RQ3, and table rows are aligned with the already-staged Network configuration and Research Questions.

Validated table:

```tex
\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Experimental design matrix linking configuration dimensions, tested options, and research-question coverage.}
\label{tab:config_summary}
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.32\linewidth} >{\raggedright\arraybackslash}X >{\centering\arraybackslash}c}
\toprule
\textbf{Configuration Dimension} & \textbf{Options Tested} & \textbf{RQ(s)} \\
\midrule
Network topology & 4-node, 4-path diamond & All \\
Time horizons & \texttt{4K}, \texttt{6K}, \texttt{8K} frames & RQ3 \\
Qubit capacity & 35 total qubits, fixed & All \\
\midrule
Allocators & Fixed, ThompsonSampling, DynamicUCB, Random & RQ3 \\
Replay capacity & $T_b=sF_b$, $T=sF_c$ & RQ3 \\
Threat models & Baseline, Stochastic, Markov, Adaptive, OnlineAdaptive & RQ1, RQ2 \\
Forecasting & None, ARIMA ($n=50$), ARIMA ($n=100$) & RQ3 \\
\midrule
Algorithm families & Classical, Predictive, Adversarial, Contextual/Neural & RQ1, RQ2 \\
\midrule
\multicolumn{3}{l}{\textit{Evaluation phases}} \\
\quad Ph 1 (MAB baseline) & 12 conditions & RQ1 \\
\quad Ph 2 (CMAB/iCMAB) & 180 conditions per family & RQ2 \\
\quad Ph 3 (Dynamic allocation) & 240 conditions & RQ3 \\
\quad Ph 4 (Capacity ablation) & 120 conditions & RQ3 \\
\bottomrule
\end{tabularx}
\end{table}
```

## Validated reduced block

```tex
\noindent\textit{Time horizons.}
We evaluate \texttt{4K}, \texttt{6K}, and \texttt{8K}-frame horizons to capture short-, mid-, and long-episode learning dynamics. Primary results use \texttt{6K} unless noted; \texttt{4K}/\texttt{8K} comparisons support the RQ3 sample-efficiency analysis.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Experimental design matrix linking configuration dimensions, tested options, and research-question coverage.}
\label{tab:config_summary}
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.32\linewidth} >{\raggedright\arraybackslash}X >{\centering\arraybackslash}c}
\toprule
\textbf{Configuration Dimension} & \textbf{Options Tested} & \textbf{RQ(s)} \\
\midrule
Network topology & 4-node, 4-path diamond & All \\
Time horizons & \texttt{4K}, \texttt{6K}, \texttt{8K} frames & RQ3 \\
Qubit capacity & 35 total qubits, fixed & All \\
\midrule
Allocators & Fixed, ThompsonSampling, DynamicUCB, Random & RQ3 \\
Replay capacity & $T_b=sF_b$, $T=sF_c$ & RQ3 \\
Threat models & Baseline, Stochastic, Markov, Adaptive, OnlineAdaptive & RQ1, RQ2 \\
Forecasting & None, ARIMA ($n=50$), ARIMA ($n=100$) & RQ3 \\
\midrule
Algorithm families & Classical, Predictive, Adversarial, Contextual/Neural & RQ1, RQ2 \\
\midrule
\multicolumn{3}{l}{\textit{Evaluation phases}} \\
\quad Ph 1 (MAB baseline) & 12 conditions & RQ1 \\
\quad Ph 2 (CMAB/iCMAB) & 180 conditions per family & RQ2 \\
\quad Ph 3 (Dynamic allocation) & 240 conditions & RQ3 \\
\quad Ph 4 (Capacity ablation) & 120 conditions & RQ3 \\
\bottomrule
\end{tabularx}
\end{table}
```

## Status

Validated by project owner and ready for staging in `ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex`.
