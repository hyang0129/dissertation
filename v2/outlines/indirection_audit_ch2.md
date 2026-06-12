# Indirection Audit — Chapter 2 (Background and Definitions)

Scope: connective prose only. Definition, Method, and Theorem bodies are load-bearing
and are excluded. 14 instances found.

---

## Instance #1
**Pattern:** 1.4 — Redundant elaboration  
**Section:** Chapter opening paragraph  
**Context:**
```
Second, this chapter \emph{defines} each primitive, while
\Cref{ch:literature-review} surveys how the field has used it. This chapter defines
the vocabulary; the literature review then situates it and the results chapters
deploy it. The chapter follows that plan.
```
**Original phrase:** `This chapter defines the vocabulary; the literature review then situates it and the results chapters deploy it. The chapter follows that plan.`  
**Proposed replacement:** *(delete both sentences; the \Cref roadmap that follows states the plan directly)*

---

## Instance #2
**Pattern:** 1.7 — Weak relational verb  
**Section:** §2.1 Out-of-Distribution Detection (closing sentence)  
**Context:**
```
This task is the setting for \Cref{ch:label-blindness,ch:domain-sensitivity-collapse}.
```
**Original phrase:** `This task is the setting for`  
**Proposed replacement:** `\Cref{ch:label-blindness,ch:domain-sensitivity-collapse} both work in this setting.`

---

## Instance #3
**Pattern:** 1.7 — Weak relational verb  
**Section:** §2.2 Anomaly Detection (opening sentence)  
**Context:**
```
Anomaly detection is adjacent to OOD detection and the two are often conflated, but
they differ in scope and training assumptions, and so in how they are evaluated.
```
**Original phrase:** `Anomaly detection is adjacent to OOD detection and the two are often conflated`  
**Proposed replacement:** `Anomaly detection and OOD detection are often conflated but differ in scope, training assumptions, and evaluation.`

---

## Instance #4
**Pattern:** 1.7 — Weak relational verb  
**Section:** §2.4 Dataset Domain (opening)  
**Context:**
```
This dissertation is concerned with the case in which all training classes share one
domain $\rvd_1$, so that $f_{\rvd}(\rvx) = \rvd_1$ for every in-distribution
$\rvx$;
```
**Original phrase:** `This dissertation is concerned with the case in which`  
**Proposed replacement:** `This dissertation studies the case where` (rest of sentence unchanged)

---

## Instance #5
**Pattern:** 1.3 — Noun clause for noun phrase  
**Section:** §2.4 Dataset Domain (DSC forward-pointer)  
**Context:**
```
That phenomenon is \emph{Domain-Sensitivity Collapse}. It, and what it does to
distance-based detection, is the contribution of \Cref{ch:domain-sensitivity-collapse}
and is not treated as a background primitive here;
```
**Original phrase:** `It, and what it does to distance-based detection, is the contribution of \Cref{ch:domain-sensitivity-collapse} and is not treated as a background primitive here`  
**Proposed replacement:** `Domain-Sensitivity Collapse and its effect on distance-based detection form the contribution of \Cref{ch:domain-sensitivity-collapse} and are not treated as background primitives here`

---

## Instance #6
**Pattern:** 1.2 — Trailing coordination clause  
**Section:** §2.5 Large Language Models (residual stream paragraph)  
**Context:**
```
These activations are computed in a single forward pass and require no resampling,
and they are the raw material an internal-state detector scores.
```
**Original phrase:** `and they are the raw material an internal-state detector scores`  
**Proposed replacement:** `These activations are computed in a single forward pass, require no resampling, and form the raw material an internal-state detector scores.`

---

## Instance #7
**Pattern:** 1.3 — Noun clause for noun phrase  
**Section:** §2.6 Information Theory (section opener)  
**Context:**
```
Information theory~\citep{shannon1948mathematical} quantifies uncertainty and the
dependence between random variables, and supplies the first of the dissertation's
two lenses: a formal way to measure how much of a target a representation has kept.
```
**Original phrase:** `a formal way to measure how much of a target a representation has kept`  
**Proposed replacement:** `a formal measure of how much information a representation retains about a target`

---

## Instance #8
**Pattern:** 1.1 — Setup clause opener  
**Section:** §2.6 Information Theory (DPI lead-in)  
**Context:**
```
One consequence matters for the language-domain chapter: information cannot be
created by processing a variable.
```
**Original phrase:** `One consequence matters for the language-domain chapter:`  
**Proposed replacement:** `Information cannot be created by processing a variable—the constraint that makes the language-domain analysis tractable.` *(delete the original sentence; replace with this)*

---

