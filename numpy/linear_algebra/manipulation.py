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
