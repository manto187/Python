import numpy as np 
x = np.array([[1,2], [4,5]])
y = np.array([[7,8], [9,10]])

print("addition\n:", np.add(x,y))
print("subtraction\n:", np.subtract(x,y))
print("division\n:", np.divide(x,y))


# element wise multiplication vs matrix multiplication
import numpy as np 
x = np.array([[1,2], [4,5]])
y = np.array([[7,8], [9,10]])

print("element wise multiplication:\n ", np.multiply(x,y))
print("matrix multiplication:\n ", np.dot(x,y))


# other useful numpy matrix functions 
import numpy as np
x = np.array([[1,2], [4,5]])
y = np.array([[7,8], 9,10])

print("square root:\n", np.sqrt(x))
print("sum of all elements:", np.sum(y))

print("column-wise sum: ", np.sum(y, axis=0))
print("row-wise sum:", np.sum(y, axis=1))
print("transpose:\n", x.T)
