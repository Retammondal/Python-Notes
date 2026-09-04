"""
=========================================================
PYTHON CONDITIONAL STATEMENTS PROCESSES WELL
=========================================================
Goal: Evaluate student marks based on the following criteria:
- Scores < 30 are Low
- Scores 30 to 69 are Average
- Scores 70 to 100 are High
- Any other score is Invalid
"""

marks = int(input("Enter your Marks : "))
print("-" * 40)

# ==========================================
# METHOD 01: Using ONLY 'if' statements
# ==========================================
# Drawback: You can't effectively use 'else' as a catch-all 
# without it attaching only to the very last 'if'. 
# Also, Python has to check every single condition, even if it already found a match.

print("--- Method 1 ---")
if marks >= 0 and marks < 30:
    print("Low Marks😭")
if marks >= 30 and marks < 70:
    print("Average Marks😛👏")
if marks >= 70 and marks <= 100:
    print("High Marks😇")
if marks > 100 or marks < 0:
    print("Invalid Marks ❌❌")

print("-" * 40)
# ==========================================
# METHOD 02: Nested 'if-else' statements
# ==========================================
# Drawback: Creates deep indentation (sometimes called the "pyramid of doom"), 
# making the code harder to read as you add more conditions.

print("--- Method 2 ---")
if marks >= 0 and marks < 30:
    print("Low Marks😭")
else:
    if marks >= 30 and marks < 70:
        print("Average Marks😛👏")
    else:
        if marks >= 70 and marks <= 100:
            print("High Marks😇")
        else:
            print("Invalid Marks ❌❌")

print("-" * 40)
# ==========================================
# METHOD 03: Using 'if-elif-else'
# ==========================================
# Benefit: Cleaner and more readable than nested ifs. 
# It stops checking conditions as soon as one evaluates to True.

print("--- Method 3 ---")
if marks >= 0 and marks < 30:
    print("Low Marks😭")
elif marks >= 30 and marks < 70:
    print("Average Marks😛👏")
elif marks >= 70 and marks <= 100:
    print("High Marks😇")
else:
    print("Invalid Marks ❌❌")

print("-" * 40)
# ==========================================
# METHOD 04: Optimized 'if-elif-else'
# ==========================================
# Benefit: The cleanest and most professional approach. 
# No need to check the lower bound (e.g., marks >= 30) 
# because previous statements already filtered those values out!

print("--- Method 4 ---")
if marks < 0:
    print("Invalid Marks ❌❌")
elif marks < 30:      # Anything < 0 is already caught above
    print("Low Marks😭")
elif marks < 70:      # Anything < 30 is already caught above
    print("Average Marks😛👏")
elif marks <= 100:    # Anything < 70 is already caught above
    print("High Marks😇")
else:                 # Only numbers > 100 are left
    print("Invalid Marks ❌❌")