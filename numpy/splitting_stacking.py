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