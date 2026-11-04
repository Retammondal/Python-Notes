import numpy as np
import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Custom Index DataFrames & .loc[] Introduction
# --------------------------------------------------------------------------------------------

df = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha", "Rohit", "Pooja"],
    "Age": [18, 19, 18, 20, 19, 18, 21, 19],
    "Branch": ["CSE", "ECE", "CSE", "IT", "ME", "CSE", "ECE", "IT"],
    "Marks": [78, 92, 65, 88, 45, 95, 56, 72],
    "Attendance": [85, 95, 70, 90, 60, 98, 75, 82]
}, index=["STUD-01","STUD-02","STUD-03","STUD-04","STUD-05","STUD-06","STUD-07","STUD-08"])
print(df)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Label-Based Row Selection (.loc[])
# --------------------------------------------------------------------------------------------
# Rows Selection --> loc, iloc
# Labeling of the Current Dataframe -- 0,1,2,3,...
# loc ==> accesses using the row labels and the column labels. (Selection & Modification)
# Syntax : df.loc[row_labels, column_labels]
#
# | Operation                  | Syntax Example                              | Result Type       |
# |----------------------------|---------------------------------------------|-------------------|
# | Single Value               | df.loc['Row_A', 'Column_1']                 | Scalar            |
# | Single Row                 | df.loc['Row_A']                             | pandas Series     |
# | Single Row as DataFrame    | df.loc[['Row_A']]                           | pandas DataFrame  |
# | Multiple Specific Rows     | df.loc[['Row_A', 'Row_C']]                  | pandas DataFrame  |
# | All Rows, Specific Columns | df.loc[:, ['Col_1', 'Col_2']]               | pandas DataFrame  |
# | Slice Rows & Columns       | df.loc['Row_A':'Row_C', 'Col_1':'Col_3']    | pandas DataFrame  |
#
# Notes:
# 1. .loc[] uses row and column labels.
# 2. Single square brackets return a Series for a single row.
# 3. Double square brackets return a DataFrame.
# 4. Slicing with .loc[] is inclusive of both start and end labels.

print(df.loc["STUD-02", "Name"]) # Give 102 id Student's Name? Accessing based on 
                                 # Row label + Column label

print(df.loc["STUD-04"])         # Give STUD-04 Full Details? 
                                 # *** NOTE : in this Pandas Series the label will be the Dataframe Headers

print(df.loc[["STUD-04"]])       # It will be in form of Dataframe

print(df.loc[["STUD-04", "STUD-07"]]) 
                                 # Give STUD-04, -07 details? It will be in form of 
                                 # Dataframe

print(df.loc["STUD-04" : "STUD-07"])
                                 # Give STUD-04 to STUD-07 details?

print(df.loc[:, ["Age", "Marks", "Branch"]])
                                 # Give All Rows, Age-Marks-Branch column in this Order?

print(df.loc["STUD-02":"STUD-06", ["Age", "Marks"]])
                                 # Give Students 2nd to 6th -- Age, Marks?


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Index-Based Row Selection (.iloc[])
# --------------------------------------------------------------------------------------------
# loc --> label (L)
# iloc --> index (I)        --> Row and column both will be traced by Indexes only...
# Pandas: Difference Between .iloc[] and .loc[]
#
# | Feature             | df.iloc[] (Integer Location)          | df.loc[] (Label Location)             |
# |---------------------|---------------------------------------|---------------------------------------|
# | Selection Criteria  | Numerical index position (0, 1, 2...) | Row / Column labels ('Age', 'ID_101') |
# | Slicing Endpoints   | Exclusive (0:3 gives 0, 1, 2)         | Inclusive ('A':'C' gives A, B, C)     |
# | Out-of-bound Errors | Raises IndexError                     | Raises KeyError for missing labels    | 

print(df.iloc[0])

print(df.iloc[-1])             # Last Student Information?

print(df.iloc[-1, 1])          # Last Student "Name"

print(df.iloc[[1, 3, 4]])      # 2nd,4th , 5th row using iloc

print(df.iloc[-4:])            # Show the details of last 4 students?

print(df.iloc[-4:, [4, 5]])    # Show the details of last 4 students and 4,5 index 
                               # columns?

