# Chapter 1 — Introduction · drafting plan (thesis-first, Option B)

Plan for writing Ch.1, the dissertation's opening chapter and bookend to Ch.7.
Companion to [00_dissertation_outline.md](00_dissertation_outline.md) (Ch.1 entry,
lines 76–92; spine §40–70) and [07_conclusion.md](07_conclusion.md) (the matched
closer — Ch.1 *promises* the arc Ch.7 *discharges*). Source to de-proposalize:
[v1 §1 (inline)](../../v1/Sample_Thesis_main.tex#L95-L161) (note: `v1/Introduction.tex`
is filler — the real v1 intro is inline in the main file).

**Status:** ⬜ not yet drafted (`chapters/01_introduction.tex` is a stub with a
bib-gate demo to delete). No number gate beyond any cited figure (the chapter cites
no results — `\Cref` source chapters instead). One **new figure asset** required
(spine schematic — see §Figure below).

**Not a port — a rebuild.** Like Ch.7, the v1 intro cannot be lifted: it is in
proposal voice, describes the superseded science (DFC/domain-filtering;
insufficient-MI hallucination framing), names an info-theory-only umbrella, and maps
a document that no longer exists (Ch.7 timeline, Ch.8 conclusion). Treat v1 §1 as a
section checklist, not a prose base.

## Structural decisions (2026-06-08, user-approved)

- **Opening = thesis-first (Option B) + one vignette.** State the unifying claim
  early — *detection is possible exactly when the representation preserves the
  structure that distinguishes the shift* — then motivate why it is the right lens.
  Embed **one concrete failure vignette** inside §1.1 (borrowed from Option C:
  e.g. a single-domain medical model confidently misreading a different modality;
  an LLM fabricating a citation). Chosen over funnel-first (A; thesis appears too
  late), pure vignette (C; too informal for a theory-led thesis with a real
  impossibility theorem), and pillars-first (D; fragments the "one thesis" framing).
  **Mirror Ch.7's opening** so the dissertation bookends on the same claim + arc.
- **Contributions = enumerated list + `\Cref` pointers.** Replace v1's prose
  "Objective 1/2/3" paragraphs with an explicit itemized contributions list, each
  item pointing to its chapter. Reads cleanly given the cross-ref discipline; lets
  the committee see deliverables at a glance.
- **Spine schematic figure = yes.** A single failure→recovery→detection schematic
  with the two lenses, in §1.1 or §1.3 (see §Figure).

## Bookend discipline (Ch.1 vs Ch.7)

Same spine, same contribution claims, **different tense and altitude**: Ch.1
*promises and maps*; Ch.7 *reflects and synthesizes*. §1.2 (contribution list) must
not become a copy of §7.1 (synthesis argument) — the intro enumerates, the
conclusion argues. Keep claims/verbs identical across the two so the bookends agree.

---

## Framing locks (carry from master outline — do NOT re-litigate)

The intro is one of the three binding sites for cross-section consistency (intro
contribution + abstract + Ch.6 results). Highest-risk place to set a verb wrong:

- **Spine = representation structure, BOTH lenses.** Lead §1.3 (and the opening)
  with "what the representation preserves" — info theory (Ch.4, Ch.6) **and**
  geometry (Ch.5). Never the info-theory-only umbrella v1 used (explicit open
  follow-up in master outline, Open Question 3(ii)).
- **Arc = failure → recovery → detection.** Ch.4 cannot, Ch.5 restores, Ch.6 reads.
- **"Guaranteed failure" is Ch.4-only.** Label Blindness is the one impossibility
  result; do not generalize the verb to the contribution list's Ch.5/6 items.
- **Ch.5 is diagnostic, not impossibility.** Contribution item must say diagnosis +
  recovery (TGT), not a no-go theorem.
- **Ch.6 verb is locked: "matches-or-outperforms (in the mean)" / parity.** Never
  "beats" / "state-of-the-art." The two NQ losses need not be detailed in the intro,
  but the verb must be the parity verb, identical to abstract + §6.5.
- **No results numbers in the intro.** `\Cref` the source chapter; no `\result{}`
  needed unless a single headline number is genuinely wanted (then gate it).

## Hard deletes / rewrites from v1 §1 (proposal + stale science)

- ✏️ **Voice:** "we propose / we will / aims to" → "we present / we show / we
  establish." Contributions describe **completed** work.
- ✏️ **Objective 1 science:** "domain feature collapse" + "domain filtering" +
  "two-stage detector" → **DSC** + **TGT** (diagnostic-geometric framing).
- ✏️ **Objective 3 science:** "insufficient MI between query and response" →
  cross-layer MI in the residual stream + one-class layer-pair contrastive probe;
  feasibility-by-trainability. Verb = parity.
