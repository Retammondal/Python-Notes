import numpy as np

# Setting own Datatype ->  -> during doing that have to follow upcasting

a = np.array([10,20,30],dtype = float)                  # Although all the int ; but i am setting float
print(a)

b = np.array([10.34, 11.2, 12.9], dtype = int)          # Float -> Integer => only decimals
print(b)

c = np.array([23,45.3,1, 0,-45], dtype = bool)          # Number -> Boolean => 0 - false, rest all True
print(c)

# d = np.array(["Retam", "Shruti"], dtype=int)          # Error -> can't be done
# print(d)

# ----------------------------------------------------------------------------------------------
# Checking Data Type
# ----------------------------------------------------------------------------------------------
print(a.dtype)
print(b.dtype)
print(c.dtype)

# --------------------------------------------------------------------------------------------
# Data Types
# --------------------------------------------------------------------------------------------
# • Use dtype= inside np.array() when you are creating an array for the first time.
# • Use .astype() on an array you already created when you need a copy of it in a different data type.

array = np.array([10.5, 20.7, 30.9])
array_int = np.array(array.astype(int))
array_int2 = np.array(array, dtype=int)

print(array)
print(array_int)
print(array_int2)