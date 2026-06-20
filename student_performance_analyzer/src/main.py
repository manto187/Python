import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

# load dataset
df = pd.read_csv("data/students.csv")
print("\nDataset: ")
print(df)

# basic info
print("\nDataset info: ")
print(df.info())

print("\nStatistics: ")
print(df.describe())

