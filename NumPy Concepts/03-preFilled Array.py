import numpy as np 

# --------------------------------------------------------------------------------------------
# 0 & 1
# --------------------------------------------------------------------------------------------
# np.zeros(shape,dtype) : Creates a new array filled with zeros for the specified shape.
# np.ones(shape, dtype) : Creates a new array filled with ones.

# To create a 2D NumPy array, you pass shape = tuple (rows, columns) 

a = np.zeros(5)         # 1D array of five floating-point zeros: [0. 0. 0. 0. 0.]
b = np.zeros((3,4))     # 2D array (3 rows, 4 columns) passed as a tuple

c = np.ones(5)          # 1D array of ones
d = np.ones((3,5))      # 3x5 2D array of ones

# --------------------------------------------------------------------------------------------
# Numbers
# --------------------------------------------------------------------------------------------
# np.full(shape, fill value, dtype)

e = np.full(6,2)        # 1D 
f = np.full((3,4),4)    # 2D

# --------------------------------------------------------------------------------------------
# Random Numbers
# --------------------------------------------------------------------------------------------
# np.random.rand(shape)

g = np.random.rand(5)
h = np.random.rand(3,5)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

## NOTE : np.zeros, np.ones --> always give Floating num, np.full --> gives whatever you given