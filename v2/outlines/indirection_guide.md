# Indirection Guide — finding it and cutting it

Indirection is the gap between where a sentence starts and where its claim lives.
The reader has to travel through setup, qualification, or restatement before reaching
the point. This guide names the patterns, shows how to find them, and shows how to
fix them. The fixes are structural — swapping surface words without changing the
scaffolding leaves the indirection intact.

---

## 1. What indirection looks like

Every pattern below delays the claim. The sentence is not wrong; it is slow.

### 1.1 Setup clause openers

The sentence announces that a claim is coming before making it.

| Tell | Example |
|---|---|
| "The trouble is that…" | "The trouble is that when such an objective is independent of the label-relevant features, the representation encodes none of the label distinction." |
| "What this means is…" | "What this means is that no detector built on it can succeed." |
| "The point is that…" | "The point is that the signal was discarded." |
| "The issue here is…" | "The issue here is one of representation." |
| "It is the case that…" | "It is the case that detection fails." |
| "Note that…" / "Observe that…" | "Note that the structure is already absent." |

**Fix:** Delete the opener. Start on the claim.

- ✗ "The trouble is that when the objective ignores label-relevant features, the representation encodes no label distinction."
- ✓ "When the objective ignores label-relevant features, the representation encodes no label distinction."

---

### 1.2 Trailing participials

The sentence states its claim and then keeps going in a participial or relative
clause that re-describes the consequence.

**Tell:** "…leaving X unable to Y", "…making it difficult to Z", "…resulting in W",
"…meaning that V."

- ✗ "The optimizer dropped the signal, leaving distance- and logit-based detectors unable to react to the shifts they were meant to flag."
- ✓ "The optimizer discarded the signal. Distance- and logit-based detectors are then blind to the very shifts they should catch."

**Fix:** End the sentence at the claim. Start a new sentence for the consequence if
it is worth stating.

---

### 1.3 Noun clause for noun phrase

A relative clause ("what X does", "what distinguishes Y") stands where a noun phrase
would be cleaner.

**Tell:** "holds what distinguishes", "captures what matters", "encodes what the
detector needs."

- ✗ "whether the representation still holds what distinguishes the shift"
- ✓ "whether the representation still encodes the relevant structure"

**Fix:** Name the thing directly. If you cannot name it, that is a sign the concept
needs a defined term, not a longer clause.

---

### 1.4 Redundant elaboration after a thesis statement

A strong declarative sentence is followed immediately by a sentence (or triplet)
that restates it in different words. The restatement adds no new information.

- ✗ "**A shift is detectable exactly when the model's learned representation still holds the structure that distinguishes it.** The model may never have encoded that structure, or have encoded it and then lost it, or have kept it. If it was never there, a detector is left with no signal and fails outright. …"
- ✓ "**A shift is detectable exactly when the model's learned representation still holds the structure that distinguishes it.**" *(paragraph ends; the figure carries the three cases)*

**Fix:** Let a strong sentence land. Cut the elaboration unless it introduces
genuinely new content (a qualification, a precision, a counter-case).

---

### 1.5 Passive with hidden agent

Passive voice is not always indirection — it is fine when the agent is unknown or
irrelevant. It becomes indirection when the agent matters and is being hidden.

**Tell:** "was present in the training data and then dropped", "was observed to
decrease", "has been shown to fail."

- ✗ "The signal was present in the training data and then dropped by the optimizer."
- ✓ "Training contained the signal; the optimizer discarded it."

**Fix:** Name the agent as the grammatical subject. If naming it makes the sentence
feel strange, ask why — the strangeness is usually a sign the claim is vague.

---

### 1.6 Expletive and existential openers

"There is / there are" and "It is X that Y" defer the real subject.

- ✗ "There is a failure mode we call label blindness."
- ✓ "We call this failure mode label blindness."

- ✗ "It is the representation that determines whether detection is possible."
- ✓ "The representation determines whether detection is possible."

---

### 1.7 Weak relational verbs

"Has", "involves", "relates to", "provides", "shows" connect a subject to a
predicate without saying what the connection is.

- ✗ "This result has implications for how detectors are designed."
- ✓ "This result tells a designer which regimes to avoid."

**Fix:** Replace the weak verb with the specific one. If you cannot find the specific
verb, the sentence is not yet fully formed — figure out the claim first.

---

## 2. How to find indirection in a passage

Read each sentence and ask:

1. **Where does the claim live?** If it is not in the first five words, why not?
2. **Does the sentence keep going after its main verb?** If so, is the tail adding
   new content or restating the head?
3. **Is the grammatical subject the thing the sentence is actually about?** If not,
   restructure so it is.
4. **Does the previous sentence already say this?** If yes, cut.

A fast mechanical check: search for "The trouble is", "What this means", "leaving",
"resulting in", "meaning that", "there is/are", "it is the case", "note that",
"observe that", "holds what", "captures what."

---

## 3. What indirection is not

Not every qualification is indirection. A sentence that hedges because the claim
*is* hedged ("detection degrades, but the structure can be put back") is accurate,
not evasive. The test is whether the sentence's travel serves the reader or just
delays them.

Similarly, a long sentence is not automatically indirect. A sentence can be long and
direct if its subject is concrete and the main verb arrives quickly.
