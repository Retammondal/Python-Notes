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

print("----------------------16-----------------------")
# --------------------------------------------------------------------------------------------
# Find the Previous Smaller Element
# Problem statement: For each element,
# find the nearest element to its left that is strictly smaller.
# If none exists, print -1.
# --------------------------------------------------------------------------------------------
# METHOD 01 :
array = [4,2,5,3,7]
result = []   # -1 for the first elemment as in left nothing exist
for i in range(-1, -(len(array)+1), -1):
    isExist = False
    for j in range(i-1, -(len(array)+1), -1):
        if (array[j]<array[i]):
            result.append(array[j])
            isExist = True
            break
    if (not isExist):
        result.append(-1)


result.reverse()        # reverse in place
print(result)

# --------------------------------------------------------------
# METHOD 02 :
arr=[4,2,5,3,7]
result = []
for i in range(len(arr)):
    isExist = False
    for j in range(i-1,-1,-1):
        if arr[j]<arr[i]:
            result.append(arr[j])
            isExist = True
            break
    if (not isExist):
        result.append(-1)
print(result)

# ========== PREVIOUS SMALLER ELEMENT ==========
# METHOD 1: Reverse Traversal (Negative Indexing)
# Logic: Traverse right to left, search for the nearest smaller element on the left, then reverse the result.
# Time: O(n²) | Space: O(n)
# Limitation: Complex indexing and extra reversal.

# METHOD 2: Nested Loops (Direct Indexing)
# Logic: Traverse left to right, search backward for the nearest smaller element.
# Time: O(n²) | Space: O(n)
# Better: Simpler and more readable than Method 1.


