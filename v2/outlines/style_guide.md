# Dissertation Style Guide — the target prose voice

Decided 2026-06-08: **standardize the whole dissertation on the Chapter 4
register** — the plain, direct, declarative voice of the published ICLR work — and
conform the more mannered chapters (Ch.1/2/3/7 + abstract) to it. This guide is the
written definition so the rewrite is reproducible and auditable, not vibes.

**Adopt Ch.4's virtues; fix Ch.4's defects.** The target is "Chapter 4 at its best,"
*not* a literal copy — Ch.4 itself has mechanical sloppiness (§3 below) that gets
cleaned up everywhere, Ch.4 included.

This guide governs **voice and mechanics only**. It is orthogonal to the **framing
locks** (spine, two lenses, "guaranteed failure" Ch.4-only, Ch.5 diagnostic, Ch.6
parity verb) in [00_dissertation_outline.md](00_dissertation_outline.md) — those are
*what* the prose may claim; this is *how* it reads. Both are cross-chapter
invariants; neither overrides the other.

---

## 1. The target voice (one paragraph)

Plain, direct, declarative. Subject–verb–object sentences that state a claim and then
give its reason. Technical terms repeated freely (a reader wants "label blindness"
called "label blindness" every time); abstract framing words used sparingly. Few
em-dashes. No grand closings, no metaphor where a literal noun works. First-person
plural ("we show", "we introduce") for contributions. The model sentence is Ch.4's:
*"OOD detection seeks to identify inputs containing a label that was never present in
the training distribution."*

## 2. Do / Don't (with real before → after from the current draft)

### 2.1 Em-dashes — use sparingly
Target density ≈ Ch.4 (≈ 0.4 per 1k words), not Ch.1 (≈ 16). Reserve the em-dash for
a genuine break in thought; convert decorative ones to commas, periods, or a colon.
- ✗ "Absent, suppressed, retained---the three studies tile the space of what a
  representation can preserve, and the detectability of the shift tracks that
  preservation exactly."
- ✓ "The three studies cover three cases: the distinguishing structure is absent
  (Chapter 4), suppressed (Chapter 5), or retained (Chapter 6). In each, detectability
  tracks how much of that structure the representation keeps."

### 2.2 No grand closings / rhetorical crescendo
- ✗ "...and whether it does is a question we now know how to ask."
- ✓ End on the technical claim, or a plain restatement of the contribution. Cut the
  flourish.

### 2.3 Concrete nouns over signature metaphors
Recurring metaphors have become a fingerprint: "tile the space", "frontier of
detectability", "two faces of one question", "read it out", "is itself evidence".
Keep at most one instance of each across the whole document; replace the rest.
- ✗ "a detector that lands in the same performance band is evidence the lens is right"
- ✓ "a detector derived from this principle reaches the same accuracy as the best
  engineered probe, which supports the principle."

### 2.4 Ration the abstract framing vocabulary
Current counts: "structure" 81×, "lens/lenses" 61×, "preserve" 36×,
"exactly/precisely when" 5×. Some repetition is the thesis and stays. But within a
paragraph, do not use "structure"/"preserve"/"lens" more than once each where a
plainer word (information, features, geometry, view, measure) carries the meaning.

### 2.5 Sentence length / periodic sentences
Break long periodic sentences (claim suspended behind two or three dashes/clauses)
into two plain sentences. The house voice favors one elaborate sentence; the target
favors two clear ones.

### 2.6 Keep
First-person plural for contributions; defining a term then using it; tight
paragraph topic sentences; the existing `\Cref` cross-reference discipline.

## 3. Mechanical consistency (objective — auto-checkable)

These apply to every chapter, **including Ch.4**, which currently violates several.

### 3.1 Hyphenation (canonical forms)
Always hyphenate when used: `self-supervised`, `in-distribution`, `out-of-distribution`,
`single-domain`, `cross-layer`, `zero-shot`, `multi-domain`, `label-relevant`,
`activation-space`. *(Current stragglers: "self supervised" ×2, "in distribution" ×1
— both in Ch.4.)*

### 3.2 Capitalization
Lowercase common nouns mid-sentence: `unsupervised learning`, `self-supervised
learning`, `zero-shot`, `supervised baseline`. Reserve initial caps for proper nouns
and **defined dissertation terms**: Label Blindness Theorem, Adjacent OOD,
Domain-Sensitivity Collapse (DSC), Teacher-Guided Training (TGT), Contrastive+Recon.
*(Current violations, all Ch.4: "Unsupervised Learning" ×4, "Zero Shot" ×1, "Self
supervised" ×1.)*

### 3.3 Banned filler / vague connectives
Replace with the specific content or cut: "due to various factors", "it is important
to note that", "a number of", "various". Name the factors or delete the sentence.

### 3.4 Citation integration
Vary it; do not chain "as proposed by X … as proposed by Y" (Ch.4). Prefer the claim
first, citation in parentheses: "Unlabeled methods can match a supervised baseline
(\citealp{...})."

## 4. Rollout plan (effort by chapter)

| Chapter | Pass | Notes |
|---|---|---|
| Ch.4 | Mechanical only (§3) | The exemplar; do **not** restyle the argument |
| Ch.5, Ch.6 | Mechanical + light de-manner | Trim imported em-dashes/flourish; ports are already dense/plainish |
| Ch.2, Ch.3, Ch.7 | Mechanical + moderate de-manner | Cut ~⅓ em-dashes, de-tic framing vocab |
| **Ch.1, abstract** | Mechanical + heavy de-manner | Most mannered: cut em-dashes, kill grand closings, vary vocab |

Order: write this guide → mechanical pass across all chapters (one commit) → per-chapter
de-manner passes (one commit each, easy to review/revert). Re-run `make paper` after each;
voice edits must not change any `\result`, number, citation, or `\Cref`.

## 5. Optional enforcement (lint)

The mechanical half (§3) is auto-checkable and fits the repo's gate culture
(bib/number gates). A `lint.py` extension could flag: unhyphenated forms from §3.1,
mid-sentence capitalized common nouns from §3.2, and banned phrases from §3.3. Voice
(§2) stays a human judgment. Add only if you want the mechanical rules enforced on
every build.
