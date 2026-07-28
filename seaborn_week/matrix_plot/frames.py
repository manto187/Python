# adding frames to a seaborn heatmap

import seaborn as sns 
import matplotlib.pyplot as plt 

example = sns.load_dataset("flights")
example = example.pivot("month", "year",
                        "passengers")

res = sns.heatmap(example)
plt.show()

# using axhline and axvline 

# example 1 
import seaborn as sns 
import matplotlib.pyplot as plt 

example = sns.load_dataset("flights")
example = example.pivot("month", "year",
                        "passengers")

res = sns.heatmap(example, cmap="BuPu")

res.axhline(y=0, color='k', linewidth=10)
res.axhline(y=example.shape[1], color='k',
            linewidth=10)
res.axvline(x=0, color='k', 
            linewidth=10)
res.axvline(x=example.shape[0],
            color='k', linewidth=10)

plt.show()

# example 2 
# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

example = np.random.rand(10, 12)
res = sns.heatmap(example, cmap = "magma",linewidths = 0.5)
res.axhline(y = 0, color = 'k',linewidth = 15)

res.axhline(y = 10, color = 'k',linewidth = 15)

res.axvline(x = 0, color = 'k',linewidth = 15)

res.axvline(x = 12, color = 'k',linewidth = 15)
plt.show()