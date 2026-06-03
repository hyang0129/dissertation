# Citation Validation Report — main.tex

Each citation used in `eccv2026/main.tex` is investigated below.
**Status legend:** ✅ Confirmed real | ⚠️ Real paper, metadata errors in .bib | ❌ Not found

---

## ✅ Yang2022openood
**Context:** Cited as an example of multi-domain OOD benchmarks (CIFAR-10/100, ImageNet variants) and again in Related Work as a strong-performing multi-domain benchmark.
**Bib entry:** Jingkang Yang et al., "OpenOOD: Benchmarking Generalized Out-of-Distribution Detection," NeurIPS 2022.
**Search:** Searched "Yang 2022 OpenOOD Benchmarking Generalized Out-of-Distribution Detection NeurIPS"
**Found:** Yes — NeurIPS 2022 Datasets & Benchmarks track. Available at https://arxiv.org/abs/2210.07242 and https://proceedings.neurips.cc/paper_files/paper/2022/hash/d201587e3a84fc4761eadc743e9b3f35-Abstract-Datasets_and_Benchmarks.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Yang2024survey
**Context:** Cited alongside Yang2022openood as a survey establishing the multi-domain OOD benchmark context.
**Bib entry:** Jingkang Yang, Kaiyang Zhou, Yixuan Li, Ziwei Liu, "Generalized Out-of-Distribution Detection: A Survey," IJCV 2024, vol. 132, pp. 4132–4163.
**Search:** Searched "Yang 2024 Generalized Out-of-Distribution Detection Survey IJCV"
**Found:** Yes — IJCV 2024. Available at https://arxiv.org/abs/2110.11334 and https://dl.acm.org/doi/10.1007/s11263-024-02117-4
**Verdict:** Confirmed real. Note: search found page range 5635–5662 in December 2024 issue; bib lists 4132–4163. Minor page number discrepancy, but paper and venue are real.

---

