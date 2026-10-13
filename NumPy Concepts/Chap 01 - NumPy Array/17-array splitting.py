import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Splitting Arrays (Equal Parts)
# --------------------------------------------------------------------------------------------
# np.split(array, no_of_splits)
# Condition -> To use split/divide in equal parts --> Array length should be 
# divisable by no_of_split. (e.g., can we split an array of 8 elements into 3 parts? No!)
# How the datas came? --> Python list of Numpy Arrays of splitted parts

numbers = np.array([
    10, 20, 30, 40,
    50, 60, 70, 80
])

# Question : Split it into 2 equal parts 
# Normal Zindaagi -- (Normal Python Slicing)
partA = numbers[:4]            
partB = numbers[4:]
print(partA)
print(partB)

# Mentos Zindaagi -- np.split()
parts = np.split(numbers, 2)   
print(parts)                   
print(parts[0])
print(parts[1])

parts = np.split(numbers, 4)   # Splitting into 4 equal parts works because 8 is 
print(parts)                   # divisible by 4.
for i in parts:
    print(i)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Splitting by Exact Indices
# --------------------------------------------------------------------------------------------
# Syntax : numpy.split(ary, indices_or_sections, axis=0)
# • indices_or_sections:
#   • Integer (N): Divides the array into N equal sub-arrays along the given axis.
#   • List of sorted integers: Specifies the exact indices where the array will be split. 
#     For example, [2, 5] splits the array into sections [:2], [2:5], and [5:]
# 
# It's like first split is always at 0 index, 2nd onwards split is included in next 
# part, excluded in pvs part.

parts = np.split(numbers, [2, 5])
                               # But everytime it is not needed to split equally 
print(parts)                   # only... Split at index 2 and index 5.

parts = np.split(numbers, [3, 5])
print(parts)                   # Question : we have to split 3ele, 2ele, 3ele


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Splitting 2-D Arrays
# --------------------------------------------------------------------------------------------
# numpy.split(ary, indices_or_sections, axis=0)
# axis = 0(x-axis) : Row-Wise    --> Split accross X-axis
# axis = 1(y-axis) : Column-Wise --> Split accross Y-axis

data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

parts_row = np.split(data, 2, axis=0)
parts_col = np.split(data, 2, axis=1)

print(parts_row)
print(parts_col)