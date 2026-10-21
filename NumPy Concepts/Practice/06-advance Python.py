print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Problem statement:
# An array contains distinct numbers from 1 to n,
# but one number is missing. Find the missing number.

# Input: [1,2,3,4,6]
# Output: 5
# --------------------------------------------------------------------------------------------

# Method 1 : 
num = [1,2,3,4,6,8,9]       # n=9
n = 9
def missing_num(arr, n):
    cont_num = list(range(1, n+1))
    missing_num = []
    for i in cont_num:
        if i not in arr:
            missing_num.append(i)
    return missing_num
print(missing_num(num,n))

# -------------------------------------------------------------------
# Method 2 : 
# Thinking : if some is missing will be not included in sum of all
# Drawback : Applicable only if 1 number missing
def find_missing(num,n):
    # sum of first n natural number : n(n+1) /2
    expected_sum = n*(n+1)//2   # Uses integer division (//) to get a whole number
    actual_sum = sum(num)

    return expected_sum - actual_sum

array = [1,2,3,4,5,7,8,9]
print(find_missing(array,n))
print(missing_num(array,n))


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Question (VVI)
# Find Two Numbers Whose Sum Equals a Target

# Problem statement:
# Given an array and a target value,
# return the indices of two distinct elements whose sum equals the target.
# Assume exactly one valid pair exists.

# Input : arr = [2,7,11,15]; target=9
# --------------------------------------------------------------------------------------------
arr = [2,7,11,15]
target = 26

def two_sum_find(arr, target):
    found = False
    length = len(arr)

    for i in range(length):
        for j in range(length):
            if (arr[i]+arr[j])==target:
                return (i,j)
                found = True
        if (found):
            break
    if (not found):
        return ()
# Method 2 : 
def two_sum(arr, target):
    seen = {}
    for i,num in enumerate(arr):
        required = target-num
        if required in seen:
            return (seen[required], i)

        seen[num] = i
        # storing the number in seen Object { number : key }
    return ()       # if nothing happens returns [] array

print(two_sum(arr,target))
print(two_sum_find(arr,target))

# -----------------------------------------------------------------------------------------
# Concept : Python's Built-in enumerate() Function
# -----------------------------------------------------------------------------------------
# 1. Purpose:
#    - Allows iterating over an iterable (list, tuple, string) while automatically keeping
#      track of the index of the current item.
#    - Eliminates the need to maintain an external counter variable (e.g., i = 0 ... i += 1)
#      or using the unpythonic `range(len(arr))`.
#
# 2. Syntax & Return Value:
#    - enumerate(iterable, start=0)
#    - Returns an enumerate object (iterator of tuples): (index, element).
#    - Unpacking syntax: `for i, num in enumerate(arr):`
#        * `i`   -> current index
#        * `num` -> current element at that index
#
# 3. Why it is critical in "Two Sum":
#    - The problem requires returning the *indices* of the two numbers, not just the numbers.
#    - `num` gives the current value to calculate `required = target - num`.
#    - `i` gives the index needed to return `(seen[required], i)` or save to `seen[num] = i`.
# -----------------------------------------------------------------------------------------

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Palindrome Problem :
# Problem statement: Determine whether a string reads the same forward and backward.
# Ignore spaces, punctuation, and differences between uppercase and lowercase letters.
# Case 1 : Only lowercase alphabets
# Case 2 : any character is present
# --------------------------------------------------------------------------------------------
string1 = "retammater"
def pal_check(string_input):
    # case sensitivity
    string = ""
    for i in (string_input).lower():
        if i.isalnum():
            string += i

    length = len(string)        # e.g. 7
    check = length//2           # e.g. 3
    isPalindrome = True

    for i in range(check):
        if string[i] != string[-(i+1)]:
            isPalindrome=False
            break
    if (isPalindrome):
        return "Yes"
    else:
        return "No"

# Method 2
def pal_check_easy(string_input):
    # case sensitivity
    string = ""
    for i in (string_input).lower():
        if i.isalnum():
            string += i
    rev_string = string[::-1]
    if string == rev_string:
        return "Yes"
    else :
        return "No"


