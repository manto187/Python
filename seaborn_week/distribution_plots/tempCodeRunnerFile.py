import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("mpg")
sns.jointplot(x="mpg", y="acceleration", 
              kind = "scatter", data = data)
plt.show()
