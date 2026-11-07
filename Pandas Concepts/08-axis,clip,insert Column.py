import pandas as pd
import numpy as np

# ==================================================
# PANDAS DATAFRAME: INSERTING COLUMNS
# ==================================================
# 1. APPENDING TO THE END
# Standard Way: Appending to the end of the DataFrame.
# Note: When using a List, you must give the exact number of rows, otherwise 
# it will give an error. When using a scalar, it fills the entire column.

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

df["C"] = [7, 8, 9]            # Method 1: Using a List

df["D"] = 0                    # Method 2: Using a scalar value (fills entire column)
print(df)


# --------------------------------------------------
# 2. INSERT AT SPECIFIC POSITION
# df.insert(location_index, column_name, values)

df.insert(2, "E", [10, 11, 12])
print(df)                      # Insert column "E" at Index 2


# --------------------------------------------------
# 3. DERIVING FROM EXISTING COLUMNS
# We can perform element-wise mathematical or string operations directly on 
# existing columns to create a new one (works because columns are Series).

df["A+B"] = df["A"] + df["B"]  # Will add A and B values together row by row
print(df)

# ==================================================
# PANDAS DATAFRAME: RENAMING COLUMNS & Rows INDEX
# ==================================================
# Pass a dictionary to the columns parameter mapping {'old_name': 'new_name'}. 
# By default, this returns a new DataFrame
df = df.rename(columns={"A+B" : "Total"})

# Rename specific rows
df = df.rename(index={0: "1st"})
print(df)


# ==================================================
# PANDAS DATAFRAME: DELETING COLUMNS
# ==================================================
# By default, this returns a new DataFrame
# Delete a Single Column
# df.drop(columns='col_name')

# Delete Multiple Column
df = df.drop(columns = ["Total", "D"])

# Delete Rows based on Index Value
# df.drop(["Row1","Row2",...])
df = df.drop("1st")
print(df)

# ==================================================
# PANDAS & NUMPY AGGREGATIONS
# ==================================================
# 1. THE `AXIS` PARAMETER
# axis = 0 (Default): Computes downwards along the rows (Column-wise summary)
#                     Collapses rows -> Gives 1 value per column (e.g., Subj Avg)
# axis = 1:           Computes across columns (Row-wise summary)
#                     Collapses columns -> Gives 1 value per row (e.g., Stu Avg)

data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Aarav", "Bhavna", "Chetan", "Divya", "Eshan"],
    "Python": [85, 78, 92, 64, 88],
    "SQL": [90, 82, 88, 70, 79],
    "Statistics": [80, 85, 95, 60, 92],
}

students = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(students)

subjects = ["Python", "SQL", "Statistics"]


# --------------------------------------------------
# 2. COLUMN-WISE MEAN (Class Average per Subject)

column_wise_avg = students[subjects].mean().round(2)
print("\n--- Class Average per Subject (axis=0) ---")
print(column_wise_avg)         # Method A: Pandas built-in .mean() (axis=0). 
                               # Preferred because it handles all cols at once.

avg_python = np.mean(students["Python"]).round(2)
avg_sql = np.mean(students["SQL"]).round(2)
avg_stats = np.mean(students["Statistics"]).round(2)
                               # Method B: NumPy np.mean() on individual Series


# --------------------------------------------------
# 3. ROW-WISE MEAN (Total Average for Each Student)

row_wise_avg = students[subjects].mean(axis=1).round(2)
print("\n--- Student Averages (axis=1) ---")
print(row_wise_avg)            # Must specify axis=1 to aggregate across subjects


# ==================================================
# TRIMMING & CAPPING WITH CLIP()
# ==================================================
# 1. CLIPPING WITH SCALAR VALUES
# The clip() method is used to trim or cap values outside of a specified upper 
# and lower boundary.
# Syntax: DataFrame.clip(lower=None, upper=None, axis=None)

df = pd.DataFrame({'A': [10, -5, 30, 15], 
                   'B': [2, 45, -12, 18]})

clipped_df = df.clip(lower=0, upper=20)
print(clipped_df)              # Cap values so they stay between 0 and 20


# --------------------------------------------------
# 2. CLIPPING WITH AN ARRAY-LIKE (DICTIONARY)

clipped_custom = df.clip(upper={'A': 12, 'B': 15})
print(clipped_custom)          # Separate upper thresholds: col A (12), col B (15)


# --------------------------------------------------
# 3. ROW-WISE CLIPPING (USING LISTS)

df = pd.DataFrame({'A': [10, -5, 30, 15], 
                   'B': [2, 45, -12, 18]})

row_lowers = [0, -2, 5, 10]    # Lower limits for Row 0, 1, 2, 3 respectively

clipped_df = df.clip(lower=row_lowers, axis=0)
print(clipped_df)              # Apply row-wise clipping by setting axis=0


# --------------------------------------------------
# 4. ROW-WISE CLIPPING (USING DATAFRAMES & SERIES)

df = pd.DataFrame({'A': [10, -5, 30], 'B': [2, 45, -12]}, 
                  index=['row_x', 'row_y', 'row_z'])
                               # DataFrame with custom row indices

row_uppers = pd.Series([8, 20, 15], index=['row_x', 'row_y', 'row_z'])
row_uppers = pd.Series({'row_x':8, 'row_y':20, 'row_z': 15})
                               # Upper limits explicitly mapped to the row names

clipped_df = df.clip(upper=row_uppers, axis=0)
print(clipped_df)              # Apply along axis=0

