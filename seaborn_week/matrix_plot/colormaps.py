import seaborn as sns 
import numpy as np 

np.random.seed(0)

data = np.random.rand(12,12)

colormap = sns.color_palette("Greens")

ax = sns.heatmap(data, cmap=colormap)

# 2
import seaborn as sns
import numpy as np


np.random.seed(0)

data = np.random.rand(12, 12)
ax = sns.heatmap(data, cmap="Greens")

# 3
sns.palplot(sns.color_palette("PiYG", 12))
sns.palplot(sns.color_palette("coolwarm", 12))

import seaborn as sns
import numpy as np


np.random.seed(0)

data = np.random.rand(12, 12)
ax = sns.heatmap(data, cmap="PiYG")