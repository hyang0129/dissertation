# Indirection Audit — Ch.1 Introduction (`01_introduction.tex`)

---

## 1.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** A machine learning model trained only on chest X-rays is shown a brain MRI. Nothing in its training prepared it for a different imaging modality, yet it does not hesitate: it returns a confident class label, as though the scan were one more X-ray. A large language model is asked for the source of a quotation it has never seen, and it supplies one anyway: an author, a year, a journal, all fluent, specific, and entirely invented. Both systems fail in the same way. Each has met an input, or produced an output, that lies outside what it can be trusted to handle, and neither can tell. What is missing in both cases is not accuracy but self-knowledge: the ability to recognize the boundary of one's own competence.

**Original:** `that lies outside what it can be trusted to handle`

**Proposed:** `that lies outside its competence`

---

## 2.

**Pattern:** 1.6 Expletive opener

**Context:** *(same paragraph as 1)*

**Original:** `What is missing in both cases is not accuracy but self-knowledge…`

**Proposed:** `Both cases lack not accuracy but self-knowledge…`

---

## 3.

**Pattern:** 1.7 Weak relational verb

**Context:** This dissertation studies that capability through two detection problems. Out-of-distribution (OOD) detection flags an input unlike the training data, and hallucination detection flags a generation not supported by fact. The literature treats them as separate problems with separate machinery, but we argue they turn on the same thing. A shift is detectable exactly when the model's learned representation still holds the structure that distinguishes it.

**Original:** `but we argue they turn on the same thing`

**Proposed:** `but both turn on the same thing`

---

## 4.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** *(same paragraph as 3)*

**Original:** `A shift is detectable exactly when the model's learned representation still holds the structure that distinguishes it.`

**Proposed:** `A shift is detectable exactly when the model's learned representation still encodes the distinguishing structure.`

---

## 5.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** We read the condition through two lenses. Information theory casts what a representation holds as mutual information, the amount its features still say about the distinction at issue. Representation geometry casts the same thing as structure in feature space: which directions carry variance, and which have flattened out. The two name one quantity. Three studies put the condition to work along one arc, from failure to recovery to detection. The rest of this chapter states the problem each study takes on, lists the contributions, sets out the method that ties them together, and maps the document.

**Original:** `the amount its features still say about the distinction at issue`

**Proposed:** `the amount its features still encode about the relevant distinction`

---

## 6.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 5)*

**Original:** `which have flattened out`

**Proposed:** `which have collapsed`

---

## 7.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 5)*

**Original:** `The rest of this chapter states the problem each study takes on, lists the contributions, sets out the method that ties them together, and maps the document.`

**Proposed:** Delete.

---

## 8.

**Pattern:** 1.1 Setup clause opener / 1.7 Weak relational verb

**Context:** A deployed model earns trust only when it can tell that an input, or an output, has left the territory it was trained on. Supervised learning tunes prediction inside the training distribution. It teaches a model nothing, on its own, about where that distribution stops. Deployment in the open world breaks the closed-set assumption as a matter of course, and that gap is the central obstacle to safe deployment. The X-ray model and the fabricating language model from the opening are not exotic failures. They are what a confident model does once it is pushed past its training experience.

**Original:** `A deployed model earns trust only when it can tell that an input, or an output, has left the territory it was trained on.`

**Proposed:** `A deployed model is trustworthy only when it detects inputs and outputs outside its training territory.`

---

## 9.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 8)*

**Original:** `Supervised learning tunes prediction inside the training distribution. It teaches a model nothing, on its own, about where that distribution stops.`

**Proposed:** `Supervised learning tunes prediction inside the training distribution and tells a model nothing about where that distribution stops.`

---

## 10.

**Pattern:** 1.2 Trailing participial

**Context:** *(same paragraph as 8)*

**Original:** `Deployment in the open world breaks the closed-set assumption as a matter of course, and that gap is the central obstacle to safe deployment.`

**Proposed:** `Deployment in the open world breaks the closed-set assumption; that gap blocks safe deployment.`

---

## 11.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** We take up this gap in three settings. Each asks the same question, whether the representation still encodes the relevant structure, and each answers differently, because the structure survives to a different degree.

**Original:** `Each asks the same question, whether the representation still encodes the relevant structure, and each answers differently, because the structure survives to a different degree.`

**Proposed:** `Each asks whether the representation still encodes the relevant structure, and each answers differently because the structure survives to a different degree.`

