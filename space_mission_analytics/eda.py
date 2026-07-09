import numpy as np 
import pandas as pd 
import os 

df = pd.read_csv("data/space_missions.csv")

print("=" * 70)
print("Space Mission Analytics - Exploratory Data Analysis")
print("=" * 70)


# basic information about the dataset
print("\n1. first five records\n")
print(df.head())

print("\n2. last five records\n")
print(df.tail())

print("\n3. random five records\n")
print(df.sample(5))

print("\n4. dataset shape\n")
print(df.shape)

print(f"\nrows   : {df.shape[0]}")
print(f"columns: {df.shape[1]}")


print("\n5. column names\n")
print(df.columns.tolist())

print("\n6. data types\n")
print(df.dtypes)

print("\n7. dataset info\n")
print(df.info())

# missing values
print("\n8. missing values\n")
missing = df.isnull().sum()
print(missing)
print("\ntotal missing values :", missing.sum())

# duplicates 
print("\n9. duplicates records\n")
duplicates = df.duplicated().sum()
print("duplicate rows :", duplicates)


# summary statistics
print("\n10. summary statistics\n")
print(df.describe())
print("\n11. categorical summary\n")
print(df.describe(include='object'))


# unique values
print("\n12. unique values per column\n")

for column in df.columns:
    print(f"{column} : {df[column].nunique()}")


# value counts
print("\n13. country distribution\n")
print(df["country"].value_counts())

print("\n14. agency distribution\n")
print(df["Agency"].value_counts())

print("\n15. rocket distribution\n")
print(df["Rocket"].value_counts())

print("\n16. weather distribution\n")
print(df["Weather"].value_counts())

print("\n17. mission status\n")
print(df["Mission_Status"].value_counts())


# success rate

success_rate = (
    df["Mission_Status"]
    .value_counts(normalize=True)
    *100
)

print("\n18. success rate (%)\n")
print(success_rate)


# numerical analysis
numerical_columns = [
    "Payload_kg",
    "Launch_Cost_USD",
    "Fuel_Used_Tons",
    "Mission_Duration_Days",
    "Delay_Days",
    "Crew_Size",
    "Revenue_USD"
]

print("\n19. numerical analysis\n")
for column in numerical_columns:
    print("="*60)
    print(column)
    print("="*60)
    print("minimum: ", df[column].min())
    print("maximum: ", df[column].max())
    print("mean: ", round(df[column].mean(), 2))
    print("median: ", round(df[column].median(), 2))
    print("std dev: ", round(df[column].std(), 2))