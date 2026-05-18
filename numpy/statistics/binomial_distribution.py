import numpy as np 
x = np.random.binomial(n=10, p=0.5)
print(x)

# example 1
import numpy as np 
arr = np.random.binomial(n=10, p=0.5, size=5)
print(arr)

# example 2 
import numpy as np 
x = np.random.binomial(12, 0.6, size=(2,3))
print(x)



# visualizing binomial distribution
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import binom 

n = 10
p = 0.5
size = 1000

data = np.random.binomial(n, p, size)

plt.hist(data, bins=np.arange(-0.5, n+1.5, 1), density=True, edgecolor='black', alpha=0.7, label='histogram')

x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

plt.scatter(x, pmf, color='red', label='theoretical PMF')
plt.vlines(x, 0, colors='red', linestyles='dashed')

plt.title("binomial distribution (n=10, p=0.5)")
plt.xlabel("number of successes")
plt.ylabel("probability")
plt.legend()
plt.grid(True)
plt.show()