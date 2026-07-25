import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict, KFold
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

    rf = RandomForestRegressor(n_estimators=300, random_state=42)
    pred = cross_val_predict(rf, X, y, cv=KFold(5, shuffle=True, random_state=42))
    print("R2:", round(r2_score(y, pred), 3))
