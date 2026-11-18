print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: Merge two sorted arrays into the first array.
# The first array has enough empty space at the end. (Without Sorting)
#
# Input:
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
#
# Output: [1,2,2,3,5,6]
# --------------------------------------------------------------------------------------------
# ? I am getting Problem in How to deal with this 0's?
nums1 = [1, 2, 3, 0, 0, 0]

# Method : This is another Answer I got just trying to implement while concept...
nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
result = []
i = 0
j = 0

while i<len(nums1) and j<len(nums2):
    if nums1[i]<=nums2[j]:
        result.append(nums1[i])
        i += 1
    elif nums1[i]>nums2[j]:
        result.append(nums2[j])
        j += 1
        # ? Problem : After merging, append leftover elements 
        # ? with `while i < len(nums1)` and `while j < len(nums2)`.
# Add Remaining Elements from nums1
while i<len(nums1):
    result.append(nums1[i])
    i += 1
# Add Remaining Elements from nums2
while j<len(nums2):
    result.append(nums2[j])
    j += 1
print(result)

# ---------------------------------------------------------------------------------
# * Method 2 : 
# Will come backwards and compare if bigger attach in place of 0
def merge(nums1,nums2):
    len_num2 = len(nums2)
    len_num1 = len(nums1)-len(nums2)                # Getting effective length
    len_total = len_num1 + len_num2                 # Merged array length

    i = len_num1-1                                  # Starting from Last
    j = len_num2-1
    k = len_total-1

    # We already have nums1 and we will add all nums2 elements in nums1
    # We are kind of comparing [1,2,3] and [2,5,6] and from last which is greater append at last

    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k-=1

    print(nums1)

merge([1, 2, 3, 0, 0, 0], [2, 5, 6])

# METHOD 1: Using Two Pointers + Extra Array
# Logic: Compare elements from the beginning of both arrays,
# append the smaller element, then append leftover elements.
# Time: O(n + m) | Space: O(n + m)

# METHOD 2: Using Three Pointers (In-Place, Backward)
# Logic: Start from the last valid elements of both arrays.
# Place the larger element at the end of nums1 and move backward.
# Continue until all nums2 elements are inserted.
# Time: O(n + m) | Space: O(1)

# CONCLUSION:
# Method 2 is optimal because it merges directly into nums1
# without using extra space or sorting.

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Problem: Return an array where each position contains the product of every other element.
# Do not use division.
#
# Example: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# --------------------------------------------------------------------------------------------

# Method 1 : Use Division Concept (Mathematical)
arr = [1, 2, 3, 4]
prod_all_elem = 1
# Collecting Product of all Elements
for elem in arr:
    prod_all_elem *= elem
# Dividing
result = []
for elem in arr:
    result.append(int(prod_all_elem/elem))
print(result)

# --------------------------------------------------------
# Method 2 : Pythonic Way (Loop)
result = []
for i in range(len(arr)):
    mul = 1
    for j in range(len(arr)):
        if i != j:
            mul = mul * arr[j]
    result.append(mul)
print(result)

# --------------------------------------------------------
# * Method 3 : 
# We will get the left product and right product
# I will loop through each element and get left product
arr = [1, 2, 3, 4]
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
                                    # PASS 1: Calculate all LEFT products
                                    # As we move left to right, we store the running product of elements before index 'i'
    left_product = 1                # For leftmost element ; left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
                                    # PASS 2: Calculate all RIGHT products & multiply with LEFT products
                                    # As we move right to left, we track the running product of elements after index 'i'
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product          # Why here *= b/c we have to multiply with existing left_prod
        right_product *= nums[i]
        
    return result
print(product_except_self(arr))

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Find the indices of two elements whose sum equals to the target.
# Example : [2,7,11,15], target = 9
# Condition : Use maximum 1 loop
# --------------------------------------------------------------------------------------------
arr = [2, 7, 11, 15]
target = 9

def sum_find(arr, target):
    seen = {}                                    # Hash map to store {value: index}
    
    for i in range(len(arr)):
        complement = target - arr[i]             # The missing number needed to hit the target
        
        if complement in seen:                   # O(1) instant lookup to see if we passed it already
            return (seen[complement], i)         # Match found: return saved index and current index

        seen[arr[i]] = i                         # No match yet: save current number and its index to the map
    return ()

print(sum_find(arr, target))

# ? But Here taking the element in next step? 
# Yes, for adding two first num will get registered first, in 2nd num find we will identify

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Find the minimum element in a rotated sorted array containing distinct elements.
# Example : [3,4,5,1,2]
# 1 - Brute Force
# 2 - Optimised
# --------------------------------------------------------------------------------------------
# Method 1:
# Loop through 2nd --> 2nd last elem & check if elem lower than both side
# ! Problem : If elem present in leftmost or, rightmost --> It will Fail
# Solution : Include the leftmost and rightmost case separately
arr = [3,4,5,1,2]
def find_min_brute(arr):
    for i in range(1, len(arr)-1):
        if (arr[i]<arr[i-1]) and (arr[i]<arr[i+1]):
            return arr[i]
    return min(arr[0], arr[-1])

print(find_min_brute([3, 4, 5, 1, 2]))
print(find_min_brute([1, 2, 3, 4, 5]))
print(find_min_brute([2, 3, 4, 5, 1]))
print(find_min_brute([2]))

# -----------------------------------------------------------------------
# Method 2 :
# We will find the point where elem is smaller than left part 
# ! Problem : it will not take the leftmost elem
# Solution : if not return anything then it must be the leftmost
def find_min_brute(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return arr[i]
    return arr[0]
print(find_min_brute([3, 4, 5, 1, 2]))
print(find_min_brute([1, 2, 3, 4, 5]))
print(find_min_brute([2, 3, 4, 5, 1]))
print(find_min_brute([2]))

# -----------------------------------------------------------------------
# Method 3 : Two Pointer Search
# ! Problem : For single elem arr -- i = j = 0 --> will fail
# Solution : minimum = arr[0] rather than float(inf)
def find_min_two_pointers(arr):
    i = 0
    j = len(arr) - 1
    
    minimum = arr[0] 
    
    while i < j:
        if arr[i] < arr[j]:
            j -= 1
            minimum = min(arr[i], minimum)
        elif arr[i] > arr[j]:
            i += 1
            minimum = min(arr[j], minimum)
        else: 
            # arr[i] == arr[j]
            # We can safely shrink the window from either side
            j -= 1 
            minimum = min(arr[j], minimum)
    return minimum

print(find_min_two_pointers([3, 4, 5, 1, 2])) # Outputs 1
print(find_min_two_pointers([5]))             # Outputs 5

# -----------------------------------------------------------------------
# * Method 4 : Binary Search (Optimised)
def find_min_binary(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right)//2

        # If mid element is greater than the rightmost elem,
        # array must be rotated in right half => min must be in righ
        if arr[mid] > arr[right]:
            left = mid + 1
        
        # Otherwise, right half is sorted
        # The min is either at mid, or at left
        else:
            right = mid
    
    # When left = right we have narrowed down to single minimum element
    return arr[left]
print(find_min_binary([3, 4, 5, 1, 2]))
print(find_min_binary([1, 2, 3, 4, 5]))
print(find_min_binary([2, 3, 4, 5, 1]))
print(find_min_binary([2]))