---

## 12.

**Pattern:** 1.1 Setup clause opener

**Context:** A recent line of work tries to flag distributional shift without labels, training on self- or unsupervised objectives that need no annotation. When the objective ignores label-relevant features, the representation encodes no label distinction and detection fails. We name this failure mode label blindness. It bites hardest exactly where safety is at stake: once OOD inputs overlap in-distribution data in feature space, unlabeled detection fails exactly where deployment demands it.

**Original:** `A recent line of work tries to flag distributional shift without labels, training on self- or unsupervised objectives that need no annotation.`

**Proposed:** `Unlabeled methods train on self- or unsupervised objectives; when those objectives ignore label-relevant features, the representation encodes no label distinction and detection fails.`

---

## 13.

**Pattern:** 1.5 Passive with hidden agent (pronoun subject)

**Context:** *(same paragraph as 12)*

**Original:** `It bites hardest exactly where safety is at stake`

**Proposed:** `Label blindness bites hardest where safety is at stake`

---

## 14.

**Pattern:** 1.1 Setup clause opener

**Context:** *(same paragraph as 12)*

**Original:** `once OOD inputs overlap in-distribution data in feature space`

**Proposed:** `when OOD inputs overlap in-distribution data in feature space`

---

## 15.

**Pattern:** 1.4 Redundant elaboration

**Context:** Many real systems train on a single narrow domain, one imaging modality or one sensor or one institution's records. Here supervised training compresses the representation into a class-aligned, low-rank subspace and erases the domain-shift directions. Training contained the signal; the optimizer discarded it. Distance- and logit-based detectors are then blind to the very shifts they should catch. This is not the fundamental impossibility of label blindness. The failure is induced by how the model was trained, and a change to training can put back what training removed.

**Original:** `This is not the fundamental impossibility of label blindness.`

**Proposed:** Absorb as a dash clause into the preceding sentence: `Distance- and logit-based detectors are then blind to the very shifts they should catch — not the fundamental impossibility of label blindness, but an induced failure.`

---

## 16.

**Pattern:** 1.5 Passive with hidden agent

**Context:** *(same paragraph as 15)*

**Original:** `The failure is induced by how the model was trained, and a change to training can put back what training removed.`

**Proposed:** `Training induces the failure, and retraining can restore the lost directions.`

---

## 17.

**Pattern:** 1.7 Weak relational verb

**Context:** Large language models routinely produce fluent text with no basis in fact. Most detectors lean on repeated sampling or outside verification, and the field has lacked any principled account of why a hallucination signal should exist at all, let alone where to find it. We show the signal sits in the model's own intermediate activations, and that an information-theoretic argument says it can be pulled out directly. Catching a hallucination then comes down to reading the representation, not stumbling onto an engineering trick.

**Original:** `Most detectors lean on repeated sampling or outside verification, and the field has lacked any principled account of why a hallucination signal should exist at all, let alone where to find it.`

**Proposed:** `Most detectors rely on repeated sampling or outside verification; the field has no principled account of why a hallucination signal exists, let alone where it lives.`

---

## 18.

**Pattern:** 1.1 Setup clause opener / 1.7 Weak relational verb

**Context:** *(same paragraph as 17)*

**Original:** `We show the signal sits in the model's own intermediate activations, and that an information-theoretic argument says it can be pulled out directly.`

**Proposed:** `The signal sits in the model's own intermediate activations; an information-theoretic argument guarantees it can be extracted directly.`

---

## 19.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 17)*

**Original:** `Catching a hallucination then comes down to reading the representation, not stumbling onto an engineering trick.`

**Proposed:** `Hallucination detection requires reading the representation, not an engineering trick.`

---

## 20.

**Pattern:** 1.7 Weak relational verb

**Context:** This dissertation makes four contributions. Each is worked out in its own chapter and each is one instance of the condition above; Ch.7 draws them together.

**Original:** `This dissertation makes four contributions.`

**Proposed:** `This dissertation contributes four results.`

---

## 21.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 20)*

**Original:** `Each is worked out in its own chapter and each is one instance of the condition above; Ch.7 draws them together.`

**Proposed:** Delete the first two clauses; keep only `Ch.7 draws them together.`

---

