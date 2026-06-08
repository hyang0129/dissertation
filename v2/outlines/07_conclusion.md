# Chapter 7 — Conclusion · drafting plan (Option B, synthesis-led)

Plan for writing Ch.7, the dissertation's closing chapter. Companion to
[00_dissertation_outline.md](00_dissertation_outline.md) (Ch.7 entry, lines
278–288; spine §40–70). Source to de-proposalize:
[v1 §8 Conclusion](../../v1/Sample_Thesis_main.tex#L1412-L1490).

**Status:** ⬜ not yet drafted (`chapters/07_conclusion.tex` is a stub). No number
gate, no foreign data, no proofs — this is the one results-free chapter. The work
is **framing**, not content: synthesize what Ch.4–6 already established.

**Not a port — a rebuild.** Unlike Ch.4 (faithful port) the v1 conclusion cannot
be lifted. It is written in proposal voice ("this dissertation proposal has
outlined," "the proposed work aims to," "success will be measured through peer
review") **and** it describes the superseded science (Domain *Feature* Collapse,
the two-stage *domain-filtering* solution). Both the voice and the substance are
stale. Treat v1 §8 as a section checklist, not a prose base.

## Structural decision (2026-06-08): Option B, synthesis-led

Chosen over Option A (recapitulative, chapter-by-chapter — wastes the one place the
three papers get argued as one thesis) and Option C (forward-led — under-claims a
real impossibility theorem + two real methods). **Lengthening is acceptable** (user
approved): the synthesis subsection in 7.1 is the payoff, not padding.

The job a stapler/three-paper dissertation conclusion must do that the individual
papers cannot: **argue the connective tissue.** Each of Ch.4/5/6 already has its own
conclusion; Ch.7 earns its place only by showing the three are *one* question asked
of three representations.

---

## Framing locks (carry from master outline — do NOT re-litigate here)

These are the cross-section consistency rules. The conclusion is the highest-risk
place to violate them (temptation to inflate on the way out the door):

- **Spine = representation structure**, *both* lenses. Lead with "what the
  representation preserves," info theory (Ch.4, Ch.6) **and** geometry (Ch.5) as its
  two tools — never an info-theory-only umbrella (2026-06-04 decision).
- **Arc = failure → recovery → detection.** Ch.4 proves the representation *cannot*
  support detection; Ch.5 *restores* the missing structure; Ch.6 *detects* from the
  structure left behind.
- **"Guaranteed failure" is Ch.4-only.** The Label Blindness theorem is the one
  genuine impossibility result. Do not generalize the verb to Ch.5/6.
- **Ch.5 is diagnostic, not impossibility.** DSC bounds are *diagnostic upper
  bounds, explicitly not guarantees*; the chapter's claim is diagnosis + recovery
  (TGT), not a no-go theorem.
- **Ch.6 verb is locked: "matches-or-outperforms (in the mean)."** Parity-from-an-
  information-theoretic-first-principle (parity = evidence the lens is right), never
  "beats" / "state-of-the-art." The two NQ losses are acknowledged, not hidden.
- **No new claims, no new results, no re-derivations** in the conclusion. Synthesize
  only what Ch.4–6 proved.

## Hard deletes from v1 §8 (proposal artifacts)

- ❌ **§ Research Timeline and Feasibility** (v1 L1466–1472) — Gantt/12-month plan.
- ❌ **§ Expected Outcomes and Success Metrics** (v1 L1474–1480) — "success measured
  by peer review / benchmark wins." Gone entirely.
- ✏️ Every "propose / will / aims to" → "present / show / establish." Drop "Proposed"
  from the contributions heading.
- ✏️ Purge superseded science: "domain feature collapse" → DSC; delete "domain
  filtering framework / two-stage detector" → TGT. v1's hallucination paragraphs are
  proposal-era ("insufficient MI between query and response") — rewrite to the real
  Ch.6 mechanism (cross-layer MI, one-class layer-pair contrastive probe).

---

## Section map

### 7.0 Opening (unnumbered lead-in, ~2 short paragraphs)
- **Do not open with a recap.** Open with the thesis statement restated at full
  strength: detection is possible exactly when the learned representation preserves
  the structure that distinguishes the shift — and the dissertation ran that lens
  across three reliability settings.
- Name the arc (failure → recovery → detection) in one sentence so the reader has
  the frame before the contribution summary.

### 7.1 Summary of Contributions *(drop "Proposed")*
Three tight per-pillar paragraphs **+ a synthesis subsection** (the Option-B payoff).

- **7.1.1 Per-pillar contributions** (one paragraph each, accomplished voice):
  - *Ch.4 — Label Blindness.* The genuine impossibility result: when the
    self-/unsupervised surrogate is independent of label-relevant features, unlabeled
    OOD detection is *guaranteed* to fail. Adjacent OOD as the evaluation paradigm
    that exposes it. (Peer-reviewed, ICLR 2025 — may note as completed/validated.)
  - *Ch.5 — DSC / TGT.* The diagnostic geometric account: single-domain supervised
    training drives features into a low-rank class subspace, suppressing
    domain-shift directions, so distance/logit scorers lose sensitivity. TGT
    recovers the lost sensitivity by distilling a frozen multi-domain teacher, with
    no inference overhead. Keep "diagnostic, not guarantee."
  - *Ch.6 — MI Hallucination Detection.* The detection result: hallucination is
    detectable from intermediate-layer activations via a one-class contrastive probe
    over cross-layer pairs, motivated by a feasibility-by-trainability argument.
    Reaches **parity** with the best engineered probe — parity as evidence the lens
    is right. Locked verb. Note the confirmed symmetric-SupCon falsifiable prediction
    as the strongest empirical-of-theory moment.
- **7.1.2 Synthesis — the three as one thesis** *(the chapter's reason to exist)*:
  - Thread the arc explicitly: Ch.4 marks the boundary where structure is absent,
    Ch.5 restores structure that training destroyed, Ch.6 reads structure the model
    already preserves. Same question — *does the representation preserve what
    distinguishes the shift?* — three answers.
  - Make the **two-lens** point concretely: info theory and geometry are not two
    topics but two instruments measuring the same thing (what is preserved). Ch.4/6
    measure it as mutual information; Ch.5 measures it as subspace geometry; the DPI
    and the variance-suppression argument are duals in spirit.

### 7.2 Broader Implications
Reframe v1's three subsections under the representation-structure umbrella (not
info-theory-only). Keep these genuinely *broader* than the chapter discussions.
- **7.2.1 AI safety & reliability** — principled failure detection vs. empirical
  patching; knowing *when* a method is guaranteed to fail (Ch.4) is itself a safety
  contribution. Relevance to narrow-domain deployment (Ch.5) and LLM factuality
  (Ch.6).
- **7.2.2 Information theory & representation geometry in ML** — the methodological
  claim: asking "what does the representation preserve" is portable across tasks and
  architectures; both lenses belong in the reliability toolkit.
- **7.2.3 Evaluation & benchmarking** — Adjacent OOD (Ch.4) and single-domain
  evaluation (Ch.5) as the lesson that benchmarks should target *theoretically
  predicted* failure modes, not just empirically convenient ones.

### 7.3 Limitations *(standalone section — decided 2026-06-08)*
Consolidated, **honest** limitations across the three pillars. Pre-stating these
defuses defense questions (committee: Desell / Ororbia / KhudaBukhsh / Yu) and buys
credibility; it also sets up 7.4 (future work addresses these). One short paragraph
per pillar + a synthesis note.
- *Ch.4.* The Label Blindness condition is an **idealization** — strict statistical
  independence between surrogate and label-relevant features. Real SSL objectives are
  partially aligned, so the theorem bounds a worst case rather than predicting exact
  field performance. Adjacent OOD is one constructed regime, not the whole shift space.
- *Ch.5.* DSC bounds are **diagnostic, not guarantees** (do not let the limitations
  section accidentally re-cast them as a no-go theorem). TGT depends on a frozen
  multi-domain teacher whose coverage caps the recoverable geometry; validation is on
  8 single-domain benchmarks, not exhaustive.
- *Ch.6.* **Parity, not dominance** — the probe matches but does not statistically
  beat ACT-ViT, with **two firm NQ losses** reported. Feasibility-by-trainability
  argues the signal *exists*, not that this probe extracts it optimally. Evaluated on
  the studied QA datasets / model families; transfer is bounded by what was tested.
- *Synthesis note.* The honest through-line: the dissertation establishes **when**
  detection is possible and **that** principled methods reach it — not that they are
  optimal. Keep this distinction crisp so the limitations don't undercut the spine.

### 7.4 Future Directions
**Genuine open problems**, not proposal leftovers — and where possible, tied back to
a 7.3 limitation so the two sections interlock. Candidates that fall out of the work
and that the dissertation honestly does *not* answer:
- Can the Label Blindness condition be *tested a priori* on a given SSL objective
  (predict blindness before training, not diagnose after)? — addresses the 7.3 Ch.4
  idealization.
- Does DSC have an **information-theoretic dual**? Ch.5 was kept deliberately
  geometric; bridging it to the info-theory lens is real open work and reinforces
  the two-lens thesis.
- Does the cross-layer-MI probe transfer across model families, and from
  **detection → mitigation** (not just flagging hallucinations but steering away)? —
  addresses the 7.3 Ch.6 transfer/optimality bounds.

### 7.5 Concluding Remarks
Short, thesis-level close. The single rhetorical move: all three are the *same
question* asked of three representations. No new content; land the plane.

---

## Drafting notes

- **Length:** longer than v1's conclusion is fine (user-approved). Budget the extra
  length into 7.1.2 (synthesis) and 7.3 (real open problems), not into recap.
- **No bib gate** for this chapter (no `\result{}` macros — it cites no numbers).
  If a specific result is referenced, `\Cref` the source chapter rather than
  restating the figure.
- **Cross-refs over restatement:** `\Cref{ch:label-blindness}` etc. throughout;
  the conclusion points back, it does not re-explain.
- **Voice check before commit:** grep the drafted `.tex` for "propose", "will ",
  "aims to", "expected", "domain feature collapse", "domain filtering", "beats",
  "state-of-the-art" — all should be zero hits.
