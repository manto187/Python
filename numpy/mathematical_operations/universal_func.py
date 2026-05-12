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