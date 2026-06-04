# references.bib — corrections (2026-06-04)

Bib-gate proposal. Each block below is a **verified** replacement for a flawed
entry found by the audit ([../reports/reference_audit.md](../reports/reference_audit.md)).
Every correction was checked against the cited canonical source (URL given).

> **STATUS: APPLIED 2026-06-04.** The 8 metadata corrections (§A `farquhar2024detecting`,
> `single2023realwaste`; §B all) were applied to `references.bib`. The 3 ⛔ DECISION
> entries were **REMOVED** per author decision (not replaced): `zhang2023sirens`,
> `rogers2020primer`, `card_data`. A separate **orphaned `huang2021mos` fragment**
> (an entry body with no `@inproceedings{...,` opening, pre-existing corruption that
> would have broken BibTeX) was also removed. Result: 161 → 158 entries.
> If `card_data` (a dataset) is needed when Ch.5 is drafted, add a verified entry then.

---

## A. Fabricated / wrong-identifier — must change

### ⛔ DECISION — `zhang2023sirens`
The current entry is **fully fabricated** (no such paper; arXiv id points to GEMBA-MQM).
It was likely confabulated from the genuine *Siren's Song* hallucination **survey**.
**Decide:** (a) replace with the real survey below, or (b) delete the entry if a
survey is not what the text needs. Replacement is verified — but confirm the
survey is the citation you actually want.

```bibtex
@article{zhang2023sirens,
  title={Siren's Song in the {AI} Ocean: A Survey on Hallucination in Large Language Models},
  author={Zhang, Yue and Li, Yafu and Cui, Leyang and Cai, Deng and Liu, Lemao and Fu, Tingchen and Huang, Xinting and Zhao, Enbo and Zhang, Yu and Xu, Chen and Chen, Yulong and Wang, Longyue and Luu, Anh Tuan and Bi, Wei and Shi, Freda and Shi, Shuming},
  journal={arXiv preprint arXiv:2309.01219},
  year={2023}
}
```
Verified: https://arxiv.org/abs/2309.01219 (title + full 16-author list confirmed).

