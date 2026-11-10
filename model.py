"""Model integration point.

Export the exact Stage1GNN and GraphLayer definitions from the original Colab notebook.
Known interface: Stage1GNN(clinical_dim), then model(rna, clinical).

Do not replace these with an approximate architecture when loading saved checkpoints:
state_dict compatibility requires exact module names, tensor shapes, and buffers.

The original model definitions were not recovered, so this module intentionally does not
provide a guessed implementation.
"""
