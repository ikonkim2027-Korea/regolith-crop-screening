import pandas as pd
from scipy.stats import linregress
from harmonize import ROOT

m = pd.read_csv(ROOT / "data" / "osd670_mixtures.csv")

# deficit = how much smaller the radish is vs the all-peat control (best case)
control = m["radish_biomass_mg"].max()
m["deficit"] = 1 - m["radish_biomass_mg"] / control

fit = linregress(m["pH"], m["deficit"])
print("deficit = %.3f*pH + %.3f" % (fit.slope, fit.intercept))
print("R2 vs pH: ", round(fit.rvalue ** 2, 3))

# CEC drops as you add regolith too, so check which one fits better
fit_cec = linregress(m["CEC"], m["deficit"])
print("R2 vs CEC:", round(fit_cec.rvalue ** 2, 3))

# it is only 4 points so this is more of a calibration than a real model,
# do not oversell the R2
print("n =", len(m))
