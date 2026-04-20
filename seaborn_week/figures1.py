# background to white

import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
sns.set_style('white')
sns.set_style('whitegrid')
sns.set_style('darkgrid')
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
plt.show()


# removing axes spines

import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
sns.countplot(x='sex', data=tips)
sns.despine()
plt.show()


# size and aspect
# non grid type plot 
import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')
plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)
plt.show()


# grid type plot 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.lmplot(x ='total_bill', y ='tip', size = 2, aspect = 4, data = tips)
plt.show()
