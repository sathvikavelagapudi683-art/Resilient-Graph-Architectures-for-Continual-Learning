# Reproducibility status and limitations

## What is present

- Aggregate six-experiment metrics (results/metrics.json).
- A compact validation comparison (results/comparison.csv).
- Configuration and expected input-file checks.
- Results-only scripts that read the stored registry.
- Stage 1–6 integration-point files that identify where exact original notebook cells must be restored.

## What is missing from the recovered bundle

The recovered project materials do not include the original Colab definitions of Stage1GNN and GraphLayer, the exact training cells for all stages, or the original checkpoints. The files model.py and stage1_train.py through stage6_learning_rate.py are therefore not complete training implementations. They are explicitly marked integration placeholders and must not be described as runnable experiment code.

The original input files expected by the experiment configuration are also not included:

- aligned_rna_mut_cnv.npz
- clinical_encoded_outcome_excluded.npz
- edge_index_shared.pt

Patient-level data and checkpoints are intentionally excluded from this public repository.

## What is needed for full reproduction

1. Export the exact Stage1GNN and GraphLayer classes from the original Colab notebook.
2. Restore the precise data-loading, graph construction, training, EWC/Fisher estimation, and evaluation cells for each experiment.
3. Restore the original input files only in an access-controlled environment; do not commit identifiable patient/genomic/clinical records.
4. Record package versions, hardware/runtime, random seeds, and checkpoint identifiers.
5. Re-run the experiments with multiple seeds and an independent final test set.
6. Define sequential experiences as meaningful tasks rather than arbitrary halves of one training cohort.

## Safe use of this repository

Run python run_pipeline.py --results-only to inspect the stored aggregate findings. The --run-training option exits intentionally until the exact original code is integrated. No result should be described as independently reproduced by the files in this public archive.
