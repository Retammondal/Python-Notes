import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Standard Python Lists vs NumPy Arrays
# --------------------------------------------------------------------------------------------
a = [3, 5, 6]                  # Want to add corresponding numbers and create a 
b = [1, 5, 6]                  # new Array using Standard Python Lists

# Method 1: Using zip()
c = []                         
for i, j in zip(a, b):
    c.append(i+j)
print(c)


# Method 2: Using range() and indices
d = []                         
n = len(a)
for i in range(n):
    d.append(a[i]+b[i])
print(d)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Element-wise Math Operations (1D Arrays)
# --------------------------------------------------------------------------------------------
a = np.array([3, 5, 6])        # Want to add corresponding numbers and create a new 
b = np.array([1, 5, 7])        # Array (Using NumPY). Both are of same size & Both 
                               # are of same datatype. Operations in NumPy are 
                               # element-wise by default. If arrays are the same 
                               # size, math operations match up indices perfectly.

print(a + b)                   # Directly does all that: [ 4 10 13]
print(a - b)                   # [ 2  0 -1]
print(a * b)                   # [ 3 25 42]
print(a / b)                   # [3.    1.    0.857]

print(a ** 2)                  # [ 9 25 36] (Exponent/Squared)
print(a + 5)                   # Adds 5 to every single element

                               # Crucial Theory: Are we actually modifying the 
                               # original arrays a and b? NO! Mathematical 
a = a + 5                      # operations output a brand new array. To save the 
                               # changes, you must reassign the variable.


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Operations (2D Arrays)
# --------------------------------------------------------------------------------------------
matrix1 = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])
matrix2 = np.array([
    [8, 4, 3], 
    [5, 4, 6]
])

print(matrix1 * 2)              # Element-wise multiplication (multiplies all by 2)
print(matrix1 + 2)

print(matrix1 + matrix2)

