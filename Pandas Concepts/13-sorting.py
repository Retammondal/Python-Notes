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