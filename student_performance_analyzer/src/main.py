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

# numpy operations 
scores = np.array(df['FinalScore'])

print("\nAverage Score: ")
print(np.mean(scores))

print("\nHighest Scores: ")
print(np.max(scores))

print("\nLowest Scores: ")
print(np.min(scores))

print("\nStandard Deviation: ")
print(np.std(scores))

# performance category 
def category(score):
    if score >=85:
        return "excellent"
    elif score >=70:
        return "good"
    else:
        return "needs improvement"
df['Performance'] = df['FinalScore'].apply(category)

print("\nperformance categories: ")
print(df[['Name', 'Performance']])

# ranking 
df['Rank'] = df['FinalScore'].rank(
    ascending=False,
    method='dense'
)

print("\nStudent Rankings: ")
print(
    df[['Name',
        'FinalScore',
        'Rank']]
)