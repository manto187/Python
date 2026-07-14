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


# agency distribution 
plt.figure(figsize=(10,6))
agency = df["Agency"].value_counts()
plt.pie(
    agency.values,
    labels=agency.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("agency distribution")
plt.savefig("figures/02_agency_distribution.png")
plt.show()


# rocket usage 
plt.figure(figsize=(12, 6))
rocket=df["Rocket"].value_counts()
sns.barplot(
    x=rocket.index,
    y=rocket.values
)
plt.xticks(rotation=90)
plt.title("rocket usage")
plt.tight_layout()
plt.savefig("figures/03_rocket_usage.png")
plt.show()


# payload distribution 
plt.figure(figsize=(10,6))
sns.histplot(
    df["Payload_kg"],
    bins=30,
    kde=True
)
plt.title("payload distribution")
plt.savefig("figures/04_payload_distribution.png")
plt.show()