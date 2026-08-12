import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
import pandas as pd
from scipy.stats import linregress
from scoring import compaction_risk

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "data")


def test_compaction_risk_bounds_and_cap():
    # min maps to 0, everything above the 95th percentile is capped to 1
    r = compaction_risk([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    assert r.min() == 0.0
    assert r.max() == 1.0
    assert r[-1] == 1.0          # the outlier sits at the ceiling
    assert (r >= 0).all() and (r <= 1).all()


def test_calibration_matches_the_paper():
    m = pd.read_csv(os.path.join(DATA, "osd670_mixtures.csv"))
    deficit = 1 - m["radish_biomass_mg"] / m["radish_biomass_mg"].max()
    fit = linregress(m["pH"], deficit)
    assert abs(fit.slope - 0.351) < 0.001
    assert abs(fit.intercept - (-1.675)) < 0.001
    assert abs(fit.rvalue ** 2 - 0.975) < 0.002


def _chem(ph):
    return min(max(0.351 * ph - 1.675, 0.0), 1.0)


def test_chem_term_clips():
    assert _chem(9.6) == 1.0                 # JSC-1A, alkaline, hits the ceiling
    assert _chem(4.0) == 0.0                 # below the line, floored at 0
    assert abs(_chem(6.0) - 0.431) < 0.001   # inside the fitted range


def _score(comp, chem, has_ph):
    return 0.4 * comp + 0.6 * chem if has_ph else comp


def test_score_combine():
    assert abs(_score(0.084, 1.0, True) - 0.6336) < 0.001  # JSC-1A
    assert _score(0.5, 0.0, False) == 0.5                  # no pH, compaction only


if __name__ == "__main__":
    test_compaction_risk_bounds_and_cap()
    test_calibration_matches_the_paper()
    test_chem_term_clips()
    test_score_combine()
    print("ok")
