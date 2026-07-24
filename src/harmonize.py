"""Cleaning up the cohesion numbers first. A lot of the older reports give a
range like "0.15 - 0.7" or put a star on estimated values, so I need to turn
those into plain numbers before I can do anything with them."""
import re
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"


def parse_num(x):
    if x is None:
        return None
    s = str(x).strip().replace("*", "")
    if s in ("", "NA", "N/A", "-"):
        return None
    nums = re.findall(r"-?\d+\.?\d*", s)
    if not nums:
        return None
    # if it is a range, just take the midpoint for now
    return sum(float(n) for n in nums) / len(nums)


def grain_percentiles():
    """d10/d50/d90 per sample from the sieve curves."""
    psd = pd.read_csv(RAW / "gasteiner" / "Dataset_Samples_PSD.csv", sep=";")
    out = {}
    for (mission, sample), g in psd.groupby(["Mission", "Sample"]):
        g = g.copy()
        g["size"] = g["Sieve size (µm)"].map(parse_num)
        g["w"] = g["weight %"].map(parse_num).fillna(0)
        g = g.sort_values("size")  # need smallest size first or the percentiles flip
        sizes = g["size"].to_numpy(dtype=float)
        w = g["w"].to_numpy(dtype=float)
        if w.sum() <= 0:
            continue
        passing = np.cumsum(w) / w.sum() * 100  # not every sample adds up to 100
        d10, d50, d90 = (float(np.interp(p, passing, sizes)) for p in (10, 50, 90))
        out[(mission, sample)] = (d10, d50, d90)
    return out


def build_stage_a():
    """Cohesion rows joined with average grain size for that mission."""
    df = pd.read_csv(RAW / "gasteiner" / "Dataset_All.csv", sep=";")
    df["cohesion_kpa"] = df["Cohesion (kPa)"].map(parse_num)
    df["bulk_density"] = df["Bulk density (g/cm^3)"].map(parse_num)
    df = df.dropna(subset=["cohesion_kpa"])

    # grain size is per sample, cohesion is per mission, so average per mission
    per_mission = {}
    for (mission, _sample), vals in grain_percentiles().items():
        per_mission.setdefault(mission, []).append(vals)
    per_mission = {m: np.mean(v, axis=0) for m, v in per_mission.items()}

    rows = []
    for _, r in df.iterrows():
        d = per_mission.get(r["Mission / Simulant"])
        rows.append({
            "mission": r["Mission / Simulant"],
            "cohesion_kpa": r["cohesion_kpa"],
            "bulk_density": r["bulk_density"],
            "d10": d[0] if d is not None else np.nan,
            "d50": d[1] if d is not None else np.nan,
            "d90": d[2] if d is not None else np.nan,
        })
    out = pd.DataFrame(rows)
    PROC.mkdir(parents=True, exist_ok=True)
    out.to_csv(PROC / "stage_a.csv", index=False)
    return out


if __name__ == "__main__":
    t = build_stage_a()
    print("rows:", len(t), "| with grain size:", int(t["d50"].notna().sum()))