## Instance #9
**Pattern:** 1.1 — Setup clause / pseudo-cleft  
**Section:** §2.6 Information Theory (DPI bridge sentence)  
**Context:**
```
The data processing inequality is what makes cross-layer mutual information
analysable in \Cref{ch:hallucination-detection}: because later activations are
deterministic functions of earlier ones, mutual information measured between learned
embeddings lower-bounds the mutual information between the underlying layer
activations, so a positive measured value certifies a positive true value
```
**Original phrase:** `The data processing inequality is what makes cross-layer mutual information analysable`  
**Proposed replacement:** `The data processing inequality enables cross-layer mutual information analysis` (rest of sentence unchanged)

---

## Instance #10
**Pattern:** 1.3 — Noun clause for noun phrase  
**Section:** §2.7 Information Bottleneck (section opener)  
**Context:**
```
The information-theoretic view becomes a tool for representation learning through
sufficiency and the information bottleneck, and it becomes \emph{operational}
through the contrastive bound that lets mutual information be estimated and
optimized.
```
**Original phrase:** `the contrastive bound that lets mutual information be estimated and optimized`  
**Proposed replacement:** `a contrastive bound for estimating and optimizing mutual information`

---

## Instance #11
**Pattern:** 1.2 — Trailing relative clause  
**Section:** §2.7 Information Bottleneck (sufficiency bridge)  
**Context:**
```
The same machinery is constructive in the language domain, but there mutual
information must be \emph{estimated} from samples, which the contrastive objective
makes possible.
```
**Original phrase:** `The same machinery is constructive in the language domain, but there mutual information must be \emph{estimated} from samples, which the contrastive objective makes possible.`  
**Proposed replacement:** `The same machinery applies in the language domain, but there mutual information must be \emph{estimated} from samples; the contrastive objective provides this.`

---

## Instance #12
**Pattern:** 1.6 — Expletive "This is a X"  
**Section:** §2.7 Information Bottleneck (InfoNCE closing)  
**Context:**
```
\Cref{ch:hallucination-detection} reads the bound in the contrapositive: a
contrastive loss that \emph{descends} below $\log K$ on a held-out split is itself
evidence that the mutual information it estimates is strictly above zero. This is a
feasibility argument, whose formal version, with supervised contrast over layer-pair
views, is developed there and proved in \Cref{app:mi-hallucination-proofs}.
```
**Original phrase:** `This is a feasibility argument, whose formal version, with supervised contrast over layer-pair views, is developed there and proved in \Cref{app:mi-hallucination-proofs}.`  
**Proposed replacement:** `This feasibility argument is formalized with supervised contrast over layer-pair views in \Cref{ch:hallucination-detection} and proved in \Cref{app:mi-hallucination-proofs}.`

---

## Instance #13
**Pattern:** 1.7 — Weak relational verb  
**Section:** §2.8 Representation Geometry (detection score bridge)  
**Context:**
```
This geometry determines how detection scores behave. \emph{Distance-based} scores,
nearest-neighbour distance~\citep{sun2022out} and the Mahalanobis
score~\citep{lee2018simple}, weight directions by Euclidean coordinate differences,
```
**Original phrase:** `This geometry determines how detection scores behave.`  
**Proposed replacement:** `This geometry governs detection scores directly.`

---

## Instance #14
**Pattern:** 1.7 — Weak relational verb  
**Section:** §2.8 Representation Geometry (chapter closing)  
**Context:**
```
These geometric primitives, together with the
information-theoretic ones of \Cref{sec:bg:infotheory,sec:bg:ib}, are the two lenses
the remainder of the dissertation applies: \Cref{ch:literature-review} surveys their
use across vision OOD and language hallucination, and
\Cref{ch:label-blindness,ch:domain-sensitivity-collapse,ch:hallucination-detection}
deploy them.
```
**Original phrase:** `These geometric primitives, together with the information-theoretic ones of \Cref{sec:bg:infotheory,sec:bg:ib}, are the two lenses the remainder of the dissertation applies:`  
**Proposed replacement:** `The remainder of the dissertation applies these two lenses---geometric and information-theoretic:`

---

## Summary

| Section | Count |
|---------|-------|
| Chapter opening | 1 |
| §2.1 OOD Detection | 1 |
| §2.2 Anomaly Detection | 1 |
| §2.3 Unlabeled OOD | 0 |
| §2.4 Domain | 2 |
| §2.5 LLMs & Hallucination | 1 |
| §2.6 Information Theory | 3 |
| §2.7 IB / Contrastive | 3 |
| §2.8 Geometry | 2 |
| **Total** | **14** |
