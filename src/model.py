import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict, GroupKFold
from sklearn.metrics import r2_score
from harmonize import build_stage_a

FEATS = ["bulk_density", "d10", "d50", "d90"]


def get_data():
    df = build_stage_a()
    for c in FEATS:
        df[c] = df[c].fillna(df[c].median())
    return df


if __name__ == "__main__":
    df = get_data()
    X = df[FEATS].to_numpy(float)
    y = df["cohesion_kpa"].to_numpy(float)

    # cohesion is really skewed (0 to ~95 kPa) so fit in log space
    ylog = np.log1p(y)
    # group by mission, otherwise samples from the same core end up on both
    # sides of the split and the score looks way better than it should
    groups = df["mission"].to_numpy()
    rf = RandomForestRegressor(n_estimators=500, min_samples_leaf=2, random_state=42)
    pred = cross_val_predict(rf, X, ylog, groups=groups, cv=GroupKFold(5))
    print("R2 (log):", round(r2_score(ylog, pred), 3))
    print("R2 (kPa):", round(r2_score(y, np.expm1(pred)), 3))

    # sanity check: does cohesion even track density? (barely, it turns out)
    from scipy.stats import spearmanr
    rho, p = spearmanr(df["bulk_density"], y)
    print("cohesion vs density spearman:", round(rho, 3), "p", round(p, 3))
