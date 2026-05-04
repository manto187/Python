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


# bar width

import matplotlib.pyplot as plt 
import numpy as np 

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)

plt.show()

# bar height

import matplotlib.pyplot as plt 
import numpy as np 

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)

plt.show()
