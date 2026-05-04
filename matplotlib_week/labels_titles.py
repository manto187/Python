# with pyplot we can add labels to the x and y axis

import numpy as np
import matplotlib.pyplot as plt


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("average pulse")
plt.ylabel("calorie burange")

plt.show()

# creating title for a plot

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burange")

plt.show()

# adding font properties for titles and labels

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

font1 = {'family': 'serif', 'color':'blue','size':20}
font2 = {'family': 'serif', 'color':'darkred','size':15}

plt.title("sports watch data", fontdict = font1)
plt.xlabel("average pulse", fontdict = font2)
plt.ylabel("calorie burnage", fontdict = font2)
plt.show()


# postioning the title
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()