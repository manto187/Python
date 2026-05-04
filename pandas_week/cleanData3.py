# to_datetime() function to format the dataframe
import pandas as pd
df = pd.read_csv('dirty_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

# removing rows with invalid dates
import pandas as pd
df = pd.read_csv('dirty_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
df.dropna(subset = ['Date'], inplace = True)
print(df.to_string())