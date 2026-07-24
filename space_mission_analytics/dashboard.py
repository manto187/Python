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

# dashboard 3 
country_revenue = (
    df.groupby("Country")["Revenue_USD"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=country_revenue.index,
    y=country_revenue.values
)

plt.title("revenue by country")
plt.ylabel("revenue (USD)")
plt.savefig("dashboard/revenue_country.png")
plt.show()

# dashboard 4 
plt.figure(figsize=(10,6))

sns.histoplot(
    df["Launch_Cost_USD"],
    bins=30,
    kde=True
)

plt.title("launch cost distribution")
plt.savefig("dashboard/cost_distribution.png")
plt.show()

# dashboard 5 
plt.figure(figsize=(10,6))

sns.histoplot(
    df["Payload_kg"],
    bins=25,
    kde=True
)

plt.title("payload distribution")
plt.savefig("dashboard/payload_distribution.png")
plt.show()


# dashboard 6 
plt.figure(figsize=(10,6))

sns.boxplot(
    y=df["Fuel_Used_Tons"]
)

plt.title("fuel usage")
plt.savefig("dashboard/fuel_boxplot.png")
plt.show()

# dashboard 7 
delay = df.groupby("Weather")["Delay_Days"].mean()
plt.figure(figsize=(10,6))

sns.barplot(
    x=delay.index,
    y=delay.values
)

plt.title("average delay by weather")
plt.savefig("dashboard/weather_delay.png")
plt.show()

# dashboard 8 
launches = df.groupby("Launch_Year").size()
plt.figure(figsize=(12,6))

plt.plot(
    launches.index,
    launches.values,
    marker="o",
    linewidth=2
)

plt.title("launches per year")
plt.xlabel("year")
plt.ylabel("number of missions")
plt.grid(True)
plt.savefig("dashboard/launches_over_years.png")    
plt.show()

# dashboard 9 
plt.figure(figsize=(12,8))
corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("correlation matrix")
plt.savefig("dashboard/correlation_heatmap.png")
plt.show()

# dashboard 10 
plt.figure(figsize=(10,6))

sns.scatterplot(
    dta=df,
    x="Payload_kg",
    y="Revenue_USD",
    hue="Mission_Status"
)

plt.title("payload vs revenue")
plt.savefig("dashboard/payload_vs_revenue.png")
plt.show()

print("\n dashboard generated successfully")