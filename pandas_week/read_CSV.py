# to_string to print entire dataframe
import pandas as pd
df = pd.read_csv("data.csv")
print(df.to_string())


# if large dataframe pandas will only return first 5 and last 5
import pandas as pd
df = pd.read_csv("data.csv")
print(df)

# max_rows 

import pandas as pd
print(pd.options.display.max_rows)

# setting max_rows
import pandas as pd
pd.options.display.max_rows = 9999

df = pd.read_csv("data.csv")
print(df)