# adding a number to each element 
import numpy as np 
a1 = np.array([2,4,6,8,10])
num= 2
result = a1+num
print(result)

# adding two arrays element wise 
import numpy as np 
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
result = a1+a2
print(result)


# element-wise scalar multiplication
import numpy as np 
a1 = np.array([1,2,3,4])
result = a1*2
print(result)


# logical operations on arrays
import numpy as np 
a1 = np.array([10,20,30])
result = a1>15
print(result)


# matrix operations using vectorization
import numpy as np 
a1 = np.array([[1,2], [3,4]])
a2 = np.array([[5,6], [7,8]])

result = np.dot(a1, a2)
print(result)