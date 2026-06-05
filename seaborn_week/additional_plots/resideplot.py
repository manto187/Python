import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")
sns.residplot(x="total_bill",
              y="tips",
              data=data)

plt.show()