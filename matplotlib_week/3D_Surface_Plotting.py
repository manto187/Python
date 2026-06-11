from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32),
             np.ones(30))
y = x.copy().T
z = (np.sin(x ** 2) + np.cos(y**2))

fig = plt.figure(figsize = (14, 9))
ax = plt.axes(projection='3d')

ax.plot_surface(x,y,z)
plt.show()