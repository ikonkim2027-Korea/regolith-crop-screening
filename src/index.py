import numpy as np
import pandas as pd
from harmonize import parse_num, RAW, ROOT

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

# combine the two
sim["score"] = 0.4 * sim["compaction"] + 0.6 * sim["chem"]

sim = sim.sort_values("score")
print(sim[["Simulant", "compaction", "chem", "score"]].to_string(index=False))
