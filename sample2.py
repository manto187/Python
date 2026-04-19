# creating a series from a list
import pandas as pd

a=[1,2,3,4,5]

myvar = pd.Series(a)
print(myvar)

# creating labels for the series
import pandas as pd
a=[1,2,3,4,5]

myvar = pd.Series(a, index = ["a", "b", "c", "d","e"])

print(myvar)

# we can use a key/value object, like dictionary when creating a series

import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)


# to select any some of items in dictionary use index arguemt and specify only the item
# you want to include in the series

import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day3"])
print(myvar)


#  dataframes 

import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)