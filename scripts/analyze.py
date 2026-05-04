import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import os

os.makedirs("results/figures", exist_ok=True)

df = pd.read_csv("data/processed/nba_clean.csv")

# ── 1. Correlation with W_PCT ──────────────────────────────────────────────
adv_features  = ["OFF_RATING","DEF_RATING","NET_RATING","TS_PCT","EFG_PCT","PACE","PIE","AST_PCT","TM_TOV_PCT"]
trad_features = ["PTS_PG","FG_PCT","FG3_PCT","REB_PG","AST_PG","TOV_PG","STL_PG","BLK_PG"]

corr_adv  = df[adv_features + ["W_PCT"]].corr()["W_PCT"].drop("W_PCT").sort_values()
corr_trad = df[trad_features + ["W_PCT"]].corr()["W_PCT"].drop("W_PCT").sort_values()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
corr_adv.plot(kind="barh", ax=axes[0], color="steelblue")
axes[0].set_title("Advanced Stats vs W_PCT")
axes[0].set_xlabel("Pearson Correlation")
corr_trad.plot(kind="barh", ax=axes[1], color="coral")
axes[1].set_title("Traditional Stats vs W_PCT")
axes[1].set_xlabel("Pearson Correlation")
plt.tight_layout()
plt.savefig("results/figures/correlations.png", dpi=150)
plt.close()

# ── 2. Random Forest – Traditional only ────────────────────────────────────
X_trad = df[trad_features].dropna()
y_trad = df.loc[X_trad.index, "W_PCT"]
Xtr, Xte, ytr, yte = train_test_split(X_trad, y_trad, test_size=0.2, random_state=42)
rf_trad = RandomForestRegressor(n_estimators=200, random_state=42)
rf_trad.fit(Xtr, ytr)
r2_trad = r2_score(yte, rf_trad.predict(Xte))
rmse_trad = mean_squared_error(yte, rf_trad.predict(Xte)) ** 0.5

# ── 3. Random Forest – Advanced only ───────────────────────────────────────
X_adv = df[adv_features].dropna()
y_adv = df.loc[X_adv.index, "W_PCT"]
Xtr2, Xte2, ytr2, yte2 = train_test_split(X_adv, y_adv, test_size=0.2, random_state=42)
rf_adv = RandomForestRegressor(n_estimators=200, random_state=42)
rf_adv.fit(Xtr2, ytr2)
r2_adv = r2_score(yte2, rf_adv.predict(Xte2))
rmse_adv = mean_squared_error(yte2, rf_adv.predict(Xte2)) ** 0.5

# ── 4. Feature importance plot ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
pd.Series(rf_trad.feature_importances_, index=trad_features).sort_values().plot(kind="barh", ax=axes[0], color="coral")
axes[0].set_title("Feature Importance – Traditional Model")
pd.Series(rf_adv.feature_importances_, index=adv_features).sort_values().plot(kind="barh", ax=axes[1], color="steelblue")
axes[1].set_title("Feature Importance – Advanced Model")
plt.tight_layout()
plt.savefig("results/figures/feature_importance.png", dpi=150)
plt.close()

# ── 5. NET_RATING vs W_PCT scatter ─────────────────────────────────────────
plt.figure(figsize=(8, 6))
plt.scatter(df["NET_RATING"], df["W_PCT"], alpha=0.4, color="steelblue")
plt.xlabel("NET_RATING")
plt.ylabel("W_PCT")
plt.title("Net Rating vs Win Percentage (1996–2023)")
plt.tight_layout()
plt.savefig("results/figures/net_rating_vs_wpct.png", dpi=150)
plt.close()

# ── 6. Save results ────────────────────────────────────────────────────────
with open("results/model_results.txt", "w") as f:
    f.write("=== Traditional Stats Model ===\n")
    f.write(f"R²:   {r2_trad:.4f}\n")
    f.write(f"RMSE: {rmse_trad:.4f}\n\n")
    f.write("=== Advanced Stats Model ===\n")
    f.write(f"R²:   {r2_adv:.4f}\n")
    f.write(f"RMSE: {rmse_adv:.4f}\n\n")
    f.write("=== Top Advanced Correlations with W_PCT ===\n")
    f.write(corr_adv.to_string() + "\n\n")
    f.write("=== Top Traditional Correlations with W_PCT ===\n")
    f.write(corr_trad.to_string() + "\n")

print("Traditional Model  →  R²:", round(r2_trad,4), " RMSE:", round(rmse_trad,4))
print("Advanced Model     →  R²:", round(r2_adv,4),  " RMSE:", round(rmse_adv,4))
print("Figures saved to results/figures/")
