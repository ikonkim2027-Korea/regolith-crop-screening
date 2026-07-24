"""Cleaning up the cohesion numbers first. A lot of the older reports give a
range like "0.15 - 0.7" or put a star on estimated values, so I need to turn
those into plain numbers before I can do anything with them."""
import re
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"


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


if __name__ == "__main__":
    gp = grain_percentiles()
    print("samples:", len(gp))
    for k in list(gp)[:5]:
        print(k, gp[k])

# TODO: join grain size onto the cohesion rows and build the stage A table
