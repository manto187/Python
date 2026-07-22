import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# loading dataset 

df = pd.read_csv("output/clean_space_missions.csv")

os.makedirs("dashboard", exist_ok=True)

sns.set_theme(style="whitegrid")

# dashboard 1 
country_success = (
    df.groupby("Country")["Mission_Status"]
    .apply(lambda x: (x=="Success").mean() *100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(
    x=country_success.index,
    y=country_success.values
)
plt.title("mission success rate by country")
plt.xlabel("country")
plt.ylabel("success rate (%)")
plt.savefig("dashboard/country_success.png")


# dashboard 2 
rocket = df["Rocket"].value_counts()
plt.figure(figsize=(12,6))

sns.barplot(
    x=rocket.index,
    y=rocket.values
)
plt.xticks(rotation=30)
plt.title("rocket usage")
plt.savefig("dashboard/rocket-usage.png")
plt.show()