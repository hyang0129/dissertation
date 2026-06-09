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

**Exception — the thesis refrain.** One sentence is allowed to recur verbatim as a
bookend: *"When the representation keeps it, a detector can read it out."* It states
the third case of the spine and appears in exactly three places — the abstract, the
Ch.1 thesis statement, and the Ch.7 thesis statement — and nowhere else. This is a
deliberate device, not a metaphor leak. The *incidental* uses of "read it out" in
running prose were reworded (to "extract"/"detect"); treat any fourth occurrence as a
leak. *(Resolved 2026-06-09: "read it out" = 3 bookend uses + 0 incidental;
"is itself evidence" reduced to 1, in the abstract.)*

### 2.4 Ration the abstract framing vocabulary
Current counts: "structure" 81×, "lens/lenses" 61×, "preserve" 36×,
"exactly/precisely when" 5×. Some repetition is the thesis and stays. But within a
paragraph, do not use "structure"/"preserve"/"lens" more than once each where a
plainer word (information, features, geometry, view, measure) carries the meaning.

### 2.5 Sentence length / periodic sentences
Break long periodic sentences (claim suspended behind two or three dashes/clauses)
into two plain sentences. The house voice favors one elaborate sentence; the target
favors two clear ones.

### 2.6 The zoom-out trap: concrete subjects in significance/closing sentences
This is the single-word counterpart to §2.3, and the rule it polices is the one the
guide most often missed. The plain register works because Ch.4's subjects are real
things (a dataset, a probe, a distance). It *fails* in field-level "significance" and
closing sentences ("More broadly, …", "This work matters …", chapter bridges), where
the slot has no concrete referent. The template still demands a subject, so it fills
with stacked abstractions joined by weak relational verbs, and to vary the rationed
framing vocabulary (§2.4) it reaches for a connotative **near-miss noun** — a word
chosen for what it *connotes*, landing one ontological category off from what it
*denotes* (catachresis). Naming an intellectual object ("a principled account") with a
**behavior word** ("a habit", "a posture", "an instinct") is the signature tell. A
second tell is **heavy-NP / dative inversion** ("adds *to AI safety* a habit …"),
which garden-paths the reader.

**Rule.** In any zoom-out / significance / closing sentence, the grammatical subject
must be a concrete referent from the work (a study, a result, a benchmark, a detector,
a theorem). Do not place an abstract noun in dative-inverted position, and do not name
an intellectual object with a behavior word.

- ✗ "More broadly, the work adds to AI safety a habit that complements benchmarking: a
  principled account of when reliability is achievable at all."
- ✓ "More broadly, the work gives AI safety a complement to benchmarking: a principled
  account of when reliability is achievable at all."

**The fix is structural, not lexical.** Do **not** treat this as a word swap. The
defect survived three style passes precisely because each pass swapped surface words
and left the inverted/nominal scaffolding intact — the draft's "a posture that
complements empirical evaluation" was "rewritten" only into the *worse* "a habit that
complements benchmarking" (plainer word, further-off category). Re-anchor the sentence
on a concrete subject; do not hunt for a better metaphor. The defect lives in the
imitations (Ch.1/7 summaries), never in the Ch.4 exemplar, whose subjects are concrete
by construction.

### 2.7 Keep
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
Lowercase common nouns **mid-sentence in running prose**: `unsupervised learning`,
`self-supervised learning`, `zero-shot`, `supervised baseline`. Reserve initial caps
for proper nouns and **defined dissertation terms**: Label Blindness Theorem, Adjacent
OOD, Domain-Sensitivity Collapse (DSC), Teacher-Guided Training (TGT), Contrastive+Recon.
*(The Ch.4 mid-sentence violations — "Unsupervised Learning" ×4, "Zero Shot",
"Self supervised" — were fixed in the 2026-06 passes.)*

