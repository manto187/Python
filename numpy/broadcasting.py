# broadcasting in numpy 
import numpy as np 
a = np.array([[1,2,3], [4,5,6]])
x=10
print(a+x)


# 1. broadcasting a scalar to a 1D array
import numpy as np 
arr = np.array([1,2,3])
result = arr+1
print(result)

# 2. broadcasting a 1D array to a 2D array
import numpy as np 
a = np.array([2,4,6])
b = np.array([[1,3,5], [7,9,11]])
result = a+b
print(result)

# 3. broadcasting in conditional operations
import numpy as np 
a = np.array([12,24,35,45,60,71])
b = np.array(["adult", "minor"])
result = np.where(a<18, b[0], b[1])
print(result)


# using broadcasting for matric multiplication
import numpy as np 
m = np.array([[1,2], [3,4]])
v = np.array([10, 20])
result = m * v
print(result)