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
#### Data Handling
We are considering excluding seasons that were cut short due to lockouts such as 2011-12 and 2019-20 to maintain consistency in our calculations. We may also normalize win totals into win percentages to mitigate these concerns. 
#### Feature Engineering
We are anticipating the need to standardize or normalize the features, especially when considering that metrics across eras are from different styles of play. We could possibly include pace-adjusted statistics to account for these changes in gameplay over time. 
# Challenges So Far
During the early stages of the project, we encountered several challenges. The first being data consistency across eras. NBA statistics from the 1990s may not be directly comparable to statistics from the modern game. This is due to both rule changes and gameplay adjustments such as increased pace of play and heavy reliance on the three point shot. Our plan to address this is to use relative or rate based statistics such as per-100 possession statistics. Our second challenge is how to handle lockout seasons. These shortened seasons may distort win totals and in turn the model training. Our two options are removing lockout seasons entirely or converting all targets to win percentage to standardize the comparisons. We will finalize this decision during the Exploratory Data Analysis phase. Our third challenge is high dimensionality. The merged dataset is expected to contain over 50 features which could increase the risk of overfitting. Our plan to address this is to use feature importance from Random Forest, apply dimensionality reduction techniques, and remove highly correlated variables. Our last problem is data integration risks. There may be some potential mismatches that occur during datasets merging. Our plan to address this is to perform validation checks after the merge and investigate null values or dropped rows. 
# Member Contributions
XXXXX
