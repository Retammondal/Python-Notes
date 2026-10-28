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

print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Index Where Left and Right Products Are Equal
# Problem statement: Find an index where the product of all elements
# to its left equals the product of all elements to its right.
# Exclude the element at that index from both products.
# Assume the array contains positive integers greater than zero.
A = [4, 3, 5, 2, 6]
# Ans:
# --------------------------------------------------------------------------------------------

def product(array):
    prod = 1
    for i in array:
        prod *= i
    return prod
n = len(A)
for i in range(n):
    if product(A[:i]) == product(A[i+1:]):
        print(i)

# Back Thinking :
# creating function which will take array input and multiply all the array elements
# then --> iterate through each product and check the first index where product of all = product of all right 
# using splicing concept

print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# (VVI)
# Answer Multiple Range-Sum Queries
# Problem statement: Given an array and several queries,
# each containing a starting index L and ending index R,
# calculate the sum of elements from index L to index R, inclusive.
# Example: Array [3, 5, 2, 8, 4]
# - Query L = 1, R = 3 -> 15
# - Query L = 0, R = 2 -> 10
# --------------------------------------------------------------------------------------------

# METHOD 01 :
array = [3,5,2,8,4]
def query(array, L, R):
    final_array = array[L : R+1]
    print(sum(final_array))

query(array,1,3)
query(array,0,2)

array = [3,5,2,8,4]

# -----------------------------------------------------
# METHOD 02 :
# Because prefix starts with a leading 0, its indices are shifted by 1 relative to array:
# prefix[k] stores the sum of the first 'k' elements of array (indices 0 to k - 1).
# prefix[0] = 0 represents the sum of First 0 elements.
def query2(array, L, R):
    prefix = [0]
    for x in array:
        prefix.append(prefix[-1] + x)
    print(prefix[R+1] - prefix[L])
query2(array,1,3)
query2(array,0,2)

# ========== MULTIPLE RANGE-SUM QUERIES ==========

# METHOD 1: Slicing + sum()
# Logic: Extract elements from L to R and calculate sum.
# Time: O(k) per query | Space: O(k)
# k = R-L+1 (number of elements in range).

# METHOD 2: Prefix Sum
# Logic: Store cumulative sums, then subtract:
# Range Sum = prefix[R+1] - prefix[L]

print("----------------------8-----------------------")
# --------------------------------------------------------------------------------------------
# Calculate the Prefix Sum Array
# Problem statement: Given an array,
# create a new array where each position contains the sum of
# all elements from index 0 to that position.
# Example: [2, 4, 1, 5, 3]
# Output:
# --------------------------------------------------------------------------------------------
array = [2,4,1,5,3]
prefix = [0]
for x in array:
    prefix.append(prefix[-1]+x)
print("Prefix Array :", prefix)

def prefix_add(index):
    print(prefix[index+1])          # Why +1 index =3 means first 4 elements
    print(prefix[1:][index])        # Here we first make the prefix 0 delete now index=3 means sum upto 3
prefix_add(3)


# METHOD 2 : We can start the prefix with the first element of array 
prefix = array[:1]      # have to use slicing to maintain the array
for x in array[1:]:
    prefix.append(prefix[-1]+x)

def prefix_add2(index):
    print(prefix[index])          
prefix_add2(3)

# ========== PREFIX SUM ARRAY ==========

# METHOD 1: Prefix with Initial Zero
# Logic: Start with [0], add cumulative sums.
# Output: [0, 2, 6, 7, 12, 15]
# Sum up to index i = prefix[i+1]
# Range sum L to R = prefix[R+1] - prefix[L]
# Best for: Multiple range-sum queries.

# METHOD 2: Prefix Without Initial Zero
# Logic: Start with first element, add cumulative sums.
# Output: [2, 6, 7, 12, 15]
# Sum up to index i = prefix[i]
# Best for: Direct prefix-sum array problems.

print("----------------------9-----------------------")
# --------------------------------------------------------------------------------------------
# (VVI)
# Find the Longest Subarray with Equal Numbers of 0s and 1s
# Problem statement: Given an array containing only 0 and 1,
# find the length of the longest contiguous subarray containing
# an equal number of zeros and ones.
# Example: [0, 1, 0, 0, 1, 1, 0]
# Output: 6
# --------------------------------------------------------------------------------------------
array = [0, 1, 0, 0, 1, 1, 0]
longest = 0
for i in array:
    zeros = 0
    ones = 0
    for j in range(i,len(array)):
        if array[j] == 0:
            zeros += 1
        else:
            ones += 1

        if zeros == ones:
            length = j - i +1
            if length > longest:
                longest = length
print(longest)

