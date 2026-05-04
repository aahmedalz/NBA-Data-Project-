import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

trad = pd.read_csv("data/raw/team_stats_traditional_rs.csv")
adv  = pd.read_csv("data/raw/team_stats_advanced_rs.csv")

# Drop rank columns and duplicate columns before merging
rank_cols_trad = [c for c in trad.columns if c.endswith("_RANK")]
rank_cols_adv  = [c for c in adv.columns if c.endswith("_RANK")]
shared_non_key = ["GP", "W", "L", "W_PCT", "MIN", "TEAM_NAME"]

trad_clean = trad.drop(columns=rank_cols_trad)
adv_clean  = adv.drop(columns=rank_cols_adv + shared_non_key)

merged = pd.merge(trad_clean, adv_clean, on=["TEAM_ID", "SEASON"], how="inner")

merged.to_csv("data/processed/nba_merged.csv", index=False)
print(f"Merged dataset shape: {merged.shape}")
print(f"Columns: {list(merged.columns)}")
print(f"Seasons covered: {sorted(merged['SEASON'].unique())}")