## 22.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** We prove that an unlabeled detector cannot work in the worst case once its self- or unsupervised objective is independent of the label-relevant features: the representation the model settles on retains no trace of the label distinction, so OOD detection is guaranteed to fail. This is the dissertation's one genuine impossibility result. We show its triggering conditions arise in ordinary deployments, and we build the Adjacent OOD benchmark, which constructs the high feature overlap that exposes the failure, the very regime that standard near/far suites sidestep. Proofs appear in App. A.

**Original:** `the representation the model settles on retains no trace of the label distinction`

**Proposed:** `the representation retains no label-distinction structure`

---

## 23.

**Pattern:** 1.1 Setup clause opener

**Context:** *(same paragraph as 22)*

**Original:** `We show its triggering conditions arise in ordinary deployments`

**Proposed:** `Its triggering conditions arise in ordinary deployments`

---

## 24.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** *(same paragraph as 22)*

**Original:** `which constructs the high feature overlap that exposes the failure, the very regime that standard near/far suites sidestep`

**Proposed:** `which constructs high feature-overlap settings — the regime standard near/far suites sidestep`

---

## 25.

**Pattern:** 1.1 Setup clause opener / 1.2 Trailing participial

**Context:** We identify and formalize domain-sensitivity collapse (DSC): training a supervised model on one domain flattens the domain-shift directions. The account is geometric, and its bounds are diagnostic rather than impossibility guarantees, predicting where distance- and logit-based scorers go numb. We then introduce Teacher-Guided Training (TGT), a training-time auxiliary objective that distills a frozen multi-domain teacher to restore the lost geometry, at no inference cost. Proofs appear in App. B.

**Original:** `The account is geometric, and its bounds are diagnostic rather than impossibility guarantees, predicting where distance- and logit-based scorers go numb.`

**Proposed:** `Geometric bounds predict where distance- and logit-based scorers go blind, and those bounds are diagnostic, not impossibility guarantees.`

---

## 26.

**Pattern:** 1.2 Trailing participial

**Context:** *(same paragraph as 25)*

**Original:** `a training-time auxiliary objective that distills a frozen multi-domain teacher to restore the lost geometry, at no inference cost`

**Proposed:** `a training-time auxiliary objective that distills a frozen multi-domain teacher, restoring the lost geometry at no inference cost`

---

## 27.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** We give a feasibility-by-trainability argument. Cross-layer mutual information in the residual stream is positive by construction, so a contrastive objective can drop below its information floor only if the signal is there. On that footing we build a one-class contrastive probe over pairs of cross-layer activations. The detector matches-or-outperforms, in the mean, the strongest engineered probe. A correct principle predicts exactly this parity, not a leaderboard win. The theory also makes a falsifiable prediction, that symmetric supervision should fail, and an ablation bears it out. Proofs appear in App. C.

**Original:** `so a contrastive objective can drop below its information floor only if the signal is there.`

**Proposed:** `…only when a hallucination signal is present.`

---

## 28.

**Pattern:** 1.1 Setup clause opener

**Context:** *(same paragraph as 27)*

**Original:** `On that footing we build a one-class contrastive probe over pairs of cross-layer activations.`

**Proposed:** `We build a one-class contrastive probe over pairs of cross-layer activations.`

---

## 29.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 27)*

**Original:** `A correct principle predicts exactly this parity, not a leaderboard win.`

**Proposed:** Delete, or compress to `Parity is what the theory predicts.`

---

## 30.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** *(same paragraph as 27)*

**Original:** `that symmetric supervision should fail`

**Proposed:** `that symmetric supervision fails`

---

## 31.

**Pattern:** 1.7 Weak relational verb

**Context:** One idea runs under all three studies: reliability turns on what the representation preserves, and information theory and geometry are two ways to measure it. This framework, not any one result, is the dissertation's main contribution.

**Original:** `One idea runs under all three studies: reliability turns on what the representation preserves`

**Proposed:** `One idea governs all three studies: reliability depends on the preserved structure.`

---

## 32.

**Pattern:** 1.6 Expletive opener / 1.7 Weak relational verb

**Context:** The method is to put one question to every problem: what does the learned representation preserve? We treat reliability as a property of the representation itself, not of a score bolted onto a finished model. The thing that matters is whether the representation still carries what distinguishes the shift. Keeping to that one question is how three unrelated-looking problems become one.

**Original:** `The thing that matters is whether the representation still carries what distinguishes the shift.`

**Proposed:** `The representation must encode the distinguishing structure.`

---

## 33.

**Pattern:** 1.1 Setup clause opener

