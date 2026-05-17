import numpy as np 
x = np.random.normal()
print(x)


# example 1 
import numpy as np 
arr = np.random.normal(size=5)
print(arr)


# example 2
import numpy as np 
m = np.random.normal(loc=10, scale=2, size=(2,3))
print(m)

# visualisation of normal distribution  
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 

# generate data 
data = np.random.normal(loc=0, scale=1, size=1000)

# plot histogram
plt.hist(data, bins=30, edgecolor="black", density=True)

# plot theoretical PDF
x = np.linspace(-4, 4, 200)
pdf = norm.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, label="theoretical PDF")

plt.title("normal distribution")
plt.xlable("value")
plt.ylabel("density")
plt.grid(True)
plt.legend()
plt.show()