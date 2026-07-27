# adding frames to a seaborn heatmap

import seaborn as sns 
import matplotlib.pyplot as plt 

example = sns.load_dataset("flights")
example = example.pivot("month", "year",
                        "passengers")

res = sns.heatmap(example)
plt.show()

