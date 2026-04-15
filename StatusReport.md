# Project Progress Report

## Overview  
This report outlines the current progress of our project, which focuses on analyzing NBA team performance by integrating traditional and advanced statistics to predict team success. The primary goal is to understand how different types of metrics contribute to team win percentage and to evaluate the predictive power of these features using machine learning techniques.  

At this stage, the project is progressing according to plan, with foundational components completed and intermediate steps actively underway. This document provides updates on completed tasks, current work, upcoming phases, challenges encountered, and contributions from each team member.

---

## Task Updates  

### Data Setup – Completed  
The data setup phase has been successfully completed, forming a strong and reliable foundation for the rest of the project. During this stage, we focused on acquiring, verifying, organizing, and initially exploring the datasets. Two primary datasets were used: `team_stats_traditional_rs.csv` and `team_stats_advanced_rs.csv`, both sourced from the NBA statistics repository.  

To ensure data integrity, we implemented SHA-256 hashing on both datasets. This step guarantees that the files remain unchanged throughout the lifecycle of the project and ensures consistency across all team members’ environments. By verifying hashes before use, we eliminate the risk of accidental modifications or discrepancies in data versions.  

In addition to data verification, we established a structured GitHub repository to support collaboration and reproducibility. The repository is organized into the following directories:
- `data/raw/` – Original datasets  
- `data/processed/` – Cleaned and merged datasets  
- `scripts/` – Python scripts for preprocessing and modeling  
- `notebooks/` – Jupyter notebooks for exploration and visualization  
- `docs/` – Project documentation and reports  

This organization ensures that all components of the project are clearly separated and easily accessible, which is especially important for team-based development.  

We also developed initial Python scripts using the Pandas library to load and inspect the datasets. These scripts perform essential checks such as identifying missing values, verifying data types, and generating summary statistics. Through this process, we identified minor inconsistencies in column naming conventions and formatting differences between datasets. These issues will be addressed during the data cleaning and merging phase.  

Overall, the data setup phase ensures that our workflow is reproducible, well-organized, and ready for more advanced analysis.

---

### Data Join – In Progress  
We are currently in the process of merging the traditional and advanced datasets into a single, unified dataset. This step is critical because it enables us to analyze relationships between different types of metrics and build predictive models using a comprehensive feature set.  

The merge is being performed using a multi-key join on `TEAM_ID` and `SEASON`. We are using an inner join approach in Pandas to ensure that only records present in both datasets are included in the final result. This helps maintain consistency and prevents the inclusion of incomplete data.  

To ensure the accuracy of the merge, we are conducting several validation checks:
- Comparing row counts before and after the merge  
- Checking for duplicate rows  
- Identifying null values in key columns  
- Verifying alignment of statistics across datasets  

In addition to automated checks, we are manually validating the merge by inspecting specific teams and seasons to confirm that the combined data is accurate. If any inconsistencies are detected, we will trace them back to their source and determine whether they are caused by missing data, formatting issues, or differences in dataset structure.  

We are also considering implementing additional safeguards, such as logging merge operations and creating intermediate datasets for debugging purposes. These steps will improve transparency and make it easier to diagnose issues if they arise.  

This phase is currently being led by Ahmed and is essential for ensuring the reliability of all subsequent analysis.

---

### Exploratory Data Analysis – Starting Soon  
Once the merged dataset has been finalized and cleaned, we will begin the exploratory data analysis (EDA) phase. This stage is crucial for understanding the structure of the data and identifying patterns that will inform feature selection and modeling decisions.  

Our EDA plan includes several key components. First, we will generate a correlation matrix to examine relationships between traditional and advanced metrics, as well as their association with win percentage. This will help identify which features are most strongly related to team success.  

Second, we will conduct distribution analysis of key variables. This involves examining the spread, central tendency, and skewness of each feature. Understanding these distributions will help us determine whether transformations, such as normalization or log scaling, are necessary.  

Third, we will assess multicollinearity among features. Highly correlated variables can negatively impact model performance and interpretability, so identifying and addressing multicollinearity will be an important step.  

Finally, we will create a variety of visualizations, including heatmaps, histograms, and scatter plots, to better understand relationships and trends within the data. These visual tools will make it easier to communicate findings and guide decision-making.  

