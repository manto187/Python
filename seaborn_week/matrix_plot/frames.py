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