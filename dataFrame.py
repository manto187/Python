# dataframe 

import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

# locating row using loc[]

import pandas as pd
data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
df = pd.DataFrame(data)
print(df.loc[0])


# use a list of indexes
import pandas as pd
data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
df = pd.DataFrame(data)
print(df.loc[[0,1]])