This phase will be led by Will and will serve as the bridge between data preparation and modeling.

---

### Modeling – Not Started  
The modeling phase will focus on building a predictive model to estimate team win percentage based on the combined dataset of traditional and advanced statistics. We plan to use a Random Forest Regressor for this task due to its flexibility and robustness.  

Random Forest is particularly well-suited for this problem because it can capture nonlinear relationships, handle high-dimensional data, and reduce overfitting through ensemble learning. Additionally, it provides feature importance metrics, which will help us identify which variables have the greatest impact on predictions.  

The modeling process will include:
- Splitting the dataset into training and testing sets  
- Training the Random Forest model  
- Evaluating performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)  
- Performing hyperparameter tuning to optimize model performance  
- Analyzing feature importance to guide further refinement  

We may also explore alternative models or ensemble approaches if time permits, but Random Forest will serve as our primary model.

---

## Updated Timeline  
The project is currently on schedule, with all completed and ongoing tasks aligning with our original timeline. There have been no significant delays, and team members are effectively coordinating their efforts.  

As we move into the EDA and modeling phases, we will continue to monitor progress closely and make adjustments if necessary. However, based on current progress, we expect to complete the project within the planned timeframe.

---

## Changes to Project Plan  

### Data Handling  
One potential adjustment to our project plan involves handling lockout-shortened seasons, such as 2011–12 and 2019–20. These seasons may introduce inconsistencies due to their reduced number of games.  

We are considering two approaches:
1. Excluding these seasons entirely  
2. Converting win totals into win percentages to standardize comparisons  

This decision will be finalized during the EDA phase based on its impact on the dataset.

### Feature Engineering  
We anticipate the need for feature engineering to account for differences in gameplay across eras. NBA basketball has evolved significantly, with changes in pace, scoring patterns, and shot selection.  

To address this, we plan to:
- Normalize or standardize features  
- Use pace-adjusted statistics  
- Incorporate per-100 possession metrics  

These steps will ensure that our model captures meaningful performance differences rather than era-specific trends.

---

## Challenges So Far  

### Data Consistency Across Eras  
One of the primary challenges is ensuring comparability between statistics from different eras. Changes in rules and playing styles can make direct comparisons misleading.  
**Solution:** Use relative and rate-based metrics.

### Lockout Seasons  
Shortened seasons may distort win totals and affect model training.  
**Solution:** Either remove these seasons or standardize the target variable.

### High Dimensionality  
The merged dataset is expected to contain over 50 features, increasing the risk of overfitting.  
**Solution:**
- Use feature importance from Random Forest  
- Apply dimensionality reduction techniques  
- Remove highly correlated variables  

### Data Integration Risks  
Merging datasets introduces the possibility of mismatches and missing values.  
**Solution:** Perform thorough validation checks and investigate anomalies.

---

## Member Contributions  

### Ahmed Al-Zamzami – Lead Data Engineer  
Ahmed has been responsible for the technical foundation of the project. He led the data acquisition and setup process, including verifying dataset integrity using SHA-256 hashing. He also organized the GitHub repository structure and developed scripts for loading and inspecting the data.  

Currently, Ahmed is leading the data merging process, ensuring that the datasets are accurately combined and validated. His work ensures that the data pipeline is robust, reproducible, and ready for analysis.

### William McKinnon – Lead Data Analyst  
William has focused on developing the analytical framework for the project. He refined the research questions, outlined the EDA approach, and began planning feature engineering and modeling strategies.  

He has also ensured that the datasets align with the project’s objectives and that the analysis will effectively compare traditional and advanced metrics. His work will guide the next stages of the project, particularly in feature selection and model development.

---

## Conclusion  
Overall, the project is progressing smoothly and remains on track. The data setup phase has been completed successfully, and the data merging process is well underway. Upcoming phases, including exploratory data analysis and modeling, are clearly defined and ready to begin once the dataset is finalized.  

By addressing challenges such as data consistency, high dimensionality, and integration risks, we are building a strong foundation for meaningful analysis. With continued collaboration and careful execution, we are confident in our ability to complete the project successfully and generate valuable insights into NBA team performance.
