import pandas as pd
from harmonize import ROOT, PROC

idx = pd.read_csv(PROC / "index.csv").reset_index(drop=True)
idx["rank"] = idx.index + 1
idx["key"] = idx["Simulant"].str.strip().str.upper()  # names have odd spacing
n = len(idx)

known = pd.read_csv(ROOT / "data" / "known_growth.csv")
for _, k in known.iterrows():
    hit = idx[idx["key"] == k["simulant"].strip().upper()]
    if hit.empty:
        print(k["simulant"], "not in the ranking")
        continue
    r = int(hit["rank"].iloc[0])
    half = "friendlier half" if r <= n / 2 else "riskier half"
    print(f"{k['simulant']}: rank {r}/{n} ({half}) -- reported: {k['outcome']}")
