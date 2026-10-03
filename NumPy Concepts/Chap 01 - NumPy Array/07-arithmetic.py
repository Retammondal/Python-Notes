import numpy as np
# Want to add corresponding numbers and create a new Array
a = [3,5,6]
b = [1,5,6]

c = []
for i, j in zip(a, b):
    c.append(i+j)
print(c)

d = []
n = len(a)
for i in range(n):
  d.append(a[i]+b[i])
print(d)

# Want to add corresponding numbers and create a new Array (Using NumPY)
a = np.array([3,5,6])
b = np.array([1,5,7])

print(a+b)      # Directly does all that
print(a-b)
print(a*b)
print(a/b)

print(a**2)
print(a+5)

# Both are of same size & Both are of same datatype

# ------------------------------------------------------------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# Element-wise multiplication
print(matrix * 2) 

# Total sum of all elements
print(matrix.sum())  # Output: 21

# Sum along rows (squashes columns)
print(matrix.sum(axis=1))  # Output: [6, 15]

# Sum along columns (squashes rows)
print(matrix.sum(axis=0))  # Output: [5, 7, 9]