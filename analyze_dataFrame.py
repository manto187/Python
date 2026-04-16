# viewing data
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))

# head

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())

# tail

import pandas as pd
df = pd.read_csv('data.csv')
print(df.tail())

# info

import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
