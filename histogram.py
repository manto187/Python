# normal data distribution in numpy

import numpy as np 

x = np.random.normal(170, 10, 250)

print(x)


# creating histogram by hist() function

import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()