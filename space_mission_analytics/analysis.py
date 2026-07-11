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