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