**Context:** *(same paragraph as 32)*

**Original:** `Keeping to that one question is how three unrelated-looking problems become one.`

**Proposed:** `That one question unifies three problems that would otherwise look unrelated.`

---

## 34.

**Pattern:** 1.5 Passive / 1.7 Weak relational verb

**Context:** We gauge the preserved structure in two ways and take whichever is clearer. The first is information-theoretic: the signal is the mutual information between the representation and the label-relevant features, and the data-processing inequality governs whether that information can survive a learned map. This view carries the impossibility result of Ch.4 and the feasibility argument of Ch.6. The second is geometric: the same structure appears as variance along particular directions, and as the rank and orientation of the class and shift subspaces, and its loss appears as collapse. This view carries the diagnosis and recovery of Ch.5. The two views land on one thing, since the information a representation throws away is the same as the set of directions it flattens. Ch.2 defines the primitives both need.

**Original:** `the signal is the mutual information between the representation and the label-relevant features`

**Proposed:** `mutual information between the representation and the label-relevant features measures the signal`

---

## 35.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** *(same paragraph as 34)*

**Original:** `whether that information can survive a learned map`

**Proposed:** `whether that information survives the learned map`

---

## 36.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 34)*

**Original:** `This view carries the impossibility result…and the feasibility argument`

**Proposed:** `This view grounds the impossibility result…and the feasibility argument`

---

## 37.

**Pattern:** 1.3 Noun clause for noun phrase

**Context:** *(same paragraph as 34)*

**Original:** `since the information a representation throws away is the same as the set of directions it flattens`

**Proposed:** `since discarded information and collapsed directions are the same thing`

---

## 38.

**Pattern:** 1.7 Weak relational verb

**Context:** Theory and experiment run together in every study, and every study is careful about its reach. We assert impossibility only where we prove it (Ch.4). We give the bounds of Ch.5 as diagnostic, not as guarantees. We report the detector of Ch.6 as reaching parity with the strongest baseline, losses shown and not buried. The dissertation pins down the conditions under which detection can work, and demonstrates principled methods operating at that boundary. It stops short of claiming they are the best possible.

**Original:** `Theory and experiment run together in every study, and every study is careful about its reach.`

**Proposed:** `Every study pairs theory with experiment and respects its own reach.`

---

## 39.

**Pattern:** 1.2 Trailing participial / 1.7 Weak relational verb

**Context:** *(same paragraph as 38)*

**Original:** `The dissertation pins down the conditions under which detection can work, and demonstrates principled methods operating at that boundary.`

**Proposed:** `The dissertation identifies the conditions under which detection works and demonstrates principled methods at that boundary.`

---

## 40.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 38)*

**Original:** `It stops short of claiming they are the best possible.`

**Proposed:** Delete.

---

## 41.

**Pattern:** 1.6 Expletive opener

**Context:** The dissertation is laid out as follows. Ch.2 defines the lens-neutral primitives the results chapters share. Ch.3 sets the three studies against prior work, organized by the same two lenses so the review reads as one argument and not three.

**Original:** `The dissertation is laid out as follows.`

**Proposed:** Delete.

---

## 42.

**Pattern:** 1.2 Trailing participial / 1.7 Weak relational verb

**Context:** *(same paragraph as 41)*

**Original:** `Ch.2 fixes the lens-neutral primitives the results chapters reuse, supplying both the information-theoretic and the geometric vocabulary the title promises.`

**Proposed:** `Ch.2 defines the lens-neutral primitives the results chapters share — the information-theoretic and geometric vocabulary the title promises.`

---

## 43.

**Pattern:** 1.2 Trailing participial

**Context:** *(same paragraph as 41)*

**Original:** `Ch.3 sets the three studies against prior work, organized by the same two lenses so the review reads as one argument and not three.`

**Proposed:** `Ch.3 positions the three studies against prior work through the same two lenses, so the review forms one argument.`

---

## 44.

**Pattern:** 1.4 Redundant elaboration

**Context:** The three results chapters then walk the arc of the figure. Ch.4 proves the label blindness theorem and introduces the Adjacent OOD benchmark, pinning down the regime where unlabeled detection cannot work. Ch.5 diagnoses domain-sensitivity collapse in single-domain models and offers Teacher-Guided Training as the recovery. Ch.6 derives the information-theoretic hallucination detector and tests it. Ch.7 pulls the three together under the representation-structure framework, sets out the dissertation's limitations, and names the open directions.

