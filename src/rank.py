import pandas as pd
from harmonize import parse_num, RAW

sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["cohesion"] = sim["Cohesion (kPa)"].map(parse_num)
sim = sim.dropna(subset=["cohesion"]).copy()

# crusting risk: higher cohesion means more crust, which dries the roots out.
# NAO-1 sits at 95 kPa and squashes everything else, so cap the top first.
c = sim["cohesion"].clip(upper=sim["cohesion"].quantile(0.95))
sim["risk"] = (c - c.min()) / (c.max() - c.min())

sim = sim.sort_values("risk")
print(sim[["Simulant", "cohesion", "risk"]].to_string(index=False))
