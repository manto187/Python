# removing empty rows and return a new data frame with no emtpy cells
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())


# remove empty rows and change the original data frame
import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())


# replacing empty cells with a new valuee

import pandas as pd
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
print(df.to_string())



# replace for only specified columnss

import pandas as pd
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace = True)
print(df.to_string())
