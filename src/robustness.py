import numpy as np
import pandas as pd
from scipy.stats import kendalltau
from harmonize import parse_num, RAW

sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["cohesion"] = sim["Cohesion (kPa)"].map(parse_num)
sim = sim.dropna(subset=["cohesion"]).reset_index(drop=True)
names = sim["Simulant"].to_numpy()


def risk_of(cvals):
    c = np.clip(cvals, None, np.quantile(cvals, 0.95))
    return (c - c.min()) / (c.max() - c.min())


base_risk = risk_of(sim["cohesion"].to_numpy())
base = names[np.argsort(base_risk)]
top3, bot3 = set(base[:3]), set(base[-3:])

# jitter the cohesion by +/-20% and see how stable the ranking is.
# seed it so I get the same number every time
rng = np.random.default_rng(0)
N = 2000
th = tb = 0
taus = []
for _ in range(N):
    noisy = risk_of(sim["cohesion"].to_numpy() * (1 + rng.uniform(-0.2, 0.2, len(sim))))
    order = names[np.argsort(noisy)]
    th += set(order[:3]) == top3
    tb += set(order[-3:]) == bot3
    taus.append(kendalltau(base_risk, noisy).statistic)

print("top 3 stable:   ", round(100 * th / N, 1), "%")
print("bottom 3 stable:", round(100 * tb / N, 1), "%")
print("median kendall tau:", round(float(np.median(taus)), 2))
