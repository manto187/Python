# inner product 
import numpy as np 
a = np.array([2,6])
b = np.array([3,10])

print("inner product of vectors a and b =")
print(np.inner(a,b))

# define matrices
x = np.array([[2,3,4],[3,2,9]])
y = np.array([[1,5,0], [5,10,3]])

print("inner product of matrices x and y =")
print(np.inner(x,y))


# outer product 
import numpy as np 

# define vectors
a = np.array([2,6])
b = np.array([3,10])

print("outer product of a and b = ")
print(np.outer(a,b))

# define matrices
x = np.array([[3,6,4], [9,4,6]])
y = np.array([[1,15,7], [3,10,8]])

print("outer product of matrices x and y =")
print(np.outer(x,y))