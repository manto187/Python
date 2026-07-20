import pandas as pd 

# load dataset 

df = pd.read_csv("data/space_missions.csv")

print("="*50)
print("SPACE MISSION ANALYTICS SYSTEM")
print("STEP 5 - ADVANCED ANALYTICS")
print("="*80)

# success rate by country 
print("\n1. success rate by country")
print("-"*60)

country_success = (
                   df.groupby("Country")["Mission_Status"]
                   .apply(lambda x: (x=="Success").mean()*100)
                   .sort_values(ascending=False)
                   )

print(country_success.round(2))

# success rate by agency 
print("\n2. success rate by agency")
print("-"*60)

agency_success = (
                   df.groupby("Agency")["Mission_Status"]
                   .apply(lambda x: (x=="Success").mean()*100)
                   .sort_values(ascending=False)
                   )

print(agency_success.round(2))


# success rate by rocket
print("\n3. success rate by rocket")
print("-"*60)

rocket_success = (
                   df.groupby("Rocket")["Mission_Status"]
                   .apply(lambda x: (x=="Success").mean()*100)
                   .sort_values(ascending=False)
                   )

print(rocket_success.round(2))

# success rate by launch site 
print("\n4. success rate by launch site")
print("-"*60)

launch_site_success = (
                       df.groupby("Launch_Site")["Mission_Status"]
                       .apply(lambda x: (x=="Success").mean()*100)
                       .sort_values(ascending=False)
                       )

print(launch_site_success.round(2))

# weather effect 
print("\n5. weather effect")
print("-"*60)

weather_success = (
                       df.groupby("Weather")["Mission_Status"]
                       .apply(lambda x: (x=="Success").mean()*100)
                       )

print(weather_success.round(2))

# average launch cost 
print("\n6. average launch cost")
print("-"*60)

print(
    df.groupby("Country")["Launch_Cost_USD"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# revenue by country 
print("\n7. total revenue by country")
print("-" * 60)

print(
    df.groupby("Country")["Revenue_USD"]
    .sum()
    .sort_values(ascending=False)
)


# revenue by agency 
print("\n8. total revenue by agency")
print("-" * 60)

print(
    df.groupby("Agency")["Revenue_USD"]
    .sum()
    .sort_values(ascending=False)
)

# average payload by rocket 
print("\n9. average payload by rocket")
print("-" * 60)

print(
    df.groupby("Rocket")["Payload_kg"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# average fuel by rocket 
print("\n10. average fuel used")
print("-" * 60)

print(
    df.groupby("Rocket")["Fuel_Used_Tons"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# average mission duration
print("\n11. average duration by country ")
print("-" * 60)

print(
    df.groupby("Country")["Mission_Duration_Days"]
    .mean()
    .round(2)
)


# delay analysis 
print("\n12. average delay by weather")
print("-" * 60)

print(
    df.groupby("Weather")["Delay_Days"]
    .mean()
    .round(2)
)

# crew size analysis
print("\n13. average crew size by agency")
print("-" * 60)

print(
    df.groupby("Agency")["Crew_Size"]
    .mean()
    .round(2)
)

# top revenue missions
print("\n14. top 10 revenue missions")
print("-" * 60) 
top = df.nlargest(
    10, 
    "Revenue_USD"
)
print(
    top[
        [
        "Mission_ID",
        "Country",
        "Agency",
        "Rocket",
            "Revenue_USD"
        ]
    ]
)

# correlation matrix 
print("\n15. correlation matrix")
print("-" * 60)
numeric = df.select_dtypes(include="number")

print(
    numeric.corr().round(2)
)
print("\nADVANCED ANALYSIS COMPLETED SUCCESSFULLY")