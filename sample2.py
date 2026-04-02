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