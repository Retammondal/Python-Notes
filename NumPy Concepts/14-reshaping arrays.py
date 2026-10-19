import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Reshaping Arrays
# --------------------------------------------------------------------------------------------
# numpy.reshape() --> function changes the dimensions of an array without altering its 
# underlying data.
#
# Method 1: Using the np.reshape function:
#           new_array = np.reshape(array, shape, order='C')
#
# Method 2: Calling the method directly on the array (Most Common):
#           new_array = array.reshape(shape, order='C')
#
# Order means how elements will be placed:
# 'C' : Default --> Fills Element Row by Row
# 'F' : Column Major Order --> Fills Element column by Column
#
# Rule : No. of rows x No. of columns = shape = total no of underlying elements

sales = np.array([             # Monthwise Sales Data
    120, 150, 180, 200,
    220, 250, 270, 300,
    320, 350, 380, 400
])

qtr_sales = sales.reshape(4,3) # Convert to 4 Quarters --> 3 months each

# qtr_sales = sales.reshape(3,3) # Error -> 3x3 != 12 (Shape size must match total elements)

print(qtr_sales)
print(sales.shape)
print(qtr_sales.shape)

sales_update = sales.reshape(2,6)   
                               # Convert the sales to 2 rows --> Automatically i have to 
                               # calculate columne will be 6
print(sales_update)

# ------------------------------------------------------------------
sales_update = sales.reshape(2,-1)  
                               # Mentos Zindagii --> Use of -1; it automatically 
                               # caluclates that part
print(sales_update)

sales_update = sales.reshape(-1,2)  
                               # Conver the sales to 2 column (calculates rows dynamically)
print(sales_update)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Flattening Arrays
# --------------------------------------------------------------------------------------------
# array.flatten() is a built-in NumPy method that collapses a multi-dimensional array 
# into a one-dimensional array copy.

sales = np.array([
    [100, 120, 150],
    [90, 110, 130],
    [200, 220, 250]
])

sales_1d = sales.flatten()     # Flattens the 3x3 2D array into a 1D array
print(sales_1d)


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Reshaping into 3-D Arrays
# --------------------------------------------------------------------------------------------
# Reshaping can also be done in 3-d also

array = np.arange(30)          # Creates a 1D array from 0 to 29

array_3d = array.reshape(2,5,3)
                               # Reshapes into 2 blocks, 5 rows each, 3 columns each 
                               # (2 x 5 x 3 = 30 elements)
print(array_3d)