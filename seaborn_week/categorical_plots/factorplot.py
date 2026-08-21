# example 1 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('Tips.csv')

sns.factorplot(x='size', y='tips', data=df)
plt.show()