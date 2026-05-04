# converting 1D array to 2D array 
import numpy as np 
arr = np.array([1,2,3,4,5,6])
r = arr.reshape(2,3)
print(r)

# creating 3D array by grouping original elements 
import numpy as np 
arr = np.array(1,2,3,4,5,6,7,8)
r = arr.reshape(2,2,2)
print(r)


# using -1 to infer dimensions
import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
r = arr.reshape(3, -1)
print(r)