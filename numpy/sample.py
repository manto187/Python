import numpy as np 

arr = np.array([1,2,3,4,5])
print(arr)

# NumPy array using special functions 

import numpy as np 

a0 = np.zeros((2, 3))
a1 = np.ones((3, 3))
af = np.full((2, 2), 7)
ar = np.arange(0, 10, 2)
la = np.linspace(0, 1, 5)

print("zero array: ", "\n", a0)
print("one array: ", "\n", a1)
print("constant array: ", "\n", af)
print("range array: ", "\n", ar)
print("linspace array: ", "\n", la)