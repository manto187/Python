# strip plot 

import seaborn as sns 
import matplotlib.pyplot as plt 

x = ['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]

ax = sns.stripplot(x=x, y=y)
ax.set(xlabel='days', ylabel='amount spent')
plt.title('dailyy spending(custom data)')
plt.show()


# swarm plot 

sns.set(style = "whitegrid")
iris = sns.load_dataset("iris")
sns.swarmplot(x="species", y="sepal_length", data=iris)
plt.title("swarm plot of sepal length by species")
plt.show()

# bar plot

tips = sns.load_dataset("tips")

sns.barplot(x="sex", y="total_bill", data=tips, palette="plasma")
plt.title("average total bill by gender")
plt.show()


# count plot 

tips = sns.load_dataset("tips")

sns.countplot(x="sex", data=tips)
plt.title("count of gender in dataset")
plt.show()