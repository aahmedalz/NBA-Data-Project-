import pandas as pd
import os

os.makedirs("results", exist_ok=True)

trad = pd.read_csv("data/raw/team_stats_traditional_rs.csv")
adv  = pd.read_csv("data/raw/team_stats_advanced_rs.csv")

with open("results/profile_report.txt", "w") as f:
    for name, df in [("Traditional", trad), ("Advanced", adv)]:
        f.write(f"{'='*50}\n{name} Dataset\n{'='*50}\n")
        f.write(f"Shape: {df.shape}\n")
        f.write(f"Seasons: {sorted(df['SEASON'].unique())}\n\n")
        f.write("Missing values:\n")
        missing = df.isnull().sum()
        f.write(str(missing[missing > 0]) + "\n\n")
        f.write("Duplicate rows: " + str(df.duplicated().sum()) + "\n\n")
        f.write("Dtypes:\n" + str(df.dtypes) + "\n\n")
        f.write("Basic stats (numeric):\n")
        f.write(str(df.describe().round(2)) + "\n\n")

print("Profile saved to results/profile_report.txt")
