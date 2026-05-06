# NBA Performance & Efficiency Analysis

## Contributors
- Ahmed AL-Zamzami
- William McKinnon

## Summary

This project investigates whether advanced efficiency metrics or traditional box-score statistics are better predictors of NBA team win percentage (W_PCT) across 27 seasons (1996–2023). The growing use of analytics within professional basketball has led teams to increasingly rely on efficiency measurements vs. raw counting stats, thus it should be quantified to see if the shift has been justified from a predictive perspective.

We collected two complementary datasets from a public NBA statistics repository: one containing traditional per-season team statistics (points, rebounds, assists, turnovers) and one containing advanced efficiency metrics (offensive rating, defensive rating, net rating, true shooting percentage, pace). Both datasets span 802 team-season records across 30 NBA teams from 1996-97 through 2022-23. We integrated these datasets via a multi-key join on TEAM_ID and SEASON, profiled and cleaned the merged data, and trained two separate Random Forest regression models,one using only traditional features and one using only advanced features, to predict each team's end-of-season win percentage.

Our findings are conclusive. The advanced stats model achieved an R² of 0.9336 and RMSE of 0.0399, explaining 93.36% of the variance in team win percentage. By contrast, the traditional stats model achieved R² of only 0.481 and RMSE of 0.1115, which is less than half the explanatory power. Among advanced metrics, NET_RATING, OFF_RATING, and DEF_RATING showed the highest individual correlations with W_PCT. Among traditional metrics, field goal percentage and turnover rate were the strongest predictors, though still far weaker than efficiency ratings. These results confirm that efficiency-based metrics are substantially more predictive of team success than raw volume statistics, providing quantitative support for the analytics movement in professional basketball.

## Data Profile

