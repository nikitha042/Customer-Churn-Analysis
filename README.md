Customer Churn Prediction & Analytics Dashboard

Project Overview

This project predicts customer churn for a telecom company using Machine Learning and provides interactive business insights through a Power BI dashboard.

The objective is to identify customers who are likely to leave the service and understand the key factors contributing to churn.

---

Business Problem

Customer churn directly impacts revenue and customer retention. By analyzing customer behavior and predicting churn, organizations can take proactive measures to retain valuable customers.

---

Dataset

Dataset: Telco Customer Churn Dataset

Records: 7,043 Customers

Target Variable: Churn (Yes/No)

---

Technologies Used

Programming & Analytics

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib

Dashboarding

- Power BI Desktop

Development Environment

- Visual Studio Code

---

Project Workflow

1. Data Preprocessing

- Loaded customer churn dataset
- Handled missing values
- Converted data types
- Removed unnecessary columns
- Created cleaned dataset

2. Exploratory Data Analysis

- Customer churn distribution analysis
- Contract type analysis
- Service usage analysis
- Revenue analysis

3. Machine Learning

- Label Encoding for categorical variables
- Train-Test Split
- Random Forest Classifier
- Model Evaluation

4. Model Output

- Churn Prediction Model
- Feature Importance Analysis
- Model Serialization using Joblib

5. Dashboard Development

Created an interactive Power BI dashboard containing:

- Total Customers KPI
- Churn Distribution
- Contract Type Analysis
- Monthly Charges Analysis
- Customer Segmentation
- Interactive Filters and Slicers

---

Project Structure

Customer-Churn-Prediction/

├── data/

│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv

│   └── cleaned_churn.csv

├── src/

│   ├── data_preprocessing.py

│   ├── train_model.py

│   ├── predict.py

│   └── visualization.py

├── models/

│   └── churn_model.pkl

├── reports/

│   ├── churn_distribution.png

│   └── feature_importance.png

├── dashboard/

│   └── churn_dashboard.pbix

└── README.md

---

Key Insights

- Month-to-month contract customers have higher churn rates.
- Customers without tech support are more likely to churn.
- Contract type significantly influences customer retention.
- Monthly charges show a strong relationship with churn behavior.

---

Future Enhancements

- Streamlit Web Application
- Hyperparameter Tuning
- Advanced Feature Engineering
- Deployment on Cloud Platforms
- Real-time Prediction Dashboard

---

Author

Nikitha Thanikonda

Data Analytics & Machine Learning Project
