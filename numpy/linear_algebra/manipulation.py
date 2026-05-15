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


# matrix operations using nested loops
a = [[1,2], [4,5]]
b = [[7,8], [9,10]]
rows  =len(a)
cols = len(a[10])

c = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        c[i][j] = a[i][j] + b[i][j]

print("addition:\n", c)

d = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        d[i][j] = a[i][j] - b[i][j]
print("subtraction:\n", d)


e = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        e[i][j] = a[i][j]/b[i][j]
print("division:", e)
