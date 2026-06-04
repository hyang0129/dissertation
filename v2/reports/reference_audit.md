# Bibliography Integrity Audit — `v2/references.bib`

**Date:** 2026-06-04  
**Scope:** all 161 entries in `v2/references.bib`, verified against external sources (arXiv, Crossref, Nature, ACL Anthology, Semantic Scholar, publisher pages).  
**Method:** multi-agent workflow `reference-audit` — 27 parallel verification batches (~6 refs each) → adversarial re-check of every non-confirmed entry → synthesis. 33 agents, 287 web lookups, ~6.8 min.  
**Purpose:** detect hallucinated / fabricated references before any chapter cites from this file.

> **Resolution (2026-06-04):** all findings actioned — see [../outlines/bib_corrections_2026-06-04.md](../outlines/bib_corrections_2026-06-04.md). 8 entries corrected; `zhang2023sirens`, `rogers2020primer`, `card_data` removed; a pre-existing orphaned `huang2021mos` fragment removed. `references.bib`: 161 → 158 entries.

## Verdict

| Status | Count | % |
|---|---|---|
| ✅ Confirmed | 156 | 96.9% |
| ⚠️ Suspicious (fabricated / corrupted) | 4 | 2.5% |
| ❓ Unresolved | 1 | 0.6% |
| **Total** | **161** | |

> A bibliography integrity audit of all 161 references in the dissertation found the large majority to be genuine, correctly attributed publications: 156 entries (96.9%) were confirmed against external sources, almost all at high confidence. However, four entries are SUSPICIOUS and must not be treated as trustworthy as written, and one dataset citation is UNRESOLVED (its source could not be located at all). Two failure modes dominate the serious problems: (1) arXiv identifiers that resolve to a completely different, unrelated paper (zhang2023sirens, farquhar2024detecting), and (2) fabricated or conflated metadata where a real title is paired with invented authors/venue or two distinct papers are merged into one entry (single2023realwaste, rogers2020primer). Separately, a long tail of confirmed entries carries real but non-trivial metadata errors -- wrong author lists (berant2013semantic, chern2023factool), a fabricated journal/volume citation (xu2017information), truncated author lists (karras2017progressive), a malformed author/title (robert1952fano), and an impossible edition year (cover1999elements) -- that are individually defensible as the source exists, but collectively indicate the .bib file was assembled without systematic identifier verification. The preprint-vs-proceedings year offsets seen throughout (e.g. hendrycks2016baseline, liang2017enhancing, devlin2018bert) are acceptable and not counted as defects.

## ⚠️ Suspicious — must fix before submission

Two failure modes: an arXiv ID resolving to an unrelated paper, and a real title paired with fabricated/conflated metadata.

### `zhang2023sirens` — Sirens: Detecting hallucinations in large language models using uncertainty
- **Problem:** Cited arXiv ID 2310.13988 resolves to "GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4" (Kocmi & Federmann, WMT 2023), an unrelated machine-translation paper. No paper exists with the title "Sirens: Detecting hallucinations in large language models using uncertainty" or the listed authors. Title, authors, and arXiv ID are mutually inconsistent with any real publication.
- **Correct identifier:** arXiv:2310.13988 (resolves to a DIFFERENT paper: GEMBA-MQM)
- **Evidence:** https://arxiv.org/abs/2310.13988 (verified = GEMBA-MQM, Kocmi & Federmann); https://arxiv.org/abs/2309.01219 (closest real work: Siren's Song survey, Yue Zhang et al.)
- **Note:** Appears FABRICATED. Likely confabulated from the real "Siren's Song in the AI Ocean: A Survey on Hallucination in LLMs" (different title; authors Yue Zhang et al.; arXiv:2309.01219). Independent verification (direct arXiv fetch + title/author web searches) reproduced the first-pass result exactly. Recommend replacing with the genuine Siren's Song survey (zhang2023sirenssong, arXiv:2309.01219) or removing the citation.

### `farquhar2024detecting` — Detecting hallucinations in large language models using semantic entropy
- **Problem:** The journal field cites arXiv:2406.15012, but that arXiv id belongs to a completely unrelated paper ("Exact discovery is polynomial for certain sparse causal Bayesian networks" by Felix L. Rios, Giusi Moffa, Jack Kuipers). The real Farquhar et al. semantic-entropy paper was published in Nature 2024 (DOI 10.1038/s41586-024-07421-0), not as that arXiv preprint. Title, authors, and year are correct.
- **Real paper:** Detecting hallucinations in large language models using semantic entropy — Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, Yarin Gal (2024, Nature, volume 630(8017), pages 625-630)
- **Correct identifier:** DOI 10.1038/s41586-024-07421-0 (Nature). The cited arXiv:2406.15012 is WRONG.
- **Evidence:** https://arxiv.org/abs/2406.15012 (independently fetched; resolves to "Exact discovery is polynomial for certain sparse causal Bayesian networks" by Rios/Moffa/Kuipers); https://www.nature.com/articles/s41586-024-07421-0 ; https://pubmed.ncbi.nlm.nih.gov/38898292/
- **Note:** Independently confirmed both halves of the first-pass finding: (1) WebFetch on arxiv.org/abs/2406.15012 returns the causal Bayesian networks paper, not the hallucination paper; (2) the genuine Farquhar/Kossen/Kuhn/Gal paper is real and appeared in Nature. The bib entry describes a real, well-known paper but carries a fabricated/incorrect resolving identifier. Correct it to the Nature DOI. Flagged suspicious because the citation as written points to an unrelated work.