### `farquhar2024detecting` — real paper, wrong identifier → fix to Nature
```bibtex
@article{farquhar2024detecting,
  title={Detecting hallucinations in large language models using semantic entropy},
  author={Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},
  journal={Nature},
  volume={630},
  number={8017},
  pages={625--630},
  year={2024},
  publisher={Nature Publishing Group},
  doi={10.1038/s41586-024-07421-0}
}
```
Verified: Nature 630(8017):625–630, 2024, DOI 10.1038/s41586-024-07421-0
(https://www.nature.com/articles/s41586-024-07421-0). Removes the wrong
`arXiv:2406.15012` (which is an unrelated causal-Bayesian-networks paper).

### `single2023realwaste` — fabricated authors + venue → fix
```bibtex
@article{single2023realwaste,
  title={RealWaste: A Novel Real-Life Data Set for Landfill Waste Classification Using Deep Learning},
  author={Single, Sam and Iranmanesh, Saeid and Raad, Raad},
  journal={Information},
  volume={14},
  number={12},
  pages={633},
  year={2023},
  publisher={MDPI},
  doi={10.3390/info14120633}
}
```
Verified: *Information* 14(12):633, 2023, DOI 10.3390/info14120633
(https://www.mdpi.com/2078-2489/14/12/633). Was: authors "Nikita Single, Harsh
Jain, Priyanka Jain" + venue "IEEE Access 11:112562–112584" — all fabricated.

### ⛔ DECISION — `rogers2020primer`
Current entry **conflates two real papers**. The key + author list match
*A Primer in BERTology*; the title field is Goldberg's unrelated *A Primer on
Neural Network Models for NLP* (JAIR 2016). **Decide which you actually cite.**
Default below assumes BERTology (matches the bibkey and authors).

```bibtex
@article{rogers2020primer,
  title={A Primer in {BERT}ology: What We Know About How {BERT} Works},
  author={Rogers, Anna and Kovaleva, Olga and Rumshisky, Anna},
  journal={Transactions of the Association for Computational Linguistics},
  volume={8},
  pages={842--866},
  year={2020},
  doi={10.1162/tacl_a_00349}
}
```
Verified: TACL 8:842–866, 2020 (https://aclanthology.org/2020.tacl-1.54/).
*Alternative if Goldberg's primer is intended:* Goldberg, JAIR 57:345–420, 2016
(arXiv:1510.00726) — would also warrant renaming the key to `goldberg2016primer`.

---

## B. Confirmed papers with wrong fields — fix metadata

### `berant2013semantic` — wrong author list
```bibtex
@inproceedings{berant2013semantic,
  title={Semantic Parsing on {F}reebase from Question-Answer Pairs},
  author={Berant, Jonathan and Chou, Andrew and Frostig, Roy and Liang, Percy},
  booktitle={Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  pages={1533--1544},
  year={2013}
}
```
Verified: https://aclanthology.org/D13-1160/. Was: "Berant, Ceccaldi, Fader,
Gabrilovich, Liang, Zettlemoyer" — Ceccaldi/Fader/Gabrilovich/Zettlemoyer are
wrong; Chou and Frostig were missing.

### `chern2023factool` — garbled author surnames + missing authors
```bibtex
@article{chern2023factool,
  title={FacTool: Factuality Detection in Generative {AI} -- A Tool Augmented Framework for Multi-Task and Multi-Domain Scenarios},
  author={Chern, I-Chun and Chern, Steffi and Chen, Shiqi and Yuan, Weizhe and Feng, Kehua and Zhou, Chunting and He, Junxian and Neubig, Graham and Liu, Pengfei},
  journal={arXiv preprint arXiv:2307.13528},
  year={2023}
}
```
Verified: https://arxiv.org/abs/2307.13528. Fixes Yuan/Feng/Zhou/Neubig and adds
Junxian He, Pengfei Liu.

### `karras2017progressive` — truncated author list
```bibtex
@article{karras2017progressive,
  title={Progressive Growing of {GAN}s for Improved Quality, Stability, and Variation},
  author={Karras, Tero and Aila, Timo and Laine, Samuli and Lehtinen, Jaakko},
  journal={arXiv preprint arXiv:1710.10196},
  year={2017}
}
```
Verified: https://arxiv.org/abs/1710.10196 (ICLR 2018). Adds Aila, Laine, Lehtinen.

### `xu2017information` — fabricated IEEE TIT venue → NeurIPS 2017
```bibtex
@inproceedings{xu2017information,
  title={Information-theoretic analysis of generalization capability of learning algorithms},
  author={Xu, Aolin and Raginsky, Maxim},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2017},
  note={arXiv:1705.07809}
}
```
Verified: NeurIPS 2017 (https://arxiv.org/abs/1705.07809, "accepted to NIPS
2017"). Removes the invented "IEEE Trans. Inf. Theory 63(9):5948–5964". Exact
proceedings page range left off rather than risk a second wrong number — add if
you want it from the NeurIPS proceedings page.

### `robert1952fano` — malformed author/title
```bibtex
@misc{robert1952fano,
  title={Class Notes for {MIT} Course 6.574: Transmission of Information},
  author={Fano, Robert M.},
  howpublished={MIT, Cambridge, MA},
  year={1952}
}
```
Real author is **Fano, Robert M.** (was "Robert, M"); "Fano." was wrongly
prepended into the title. (Source of Fano's inequality; class notes, not indexed
with a DOI.)

### `cover1999elements` — impossible edition year
```bibtex
@book{cover1999elements,
  title={Elements of Information Theory},
  author={Cover, Thomas M. and Thomas, Joy A.},
  edition={2nd},
  year={2006},
  publisher={Wiley-Interscience}
}
```
No 1999 edition exists — editions are 1991 (1st) and 2006 (2nd). Set to 2006 2nd
ed. (Bibkey left as-is to avoid churn; rename to `cover2006elements` only if you
prefer.)

---

## C. ⛔ DECISION — `card_data` (unresolved, needs the real source)
The cited Kaggle URL (`adityasoni04/playing-cards-dataset`) is a **dead 404** and
no Kaggle user with that handle exists. I can't draft a correct entry without
knowing the dataset you actually used. **Tell me which playing-cards dataset the
experiments used** (owner + working URL) and I'll build the entry. A corroborated
candidate, *if* it matches your data, is `gpiosenka/cards-image-datasetclassification`
— but do **not** assume; the dataset identity affects reproducibility.

---

## How to apply
On your approval I will edit `references.bib` in place with the blocks above
(skipping the ⛔ DECISION items until you choose), and we can then add
`check_refs.py` (Layer 2) so the build fails if any identifier ever again
resolves to the wrong title.
