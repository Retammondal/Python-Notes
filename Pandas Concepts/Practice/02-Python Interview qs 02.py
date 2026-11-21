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

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: Given a sorted array where every element appears exactly twice
# except one element, find the element that appears only once.
#
# 1- brute force
# 2- optimal algo
# --------------------------------------------------------------------------------------------

# Method 1 :
# Will Count all the occurances
# Object.items() --> will iterate through it if last one = 1 , give 1st one
from collections import Counter
nums = [1,1,2,3,3,4,4,8,8]
count = Counter(nums)
result = None

for item,occurance in count.items():
    if occurance == 1:
        result = item
        break
print(result)

# -----------------------------------------------------------------------
# * Method 2 : Binary Search (Optimised)
# If all elem are twice twice --> it should be even no of array
# IF any one occurs one --> it should be odd no of array
def single_non_duplicate(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left+right) // 2
                                # Snap mid to an EVEN index so we always inspect the start of a pair.
                                # Before the single element, every valid pair sits at (even, odd).
        if mid % 2 == 1:
            mid -= 1

                                # If nums[mid] matches nums[mid + 1], the pairing is still intact up to here.
                                # That means the single element hasn't disrupted the order yet -> search right.
        if nums[mid] == nums[mid+1]:            # [1,1,2,2,3,4,4] --> elem is right side
            left = mid + 2

                                # The (even, odd) pairing is broken. Either nums[mid] IS the answer,
                                # or the single element appeared earlier -> keep mid and search left.
        else:
            right = mid
    return nums[left]
# ! Problem : Why mid%2 == 1 imp? mid will always come even?
# No!! Mid index will not always come even..

print(single_non_duplicate([1, 1, 2, 2, 3, 4, 4]))             # --> mid = 3 (odd) => here mid-1 imp!
print(single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]))       # --> mid = 4 (even)

print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# Problem: Given three sorted arrays, return all elements that appear in all three arrays.
#
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 5, 7, 9]
# arr3 = [1, 3, 4, 5, 8]
#
# Output:
# --------------------------------------------------------------------------------------------
# Method 1 :
def common_elements(a,b,c):
    i = j = k = 0
    result = []

    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            result.append(a[i])
            i, j, k = i + 1, j + 1, k + 1
        elif a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        else:
            k += 1
    return result
print(common_elements(
    [1, 2, 3, 4, 5],
    [1, 2, 5, 7, 9],
    [1, 3, 4, 5, 8]
))

# -------------------------------------------------------
# Method 2 :
# Simple way is using Set Data Structures
# Set Intersection : using & operator
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

result = set(arr1) & set(arr2) & set(arr3)
print(list(result))

print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# ! Little Doubt is there..
# Problem: Given arrival and departure times of trains,
# find the minimum number of platforms required so that no train has to wait.
#
# A platform can be reused when a train departs at the same time another arrives.
#
# Arrival:   [900, 940, 950, 1100, 1500, 1800]
# Departure: [910, 1200, 1120, 1130, 1900, 2000]
#
# Output: 3
# --------------------------------------------------------------------------------------------

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

def min_platforms(arrival, departure):
    arrival = sorted(arrival)       # Sort arrival times
    departure = sorted(departure)   # Sort departure times

    i = 1
    j = 0                       # Two pointers for arrival and departure

    current_platform = 1            # Currently occupied platforms (Minimum = 1)
    max_platform = 1                # Maximum platforms occupied at once (Minimum = 1)

    while i < len(arrival) and j < len(departure):

                                        # Previous one still not left, new One came -> Platform Added
        if arrival[i] < departure[j]:
            current_platform += 1
            i += 1

                                        # Next one came after previous one left.. 
        else:
            current_platform -= 1
            j += 1

                                        # Track the maximum platforms needed
        max_platform = max(max_platform, current_platform)

    return max_platform

print(min_platforms(arrival, departure))  # Output: 3

