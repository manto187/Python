import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

data = np.random.randint(1,100,(10,10))
sns.heatmap(data)
plt.show()

# example 1 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

data = np.random.randint(1,100,(10,10))
sns.heatmap(data, vmin=30, vmax=70)
plt.show()


# example 2 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

data = np.random.randint(1,100,(10,10))
sns.heatmap(data, cmap='tab20')
plt.show()

# example 3 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

data = np.random.randint(1,100,(10,10))
sns.heatmap(data, cmap='coolwarm', center=50)
plt.show()

# advance customizations in seaborn heatmap
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.colors as mcolors

data=np.random.rand(10,10) *100
plt.figure(figsize=(12,8))

sns.heatmap(
    data,
    xticklabels=list("ABCDEFGHIJ"),
    yticklabels=False,
    norm=mcolors.LogNorm(),
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("custom heatmap", fontsize=16)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()