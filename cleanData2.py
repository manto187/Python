# calculate mean and replace empty cells with values
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())


# calculating median and replacing empty values with it 

import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())


# calculating mode and replacing empty values with it

import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())