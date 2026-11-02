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

print("----------------------10-----------------------")
# --------------------------------------------------------------------------------------------
# (VVI)
# Find the Minimum Length Subarray with Sum at Least S
# Problem statement: Given an array of positive integers and a target S,
# find the minimum length of a contiguous subarray whose sum is at least S.
# Print 0 if no such subarray exists.
# Example: [2, 3, 1, 2, 4, 3], S = 7
# Output : [4,3] --> 2
# --------------------------------------------------------------------------------------------
min_length = float('inf')
# Why ? whenever we need minimum we will initialize with maximum possible value...easy for later
# Why ? whenever we need maximum we will initialize with minimum possible value...easy for later

array = [2, 3, 1, 2, 4, 3]
S = 7

for i in range(len(array)):
    total = 0
    for j in range(i,len(array)):
        total = total + array[j]

        if total >= S:
            length = j - i + 1
            if length < min_length:
                min_length = length
                break

print(length)

print("----------------------11-----------------------")
# ========== MAXIMUM PRODUCT OF TWO ELEMENTS ==========
# * VVI
# --------------------------------------------------------------------------------------------
# Find the Maximum Product of Two Elements
# Problem statement:
# Find the maximum product obtainable by multiplying two elements at different indices.
# The array may contain positive and negative integers.
# Example: [-10, -3, 5, 6, -2]
# --------------------------------------------------------------------------------------------

array = [-10, -3, 5, 6, -2]


# METHOD 1: Brute Force (Direct Comparison)
# Logic: Multiply every element with every other element.
# Problem: Checks the same pair twice (a*b and b*a).
# Time: O(n²) | Space: O(n) for storing pairs.
# Best for: Understanding brute-force logic.

max_product = float('-inf')
products = []

for i in range(len(array)):
    for j in range(len(array)):
        if i != j:
            prod = array[i] * array[j]
            if prod > max_product:
                max_product = prod
                products.append((array[i], array[j]))

print(max_product)

# -----------------------------------------------------------
# METHOD 2: Optimized Brute Force (Index Comparison)
# Logic: Start j from i+1 to avoid duplicate pairs.
# Every pair is checked exactly once.
# Time: O(n²) | Space: O(1)
# Best for: Avoiding unnecessary comparisons.

max_product = float('-inf')

for i in range(len(array)):
    for j in range(i+1, len(array)):
        prod = array[i] * array[j]
        if prod > max_product:
            max_product = prod

print(max_product)


# -----------------------------------------------------------
# * VVI
# METHOD 3: Tracking Two Largest and Two Smallest
# Logic: Track the two largest and two smallest numbers.
# Two negative numbers can also produce the maximum positive product.
# max1, max2 = Two largest numbers.
# min1, min2 = Two smallest numbers.
# Time: O(n) | Space: O(1)
# Best for: Optimal algorithmic solution (Single Pass).

max1 = max2 = float('-inf')
min1 = min2 = float('inf')

for x in array:
    # --- Tracking the Top 2 Largest Values ---
    # If x is greater than our current largest value
    if x > max1:
        max2 = max1       # Old largest shifts to second largest
        max1 = x          # Update the new largest value
    # If x is smaller than max1 but greater than our 2nd largest
    elif x > max2:
        max2 = x          # Update the new second largest value

    # --- Tracking the Top 2 Smallest Values ---
    # If x is smaller than our current smallest value
    if x < min1:
        min2 = min1       # Old smallest shifts to second smallest
        min1 = x          # Update the new smallest value
    # If x is greater than min1 but smaller than our 2nd smallest
    elif x < min2:
        min2 = x          # Update the new second smallest value


max_product = max(max1 * max2, min1 * min2)
print(max_product)


# -----------------------------------------------------------
# METHOD 4: Sorting Approach
# Logic: Sort the array in ascending order.
# Maximum product = max(product of first two, last two).
# Why? Two smallest negatives or two largest positives
# can produce the maximum product.
# Time: O(n log n) | Space: O(1) auxiliary space*
# Best for: Simple implementation using sorting.

