# PhD Dissertation: Label Blindness in Unlabeled Out-of-Distribution Detection

This repository contains the LaTeX source code for my PhD dissertation, which includes the integration of my ICLR 2025 paper "Can We Ignore Labels in Out-of-Distribution Detection?" as Chapter 4.

## Overview

The dissertation explores the theoretical foundations and practical implications of label blindness in unlabeled out-of-distribution (OOD) detection methods. The main contribution is the Label Blindness Theorem, which proves that self-supervised and unsupervised OOD detection methods are guaranteed to fail when their learning objectives are independent of the features relevant for label prediction.

## Structure

- **Chapter 1**: Introduction
- **Chapter 2**: Background and Literature Review
- **Chapter 3**: [Placeholder for additional research]
- **Chapter 4**: Label Blindness in Unlabeled OOD Detection (ICLR 2025 paper)
- **Chapter 5-8**: [Placeholders for future chapters]
- **Appendix A**: Theoretical Proofs for Label Blindness

## Key Contributions

### Chapter 4: Label Blindness Theory

1. **Label Blindness Theorem**: Theoretical proof that unlabeled OOD detection methods fail when the surrogate learning task is independent of label-relevant features.

2. **Adjacent OOD Benchmark**: Novel evaluation methodology that tests OOD detection when there is significant feature overlap between in-distribution and out-of-distribution data.

3. **Experimental Validation**: Comprehensive experiments showing that existing unlabeled OOD methods perform poorly on Adjacent OOD tasks.

### Appendix A: Mathematical Proofs

Complete mathematical proofs including:
- Properties of mutual information and entropy
- Strict Label Blindness in the Minimal Sufficient Statistic
- Independence of Filtered Distributions
- Unavoidable Risk of Overlapping OOD Data

## Compilation

To compile the dissertation:

```bash
pdflatex Sample_Thesis_main.tex
bibtex Sample_Thesis_main
pdflatex Sample_Thesis_main.tex
pdflatex Sample_Thesis_main.tex
```

## Files

- `Sample_Thesis_main.tex`: Main dissertation file
- `AppendixA.tex`: Theoretical proofs appendix
- `Bibliography.bib`: Complete bibliography
- `images/`: Figures and experimental results (PNG, JPG, PDF)
- `ICLR_2025_SSL_OOD__Camera_Ready_/`: Original ICLR paper source

## Citation

If you use this work, please cite:

```bibtex
@inproceedings{yang2025label,
  title={Can We Ignore Labels in Out-of-Distribution Detection?},
  author={Yang, Hong and Yu, Qi and Desell, Travis},
  booktitle={International Conference on Learning Representations},
  year={2025}
}
```

## License

This work is licensed under [appropriate license - to be determined].

## Contact

Hong Yang - [email] - [institution]

## Notes 

Add citations to references 
Add ICLR 2025 paper to label blindness 
Make a clear distinction between completed and proposed work 
