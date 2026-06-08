# Front Matter · drafting plan (Abstract · Acknowledgements · Dedication)

Plan for the remaining front-matter stubs — the last items on the critical path
after Ch.1/Ch.7. Companion to [00_dissertation_outline.md](00_dissertation_outline.md).
Render order set in [main.tex](../main.tex#L99-L102): Abstract → Acknowledgements →
Dedication → Publications → ToC. Files:
[frontmatter/Abstract.tex](../frontmatter/Abstract.tex),
[frontmatter/Acknowledgements.tex](../frontmatter/Acknowledgements.tex),
[frontmatter/Dedication.tex](../frontmatter/Dedication.tex).

**Status:** Abstract ⬜ · Acknowledgements ⬜ · Dedication ⬜ (all 3 stubs).
CoverPage ✅ structure but **placeholders unfilled** (advisor/committee/date — see
§Gaps). Publications ✅ done.

**Division of labor (who writes what):**
- **Abstract** — *Claude can fully draft.* Technical summary; rebuild from the spine
  framing (not a port of the stale v1 abstract).
- **Acknowledgements** — *author supplies substance; Claude can scaffold.* Names of
  people/funders are the author's to provide.
- **Dedication** — *author only.* One personal line; not Claude's to write.

---

## 1. Abstract (Claude-draftable)

**Rebuild, not a port.** [v1/Abstract.tex](../../v1/Abstract.tex) is proposal-voiced
("proposes novel"), uses the **info-theory-only umbrella** (wrong — must be
representation-structure, two lenses), and **overclaims** ("superior performance",
"theoretical guarantees about detection performance") — both violate locked framing
(Ch.6 parity verb; Ch.5 diagnostic-not-guarantee). Do not reuse its claims.

**Framing locks (same as Ch.1/Ch.7 — this is the 3rd binding site for cross-section
consistency: abstract + §1 contribution + §6 results):**
- Lead with the **representation-structure** thesis, BOTH lenses (info theory +
  geometry). Never info-theory-only.
- Arc = failure → recovery → detection; "guaranteed failure" is Ch.4-only.
- Ch.5 = diagnostic + recovery (TGT), not impossibility.
- Ch.6 verb = **"matches-or-outperforms (in the mean)" / parity**, never "beats" /
  "superior" / "state-of-the-art."
- No hard-coded result numbers (front matter isn't gated, but stay consistent —
  qualitative claims only).

**Content (≈250–350 words; check RIT/ProQuest cap — UMI abstracts are often capped
at 350 words):**
1. The reliability problem (OOD detection + LLM hallucination) and the unifying
   claim (detection possible iff the representation preserves distinguishing
   structure).
2. The two lenses (info theory + geometry) as instruments for "what the
   representation preserves."
3. One sentence per pillar in the failure→recovery→detection arc:
   - Ch.4: Label Blindness — guaranteed failure of unlabeled OOD when the surrogate
     is label-independent; Adjacent OOD benchmark.
   - Ch.5: DSC (diagnostic geometric account) + TGT recovery, no inference overhead.
   - Ch.6: information-theoretic hallucination detector; parity with the best
     engineered probe = evidence the principle is right.
4. Closing: the contribution is the unifying framework + the demonstration that
   principled methods reach the detectability frontier (not optimality).

**Mirror the Ch.1 opening and Ch.7 close** — same claim, compressed. Verb/claim
agreement across abstract ↔ §1.2 ↔ §6 is mandatory.

## 2. Acknowledgements (author supplies; Claude scaffolds)

Warm but professional; ~½–2 pages. Conventional order:
1. **Advisor(s)** — most prominent; mentorship/guidance. *(Cover page advisor field
   is still a placeholder — confirm who.)*
2. **Committee** — by name. Per [dissertation-committee] memory: Desell, Ororbia,
   KhudaBukhsh, Yu (RIT-internal). Confirm roles (advisor vs. members vs. program
   director vs. external chair) against the cover-page fields.
3. **Collaborators / co-authors** — the three papers behind Ch.4–6 (e.g., ECCV
   co-authors Kar/Yu/Desell/Ororbia); labmates.
4. **Funding & resources — often MANDATORY.** Grants (with numbers), fellowships,
   institutional support, compute/data providers. Funders frequently require explicit
   acknowledgement — do not skip. *(Author: list grant numbers / compute sources.)*
5. **Department / institution / staff.**
6. **Family / partner / friends** — personal support.

Claude can produce a **labelled skeleton** with bracketed slots once the author says
who goes in each bucket. Specific > generic.

## 3. Dedication (author only)

One line to a few lines, centered, often no heading. To family / mentor / someone
meaningful, or a short quote. Optional. **Personal — author writes this; Claude does
not draft it.** A `\begin{dedication}` placeholder can hold `% TODO` until then.

---

## Gaps to close before final (not blockers for drafting the abstract)

- **CoverPage placeholders** ([CoverPage.tex](../frontmatter/CoverPage.tex)):
  `\advisor`, `\memberA–D`, `\externalchair`, `\degreedate` all still bracketed.
  Committee names known from memory (Desell/Ororbia/KhudaBukhsh/Yu); **role
  assignment + advisor + program-director + date** need author confirmation. Defense
  target Aug 2026, so `\degreedate` likely "August 2026" pending acceptance.
- **Order check:** main.tex renders Dedication *after* Acknowledgements. Many theses
  put the dedication first; RIT's `thesisfrontmatter` template may dictate this
  order — confirm against the official RIT format spec before reordering (low risk,
  but verify).
- **Abstract length:** confirm the RIT/ProQuest word cap (commonly 350) and trim to
  fit.

## Build note

Front matter is **not bib-gated** for numbers, but keep claims consistent with the
gated chapters. `\begin{abstract|acknowledgements|dedication}` environments come from
`thesisfrontmatter.sty`; the stubs already compile, so keep the environment form.
Build: `make PYTHON=../.venv/bin/python paper`.
