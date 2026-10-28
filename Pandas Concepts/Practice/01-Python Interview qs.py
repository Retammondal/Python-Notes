print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Product of All Elements Except the Current Element

# Problem statement: Create a result array in which each position contains
# the product of all the other array elements, without dividing by the current element.
# Example : [1,2,3,4]
# --------------------------------------------------------------------------------------------
array = [1,2,0,4]
output = []
for i in array:
    mul = 1
    for j in array:
        if i!=j:
            mul = mul*j
    output.append(mul)
print(output)

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Left Rotate an Array by One Position
# Problem statement:
# Given an array, rotate all elements one position to the left.
# The first element should move to the last position.
# Example : [10,20,30,40,50]
# Output :
# --------------------------------------------------------------------------------------------
array = [10,20,30,40,50]

# MEthod 1 :
new_array = array.copy()

n = len(array)
for i in range(n):
    new_array[i-1] = array[i]
print(new_array)

# MEthod 2 :
new_array = array[1:] + [array[0]]
# why the 2nd thing need to be in array; 
# b/c array[1:] - gives list but array[0] give Number so convert to list to concatanate
new_array = array[1:] + array[:1]
print(new_array)

# ========== LEFT ROTATE ARRAY BY ONE ==========

# METHOD 1: Index Shifting
# Logic: Copy array, then place array[i] at index i-1.
# When i=0, index -1 refers to the last position.
# Time: O(n) | Space: O(n)
# Good for understanding indexing and loops.

# METHOD 2: List Slicing
# Logic: Take elements from index 1 onward,
# then append the first element at the end.
# Time: O(n) | Space: O(n)
# Shorter, cleaner, and more Pythonic.

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Right Rotate an Array by K Positions
# Problem statement: Rotate an array to the right by k positions.
# Example: [1, 2, 3, 4, 5], k = 2
# Output:
# --------------------------------------------------------------------------------------------
array = [1,2,3,4,5,6,7]
k = 2
new_array = array[-k:] + array[:-k]
print(new_array)

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Intersection of Two Arrays without Duplicates
# Problem statement: Print every element that appears in both arrays.
# Do not print duplicates.
# --------------------------------------------------------------------------------------------
arr1 = [10,20,30,40,50,90]
arr2 = [10,20,20,60,80,90]

output = []
for i in arr1:
    if (i not in output) & (i in arr2):
        output.append(i)
print(output)

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Union of Two Arrays
# Problem statement: Print every distinct element that appears in either of two arrays.
# Do not print duplicates.
# --------------------------------------------------------------------------------------------
arr1 = [10,20,30,40,50,90]
arr2 = [10,20,20,60,80,90]

output = list(set(arr1 + arr2))         # convert to set --> then again to list
print(output)

# Method 2 : Without using Set
output = []
for i in arr1:
    if i not in output:
        output.append(i)
for i in arr2:
    if i not in output:
        output.append(i)
print(output)