print(pal_check(string1))
print(pal_check("a@bb@a"))
print(pal_check_easy(string1))
print(pal_check_easy("A@#BB#@a"))


print(pal_check("A man, a plan, a canal: Panama"))
print(pal_check_easy("A man, a plan, a canal: Panama"))

# --------------------------------------------------------------
# METHOD 1: Two-Pointer Approach
# Logic: Compare characters from both ends toward the center.
# Stops immediately when a mismatch is found.
# Time: O(n) | Space: O(n) (due to cleaning)
# Best for: Interviews, algorithmic thinking, lower memory usage.

# METHOD 2: String Reversal
# Logic: Reverse the cleaned string and compare with original.
# Simpler and more readable, but creates an extra reversed copy.
# Time: O(n) | Space: O(n)
# Best for: Clean, short, Pythonic code.

# CONCLUSION:
# Both have O(n) time and space complexity.
# Method 1: More memory-efficient, supports early exit.
# Method 2: More readable, often faster in Python due to slicing.
# ------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Concept : Defining Characters and Character Classification in Python
# -----------------------------------------------------------------------------------------
# 1. No Dedicated `char` Type in Python:
#    - Unlike C, C++, or Java, Python has no distinct `char` data type.
#    - A single character is simply a `str` of length 1 (e.g., isinstance(ch, str) and len(ch) == 1).
#
# 2. Built-in String Classification Methods:
#    - ch.isalpha() : True if all characters are letters (a-z, A-Z, plus unicode letters).
#    - ch.isdigit() : True if all characters are digits (0-9, superscripts).
#    - ch.isnumeric(): True for numbers including fractions, roman numerals (e.g., "½", "Ⅳ").
#    - ch.isalnum() : True if letter or digit (alphanumeric).
#    - ch.isspace() : True if whitespace (' ', '\t', '\n').
#    - Symbols/Punctuation: There is no `.issymbol()`. A character is a symbol/punctuation if:
#      `not ch.isalnum() and not ch.isspace()` or via the `string.punctuation` set.

# -----------------------------------------------------------------------------------------
# Concept : Type Checking with isinstance() vs. type()
# -----------------------------------------------------------------------------------------
# 1. Purpose:
#    - Checks whether an object is an instance of a specified class, or a subclass of it.
#    - Signature: isinstance(object, classinfo)
#        * `object`: The variable/value to evaluate.
#        * `classinfo`: A class, type, or a tuple of classes/types (acts like logical OR).
#    - Returns: True if match, False otherwise.
#
# 2. Key Advantage over type():
#    - `isinstance()` supports inheritance (polymorphism):
#        * isinstance(True, int) -> True (bool is a subclass of int in Python).
#        * type(True) == int    -> False (strict, ignores subclasses).
#    - In idiomatic Python, prefer `isinstance()` to respect object hierarchies.
#
# 3. Tuple of Types (Multi-type check):
#    - You can pass a tuple to check if an object matches ANY of the listed types:
#        * isinstance(x, (int, float)) -> checks if x is numeric.
#    - In Python 3.10+, union syntax is also valid: isinstance(x, int | float).
# -----------------------------------------------------------------------------------------


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# Anagram Problem :
# Problem statement: Two strings are anagrams 
# if they contain the same characters with the same frequencies, regardless of order.
# Ignore spaces and case.
# Input:
# s1: "Listen",
# s2: "Silent"
# --------------------------------------------------------------------------------------------

# MEthod 1 : 
def anagram_check(string1, string2):
    characters1 = {}
    characters2 = {}
    for i in string1.lower():
        if i not in characters1:
            characters1[i] = 1
        else:
            characters1[i] += 1
    for j in string2.lower():
        if j not in characters2:
            characters2[j] = 1
        else:
            characters2[j] += 1
    if characters1==characters2:
        return "Anagram"
    else :
        return "Not Anagram"

