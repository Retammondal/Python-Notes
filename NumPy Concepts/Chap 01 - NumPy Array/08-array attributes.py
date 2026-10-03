import numpy as np 

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Array Properties
# --------------------------------------------------------------------------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix.shape)            # .shape : A tuple indicating the size of each 
                               # dimension. For 2D -> (rows, columns); For 1D -> 
                               # (number of elements,). Output: (2, 3)

print(matrix.ndim)             # .ndim : Number of dimensions (1 for 1D, 2 for 2D, 
                               # 3 for 3D, etc.). Output: 2

print(matrix.size)             # .size : Total number of elements in the entire 
                               # array. Output: 6

print(matrix.dtype)            # .dtype : The data type of the elements. Output: int64

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Length of NumPy Array
# --------------------------------------------------------------------------------------------
array_1d = np.array([10, 20, 30, 40])

array_2d = np.array([          # len() gives the length of the outermost dimension.
    [10, 15, 18],              # (Just like Python List). Row 0
    [20, 25, 30]               # Row 1
])

print(len(array_1d))           # 4. For a 1D array -> number of elements
print(len(array_2d))           # 2 -> Number of rows. For a 2D array -> number of rows. 
                               # For higher dimensions -> size of the first dimension.

print(array_2d.size)           # 6 -> Total elements

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Dimensions of NumPy Array
# --------------------------------------------------------------------------------------------
array_3d = np.array([          # NumPy arrays can have multiple dimensions: 
    [                          # 3-D NumPy Array
        [10, 15, 18],
        [20, 25, 30]
    ],
    [
        [5, 6, 7],
        [7, 6, 9]
    ]
])

print(array_1d.ndim)           # 1
print(array_2d.ndim)           # 2
print(array_3d.ndim)           # 3

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# Shape of NumPy Array
# --------------------------------------------------------------------------------------------
sales = np.array([
    [125000, 148000, 135000, 172000],       # Year 2024 quarterwise data
    [100000, 148000, 130000, 160000]        # Year 2025 quarterwise data
])

print(sales.shape)             # (2, 4) -> 2 Rows, 4 Columns
print(array_1d.shape)          # (4,) -> 1D array with 4 elements. NOTE: 1D array 
                               # shape is (4,), NOT (1,4)

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# Size of NumPy Array
# --------------------------------------------------------------------------------------------
print(array_1d.size)           # 4. .size -> Total number of elements in the array.

print(array_2d.size)           # 6. Relation between size and shape: 
                               # For a 2D array: rows × columns = size