## ✅ Oquab2024dinov2
**Context:** Cited multiple times as the frozen multi-domain teacher (DINOv2 ViT-S/14) used in TGT, and as a key reference for teacher-student extensions to self-supervised pre-training.
**Bib entry:** Maxime Oquab et al., "DINOv2: Learning Robust Visual Features without Supervision," TMLR 2024.
**Search:** Searched "Oquab 2024 DINOv2 Learning Robust Visual Features without Supervision TMLR"
**Found:** Yes — TMLR 2024. Available at https://arxiv.org/abs/2304.07193 and https://openreview.net/forum?id=a68SUt6zFt
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Hendrycks2017msp
**Context:** Cited in Related Work as the MSP (Maximum Softmax Probability) baseline; also cited in Theory section as a logit-based score that fails under DSC.
**Bib entry:** Dan Hendrycks and Kevin Gimpel, "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks," ICLR 2017.
**Search:** Searched "Hendrycks Gimpel 2017 Baseline Detecting Misclassified Out-of-Distribution Examples ICLR"
**Found:** Yes — ICLR 2017. Available at https://arxiv.org/abs/1610.02136 and https://openreview.net/forum?id=Hkg4TI9xl
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Liang2018odin
**Context:** Cited in Related Work under "Logit- and softmax-based methods" as ODIN (temperature scaling + input perturbation).
**Bib entry:** Shiyu Liang, Yixuan Li, R. Srikant, "Enhancing the Reliability of Out-of-Distribution Image Detection in Neural Networks," ICLR 2018.
**Search:** Searched "Liang Li Srikant 2018 ODIN Enhancing Reliability Out-of-Distribution Image Detection ICLR"
**Found:** Yes — ICLR 2018. Available at https://arxiv.org/abs/1706.02690 and https://openreview.net/forum?id=H1VGkIxRZ
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Liu2020energy
**Context:** Cited in Related Work as the Energy score method (log-sum-exp of logits); also cited in Theory section as a logit-based score that fails under DSC, and listed as a scorer in experiments.
**Bib entry:** Weitang Liu, Xiaoyun Wang, John D. Owens, Yixuan Li, "Energy-based Out-of-Distribution Detection," NeurIPS 2020.
**Search:** Searched "Liu 2020 Energy-based Out-of-Distribution Detection NeurIPS Weitang Liu"
**Found:** Yes — NeurIPS 2020. Available at https://arxiv.org/abs/2010.03759 and https://proceedings.neurips.cc/paper/2020/hash/f5496252609c43eb8a3d147ab9b9c006-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Sun2021react
**Context:** Cited in Related Work as the ReAct method (activation truncation before computing logits).
**Bib entry:** Yiyou Sun, Chuan Guo, Yixuan Li, "ReAct: Out-of-Distribution Detection With Rectified Activations," NeurIPS 2021.
**Search:** Searched "Sun 2021 ReAct Out-of-Distribution Detection Rectified Activations NeurIPS Yiyou Sun"
**Found:** Yes — NeurIPS 2021. Available at https://arxiv.org/abs/2111.12797 and https://proceedings.neurips.cc/paper/2021/hash/01894d6f048493d2cacde3c579c315a3-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Sun2022dice
**Context:** Cited in Related Work as the DICE method (weight sparsification before computing logits).
**Bib entry:** Yiyou Sun, Yixuan Li, "DICE: Leveraging Sparsification for Out-of-Distribution Detection," ECCV 2022.
**Search:** Searched "Sun Li 2022 DICE Leveraging Sparsification Out-of-Distribution Detection ECCV"
**Found:** Yes — ECCV 2022. Available at https://arxiv.org/abs/2111.09805 and https://link.springer.com/chapter/10.1007/978-3-031-20053-3_40
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Lee2018maha
**Context:** Cited in Related Work as the Mahalanobis Distance Score (MDS); also cited multiple times in the Theory section when discussing distance-based score failure.
**Bib entry:** Kimin Lee, Kibok Lee, Honglak Lee, Jinwoo Shin, "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks," NeurIPS 2018.
**Search:** Searched "Lee 2018 Mahalanobis Simple Unified Framework Detecting Out-of-Distribution NeurIPS Kimin Lee"
**Found:** Yes — NeurIPS 2018. Available at https://arxiv.org/abs/1807.03888 and https://proceedings.neurips.cc/paper/2018/hash/abdeb6f575ac5c6676b747bca8d09cc2-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Sun2022knn
**Context:** Cited in Related Work as the KNN distance-based OOD detector; also cited in the Theory section discussing distance-score failure under DSC.
**Bib entry:** Yiyou Sun, Yifei Ming, Xiaojin Zhu, Yixuan Li, "Out-of-Distribution Detection with Deep Nearest Neighbors," ICML 2022.
**Search:** Searched "Sun 2022 Out-of-Distribution Detection Deep Nearest Neighbors ICML kNN Yiyou Sun"
**Found:** Yes — ICML 2022 (Spotlight). Available at https://arxiv.org/abs/2204.06507 and https://proceedings.mlr.press/v162/sun22d/sun22d.pdf
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Wang2022vim
**Context:** Cited in Related Work as the ViM (Virtual-logit Matching) method; also used as a scorer key in Experiments. The bib key `Wang2022vim` is also reused for SCALE (a separate method), which is a minor bib inconsistency in the paper.
**Bib entry:** Haoqi Wang, Zhizhong Li, Litong Feng, Wayne Zhang, "ViM: Out-of-Distribution with Virtual-logit Matching," CVPR 2022.
**Search:** Searched "Wang 2022 ViM Virtual-logit Matching Out-of-Distribution CVPR Haoqi Wang"
**Found:** Yes — CVPR 2022. Available at https://arxiv.org/abs/2203.10807 and https://openaccess.thecvf.com/content/CVPR2022/html/Wang_ViM_Out-of-Distribution_With_Virtual-Logit_Matching_CVPR_2022_paper.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Sehwag2021ssd
**Context:** Cited in Related Work as SSD+ which combines self-supervised features with Mahalanobis scoring.
**Bib entry:** Vikash Sehwag, Mung Chiang, Prateek Mittal, "SSD: A Unified Framework for Self-Supervised Outlier Detection," ICLR 2021.
**Search:** Searched "Sehwag 2021 SSD Unified Framework Self-Supervised Outlier Detection ICLR"
**Found:** Yes — ICLR 2021. Available at https://arxiv.org/abs/2103.12051 and https://openreview.net/forum?id=v5gjXpmR8J
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Tack2020csi
**Context:** Cited in Related Work as one of the contrastive representation methods that improve OOD separation.
**Bib entry:** Jihoon Tack, Sangwoo Mo, Jongheon Jeong, Jinwoo Shin, "CSI: Novelty Detection via Contrastive Learning on Distributionally Shifted Instances," NeurIPS 2020.
**Search:** Searched "Tack 2020 CSI Novelty Detection Contrastive Learning Distributionally Shifted Instances NeurIPS"
**Found:** Yes — NeurIPS 2020. Available at https://arxiv.org/abs/2007.08176 and https://proceedings.neurips.cc/paper/2020/hash/8965f76632d7672e7d3cf29c87ecaa0c-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Winkens2020contrastive
**Context:** Cited in Related Work as one of the contrastive approaches improving OOD separation.
**Bib entry:** Jim Winkens et al. (13 authors including Olaf Ronneberger), "Contrastive Training for Improved Out-of-Distribution Detection," arXiv preprint 2007.05566, 2020.
**Search:** Searched "Winkens 2020 Contrastive Training Improved Out-of-Distribution Detection arXiv"
**Found:** Yes — arXiv 2020 preprint. Available at https://arxiv.org/abs/2007.05566
**Verdict:** Confirmed real. Note: The bib lists this as `@inproceedings` with `booktitle = {arXiv preprint arXiv:2007.05566}`, which is unusual formatting — it is technically an arXiv preprint, not a conference paper. The paper is real but the bib type/venue fields are irregular.

