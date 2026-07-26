import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
import numpy as np 

data = pd.read_csv("Amazon.csv")

mask =np.triu(np.ones_like(data.corr()))

dataplot = sns.heatmap(data.corr(), cmap="YlGnBu",
annot=True, mask=mask)

plt.show()


# example 2 
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb
import numpy as np 

data = pd.read_csv("exoplanets.csv")

mask = np.triu(np.ones_like(data.corr()))

dataplot = sb.heatmap(data.corr(), mask=mask)

mp.show()