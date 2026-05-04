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



# arrays using random number generation...
import numpy as np 

ar = np.random.rand(2, 3)
an = np.random.randn(2, 2)
ai = np.random.randint(1, 10, size=(2,3))

print(ar)
print(an)
print(ai)



# creating arrays using matrix creating routines
import numpy as np 

im = np.eye(3)
da = np.diag([1, 2, 3])
a0 = np.zeros_like(da)
a1 = np.ones_like(da)

print(im)
print(da)
print(a0)
print(a1)