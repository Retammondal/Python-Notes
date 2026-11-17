import pandas as pd

# ==================================================
# PYTHON LIST SORTING vs PANDAS SORTING
# ==================================================
# 1. NATIVE PYTHON LIST SORTING
# How Sorting helps in Data Analytics? To get Top 5 High Value Customers etc.

marks = [75, 90, 65, 88, 95, 80]

marks.sort()                   # How to sort it? Native sort() sorts the list in 
print(marks)                   # place (ascending by default).

marks.sort(reverse=True)       # Want to sort in Descending Order?
print(marks)


# --------------------------------------------------
# 2. FILTERING FOR MIN/MAX (THE HARD WAY)

df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 76, 95, 88],
    "Attendance": [90, 95, 80, 98, 85]
})
print(df)

max_marks = max(df["Marks"])   # Which Student has the Highest Marks?
                               # --> Will give the Highest Marks scalar value.

max_marks_stud_data = df[df["Marks"] == max_marks]
                               # --> Will give that row matching the Highest Marks.

max_marks_stud_name = max_marks_stud_data["Student"]
                               # --> Will extract just the "Student" column.

print(max_marks_stud_data)          
print(max_marks_stud_name)          

print(df[df["Attendance"] == min(df["Attendance"])]["Student"])
                               # Who has the lowest Attendance? (One-liner)

print(df[df["Age"] == min(df["Age"])]["Student"])
                               # Who is the Youngest Student? (One-liner)


# ==================================================
# PANDAS: SORTING DATAFRAMES (THE SMART WAY)
# ==================================================
# But Doing all these are unnecessarily complicated... 
# Sorting the Data is much better and cleaner.

# 1. SORTING A SINGLE COLUMN
# df.sort_values(by='column_name')                  --> Ascending (default)
# df.sort_values(by='column_name', ascending=False) --> Descending
# Note: It returns a NEW DataFrame, it doesn't change the original by default.

df_sort = df.sort_values(by='Age')
print(df_sort)                 # * Note : In Sorting, the Entire Row will be 
                               # shifted, but its index label (0, 1, 2...) 
                               # will travel with it.


# --------------------------------------------------
# 2. SORTING MULTIPLE COLUMNS
# Pass a list of Columns to 'by', and pass a matching list of booleans 
# to 'ascending' to control the direction for each column independently.

df_sorted = df.sort_values(by=['Age', 'Student'], ascending=[True, True])
print(df_sorted)               # Sort by Age, then by Name Alphabetically.


# --------------------------------------------------
# 3. MANAGING MISSING VALUES (NaN)

# df_sorted = df.sort_values(by='Score', na_position='first')
                               # By default, missing data (NaN) is placed at 
                               # the end of the sorted result. You can push 
                               # them to the top using na_position='first'.


# --------------------------------------------------
# 4. CLEANING UP THE INDEX AFTER SORTING
# To fix the scrambled indices (e.g., 3, 1, 4, 0, 2) back to a clean 0, 1, 2...

df_sorted = df.sort_values(by='Age', ignore_index=True)
                               # Reset the index during the sort operation 
                               # using ignore_index=True.


# ==================================================
# STABLE VS UNSTABLE SORTING (kind parameter)
# ==================================================
# In pandas, stable sorting keeps rows with equal sort values in their original relative order,
# while unstable sorting may scramble the relative order of those ties

# Feature              | Unstable Sorting          | Stable Sorting
# ---------------------|---------------------------|---------------------------
# Algorithms           | Quicksort, Heapsort       | Mergesort, Timsort
# Tied Values          | May change original order | Preserves original order
# Pandas Default       | quicksort (single column) | Stable sort when explicitly selected 
#                                                    + For Multiple Column
# Memory Usage         | Generally lower           | Generally higher (Mergesort)

# Syntax :
# kind="quicksort" (default) --> Unstable; 
#     ="stable"              --> Stable

# Note: Multi-column Exception: for multi column pandas ignores kind parameter and use Stable

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["Sales", "HR", "Sales", "HR"]
})

# Stable sort: Alice stays before Charlie; Bob stays before David
stable_df = df.sort_values(by="Department", kind="stable")

# Unstable sort: Charlie might appear before Alice on large datasets
unstable_df = df.sort_values(by="Department", kind="quicksort")

print(stable_df)
print(unstable_df)

# ==================================================
# Sorting by Index Labels (df.sort_index())
# ==================================================
# 1. Purpose:
#    - Sorts a DataFrame or Series by its ROW index labels (axis=0) or COLUMN names (axis=1),
#      rather than by the data values inside columns (which is done by df.sort_values()).
#
# 2. Syntax:
#    df.sort_index(
#        axis=0,              # 0 = sort rows by index | 1 = sort columns alphabetically
#        ascending=True,      # True = A-Z / 0-9 | False = Z-A / 9-0
#        kind='quicksort',    # Sorting algorithm: 'quicksort', 'mergesort', 'stable'
#        na_position='last',  # Where to put NaN index labels: 'first' or 'last'
#        ignore_index=False   # True = resets resulting index to clean 0, 1, 2...
#    )
# -----------------------------------------------------------------------------------------

import pandas as pd

# Sample DataFrame with scrambled row index and unsorted column names
df = pd.DataFrame(
    {
        "Math":    [88, 92, 79, 95],
        "English": [85, 90, 82, 91],
        "Biology": [91, 87, 84, 89]
    },
    index=[103, 101, 104, 102]
)

print("Original DataFrame (Unsorted Index & Columns):")
print(df)

# -----------------------------------------------------------------------------------------
# 1. Sort Rows by Index (Default: axis=0, ascending=True)
# Orders rows cleanly as 101 -> 102 -> 103 -> 104
row_sorted = df.sort_index()
print("\nSorted by Row Index (Ascending):")
print(row_sorted)

# -----------------------------------------------------------------------------------------
# 2. Sort Columns Alphabetically (axis=1)
# Orders columns as Biology -> English -> Math
col_sorted = df.sort_index(axis=1)
print("\nSorted by Column Names (axis=1):")
print(col_sorted)

