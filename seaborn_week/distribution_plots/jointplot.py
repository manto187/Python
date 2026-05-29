# example 1
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("attention")

sns.jointplot(x="solutions", y="score", 
              kind = "hex", data = data)
plt.show()

# example 2 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("mpg")
sns.jointplot(x="mpg", y="acceleration", 
              kind = "scatter", data = data)
plt.show()


# example 3 
import seaborn as sns 
import matplotlib.pyplot as plt 
data = sns.load_dataset("exercise")

sns.jointplot(x="id", y="pulse", 
              kind = "kde", data = data)
plt.show()