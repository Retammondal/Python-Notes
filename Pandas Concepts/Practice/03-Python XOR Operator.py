# -----------------------------------------------------------------------------------------
# Concept : The Augmented Bitwise XOR Operator (^=) in Python
# -----------------------------------------------------------------------------------------
# 1. Meaning & Syntax:
#    - `a ^= b` is the shorthand for `a = a ^ b`.
#    - `^` is the Bitwise XOR (Exclusive OR) operator.
#    - It performs XOR between the operands and reassigns the result in-place to `a`.
#
# 2. XOR Truth Table (Element by Element):
#    - Returns 1 if bits are DIFFERENT, and 0 if bits are the SAME:
#        0 ^ 0 -> 0
#        1 ^ 1 -> 0
#        0 ^ 1 -> 1
#        1 ^ 0 -> 1
#
# 3. Essential Mathematical Properties of XOR:
#    - Self-Inverse  : x ^ x = 0        (Any number XORed with itself cancels out)
#    - Identity      : x ^ 0 = x        (XOR with 0 leaves the number unchanged)
#    - Commutative   : a ^ b = b ^ a
#    - Associative   : (a ^ b) ^ c = a ^ (b ^ c)
#
# 4. In Sets:
#    - When used on Python `set` objects, `^=` performs in-place Symmetric Difference
#      (keeps elements in either set, but NOT in both).
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Use Case 1: Standard Bitwise XOR Assignment on Integers
# -----------------------------------------------------------------------------------------
a = 6   # Binary: 110
b = 3   # Binary: 011

a ^= b  # Binary: 110 ^ 011 = 101 (Decimal: 5)
print("Result of 6 ^= 3:", a)  # Output: 5


# -----------------------------------------------------------------------------------------
# Use Case 2: Classic DSA Problem - Single Number (Find Unique Element)
# -----------------------------------------------------------------------------------------
# Given an array where every element appears twice except one, find the unique one.
# Because x ^ x = 0 and x ^ 0 = x, duplicates cancel out!

nums = [4, 1, 2, 1, 2]
unique = 0

for num in nums:
    unique ^= num  # (0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2) -> (4 ^ (1^1) ^ (2^2)) -> 4 ^ 0 ^ 0 = 4

print("Unique element found:", unique)  # Output: 4


# -----------------------------------------------------------------------------------------
# Use Case 3: Swapping Two Variables Without a Temp Variable
# -----------------------------------------------------------------------------------------
x = 10
y = 20

x ^= y
y ^= x
x ^= y

print(f"Swapped values: x = {x}, y = {y}")  # Output: x = 20, y = 10

# Step 1: x ^= y
#   x now holds (X ^ Y)
#   y still holds Y
#
# Step 2: y ^= x
#   y = Y ^ (X ^ Y)
#     = (Y ^ Y) ^ X      <- Y cancels out! (Y ^ Y = 0)
#     = 0 ^ X = X
#   Now y holds the original X value!
#
# Step 3: x ^= y
#   x = (X ^ Y) ^ X      <- remember y is now X
#     = (X ^ X) ^ Y      <- X cancels out! (X ^ X = 0)
#     = 0 ^ Y = Y
#   Now x holds the original Y value!

# Practical Note:
# In Python, standard swapping is written as `x, y = y, x` (tuple unpacking).
# The XOR trick is an interview/low-level programming classic that saves registers/memory.


# =========================================================================================
# Use Case 4 - In-Place Symmetric Difference on Sets
# =========================================================================================
# In mathematics and set theory:
#   - Union (|)              : All items in A or B
#   - Intersection (&)       : Only items in BOTH A and B
#   - Symmetric Difference (^): Items in A OR B, but NOT in BOTH (cancels shared items)
#
# Just like XOR on numbers cancels out identical bits (1 ^ 1 = 0),
# XOR on sets cancels out identical items present in both sets!
#
# Difference between ^ and ^=:
#   - s1 ^ s2  : Creates a brand NEW set in memory.
#   - s1 ^= s2 : Mutates `s1` in-place (same as s1.symmetric_difference_update(s2)).

frontend_devs = {"Alice", "Bob", "Charlie"}
backend_devs  = {"Charlie", "David", "Alice"}

# Who works on ONLY ONE stack? (Exclude full-stack devs: Alice, Charlie)
frontend_devs ^= backend_devs

# "Alice" and "Charlie" are in both -> CANCELLED OUT
# "Bob" (only frontend) and "David" (only backend) -> KEPT
print("\nSpecialized devs (exclusive to one side):", frontend_devs)
# Output: {'Bob', 'David'}