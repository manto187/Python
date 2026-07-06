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