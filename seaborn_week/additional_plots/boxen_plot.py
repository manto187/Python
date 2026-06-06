import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")

sns.boxenplot(x="day", y="total_bill", data = data)
plt.show()


# example 2 
import seaborn as sns 
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.boxenplot(x="day", y="total_bill", hue="sex",
              data=data, width=0.8)
plt.show()

# example 3 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")

sns.boxenplot(x="total_bill",
              y="size", data=data, orient="h")
plt.show()