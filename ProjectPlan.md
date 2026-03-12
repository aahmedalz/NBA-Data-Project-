# Project Plan: NBA Performance & Efficiency Analysis

## Overview
The goal of this project is to analyze the relationship between traditional box-score metrics and advanced efficiency ratings to determine which factors most accurately predict a team's winning percentage ($W\_PCT$). We aim to build a predictive model using **Random Forest** to identify if efficiency-based metrics (like `OFF_RATING` and `DEF_RATING`) hold more predictive power than traditional volume stats (like `FGM` or `REB`). Our approach involves cleaning and merging historical datasets, performing exploratory data analysis, and implementing a machine learning pipeline in Python.

## Team
* **Ahmed AL-Zamzami:** Lead Data Engineer. Responsible for data acquisition, GitHub management, data integrity verification (SHA-256), and merging datasets using Pandas.
* **William McKinnon:** Lead Data Analyst. Responsible for exploratory data analysis (EDA), feature engineering, and training the Random Forest regression model.

## Research Questions
1. Which specific metrics from the Advanced dataset (e.g., `NET_RATING`, `TS_PCT`) have the highest correlation with a team's actual win total compared to Traditional metrics?
2. Can a machine learning model accurately predict a team's end-of-season win percentage using only traditional box-score averages?

## Datasets
We are using two distinct datasets sourced from the NBA-dataset-stats repository (non-Kaggle):

1. **Dataset 1: Traditional Team Stats (`team_stats_traditional_rs.csv`)**
   * **Description:** Contains raw volume totals such as Field Goals Made (FGM), Rebounds (REB), and Assists (AST) for all teams from 1996 to 2024.
2. **Dataset 2: Advanced Team Stats (`team_stats_advanced_rs.csv`)**
   * **Description:** Contains calculated efficiency metrics such as Offensive Rating, Defensive Rating, Pace, and True Shooting Percentage (TS_PCT).

**Integration:** These datasets will be integrated via a multi-key join on `TEAM_ID` and `SEASON`.

## Kaggle Clause
No Kaggle datasets are used in this project. All data is sourced from historical archives that reflect real-world data collection from the official NBA API. This avoids the "analysis-ready" nature of Kaggle and requires us to handle raw data cleaning and join logic manually.

## Timeline
| Task | Description | Deadline | Responsibility |
| :--- | :--- | :--- | :--- |
| **Data Setup** | Verify CSV integrity via SHA-256 and setup repo structure. | Week 9-10| Team |
| **Data Join** | Merge Traditional and Advanced datasets on Team ID and Season. | Week 10-12 | Ahmed |
| **EDA** | Identify correlations and visualize statistical distributions. | Week 12-13 | Will |
| **Modeling** | Train and test the Random Forest Regressor. | Before deadline? | Team |

## Constraints
* **Data Consistency:** Historical stats (1990s) may have slightly different recording standards than modern tracking stats.
* **Dimensionality:** With over 50 combined columns, we must use careful feature selection to avoid overfitting our model.

## Gaps
* We need to determine if we should exclude "lockout" shortened seasons (like 2011-12 and the 2020 bubble) to keep the win totals consistent.
* We need to determine how we will handle rule changes and pace of play changes which have affected the league in the last 30 years.