print("----------------------8-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: You start with a score of 1. You can either:
# - Double the current score.
# - Increase the current score by 1.
# Given a target, find the minimum number of moves required to reach it.
#
#
# target = 10
# --------------------------------------------------------------------------------------------
# Going Forward : First double if doubling not get target + 1
# ❌ Wrong? Why? Rather than that if we +1 then double --> moves are more minimum
def min_moves(score, target):
    moves = 0
    while score < target:
        if (score * 2) < target:
            score = score * 2
            moves += 1
        else:
            score += 1
            moves += 1
    return (score,moves)
print(min_moves(1,10))

# ✅ Correct Method : Reverse Greedy Approach
# Come Backward
# If target is odd -1 ; even / 2
# If target drops below score*2 => doubling is not possible directly give (target-score)
def min_moves(score,target):
    moves = 0
    while target > score:
        # First case if target becomes less than score * 2
        if target < (score * 2):
            moves += target - score
            break
        
        if target % 2 == 0:                 # Target is even
            target //= 2
        else:                               # Target is odd
            target -= 1
        moves += 1
    return moves
print(min_moves(1,10))
print(min_moves(1,1))
print(min_moves(1,15))
print(min_moves(0,10))

print("----------------------9-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: Given an integer array,
# find the maximum product possible by multiplying any three elements.
# Use Mathematical Logic
#
# Input: nums = [1, 2, 3, 4]
# Output: 24
# --------------------------------------------------------------------------------------------
# Mathematical Logic : Product of 3 largest element but it will fail if both +/- numbers are present
# [-10,-10,1,2,3] --> 1*2*3 ❌ --> -10*-10*3 ✅

# Two Ways 
# 1. Product of the 3 largest element
# 2. Sorting -> max(product of last 3 element or, product of smallest 2 and largest 1)
def max_product_3(arr):
    arr.sort()
    largest_products = 1
    for n in arr[-3:]:
        largest_products *= n

    large_smallest_products = arr[0]*arr[1]*arr[-1]

    return max(largest_products, large_smallest_products)
print(max_product_3([1, 2, 3, 4]))
print(max_product_3([-10,-10,1,2,3]))

print("----------------------10-----------------------")
# --------------------------------------------------------------------------------------------
# *VVI
# Problem: You are given an array representing card values.
# You can pick exactly k cards from either the beginning or the end.
# Find the maximum possible score (sum of the values).
#
# Input: cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
# Output: 12
# --------------------------------------------------------------------------------------------
# Wrong Thinking : I was think either first 3 or, last 3 ❌
# We can take both...
# We will get sum of first 3...then gradually remove one and add last one..and check max
def max_score(cardPoints, k):
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum

    for i in range(1,k+1):
        current_sum -= cardPoints[k-i]
        current_sum += cardPoints[-i]

        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_score([1, 2, 3, 4, 5, 6, 1], 3))

print("----------------------11-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem: Given an integer array,
# count the number of pairs (i, j) such that i < j and nums[i] == nums[j].
#
# Input: nums = [1, 2, 3, 1, 1, 3]
# Output: 4
# Indices : (0,3) (0,4) (3,4) (2,5)
# --------------------------------------------------------------------------------------------

# Method 1 : 2 Loops (Basic Method)
nums = [1, 2, 3, 1, 1, 3]
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            count += 1
print(count)

# -----------------------------------------
# * Method 2 :
# Here we need identical element later on...doesn't mean with positions
# * Good Pairs:
# A good pair is formed by choosing any two elements having equal values.
# 1,1,1
# How many good pairs can be formed ? -- 2 ❌ 3 ✅

# * Formula:
# Among n equal elements, the number of possible good pairs is:
# n * (n - 1) // 2

# Steps :
# First store the count of same identical element...when the identicality finishes count good pairs
def num_identical_pairs(nums):
    nums.sort()

    pairs = 0
    count = 1                                   # Will count identical elem 

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:                # If elems are identical add in count
            count += 1
        else:                                   # When the identicality ends, count the pairs
            pairs += count * (count - 1) // 2
            count = 1
    
    pairs += count * (count - 1) // 2           # Why? -- if count is in last

    return pairs
print(num_identical_pairs([1, 2, 3, 1, 1, 3]))

# 21 Nov 2026
print("----------------------12-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Sort an array containing only 0s, 1s and 2s without using a built-in sorting function.
#
# Example: [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]
# Without Sorting --> Linear Complexity
# --------------------------------------------------------------------------------------------
# Method 1 : 
# First Counting no. --> then create a new array by extending
arr = [2, 0, 2, 1, 1, 0, 1]
sample_arr = []
counter = Counter(arr)
sample_arr.extend([0]*counter[0])
sample_arr.extend([1]*counter[1])
sample_arr.extend([2]*counter[2])
print(sample_arr)

# -------------------------------------------------------------
# Method 2 :
# Same Step but adding in same array

index = 0                   # Starting with 0 index; one after one will add and increase this index
arr = [2, 0, 2, 1, 1, 0, 1]
counter = Counter(arr)
for i in range(counter[0]):
    arr[index] = 0
    index += 1
for i in range(counter[1]):
    arr[index] = 1
    index += 1
for i in range(counter[2]):
    arr[index] = 2
    index += 1
print(arr)
# * Note : Is here Loop is 3 times? - NO! it's one time on the array if you observe -- Linear Complexity
# ? But wait....Counter -- this will also be count as an Iteration -- ❌ Linear Complexity

# -------------------------------------------------------------
# * Method 3 : 1 Iteration : Dutch National Flag Algorithm (Three Pointers)
# Idea -> 
# Maintain 4 zones:
# [ 0 ... low-1 ] = 0s
# [ low...mid-1 ] = 1s
# [ mid...high ] => Unknown (To be checked)
# [ high=1 ... ] = 2s
def sort_array(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    # keep going untill the unknown zone is empty
    while mid <= high:
        if nums[mid] == 0:
            # make the low index = 0 but what about the value of that low --> need to again check in mid
            nums[low], nums[mid] = nums[mid], nums[low]         # Swapping value to recheck
            low += 1
            mid += 1
        elif nums[mid] == 1:                    # 1 belongs in the middle, so leave it and move on
            mid += 1
        else:                                   # if == 2
                                                            # Why to swap?
                                                            # i will swap that last value now last value need to check
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
print(sort_array([2, 0, 2, 1, 1, 0, 1]))

# METHOD 1: Using Counter + Extra Array
# Logic: Count occurrences of 0, 1 and 2, then extend a new array
# with the required number of each element.
# Time: O(n) | Space: O(n)

# METHOD 2: Using Counter + In-Place Overwriting
# Logic: Count occurrences, then overwrite the original array
# with all 0s, followed by 1s and 2s.
# Time: O(n) | Space: O(1) auxiliary space

# METHOD 3: Dutch National Flag Algorithm (Three Pointers)
# Logic: Maintain three pointers (low, mid, high) to divide the
# array into 0s, 1s, 2s and an unknown region. Sort using swaps.
# Time: O(n) | Space: O(1)

print("----------------------13-----------------------")
# --------------------------------------------------------------------------------------------
# Given an array of length n containing values from 1 to n, find all numbers missing from the array.
# Duplicates has been created in place of missing contents

# Example: [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [5,6]
# --------------------------------------------------------------------------------------------
# If you remember we have done this question using Sum of n Natural no...
# But here it's not going to work, as multiple numbers missing

# Method 1 :
# Create a array from 1-n --> just compare using while loop

# ------------------------------------------------------------------------------
# Method 2 :
def find_disappeared(nums):
    present = set(nums)
    result = []

    for i in range(1,len(nums)+1):          # going from 1-n each numbers
        if i not in present:
            result.append(i)
    return result
print(find_disappeared([4, 3, 2, 7, 8, 2, 3, 1]))

# ------------------------------------------------------------------------------
# Method 3 : (Mentos Zindagi)
# Using Set
given_arr = [4, 3, 2, 7, 8, 2, 3, 1]
given_arr = set(given_arr)
taken_arr = set(range(1,max(given_arr)+1))
diff = taken_arr - given_arr
print(given_arr)
print(taken_arr)
print(diff)

# * Note whenever unique occurances waala sawaal came --> Best is Set Data Structures

# METHOD 1: Using Comparison (Brute Force)
# Logic: Generate numbers from 1 to n and check each number
# against the original array.
# Time: O(n²) | Space: O(n) for the result

# METHOD 2: Using Set + Loop
# Logic: Convert the array into a set for fast lookup, then
# check which numbers from 1 to n are missing.
# Time: O(n) average | Space: O(n)

# METHOD 3: Using Set Difference
# Logic: Create a set containing numbers from 1 to n,
# then subtract the set of present numbers.
# Time: O(n) average | Space: O(n)

print("----------------------14-----------------------")
# --------------------------------------------------------------------------------------------
# Problem statement: Given a lowercase English string and an integer k,
# find the maximum number of vowels in any contiguous substring of length k.
#
# Input: s = "abciiidef", k = 3
# Output: 3
# --------------------------------------------------------------------------------------------
# Method 1 :
# We all know...iterating and get max and current

# Method 2 :
# take a window of k lenght and go one after one and check max vowels within it
def max_vowels(string,k):
    vowels = "aeiou"

    current = sum(1 for chr in string[:k] if chr in vowels)         # Window of first k elements
    max_vowel = current

    for i in range(k, len(string)):
        if string[i] in vowels:                 # If coming elem is vowel add in current
            current += 1
        
        if string[i-k] in vowels:               # If removing elem was also vowel, remove from current
            current -= 1
        
        max_vowel = max(max_vowel, current)
    return max_vowel     

print(max_vowels("abciiidef", 3))

print("----------------------15-----------------------")
# --------------------------------------------------------------------------------------------
# * VVI
# Problem statement: Given an array of strings,
# find the longest suffix shared by all strings.
# If no common suffix exists, return an empty string.
#
# Input: words = ["running", "jogging", "walking"]
# Output:
# --------------------------------------------------------------------------------------------

# METHOD : Reverse Strings + Common Prefix
# Logic: Reverse the first string, then compare it with every
# other reversed string and keep only the matching prefix.
# Finally, reverse the remaining prefix to get the common suffix.

def longest_suffix(words):
    suffix = words[0][::-1]                 # Flipping the words --> To make it Prefix Problem
    
    for word in words[1:]:
        word = word[::-1]                   # Flipping
        i = 0

                                            # Move forward while inside both words and letters match
        while i < min(len(suffix),len(word)):
            if suffix[i] == word[i]:
                i += 1
            else:
                break
        
        suffix = suffix[:i]                 # Trim to only the shared matching part
    return suffix[::-1]
print(longest_suffix(["running", "jogging", "walking"]))

print("----------------------16-----------------------")
# --------------------------------------------------------------------------------------------
# * Did on my own, but Good Question
# Problem statement: Given a string,
# determine whether it can be constructed by repeating one of its proper non-empty substrings multiple times
#
# Input: s = "abababab"
# Output: Yes (ab x 2)
# --------------------------------------------------------------------------------------------
def repeating_substring(string):
    n = len(string)
    for i in range(1, n//2+1):                          # i is the length of substring
        if n % i == 0:                                  # string len is dividable substring length 
            substring = string[:i]
            repeats = n // i
            if string == substring * repeats:
                return f"Yes ({substring} x {repeats})"
    return "No"
    
print(repeating_substring("abababab"))    # Yes (ab x 4)
print(repeating_substring("abab"))        # Yes (ab x 2)
print(repeating_substring("abcabc"))      # Yes (abc x 2)
print(repeating_substring("aba"))         # No
print(repeating_substring("a"))           # No
print(repeating_substring("abcab"))       # No
