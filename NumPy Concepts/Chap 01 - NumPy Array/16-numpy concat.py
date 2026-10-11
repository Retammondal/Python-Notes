import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Counting Categories (Boolean Masking & Aggregation)
# --------------------------------------------------------------------------------------------
# In NumPy, counting occurrences of specific values is done without 'for' loops.
# It relies on two core mathematical/logical concepts:
# 
# 1. Boolean Masking: Comparing an array to a value creates a new array of purely True/False.
# 2. Integer Value  : In Python/NumPy, 'True' mathematically evaluates to 1, and 'False' to 0.
#
# Concept        : Summing a boolean array simply adds up the 1s (the True values).
# NumPy Syntax   : count = np.sum(array == "Value") or np.sum(array > Number)

test_scores = np.array([98, 85, 92, 74, 99, 81, 65, 95])
                               # Example: Quality testing scores for manufactured parts 
                               # (out of 100)

part_status = np.where(test_scores >= 95, "Perfect", np.where(test_scores >= 80, "Acceptable", "Defective"))
                               # Categorizing the parts based on scores using nested 
                               # np.where. >= 95 -> "Perfect", >= 80 -> "Acceptable", 
                               # Otherwise -> "Defective"

print(part_status)             # Output: ['Perfect' 'Acceptable' 'Acceptable' 'Defective' ...]

# --- Boolean Masking ---
is_perfect = (part_status == "Perfect")
print(is_perfect)              # Output: [ True False False False  True False False  True]

# --- Counting Metrics ---
total_perfect = np.sum(part_status == "Perfect")       
                               # Output: 3 (Because 1 + 0 + 0 + 0 + 1 + 0 + 0 + 1 = 3)

total_acceptable = np.sum(part_status == "Acceptable") 
                               # Output: 3

total_defective = np.sum(part_status == "Defective")   
                               # Output: 2

print(total_perfect)
print(total_acceptable)
print(total_defective)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Appending and Concatenating Arrays (1-D)
# --------------------------------------------------------------------------------------------
# numpy.append(old array, new array)
# The numpy.append() function appends values to the end of an array.
# Immutable : Don't modify the Original Array, create a new one...
# 
# numpy.concatenate((array1, array2, ...))
# np.concatenate is a fundamental NumPy function used to join a sequence of arrays 
# along an existing axis.

january = np.array([120, 150, 180])
february = np.array([140, 160, 200])

print(january)
print(february)

# How to Combine them?
combine = np.append(january, february)
print(combine)                 # Using np.append()

combine = np.concatenate((january, february))
print(combine)                 # Using np.concatenate()

march = np.array([100, 60, 220, 250])

combine3 = np.concatenate((january, february, march))
print(combine3)                # How to do it for 3 arrays: np.append will only take 
                               # one array, but np.concatenate can take more than 1


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Concatenating 2-D Arrays
# --------------------------------------------------------------------------------------------
# Syntax : np.concatenate((array1, array2, ...), axis=0)

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])

print(np.concatenate((a, b)))  # axis=0 (Default): Stacks vertically (adds rows)

print(np.concatenate((a, b), axis=1))
                               # axis=1: Stacks horizontally (adds columns)

print(np.concatenate((a, b), axis=None))
                               # axis=None: Flattens both matrices into a single 1D array

# IMPORTANT NOTE:                                
# Shape Mismatch: All dimensions except the one you are concatenating must match exactly.
# axis=0 (Adding rows)      : Number of columns must be exactly the same.
# axis=1 (Adding columns)   : Number of rows must be exactly the same.
# axis=None (Flattening)    : Shape doesn't matter.


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Stacking Arrays (Another Version of axis = 0/1)
# --------------------------------------------------------------------------------------------
# np.vstack() Vertically Stacks the Arrays (acts like axis = 0)
# np.hstack() Horizontally Stacks the Arrays (acts like axis = 1)

# print(np.vstack((a,b)))               # Vertically Stacks the Arrays (axis = 0) (Requires 
# print(np.hstack((a,b)))               # previous definition of 2D arrays 'a' and 'b')

jan_sales = np.array([70, 80, 90])
feb_sales = np.array([65, 75, 85])
mar_sales = np.array([88, 92, 95])

overall_sales = np.vstack((jan_sales, feb_sales, mar_sales))
                                        # Usecase Example of VStack: Stack multiple 1D arrays
print(overall_sales)                    # into a single 2D matrix (each array becomes a row)


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. np.column_stack() --> Combining 1D Arrays into Columns
# --------------------------------------------------------------------------------------------
# numpy.column_stack() --> Turns 1D Arrays into columns to make a 2-D array 
# (Combines side-by-side).

# For 2-D Arrays no special use --> acts exactly like np.hstack.
# np.row_stack() --> also exists, but acts exactly like np.vstack.

# ----------------------------------------------------------------------------
# Question: Make a Numpy Array where ids, salary, and experience will be columns.
ids = np.array([101, 102, 103])
salary = np.array([50000, 65000, 72000])
experience = np.array([3, 5, 7])
# ----------------------------------------------------------------------------

# Method 1 - Normal Zindaagi: Reshape 1D to 2D column
idsReshape = ids.reshape(-1,1)  
salaryReshape = salary.reshape(-1,1)         
experienceReshape = experience.reshape(-1,1)    

employeeDetails = np.hstack((idsReshape, salaryReshape, experienceReshape))
print(employeeDetails)                  # Horizontally stack the reshaped column vectors

print(np.column_stack((ids, salary, experience)))

# Method 2- Mentos Zindagi: np.column_stack automatically 
# treats 1D arrays as columns and stacks them.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.column_stack((a, b))
print(result)                  # Output:
                               # [[1 4]
                               #  [2 5]
                               #  [3 6]]