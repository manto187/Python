import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

# load dataset
df = pd.read_csv("data/student.csv")
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

# correlation 
print("\nCorrelation matrix: ")
print(df.corr(numeric_only=True))

# visualization 1 
plt.figure(figsize=(8,5))
sns.barplot(
    x='Name',
    y='FinalScore',
    data=df
)
plt.title("Student Scores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# visualization 
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='StudyHours',
    y='FinalScore',
    data=df,
    s=100
)
plt.title(
    "Study Hours vs Final Score"
)
plt.show()


# visualization 3 
plt.figure(figsize=(8,5))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title("correlation heatmap")
plt.show()
