# plotting x and y points
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y)
plt.show()

# plotting without line

import matplotlib.pyplot as plot
import numpy as np

x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y, 'o')
plt.show()

# plotting with multiple points

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x, y)
plt.show()


# default x points

import matplotlib.pyplot as plt
import numpy as np

y = np.array([3,8,1,10])

plt.plot(y)
plt.show()