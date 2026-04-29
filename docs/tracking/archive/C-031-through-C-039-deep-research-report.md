# Review of Tasks C-031 Through C-039

## Context from the current manuscript

Your paper already frames the problem as **joint entanglement routing (path selection) and qubit allocation** under **stochastic and adversarial threats**, and it positions the contribution as a **unified evaluation + deployment guidance** across multiple algorithm families and capacity/allocator semantics. This is explicit in the Introduction’s opening, where you describe dynamic path selection and allocation under “noisy, uncertain, and adversarial conditions” and motivate a bandit formulation. citeturn6view1

The Introduction also already includes a “Gap in Prior Work” subsection and a structured cascade into “Our Approach and Evaluation Scope,” followed by a named “Capacity Paradox” claim and a “Key Contributions” list. citeturn25view0turn25view1turn25view3

That structure matters because most of C-031…C-039 is about aligning **framing + clarity + citation hygiene** with what the paper is already doing.

## Title and abstract alignment

### C-031 Title — include “Entanglement Routing”

**What you have now.** The title currently foregrounds “Qubit Allocation” and “Stochastic Bandits.” citeturn2view0  
However, the abstract, keywords, and the body repeatedly emphasize *entanglement routing* and *threat/adversarial regimes*, not only “stochastic.” The keywords explicitly include “entanglement routing” and “adversarial learning.” citeturn24view0turn22view0

**Does the proposed fix make sense?** Yes: adding “entanglement routing” is strongly consistent with how the paper presents itself (keywords + intro + cross-testbed validation). citeturn22view0turn25view3  
Where I’d tighten your proposal is the **“stochastic” vs “threat-aware/adversarial” implication**. Your current title says “stochastic,” but the paper’s central taxonomy and results emphasize adversarial escalation (Markov/Adaptive/OnlineAdaptive) and a capacity paradox driven by *predictability under strategic disruption*. citeturn24view1turn25view3

**Recommended direction (principle).**  
- Keep “Entanglement Routing and Qubit Allocation” (good).  
- Replace “stochastic bandits” with a phrase that covers your full scope: “context-aware bandits,” “bandit learning under threats,” or “adversarial-robust bandits.” This prevents the title from underselling the core message.

**Implementation check.** If you keep “context-aware” in the title, it is supported by your repeated framing that context/representation stabilizes routing and by the way you compare contextual/iCMAB/hybrid families. citeturn25view2turn24view1

---

### C-032 Abstract — clarify contribution type; reduce numeric overload; fix referents

**What you have now.** The abstract currently:  
- Opens with the right high-level problem statement (joint routing + allocation under noisy/adversarial conditions). citeturn6view1turn26view0  
- Then becomes very number-dense (“552 configurations,” “13 algorithms,” “4 allocators,” “2 capacity settings,” plus multiple efficiency ranges across internal/external suites). citeturn26view0turn25view2  
- Uses an ambiguous pronoun (“They outperform…”), where “they” refers to pursuit–neural hybrids but is not re-anchored. citeturn26view0  
- Contains an inline author note and a duplicated/alternate abstract draft that should not remain in the compiled manuscript. citeturn26view0

**Does your proposed rewrite structure make sense?** Yes—your rewrite approach is consistent with what the paper actually claims: evaluation across threats, identifying pursuit–neural hybrids as robust, and highlighting the “capacity paradox.” citeturn26view0turn25view3  
But there are two important adjustments to keep it “fit-to-paper”:

1. **Be careful with what is “new.”**  
   The abstract must not imply you *only* evaluate unless that’s the intended framing, but it also must not over-claim novel algorithms unless your manuscript clearly presents CPursuitNeuralUCB/iCPursuitNeuralUCB as proposed by you (not imported baselines). Your own related-work contrasts describe Huang/EXPNeuralUCB as prior work and say “we introduce pursuit–neural hybrids,” which supports a “we develop/introduce” statement—but keep it measured. citeturn8view3turn8view4turn25view0

