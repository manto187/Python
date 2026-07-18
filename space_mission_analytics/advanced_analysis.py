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