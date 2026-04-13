import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from churn import train_churn_model

# Load dataset
df = pd.read_csv("data/onlinedeliverydata.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("Shape:", df.shape)
print(df.head())
print(df.columns)

# Preprocessing
df = df.drop_duplicates()
df = df.fillna(df.mode().iloc[0])

# Use only business-critical deployment-safe features
selected_features = [
    "Age",
    "Family size",
    "Late Delivery",
    "Poor Hygiene",
    "Bad past experience",
    "Long delivery time",
    "More Offers and Discount",
    "Good Food quality",
    "Ease and convenient"
]

X = df[selected_features].copy()
y = df["Output"]

# Proper ordinal Likert mapping
likert_map = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly agree": 5
}

survey_cols = [
    "Late Delivery",
    "Poor Hygiene",
    "Bad past experience",
    "Long delivery time",
    "More Offers and Discount",
    "Good Food quality",
    "Ease and convenient"
]

for col in survey_cols:
    X[col] = X[col].map(likert_map)

# Fill any unmatched values safely
X = X.fillna(3)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data ready")

# Train model
model = train_churn_model(X_train, X_test, y_train, y_test)

# Save exact deployment feature order
joblib.dump(X.columns.tolist(), "models/feature_columns.pkl")

print("Phase 1 complete ✅")