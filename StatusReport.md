# Task Updates
#### Data Setup – Completed
The data setup phase has been successfully completed. During this stage, we mainly focused on preparing the datasets and creating a workflow. Both datasets (team_stats_traditional_rs.csv and team_stats_advanced_rs.csv) were downloaded from the NBA dataset stats repository. Data integrity was verified using SHA-256 hashing, which ensures that the datasets will remain unchanged throughout the process of our project. A structured GitHub repository was created in order to organize raw datasets, processed datasets, scripts, and documentation. Initial Python scripts were written to load and inspect datasets using Pandas. 
#### Data Join – In Progress
We have begun merging the traditional and advanced datasets using a multi-key join on TEAM_ID and SEASON. Our planned approach is to use Pandas to merge with inner join logic, validate join accuracy by checking row counts and null values, and generate a cleaned dataset for analysis. This is being led by Ahmed. 
#### Exploratory Data Analysis – Starting Soon
Once the datasets are merged we will begin this process. Our analysis will include a correlation matrix comparing the traditional and advanced metrics, a distribution analysis of key variables, identification of multicollinearity, and visualizations. This is being led by Will and will inform feature selection for modeling. 
#### Modeling – Not Started
The modeling phase will involve training a Random Forest Regressor to predict team win percentage. 

# Updated Timeline
Overall, the project is on schedule. There are no delays so far so the timeline will remain consistent with our original project plan. 
# Changes to Project Plan
XXXXX
# Challenges So Far
XXXXX
# Member Contributions
XXXXX
