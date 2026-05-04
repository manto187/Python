# seaborn.facetgrid() method

import seaborn 
import matplotlib.pyplot as plt 

df = seaborn.load_dataset('tips')

graph = seaborn.FacetGrid(df, col = "sex", hue = "day")
graph.map(plt.scatter, "total_bill", "tip", edgecolor = "w").add_legend()
plt.show()