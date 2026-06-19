import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.boxplot(x="day", y="tips", data=df)
plt.show()

# example 1 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")
sns.boxplot(x=df["total_bill"])
plt.show()

# example 2 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker", data=df)
plt.show()

# example 3 
import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
palette = {'Male': 'skyblue', 'Female': 'lightpink'}
sns.boxplot(x="day", y="tips", hue="sex", data=df, palette=palette)
plt.show()

# example 4 
import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.boxplot(x="day", y="tips", data=df, linewidth=2)
plt.show()

# 