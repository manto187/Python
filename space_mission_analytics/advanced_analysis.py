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
