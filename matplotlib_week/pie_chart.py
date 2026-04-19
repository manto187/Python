# creating pie chart
import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# adding lables to charts

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 


# startangle paramter

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()


# exploding the pie chart

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()


# adding shadown to pie chart

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()


# set color of each wedge with colors paramter

import matplotlib.pyplot as plt 
import numpy as np 
 
y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()


# adding list of explanations to each wedge

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()


# legend with the header
import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35, 25, 25, 15])
mylabels = ["apples", "bananas", "cherries", "dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "four fruits")
plt.show()
