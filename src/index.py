import numpy as np
import pandas as pd
from harmonize import parse_num, RAW, ROOT, PROC

# compaction risk from measured cohesion
sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["cohesion"] = sim["Cohesion (kPa)"].map(parse_num)
sim = sim.dropna(subset=["cohesion"]).copy()
c = sim["cohesion"].clip(upper=sim["cohesion"].quantile(0.95))
sim["compaction"] = (c - c.min()) / (c.max() - c.min())

# chemistry stress from the pH calibration (numbers from calibrate.py)
ph = pd.read_csv(ROOT / "data" / "sim_ph.csv")
sim = sim.merge(ph, left_on="Simulant", right_on="simulant", how="left")
sim["chem"] = (0.351 * sim["pH"] - 1.675).clip(0, 1)

# combine the two. most simulants have no pH, so fall back to compaction only
# for those instead of getting a NaN
sim["score"] = np.where(
    sim["pH"].notna(),
    0.4 * sim["compaction"] + 0.6 * sim["chem"],
    sim["compaction"],
)

sim = sim.sort_values("score").reset_index(drop=True)
out = sim[["Simulant", "compaction", "chem", "score"]]
PROC.mkdir(parents=True, exist_ok=True)
out.to_csv(PROC / "index.csv", index=False)
print(out.to_string(index=False))

print("\nfriendliest:", ", ".join(sim["Simulant"].head(3)))
print("riskiest:  ", ", ".join(sim["Simulant"].tail(3)))

# reality check: only JSC-1A has a pH, so the chemistry only moves one row and
# the ranking is basically still the compaction one
print("\nsimulants with measured pH:", int(sim["pH"].notna().sum()), "of", len(sim))