---

## ✅ Khosla2020supcon
**Context:** Cited in Related Work for contrastive representations improving OOD separation; also cited in Experiments as the SupCon baseline backbone.
**Bib entry:** Prannay Khosla et al., "Supervised Contrastive Learning," NeurIPS 2020.
**Search:** Searched "Khosla 2020 Supervised Contrastive Learning NeurIPS"
**Found:** Yes — NeurIPS 2020. Available at https://arxiv.org/abs/2004.11362 and https://proceedings.neurips.cc/paper/2020/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Cao2020medood
**Context:** Cited in Related Work as an example of single-domain regime (medical imaging, remote sensing, industrial inspection) where standard OOD methods degrade.
**Bib entry:** Tianshi Cao, Chinwei Huang, David Yu-Tung Hui, Joseph Paul Cohen, "A Benchmark of Medical Out of Distribution Detection," NeurIPS Workshop on Machine Learning for Health, 2020.
**Search:** Searched "Cao Huang Hui Cohen 2020 Benchmark Medical Out of Distribution Detection NeurIPS Workshop"
**Found:** Yes — arXiv 2020 (arXiv:2007.04250), subsequently published in the Journal of Machine Learning for Biomedical Imaging. Available at https://arxiv.org/abs/2007.04250
**Verdict:** Confirmed real. The paper was presented at a NeurIPS 2020 workshop (ML for Health), consistent with the bib entry.

---

## ✅ Berger2021medood
**Context:** Cited alongside Cao2020medood for single-domain performance degradation (medical/specialized domains).
**Bib entry:** Christoph Berger, Magdalini Paschali, Ben Glocker, Konstantinos Kamnitsas, "Confidence-based Out-of-Distribution Detection: A Comparative Study and Analysis," arXiv preprint arXiv:2107.02568, 2021.
**Search:** Searched "Berger Paschali Glocker Kamnitsas 2021 Confidence Out-of-Distribution Detection Comparative Study arXiv 2107.02568"
**Found:** Yes — arXiv 2021, also published in Springer UNSURE/PIPPI 2021 proceedings. Available at https://arxiv.org/abs/2107.02568 and https://link.springer.com/chapter/10.1007/978-3-030-87735-4_12
**Verdict:** Confirmed real. Authors and arXiv ID match exactly.

---

## ✅ Papyan2020nc
**Context:** Cited several times as the foundational neural collapse paper (ETF geometry); cited in Theory as the basis for the connection between DSC and neural collapse.
**Bib entry:** Vardan Papyan, X. Y. Han, David L. Donoho, "Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training," PNAS 2020, vol. 117, no. 40, pp. 24652–24663.
**Search:** Searched "Papyan Han Donoho 2020 Prevalence Neural Collapse Terminal Phase Deep Learning PNAS"
**Found:** Yes — PNAS 2020. Available at https://arxiv.org/abs/2008.08186 and https://www.pnas.org/doi/10.1073/pnas.2015509117
**Verdict:** Confirmed real. Authors, title, venue, volume, and page numbers match exactly.

---

