# does the crusting-risk order actually depend on using cohesion, or would
# another mechanical property give the same ranking? cohesion is the property
# Russell tied to crusting, but the database also carries friction angle and
# bulk density, so this checks how much the three agree before i lean on cohesion.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, kendalltau
from harmonize import parse_num, RAW
from scoring import compaction_risk

HERE = Path(__file__).resolve().parent
s = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
cols = {
    "cohesion": "Cohesion (kPa)",
    "friction": "Angle of internal friction (degree)",
    "density": "Bulk density (g/cm^3)",
}
for k, col in cols.items():
    s[k] = s[col].map(parse_num)

report = []


def w(x=""):
    report.append(x)


w("# property sensitivity")
w()
w("Crusting risk from cohesion compared with the order the other mechanical")
w("properties would give. All three should point the same way if the ranking")
w("reflects a general strength axis rather than one measurement.")
w()

base = s.dropna(subset=["cohesion"]).copy()
base["risk"] = compaction_risk(base["cohesion"].to_numpy())
by_coh = base.sort_values("risk")["Simulant"].tolist()

for k in ["friction", "density"]:
    both = s.dropna(subset=["cohesion", k])
    rho, p = spearmanr(both["cohesion"], both[k])
    tau, _ = kendalltau(both["cohesion"], both[k])
    w(f"cohesion vs {k}: n={len(both)}, Spearman {rho:+.2f} (p={p:.2f}), "
      f"Kendall {tau:+.2f}")

w()
# if you built the same risk from density instead, how much would the two ends move
dens = s.dropna(subset=["density"]).copy()
dens["drisk"] = compaction_risk(dens["density"].to_numpy())
by_den = dens.sort_values("drisk")["Simulant"].tolist()
shared = set(base["Simulant"]) & set(dens["Simulant"])
coh_order = [x for x in by_coh if x in shared]
den_order = [x for x in by_den if x in shared]
top_overlap = len(set(coh_order[:5]) & set(den_order[:5]))
bot_overlap = len(set(coh_order[-5:]) & set(den_order[-5:]))
w(f"if ranked by bulk density instead of cohesion (n={len(shared)} shared):")
w(f"- friendliest-5 shared with the cohesion ranking: {top_overlap} of 5")
w(f"- riskiest-5 shared with the cohesion ranking: {bot_overlap} of 5")

(HERE / "property_report.md").write_text("\n".join(report) + "\n")
print("\n".join(report))
print("\nwrote property_report.md")
