# accessing 1D elements in 1D arrays
import numpy as np 

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])


# accessing 2D elements in multidimensional arrays
import numpy as np 

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(matrix[1,2])


# accessing 3D elements in multidimensional arrays
import numpy as np 

cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[1,2,0])


# 3. slicing arrays 

# slicing 1D arrays 
import numpy as np 

arr = np.array([0,1,2,3,4,5])

print(arr[1:4])

# slicing multidimensional arrays
import numpy as np 

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(matrix[0:2, 1:3])


# 4.Bolean indexing

import numpy as np 

arr = np.array([10, 15, 20, 25, 30])

print(arr[arr>20])

# using logical operators with boolean indexing
import numpy as np 

arr = np.array([10, 20, 30, 40, 50])

print(arr[(arr>20) & (arr<50)])