# Resilient Graph Architectures for Continual Learning

A research project exploring graph neural networks for biomedical prediction using RNA-derived and clinical features, with a six-experiment study of Elastic Weight Consolidation (EWC), experience-subset retention, EWC penalty strength, and learning-rate sensitivity.

## Repository status

This is a research/results archive. Full training reproduction is incomplete. The recovered project materials include aggregate experiment results, configuration and input checks, and stage integration points. The exact original Stage1GNN and GraphLayer definitions, all six original training cells, checkpoints, and patient-level data were not recovered. The stage scripts are therefore documented integration placeholders, not runnable training implementations. See docs/REPRODUCIBILITY.md.

## Research question

Can a graph neural network learn from a second training experience while retaining what it learned from the first, and does EWC improve that behaviour on the validation split?

The six stages recorded in the project are:
1. Stage 1 baseline training.
2. EWC fine-tuning on a second experience.
3. Experience-subset retention and forgetting analysis.
4. Matched EWC versus no-EWC comparison.
5. EWC penalty-strength sweep (lambda 1, 50, 100).
6. Learning-rate sweep (1e-5, 1e-4, 3e-4).

The two experiences were arbitrary halves of the training cohort, not separate biological tasks. This limits the strength of conclusions about continual learning.

## Dataset and evaluation setup

The experiment registry describes 789 aligned patient records, split into 631 training and 158 validation patients. Labels were imbalanced:

| Split | Negative | Positive | Total |
|---|---:|---:|---:|
| Training | 546 | 85 | 631 |
| Validation | 137 | 21 | 158 |
| Total | 683 | 106 | 789 |

The aligned feature set is described as containing 17,940 gene-level features in each RNA, mutation, and copy-number array, plus 2,672 encoded clinical features. The Stage 1 experiment is described as an RNA-plus-clinical GNN. Do not assume every modality was used in that model unless the exact original model code confirms it.

Primary reported metrics are ROC-AUC and PR-AUC. PR-AUC is especially relevant because positive labels are underrepresented.

## Key findings

- Independent Stage 1 validation evaluation: ROC-AUC 0.8947 and PR-AUC 0.7273.
- Stage 2 EWC (lambda 10): ROC-AUC 0.8919 and PR-AUC 0.6935.
- In the matched Experiment 4 comparison, no EWC scored 0.8895 / 0.6887, while EWC (lambda 5) scored 0.8815 / 0.6716 (ROC-AUC / PR-AUC).
- Across Experiments 5–6, the best validation ROC-AUC was 0.8957 at learning rate 1e-5; the best validation PR-AUC was 0.7020 at learning rate 1e-4.
- Experience-subset scores near 1.0 are not independent held-out generalization results.

The reported results do not show that EWC improved validation performance in the matched comparison. They do not establish prevention of catastrophic forgetting across distinct tasks.

## Results-only quick start

Python 3.9+ is suitable for the results-only utilities.

1. Install dependencies with: pip install -r requirements.txt
2. Inspect the results with: python run_pipeline.py --results-only
3. Print selected stored metrics with: python evaluate.py

These commands read the aggregate registry in results/metrics.json. They do not train a model. The --run-training option exits intentionally until the exact original model and training cells are restored.

## Repository structure

- config.py and data_loader.py: expected paths and input-file checks.
- model.py: interface note; exact original model definition is missing.
- stage1_train.py through stage6_learning_rate.py: integration placeholders.
- run_pipeline.py and evaluate.py: results-only utilities.
- results/metrics.json and results/comparison.csv: aggregate experiment metrics.
- docs/EXPERIMENTS.md and docs/REPRODUCIBILITY.md: experiment record and reproduction limitations.

## Data privacy

Raw RNA, mutation, copy-number, and clinical records, patient identifiers, embeddings, predictions, and model checkpoints are not included. These may contain sensitive genomic or health information and should not be published in a public repository. The results directory contains aggregate experiment metrics only.

## Scope

This is an exploratory academic research project, not a clinical diagnostic system and not validated for clinical decision-making. Stronger claims require repeated-seed experiments, an independent final test set, a prediction-time clinical-feature audit, and meaningful sequential tasks.
