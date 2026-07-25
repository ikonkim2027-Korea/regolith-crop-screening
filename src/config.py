from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
OUT = ROOT / "outputs"

SEED = 42

# features for the cohesion model (never ended up computing sorting)
GRAIN_FEATURES = ["d10", "d50", "d90", "bulk_density"]
TARGET = "cohesion_kpa"

for d in (RAW, PROC, OUT):
    d.mkdir(parents=True, exist_ok=True)
