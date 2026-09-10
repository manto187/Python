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