array.sort()

first_two_prod = array[0] * array[1]
last_two_prod = array[-1] * array[-2]

max_product = max(first_two_prod, last_two_prod)
print(max_product)


# ========== CONCLUSION ==========

# Method 1: Checks duplicate pairs unnecessarily.
# Method 2: Checks each pair only once.
# Method 3: Tracks extreme values without sorting.
# Method 4: Sorts the array and compares extreme pairs.

# Method 1 & 2: O(n²) time.u
# Method 3: O(n) time | O(1) space.
# Method 4: O(n log n) time.

# Method 3 is the most time-efficient.
# Method 4 is simpler but requires sorting.

# IMPORTANT:
# At least two elements are required.
# Method 4 modifies the original array.
# *Sorting space complexity depends on Python's sorting implementation.

print("----------------------12-----------------------")
# --------------------------------------------------------------------------------------------
# *? VVI
# ========== MINIMUM ABSOLUTE SUM OF TWO ELEMENTS ==========
# Find the Minimum Absolute Sum of Two Elements
# Problem statement: Find two elements at different indices whose sum has the smallest absolute value.
# Example: [-8, 4, 5, -2, 10]
# --------------------------------------------------------------------------------------------

array = [-8, 4, 0, 5, -2, 10]


# METHOD 1: Brute Force (Nested Loops)
# Logic: Check every unique pair and calculate absolute sum.
# Update minimum whenever a smaller absolute sum is found.
# Time: O(n²) | Space: O(1)
# Best for: Understanding the problem and checking all pairs.

min_sum = float('inf')

for i in range(len(array)):
    for j in range(i+1, len(array)):
        abs_sum = abs(array[i] + array[j])
        if abs_sum < min_sum:
            min_sum = abs_sum

print(min_sum)

# --------------------------------------------------------------
# *! METHOD 2: Sorting + Two Pointers
# Logic: Sort the array first.
# Use left and right pointers at opposite ends.
# If sum is positive, move right pointer left.
# If sum is negative, move left pointer right.
# If sum is zero, we have the minimum possible answer.
# Time: O(n log n) | Space: O(1) auxiliary*
# Best for: Efficient solution using Two Pointers.



# Step 1: Sort the array in non-decreasing order.
# Sorting enables a greedy two-pointer strategy because values on the left
# are smaller (more negative/less positive) and values on the right are larger.
# Time Complexity: O(n log n)
array.sort()

# Step 2: Initialize two pointers at opposite extremes.
left = 0                  # Points to the smallest available element
right = len(array) - 1    # Points to the largest available element

# min_sum tracks the smallest absolute difference from 0 encountered so far.
min_sum = float('inf')

# Step 3: Shrink the window inward until the two pointers meet.
while left < right:
    # Calculate the algebraic sum of the current pair.
    current_sum = array[left] + array[right]

    # Update min_sum with the magnitude (absolute value) of current_sum.
    # Closest to zero means minimizing abs(current_sum).
    min_sum = min(min_sum, abs(current_sum))

    # Step 4: Decide which pointer to move based on the direction of current_sum.
    if current_sum > 0:
        # The sum is too positive. To pull the sum closer to 0,
        # decrease the larger value by moving the right pointer inward.
        right -= 1

    elif current_sum < 0:
        # The sum is too negative. To push the sum closer to 0,
        # increase the smaller value by moving the left pointer inward.
        left += 1

    else:
        # current_sum == 0 is the theoretical minimum absolute sum possible.
        # No further pair can beat 0, so exit early.
        min_sum = 0
        break

# Step 5: Output the result.
print(min_sum)

# ========== CONCLUSION ==========

# Method 1: Checks every possible pair.
# Method 2: Uses sorting + Two Pointers.
# Method 1: O(n²) time | O(1) space.
# Method 2: O(n log n) time | O(1) auxiliary space*.

# Method 1: Simple but slower for large arrays.
# Method 2: More efficient for large arrays.
# Important: At least two elements are required.
# *Python sorting uses additional internal memory.


