import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)
os.makedirs("results", exist_ok=True)

df = pd.read_csv("data/processed/nba_merged.csv")

log = []
log.append(f"Original shape: {df.shape}")

# Flag shortened seasons
shortened = ["1998-99", "2011-12", "2019-20", "2020-21"]
df["SHORTENED_SEASON"] = df["SEASON"].isin(shortened).astype(int)
log.append(f"Shortened seasons flagged: {shortened}")

# Normalize per-game stats by games played (volume -> per game)
per_game_cols = ["FGM","FGA","FG3M","FG3A","FTM","FTA","OREB","DREB","REB","AST","TOV","STL","BLK","PTS"]
for col in per_game_cols:
    df[col + "_PG"] = (df[col] / df["GP"]).round(3)
log.append(f"Created per-game columns for: {per_game_cols}")

# Remove outlier seasons with fewer than 50 games (extreme lockouts)
before = len(df)
df = df[df["GP"] >= 50]
log.append(f"Removed {before - len(df)} rows with GP < 50 (none expected)")

log.append(f"Final shape: {df.shape}")

df.to_csv("data/processed/nba_clean.csv", index=False)

with open("results/cleaning_log.txt", "w") as f:
    f.write("\n".join(log))

print("\n".join(log))
print("\nSaved to data/processed/nba_clean.csv")
