# example 1
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("attention")

sns.jointplot(x="solutions", y="score", 
              kind = "hex", data = data)
plt.show()
