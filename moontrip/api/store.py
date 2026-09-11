# ============================================================
# BASELINE — implemented by the study team. Do not modify for
# tasks M1-M12.
# ============================================================
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load(name):
    """Load `data/<name>.json` and return the parsed JSON."""
    path = os.path.join(DATA_DIR, f"{name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(name, data):
    """Write `data` to `data/<name>.json`, pretty-printed."""
    path = os.path.join(DATA_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
