import numpy as np 
a = [[1,2], [2,3]]
b = [[4,5], [6,7]]

print("matrix A: ")
print(a)
print("matrix B: ")
print(b)

c = np.dot(a, b)
print("result: ")
print(c)


# example 2
import numpy as np 
x = [[1,2], [2,3], [4,5]]
y = [[4,5,1], [6,7,2]]

print("matrix x: ")
print(x)
print("matrix y: ")
print(y)

result = np.dot(x, y)
print("result:")
print(result)