# ! Case Thinking -- Wrong
# all are positive --> lowest 2 ka sum
# all are negative --> highest 2 ka sum
# positive + negative --> lowest 2 ka sum > 0 , highest 2ka sum<0 , max+ min 

# Why? one positive and one negative sum absolute can be include..

print("----------------------13-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Number of Triplets with a Given Sum
# Problem statement: Count all triplets at three distinct indices whose sum equals a target value.
# Example: [1, 2, 3, 4, 5], target 9
# Output:
# --------------------------------------------------------------------------------------------
array = [1, 2, 3, 4, 5]
target = 9
triplet = []
length = len(array)
for i in range(length):
    for j in range(i+1,length):
        for z in range(j+1,length):
            sum = array[i] + array[j] + array[z]
            if sum == target:
                triplet.append((i,j,z))
print(triplet)

print("----------------------14-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Find the Longest Mountain in an Array
# Problem statement:
# A mountain is a contiguous sequence that strictly increases to a peak and then strictly decreases.
# Find the length of the longest mountain.
# A valid mountain must contain at least three elements.
# Example: [2, 1, 4, 7, 3, 2, 5]
# Output:
# --------------------------------------------------------------------------------------------
# thinking -- i will separate out a list where every element is increasing -- 
# Find indexes where the change is occuring
#   element is < previous and <next --> Lower
#   element is > previuos and > next  --> Upper Peak

# Find Peak where leftside increases and rightside decreases frequently

array = [2, 1, 4, 7, 3, 2, 5]
n = len(array)
longest = 0

# Step 1: Mountains require at least 3 elements, so peaks can only exist from index 1 to n-2.
for i in range(1, n - 1):
    # Step 2: Check if current element is a peak (strictly greater than both neighbors).
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        left = i
        right = i
        
        # Step 3: Expand leftward while the sequence strictly decreases going backward.
        while left > 0 and array[left - 1] < array[left]:
            left -= 1
            
        # Step 4: Expand rightward while the sequence strictly decreases going forward.
        # Boundary guard: Ensure right < n - 1 to prevent array[right + 1] IndexError.
        while right < n - 1 and array[right] > array[right + 1]:
            right += 1
            
        # Step 5: Calculate current mountain length and update maximum found so far.
        length = right - left + 1
        if length > longest:
            longest = length

print("Longest Mountain :", longest)

# ========== CONCLUSION ==========
# Review of your logic
# 1. Find a peak: array[i] > array[i-1] and array[i] > array[i+1].
# 2. Expand left while elements are strictly increasing towards the peak.
# 3. Expand right while elements are strictly decreasing from the peak.
# 4. Calculate the mountain length and update longest.

print("----------------------15-----------------------")
# ========== FIRST NON-REPEATING ELEMENT ==========
# --------------------------------------------------------------------------------------------
# Find the First Non-Repeating Element
# Problem statement: Find the first element whose frequency is exactly 1.
# Input:
# 4 5 4 6 5 7 6
# --------------------------------------------------------------------------------------------
array = [4,5,4,8,6,5,7,6]
dic = {}
for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(list(dic.keys()))
print(list(dic.values()))
for x in dic.keys():
    if dic[x]==1:
        print(x)
        break

# Method 2
for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            count+=1
    if count == 1:
        print(array[i])
        break

# ========== CONCLUSION ==========
# METHOD 1: Frequency Dictionary (Hash Map)
# Logic:
# 1. Traverse the array and store each element's frequency in a dictionary.
# 2. Traverse the dictionary in insertion order.
# 3. Return the first element whose frequency is 1.
# Time: O(n) | Space: O(n)
# Recommended: Efficient and preserves the original element order.

# METHOD 2: Brute Force (Nested Loops)
# Logic:
# 1. Take each element and compare it with every other element.
# 2. Count its occurrences in the array.
# 3. If frequency is 1, return that element.
# Time: O(n²) | Space: O(1)
# Not recommended for large arrays due to repeated comparisons.