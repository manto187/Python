import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

data = pd.read_csv("#")

co_mtx = data.corr(numeric_only=True)

print(co_mtx)

plt.title("Correlation Heatmap")
sns.heatmap(co_mtx, cmap="YlGnBu", annot=True)
plt.show()