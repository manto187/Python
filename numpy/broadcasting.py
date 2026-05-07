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


# scaling data with broadcasting
import numpy as np 
fd = np.array([[0.8, 2.9, 3.9],
               [52.4, 23.6, 36.5],
               [55.2, 31.7, 23.9],
               [14.4, 11.0, 4.9]])
cpg = np.array([9,4,4])
result = fd / cpg
print(result)


# adjusting temprature data across multiple locations 
import numpy as np 
temp = np.array([[30, 32, 34, 33, 31],
                 [25, 27, 29, 28, 26],
                 [20, 22, 24, 23, 21]])

corr = np.array([1.5, -0.5, 2.0])
res = temp+corr[:, None]
print(res)



# normalizing image data 
import numpy as np 
img = np.array([[[100, 120, 130],
                 [90, 110, 140],
                 [80, 100, 120]]])

m = img.mean(axis = 0)
s = img.std(axis = 0)
res = (img - m) /s
print(res)