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


# example 3 
import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
sns.barplot(x='fare', y='class', hue='sex', data=df)
plt.show()

# example 4 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data=df,
            order=["Third", "Second", "First"])
plt.show()

# example 5 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data=df, color="salmon")
plt.show()


# example 6 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data=df, ci=None)
plt.show()

# example 7 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('titanic')
sns.barplot(x='class', y='fare', data=df, hue='sex', palette='pastel')
plt.show()