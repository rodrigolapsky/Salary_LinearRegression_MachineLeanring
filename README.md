Salary Prediction Study: Multiple Linear Regression Analysis

🚀 Overview This project presents an in-depth study of salary prediction using Machine Learning. With one year of experience in Data Science and Machine Learning, I developed this end-to-end pipeline focused on transforming raw data into actionable insights. The project highlights rigorous Data Engineering, exploratory analysis, and hyperparameter tuning to achieve high predictive accuracy.

🛠️ Tech Stack Data Manipulation: Pandas, NumPy Visualization: Seaborn, Matplotlib Statistical Analysis: Dython (for categorical correlation analysis) Machine Learning: Scikit-Learn Models Tested: Linear Regression, Ridge, Lasso, ElasticNet, RandomForest, and KNN. Optimization: GridSearchCV

📊 Key Features & Data Engineering Target Encoding: Transformed the job_title column by mapping it to the mean salary, capturing high-correlation patterns without increasing dimensionality. Binary Encoding: Converted gender into a binary numerical format to optimize compatibility with linear models. Correlation Analysis: Used the Dython library to generate a correlation matrix that handles both categorical and numerical data, avoiding manual encoding for initial insights.

🏆 Model Selection: Why ElasticNet? After conducting an extensive search using GridSearchCV, multiple models were evaluated. Final Choice: ElasticNet Performance (R² Score): 96.47% Rationale: Although the baseline model achieved a slightly higher score in a single test, ElasticNet was chosen for its statistical security. By balancing L1 and L2 regularization, it ensures a more robust generalization, preventing overfitting and providing more reliable coefficients for long-term use.

📈 Results & Insights The model effectively identifies the primary drivers of salary variance. The Feature Importance analysis (based on the model's coefficients) proves that the engineered features, especially the optimized job_title, were crucial for the 96.47% accuracy.
