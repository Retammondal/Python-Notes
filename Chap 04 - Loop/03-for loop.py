"""
=========================================================
PYTHON FOR LOOPS & ITERATION 
=========================================================
Core Concept: 'i' acts as a temporary variable (or "box") 
that holds the current item for each independent loop cycle.
"""

# ==========================================
# 1. LOOPING WITH RANGE
# ==========================================
print("--- Range Loop ---")
# loop 1 (i = 0): print i
# loop 2 (i = 1): print i ... and so on up to 4.
for i in range(5):
    print(i, end=" ")
print()                     # will just give an Enter to exiting end = " "
for i in range(5):
    print(i+1, end=" ")

print("\n")                 # Adds a new line for clean output


# ==========================================
# 2. ITERATING OVER STRINGS
# ==========================================
print("--- String Iteration ---")
# Python recognizes that a string is just a collection of characters.
# loop 1 (i = "R")
# loop 2 (i = "e") ...
for i in "Retam":
    print(i, end=" ")
print("\n")


# ==========================================
# 3. IGNORING THE VARIABLE ('i' as a pure timer)
# ==========================================
print("--- Looping just to repeat an action ---")
# Why do we get "Hi" 5 times?
# Because "Retam" has 5 characters. 'i' takes 'R', 'e', 't', 'a', 'm', 
# making the loop run 5 times, even if we don't actually print 'i'.
for i in "Retam":
    print("Hi", end=" ")
print("\n")


# ==========================================
# 4. MULTIPLE ACTIONS IN ONE LOOP
# ==========================================
print("--- Multiple Prints in Loop ---")

for i in "Reet a":
    print("Hi", end=" ")
    print(i, end=" ")
print("\n")


# ==========================================
# 5. CUSTOM VARIABLE NAMES
# ==========================================
print("--- Custom Variable Names ---")
# Instead of 'i', you can name the variable anything you want (like 'num', 'char', 'x').
for num in range(2, 11, 1):
    print(num, end=" ")
print("\n")


# ==========================================
# 6. RANGE WITH STEP & EXCLUSIVE STOP
# ==========================================
print("--- Range with Start, Stop, and Step ---")
# range(start, stop, step) -> Stop value (9) is EXCLUSIVE, so it stops at 8.
for i in range(1, 9, 2): 
    print(i, end=" ")
print("\n")

