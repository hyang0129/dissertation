# MMLU Rebuttal Stash

**Not compiled into the PDF.** Pre-written one-paste-away response if a reviewer asks "why no MMLU?"

## Framing

MMLU is omitted from the main paper because our substring-match label degenerates on single-letter MCQ answers, making the gold labels unreliable for all eight methods we evaluate.

## The labeling failure mode

Our hallucination label is computed by substring-matching the model's response against the gold answer. For MMLU, the gold answer is a single option letter — "A", "B", "C", or "D" — and the response is free-form. A single-letter substring matches anywhere in the response: inside an unrelated word ("**A**ttention is the answer"), inside an explanation that mentions other options ("The answer is not option **A**"), or in degenerate decoder outputs. The match also misses correct responses that name the option content instead of the letter ("the answer is photosynthesis" vs. gold "C"). The net effect is bidirectional label flipping with no clear sign, so every method's MMLU AUROC is measuring its agreement with a noisy label rather than its agreement with whether the model actually hallucinated. This pathology does not apply to the five paper datasets, where the gold answer is a free-form span (typically multi-token) and substring-match is the dominant labeling convention in the probing literature.

## Numbers anyway

For transparency, here are MMLU AUROC values across all eight methods that have MMLU cells in `results/results_table.csv` (mean across 5 seeds where applicable; output-space scalars are deterministic single values). Method/metric mapping matches `results/draft_headline_table.md` (knn_auroc for ours; seq_logprob_auroc for LogProb; mean_entropy_auroc for Token Entropy; p_true_auroc_best for P(true); plain `auroc` for the probes).

| Method | Llama-3.1-8B | Qwen3-8B |
|---|---|---|
| LogProb (seq) | 0.595 | 0.622 |
| Token Entropy | 0.589 | 0.627 |
| P(true) | 0.660 | 0.682 |
| Linear Probe | 0.783 | 0.828 |
| SAPLMA | 0.640 | 0.684 |
| LLMsKnow Probe | 0.801 | 0.792 |
| ACT-ViT | 0.662 | 0.677 |
| **Contrastive+Recon (ours)** | **0.812** | **0.833** |

Source rows: dataset id `mmlu_memmap` (Llama) and `mmlu_qwen3_memmap` (Qwen3) in `results/results_table.csv`, filtered to `status=complete`. Means computed from the per-seed rows; see `results/results_table.csv` directly.

## Observation

Ours is in fact the top-AUROC method on both models even with the broken label, and our margin over the next-best activation-space probe (LLMsKnow on Llama, Linear Probe on Qwen) is consistent with the §5 main-paper pattern. **ACT-ViT under-performs every other activation-space probe on MMLU** (0.66/0.68 vs. others at 0.78–0.83), which is consistent with the broken-label hypothesis: a method that reads finer-grained token-position activation structure (ACT-ViT operates on the full `(L × N × D)` tensor) is more sensitive to noise in the supervision signal than probes that pool over positions.

## What a fair MMLU eval would need

Either (a) LLM-judge labels with a documented prompt, or (b) option-letter exact-match with format normalization — a regex such as `\b[ABCD]\b` against the response, anchored to typical answer-prefix positions ("The answer is X", "Option X", etc.) and with explicit handling for "the answer is not X" negations. Both are out of scope for this paper; we chose silent omission over a half-fix that would still leave the label noisy.

---

Source data: `results/results_table.csv`. This file is intentionally outside `paper/sections/` and does not appear in the compiled PDF.
