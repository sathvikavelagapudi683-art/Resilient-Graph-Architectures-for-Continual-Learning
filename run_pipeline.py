"""Safe entry point for viewing results; training needs exact original Colab source."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-only", action="store_true")
    parser.add_argument("--run-training", action="store_true")
    args = parser.parse_args()

    if args.run_training:
        raise SystemExit(
            "Training is not wired: export the exact Stage1GNN/GraphLayer "
            "and training cells from Colab first."
        )
    if not args.results_only:
        parser.error("Use --results-only to inspect the stored aggregate metrics.")

    data = json.loads((ROOT / "results" / "metrics.json").read_text())
    print("Results:", ROOT / "results" / "metrics.json")
    print("Best ROC-AUC in experiments 5–6:",
          data["interpretation"]["best_validation_roc_auc_exp5_6"])
    print("Best PR-AUC in experiments 5–6:",
          data["interpretation"]["best_validation_pr_auc_exp5_6"])
    print("Caveats:")
    for note in data["interpretation"]["caveats"]:
        print("-", note)


if __name__ == "__main__":
    main()
