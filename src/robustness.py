import numpy as np
import pandas as pd
from harmonize import parse_num, RAW

sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["cohesion"] = sim["Cohesion (kPa)"].map(parse_num)
sim = sim.dropna(subset=["cohesion"]).reset_index(drop=True)
names = sim["Simulant"].to_numpy()


def ranking(cvals):
    c = np.clip(cvals, None, np.quantile(cvals, 0.95))
    risk = (c - c.min()) / (c.max() - c.min())
    return names[np.argsort(risk)]


base = ranking(sim["cohesion"].to_numpy())
top3, bot3 = set(base[:3]), set(base[-3:])

# jitter the cohesion by +/-20% and see how often the ends stay the same
N = 2000
th = tb = 0
for _ in range(N):
    noisy = sim["cohesion"].to_numpy() * (1 + np.random.uniform(-0.2, 0.2, len(sim)))
    order = ranking(noisy)
    th += set(order[:3]) == top3
    tb += set(order[-3:]) == bot3

print("top 3 stable:   ", round(100 * th / N, 1), "%")
print("bottom 3 stable:", round(100 * tb / N, 1), "%")
