import pandas as pd

# Load Benin data
df = pd.read_csv("Benin.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Summary statistics
print("\nSummary:")
print(df.describe())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())