print(anagram_check("Listen", "Silent"))
# print(anagram_check("List,e n", "Sil, ent"))      // It will fail to do so...

# ---------------------------------------------------------------
# Method 2 : Solves the Problem of Symbol and spaces

def anagram_check(string1_sample, string2_sample):
    characters1 = {}
    characters2 = {}
        # case sensitivity and symbol check
    string1 = ""
    string2 = ""
    for i in (string1_sample).lower():
        if i.isalnum():
            string1 += i
    for i in (string2_sample).lower():
        if i.isalnum():
            string2 += i


    for i in string1:
        if i not in characters1:
            characters1[i] = 1
        else:
            characters1[i] += 1
    for j in string2:
        if j not in characters2:
            characters2[j] = 1
        else:
            characters2[j] += 1
    if characters1==characters2:
        return "Anagram"
    else :
        return "Not Anagram"

print(anagram_check("Listen", "Silent"))
print(anagram_check("List,e n", "Sil, ent"))    

# ---------------------------------------------------------------
# Method 3 : Solves the Problem of Symbol and spaces

def are_anagrams(string1_sample,string2_sample):
    is_anagram = True
    # string1 = string1_sample.replace(" ","")
    string1 = "".join([char.lower() for char in string1_sample if char.isalnum()])
    string2 = "".join([char.lower() for char in string2_sample if char.isalnum()])
    
    if len(string1) != len(string2):
        is_anagram = False
    
    frequency = {}

    for char in string1:
        frequency[char] = frequency.get(char,0) + 1         # New Concept+ THinking
    for char in string2:
        if char not in frequency:
            is_anagram = False
            return is_anagram               # stop the loop and function here
        frequency[char] -= 1
        if frequency[char] < 0:
            is_anagram = False
            return is_anagram
    return is_anagram

print("Anagram Check :" ,are_anagrams("List,@e n", "Sil, @ent"))  # Output: True
print("Anagram Check :", are_anagrams("Hello", "World!!"))        # Output: False (Exits early!)

# ---------------------------------------------------------------
# Method 4 : Using Sort

def are_anagrams(string1_sample,string2_sample):
    is_anagram = True

    # sorting the string and also removing extra spaces and characters
    string1 = sorted("".join([char.lower() for char in string1_sample if char.isalnum()]))
    string2 = sorted("".join([char.lower() for char in string2_sample if char.isalnum()]))

    # after sorting obviously both the string will be same if anagram
    if (string1 != string2):
        is_anagram=False
        return is_anagram
    return is_anagram


print("Anagram Check :" ,are_anagrams("List,@e n", "Sil, @ent"))  # Output: True
print("Anagram Check :", are_anagrams("Hello", "World!!"))        # Output: False (Exits early!)




# ================= ANAGRAM: METHOD COMPARISON =================

# METHOD 2: Two Frequency Dictionaries
# Logic: Count character frequencies separately and compare dictionaries.
# Time: O(n + m) | Space: O(n + m)
# Simple to understand, but uses two dictionaries.

# METHOD 3: Single Frequency Dictionary
# Logic: Add counts from string1, subtract counts using string2.
# Time: O(n + m) | Space: O(n + m)
# Supports early exit and uses only one frequency dictionary.
# Best for: Interviews and algorithmic thinking.

# METHOD 4: Sorting Approach
# Logic: Sort both cleaned strings and compare them.
# Time: O(n log n + m log m) | Space: O(n + m)
# Short and readable, but sorting is slower for large inputs.

# CONCLUSION:
# Method 3: Best overall algorithmic approach.
# Method 2: Easiest for understanding frequency counting.
# Method 4: Simplest logic, but less time-efficient.


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# First Unique Character Problem :
# Problem statement: Given a string, find the first character that appears exactly once.[cite: 2]
# Return -1 if every character repeats.[cite: 2]
# Assumption : lower and upper letter are taking as same value
# --------------------------------------------------------------------------------------------
def unique_char(string_sample):
    # Has to remove all the symbols and spaces first
    string = "".join([char.lower() for char in string_sample if char.isalnum()])

    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char,0) + 1

    # Will iterate through dictionary now the first key with value 1 ?
    for key,value in frequency.items():
        if value==1:
            return key
    return -1

