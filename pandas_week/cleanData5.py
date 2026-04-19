# removing dupliactes and returing boolean values for each row
import pandas as pd
df = pd.read_csv('data.csv')
print(df.duplicated())


# removing duplicates from original dataframe
import pandas as pd
df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True)

print(df.to_string())
