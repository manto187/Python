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