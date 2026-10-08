import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Numpy.sort(array)
# --------------------------------------------------------------------------------------------
# np.sort is a NumPy function used to return a sorted copy of an array. 
# Immutable : Don't modify original, create new one 
# Note : Python's built-in list.sort(), which modifies the original list in-place (Mutable)
# Important Note : It gives by default in Descending Order

arr = np.array([3, 1, 5, 2, 4])
sorted_arr = np.sort(arr)

print(sorted_arr)              # Output: [1 2 3 4 5]
print(arr)                     # Output: [3 1 5 2 4] (Original is unchanged)

sorted_arr_asc = np.sort(arr)[::-1]
                               # How to get values in Ascending Order?? --> Apply 
                               # Slicing Concept
print(sorted_arr_asc)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Numpy.percentile(array, percentile)
# --------------------------------------------------------------------------------------------
# np.percentile() is a NumPy function used to compute the q-th percentile of data.
# A percentile is a statistical measure that indicates the percentage of a dataset 
# that falls at or below a specific value.
#
# Instead, it uses interpolation to calculate a single, exact value between the two 
# closest points. For example, if the 75th percentile falls exactly halfway between 
# 40 and 50, NumPy uses its default linear interpolation to return a single value: 45.0.

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = np.percentile(data, 70)
                               # Find the 70th percentile
print(result)                  # Output: 73.0

quartiles = np.percentile(data, [25, 50, 75])
                               # Calculate the 25th (Q1), 50th (Median), and 75th 
                               # (Q3) percentiles
print(quartiles)               # Output: [20. 30. 40.]