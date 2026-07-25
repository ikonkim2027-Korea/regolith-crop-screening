import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_predict, GroupKFold
from sklearn.metrics import r2_score
from model import get_data, FEATS

df = get_data()
X = df[FEATS].to_numpy(float)
y = np.log1p(df["cohesion_kpa"].to_numpy(float))
groups = df["mission"].to_numpy()

gbm = GradientBoostingRegressor(random_state=42)
pred = cross_val_predict(gbm, X, y, groups=groups, cv=GroupKFold(5))
print("gbm R2 (log):", round(r2_score(y, pred), 3))