print("Unique :" ,unique_char("Retam mondal"))
print("Unique :" ,unique_char("ttamondadkn"))
print("Unique :" ,unique_char("ttammondaokdkn"))
print("Unique :" ,unique_char("aabbcddee"))


print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# Longest Word Problem :
# Problem statement: Given a sentence, return its longest word.
# If multiple words have the same maximum length, return the last one.
# Input: "Python makes problem solving easier"
# --------------------------------------------------------------------------------------------
def long_word(string_sample):
    # string = string1_sample.split(" ")      # splitting based on empty space
    string = string_sample.split()

    max_len = float("-inf")     # best thing to use
    max_word = None

    for word in string[::-1]:
        # max_len = len(word) if len(word) > max_len else max_len
        if len(word) > max_len:
            max_len = len(word)
            max_word = word

    return (max_word,max_len)

print(long_word("Python makesscee  problem solving easierway"))


# -----------------------------------------------------------------------------------------
# Concept : str.split() vs. str.split(" ") in Python
# -----------------------------------------------------------------------------------------
# 1. str.split() (No argument / sep=None):
#    - Treats ANY consecutive whitespace (spaces, tabs \t, newlines \n) as a SINGLE delimiter.
#    - Automatically strips leading and trailing whitespace before splitting.
#    - NEVER produces empty strings ('') in the resulting list.
#
# 2. str.split(" ") (Explicit single space argument):
#    - Treats EXACTLY ONE single space character (' ') as the delimiter.
#    - Does NOT group consecutive spaces; each extra space results in an empty string ('').
#    - Preserves tabs (\t) and newlines (\n) inside tokens instead of splitting on them.
#    - Keeps empty strings if there are leading or trailing spaces.
# -----------------------------------------------------------------------------------------

print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# Merge Sorted Arrays Problem :
# Problem statement:
# Given two arrays sorted in ascending order,
# merge them into one sorted array without sorting the combined result afterward.
# --------------------------------------------------------------------------------------------
# I will do first merge then sort --> this is not going to work
# we have to do sorting along in Operation

def merge_sort(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else :
            result.append(arr2[j])
            j += 1
    # wheneve in upper any one will get exhaust lower things will work
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result

arr1 = [1,4,7,9]
arr2 = [2,3,8,10]
print(merge_sort(arr1, arr2))

# ================= Thinking =================
# METHOD: Two-Pointer Technique (Merge Sorted Arrays)
# Logic:
# 1. Use two pointers (i, j), one for each sorted array.
# 2. Compare elements and append the smaller one to result.
# 3. Move the pointer of the selected element forward.
# 4. Append remaining elements after one array is exhausted.

# Time Complexity: O(n + m) - each element visited once.
# Space Complexity: O(n + m) - new merged array.

# WHY EFFICIENT?
# No additional sorting required.
# Better than merge + sort: O((n+m) log(n+m)).
# Works with duplicates, negative numbers, and empty arrays.

# NOTE: This is the MERGE step of Merge Sort,
# not the complete Merge Sort algorithm.

# -----------------------------------------------------------------------------------------
# Concept : The while Loop in Python
# -----------------------------------------------------------------------------------------
# 1. Core Idea:
#    - A control-flow statement that repeats a block of code as long as a test condition is True.
#    - Evaluates the condition BEFORE every iteration (pre-test loop). If the condition is
#      initially False, the body never runs.
#
# 2. Syntax Anatomy:
#    initialization     -> i = 0
#    while <condition>: -> while i < 5:
#        statements     ->     print(i)
#        update step    ->     i += 1  # Omitting this creates an infinite loop!
#
# 3. Execution Flow:
#    [Condition Check] ── True ──> [Run Body] ──> [Update State] ──> [Loop Back]
#           │
#         False
#           │
#           ▼
#      [Exit Loop]
# -----------------------------------------------------------------------------------------