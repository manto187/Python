import numpy as np 
arr = [20, 2, 7, 1, 34]
result = np.mean(arr)
print(result)

# 1. find average of 1D array 
import numpy as np 
arr = [20, 2, 7, 1, 34]
result = np.mean(arr)
print(result)

# 2. compute mean of all elements, each row and column using axis 
import numpy as np 
arr = [[14, 17, 12],
       [15, 6, 27],
       [23, 2, 54]]
print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# 3. store result of row-wise mean into another array using out 
import numpy as np 
arr = [[5, 10, 15],
       [3, 6, 9],
       [8, 16, 24]]
result = np.zeros(3)
np.mean(arr, axis=1, out=result)
print(result)   