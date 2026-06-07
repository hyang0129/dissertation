# references.bib — Ch.6 staging candidates (2026-06-06)

The **7 genuinely-new** entries Ch.6 needs that are *not* in `references.bib` and
were *not* in the source paper's own `.bib` either (the source carried them as
"pending-approval candidates" — datasets, models, and one baseline). Per the bib
gate these are **proposals**: all 7 web-verified 2026-06-06 (arXiv/ACL/venue
confirmed); apply via the gate (the PreToolUse hook ask-prompts on the
`references.bib` edit).

This is **separate** from `bib_staging.md` (2026-06-04, the source's own 16 Ch.6
refs — already applied) and from the §3b remaps below (no `.bib` change — those
are key substitutions made in prose at draft time).

**Legend:** ✅ web-verified 2026-06-06.

---

## A. New entries to insert (7) — ✅ all verified

### Models (2)
- ✅ **`grattafiori2024llama3`** — Grattafiori et al., *The Llama 3 Herd of Models*,
  arXiv:2407.21783, 2024. (Primary eval model: Llama-3.1-8B-Instruct.)
- ✅ **`yang2025qwen3`** — An Yang et al., *Qwen3 Technical Report*,
  arXiv:2505.09388, 2025. (Second eval model: Qwen3-8B.)

### Datasets (4)
- ✅ **`yang2018hotpotqa`** — Yang et al., *HotpotQA: A Dataset for Diverse,
  Explainable Multi-hop Question Answering*, EMNLP 2018 (arXiv:1809.09600).
- ✅ **`mallen2023popqa`** — Mallen et al., *When Not to Trust Language Models:
  Investigating Effectiveness of Parametric and Non-Parametric Memories* (PopQA),
  ACL 2023 (arXiv:2212.10511).
- ✅ **`welbl2017sciq`** — Welbl, Liu, Gardner, *Crowdsourcing Multiple Choice
  Science Questions* (SciQ), W-NUT @ EMNLP 2017 (arXiv:1707.06209).
- ✅ **`dunn2017searchqa`** — Dunn et al., *SearchQA: A New Q&A Dataset Augmented
  with Context from a Search Engine*, arXiv:1704.05179, 2017.

### Baseline (1) — **source guess corrected**
- ✅ **`orgad2024llmsknow`** — Orgad, Toker, Gekhman, Reichart, Szpektor, Kotek,
  Belinkov, *LLMs Know More Than They Show: On the Intrinsic Representation of LLM
  Hallucinations*, ICLR 2025 (arXiv:2410.02707). Repo `technion-cs-nlp/LLMsKnow`
  — confirms the baseline name **"LLMsKnow"** (= `llmsknow_probe` in
  `hallu_headline.csv`). **Resolves source open item I-5**: the source markdown
  guessed *"Slobodkin et al."* / `[UNKNOWN — verify]` — that was **wrong**. First
  author is Hadas Orgad; senior author is Yonatan Belinkov (same as the existing
  `belinkov2019analysis`).

### BibTeX (ready to paste)
```bibtex
@article{grattafiori2024llama3,
  title={The Llama 3 Herd of Models},
  author={Grattafiori, Aaron and others},
  journal={arXiv preprint arXiv:2407.21783},
  year={2024}
}

@article{yang2025qwen3,
  title={Qwen3 Technical Report},
  author={Yang, An and others},
  journal={arXiv preprint arXiv:2505.09388},
  year={2025}
}

@inproceedings{yang2018hotpotqa,
  title={HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering},
  author={Yang, Zhilin and Qi, Peng and Zhang, Saizheng and Bengio, Yoshua and Cohen, William W and Salakhutdinov, Ruslan and Manning, Christopher D},
  booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2018}
}

@inproceedings{mallen2023popqa,
  title={When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories},
  author={Mallen, Alex and Asai, Akari and Zhong, Victor and Das, Rajarshi and Khashabi, Daniel and Hajishirzi, Hannaneh},
  booktitle={Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2023}
}

@article{welbl2017sciq,
  title={Crowdsourcing Multiple Choice Science Questions},
  author={Welbl, Johannes and Liu, Nelson F and Gardner, Matt},
  journal={arXiv preprint arXiv:1707.06209},
  year={2017}
}

@article{dunn2017searchqa,
  title={SearchQA: A New Q\&A Dataset Augmented with Context from a Search Engine},
  author={Dunn, Matthew and Sagun, Levent and Higgins, Mike and Guney, V Ugur and Cirik, Volkan and Cho, Kyunghyun},
  journal={arXiv preprint arXiv:1704.05179},
  year={2017}
}

@inproceedings{orgad2024llmsknow,
  title={LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations},
  author={Orgad, Hadas and Toker, Michael and Gekhman, Zorik and Reichart, Roi and Szpektor, Idan and Kotek, Hadas and Belinkov, Yonatan},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2025}
}
```

---

## B. Remaps — NO `.bib` change (5)

Same paper already in the gated bib under a different key. Apply as **key
substitution in Ch.6 prose** at draft time; do **not** add a second entry.

| Source-paper key | Gated key (use this) |
|---|---|
| `khosla2020supcon` | `khosla2020supervised` |
| `oord2018cpc` | `oord2018representation` |
| `hjelm2019deepinfomax` | `hjelm2019learning` |
| `farquhar2024semantic` | `farquhar2024detecting` |
| `kwiatkowski2019nq` | `kwiatkowski2019natural` |

---

## C. Already present — no action (21)
`alain2017understanding, azaria2023internal, bang2025hallulens,
barshalom2025actvit, belinkov2019analysis, chen2020simclr, gao2021simcse,
ji2022survey, kadavath2022language, kossen2024semantic, li2023iti,
manakul2023selfcheckgpt, marks2024geometry, min2023factscore,
poole2019variational, sun2020codir, suresh2025clap, tian2020crd, tishby2015deep,
wang2021understanding, zhang2022cds, zhang2025icr` (incl. the CRD/CoDIR/CDS
novelty-footnote trio and ACT-ViT/CLAP/ICR).

---

## Apply checklist
- [ ] Insert the 7 BibTeX blocks above into `references.bib` (gate hook will prompt).
- [ ] On insert, bump any entry count noted in `bib_staging.md` (192 → 199).
- [ ] Sweep Ch.6 prose for the §B remaps (when §6.x drafts).
- [ ] Update `outlines/06_hallucination_detection.md` §3c: LLMsKnow key resolved to
      `orgad2024llmsknow` (was the unconfirmed `slobodkin2024llmsknow`).