- ✏️ **§1.3 umbrella:** "information theory as the unifying framework" →
  representation-structure umbrella, two lenses.
- ✏️ **§1.4 document map:** rewrite to the real 7-chapter structure. ❌ delete the
  "Ch.7 research timeline / Ch.8 conclusion" map (Ch.7 = conclusion now).
- ✏️ **§1.5 rename:** "Expected Impact and Significance" → **"Significance"** (drop
  proposal-era "Expected").

---

## Section map

### 1.0 Opening (unnumbered, ~3 paragraphs — thesis-first)
- Para 1: the reliability problem in the open world, with **one concrete vignette**
  (modality shift OR LLM fabrication) to ground it.
- Para 2: name the two faces (OOD detection + LLM hallucination) and state the
  **unifying claim** explicitly (representation preserves distinguishing structure).
- Para 3: name the **two lenses** (info theory + geometry) and the **arc**
  (failure → recovery → detection); forward-point to the spine figure.

### 1.1 Problem Statement and Motivation
- The three reliability settings as instances of one question, not three problems:
  unlabeled OOD (structure absent), single-domain OOD (structure suppressed), LLM
  hallucination (structure retained). Keep the vignette here if not in 1.0.
- **Spine figure** anchors here (or §1.3) — see §Figure.

### 1.2 Research Objectives and Contributions *(drop "Proposed")*
- Short framing paragraph, then an **enumerated contribution list**, each item
  `\Cref`-pointing to its chapter and stated in accomplished voice:
  1. Label Blindness theorem + Adjacent OOD benchmark (`\Cref{ch:label-blindness}`)
     — the guaranteed-failure result.
  2. DSC diagnosis + TGT recovery (`\Cref{ch:domain-sensitivity-collapse}`) —
     diagnostic-geometric, no inference overhead.
  3. Information-theoretic hallucination detector
     (`\Cref{ch:hallucination-detection}`) — feasibility-by-trainability; reaches
     **parity** (locked verb) with the best engineered probe; confirmed
     symmetric-SupCon prediction.
  4. (optional 4th) the cross-cutting methodological contribution: the
     two-lens representation-structure framework itself.

### 1.3 Methodology and Approach
- **Lead with the representation-structure umbrella** (the open follow-up). Both
  lenses as tools for "what the representation preserves": info theory
  (MI/DPI/InfoNCE) and geometry (effective rank, class vs domain-shift subspaces).
- Theory + empirical validation posture; honesty discipline (parity reported with
  losses, diagnostic bounds not over-claimed). Back-ref Ch.2 for primitives.

### 1.4 Dissertation Organization
- Rewrite to the true 7-chapter map: Ch.2 Background (two lenses) · Ch.3 Lit Review
  · Ch.4 Label Blindness · Ch.5 DSC/TGT · Ch.6 MI Hallucination · Ch.7 Conclusion ·
  Appendices A/B/C. `\Cref` each. **No** timeline chapter.

### 1.5 Significance *(renamed from v1 "Expected Impact and Significance")*
- Theory (frontier of detectability), practice (narrow-domain deployment; factuality
  detection without sampling overhead), and the broader AI-safety posture: principled
  accounts of *when* methods can work, not just benchmark wins. Keep brief; do not
  pre-empt §7.2 — Ch.1 promises significance, Ch.7 reflects on it.

---

## Figure: spine schematic (NEW asset)

- **Content:** failure → recovery → detection arc across the three studies, with the
  two lenses (info theory / geometry) labeled; structure absent / suppressed /
  retained. One glance = the whole dissertation.
- **Pipeline:** add a renderer under `figures_src/` (matplotlib or TikZ-via-source);
  output to `generated/figures/` like the Ch.5/6 figures. **No numbers** → no
  bib-gate concern, but it must build under `make figures`.
- **Placement:** §1.1 (anchor the motivation) or §1.3 (anchor the method framing).
  Decide at draft time; lean §1.1.

## Drafting notes

- **No bib gate numbers:** `\Cref` source chapters rather than restating results.
- **Voice-check grep before commit** (expect 0 substantive hits): `propose`,
  `will `, `aims to`, `expected`, `domain feature collapse`, `domain filtering`,
  `two-stage`, `beats`, `state-of-the-art`, `insufficient mutual information`.
- **Cross-check against Ch.7 + abstract** for claim/verb agreement (bookend
  discipline). The abstract (front matter, ⬜) should be drafted from this same
  framing — flag to do together or right after Ch.1.
- **Build:** `make PYTHON=../.venv/bin/python paper` (repo-local venv; deps installed
  2026-06-08). If the spine figure is added, confirm `make figures` renders it.
