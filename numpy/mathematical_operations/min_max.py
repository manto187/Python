# max() function 
import numpy as np 
a = 10 
b = 21
print(np.maximum(a,b))

# compare 1D array and return element wise max values
import numpy as np 
a = np.array([2,8,123])
b = np.array([3,3,15])
print(np.maximum(a,b))


# when NaN values exists
import numpy as np 
a = np.array([np.nan, 0, np.nan])
b = np.array([np.nan, 0, np.nan])
print(np.maximum(a, b))

# compare two arrays of diff shapes using broadcasting and returns element wise maxima
import numpy as np 
a = np.array([[1,4,7], [2,5,8]])
b = np.array([3,3,3])
print(np.maximum(a,b))