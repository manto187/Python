import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("Projects/netflix_titles.csv")

# missing values 
df['country'] = df['country'].fillna("Unknown")

sns.countplot(data=df, x='type')
plt.title("movies vs tv shows")
plt.show()

year_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.plot(year_counts.index, year_counts.values)
plt.title("netflix content by year")
plt.xlabel("year")
plt.ylabel("count")
plt.show()

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values,
            y=top_countries.index)

plt.title("top producing countries")
plt.show()