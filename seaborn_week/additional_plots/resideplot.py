import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")
sns.residplot(x="total_bill",
              y="tips",
              data=data)

plt.show()


# example 2 
import seaborn as sns 
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")

sns.residplot(x="petal_length",
              y="petal_width",
              data=data,
              lowess=True)
plt.show()