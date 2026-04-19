# creating bars

import matplotlib.pyplot as plt 
import numpy as np 

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()


# horizantal bars

import matplotlib.pyplot as plt
import numpy as np 

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()


# bar color
import matplotlib.pyplot as plt
import numpy as np 

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.bar(x, y, color = "hotpink")
plt.bar(x, y, color = "#4CAF50")
plt.show()


