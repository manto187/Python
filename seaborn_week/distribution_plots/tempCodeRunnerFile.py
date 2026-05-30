import seaborn as sns 
import matplotlib.pyplot as plt 
data = sns.load_dataset("exercise")

sns.jointplot(x="id", y="pulse", 
              kind = "kde", data = data)
plt.show()