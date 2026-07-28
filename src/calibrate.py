import pandas as pd
from scipy.stats import linregress
from harmonize import ROOT

m = pd.read_csv(ROOT / "data" / "osd670_mixtures.csv")

# deficit = how much smaller the radish is vs the all-peat control (best case)
control = m["radish_biomass_mg"].max()
m["deficit"] = 1 - m["radish_biomass_mg"] / control

fit = linregress(m["pH"], m["deficit"])
print("deficit = %.3f*pH + %.3f" % (fit.slope, fit.intercept))
print("R2:", round(fit.rvalue ** 2, 3))
