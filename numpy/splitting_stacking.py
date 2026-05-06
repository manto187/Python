# stacking 1D arrays to form 2D arrays
import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = np.stack((arr1, arr2), axis=0)
print(result)


# stacking same 1D array along axis 0, 1, -1 changing the output 
import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.stack((arr1, arr2), axis=0))
print(np.stack((arr1, arr2), axis=1))
print(np.stack((arr1, arr2), axis=-1))



# stacking two 2D arrays along axis 0,1,2 to show how the new 3D structure changes
import numpy as np 
x = np.array([[1,2,3],
              [4,5,6]])
y = np.array([[7,8,9],
              [10,11,12]])

print(np.stack((x,y), axis=0))
print(np.stack((x,y), axis=1))
print(np.stack((x,y), axis=2))



# stacking two 3D arrays along axis 0,1,2 to demonstrate how stacking works with higher dimension data
import numpy as np 
m = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
n = np.array([[[10,20], [30,40],[50, 60], [70, 80]]])

print(np.stack((m,n), axis=0))
print(np.stack((m,n), axis=1))
print(np.stack((m,n), axis=2))
print(np.stack((m,n), axis=3))




# splitting 1D array into three smaller parts
import numpy as np 
arr = np.array([1,2,3,4,5,6])
result = np.array_split(arr, 3)
print(result)


# splitting methods.
# 1. numpy.split() to divide array into equal-sized subarrays
import numpy as np 
arr = np.array(6)
result = np.split(arr, 2)
print(result)

# 2. numpy.array_split() 
import numpy as np 
arr = np.array(13)
result = np.array_split(arr, 4)
print(result)

