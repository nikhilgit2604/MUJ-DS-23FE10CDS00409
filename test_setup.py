from src.data_loader import load_data
from src.preprocessing import clean_text


df = load_data("data/complaints.csv")

print("Dataset loaded successfully!")
print("Number of complaints:", len(df))

print("\nCategories:")
print(df["category"].value_counts())

print("\nOriginal:")
print(df["text"].iloc[0])

print("\nCleaned:")
print(clean_text(df["text"].iloc[0]))