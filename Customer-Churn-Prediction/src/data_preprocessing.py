import pandas as pd

# Load original dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Remove customerID column
df.drop("customerID", axis=1, inplace=True)

# Save cleaned dataset
df.to_csv("data/cleaned_churn.csv", index=False)

print("Cleaned dataset saved successfully!")
print("Shape:", df.shape)