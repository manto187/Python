import seaborn as sns 
import matplotlib.pyplot as plt 
df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data=df)
plt.show()


# example 2
import seaborn as sns 
import matplotlib.pyplot as plt 
df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', hue='sex', data=df)
plt.show()