2. **Ensure counts are consistent with the body.**  
   In the Introduction you say “16 models (15 learned + Oracle)” and later you report “7,890 evaluations across 835 unique settings.” citeturn25view1turn24view1  
   In the abstract you say “13 algorithms” and “552 configurations.” citeturn26view0  
   This is not automatically wrong (it could reflect different corpora), but it will confuse a reviewer unless you either:
   - remove most counts from the abstract, or  
   - make the abstract’s count language match the “curated corpora” framing (e.g., “across curated corpora spanning X models…”). citeturn25view0turn25view1

**A fit-to-paper abstract strategy.**  
- Keep **one** scale indicator (either “552 configurations” or “three external testbeds spanning 15–100 nodes”), but not both plus multiple internal/external efficiency ranges. citeturn26view0turn25view2  
- Name the subject in every key claim (“pursuit–neural hybrids outperform…”) instead of “they.” citeturn26view0  
- Keep the “capacity paradox” sentence, but preserve the paper’s own wording around “predictability—not bandwidth” and keep “pp” if you mean *percentage points*, since you already use that in the abstract draft. citeturn26view0turn25view3

## Introduction citations and flow

### C-033 Add citations for the “reliable end-to-end entanglement is difficult to sustain” claim

**What you have now.** The sentence claims fragility, probabilistic generation/swapping, and degradation under decoherence/interference, but it carries no immediate citations; the following clause cites repeaters and waiting time, while later sentences cite no-cloning, teleportation, and probabilistic swapping. citeturn22view0

**Does the proposed fix make sense?** Yes: that sentence is a factual claim and should be anchored. citeturn22view0  
Your instinct to cite foundational repeater/swapping work is directionally correct, but you can also strengthen it with citations that explicitly talk about decoherence/noise in quantum networking practice.

**High-confidence support from your cross-testbed sources.**  
Because you already cite the cross-testbed papers later, you can safely use one (or more) as evidence that these are *practical routing constraints*, not just theoretical background:

- The entity["people","Vini Chaudhary","quantum networking author"] et al. “Learning-based Route Selection in Noisy Quantum Communication Networks” explicitly states that qubits are vulnerable to decoherence due to noise in channels and environment and motivates repeaters and entanglement swapping under imperfect memories/gates. citeturn27view0turn27view1  
- entity["people","Maoli Liu","quantum networking author"] et al. “Quantum BGP with Online Path Selection via Network Benchmarking” motivates routing in part because coherence loss limits transmission and because no-cloning prevents store-and-forward, and it formalizes noise via channels (including depolarizing models). citeturn17view0turn19view0  

**Recommendation.**  
Anchor the “fragile/probabilistic/decoherence” sentence with citations that cover:
- probabilistic/repeater constraints (you already cite Briegel + a waiting-time paper immediately after), and  
- explicit decoherence/noise in routing contexts (Chaudhary and/or QBGP are strong here). citeturn22view0turn27view0turn17view0

---

### C-034 Waiting-time effects citations

**What you have now.** You cite repeater architecture and a waiting-time reference for “stochastic waiting-time effects that compound along multi-hop routes.” citeturn22view0

**Does your “keep as-is or add one more” stance make sense?** Mostly, but with an important caveat: adding a citation should be done only if it truly supports *waiting-time compounding* in repeater chains.

You already have good contextual motivation from the cross-testbed papers: Chaudhary explicitly discusses multi-hop repeater paths, swapping steps, and decoherence/noise accumulation in channels/memory/operations. citeturn27view1turn27view2  
If you add one more citation here, the best kind is a **repeater waiting-time / memory-decoherence** reference, not a general multi-path routing protocol.

**Recommendation.**  
- If `wang2019waiting` is genuinely a waiting-time repeater-chain paper (as your prose assumes), keeping it may be enough. citeturn22view0  
- If you want to add a second citation, choose one that clearly addresses **waiting times / memory effects in repeater chains**, not just “multi-path routing exists.”

## Structured introduction and contributions clarity

### C-035 Remove “Gap in Prior Work” heading