## ✅ Zhu2021nc
**Context:** Cited alongside Papyan2020nc confirming ETF geometry as a global minimizer of cross-entropy loss; also cited in Theory for context of the DSC/neural-collapse connection.
**Bib entry:** Zhihui Zhu, Tianyu Ding, Jinxin Zhou, Xiao Li, Qing Qu, "A Geometric Analysis of Neural Collapse with Unconstrained Features," NeurIPS 2021.
**Search:** Searched "Zhu Ding Zhou 2021 Geometric Analysis Neural Collapse Unconstrained Features NeurIPS"
**Found:** Yes — NeurIPS 2021. Available at https://arxiv.org/abs/2105.02375 and https://proceedings.neurips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html
**Verdict:** Confirmed real. Note: the bib only lists 5 authors; the actual paper has 7 (also Chong You, Jeremias Sulam). Minor author-list truncation, otherwise correct.

---

## ⚠️ Haas2022ncood — METADATA ERRORS
**Context:** Cited in Related Work as the paper showing that neural-collapse-adjacent representations harm OOD separability and that L2 normalization partially mitigates this.
**Bib entry:**
```
author = {Julia Haas and William Yolland and Tim G. J. Rudner},
booktitle = {ICML Workshop on Pre-training},
year = {2022}
```
**Search:** Searched "Haas Yolland Rudner Neural Collapse Out-of-Distribution 2022 ICML Workshop" and "Haas Yolland Rudner Tim Rudner Neural Collapse"
**Found:** Paper arXiv:2209.08378 exists, titled "Linking Neural Collapse and L2 Normalization with Improved Out-of-Distribution Detection in Deep Neural Networks."
**Issue:** The actual paper's authors are **Jarrod Haas, William Yolland, and Bernhard T. Rabus** (or Bernhard Rabus), published in **TMLR (Transactions on Machine Learning Research)**. The bib entry has:
- Wrong first author: "Julia Haas" → should be "Jarrod Haas"
- Wrong third author: "Tim G. J. Rudner" → should be "Bernhard T. Rabus" (Tim Rudner is a real researcher but not an author of this paper)
- Wrong venue: "ICML Workshop on Pre-training" → paper published in TMLR
**Verdict:** The paper itself is real and the content described is accurate, but the author names and venue in the .bib are incorrect/hallucinated.

---

## ✅ Liu2023nci
**Context:** Cited in Related Work as the Neural Collapse Inspired (NCI) detector that scores OOD inputs by alignment with the predicted class weight vector; also listed as a scorer in Experiments.
**Bib entry:** Litian Liu, Yao Qin, "Detecting Out-of-Distribution Through the Lens of Neural Collapse," CVPR, year = 2025.
**Search:** Searched "Liu Qin Detecting Out-of-Distribution Through Lens Neural Collapse CVPR 2025"
**Found:** Yes — CVPR 2025. Available at https://arxiv.org/abs/2311.01479 and https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Detecting_Out-of-Distribution_Through_the_Lens_of_Neural_Collapse_CVPR_2025_paper.pdf and https://github.com/litianliu/NCI-OOD
**Verdict:** Confirmed real. Authors, title, and venue (CVPR 2025) match exactly. The bib key says "Liu2023nci" reflecting the arXiv submission year (2023) while the published venue is CVPR 2025 — this is a common practice.

---

## ✅ Jing2022rank
**Context:** Cited in Related Work as the dimensional collapse paper; also cited in Theory (Sec. 3.2) as the result that L2-regularized models discard task-irrelevant directions.
**Bib entry:** Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian, "Understanding Dimensional Collapse in Contrastive Self-Supervised Learning," ICLR 2022.
**Search:** Searched "Jing Vincent LeCun Tian 2022 Understanding Dimensional Collapse Contrastive Self-Supervised Learning ICLR"
**Found:** Yes — ICLR 2022. Available at https://arxiv.org/abs/2110.09348 and https://iclr.cc/virtual/2022/poster/6792
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ⚠️ Galanti2022collapse — AUTHOR METADATA HALLUCINATED
**Context:** Cited in Related Work for the result that neural collapse persists across transfer tasks and shapes fine-tuning dynamics.
**Bib entry:**
```
author = {Tomer Galanti and Andrés Magyar and Lilach Eden and Michal Irani},
booktitle = ICLR,
year = {2022}
```
**Search:** Searched "Galanti Magyar Eden Irani Neural Collapse transfer learning ICLR 2022" and "Galanti Neural Collapse transfer learning ICLR 2022 arxiv 2112.15121"
**Found:** Paper arXiv:2112.15121 exists, titled "On the Role of Neural Collapse in Transfer Learning," ICLR 2022.
**Issue:** The actual authors are **Tomer Galanti, András György, and Marcus Hutter**. The bib entry lists completely different people ("Andrés Magyar," "Lilach Eden," and "Michal Irani") who are not authors of this paper. Only the first author (Tomer Galanti) is correct. The venue (ICLR 2022) is correct.
**Verdict:** The paper is real and the venue is correct, but 3 of the 4 listed author names are hallucinated/incorrect. This is a significant metadata error.

