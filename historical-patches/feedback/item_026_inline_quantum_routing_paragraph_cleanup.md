# Item 026 — Inline cleanup: quantum routing/resource-allocation paragraph

## Feedback item

**Reviewer:** Unattached inline manuscript issue  
**Date/time:** Not specified  
**Feedback:**

> Inline highlighted text indicates unresolved wording: `\hl{?creates the problem that?}`

## Task

Replace the unresolved highlighted phrase with a clean causal transition that explains why quantum routing constraints make path selection inseparable from qubit allocation.

## Content in question

```tex
Quantum routing also differs fundamentally from classical packet-switching routing because the underlying resource is \emph{entanglement}, not transferable data~\cite{kimble2008quantum,wehner2018quantum}. Quantum states cannot be copied or amplified due to the no-cloning theorem~\cite{wootters1982single}, so classical store-and-forward buffering does not apply. Instead, routing must establish and consume entanglement under limited memory coherence, probabilistic swapping, and fidelity loss induced by operations and delay~\cite{bennett1993teleporting,zukowski1993event}. This \hl{?creates the problem that?} path selection is inseparable from resource allocation: how qubits are distributed across candidate paths affects both achievable success probability and the feedback the learner receives. In realistic deployments, routing therefore becomes a joint decision problem over \emph{path selection}, \emph{qubit allocation}, and \emph{learning under uncertainty}~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

## Proposed solution

```tex
Quantum routing differs fundamentally from classical packet-switching because the routed resource is \emph{entanglement}, not transferable data~\cite{kimble2008quantum,wehner2018quantum}. Quantum states cannot be copied or amplified due to the no-cloning theorem~\cite{wootters1982single}, so classical store-and-forward buffering does not apply. Instead, routing must establish and consume entanglement under limited memory coherence, probabilistic swapping, and fidelity loss induced by operations and delay~\cite{bennett1993teleporting,zukowski1993event}. These constraints make path selection inseparable from resource allocation: how qubits are distributed across candidate paths affects both achievable success probability and the feedback observed by the learner. In realistic deployments, routing therefore becomes a joint decision problem over \emph{path selection}, \emph{qubit allocation}, and \emph{learning under uncertainty}~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

## Decision / status

**Approved.** Replace the highlighted unresolved phrase with the cleaner causal transition and remove the duplicate `routing` wording in the first sentence.