print("----------------------17-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# ========== BEST TIME TO BUY AND SELL ONCE ==========
# Find the Best Time to Buy and Sell Once
# Problem statement: Given daily stock prices,
# find the maximum profit possible by buying once and selling later.
# If no profit is possible, return 0.
# Example: [7, 1, 5, 3, 6, 4]
# Output:
# --------------------------------------------------------------------------------------------

# METHOD 1
prices = [7, 1, 5, 3, 6, 4]
max_profit = []
for i in range(len(prices)):
    maxP = 0
    for j in range(i+1,len(prices)):
        if prices[j]>prices[i]:
            profit = prices[j] - prices[i]
            if profit > maxP:
                maxP = profit
    max_profit.append(maxP)

print(max_profit)

# ------------------------------------------------------------
#* METHOD 2
# What if I only want to show the Max_profit for all?
prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')
max_profit = 0

for price in prices:
    # In every loop I am assuming it's my Selling Price & Buying Price as Min_Price
    profit = price - min_price
    if price<min_price:
        min_price = price               # Update the lowest buying price seen so far

    elif profit > max_profit:           # Calculate profit if sold today, 
        max_profit = profit             # and update max_profit if it's higher
print(max_profit)


# METHOD 1: Brute Force (Check Every Buy-Sell Pair)
# Logic:
# 1. Consider each day as a buying day.
# 2. Check every later day as a selling day.
# 3. Calculate profit and store the maximum profit for each buying day.
# Time: O(n²) | Space: O(n) for storing individual maximum profits.
# Useful for understanding all possible buy-sell combinations.
# Limitation: Repeated comparisons make it inefficient.

# METHOD 2: Single Pass (Track Minimum Price)
# Logic:
# 1. Track the lowest price seen so far (buying price).
# 2. Calculate potential profit at each day (selling today).
# 3. Update maximum profit if the new profit is higher.
# 4. Update minimum price for future buying opportunities.
# Time: O(n) | Space: O(1)
# Recommended: Most efficient approach.



print("----------------------18-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Find the Smallest Difference Between Two Sorted Arrays
# Problem statement: Given two arrays sorted in ascending order,
# find the smallest absolute difference between an element of the first array and an element of the second.
# Example: A = [1, 4, 8, 10], B = [2, 5, 9, 12]
# Output: 
# --------------------------------------------------------------------------------------------
# Method 1
# looping through array and check -- Tranditional Method
# -------------------------------------------------------------------------
# Method 2: Two-Pointer Approach
# Time Complexity: O(N + M) where N and M are lengths of arrays a and b.
# Space Complexity: O(1) as it operates in-place with pointers.

a = [1, 4, 8, 10]
b = [2, 5, 9, 12]

# Initialize two pointers at the beginning of both sorted arrays
i = 0
j = 0

# Assume the initial difference is the minimum
minimum = abs(a[0] - b[0])

# Traverse until we run out of elements in either array
while i < len(a) and j < len(b):
    # Calculate the absolute difference between the current elements
    diff = abs(a[i] - b[j])
    
    # Update the minimum difference found so far
    if diff < minimum:
        minimum = diff
    
    # THE CORE THINKING LOGIC:
    # Since both arrays are sorted in ascending order:
    # - If a[i] is smaller than b[j], incrementing 'j' would make b[j] even larger, 
    #   widening the gap between them. To bring them closer, we must move 'i' forward.
    # - Conversely, if b[j] is smaller or equal, we move 'j' forward to close the gap.
    if a[i] < b[j]:
        i += 1
    else:
        j += 1

# Output the smallest absolute difference found
print(minimum)  # Output: 1 (from pairs like |1-2|, |4-5|, |8-9|, |10-9|)

# * NOTE : Method 2 needs the both arrays to be sorted but Method 1 don't want that

print("----------------------19-----------------------")
# --------------------------------------------------------------------------------------------
# Count the Number of Inversions
# Problem statement: An inversion is a pair of indices (i, j) where i < j but arr[i] > arr[j].
# Count all inversions in the array.
# Example: [2, 4, 1, 3, 5]
# Output:
# --------------------------------------------------------------------------------------------
array = [2, 4, 1, 3, 5]
count = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            count += 1
print(count)

print("----------------------20-----------------------")
# --------------------------------------------------------------------------------------------
# GCD Using Euclidean Algorithm Problem :
# Problem: Find the greatest common divisor (GCD) of two positive integers
# using the Euclidean algorithm.
# input: 48, 18
# Output:
# 18 -> 1,2,3,6,9,18
# 48 -> 1,2,3,4,6,12,16,24,48
# Common Divisors -- 1,2,3,6
# Greatest Common Divisor (GCD) = 6
# --------------------------------------------------------------------------------------------
# METHOD 1: BruteForce Method
def findGCD(entry1, entry2):
    if entry1 > entry2:
        num1 = entry1
        num2 = entry2
    elif entry1 < entry2:
        num1 = entry2
        num2 = entry1

    gcd_num1 = []
    gcd_num2 = []
    gcd = []
    for i in range(1, num1+1):
        if num1 % i == 0:
            gcd_num1.append(i)
    for j in range(1, num2+1):
        if num2 % j == 0:
            gcd_num2.append(j)
            if j in gcd_num1:
                gcd.append(j)
        
    # print(gcd_num1)
    # print(gcd_num2)
    # print(gcd)
    print(max(gcd))
findGCD(48,18)
findGCD(18,48)

# ---------------------------------------------------
# METHOD 2:
input_arr = [18,48]

def find_gcd(arr):
    greatest_divisor = 1
    for i in range(1, min(arr)+1):
        if arr[0]%i ==0 and arr[1]%i == 0:
            greatest_divisor = i
    print(greatest_divisor)
    return greatest_divisor
find_gcd(input_arr)


# ========== GCD USING EUCLIDEAN ALGORITHM ==========

# METHOD 1: Brute Force (Common Divisors)
# Logic:
# 1. Find all divisors of both numbers.
# 2. Identify common divisors.
# 3. Return the greatest common divisor.
# Time: O(n) | Space: O(n) for storing divisor lists.
# Limitation: Creates unnecessary lists and checks many divisors.

# METHOD 2: Brute Force (Check Up to Minimum)
# Logic:
# 1. Iterate from 1 to the smaller number.
# 2. Check whether both numbers are divisible by the current number.
# 3. Update the greatest divisor found.
# Time: O(min(a,b)) | Space: O(1)
# Improvement: Avoids storing divisor lists, but still checks every number.


# ========== CONCLUSION ==========
# Method 1: Understands common divisors.
# Method 2: Improves space complexity.


print("----------------------21-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: Calculate the least common multiple of two positive integers.
# Use the relationship between LCM and GCD.
# input: 12, 18
# Output:
# 12 -> 12,24,36,48
# 18 -> 18,36,..
# Common Multiple -- 36,...
# Least Common Multiple (LCM) = 36
# --------------------------------------------------------------------------------------------

# Method 1 :
arr = [12,18]
i = 1
max_num_multiple = []
lcm = 0
while i>0 and i<5:
    num = min(arr)*i
    max_num_multiple.append(max(arr)*i)
    if num in max_num_multiple:
        lcm = num
        break
    i += 1
print(lcm)

# --------------------------------------------------------
# Method 2 :
# Relationship b/w GCD and LCM => a * b = GCD x LCM
a,b = 12,18

gcd = find_gcd([a,b])
lcm = (a*b)//gcd
print(lcm)

# METHOD 1: Brute Force (Common Multiples)
# Logic: Generate multiples of the smaller number and check which is divisible by the larger number.
# Time: O(a*b) worst case | Space: O(1)
# Limitation: Repeated checking; inefficient.

# METHOD 2: GCD-LCM Relationship
# Logic: Calculate GCD first, then use LCM = (a * b) // GCD.
# Time: O(log(min(a,b))) | Space: O(1)
# Recommended: Efficient approach using Euclidean GCD.

print("----------------------21-----------------------")
# --------------------------------------------------------------------------------------------
# Problem: Determine whether a number greater than 1 is prime.
# Use trial division only up to its square root.
# --------------------------------------------------------------------------------------------
num = 29
def prime_check(number):
    sq_root_num = int(number ** 0.5)   
    for i in range(2,sq_root_num+1):
        if number % i == 0 :
            print("Not Prime")
            return
    print("Prime")
prime_check(num)


# Method 2:
num = 29

def prime_check(num):
    is_Prime = num>1          # by default coming to be true
    i = 2

    while i*i <= num:
        if num % i == 0:
            is_Prime = False
            break
        i+=1
    # print("Prime" if is_Prime else "Not Prime")
    # return "Prime" if is_Prime else "Not Prime"
    return True if is_Prime else False

prime_check(num)
print(prime_check(num))

# METHOD 1: Trial Division (Using Square Root)
# Logic: Check divisibility from 2 up to the square root of the number.
# Time: O(√n) | Space: O(1)
# Limitation: Calculates square root separately.

# METHOD 2: Trial Division (Using i * i)
# Logic: Check divisibility while i * i <= num. Stop if a divisor is found.
# Time: O(√n) | Space: O(1)
# Recommended: Avoids square-root calculation and returns a Boolean.

# CONCLUSION:
# Both methods have the same complexity. Method 2 is slightly cleaner.

print("----------------------22-----------------------")
# --------------------------------------------------------------------------------------------
# Given two integers L and R, print all prime numbers in the inclusive range.
# --------------------------------------------------------------------------------------------
low,high = 10,25
arr = []
for i in range(low,high+1):
    if(prime_check(i)):
        arr.append(i)
print(arr)


print("----------------------23-----------------------")
# --------------------------------------------------------------------------------------------
# Problem:
# Each row and each column of a matrix is sorted in ascending order.
# Determine whether a target exists. Use the efficient top-right-corner approach.
# Example: Matrix [[1,4,7],[2,5,8],[3,6,9]], target 6
# 1- Try to do with 2 loops
# 2 - Try to do with 1 loop onl
# --------------------------------------------------------------------------------------------
# Method 1 : We can do by going through 2 loop & get value by array[i][j]
# Method 2 : Use the fact that Matrix is sorted
matrix = [[1,4,7],[2,5,8],[3,6,9]]
import numpy as np
matrix_np = np.array(matrix)
print(matrix_np)

# Convert it to like this
# 1 4 7
# 2 5 8
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

matrix = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
target = 6
rows = len(matrix)
cols = len(matrix[0])

i,j = 0, cols-1
found = False

while i<rows and j>=0:
    if matrix[i][j] == target:
        found = True
        break
    elif matrix[i][j] > target:
        j -= 1
    else: 
        i += 1
print("Found" if found else "Not Found")

# METHOD 1: Brute Force (Nested Loops)
# Logic: Traverse every row and column to find the target.
# Time: O(rows * cols) | Space: O(1)
# Simple but inefficient for large matrices.

# METHOD 2: Staircase Search (Top-Right Corner)
# Logic: Start at the top-right corner.
# If current > target, move left.
# If current < target, move down.
# Time: O(rows + cols) | Space: O(1)
# Recommended: Uses sorted rows and columns to eliminate possibilities.

# CONCLUSION:
# Method 1: Checks every element.
# Method 2: Searches efficiently using one loop.


print("----------------------24-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem:
# Repeatedly add the digits of a positive integer untill only one digit remains
# Input : 9875
# 9875 --> 9+8+7+5 = 29
# 29 --> 2+9 = 11
# 11 --> 1+1 = 2
# --------------------------------------------------------------------------------------------
# METHOD 1

# Initial State
num = 9875
n = len(str(abs(num)))          # 4

                                                # Keep breaking the number down until only 1 digit is left
while n>1:
    sum = 0
    for n in str(num):
        sum = sum + int(n)
    num = sum
    n = len(str(sum))                           # Count digits of the new sum to check if we loop again
print(sum)

# -------------------------------------------------------------------
# * Method 2
num = 9875

                                                # Outer loop: repeats until 'num' is reduced to a single digit (< 10)
while num >= 10:        
    digit_sum = 0    
                                                # Inner loop: extracts and sums every digit of 'num'
    while num > 0:
        digit_sum = digit_sum + num % 10        # num % 10 gets the last digit
        num = num // 10                         # num // 10 removes the last digit
    num = digit_sum                             # Update 'num' with the sum for the next round

print(num)  # Output: 2

# ========== REPEATED DIGIT SUM ==========

# METHOD 1: String Conversion (Convert Digits to String)
# Logic:
# 1. Convert the number into a string to access individual digits.
# 2. Convert each digit back to integer and calculate their sum.
# 3. Repeat until the sum contains only one digit.
# Limitation: Repeated string conversions are required.

# METHOD 2: Mathematical Approach (Modulo and Floor Division)
# Logic:
# * 1. Use num % 10 to extract the last digit.
# * 2. Use num // 10 to remove the last digit.
# 3. Repeat until all digits are added.
# 4. Replace num with digit_sum and repeat until num < 10.
# Recommended: Avoids string conversion and extra storage.

print("----------------------25-----------------------")
# --------------------------------------------------------------------------------------------
# Problem:
# Given a Positive number, count the number of digits in it
# 1456 --> 4
# --------------------------------------------------------------------------------------------
num = 1456
current_num = num
count = 0
while current_num > 0:
    current_num = current_num // 10         # Removing the last one
    count += 1                                # adding to sum
print(count)

print("----------------------26-----------------------")
# --------------------------------------------------------------------------------------------
# A number is an ArmString number 
# if the sum of each digit raised to the number of digits equals to the original number.
# Example : 153, d = 3
# 1^3 + 5^3 + 3^3 = 153 --> Armstrong
# --------------------------------------------------------------------------------------------
num = 1456
def is_armstring(number):
    current_num = number
    digit = []
    count = 0
    while current_num > 0:
        last_digit = current_num % 10         # Getting the last digit
        current_num //=10                     # Removing the last digit
        digit.append(last_digit)              # Adding last digit 
        count += 1

    digit_sum = 0
    for x in digit:
        digit_sum += x**3
    if digit_sum == number:
        return True
    else:
        return False
print(is_armstring(num))
print(is_armstring(153))

print("----------------------27-----------------------")
# --------------------------------------------------------------------------------------------

# Write a code to find the Factorial of a Given Number
# Recursive Method
# Iterative Method
# Example : 5! = 5*4*3*2*1
# --------------------------------------------------------------------------------------------
num = 5
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(factorial)

# Method 2 -> Recursive method
# Recursion --> A Function calling itself
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)                    # Each time it will call itself...untill 1/0 came

# ========== FACTORIAL OF A NUMBER ==========

# METHOD 1: Iterative Method (Using For Loop)
# Recommended: Simple and memory-efficient.

# METHOD 2: Recursive Method (Function Calling Itself)
# Logic:
# 1. Define a base case: if n == 0 or n == 1, return 1.
# 2. Otherwise, return n * fact(n-1).
# 3. Each function call reduces n until the base case is reached.
# Best for: Understanding recursion and problems with recursive structure.

print("----------------------28-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Find the Nth Fibonacci number
# Problem:
# The Fibonacci sequence starts with 0, 1.
# Each subsequent term is the sum of the previous two.
# Find the term at zero-based index N.
# n = 7, output: 13
# 0, 1, 1, 2, 3, 5, 8, 13,....
# --------------------------------------------------------------------------------------------

# METHOD 1 : Iterative Approach
prev_prev = 0           # Previous Previous Element
prev = 1                # Previous Element
current_element = 0 
term_index = 7
# Starting the Loop from 2nd index as 0th and 1st element = 1(We know)
for i in range(2,term_index+1):
    current_element = prev_prev + prev              # Current = sum(last two)

    # Setting things for Next Iteration
    # Prev --> converted to --> prev prev
    # Curr --> converted to --> prev
    prev_prev = prev
    prev = current_element

print(current_element)

# -------------------------------------------------------------------
# METHOD 2 : Recursive Method
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)              # Recursive Case
print(fibonacci(7))
print(fibonacci(4))             # 3


# RECURSION TREE VISUALIZATION: fib(4)
# -------------------------------------------------------------------
# Each non-leaf node evaluates its left child first, then its right child.
#
#                         fib(4)  -> Returns 3
#                        /      \
#                       /        \
#                 fib(3)          fib(2)  -> Returns 1
#                /      \         /     \
#               /        \     fib(1)  fib(0)
#           fib(2)      fib(1)   (1)     (0)
#          /      \       (1)
#       fib(1)  fib(0)
#        (1)     (0)
#
# Total calls: 9 calls to compute fib(4)
# Redundant work: fib(2) is calculated twice from scratch.
# ----------------------------------------------------------------------------

print("----------------------29-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Check whether two strings are anagrams
# Problem:
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.
# Assume the strings contain lowercase English letters.
# Example: Input: listen, silent
# Output:
# --------------------------------------------------------------------------------------------
# Method 1 : 
# Create a dictionary and check
def is_anagram(sample_str1, sample_str2):
    data_check = {}
    str1 = sample_str1.lower().strip()
    str2 = sample_str2.lower().strip()

    for i in str1:
        if i in data_check:
            data_check[i] += 1
        else:
            data_check[i] = 1
    for j in str2:
        if (j in data_check):
            data_check[j] -= 1
            if data_check[j] == 0:
                del data_check[j]
        else:
            return "not_anagram"
    if (not data_check):
        return "anagram"
    else:
        return "not_anagram"  # Explicitly handles cases where str1 is longer than str2

print(is_anagram("listen", "silent"))

# * Method 2 :
# Considering both string is in lowercase + No space inside/Outside
# ASCII Values
str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):        
    print("Not Anagram")
else:
    freq = [0]*26               # Creating list of 26 characters ; all 0

    # print(ord('a'))           # 97
    # print(ord('z'))           # 122

    for ch in str1:
        freq[ord(ch) - ord('a')] += 1       # Ques: for d it will come 3 
                                            # --> but in python 0-indexing ultimatly will get 4
    for ch in str2:
        freq[ord(ch) - ord('a')] -= 1
    
    if all(x == 0 for x in freq):
        print("Anagrams")
    else:
        print("Not Anagrams")

# METHOD 1: Frequency Dictionary (Single Hash Map)
# Logic: Increment character counts from str1, decrement using str2.
# Remove characters when their frequency becomes 0.

# METHOD 2: Character Frequency Array (ASCII)
# Logic: Create an array of 26 zeros.
# Increment frequency for str1 and decrement for str2 using ASCII indexes.
# If all values are 0, the strings are anagrams.

print("----------------------30-----------------------")
# --------------------------------------------------------------------------------------------
# Find the first non-repeating character in a string
# Problem:
# Find the first character that appears exactly once.
# If every character repeats, print None. Assume lowercase English letters.
# Use the ASCII Concept
# Example : Input : swiss
# --------------------------------------------------------------------------------------------
text = "swiss"
freq = [0]*26
for i in text:
    freq[ord(i) - ord('a')] += 1
answer = None
for j in text:
    if freq[ord(j) - ord('a')] == 1:
        answer = j
        break
print(answer if answer is not None else "None")

print("----------------------31-----------------------")
# --------------------------------------------------------------------------------------------
# Calculate the average of elements greater than a given value
# Problem statement:
# Given an array and a number K, calculate the average of all elements strictly greater than K.
# If no element qualifies, print No elements.
# Example: Array = [10, 25, 30, 15, 40], K = 20
# Output:
# --------------------------------------------------------------------------------------------
import numpy as np
array = [10, 25, 30, 15, 40]
final_arr = []
K = 20
for i in array:
    if i > K:
        final_arr.append(i)
# Handle the edge case where no elements qualify
if len(final_arr) > 0:
    avg = np.mean(final_arr).round(2)
    print(avg)
else:
    print("No elements")

print("----------------------32-----------------------")
# --------------------------------------------------------------------------------------------
# Find the difference between the sum of even and odd elements
# Problem statement: Calculate the sum of even-valued elements
# and the sum of odd-valued elements.
# Print the absolute difference between the two sums.
# Example: [2, 7, 4, 9, 6]
# Output:
# --------------------------------------------------------------------------------------------
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(5))       # False

array = [2, 7, 4, 9, 6]
even_sum = 0
odd_sum = 0
for i in array:
    if is_even(i):
        even_sum += i
    else:
        odd_sum += i
diff = abs(even_sum - odd_sum)
print(diff)

print("----------------------33-----------------------")
# --------------------------------------------------------------------------------------------
# Find the element closest to zero
# Problem statement: Given an array containing positive and negative integers,
# find the element whose absolute value is smallest.
# If two elements are equally close to zero, choose the positive one.
# Example: [-8, 3, -2, 5, 2]
# --------------------------------------------------------------------------------------------
array = [-8, 3, -2, 5, 2]
closest = float('inf')

for i in array:
    if abs(i) < abs(closest):       
        closest = i
    elif (abs(i) == abs(closest) and i > closest):
        closest = i
print(closest)

print("----------------------34-----------------------")
# --------------------------------------------------------------------------------------------
# Find the longest consecutive run of positive numbers
# Problem statement:
# Find the length of the longest contiguous sequence containing only positive numbers.
# Zero and negative values break the sequence.
# Example: [2, 3, -1, 4, 5, 6, 0, 8]
# Output:
# --------------------------------------------------------------------------------------------
array = [2, 3, -1, 4, 5, 6, 0, 8]

# Method 1
def long_run(array):
    longest_array = []
    longest = 0
    for i in array:
        if i > 0:
            longest += 1
        elif i <= 0:
            longest_array.append(longest)
            longest = 0
    longest_array.append(longest)           # appends if all positive comes at last
    return max(longest_array)
print(long_run(array))

# Method 2 :
def long_run(array):
    longest = 0
    current = 0
    for i in array:
        if i > 0:
            current += 1
            longest = max(current, longest)
        else:
            current = 0                     # longest will stay and current will be reset
    return longest
print(long_run(array))

# METHOD 1: Track Runs (Using Extra List)
# Logic: Count consecutive positive numbers and store each run length.
# Return the maximum run length.

# METHOD 2: Single Pass (Track Current and Longest)
# Logic: Increment current for positive numbers, reset on zero/negative.
# Update longest whenever current increases.

print("----------------------35-----------------------")
# --------------------------------------------------------------------------------------------
# Interleave two arrays
# Problem statement: Given two arrays of equal length,
# create a new array by alternating elements from each array, starting with the first array.
# Example: A = [1, 2, 3], B = [7, 8, 9]
# Output: [1, 7, 2, 8, 3, 9]
# --------------------------------------------------------------------------------------------
a = [1, 2, 3]
b = [7, 8, 9]
result = []

for i in range(len(a)):
    result.append(a[i])
    result.append(b[i])

print(result)

# Mentos Zindagi : Using Zip
a = [1, 2, 3]
b = [7, 8, 9]
result = []
for i,j in zip(a,b):
    # result.append(i,j)            --> Wrong ! or, use 2 times
    result.extend([i,j])
print(result)


print("----------------------36-----------------------")
# --------------------------------------------------------------------------------------------
# Find the longest word in a sentence
# Problem statement: Given a sentence containing words separated by spaces,
# print the longest word. If multiple words have the same maximum length, print the first one.
# Example: "Python makes coding enjoyable"
# Output:
# --------------------------------------------------------------------------------------------
sentence = "Python makes coding enjoyable"
words_list = sentence.split(" ")
print(words_list)

current = 0
longest = ("",0)
for text in words_list:
    current = len(text) 
    if current > longest[1]:
        longest = (text,current)
print(longest[0])

print("----------------------37-----------------------")
# --------------------------------------------------------------------------------------------
# Count uppercase and lowercase letters
# Problem statement: Given a string containing English letters,
# count the uppercase letters and lowercase letters separately.
# Ignore digits, spaces, and punctuation.
# Example: "Hello WORLD 123"
# Output:
# upper-case - 6
# lower-case - 4
# --------------------------------------------------------------------------------------------
sentence = "Hello  WORLD    123"
# need_sent = "".join(sentence.split(" "))
upper_case = 0
lower_case = 0
for x in sentence:
    if x.isupper():
        upper_case += 1
    elif x.islower():
        lower_case += 1
print(upper_case)
print(lower_case)

# MEthod 2 : 
upper_case = 0
lower_case = 0
for x in sentence:
    if 'A' <= x <= 'Z':             # * We already know this comparison happens based on ord(character)
        upper_case += 1
    elif 'a' <= x <= 'z':
        lower_case += 1
print(upper_case)
print(lower_case)

# METHOD 1: Built-in String Methods
# Logic: Use isupper() and islower() to identify and count letters.
# Recommended: Simple and readable.

# METHOD 2: Character Range Comparison (ASCII)
# Logic: Check whether each character falls between 'A'-'Z' or 'a'-'z'.
# Best for: Understanding character comparison using ASCII values.

# ? Mistake By me: Put else except elif?
# NO! B/c it will also count #,!,@ or, numbers will be taken to lower+=1; so use elif only..

print("----------------------38-----------------------")
# --------------------------------------------------------------------------------------------
# Remove all occurrences of a chosen pattern
# Problem statement: Given a string and a pattern,
# remove every occurrence of that pattern while preserving the order of the remaining characters.
# Example: String = "programming", character = "mi"
# output:
# --------------------------------------------------------------------------------------------
string = "programming"
updated = "".join(string.split("mi"))
updated = string.replace("mi","")
print(updated)