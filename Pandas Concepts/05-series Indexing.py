import pandas as pd

import numpy as np
df = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Priya", "Rahul", "Sneha",
    "Karan", "Neha", "Rohit", "Pooja"],
    "Age": [18, 19, 18, 20, 19, 18, 21, 19],
    "Branch": ["CSE", "ECE", "CSE", "IT",
    "ME", "CSE", "ECE", "IT"],
    "Marks": [78, 92, 65, 88, 45, 95, 56, 72],
    "Attendance": [85, 95, 70, 90, 60, 98, 75, 82]
})

print("----------------------1-----------------------")
# ==============================================================================
# PANDAS SERIES INDEXING: STANDARD VS POSITION-BASED (.iloc)
# ==============================================================================
# Give me Name of the first and last student (Without head and tail)

names = df["Name"]             # Extract the "Name" column as a Pandas Series


# ------------------------------------------------------------------------------
# 1. Method 1: Standard Bracket Indexing (Label-Based)
# ------------------------------------------------------------------------------
# Behavior: Looks for explicit labels in the index, NOT absolute positions.

print(names[0])                # 1. First Element. Works if the literal index 
                               # label '0' exists.

# print(names[-1])             # 2. Last Element (The Wrong Way). ERROR: Raises 
                               # KeyError. Pandas looks for a literal label 
                               # named `-1`, not the "last item".

print(names[len(names) - 1])   # 3. Last Element (The Safe Way using Label Math). 
                               # Works only if the index is a standard, unbroken 
                               # 0-indexed range (0, 1, 2...).


print("----------------------2-----------------------")
# ------------------------------------------------------------------------------
# 2. Method 2: .iloc Indexing (Position-Based) - RECOMMENDED
# ------------------------------------------------------------------------------
# Behavior: Acts exactly like a standard Python list. It completely ignores
# the index labels and looks strictly at the 0-indexed absolute position.

print(names.iloc[0])           # 1. First Element by absolute position

print(names.iloc[-1])          # 2. Last Element using negative indexing. Works 
                               # perfectly because .iloc natively understands 
                               # negative positioning.


# ==============================================================================
# SUMMARY TABLE
# ==============================================================================
# Method        | Syntax        | Negative Indexing? | Look-up Type
# --------------|---------------|--------------------|-------------------------
# Standard      | names[0]      | No (KeyError)      | Label-based
# Positional    | names.iloc[0] | Yes (.iloc[-1])    | Position-based (List-like)