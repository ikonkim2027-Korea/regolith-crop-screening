# a data-quality pass over the raw inputs, kept separate from the modelling.
# i want to know exactly what is present, what is missing, and where every
# number comes from before trusting a ranking built on top of it. writes a short
# report so i can glance at the state of the data without rerunning anything.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import pandas as pd
from harmonize import parse_num, RAW, ROOT

HERE = Path(__file__).resolve().parent
report = []


def line(s=""):
    report.append(s)


sim = pd.read_csv(RAW / "gasteiner" / "Dataset_Simulants.csv")
sim["coh"] = sim["Cohesion (kPa)"].map(parse_num)
sim["bd"] = sim["Bulk density (g/cm^3)"].map(parse_num)
coh = sim["coh"].dropna()
cap = coh.quantile(0.95)
outliers = sim.loc[sim["coh"] > cap, "Simulant"].tolist()

line("# data check")
line()
line(f"simulant table: {len(sim)} rows")
line(f"- with cohesion: {sim['coh'].notna().sum()}  (dropped for no cohesion: "
     f"{sim['coh'].isna().sum()})")
line(f"- with bulk density: {sim['bd'].notna().sum()}")
line(f"- duplicate simulant names: {sim['Simulant'].duplicated().sum()}")
line(f"- cohesion kPa: min {coh.min():.2f}, median {coh.median():.2f}, "
     f"max {coh.max():.2f}")
line(f"- above the 95th percentile ({cap:.1f} kPa), so capped in the score: "
     f"{', '.join(outliers)}")
line()

mix = pd.read_csv(ROOT / "data" / "osd670_mixtures.csv")
line(f"calibration: {len(mix)} peat/simulant mixtures, pH {mix['pH'].min()} to "
     f"{mix['pH'].max()}")
line("- two of the four biomass values were read off Russell's figure by eye")
ph = pd.read_csv(ROOT / "data" / "sim_ph.csv")
line(f"chemistry coverage: {len(ph)} of {sim['coh'].notna().sum()} ranked "
     f"simulants have a published pH")
grow = pd.read_csv(ROOT / "data" / "known_growth.csv")
line(f"ground truth for validation: {len(grow)} simulants with published growth")
line()

idx = pd.read_csv(ROOT / "data" / "processed" / "index.csv")
untraceable = sorted(set(idx["Simulant"]) - set(sim["Simulant"]))
line("cross-checks")
line(f"- index.csv rows: {len(idx)}, equals the cohesion count: "
     f"{len(idx) == int(sim['coh'].notna().sum())}")
line(f"- ranked names missing from the source table: {len(untraceable)}")

(HERE / "data_report.md").write_text("\n".join(report) + "\n")
print("\n".join(report))
print("\nwrote data_report.md")