---

## ✅ Hinton2015kd
**Context:** Cited in Related Work as the introduction of knowledge distillation (student matching teacher's softened output distribution).
**Bib entry:** Geoffrey Hinton, Oriol Vinyals, Jeff Dean, "Distilling the Knowledge in a Neural Network," arXiv preprint arXiv:1503.02531, 2015.
**Search:** Searched "Hinton Vinyals Dean 2015 Distilling Knowledge Neural Network arXiv 1503.02531"
**Found:** Yes — arXiv 2015 (NIPS 2014 Deep Learning Workshop). Available at https://arxiv.org/abs/1503.02531
**Verdict:** Confirmed real. Authors, title, and arXiv ID match exactly.

---

## ✅ Touvron2021deit
**Context:** Cited in Related Work as an example of teacher-student transfer extended to vision transformers.
**Bib entry:** Hugo Touvron et al., "Training data-efficient image transformers & distillation through attention," ICML 2021.
**Search:** Searched "Touvron 2021 Training data-efficient image transformers distillation attention ICML DeiT"
**Found:** Yes — ICML 2021. Available at https://arxiv.org/abs/2012.12877 and https://proceedings.mlr.press/v139/touvron21a.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Caron2021dino
**Context:** Cited in Related Work as an example of teacher-student transfer extended to self-supervised pre-training.
**Bib entry:** Mathilde Caron et al., "Emerging Properties in Self-Supervised Vision Transformers," ICCV 2021.
**Search:** Searched "Caron 2021 DINO Emerging Properties Self-Supervised Vision Transformers ICCV"
**Found:** Yes — ICCV 2021. Available at https://arxiv.org/abs/2104.14294 and https://openaccess.thecvf.com/content/ICCV2021/html/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Yang2025pskd — REPLACED Li2023kdood
**Context:** Cited in Related Work (Sec. 2.3, Knowledge Distillation and Teacher-Student Frameworks) as using KD losses to sharpen OOD detection in the student.
**Action:** Original `Li2023kdood` ("KD-OOD: Knowledge Distillation for Handling Out-of-Distribution Data," AAAI 2023) could not be found after 3+ searches and is likely hallucinated. Replaced with Yang and Xu, ICML 2025.
**Bib entry:** Yang Yang and Haonan Xu, "Strengthen Out-of-Distribution Detection Capability with Progressive Self-Knowledge Distillation," ICML 2025.
**Found:** Yes — ICML 2025. Available at https://icml.cc/virtual/2025/poster/44372 and https://openreview.net/forum?id=iA8lD3oG5G
**Verdict:** Confirmed real. Uses progressive self-knowledge distillation (multi-level KD from past model states) to improve OOD detection scores while preserving in-distribution accuracy. Top-tier venue (ICML).

---

## ✅ Fort2021pretrained
**Context:** Cited in Related Work (Sec. 2.4, Fine-Tuning and OOD Detection) as showing that pre-trained features are strong OOD baselines but fine-tuning can degrade this advantage.
**Bib entry:** Stanislav Fort, Jie Ren, Balaji Lakshminarayanan, "Exploring the Limits of Out-of-Distribution Detection in Vision and NLP," NeurIPS 2021.
**Search:** Searched "Fort Ren Lakshminarayanan 2021 Exploring Limits Out-of-Distribution Detection Vision NLP NeurIPS"
**Found:** Yes — NeurIPS 2021. Available at https://arxiv.org/abs/2106.03004 and https://proceedings.neurips.cc/paper/2021/hash/3941c4358616274ac2436eacf67fae05-Abstract.html
**Verdict:** Confirmed real. Authors, title, and venue match exactly.

---

## ✅ Kumar2022lp — REPLACED Ming2022delving
**Context:** Cited in Related Work (Sec. 2.4) as showing full fine-tuning can distort pretrained features and hurt out-of-distribution performance.
**Action:** The original `Ming2022delving` entry had hallucinated metadata (wrong title, wrong authors, paper was about CLIP/VLMs not ViTs). Replaced with Kumar et al. ICLR 2022, which directly supports the claim made in the text.
**Bib entry:** Ananya Kumar, Aditi Raghunathan, Robbie Jones, Tengyu Ma, Percy Liang, "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution," ICLR 2022.
**Found:** Yes — ICLR 2022. Available at https://arxiv.org/abs/2202.10054 and https://openreview.net/forum?id=UYneFzXSJWh
**Verdict:** Confirmed real. Shows fine-tuning gets +2% ID accuracy but −7% OOD accuracy vs linear probing across vision benchmarks.

---

## ✅ yangcan
**Context:** Cited in the Theory section (Sec. 3.3) as evidence that a multi-domain teacher (DINOv2) fails on in-domain OOD because self-supervised features carry no class-discriminative structure.
**Bib entry:** Hong Yang, Qi Yu, Travis Desell, "Can We Ignore Labels in Out of Distribution Detection?", ICLR 2025.
**Search:** Searched "Yang Yu Desell Can We Ignore Labels in Out of Distribution Detection ICLR 2025"
**Found:** Yes — ICLR 2025. Available at https://arxiv.org/abs/2504.14704 and https://openreview.net/forum?id=falBlwUsIH
**Verdict:** Confirmed real. Authors, title, and venue match exactly. (Note: this is likely a self-citation by the paper's author.)

---

## ✅ yang2023medmnist
**Context:** Cited in Experiments (Sec. 4.1) as "the standard OpenOOD MedMNIST-style OOD evaluation protocol."
**Bib entry:** Jiancheng Yang, Rui Shi, Donglai Wei et al., "MedMNIST v2 - a large-scale lightweight benchmark for 2D and 3D biomedical image classification," Scientific Data, vol. 10, no. 1, p. 41, 2023.
**Search:** Searched "yang2023medmnist MedMNIST v2 large-scale lightweight benchmark biomedical image classification Scientific Data 2023"
**Found:** Yes — Scientific Data 2023. Available at https://www.nature.com/articles/s41597-022-01721-8 and https://arxiv.org/abs/2110.14795
**Verdict:** Confirmed real. Authors, title, venue, volume, and page number all match exactly.

---

## Summary Table

| Key | Status | Issue |
|---|---|---|
| Yang2022openood | ✅ Real | — |
| Yang2024survey | ✅ Real | Minor page-number discrepancy |
| Oquab2024dinov2 | ✅ Real | — |
| Hendrycks2017msp | ✅ Real | — |
| Liang2018odin | ✅ Real | — |
| Liu2020energy | ✅ Real | — |
| Sun2021react | ✅ Real | — |
| Sun2022dice | ✅ Real | — |
| Lee2018maha | ✅ Real | — |
| Sun2022knn | ✅ Real | — |
| Wang2022vim | ✅ Real | — |
| Sehwag2021ssd | ✅ Real | — |
| Tack2020csi | ✅ Real | — |
| Winkens2020contrastive | ✅ Real | Bib uses `@inproceedings` for arXiv preprint |
| Khosla2020supcon | ✅ Real | — |
| Cao2020medood | ✅ Real | — |
| Berger2021medood | ✅ Real | — |
| Papyan2020nc | ✅ Real | — |
| Zhu2021nc | ✅ Real | Minor author truncation (5/7 authors) |
| **Haas2022ncood** | ⚠️ Metadata errors | Wrong first author (Julia→Jarrod), wrong 3rd author (Rudner→Rabus), wrong venue (ICML Workshop→TMLR) |
| Liu2023nci | ✅ Real | Key year (2023) reflects arXiv; venue is CVPR 2025 |
| Jing2022rank | ✅ Real | — |
| **Galanti2022collapse** | ⚠️ Author hallucination | Only first author (Galanti) correct; 3 other names fabricated |
| Hinton2015kd | ✅ Real | — |
| Touvron2021deit | ✅ Real | — |
| Caron2021dino | ✅ Real | — |
| **Yang2025pskd** (replaced Li2023kdood) | ✅ Real | Li2023kdood was not found/likely hallucinated; replaced with Yang & Xu ICML 2025 |
| Fort2021pretrained | ✅ Real | — |
| **Kumar2022lp** (replaced Ming2022delving) | ✅ Real | Ming had hallucinated metadata; replaced with Kumar ICLR 2022 |
| yangcan | ✅ Real | — |
| yang2023medmnist | ✅ Real | — |
