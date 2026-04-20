import seaborn as sns 
import matplotlib.pyplot as plt 

sns.set_palette("Set2")
data=[3,5,7,9,2,4,6,8]
sns.barplot(x=range(len(data)), y=data)
plt.show()

# qualitative color palette
from matplotlib import pyplot as plt 
import seaborn as sns 

cp = sns.color_palette()
sns.palplot(cp)
plt.show()

# sequential color palette
from matplotlib import pyplot as plt 
import seaborn as sns 

sns.palplot(sns.color_palette("Greys"))
plt.show()

# diverging color palette 
from matplotlib import pyplot as plt 
import seaborn as sns 

sns.palplot(sns.color_palette("terrain_r", 7))
plt.show()