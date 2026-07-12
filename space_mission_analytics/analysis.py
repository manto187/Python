import pandas as pd 

# load dataset 
df = pd.read_csv("data/space_missions.csv")
print("=" *70)
print("space mission analtics system")
print("step 3 - mission analytics")
print("="*70)

# total missions
print("\n1. total missions")
print("-" * 50)
print("total missions :", len(df))

# total successful missions
print("\n2. total successful missions")
print("-" *50)
success = df[df["Mission_Status"] == "Success"]
print("successful missions :", len(success))

# total failed missions
failure = df[df["Mission_Status"] == "Failure"]
print("\n3. total failed missions")
print("-" * 50)
print("failed missions :", len(failure))

# success percentage
success_rate = (len(success)/len(df))*100
print("\n4. success rate")
print("-" * 50)
print(f"{success_rate:.2f}%")

# failure percentage
failure_rate = (len(failure)/len(df))*100
print("\n5. failure rate")
print("-" * 50)
print(f"{failure_rate:.2f}%")

# mission by country 
print("\n6. missions by country")
print("-"*50)
country_missions = df.groupby("Country").size()
print(country_missions.sort_values(ascending=False))

# mission by agency 
print("\n7. missions by agency")
print("-"*50)
agency_missions = df.groupby("Agency").size()
print(agency_missions.sort_values(ascending=False))

# mission by rocket 
print("\n8. missions by rocket")
print("-"*50)
rocket_missions = df.groupby("Rocket").size()
print(rocket_missions.sort_values(ascending=False))

# mission by launch site 
print("\n9. missions by launch site")
print("-"*50)
launch_site_missions = df.groupby("Launch_Site").size()
print(launch_site_missions.sort_values(ascending=False))

# mission by orbit 
print("\n10. missions by orbit")
print("-"*50)
orbit_missions = df.groupby("Orbit").size()
print(orbit_missions.sort_values(ascending=False))

# mission by weather 
print("\n11. missions by weather")
print("-"*50)
weather_missions = df.groupby("Weather").size()
print(weather_missions.sort_values(ascending=False))

# average payload
print("\n12. average payload")
print("-"*50)
print(round(df["payload_kg"].mean(), 2), "kg")


# maximum payload
print("\n13. maximum payload")
print("-"*50)
print(round(df["payload_kg"].max()), "kg")

# minimum payload
print("\n14. minimum payload")
print("-"*50)
print(round(df["payload_kg"].min()), "kg")

# average launch cost
print("\n15. average launch cost")
print("-"*50)
print("${:,.2f}".format(df["launch_cost_usd"].mean()))


# total revenue
print("\n16. total revenue")
print("-"*50)
print("${:,.2f}".format(df["revenue_usd"].sum()))

# average revenue
print("\n17. average revenue")
print("-"*50)
print("${:,.2f}".format(df["revenue_usd"].mean()))

# average fuel used
print("\n18. average fuel used")
print("-"*50)
print(round(df["fuel_used_tons"].mean(), 2), "tons")


# average mission duration
print("\n18. average mission duration")
print("-"*50)
print(round(df["mission_duration_days"].mean(), 2), "days")


# average delay
print("\n20. average delay")
print("-"*50)
print(round(df["delay_days"].mean(), 2), "days")

# top 10 most expensive missions 
print("\n21. top 10 most expensive missions")
print("-"*50)

top_cost = df.sort_values(
    by="launch_cost_usd",
    ascending=False
)

print(
    top_cost[
        [
            "mission_ID",
            "country",
            "agency",
            "rocket",
            "launch_cost_usd"
        ]
    ].head(10)
)