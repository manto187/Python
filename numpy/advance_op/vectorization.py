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


# applying custom functions using np.vectorize()
import numpy as np 
a1 = np.array([1,2,3,4])
vec = np.vectorize(lambda x: x**2+2*x+1)
result = vec(a1)
print(result)


# vector aggregation operations
import numpy as np 
a1 = np.array([1,2,3])
r1 = a1.sum()
r2 = a1.mean()
print(r1)
print(r2)

# performance comparison: loop vs vectorization

import numpy as np 
import time 
arr = np.arange(1_000_000)

# loop 
t1 = time.time()
loop_res = [x*2 for x in arr]
t2 = time.time()

# vectorized
t3 = time.time()
vec_res = arr*2
t4 = time.time()

print("loop time:", t2-t1)
print("vectorized time:", t4-t3)