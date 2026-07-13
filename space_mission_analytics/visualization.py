import os 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("data/space_missions_analytics.csv")

os.makedirs("figures", exist_ok=True)

sns.set_style("whitegrid")

# missions by country 
plt.figure(figsize=(10, 6))
country = df["Country"].value_counts()
sns.barplot(
    x=country.index,
    y=country.values
)
plt.title("space missions by country")
plt.xlabel("country")
plt.ylabel("number of missions")
plt.tight_layout()
plt.savefig("figures/01_country_missions.png")
plt.show()