import numpy as np 

A = np.array([[50, 29], [30,44]])
sign, logdet = np.linalg.slogdet(A)
result = sign * np.exp(logdet)
print("determinant of A =", result)