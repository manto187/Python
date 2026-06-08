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


# example 2 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (8, 8))
ax = plt.axes(projection = '3d')

z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
zline = z

ax.plot3D(x, y, zline, 'gray')
plt.show()