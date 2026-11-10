# Six-experiment results summary

All values are copied from the recovered experiment registry and presentation. ROC-AUC and PR-AUC are validation metrics unless explicitly marked as experience-subset scores.

## Experiment 1 — Stage 1 baseline

| Evaluation entry | ROC-AUC | PR-AUC |
|---|---:|---:|
| Training-run best validation result (epoch 5) | 0.9072 | 0.7396 |
| Independent validation evaluation | 0.8947 | 0.7273 |

These are two separate recorded evaluation entries. Their difference is not reconciled in the recovered artifacts.

## Experiment 2 — EWC fine-tuning

| Configuration | Best epoch | ROC-AUC | PR-AUC |
|---|---:|---:|---:|
| EWC, lambda = 10 | 3 | 0.8919 | 0.6935 |

## Experiment 3 — Experience-subset retention

These scores were calculated on the experience subsets, not an independent held-out test set.

| Model state | Experience 1 ROC-AUC | Experience 1 PR-AUC | Experience 2 ROC-AUC | Experience 2 PR-AUC |
|---|---:|---:|---:|---:|
| Before experience 2 | 0.9983 | 0.9923 | 0.9991 | 0.9948 |
| After experience 2 with EWC | 0.9961 | 0.9829 | 1.0000 | 1.0000 |
| After experience 2 without EWC | 0.9986 | 0.9923 | 1.0000 | 1.0000 |

The recorded Experience 1 ROC-AUC change was a drop of 0.0021804 with EWC and a tiny increase of 0.0003489 without EWC. This is not sufficient evidence of generalization or robust forgetting prevention.

## Experiment 4 — Matched EWC versus no-EWC comparison

The recovered notes state that initialization, split, and three training epochs were matched; lambda = 5 for the EWC run.

| Configuration | ROC-AUC | PR-AUC |
|---|---:|---:|
| No EWC | 0.8895 | 0.6887 |
| EWC (lambda = 5) | 0.8815 | 0.6716 |

No EWC scored higher on both reported validation metrics in this comparison.

## Experiment 5 — EWC penalty-strength sweep

| EWC penalty | ROC-AUC | PR-AUC |
|---:|---:|---:|
| lambda = 1 | 0.8693 | 0.6658 |
| lambda = 50 | 0.8540 | 0.6674 |
| lambda = 100 | 0.8561 | 0.6186 |

The highest ROC-AUC occurred at lambda = 1; the highest PR-AUC occurred at lambda = 50. A stronger penalty did not consistently improve validation performance.

## Experiment 6 — Learning-rate sweep (without EWC)

| Learning rate | ROC-AUC | PR-AUC |
|---|---:|---:|
| 1e-5 | 0.8957 | 0.6958 |
| 1e-4 | 0.8891 | 0.7020 |
| 3e-4 | 0.8839 | 0.6696 |

The highest ROC-AUC occurred at 1e-5; the highest PR-AUC occurred at 1e-4.

## Overall interpretation

- EWC did not improve validation metrics in the reported matched comparison.
- Learning-rate selection affected validation results.
- Near-perfect experience-subset scores must not be reported as held-out test performance.
- The two experiences were arbitrary halves of the same training cohort, not distinct tasks or modalities.
- The current experiments do not establish that EWC prevents catastrophic forgetting across distinct tasks.
