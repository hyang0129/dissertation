# ECCV 2026 Author Guidelines (extracted from template)

These are the original ECCV submission guidelines that were included in the LaTeX template.
Kept here for reference during paper preparation.

---

## Initial Submission

### Language
All manuscripts must be in English.

### Template
Papers must be prepared with the official LNCS style from Springer.
This applies to both review and camera-ready versions.
Springer requires manuscripts to be prepared in LaTeX (strongly encouraged) or Microsoft Word.

Authors preparing their paper with LaTeX must use the template provided by ECCV, which is based on the corresponding Springer class file `llncs.cls` but includes line numbers for review and properly anonymizes the paper for review.
Authors who cannot use LaTeX can alternatively use the official LNCS Word template from Springer.
However, it is the authors' responsibility to ensure that the resulting PDF file is consistent with the example paper and follows it as closely as possible (i.e., includes line numbers, is properly anonymized, etc.).

The class/style files and the template must not be manipulated and the guidelines regarding font sizes and format must be adhered to.
For example, please refrain from using any LaTeX or TeX command that modifies the layout settings of the template (e.g., `\textheight`, `\vspace`, `\baselinestretch`, etc.).
Such manual layout adjustments should be limited to very exceptional cases.

Papers that differ significantly from the required style may be rejected without review.

#### Fonts
Springer's templates for LaTeX are based on CMR, and the XML templates for Word are based on Times.
Use the font according to the template used for your papers.
Specifically, please refrain from using Times when preparing your paper with LaTeX.
Using a different font can be interpreted as purposely circumventing the length limitations and may lead to rejection without review.

### Paper Length
Papers submitted for review must be complete.
The length should match that intended for final publication.
Papers accepted for the conference will be allocated 14 pages (plus additional pages for references) in the proceedings.
Note that the allocated 14 pages do not include the references.

Papers with more than 14 pages (excluding references) will be rejected without review.
This includes papers where the margins and formatting including the font are deemed to have been significantly altered from those laid down by this style guide.

### Paper ID
It is imperative that the paper ID is mentioned on each page of the manuscript of the review version.
Enter your paper ID in the appropriate place in the LaTeX template (see `%TODO REVIEW`).
The paper ID is a number automatically assigned to your submission when registering your paper submission on the submission site.

### Line Numbering
All lines should be numbered in the initial submission.
This makes reviewing more efficient, because reviewers can refer to a line on a page.
Line numbering is removed in the camera-ready version.

---

## Policies
The policies governing the review process of ECCV 2026 are detailed on the conference webpage (https://eccv.ecva.net/Conferences/2026/SubmissionPolicies), such as regarding confidentiality, dual submissions, double-blind reviewing, plagiarism, and more.
By submitting a paper to ECCV, the authors acknowledge that they have read the submission policies and that the submission follows the rules set forth.

Accepted papers will be published in LNCS proceedings with Springer.
To that end, authors must follow the Springer Nature Code of Conduct for Authors (https://www.springernature.com/gp/authors/book-authors-code-of-conduct).

---

## Preserving Anonymity

ECCV reviewing is double blind: authors do not know the names of the area chair/reviewers, and reviewers cannot infer author names from the submission.

- Do not identify the authors nor provide links to websites that identify the authors.
- If citing a concurrent ECCV submission: (1) cite anonymously, (2) argue non-trivial differences in the body, (3) include anonymized versions in supplemental.

Blind review means you do not use the words "my" or "our" when citing previous work. That is all.

- Saying "this builds on the work of Lucy Smith [1]" does not say that you are Lucy Smith.
- Do NOT say "as we show in [7]"; instead say "as Smith and Jones show in [7]".

For concurrent submissions, include the anonymized parallel submission as supplemental material and cite it as:
> [1] Authors. "The frobnicatable foo filter", ECCV 2026 Submission ID 00324, Supplied as supplemental material 00324.pdf.

For tech reports: the paper must stand on its own. You may say "further details may be found in [ref]" and submit the tech report as supplemental.

Authors must omit acknowledgements in the review copy (add in final copy).

---

## Formatting Guidelines

### Headings
- Capitalize headings (nouns, verbs, etc.; not articles, prepositions, conjunctions).
- Align to the left (except title).
- Only first two levels of section headings should be numbered.
- Do not use "0" when numbering section headings.

Font sizes:
| Heading level | Example | Font size and style |
|---|---|---|
| Title (centered) | **Lecture Notes ...** | 14 point, bold |
| 1st-level heading | **1 Introduction** | 12 point, bold |
| 2nd-level heading | **2.1 Printing Area** | 10 point, bold |
| 3rd-level heading | **Headings.** Text follows ... | 10 point, bold |
| 4th-level heading | *Remark.* Text follows ... | 10 point, italic |

### Figures
- Use `graphicx` package for LaTeX.
- All illustrations must be clear and legible.
- Use vector graphics for diagrams and schemas whenever possible.
- Line drawings: resolution of at least 800 dpi (preferably 1200 dpi).
- Minimum font size in figures: 6pt (~2mm character height).
- Figures should be numbered with captions positioned **under** the figures.
- Tables should have captions positioned **above** the tables.
- Use floating objects; avoid location parameter "h".

### Formulas
- Displayed equations centered on a separate line.
- Number all equations for reference (consecutive within the contribution).
- Do not include section counters in numbering.
- Equations should never be in color.
- Equations should be punctuated as ordinary text.
- See Mermin's description: https://doi.org/10.1063/1.2811173

### Lemmas, Propositions, and Theorems
- Numbers should appear in consecutive order, starting with Lemma 1.
- Do not include section counters (e.g., avoid "Theorem 1.1").

### Footnotes
- Superscript numeral appears directly after the word or following punctuation.
- No footnotes in the abstract.

### Cross References
- Use `\cref{...}` for cross-referencing figures, tables, equations, or sections.
- Use `\Cref{...}` at the beginning of a sentence.

### Program Code
- Set in typewriter font (e.g., `\texttt{...}`).

### Citations
- Arabic numbers in brackets (not superscript).
- References should be formatted with the official LNCS reference style (`splncs04.bst`).
- Include DOIs when possible.
- All references cited in text should be in the reference list and vice versa.

### Miscellaneous
- Use `\eg` macro (not *e.g.*) for correct spacing.
- Use `\etal` macro for "et al." (only when 3+ authors).

### Most Frequently Encountered Issues Checklist
- [ ] Removed all `\vspace` and `\hspace` commands.
- [ ] No `\cite` in the abstract.
- [ ] Entered a correct `\titlerunning{}` command.
- [ ] Same name spelling across all accepted ECCV / ECCV Workshop papers.
- [ ] Acknowledgments use `\section*{}` (unnumbered).
- [ ] Paper is no longer than 14 pages (excluding references and acknowledgments).
- [ ] Font size not decreased to fit into 14 pages.