**What you have now.** The Introduction uses several explicit subsections (“Gap in Prior Work,” “Our Approach and Evaluation Scope,” “The Capacity Paradox,” “Key Contributions”). citeturn25view0turn25view1turn25view3  

**Does removing only this one heading make sense?** It can, but there’s a structural consistency issue:

- If the intent is to have a smooth narrative intro with minimal sub-structure, then removing “Gap in Prior Work” alone while leaving the other subsection headings may *increase* inconsistency. citeturn25view0turn25view3  
- If the intent is simply that “Gap in Prior Work” reads as a “speed bump,” then merging that content into the preceding paragraph is reasonable, but you should consider also whether the remaining subsections should become **paragraph-style signposts** rather than full \subsection blocks.

**Recommendation.**  
Either:
- keep the heading but adjust wording to flow (“Prior work limitations” / “Motivation and gaps”), or  
- convert the entire intro’s subheadings to a consistent paragraph-style scheme (e.g., \paragraph{Gap in prior work.} etc.) so you don’t “half-de-structure.” citeturn25view0turn25view3

---

### C-036 Move evaluation counts to Study Design or later

**What you have now.** You currently include “In total, we report about 7,890… across 835 unique…” within the Introduction’s scope paragraph. citeturn25view1  
You already have a dedicated **Study Design** section that explains the experimental setup and could naturally host this accounting. citeturn29view0turn29view2

**Does the proposed fix make sense?** Yes. This specific kind of “accounting line” generally reads better in Study Design / Experiment Design, where readers expect enumeration of runs/configs. Your Study Design section already talks about modular four-phase evaluation and provides an “Experimental Design” subsection; that’s the right place. citeturn29view0turn29view2

**Recommendation.**  
In the Introduction, keep only *coarse* breadth markers (models, threats, allocators, capacity semantics), and move the exact “7,890 / 835” line to Study Design. citeturn25view1turn29view2

---

### C-037 Rewrite the “Unified, reproducible benchmarking…” contributions bullet

**What you have now.** The first contributions bullet is readable but still dense: it enumerates EXP3-family adversarial baselines, CMAB/iCMAB, hybrids, and several citations in one sentence. citeturn25view1turn25view3  
Also, the citation key used in this bullet is `auer2002exp3`. citeturn25view3turn22view0

**Does your proposed rewrite make sense?** Yes: it will improve readability and reduce “citation dump” feeling, while keeping the same meaning. citeturn25view3

**One additional fit-to-paper check.**  
Your manuscript’s tracker text elsewhere already references `auer2002nonstochastic` as the EXP3 anchor in the “Foundational Bandits and Regret Regimes” audit section, meaning you may currently have **inconsistent citation keys** across the repo/manuscript. citeturn9view4  
So your instinct to normalize the EXP3 citation key is reasonable, but you should confirm which key exists in your actual `.bib` and standardize everywhere.

**Recommendation.**  
- Make the bullet shorter and put the “enabling fair comparisons” payoff at the end.  
- Standardize the EXP3 citation key and keep consistent across Intro + contributions + related work. citeturn25view3turn9view4

## Framework and cross-testbed clarity

### C-038 Explain (and align) the evaluation framework layers

**What you have now.** The paper contains a detailed TikZ “Modular framework” figure with six layers (Allocator → Configuration → Evaluator → Runner → Model → Visualizer) and short descriptor phrases, but there is not a matching textual explanation block that clearly states what each layer does and how they interact end-to-end. citeturn30view4turn30view5turn30view6

**Does your proposed “add 1–2 sentences per layer” fix make sense?** Yes, with a key refinement:

- Your diagram currently lists only a subset of algorithms inside the “Configuration” block (the hybrid set) even though the paper earlier states the scope is 16 models. citeturn30view4turn25view0turn25view1  
- A textual layer explanation should explicitly say the figure is an **architectural abstraction** and that the “Algorithms” list in the diagram is illustrative or corpus-specific (e.g., hybrid suite). Otherwise, a reviewer may think you only evaluate those 4 algorithms. citeturn30view4turn25view1

