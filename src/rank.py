import pandas as pd
from harmonize import parse_num, RAW

sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["cohesion"] = sim["Cohesion (kPa)"].map(parse_num)
sim = sim.dropna(subset=["cohesion"]).copy()

# crusting risk: higher cohesion means more crust, which dries the roots out
c = sim["cohesion"]
sim["risk"] = (c - c.min()) / (c.max() - c.min())

sim = sim.sort_values("risk")
print(sim[["Simulant", "cohesion", "risk"]].to_string(index=False))
