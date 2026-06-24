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

# example 2 
sns.set(style='whitegrid')
tips = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill", data=tips, jitter=0.1)
plt.show()


# example 3 
import seaborn as sns 
import matplotlib.pyplot as plt 

sns.set(style='whitegrid')
tips = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill",
              hue="smoker", 
              data=tips, palette="Set1", size=20, marker="s", alpha=0.2)
plt.show()