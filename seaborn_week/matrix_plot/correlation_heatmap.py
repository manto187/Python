import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

data = pd.read_csv("#")

co_mtx = data.corr(numeric_only=True)

print(co_mtx)

plt.title("Correlation Heatmap")
sns.heatmap(co_mtx, cmap="YlGnBu", annot=True)
plt.show()

# correlation heatmap for NASA exoplanet dataset
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

data = pd.read_csv("exoplanets.csv")

dataplot = sb.heatmap(data.corr(numeric_only=True))

mp.show()