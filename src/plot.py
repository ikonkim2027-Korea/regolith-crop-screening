import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from harmonize import PROC, ROOT

r = pd.read_csv(PROC / "ranking.csv")

plt.figure(figsize=(6, 8))
plt.barh(r["Simulant"], r["risk"])
plt.xlabel("crusting risk (0 = friendliest)")
plt.tight_layout()

(ROOT / "outputs").mkdir(exist_ok=True)
plt.savefig(ROOT / "outputs" / "ranking.png", dpi=150)
print("saved outputs/ranking.png")