### `single2023realwaste` — RealWaste: A Novel Real-Life Data Set for Landfill Waste Classification Using Deep Learning
- **Problem:** Title and year match a REAL paper, but authors and venue are fabricated. Bib lists authors 'Single, Nikita and Jain, Harsh and Jain, Priyanka' — the real authors are Sam Single, Saeid Iranmanesh, Raad Raad (only the surname 'Single' overlaps; 'Nikita Single', 'Harsh Jain', and 'Priyanka Jain' are all wrong/invented). Bib venue is 'IEEE Access, vol. 11, pp. 112562-112584, publisher IEEE' — the real venue is MDPI journal Information, vol. 14, no. 12, article 633, DOI 10.3390/info14120633. Page range and volume are also wrong.
- **Real paper:** RealWaste: A Novel Real-Life Data Set for Landfill Waste Classification Using Deep Learning — Sam Single, Saeid Iranmanesh, Raad Raad (2023, Information (MDPI), vol. 14, no. 12, article 633)
- **Correct identifier:** 10.3390/info14120633
- **Evidence:** https://www.mdpi.com/2078-2489/14/12/633 ; https://www.semanticscholar.org/paper/RealWaste:-A-Novel-Real-Life-Data-Set-for-Landfill-Single-Iranmanesh/19755b7264e1d39949cb71b5dd878b9276101d7c ; https://www.preprints.org/manuscript/202311.0347/v1
- **Note:** Independently re-verified via WebSearch. The underlying paper genuinely exists (RealWaste dataset, Whyte's Gully landfill, Wollongong NSW; 4752 images, 9 classes; Inception V3 89.19% accuracy), but the citation's author list and journal/volume/pages metadata are largely fabricated. A correct citation would be: Single, S.; Iranmanesh, S.; Raad, R. "RealWaste: A Novel Real-Life Data Set for Landfill Waste Classification Using Deep Learning." Information 2023, 14(12), 633.

### `rogers2020primer` — A primer on neural network models for natural language processing
- **Problem:** The entry conflates two distinct real papers. The cited TITLE ("A primer on neural network models for natural language processing") is Yoav Goldberg's JAIR 2016 article (vol. 57, pp. 345-420), but the cited AUTHORS (Rogers, Kovaleva, Rumshisky) wrote a different paper, "A Primer in BERTology" (TACL 2020, vol. 8, pp. 842-866). The bib's journal=JAIR matches Goldberg not Rogers; volume=61 matches neither (Goldberg=57, Rogers=8); pages=65-95 match neither (Goldberg=345-420, Rogers=842-866); year=2020 matches Rogers not Goldberg. No single real paper matches the entry as written.
- **Real paper:** A Primer in BERTology: What We Know About How BERT Works (matches the cited authors); the cited title belongs to a different paper: "A Primer on Neural Network Models for Natural Language Processing" by Yoav Goldberg — Anna Rogers, Olga Kovaleva, Anna Rumshisky (authors of "A Primer in BERTology", TACL 2020). The cited title's actual author is Yoav Goldberg (JAIR 2016). (2020 (Rogers et al. BERTology); 2016 (Goldberg JAIR primer), Transactions of the Association for Computational Linguistics (TACL), vol. 8, pp. 842-866 (Rogers et al.); the cited title appeared in JAIR vol. 57, pp. 345-420 (Goldberg).)
- **Correct identifier:** 10.1162/tacl_a_00349 / arXiv:2002.12327 (Rogers et al.); arXiv:1510.00726 / JAIR view/11030 (Goldberg)
- **Evidence:** https://aclanthology.org/2020.tacl-1.54/ ; https://arxiv.org/abs/2002.12327 ; https://jair.org/index.php/jair/article/view/11030 ; https://arxiv.org/abs/1510.00726
- **Note:** Independently confirms the first-pass verdict. The entry is a garbled/fabricated reference mashing Goldberg's title+journal onto Rogers et al.'s authorship+year, with a volume (61) and page range (65-95) belonging to neither. Likely intended citation is either Goldberg 2016 (if the title is what matters) or Rogers et al. 2020 "A Primer in BERTology" (if the authors/year are what matters). Author should pick one and correct all fields.

## ❓ Unresolved — verify by hand

### `card_data` — Playing Cards Dataset
- **Problem:** Cited Kaggle URL (handle adityasoni04) returns a confirmed HTTP 404 and is not indexed/cached by any search engine. The Kaggle users named "Aditya Soni" that actually exist use the handles adityaecdrid and dasyud, not adityasoni04, so the cited owner handle does not match any known account. Many "Playing Cards Dataset" entries exist on Kaggle but all under different owners (vdntdesai11, hugopaigneau, andy8744, jaypradipshah, gpiosenka, ashraygattani, jamesmcguigan); none is owned by an "Aditya Soni." No corroboration of a 2020 Playing Cards Dataset by Aditya Soni at the cited handle.
- **Evidence:** https://www.kaggle.com/datasets/adityasoni04/playing-cards-dataset (HTTP 404, confirmed) ; https://www.kaggle.com/adityaecdrid ; https://www.kaggle.com/dasyud ; web searches for "adityasoni04 kaggle playing cards" and "Aditya Soni Playing Cards Dataset Kaggle" returned no matching dataset
- **Note:** Adversarial second pass. Handle mismatch (adityasoni04 vs. the real adityaecdrid/dasyud) is positive evidence the citation as written is wrong, pushing toward suspicious. However, Kaggle datasets are routinely deleted or renamed and dataset slugs change, and Kaggle pages sit behind reCAPTCHA/anti-bot so are poorly indexed; a 404 plus absence from search is therefore not conclusive proof the dataset never existed. Cannot affirmatively confirm (no title/owner match found) and cannot prove fabrication. Genuinely undeterminable without a logged-in Kaggle check; the dataset is also low-stakes (a generic playing-cards image dataset, freely substitutable). Recommend manual verification by a logged-in user or replacing with one of the corroborated alternatives (e.g., gpiosenka/cards-image-datasetclassification).

## Key findings (synthesis)

Includes confirmed entries that cite a *real* paper but carry wrong fields — fix the metadata; the source is safe to keep.

- SUSPICIOUS - zhang2023sirens: The cited arXiv ID 2310.13988 resolves to an UNRELATED machine-translation paper ('GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4', Kocmi & Federmann, WMT 2023). No paper exists with the cited title ('Sirens: Detecting hallucinations in large language models using uncertainty') or the listed authors. Title, authors, and arXiv ID are mutually inconsistent with any real publication. This entry appears to be entirely fabricated/hallucinated and must be removed.
- SUSPICIOUS - farquhar2024detecting: The journal field cites arXiv:2406.15012, but that ID belongs to an unrelated paper ('Exact discovery is polynomial for certain sparse causal Bayesian networks', Rios/Moffa/Kuipers). The real Farquhar et al. semantic-entropy paper IS genuine but was published in Nature 2024 (DOI 10.1038/s41586-024-07421-0). Fix by replacing the wrong arXiv ID with the correct Nature DOI; the paper itself is real.
- SUSPICIOUS - single2023realwaste: Real title and year, but FABRICATED authors and venue. Bib lists authors 'Single, Nikita and Jain, Harsh and Jain, Priyanka' -- the real authors are Sam Single, Saeid Iranmanesh, Raad Raad (only surname 'Single' overlaps). Bib venue 'IEEE Access, vol. 11, pp. 112562-112584' is wrong; real venue is MDPI Information, vol. 14, no. 12, article 633, DOI 10.3390/info14120633. Volume and page range are also fabricated.
- SUSPICIOUS - rogers2020primer: Entry CONFLATES two distinct real papers. The cited title ('A primer on neural network models for natural language processing') is Yoav Goldberg's JAIR 2016 article (vol. 57, pp. 345-420), but the cited authors (Rogers, Kovaleva, Rumshisky) wrote a DIFFERENT paper, 'A Primer in BERTology' (TACL 2020, vol. 8, pp. 842-866). Volume=61 and pages=65-95 match NEITHER paper. No single real publication matches the entry as written.
- UNRESOLVED - card_data: The cited Kaggle URL (handle adityasoni04) returns a confirmed HTTP 404 and is not indexed by any search engine. No Kaggle user 'Aditya Soni' uses that handle. Multiple 'Playing Cards' datasets exist on Kaggle but all under different owners; none corroborates a 2020 dataset by this author at the cited handle. Source cannot be verified.
- CONFIRMED but WRONG AUTHORS - berant2013semantic: Real authors are Berant, Chou, Frostig, Liang. Bib lists 'Berant, Ceccaldi, Fader, Gabrilovich, Liang, Zettlemoyer' -- four fabricated/incorrect co-authors, and the real co-authors Chou and Frostig are missing. Title/year/venue/pages correct.
- CONFIRMED but FABRICATED VENUE CITATION - xu2017information: Bib claims 'IEEE Transactions on Information Theory, vol 63, no 9, pp 5948-5964, 2017'. The real paper was published at NeurIPS 2017 (pp 2525-2534) / arXiv:1705.07809; it was NOT in IEEE TIT vol 63 no 9. The volume/page citation is invented.
- CONFIRMED but GARBLED AUTHORS - chern2023factool: Multiple surnames corrupted ('Qian, Weizhe' should be 'Yuan, Weizhe'; 'Wei, Kehua' should be 'Feng, Kehua'; 'Zou, Chunting' should be 'Zhou, Chunting'; 'Graham, Neubig' malformed), and authors Junxian He and Pengfei Liu are missing.
- CONFIRMED but MALFORMED - robert1952fano: Author field 'Robert, M' is wrong (real author is Robert M. Fano, surname Fano), and 'Fano.' was erroneously prepended into the title. Correct title: 'Class Notes for MIT Course 6.574: Transmission of Information'. The source is real (Fano's inequality).
- CONFIRMED but TRUNCATED AUTHOR LIST - karras2017progressive: Bib lists only 'Karras, Tero'; the real paper has four authors (Karras, Aila, Laine, Lehtinen).
- CONFIRMED but IMPOSSIBLE YEAR - cover1999elements: Bib says 1999, but 'Elements of Information Theory' has only 1991 (1st ed.) and 2006 (2nd ed.) editions; there is no 1999 edition. Likely a citation-year error.
- MINOR/COSMETIC discrepancies on otherwise-confirmed entries: pagination off-by-one or differing convention (zhou2022rethinking, baldi2012autoencoders, raffel2020exploring); title word omitted (saxe2019information missing 'On the'); entry-type mismatches @article-vs-conference (liu2025detecting, locatello2019challenging, kim2018interpretability); 'and others' collapsing a final author (peng2023check, kim2018interpretability). None invalidate the source.
- Several confirmed sources are non-peer-reviewed by nature and correctly framed as such: drummond2006open (workshop slides), icmlface (Kaggle competition), ng2011sparse (lecture notes), robert1952fano (class notes), AIPlanet_DataSprint107_2024 (challenge page).

## Recommendations

- REMOVE or fully replace zhang2023sirens. As written it matches no real publication (title, authors, and arXiv ID are mutually inconsistent; the ID points to GEMBA-MQM). If a hallucination-detection-by-uncertainty citation is intended, find the actual paper and rebuild the entry from scratch; do not ship this entry.
- FIX farquhar2024detecting by replacing the incorrect journal/arXiv field (2406.15012) with the correct Nature 2024 citation and DOI 10.1038/s41586-024-07421-0. The paper is genuine, only the identifier is wrong.
- FIX single2023realwaste by correcting authors to Sam Single, Saeid Iranmanesh, Raad Raad and the venue to MDPI Information, vol. 14, no. 12, art. 633, DOI 10.3390/info14120633. The current authors, venue, volume, and pages are fabricated.
- RESOLVE rogers2020primer by splitting it: decide which paper is actually cited in the text. If the BERTology survey is meant, use Rogers/Kovaleva/Rumshisky, TACL 2020, vol. 8, pp. 842-866; if Goldberg's primer is meant, use Goldberg, JAIR 2016, vol. 57, pp. 345-420. The current merged entry is invalid either way.
- VERIFY-BY-HAND or replace card_data: locate the actual Kaggle dataset used (correct owner handle and a working URL) or substitute an equivalent dataset with a resolvable link; the cited URL is a dead 404 with no archived copy.
- CORRECT the author lists for berant2013semantic (Berant, Chou, Frostig, Liang), chern2023factool (de-garble surnames and add Junxian He, Pengfei Liu), and karras2017progressive (add Aila, Laine, Lehtinen).
- CORRECT the venue for xu2017information to NeurIPS 2017 (pp. 2525-2534) / arXiv:1705.07809 and delete the fabricated IEEE TIT vol/no/pages.
- CLEAN UP robert1952fano (author = Fano, Robert M.; remove 'Fano.' from the title) and cover1999elements (set year to 1991 or 2006 to match an actual edition).
- PROCESS: add a DOI or arXiv ID to every entry where one exists, and verify each identifier resolves to the cited title before submission. The two most dangerous defects (zhang2023sirens, farquhar2024detecting) were only catchable by resolving the identifier -- mechanical DOI/arXiv resolution would have caught both immediately.
- PROCESS: run an automated check that the identifier's title matches the bib title field, and prefer pulling full author lists from the canonical source rather than using 'and others' or 'et al.', which masked several of the author errors found here.
- PROCESS: the four serious defects cluster in the LLM-hallucination and dataset citations (zhang2023sirens, farquhar2024detecting, single2023realwaste, card_data) -- the newest additions to the bibliography. Give the most recently added references a second, manual verification pass, as these were the least vetted.

## Appendix — full per-entry results

| Key | Status | Identifier (verified) | Discrepancies |
|---|---|---|---|
| `achille2018emergence` | ✅ confirmed | https://jmlr.org/papers/v19/17-646.html ; arXiv:1706.01350 | — |
| `AIPlanet_DataSprint107_2024` | ✅ confirmed | https://aiplanet.com/challenges/325/butterfly_identification | Bib key says 2024 but year field says 2023 (minor internal inconsistency). Direct WebFetch of the URL returned 403, but a web search confirmed the challenge … |
| `alemi2017deep` | ✅ confirmed | arXiv:1612.00410 | — |
| `bakator2018deep` | ✅ confirmed | 10.3390/mti2030047 | — |
| `baldi2012autoencoders` | ✅ confirmed | https://proceedings.mlr.press/v27/baldi12a.html | Pages listed as 37-49; PMLR lists 37-50. Trivial off-by-one on end page. |
| `bang2025hallulens` | ✅ confirmed | arXiv:2504.17550 | — |
| `bartholomew1987latent` | ✅ confirmed | ISBN 0195206150 (Oxford University Press ed.) | Publisher: 1987 edition was originally Charles Griffin; an Oxford University Press edition (ISBN 0195206150) also exists for 1987, so 'Oxford University Pres… |
| `belghazi2018mutual` | ✅ confirmed | arXiv:1801.04062 | — |
| `ben2010theory` | ✅ confirmed | 10.1007/s10994-009-5152-4 | — |
| `berant2013semantic` | ✅ confirmed | ACL Anthology D13-1160; https://aclanthology.org/D13-1160/ | AUTHOR LIST WRONG. Real authors are Berant, Chou, Frostig, Liang. Bib lists 'Berant, Ceccaldi, Fader, Gabrilovich, Liang, Zettlemoyer' -- Ceccaldi, Fader, Ga… |
| `bossard14` | ✅ confirmed | DOI:10.1007/978-3-319-10599-4_29 | — |
| `brown2020language` | ✅ confirmed | arXiv:2005.14165 ; https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html | — |
| `burns2023discovering` | ✅ confirmed | arXiv:2212.03827 | Bib lists it as an arXiv article; it was also published at ICLR 2023. Minor venue note only. |
| `cao2020benchmark` | ✅ confirmed | arXiv:2007.04250 | none — arXiv id 2007.04250 resolves to exact title and all four authors |
| `card_data` | ❓ unresolved | https://www.kaggle.com/datasets/adityasoni04/playing-cards-dataset | Cited Kaggle URL (handle adityasoni04) returns a confirmed HTTP 404 and is not indexed/cached by any search engine. The Kaggle users named "Aditya Soni" that… |
| `chen2016infogan` | ✅ confirmed | arXiv:1606.03657 | — |
| `chen2020simclr` | ✅ confirmed | arXiv:2002.05709 ; https://proceedings.mlr.press/v119/chen20j.html | none -- title, all four authors, year (2020), venue (ICML/PMLR), pages 1597-1607 all match. |
| `chen2020simple` | ✅ confirmed | arXiv:2002.05709 | — |
| `chen2021exploring` | ✅ confirmed | arXiv:2011.10566 | — |
| `chen2023understanding` | ✅ confirmed | arXiv:2304.11327 | — |
| `chern2023factool` | ✅ confirmed | arXiv:2307.13528 | Author list in bib is garbled: 'Qian, Weizhe' should be 'Yuan, Weizhe'; 'Wei, Kehua' should be 'Feng, Kehua'; 'Zou, Chunting' should be 'Zhou, Chunting'; 'Gr… |
| `cifar10` | ✅ confirmed | https://www.cs.toronto.edu/~kriz/cifar.html | — |
| `cimpoi2014describing` | ✅ confirmed | 10.1109/CVPR.2014.461 ; arXiv:1311.3618 | none; pages 3606-3613 match CVPR 2014 proceedings (DTD dataset) |
| `cover1999elements` | ✅ confirmed | ISBN 9780471062592 (1st ed.); 10.1002/047174882X (2nd ed.) | Year mismatch: bib says 1999, but known editions are 1991 (1st) and 2006 (2nd). No 1999 edition; likely a citation-year error. Title, authors, and publisher … |
| `creswell2018generative` | ✅ confirmed | 10.1109/MSP.2017.2765202 (arXiv:1710.07035) | none (cited IEEE journal version; arXiv preprint 1710.07035 also exists) |
| `daxberger2019bayesian` | ✅ confirmed | arXiv:1912.05651 | — |
| `deng2009imagenet` | ✅ confirmed | IEEE Xplore doc 5206848 (pp. 248-255) | — |
| `devlin2018bert` | ✅ confirmed | arXiv:1810.04805 | bib cites arXiv preprint year 2018; conference publication is NAACL 2019. Acceptable preprint-vs-proceedings difference. Title and authors match exactly. |
| `donahue2016adversarial` | ✅ confirmed | arXiv:1605.09782 | bib year 2016 reflects arXiv preprint; the ICLR conference version is 2017. Off-by-one but acceptable. Title/authors/venue match exactly. |
| `dosovitskiy2020image` | ✅ confirmed | arXiv:2010.11929 | none — ViT paper; arXiv id 2010.11929 resolves to the exact title and matching author list |
| `drummond2006open` | ✅ confirmed | https://www.cs.man.ac.uk/~drummond/presentations/OWA.pdf | This is a workshop presentation/slides (University of Manchester, 2006) rather than a formal peer-reviewed paper, which matches the @inproceedings/eSI-worksh… |
| `du2024and` | ✅ confirmed | arXiv:2405.18635 | Cited as arXiv preprint; the paper was also accepted to ICML 2024. Minor venue note only. |
| `du2024does` | ✅ confirmed | arXiv:2402.03502 ; https://openreview.net/forum?id=jlEjB8MVGa | — |
| `dumoulin2016adversarially` | ✅ confirmed | arXiv:1606.00704 | bib year 2016 reflects arXiv preprint; the ICLR conference version is 2017. Off-by-one but acceptable. Full author list and title match exactly. |
| `ekim2024distribution` | ✅ confirmed | arXiv:2412.13394 | — |
| `esmaeilpour2022zero` | ✅ confirmed | 10.1609/aaai.v36i6.20610 (arXiv:2109.02748) | none (volume 36, number 6, pages 6568-6576 match exactly) |
| `fang2022out` | ✅ confirmed | arXiv:2210.14707 ; NeurIPS 2022 hash f0e91b1314fa5eabf1d7ef6d1561ecec | — |
| `farquhar2024detecting` | ⚠️ suspicious | DOI 10.1038/s41586-024-07421-0 (Nature). The cited arXiv:2406.15012 is WRONG. | The journal field cites arXiv:2406.15012, but that arXiv id belongs to a completely unrelated paper ("Exact discovery is polynomial for certain sparse causal… |
| `fashion` | ✅ confirmed | arXiv:1708.07747 | — |
| `federici2020learning` | ✅ confirmed | arXiv:2002.07017 | none (also appeared at ICLR 2020; bib lists it as arXiv preprint, acceptable) |
| `food` | ✅ confirmed | https://doi.org/10.1007/978-3-319-10599-4_29 | — |
| `fort2021exploring` | ✅ confirmed | arXiv:2106.03004 | — |
| `gao2021simcse` | ✅ confirmed | ACL Anthology 2021.emnlp-main.552 ; arXiv:2104.08821 | none -- title, all three authors, year (2021), venue (EMNLP 2021), pages 6894-6910 all match. |
| `gidaris2018unsupervised` | ✅ confirmed | arXiv:1803.07728 | none (also published at ICLR 2018, bib cites arXiv preprint which is fine) |
| `goodfellow2014generative` | ✅ confirmed | https://papers.nips.cc/paper/5423-generative-adversarial-nets | — |
| `guille2024cadet` | ✅ confirmed | arXiv:2210.01742 ; https://proceedings.neurips.cc/paper_files/paper/2023/hash/1700ad4e6252e8f2955909f96367b34d-Abstract-Conference.html | Bib lists year=2024; paper was published at NeurIPS 2023 (proceedings volume 36 corresponds to the 2023 conference). Minor year discrepancy; volume 36 is cor… |
| `he2016deep` | ✅ confirmed | arXiv:1512.03385 ; doi:10.1109/CVPR.2016.90 | none — landmark ResNet paper, title/authors/venue/pages/year all match |
| `he2020momentum` | ✅ confirmed | arXiv:1911.05722 | — |
| `he2022masked` | ✅ confirmed | arXiv:2111.06377 | — |
| `helber2019eurosat` | ✅ confirmed | arXiv:1709.00029 / IEEE Xplore doc 8736785 | — |
| `hendrycks2016baseline` | ✅ confirmed | arXiv:1610.02136 | Minor: published at ICLR 2017; bib cites 2016 arXiv preprint date. Acceptable. |
| `hendrycks2019using` | ✅ confirmed | arXiv:1906.12340 | — |
| `hewitt2019structural` | ✅ confirmed | aclanthology.org/N19-1419 | — |
| `higgins2017beta` | ✅ confirmed | https://openreview.net/forum?id=Sy2fzU9gl | — |
| `hinton2006reducing` | ✅ confirmed | 10.1126/science.1127647 | — |
| `hinton2015distilling` | ✅ confirmed | arXiv:1503.02531 | — |
| `hjelm2019learning` | ✅ confirmed | arXiv:1808.06670 | — |
| `ho2020denoising` | ✅ confirmed | arXiv:2006.11239 ; https://papers.nips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html | — |
| `houlsby2019parameter` | ✅ confirmed | arXiv:1902.00751 / proceedings.mlr.press/v97/houlsby19a | — |
| `huang2020survey` | ✅ confirmed | 10.1016/j.cosrev.2020.100270 (arXiv:1812.08342) | — |
| `huang2021mos` | ✅ confirmed | arXiv:2105.01879 | — |
| `hyvarinen2000independent` | ✅ confirmed | 10.1016/S0893-6080(00)00026-5 | — |
| `icmlface` | ✅ confirmed | https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge | This is a Kaggle competition (origin of the FER-2013 dataset), not a peer-reviewed paper. The URL, title, year, and the author list correspond to Kaggle's of… |
| `ILSVRC15` | ✅ confirmed | 10.1007/s11263-015-0816-y ; arXiv:1409.0575 | none; DOI, volume 115, number 3, pages 211-252, year, journal all match |
| `jordan1999introduction` | ✅ confirmed | 10.1023/A:1007665907178 | — |
| `joshi2017triviaqa` | ✅ confirmed | https://aclanthology.org/P17-1147/ ; arXiv:1705.03551 | — |
| `kafunah2023out` | ✅ confirmed | https://ieeexplore.ieee.org/document/10332173/ | — |
| `karras2017progressive` | ✅ confirmed | arXiv:1710.10196 | Bib author list contains only 'Karras, Tero' but the real paper has four authors: Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen. Incomplete author li… |
| `katz2022training` | ✅ confirmed | arXiv:2202.03299 ; https://proceedings.mlr.press/v162/katz-samuels22a.html | — |
| `khalid2022rodd` | ✅ confirmed | arXiv:2204.02553 | — |
| `khosla2020supervised` | ✅ confirmed | arXiv:2004.11362 | — |
| `kim2018interpretability` | ✅ confirmed | arXiv:1711.11279 / proceedings.mlr.press/v80/kim18d.html | Entry type is @article but it is conference proceedings (ICML/PMLR); otherwise matches. Authors list ends with 'and others' (real list adds Rory Sayres). |
| `kim2021wafer` | ✅ confirmed | 10.1016/j.microrel.2021.114157 | — |
| `kingma2014auto` | ✅ confirmed | arXiv:1312.6114 | — |
| `KrauseStarkDengFei-Fei_3DRR2013` | ✅ confirmed | https://openaccess.thecvf.com/content_iccv_workshops_2013/W19/papers/Krause_3D_Object_Representations_2013_ICCV_paper.pdf | — |
| `krizhevsky2009learning` | ✅ confirmed | https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf | — |
| `krizhevsky2012imagenet` | ✅ confirmed | https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks | — |
| `kwiatkowski2019natural` | ✅ confirmed | 10.1162/tacl_a_00276 | — |
| `lakshminarayanan2017simple` | ✅ confirmed | arXiv:1612.01474 ; https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html | — |
| `lecun1998gradient` | ✅ confirmed | https://doi.org/10.1109/5.726791 | — |
| `lee2018simple` | ✅ confirmed | arXiv:1807.03888 ; NeurIPS paper 7947 | — |
| `li2023halueval` | ✅ confirmed | arXiv:2305.11747 | — |
| `liang2017enhancing` | ✅ confirmed | arXiv:1706.02690 | Minor: published at ICLR 2018; bib cites 2017 arXiv preprint. Acceptable. |
| `lin2021truthfulqa` | ✅ confirmed | arXiv:2109.07958 ; ACL Anthology 2022.acl-long.229 | Bib lists venue as 'Proceedings of the 59th Annual Meeting of the ACL and 11th IJCNLP (Volume 1: Long Papers)' (i.e., ACL-IJCNLP 2021) with year 2021. The pa… |
| `lin2022truthfulqa` | ✅ confirmed | aclanthology.org/2022.acl-long.229 ; arXiv:2109.07958 | none — title, authors, venue, pages (3214-3252) and year all match |
| `linsker1988self` | ✅ confirmed | 10.1109/2.36 | — |
| `liu2020energy` | ✅ confirmed | arXiv:2010.03759 | — |
| `liu2023unsupervised` | ✅ confirmed | arXiv:2302.10326 ; PMLR proceedings.mlr.press/v202/liu23bd.html | — |
| `liu2025detecting` | ✅ confirmed | arXiv:2311.01479 | Entry type is @article but it is a CVPR 2025 conference paper (minor); arXiv preprint dates to 2023, published at CVPR 2025. |
| `locatello2019challenging` | ✅ confirmed | arXiv:1811.12359 ; https://proceedings.mlr.press/v97/locatello19a.html | Minor: bib uses @article with journal='International conference on machine learning'; it is actually ICML 2019 conference proceedings (PMLR). Title/authors/y… |
| `manakul2023selfcheckgpt` | ✅ confirmed | arXiv:2303.08896 | — |
| `mazurowski2019deep` | ✅ confirmed | 10.1002/jmri.26534 ; PMID 30575178 | — |
| `mcallester1999pac` | ✅ confirmed | 10.1145/307400.307435 | — |
| `mccloskey1989catastrophic` | ✅ confirmed | https://www.sciencedirect.com/science/article/abs/pii/S0079742108605368 | — |
| `mikolov2013efficient` | ✅ confirmed | arXiv:1301.3781 | — |
| `mohseni2020self` | ✅ confirmed | DOI:10.1609/aaai.v34i04.5966 | — |
| `mollahosseini2017affectnet` | ✅ confirmed | arXiv:1708.03985 / DOI:10.1109/TAFFC.2017.2740923 | Title/authors/venue/volume/pages match. Bib year 2017 reflects the arXiv preprint / early-access date; the TAC journal issue (vol 10, no 1) is dated 2019. Mi… |
| `narayanaswamy2023exploring` | ✅ confirmed | doi:10.1109/ICCVW60793.2023.00493 ; openaccess.thecvf.com ICCV2023W/UnCV | Minor venue precision: it is an ICCV 2023 Workshop (ICCVW, UnCV workshop) paper, but the bib lists the main 'Proceedings of the IEEE/CVF International Confer… |
| `netzer2011reading` | ✅ confirmed | http://ai.stanford.edu/~twangcat/papers/nips2011_housenumbers.pdf | none (bib omits venue; this is the well-known SVHN NIPS workshop paper) |
| `ng2011sparse` | ✅ confirmed | https://web.stanford.edu/class/cs294a/sparseAutoencoder_2011new.pdf | — |
| `olah2020zoom` | ✅ confirmed | DOI:10.23915/distill.00024.001 ; https://distill.pub/2020/circuits/zoom-in/ | — |
| `oord2018representation` | ✅ confirmed | arXiv:1807.03748 | Minor: bib uses @inproceedings with booktitle set to the arXiv id; this is an arXiv preprint (CPC), not formal proceedings. Title/authors/year correct. |
| `oquab2023dinov2` | ✅ confirmed | arXiv:2304.07193 | — |
| `pearson1901liii` | ✅ confirmed | 10.1080/14786440109462720 | — |
| `peng2005feature` | ✅ confirmed | 10.1109/TPAMI.2005.159 | Published title includes a colon ('Mutual Information: Criteria of...') vs bib ('mutual information criteria of...'); trivial punctuation/phrasing difference… |
| `peng2023check` | ✅ confirmed | arXiv:2302.12813 | Bib uses 'and others' which collapses the final author (Jianfeng Gao). Otherwise matches. |
| `pennington2014glove` | ✅ confirmed | ACL Anthology D14-1162 | — |
| `plant` | ✅ confirmed | arXiv:1511.08060 | none (WebFetch displayed a truncated title without the 'through machine learning and crowdsourcing' suffix, but it is the same paper/eprint) |
| `pmlr-v235-xu24ae` | ✅ confirmed | https://proceedings.mlr.press/v235/xu24ae.html | — |
| `poole2019variational` | ✅ confirmed | arXiv:1905.06922 ; https://proceedings.mlr.press/v97/poole19a.html | none -- title, all five authors, year (2019), venue (ICML/PMLR), pages 5171-5180 all match. |
| `radford2018improving` | ✅ confirmed | https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf | — |
| `radford2021learning` | ✅ confirmed | https://proceedings.mlr.press/v139/radford21a.html (arXiv:2103.00020) | none (CLIP paper; pages 8748-8763 match) |
| `raffel2020exploring` | ✅ confirmed | arXiv:1910.10683 ; https://www.jmlr.org/papers/v21/20-074.html | Minor: bib lists pages 5485-5551; JMLR/arXiv page the article as 21(140):1-67. Page numbers reflect the collated-volume convention sometimes used. Title/auth… |
| `ramanagopal2018failing` | ✅ confirmed | 10.1109/LRA.2018.2857402 (IEEE doc 8412512) ; arXiv:1707.00051 | none; volume 3, number 4, pages 3860-3867, IEEE RA-L, 2018 all match |
| `rezende2014stochastic` | ✅ confirmed | https://proceedings.mlr.press/v32/rezende14.html ; arXiv:1401.4082 | — |
| `rifai2011contractive` | ✅ confirmed | https://dblp.uni-trier.de/rec/conf/icml/RifaiVMGB11.html | — |
| `robert1952fano` | ✅ confirmed | Commonly cited as R. M. Fano, Class Notes for MIT Course 6.574, 1952 (basis of Fano's inequality, later expanded into the 1961 MIT Press book 'Transmission of Information') | The bib entry is badly malformed: the author field is 'Robert, M' but the real author is Robert M. Fano (surname Fano), and the surname 'Fano.' was erroneous… |
| `rock_data` | ✅ confirmed | DOI:10.34740/kaggle/ds/1293628 (resolves to https://www.kaggle.com/ds/1293628 ; dataset at https://www.kaggle.com/datasets/salmaneunus/rock-classification) | none material; bib lists author surname 'Nahin, Rakibul' while the full name is Rakibul Alam Nahin (same person). |
| `rogers2020primer` | ⚠️ suspicious | 10.1162/tacl_a_00349 / arXiv:2002.12327 (Rogers et al.); arXiv:1510.00726 / JAIR view/11030 (Goldberg) | The entry conflates two distinct real papers. The cited TITLE ("A primer on neural network models for natural language processing") is Yoav Goldberg's JAIR 2… |
| `runge2019detecting` | ✅ confirmed | 10.1126/sciadv.aau4996 | none (arXiv preprint 1702.07007 has slightly shorter title 'Detecting causal associations...'; published Science Advances version matches bib exactly). |
| `saadati2024out` | ✅ confirmed | doi:10.34133/plantphenomics.0170 ; arXiv:2305.01823 | — |
| `saxe2019information` | ✅ confirmed | 10.1088/1742-5468/ab3985 | Bib title omits the leading word 'On the'; real title is 'On the information bottleneck theory of deep learning'. Authors, journal, volume/number/pages (1240… |
| `sehwag2021ssd` | ✅ confirmed | arXiv:2103.12051 | none (paper also accepted at ICLR 2021; bib lists arXiv preprint) |
| `selvaraju2017grad` | ✅ confirmed | arXiv:1610.02391 | — |
| `shannon1948mathematical` | ✅ confirmed | 10.1002/j.1538-7305.1948.tb01338.x | — |
| `sharma2018conceptual` | ✅ confirmed | ACL Anthology P18-1238 (10.18653/v1/P18-1238) | none (pages 2556-2565 match) |
| `shwartz2017opening` | ✅ confirmed | arXiv:1703.00810 | — |
| `shwartz2023compress` | ✅ confirmed | arXiv:2304.09355 | — |
| `single2023realwaste` | ⚠️ suspicious | 10.3390/info14120633 | Title and year match a REAL paper, but authors and venue are fabricated. Bib lists authors 'Single, Nikita and Jain, Harsh and Jain, Priyanka' — the real aut… |
| `song2020score` | ✅ confirmed | arXiv:2011.13456 ; https://openreview.net/forum?id=PxTIG12RRHS | none (bib key says 2020 but year field correctly says 2021; ICLR 2021 is correct) |
| `sun2021react` | ✅ confirmed | arXiv:2111.12797 | — |
| `sun2022out` | ✅ confirmed | arXiv:2204.06507 ; https://proceedings.mlr.press/v162/sun22d.html | — |
| `tack2020csi` | ✅ confirmed | https://proceedings.neurips.cc/paper/2020/hash/8965f76632d7672e7d3cf29c87ecaa0c-Abstract.html | — |
| `tenney2019bert` | ✅ confirmed | aclanthology.org/P19-1452 / arXiv:1905.05950 | — |
| `thorne2018fever` | ✅ confirmed | ACL Anthology N18-1074 ; arXiv:1803.05355 | none -- title, all four authors, year (2018), venue (NAACL-HLT 2018), and pages 809-819 all match. |
| `tipping1999probabilistic` | ✅ confirmed | 10.1111/1467-9868.00196 | — |
| `tishby2000information` | ✅ confirmed | arXiv:physics/0004057 | — |
| `tishby2015deep` | ✅ confirmed | DOI:10.1109/ITW.2015.7133169 | — |
| `vaswani2017attention` | ✅ confirmed | arXiv:1706.03762 | none — Transformer paper, all 8 authors and venue/volume/year match |
| `vincent2008extracting` | ✅ confirmed | 10.1145/1390156.1390294 | — |
| `voita2019analyzing` | ✅ confirmed | aclanthology.org/P19-1580 / arXiv:1905.09418 | — |
| `voita2019information` | ✅ confirmed | aclanthology.org/2020.emnlp-main.14 / arXiv:2003.12298 | Minor: bibkey says 2019 but the year field correctly says 2020 (EMNLP 2020). Key naming is harmless. |
| `vyas2018out` | ✅ confirmed | arXiv:1809.03576 | — |
| `wang2021deep` | ✅ confirmed | 10.1016/j.neucom.2020.10.081 | — |
| `wang2023clipn` | ✅ confirmed | arXiv:2308.12213 ; CVF open access ICCV 2023 | — |
| `xiao2020likelihood` | ✅ confirmed | arXiv:2003.02977 ; NeurIPS proceedings hash eddea82ad2755b24c4e168c5fc2ebd40 | none; volume 33 (NeurIPS 2020) matches |
| `xu2017information` | ✅ confirmed | arXiv:1705.07809 | VENUE MISMATCH: bib lists 'IEEE Transactions on Information Theory, vol 63, no 9, pp 5948-5964, 2017'. The real paper was published at NeurIPS 2017 (pp 2525-… |
| `xuscaling` | ✅ confirmed | arXiv:2310.00227 ; OpenReview id=RDSTjtnqCg | — |
| `yang2021generalized` | ✅ confirmed | arXiv:2110.11334 | — |
| `yang2021image` | ✅ confirmed | 10.1016/j.renene.2020.08.125 (ScienceDirect pii S0960148120313707) | — |
| `yang2022openood` | ✅ confirmed | arXiv:2210.07242 ; https://proceedings.neurips.cc/paper_files/paper/2022/hash/d201587e3a84fc4761eadc743e9b3f35-Abstract-Datasets_and_Benchmarks.html | — |
| `yang2023medmnist` | ✅ confirmed | https://doi.org/10.1038/s41597-022-01721-8 ; arXiv:2110.14795 | — |
| `yangcan` | ✅ confirmed | arXiv:2504.14704 ; OpenReview id=falBlwUsIH | — |
| `yoga_data` | ✅ confirmed | https://www.kaggle.com/datasets/sumanthvrao/yoga-poses | — |
| `yu2015lsun` | ✅ confirmed | arXiv:1506.03365 | none; arXiv id 1506.03365 matches |
| `zhang2021out` | ✅ confirmed | DOI:10.1007/978-3-030-87735-4_10 | — |
| `zhang2021understanding` | ✅ confirmed | arXiv:2107.06908 / PMLR v139 zhang21g | — |
| `zhang2023openood` | ✅ confirmed | arXiv:2306.09301 | — |
| `zhang2023sirens` | ⚠️ suspicious | arXiv:2310.13988 (resolves to a DIFFERENT paper: GEMBA-MQM) | Cited arXiv ID 2310.13988 resolves to "GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4" (Kocmi & Federmann, WMT 2023), an unrelated machine-t… |
| `zhou2017places` | ✅ confirmed | https://doi.org/10.1109/TPAMI.2017.2723009 | Bib lists year 2017; the TPAMI volume 40(6) issue was published June 2018 (online first 2017). Minor year discrepancy; all other fields (volume, number, page… |
| `zhou2022rethinking` | ✅ confirmed | arXiv:2203.02194 | Page numbers: bib lists 7379--7387; one source cites 7369-7377. Minor pagination discrepancy only; title/author/venue/year all match. |
