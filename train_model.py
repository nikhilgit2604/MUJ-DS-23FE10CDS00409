from src.data_loader import load_data
from src.classifier import train_classifier

import joblib


# Load dataset
df = load_data("data/complaints.csv")

print("Dataset loaded successfully.")
print(f"Total complaints: {len(df)}")

print("\nCategory distribution:")
print(df["category"].value_counts())


# Train model
model = train_classifier(df)


# Save model
joblib.dump(
    model,
    "models/complaint_classifier.pkl"
)

print("\nModel saved successfully!")
print("Location: models/complaint_classifier.pkl")