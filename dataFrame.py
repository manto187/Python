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


# named indexes

import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)


# locating named indexes

import pandas as pd

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])


# loading files into a dataframe

import pandas as pd
df = pd.read_csv("data.csv")
print(df)