**Recommendation.**  
Implement a short textual “layers” paragraph/list that:
- mirrors the six layer names exactly as shown in the figure, and  
- clarifies the scope mismatch (diagram shows an example configuration; full corpora include 16 models and multiple horizons). citeturn30view4turn25view1turn30view0

---

### C-039 Cross-testbed validation — explain noise models/settings accurately

**What you have now (contributions bullet).** You describe external testbeds as spanning “diverse noise models (stochastic gate errors, fusion-based entanglement, context-driven dynamics).” citeturn25view1  
But that phrase is currently under-specified and arguably slightly mismatched to what at least one of the “Paper 7” sources actually does.

**What you have now (Cross-Testbed section).** You provide much more detail in the actual Cross-Testbed Validation section, including testbed sizes and the named noise model classes for Paper 2 and Paper 12. citeturn7view1turn7view2  
So, the core issue is not that you lack a section—rather, it’s that the **compressed description** in Key Contributions is too vague and may be slightly inaccurate.

**Deep check against the underlying sources.**

- Paper 2 (Chaudhary et al.) explicitly models probabilistic noises across fibers/memory/gates, and discusses decoherence and entanglement swapping under imperfect operations; it also explicitly mentions BSM and gate error probabilities (e.g., `pBSM = 0.2`, `pgate = 0.2`) and probability functions for fiber depolarization and memory dephasing. citeturn27view0turn21view1turn21view3  
- Paper 7 (QBGP) explicitly frames noise in terms of quantum noise channels; it introduces depolarizing channels and explains average fidelity under a depolarizing parameter, and it uses network benchmarking under a Markovian assumption to estimate channel/path fidelity. citeturn19view0turn19view1turn18view5  
  This is not best described as “context-driven external rewards”; it is more properly described as **(simplified) noise-channel modeling + benchmarking-driven fidelity estimation**.
- Paper 12 (QuARC) explicitly characterizes fusion success probabilities (e.g., n-fusion succeeds with probability \(q^n\)) and studies routing performance sensitivity to physical parameters like entanglement generation probability \(p\) and fusion probability \(q\). citeturn20view0turn20view7turn17view1  

**Does your proposed bullet-list expansion make sense?** Yes, and it’s easy to make it “fit-to-paper” by anchoring each bullet to what the original paper emphasizes:
- Chaudhary: probabilistic noise across fiber/memory/gates + decoherence during swapping. citeturn27view0turn21view1  
- QBGP: depolarizing channel model + benchmarking to estimate fidelity. citeturn19view0turn19view1  
- QuARC: fusion-based routing + explicit fusion probability \(q\) and sensitivity to physical parameters \(p, q\). citeturn20view0turn20view7turn17view1  

**Recommendation.**  
- Upgrade the Key Contributions “diverse noise models” parenthetical to match the underlying papers.  
- Keep the Cross-Testbed section as the authoritative detail level; add 1–2 clarifying phrases (not necessarily full bullets) if you want consistency between the contributions bullet and the section. citeturn25view1turn7view1turn7view2

## Missing or adjacent items you should flag while implementing C-031 to C-039

These are not “new tasks,” but they are tightly coupled to C-031…C-039 and will prevent rework:

- **Abstract duplication and inline author note must be removed** when you finalize C-032; otherwise you risk accidentally compiling the wrong draft or leaking internal comments. citeturn26view0  
- **Scope-number consistency**: the Introduction says 16 models and 7,890/835 totals, while the abstract cites 13 algorithms and 552 configs. Either reconcile the story (“curated corpora” vs “full portfolio”) or reduce numeric specificity in the abstract. citeturn25view1turn26view0  
- **Framework figure vs stated scope**: the framework diagram’s “Algorithms” list appears to reflect only the hybrid subset, while your narrative scope includes multiple families. If C-038 adds text, it should explicitly prevent confusion here. citeturn30view4turn25view1  
- **Paper 7 noise-model wording** in the Key Contributions bullet should be corrected to align with QBGP’s modeling/benchmarking framing, because “context-driven dynamics” can read like a completely different simulator assumption than what the cited paper describes. citeturn25view1turn19view0turn18view5