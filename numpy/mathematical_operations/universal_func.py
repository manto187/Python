import numpy as np 
angles = np.array([0, 30, 45, 60, 90])
rad = np.deg2rad(angles)

sin_vals = np.sin(rad)
print("sine values: ", sin_vals)

inv_sin = np.rad2deg(np.arcsin(sin_vals))
print("inverse sine (degrees): ", inv_sin)

sinh_vals = np.sinh(rad)
print("hyperbolic sine: ", sinh_vals)

hyp = np.hypot(3, 4)
print("hypotenuse: ", hyp)



import numpy as np 
weights = np.array([150.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])

# min and max 
print("min and max", np.amin(weights), np.amax(weights))

# range
print("range: ", np.ptp(weights))

# 70th percentile 
print("70th percentile: ", np.percentile(weights, 70))

# mean
print("mean: ", np.mean(weights))

# standard deviation
print("standard deviation: ", np.std(weights))

# variance
print("variance: ", np.var(weights))

# average
print("average: ", np.average(weights))



# basic bitwise operations on arrays of integers 
import numpy as np 
even = np.array([0, 2, 4, 6, 8, 16, 32])
odd = np.array([1, 3, 5, 7, 9, 17, 33])

# bitwise AND, OR, XOR 
print("AND: ", np.bitwise_and(even, odd))
print("OR: ", np.bitwise_or(even, odd))
print("XOR: ", np.bitwise_xor(even, odd))

# bitwise NOT
print("invert: ", np.invert(even))

# bit shifts
print("left shifts: ", np.left_shift(even, 1))
print("right shift: ", np.right_shift(even, 1))