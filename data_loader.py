"""Check that the original experiment inputs exist."""
from config import DATA_ALIGNED, DATA_CLINICAL, EDGE_INDEX


def check_inputs():
    missing = [str(path) for path in (DATA_ALIGNED, DATA_CLINICAL, EDGE_INDEX) if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required input files:\n" + "\n".join(missing))
    print("All required input files found.")


if __name__ == "__main__":
    check_inputs()