**Original:** `The three results chapters then walk the arc of the figure.`

**Proposed:** Delete.

---

## 45.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 44)*

**Original:** `Ch.7 pulls the three together under the representation-structure framework, sets out the dissertation's limitations, and names the open directions.`

**Proposed:** `Ch.7 unifies the three studies, states the limitations, and identifies the open directions.`

---

## 46.

**Pattern:** 1.1 Setup clause opener

**Context:** This work matters in two ways, one foundational and one practical. The foundational claim is that one condition, whether the representation preserves the distinguishing structure, sits under reliability across settings as far apart as detecting an out-of-distribution image and catching a language model's hallucination, and that information theory and geometry are two readings of that one condition. A benchmark cannot tell you whether a whole class of methods can work; it only scores the methods you happen to run. The label blindness theorem tells a practitioner what not to trust, and the feasibility argument tells them where a signal has to be.

**Original:** `This work matters in two ways, one foundational and one practical.`

**Proposed:** `This work contributes on two levels, foundational and practical.`

---

## 47.

**Pattern:** 1.1 Setup clause opener / 1.3 Noun clause

**Context:** *(same paragraph as 46)*

**Original:** `The foundational claim is that one condition, whether the representation preserves the distinguishing structure, sits under reliability across settings as far apart as detecting an out-of-distribution image and catching a language model's hallucination`

**Proposed:** `One condition governs reliability from OOD image detection to hallucination catching`

---

## 48.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 46)*

**Original:** `A benchmark cannot tell you whether a whole class of methods can work; it only scores the methods you happen to run.`

**Proposed:** `A benchmark scores only the methods it runs; it cannot determine whether a whole class of methods can work.`

---

## 49.

**Pattern:** 1.3 Noun clause / 1.7 Weak relational verb

**Context:** *(same paragraph as 46)*

**Original:** `The label blindness theorem tells a practitioner what not to trust, and the feasibility argument tells them where a signal has to be.`

**Proposed:** `The label blindness theorem tells a practitioner which regimes to avoid; the feasibility argument identifies where the signal must exist.`

---

## 50.

**Pattern:** 1.1 Setup clause opener

**Context:** The practical payoff is that each study yields concrete guidance for deployment. The label blindness result and the Adjacent OOD benchmark warn against unlabeled detection in the feature-overlap regimes safety-critical systems actually meet. The domain-sensitivity collapse diagnosis, and its no-overhead fix, bear directly on the narrow-domain models common in medical imaging and remote sensing. The hallucination detector gives a single-pass way to flag unsupported generation wherever factual accuracy is the point. Read together, the three studies hand AI safety a complement to benchmarking: a principled account of when reliability is within reach at all. Ch.7 returns to the point once the evidence is in.

**Original:** `The practical payoff is that each study yields concrete guidance for deployment.`

**Proposed:** `Each study yields concrete guidance for deployment.`

---

## 51.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 50)*

**Original:** `The hallucination detector gives a single-pass way to flag unsupported generation wherever factual accuracy is the point.`

**Proposed:** `The hallucination detector flags unsupported generation in a single pass, wherever factual accuracy matters.`

---

## 52.

**Pattern:** 1.7 Weak relational verb

**Context:** *(same paragraph as 50)*

**Original:** `Read together, the three studies hand AI safety a complement to benchmarking: a principled account of when reliability is within reach at all.`

**Proposed:** `Read together, the three studies give AI safety a principled account of when reliability is achievable — a complement to benchmarking.`

---

## 53.

**Pattern:** 1.4 Redundant elaboration

**Context:** *(same paragraph as 50)*

**Original:** `Ch.7 returns to the point once the evidence is in.`

**Proposed:** Delete.

---

## Summary

| Pattern | Count |
|---|---|
| 1.1 Setup clause opener | 12 |
| 1.2 Trailing participial | 8 |
| 1.3 Noun clause for noun phrase | 12 |
| 1.4 Redundant elaboration | 13 |
| 1.5 Passive with hidden agent | 4 |
| 1.6 Expletive opener | 3 |
| 1.7 Weak relational verb | 18 |

Many instances carry two patterns. **1.7 (weak relational verbs)** and **1.4 (redundant elaboration)** are the dominant problems. The most impactful single changes are the deletions (7, 21, 40, 41, 44, 53) and the collapses of double-announcement frames (18, 23, 28).
