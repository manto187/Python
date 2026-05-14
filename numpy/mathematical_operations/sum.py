import numpy as np 
arr = np.array([5,10,15])
print(np.sum(arr))


# 1. example explaining how sum 1D array and changing data type affects the result 
import numpy as np 
arr = np.array([20, 2, 0.2, 10, 4])
print(np.sum(arr))
print(np.sum(arr, dtype=np.uint8))
print(np.sum(arr, dtype=np.float32))

# 2. example explaining sum of 2D arrays 
import numpy as np 
arr = np.array([[14, 17, 12, 33, 44],
                [15, 6, 27, 8, 19],
                [23, 2, 54, 1, 4]])

print(np.sum(arr))
print(np.sum(arr, dtype = np.uint8))
print(np.sum(arr, dtype = np.float32))


# 4. example showing summing 2D array along rows, columns and using keepdims=true
import numpy as np 
arr = np.array([[14, 17, 12, 33, 44],
                [15, 6, 27, 8, 19],
                [23, 2, 54, 1, 4]])

print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.sum(arr, axis=1, keepdims=True))