### Dataset 1: Traditional Team Stats
- **File location:** `data/raw/team_stats_traditional_rs.csv`
- **Source:** NBA-Dataset-Stats GitHub repository (https://github.com/datasets/nba-dataset-stats)
- **Shape:** 802 rows x 55 columns
- **Key columns:** TEAM_ID, TEAM_NAME, GP, W, L, W_PCT, FGM, FGA, FG_PCT, FG3M, REB, AST, TOV, STL, BLK, PTS, PLUS_MINUS, SEASON
- **Coverage:** All 30 NBA teams across 27 seasons (1996-97 through 2022-23)
- **Ethical constraints:** This dataset contains publicly available NBA team statistics aggregated at the season level. No personally identifiable information is present. The data originates from NBA.com, which makes aggregate team statistics publicly accessible. No consent issues apply as this is institutional performance data.
- **Relation to research questions:** Provides the traditional box-score features used to train the baseline predictive model and to compare correlations against advanced metrics.

### Dataset 2: Advanced Team Stats
- **File location:** `data/raw/team_stats_advanced_rs.csv`
- **Source:** NBA-Dataset-Stats GitHub repository (https://github.com/datasets/nba-dataset-stats)
- **Shape:** 802 rows x 47 columns
- **Key columns:** TEAM_ID, TEAM_NAME, GP, W, L, W_PCT, OFF_RATING, DEF_RATING, NET_RATING, TS_PCT, EFG_PCT, PACE, PIE, AST_PCT, TM_TOV_PCT, SEASON
- **Coverage:** Same 30 teams and 27 seasons as Dataset 1
- **Ethical constraints:** Same as Dataset 1. All metrics are derived from publicly reported game data. No privacy concerns.
- **Relation to research questions:** Provides the advanced efficiency features used to train the primary predictive model and to answer which metrics best correlate with winning.

### Integration
The two datasets were integrated in `scripts/integrate.py` using an inner join on the composite key (TEAM_ID, SEASON). Before merging, all _RANK suffix columns were dropped from both datasets, and shared non-key columns (GP, W, L, W_PCT, MIN, TEAM_NAME) were dropped from the advanced dataset to prevent duplication. The resulting merged dataset contains 802 rows x 49 columns saved to `data/processed/nba_merged.csv`. No records were lost in the join, confirming perfect alignment between both datasets.

## Data Quality

Data quality assessment was performed using `scripts/profile.py`, generating a full profile report at `results/profile_report.txt`.

**Completeness:** Neither dataset contained any missing values across all columns. The missing value check returned zero for every column in both files across all 802 records.

**Uniqueness:** Neither dataset contained duplicate rows. Each row uniquely identifies one team in one season.

**Consistency:** All statistical columns were correctly typed as float64, identifiers as int64, and categorical fields as strings. No type mismatches were found.

**Temporal coverage:** Both datasets cover the same 27 seasons. However, four seasons had fewer than 82 games: 1998-99 (50 games, labor lockout), 2011-12 (66 games, lockout), 2019-20 (~65 games, COVID-19 bubble), and 2020-21 (72 games, COVID-19). This creates a comparability issue for volume-based statistics across seasons.

**Range validity:** No team played fewer than 50 games in any season. W_PCT values ranged from approximately 0.1 to 0.9, consistent with expected NBA outcomes.

## Data Cleaning

Cleaning was performed in `scripts/clean.py` with a log saved to `results/cleaning_log.txt`.

**1. Shortened season flagging:** A binary column SHORTENED_SEASON was added, set to 1 for the four shortened seasons (1998-99, 2011-12, 2019-20, 2020-21). These seasons were retained because W_PCT remains valid regardless of season length. The flag allows analyses to control for this factor.

**2. Per-game normalization:** Fourteen counting stat columns were divided by GP to produce per-game equivalents (PTS_PG, REB_PG, AST_PG, etc.). This addresses the shortened season comparability problem, that a team's total points in a 66-game season is not directly comparable to one in an 82-game season, but per-game averages are. The traditional stats model uses these normalized columns.

**3. Outlier validation:** A check confirmed no records had GP < 50, validating dataset integrity.

Final cleaned dataset: 802 rows x 64 columns saved to `data/processed/nba_clean.csv`.

## Findings

Two Random Forest Regressor models (200 estimators, random_state=42) were trained on an 80/20 train-test split predicting W_PCT:

| Model | Feature Set | R² | RMSE |
|---|---|---|---|
| Traditional Stats | PTS_PG, FG_PCT, FG3_PCT, REB_PG, AST_PG, TOV_PG, STL_PG, BLK_PG | 0.481 | 0.1115 |
| Advanced Stats | OFF_RATING, DEF_RATING, NET_RATING, TS_PCT, EFG_PCT, PACE, PIE, AST_PCT, TM_TOV_PCT | 0.9336 | 0.0399 |

**RQ1:** NET_RATING had the highest correlation with W_PCT among all features, followed by OFF_RATING and DEF_RATING. Among traditional stats, FG_PCT and TOV_PG showed the strongest relationships but were considerably weaker than the top advanced metrics.

**RQ2:** The traditional-only model achieved R² = 0.481, confirming moderate but insufficient predictive power from raw stats alone. The advanced model's R² of 0.9336 is nearly double, demonstrating that efficiency context is essential for accurate win prediction.

Visualizations are saved in `results/figures/`: correlation bar charts, feature importance plots, and a NET_RATING vs W_PCT scatter plot across all 802 team-seasons.

## Future Work

This project confirmed with high confidence that advanced efficiency metrics are superior predictors of NBA team success. Several extensions are worth pursuing.

Incorporating player-level data would enable roster-based predictions, so teams could be modeled by aggregating individual player efficiency metrics, potentially improving predictions for teams undergoing mid-season roster changes.

A temporal analysis would reveal how predictive relationships have evolved across eras. The NBA has shifted dramatically toward three-point shooting since 2015. Era-specific models could test whether the same metrics remain equally predictive across different epochs.

The current models treat each team-season as an independent observation. A time-series approach accounting for franchise continuity could capture dynasty effects that persist across seasons.

One of the primary findings of this research was how to standardize a team's performance metrics in accordance to games played to assure that standard volume statistics will be used when comparing performance metrics across multiple seasons in the same era. The significance of this quality problem is easily overlooked, but it can play an important role in how to interpret performance metrics across multiple seasons of play.

## Challenges

**Schema verification:** Confirming that the two CSV files actually contained distinct feature sets required inspecting column headers directly before any integration work could begin.

**Deduplication before merging:** Both datasets shared several column names that were not part of the join key. Failing to drop these before merging would have produced duplicate suffixed columns. Careful identification of shared non-key columns before the join was necessary.

**Shortened season handling:** Deciding how to handle four shortened seasons required careful thought. Dropping them would discard 15% of observations. Keeping them without adjustment would introduce volume-stat comparability issues. Flagging and normalizing was the right middle ground.

**Workflow reproducibility:** Mapping the correct file inputs and outputs for each Snakemake rule required careful attention to ensure the dependency graph was correctly specified.

## Reproducing

1. Clone the repository: `git clone https://github.com/aahmedalz/NBA-Data-Project-`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the full workflow: `snakemake --cores 1`

To run scripts manually in order:
python scripts/acquire.py
python scripts/profile.py
python scripts/integrate.py
python scripts/clean.py
python scripts/analyze.py

All input data is in `data/raw/`. SHA-256 checksums are in `data/raw/checksums.txt`. All results are in `results/`.

## References

- NBA-Dataset-Stats. (2024). *NBA team statistics dataset*. GitHub. https://github.com/datasets/nba-dataset-stats
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 51-56.
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
- Mölder, F., et al. (2021). Sustainable data analysis with Snakemake. *F1000Research*, 10, 33.
- Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90-95.
- Waskom, M. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software*, 6(60), 3021.
