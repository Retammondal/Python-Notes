# Broadcasting
# Broadcasting is a powerful mechanism in Python's NumPy library 
# that allows arithmetic operations on arrays of different shapes
# instead of Python slop loops
import numpy as np

marks = np.array([70, 80, 90])
updated_marks = np.zeros(len(marks), dtype=int)
for i in range(len(marks)):
    updated_marks[i] = marks[i] + 5

print(updated_marks)


marks = np.array([70, 80, 90])
updated_marks = marks + 5       # Broadcasting
# what it does here? it creates an array of [5,5,5,5,5...] and do the arithmetic operation then elementwise
marksAdd = np.array([5,5,5])
updated_marks = marks + marksAdd    # backend of Broadcasting
print(updated_marks)

print('-----------------------------------------------------')
# Case 1 : Arrays and Scaler
# scaler stretches to match the dimension of Array
arr = np.array(
    [[ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12]]
)

# The scalar '2' is treated as shape (1,) and broadcast to (3,4)
result = arr * 2
print(result)

print('-----------------------------------------------------')
# Case 2 : Two Arrays
arr = np.array(
    [[ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12]]
)
row_arr = np.array([1,2,3,4])
col_arr = np.array([
    [1],
    [2],
    [3]
])
print(np.ndim(col_arr))
print(np.shape(col_arr))
print(arr+row_arr)
print(arr+col_arr)
# AI Please go more depth in this topic

print('-----------------------------------------------------')
# Case 3 : Row Vector and Column Vector (Creating a Grid)
col = np.array([[1], 
                [2], 
                [3]])

row = np.array([10, 20, 30])

# Both stretch to shape (3, 3)
result = col + row
print(result)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

