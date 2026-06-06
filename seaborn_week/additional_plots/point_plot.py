import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")

sns.pointplot(x="sex",
              y="total_bill",
              data=data)
plt.show()

# example 2
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")

sns.pointplot(x="sex",
              y="total_bill",
              hue="smoker",
              data=data)
plt.show()