import seaborn as sns 
import matplotlib.pyplot as plt 

sns.set(style='whitegrid')
tip = sns.load_dataset("tips")

sns.stripplot(x="day", y="total_bill", data=tip)
plt.show()


# example 1 
sns.set(style='whitegrid')
tips = sns.load_dataset("tips")
sns.stripplot(x=tips["total_bill"])
plt.show()