**Headings are exempt — they use Title Case.** The document-wide house convention for
`\section`/`\subsection`/`\paragraph` titles is Title Case ("Out-of-Distribution
Detection", "Teacher-Guided Training", "Self-Supervised Baselines"). Do **not**
lowercase headings to satisfy the rule above; that rule governs running prose only.
The only heading defect to watch is *internal* inconsistency — e.g. a hyphenated
compound capitalized as "Self-supervised" in one heading and "Self-Supervised" in
another. Capitalize every significant element of a hyphenated compound ("Self-Supervised",
"Single-Domain"); keep short function words lowercase ("of", "and", "for").

### 3.2a Spelling — American English (canonical)
The dissertation is American English (RIT; the Ch.4 ICLR exemplar and the abstract are
American). Use `-ize`/`-ization`/`-yze` and American forms throughout; do not import
British `-ise`/`-isation`/`-yse` or `-our`/`-re`/`-lled` spellings.
- ✓ `optimize`, `characterize`, `generalization`, `analyze`, `labeled`, `modeling`,
  `behavior`, `color`, `favor`, `center`, `gray`/`grayscale`, `catalog`
- ✗ `optimise`, `characterise`, `generalisation`, `analyse`, `labelled`, `modelling`,
  `behaviour`, `colour`, `favour`, `centre`, `grey`/`greyscale`, `catalogue`
*(Resolved 2026-06-09: ~50 British forms, concentrated in Ch.3/Ch.5, converted. Note
words spelled the same in both dialects — "characteristics", the plural noun
"analyses" — and do not over-correct them.)* This is auto-checkable; see §5.

### 3.3 Banned filler / vague connectives
Replace with the specific content or cut: "due to various factors", "it is important
to note that", "a number of", "various". Name the factors or delete the sentence.

### 3.4 Citation integration
Vary it; do not chain "as proposed by X … as proposed by Y" (Ch.4). Prefer the claim
first, citation in parentheses: "Unlabeled methods can match a supervised baseline
(\citealp{...})."

## 4. Rollout plan (effort by chapter)

**✅ DONE 2026-06-08.** All passes executed and pushed; every piece is at 0 em-dashes
except Ch.4 (1, the exemplar). Each pass was its own commit, built clean
(`make paper` exit 0, lint + check_refs OK, 0 undefined refs, all `\result` keys
resolve). Decision recorded: **fresh-authored pieces got full rewrites** (sentence
architecture re-authored); **ported results chapters got surgical de-manner only**
(em-dashes converted, prose tied to numbers/proofs left intact).

| Chapter | Pass run | Commit |
|---|---|---|
| Ch.4 | Mechanical only (§3) — hyphenation/caps/filler | `8d6b5a6` |
| Ch.1 | Full rewrite (deepest) | `ea29491` (after de-manner `37c9c9c`) |
| Abstract | Full rewrite | `ed6005c` |
| Ch.7 | Full rewrite | `4d8a2b0` |
| Ch.2 | Full rewrite (prose; definition bodies untouched) | `70c94f9` |
| Ch.3 | Full rewrite (prose; dropped "Spine tie." labels) | `563d33f` |
| Ch.5 | Surgical de-manner (36 em-dashes; 4 splices fixed) | `b0ef0ee` |
| Ch.6 | Surgical de-manner (63 em-dashes; no splices) | `9103ec5` |

Residual: the ported chapters (Ch.5/6) keep a touch more paper-prose rhythm than the
fully re-authored ones — by design (their prose is load-bearing for numbers/proofs).
Bringing them to the full-rewrite standard is a larger, higher-risk pass, deliberately
not run.

Order followed: guide → mechanical pass (Ch.4) → per-chapter passes (one commit each).
`make paper` was re-run after each; no `\result`, number, citation, or `\Cref` changed.

**Follow-up 2026-06-09.** A review found two residual mechanical items the earlier
passes missed: (a) a British/American spelling split (~50 British forms in Ch.3/5,
American everywhere else) and (b) signature metaphors over the §2.3 cap. Fixed:
spelling standardized to American (§3.2a added), incidental "read it out"/"is itself
evidence" reworded with the thesis refrain preserved (§2.3 exception added), and the
one inconsistent Ch.4 heading ("Self-supervised" → "Self-Supervised") aligned to the
house Title Case (§3.2 heading note added). `make paper` exit 0 (147 pp), lint OK,
diff prose-only.

A root-cause review of one "alien"-reading sentence (the §1.5 significance closer,
"…adds to AI safety a habit…") found a §2.3 blind spot: the guide policed multi-word
signature metaphors but not single-word catachresis or dative inversion in zoom-out
sentences. Traced the sentence's git lineage and found the defect *survived* the
de-manner and full-rewrite passes (draft "a posture that complements empirical
evaluation" → rewrite "a habit that complements benchmarking": surface swapped,
scaffolding kept, category error worsened). Added §2.6 (concrete subjects in
significance/closing sentences; fix is structural not lexical) and a partial lint note
in §5.

## 5. Enforcement (gates): the lint half and the voice meter

The mechanical half (§3) is auto-checkable and fits the repo's gate culture
(bib/number gates). A `lint.py` extension could flag: unhyphenated forms from §3.1,
mid-sentence capitalized common nouns from §3.2, banned phrases from §3.3, and
**British spellings from §3.2a** (a fixed `-ise→-ize`/`-our→-or`/etc. wordlist,
excluding the same-in-both words). Spelling is the highest-value addition — it drifts
back in every newly-authored paragraph and is unambiguous to check.

The **texture** half is now built: `voice_meter.py` (`make voice`) measures
sentence-length variance, tricolon density, and **cross-chapter n-gram repetition**
against the Ch.4 profile (`data/voice_profile_ch4.json`, rebuilt with
`make voice-profile`). It is warning-only and deliberately kept out of `make paper`
until the framing chapters pass; run `python voice_meter.py --gate` to fail on a
gateable issue (flat burstiness, tricolon cap, or a new cross-chapter 6-gram). The
behavior-word tell of §2.6 (flag "habit/posture/instinct/reflex/muscle" near
"account/argument/framework/principle") and the dative-inversion half stay human
judgment. See §6 for how to use the meter inside a rewrite.

## 6. The voice problem is GENERATIVE, not subtractive (read this before a rewrite)

**Decided 2026-06-09.** §§1–5 above are a *detect-and-patch* system: a banned-list
of surface tells, removed after the fact. That approach plateaued, and §2.6 is the
autopsy — every patch pass swaps surface words and leaves the sentence scaffolding
(and the category error) intact, because each pass is itself a generation step that
re-launders the prose back toward the model's smooth, typical mode. You cannot
subtract your way to a human voice. The Ch.4 register is a *property of the
generative process*, so the fix is to **regenerate, not patch.**

### 6.1 What the meter actually found (correct the intuition)

`voice_meter.py` (the VOICE METER, companion to `lint.py`) measures texture against
the human Ch.4 exemplar. Run on the framing chapters, it overturned the obvious
hypothesis:

* **Burstiness is NOT the tell here.** Every framing chapter already has *more*
  sentence-length variance than Ch.4 (cv ≈ 0.48–0.52 vs Ch.4's 0.41). Do not waste
  effort "adding short and long sentences" — that box is already checked.
* **The two real, measured tells are:**
  1. **Cross-chapter verbatim repetition.** The thesis sentence
     ("…detection is possible exactly when the learned representation preserves the
     structure that distinguishes the shift") and ~40 other 6-grams are recited
     near-verbatim across abstract + Ch.1 + Ch.3 + Ch.7. This is the dominant tell.
  2. **Tricolon density.** Ch.2/3/7 run 3.9–5.4 rule-of-three lists per 1k words;
     Ch.4 runs 1.0. The relentless "A, B, and C" scaffolding is machine cadence.

So the rewrite target is concrete and measurable: **kill the recited n-grams and
halve the tricolons**, while leaving the (already good) sentence-length variance
alone.

### 6.2 The regenerate-not-patch workflow (run this, don't hand-edit)

For each framing piece (abstract, Ch.1/2/3/7), section by section:

1. **Strip the claims to bare bullets.** Extract *what the section must say* as a
   terse, unphrased bullet list (claim, reason, cross-ref). Discard the existing
   prose entirely — if you keep it on screen, the regen anchors to its mode. The
   framing locks ([00_dissertation_outline.md](00_dissertation_outline.md)) and the
   `\result`/`\cite`/`\Cref` content are invariants and must survive verbatim; the
   *sentences* are disposable.
2. **Condition on Ch.4 spans chosen for RHYTHM, not topic.** Paste 3–5 verbatim
   Ch.4 paragraphs picked for structural diversity (one short punchy one, one long
   technical one, the soft closer) — explicitly *not* the Ch.4 paragraph nearest in
   subject. (Length-matched exemplars improve voice fidelity; topic-matched ones
   hurt it.)
3. **Generate 3–5 structurally different drafts, then select/splice.** Ask for
   several drafts that vary their structure, and splice at *paragraph* boundaries
   (sentence-level splicing produces incoherent Frankenstein prose).
4. **Enforce the anti-scaffolding constraints in the prompt:** no three-item
   parallel lists (use one item or an uneven 2/4); no balanced aphoristic closer
   (end on the plainest statement of the claim — §2.2); do not reuse a sentence,
   appositive, or example-triple that appears in another chapter; vary the thesis
   statement asymmetrically across its three homes (different length, order, and
   which case you lead with) — only the one sanctioned bookend (§2.3) recurs verbatim.
5. **Gate before a human reads it.** `make voice` (or `python voice_meter.py --gate`)
   must show the section's tricolon rate under the cap and add **no** new
   cross-chapter 6-gram. Regenerate until it passes.
6. **The meter-guided 2nd pass (do this for EVERY chapter, not just the pilot).**
   The bulk regenerate of step 3 will not clear all the recited n-grams in one shot
   — splicing and paraphrase shift the overlaps around. So after it, run the meter
   against the *other* framing files and work the residual list it prints. This pass
   is **targeted edits, not a re-regenerate**: each remaining phrase is one or two
   words from clearing. **Triage every residual into one of three buckets:**
   * **Genuine recitation** → fix in place. A reused sentence, appositive, scope
     statement ("…shows when detection is possible and that principled methods reach
     that limit"), or method description ("we build a one-class contrastive probe
     over cross-layer activation pairs"). Change the framing, not the meaning; note
     that the matching span often sits *before* your first edit, so re-measure and
     repeat until it clears.
   * **Defined technical term** → leave it. The theorem vocabulary ("independent of
     the label-relevant features", "minimal sufficient statistic") is *supposed* to
     recur (§1). Do not contort prose to dodge a defined term.
   * **Framing-lock-mandated** → whitelist it, do not rewrite. Phrases the locks fix
     verbatim (the Ch.6 parity verb "matches-or-outperforms, in the mean … strongest
     engineered probe") recur by design. Add them to `SANCTIONED_BOOKENDS` in
     `voice_meter.py`, exactly as the thesis bookend already is, so the meter stops
     flagging them. Two are whitelisted as of 2026-06-09.
   Iterate steps 5–6 until the only cross-chapter repeats left are the second and
   third buckets. (Ch.7 pilot, 2026-06-09: tricolons 4.88→1.58/1k; cross-chapter
   repeats 23→4, the 4 being windows of the one term "label-relevant features".)
7. **One human read-aloud pass** for local stake and unevenness (§6.3). This is the
   only step that is not automatable.

### 6.3 The irreducible residual (do not try to automate this)

Ch.4 reads human partly because its author cared unevenly — a longer aside where
the idea was interesting, a soft real wish at the close, a minor roughness left in.
A model asked to *simulate* unevenness produces *uniform* unevenness, and
manufactured imperfection reads as its own artifact. The meter + workflow get ~80–90%
of the way (the surface tells go, the cadence flattens toward Ch.4); the last 10% is
a human read-aloud pass, not another rule. Gate the mechanical; reserve judgment for
voice.

