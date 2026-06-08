import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x+y

fig = plt.figure(figsize = (10,10))

ax = plt.axes(projection = '3d')

ax.scatter(x, y, z, c=c)
plt.show()