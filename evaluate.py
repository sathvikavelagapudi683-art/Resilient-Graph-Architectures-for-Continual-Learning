"""Print validation metrics from the bundled results registry."""
import json
from pathlib import Path

metrics_path = Path(__file__).resolve().parent / "results" / "metrics.json"
data = json.loads(metrics_path.read_text())

for experiment in ("experiment_5_ewc_strength", "experiment_6_learning_rate"):
    print("\n" + experiment)
    for name, result in data[experiment].items():
        print(name, "validation:", result["validation"])
