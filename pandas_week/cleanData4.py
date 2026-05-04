# replacing specific row with a value
import pandas as pd
df = pd.read_csv('data.csv')
df.loc[7, 'Duration'] = 45
print(df.to_string())


# looping through duration column and replace whole column
import pandas as pd
df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print(df.to_string())


# removing rows with values > 120
import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())