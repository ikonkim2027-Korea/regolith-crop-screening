# draws the score distribution for the paper. the point of this figure is to
# show how lopsided the scores are: most simulants sit low, only a few climb
# into the risky end. that clustering is hard to see from the table alone.
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

df = pd.read_csv(ROOT / "data" / "processed" / "index.csv")

fig, ax = plt.subplots(figsize=(3.4, 2.2))
ax.hist(df["score"], bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0], color="#4a6b3a",
        edgecolor="white")
ax.set_xlabel("screening score")
ax.set_ylabel("number of simulants")
ax.set_xlim(0, 1)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
fig.savefig(HERE / "fig_scores.png", dpi=200, metadata={"Software": None})
print("wrote fig_scores.png")
