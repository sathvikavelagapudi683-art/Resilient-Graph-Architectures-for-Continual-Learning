"""Paths for the continual GNN experiment."""
import os
from pathlib import Path

GAT_ROOT = Path(os.environ.get("GAT_ROOT", "/content/drive/MyDrive/AIML/gat_experiment"))
CONTINUAL_ROOT = GAT_ROOT / "continual_gnn_v1"
DATA_ALIGNED = GAT_ROOT / "aligned_rna_mut_cnv.npz"
DATA_CLINICAL = GAT_ROOT / "clinical_encoded_outcome_excluded.npz"
EDGE_INDEX = GAT_ROOT / "edge_index_shared.pt"
STAGE_DIRS = {
    i: CONTINUAL_ROOT / name
    for i, name in {
        1: "stage1_rna",
        2: "stage2_ewc",
        3: "stage3_forgetting",
        4: "stage4_fair_comparison",
        5: "stage5_ewc_strength",
        6: "stage6_learning_rate",
    }.items()
}
