from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
OUT = ROOT / "outputs"

SEED = 42

# features I want to try for predicting cohesion (might change later)
GRAIN_FEATURES = ["d10", "d50", "d90", "sorting", "bulk_density"]
TARGET = "cohesion_kpa"

for d in (RAW, PROC, OUT):
    d.mkdir(parents=True, exist_ok=True)
