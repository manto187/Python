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


# resizing 1D array of 6 elements into a 2x3 array using np.resize()
import numpy as np 
arr = np.array([1,2,3,4,5,6])
arr.resize((2,3))
print(arr)


# resizing 6 elements array into 3x4 array using np.resize() in-place
import numpy as np 
arr = np.array([1,2,3,4,5,6])
arr.resize((3,4))
print(arr)  

# resizing array into a 2x2 shape
import numpy as np 
arr = np.array([1,2,3,4])
arr.resize((2,2))
print(arr)