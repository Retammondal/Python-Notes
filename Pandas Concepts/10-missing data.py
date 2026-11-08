import pandas as pd
import numpy as np

# ==================================================
# PANDAS: HANDLING MISSING DATA (NaN)
# ==================================================
# 1. THEORY & SETUP
# Problems with Missing Data:
# - Stats (avg/min/max) can be miscalculated (counted as an item but holds no value).
# - Machine Learning Algorithms will fail if data is missing.
# 
# How to Deal with Missing Data?
# 1. Drop the missing values --> dropna() (Bad if huge amounts of data are missing)
# 2. Filling the missing values --> fillna()
#
# Why NaN (Not a Number) comes in picture?
# 1. 0 divided by 0, Infinity minus Infinity, Square root of negative number.
# 2. Missing data in a spreadsheet or database (e.g., an empty cell imported).

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 92, np.nan, 78, None],
    "Attendance": [90, 95, 75, np.nan, 80],
    "Branch": ["CSE", "IT", "CSE", None, "ME"]
})

print(df)                      # Wherever there is 'None' in the dataframe, it 
                               # will automatically be converted to 'NaN'.

print(df.dtypes)               # Notice: If we give None/np.nan, it will NOT 
                               # change the numeric dtype of that column.
                               # But if we wrote "Unknown", it would change 
                               # the whole series type to Object (String).

print("----------------1----------------")
# --------------------------------------------------
# 2. IDENTIFYING MISSING DATA (.isna / .isnull)

print(df.isna())               # Prints True where the data is Missing (NaN).
                               # Note: df.isnull() is exactly the same function.
print(df.isnull())

print("----------------2----------------")
# Count the Number of 'NaN' in Each Column -->
print(df.isna().sum())         # Gives a Series showing the total count of missing values for Each Column

print("----------------3----------------")
# Count the Number of 'NaN' in Each Row -->
print(df.isna().sum(axis=1))

print("----------------4----------------")
# Count Total Number of 'NaN' in Total DataFrame -->
print(df.isna().sum().sum())   # How to get the TOTAL missing values across 
                               # the entire DataFrame (rather than column-wise).


print("----------------5----------------")
# --------------------------------------------------
# 3. IDENTIFYING PRESENT DATA (.notna)
# Opposite off 'isna' --> Count thee Actual Datas

print(df.notna())              # Prints True where the data is Present (Valid).

print(df.notna().sum())        # Total valid data points per column.

print(df.notna().sum().sum())  # Total valid data points across the whole DF.


print("----------------6----------------")
# --------------------------------------------------
# 4. ROW & COLUMN COMPLETENESS CHECKS (.any / .all)
# Reminder: axis=0 (default) checks Columns. axis=1 checks Rows.

print(df.notna().all())        # If a column has ALL data present -> True.

print(df.notna().any())        # If a column has ANY data present -> True.

print("----------------7----------------")
print(df.notna().all(axis=1))  # How to check if a Row has ALL Present data?
                               # If every cell in a row is present -> True.

print(df.notna().any(axis=1))  # If a row has ANY data present -> True.


print("----------------8----------------")
print(df.isna().any())         # If a column has ANY missing data -> True.

print(df.isna().all())         # If a column has ALL missing data -> True.

print("----------------9----------------")
# Question : What % of values are missing in the entire dataframe?
total_df_entries = df.size
total_missing_entries = df.isna().sum().sum()
missingPerc = total_missing_entries*100/total_df_entries
print(missingPerc)

# Question : What % of rows have some missing data?
rows_missing_data = df.isna().any(axis=1).sum()
total_rows = len(df)
missingRowsPerc = rows_missing_data*100/total_rows
print(missingRowsPerc)