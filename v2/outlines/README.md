# outlines/

Per-chapter planning docs (Markdown). These are **not compiled** — they are
where structure, argument, and *proposed citations* are worked out before prose
lands in `chapters/*.tex`.

## Citation gate (why this directory exists)

`references.bib` is human-gated: an agent never edits the `.bib` directly.
Instead, a new citation is first proposed here (in the relevant chapter outline)
with enough bibliographic detail for a human to verify, and only then added to
`references.bib` by a human. This keeps the bibliography trustworthy and is the
companion to the build-time number gate (`make lint`).

Mirror one file per chapter, e.g. `01_introduction.md`, `02_background.md`, ...
