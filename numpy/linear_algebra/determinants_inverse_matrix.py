import numpy as np 

A = np.array([[50, 29], [30,44]])
sign, logdet = np.linalg.slogdet(A)
result = sign * np.exp(logdet)
print("determinant of A =", result)


# example 2 
import numpy as np 
A = np.array([[1,2],[3,4]])
result = np.linalg.det(A)
print("determinant of A =", result)

# inverse of a matrix
# example 1
import numpy as np 
A = np.array([[6,1,1],
              [4,-2,5],
              [2,8,7]])
print(np.linalg.inv(A))

# example 2 
import numpy as np 
A = np.array([[6,1,1,3],
              [4,-2,5,1],
              [2,8,7,6],
              [3,1,9,7]])
print(np.linalg.inv(A))