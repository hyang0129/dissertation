# Indirection Audit — Chapter 7 (Conclusion)

All prose is connective in Ch.7. The chapter was regenerated-and-gated on 2026-06-09,
so it is already fairly direct; this audit finds 8 genuine instances plus one
structural pattern deliberately **excluded** (see note). Patterns reference
`outlines/indirection_guide.md`.

---

## Instance #1
**Pattern:** 1.7 — Weak relational verb (also clears a §2.8 «holds» register hit)
**Section:** §7.1.1 Label blindness paragraph
**Context:**
```
the minimal sufficient statistic the
model learns holds nothing about the label distinction, and detection against that
distinction is \emph{guaranteed to fail}
```
**Original phrase:** `holds nothing about the label distinction`
**Proposed replacement:** `the minimal sufficient statistic the model learns encodes nothing of the label distinction, and detection against that distinction is \emph{guaranteed to fail}`

---

## Instance #2
**Pattern:** 1.6 — Expletive opener (`it is that …`)
**Section:** §7.1.1 Label blindness paragraph
**Context:**
```
The result is not that current methods happen to score badly; it is
that no method resting on a label-independent objective can work in the worst case.
```
**Original phrase:** `it is that no method resting on a label-independent objective can work in the worst case`
**Proposed replacement:** `The result is not that current methods happen to score badly, but that no method resting on a label-independent objective can work in the worst case.`

---

## Instance #3
**Pattern:** 1.2 — Trailing participial (`leaving …`) + over-long sentence
**Section:** §7.1.1 Domain-sensitivity collapse paragraph
**Context:**
```
Supervised training on one domain pulls the features
into a single low-rank subspace aligned with the classes, leaving the domain-shift
directions flat, so distance-based and logit-based scorers stop
reacting to shifts they ought to catch.
```
**Original phrase:** `…aligned with the classes, leaving the domain-shift directions flat, so distance-based and logit-based scorers stop reacting…`
**Proposed replacement:** `Supervised training on one domain pulls the features into a single low-rank subspace aligned with the classes and flattens the domain-shift directions. Distance- and logit-based scorers then stop reacting to shifts they ought to catch.`

---

## Instance #4
**Pattern:** 1.1 / 1.3 — Cleft setup (`What makes them X is that Y`)
**Section:** §7.1.2 Synthesis
**Context:**
```
What makes them
one dissertation is that each puts the same question to its own setting.
```
**Original phrase:** `What makes them one dissertation is that each puts the same question to its own setting.`
**Proposed replacement:** `They form one dissertation because each puts the same question to its own setting.`

---

## Instance #5
**Pattern:** 1.7 — Weak relational verb (`gives … a way to`)
**Section:** §7.2.1 AI Safety and Reliability
**Context:**
```
Locating the hallucination signal inside a model's
activations gives factuality-critical applications a way to check a generation
without paying for extra samples.
```
**Original phrase:** `gives factuality-critical applications a way to check a generation`
**Proposed replacement:** `Locating the hallucination signal inside a model's activations lets factuality-critical applications check a generation without paying for extra samples.`

---

## Instance #6
**Pattern:** 1.1 — Setup clause opener (`The wider point is that …`)
**Section:** §7.2.3 Evaluation and Benchmarking (section closer)
**Context:**
```
The wider point is that how you evaluate is itself a choice with
consequences.
```
**Original phrase:** `The wider point is that how you evaluate is itself a choice with consequences.`
**Proposed replacement:** `How you evaluate is itself a choice with consequences.`

---

## Instance #7
**Pattern:** 1.6 — Expletive opener (`It is worth being clear about …`)
**Section:** §7.3 Limitations (opener)
**Context:**
```
It is worth being clear about how far the claims go and where they stop. The thesis
has two halves.
```
**Original phrase:** `It is worth being clear about how far the claims go and where they stop.`
**Proposed replacement:** `How far the claims reach, and where they stop, is worth stating plainly.`

---

## Instance #8
**Pattern:** 1.3 — Noun clause for noun phrase (`say what joins them`)
**Section:** §7.1 Summary of Contributions (opener)
**Context:**
```
We take the three studies one
at a time and then say what joins them, since the dissertation's main claim is that
they form a single argument and not three separate ones.
```
**Original phrase:** `say what joins them`
**Proposed replacement:** `name their common thread`

---

## Considered but excluded

**Ch. opening three-case elaboration (lines 22–25) — pattern 1.4.** The thesis
sentence is followed by the three cases ("A representation that never encoded that
structure leaves a detector nothing to find. … When the representation keeps it, a
detector can read it out."), which `indirection_guide.md` §1.4 flags as redundant
elaboration. **Left intact:** the file's framing lock fixes the chapter's spine as the
`failure → recovery → detection` arc, and in the conclusion's opening this is the
synthesis the chapter exists to state, not throat-clearing before a claim. Cutting it
would violate the lock.

---

## Summary

| Section | Count |
|---------|-------|
| §7.1 Summary opener | 1 |
| §7.1.1 Per-study | 3 |
| §7.1.2 Synthesis | 1 |
| §7.2 Implications | 2 |
| §7.3 Limitations | 1 |
| **Total** | **8** |
