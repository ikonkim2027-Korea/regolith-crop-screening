# turns the raw index.csv into a clean ranked table i can paste into the paper.
# sorts friendliest -> riskiest and adds a 1-based rank column.
import pandas as pd
from config import PROC

df = pd.read_csv(PROC / "index.csv")
df = df.sort_values("score").reset_index(drop=True)
df.insert(0, "rank", df.index + 1)

# round so the paper table is readable, keep the csv full precision separately
out = df.copy()
out["score"] = out["score"].round(3)
out["compaction"] = out["compaction"].round(3)

out.to_csv(PROC / "ranked.csv", index=False)
print(out[["rank", "Simulant", "score"]].to_string(index=False))
print(f"\n{len(df)} simulants ranked")
