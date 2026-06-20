import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load cleaned data
df = pd.read_csv("data/cleaned_churn.csv")

# Load model
model = joblib.load("models/churn_model.pkl")

# Prepare data
X = df.drop("Churn", axis=1)

# Encode text columns
for col in X.select_dtypes(include="object").columns:
    X[col] = X[col].astype("category").cat.codes

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
).head(10)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(
    data=importance,
    x="Importance",
    y="Feature"
)

plt.title("Top 10 Important Features")
plt.tight_layout()

plt.savefig("reports/feature_importance.png")
plt.show()

print("Feature Importance Chart Saved!")