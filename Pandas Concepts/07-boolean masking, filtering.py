import numpy as np
import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Setup DataFrames
# --------------------------------------------------------------------------------------------

expenses = pd.DataFrame({
    "Category": ["Rent", "Food", "Travel", "Internet", "Shopping"],
    "Amount": [12000, 6000, 2500, 900, 3500],
    "Essential": [True, True, False, True, False]
})

courses = pd.DataFrame({
    "Student": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Python": [85, 92, 60, 78, 45],
    "SQL": [80, 88, 72, 90, 50],
    "Pandas": [82, 95, 65, 86, 40]
})


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Column Projection (Selecting specific columns)
# --------------------------------------------------------------------------------------------
# Pass a Python list of column names inside outer brackets `[['col1', 'col2']]`
# to retain a 2D DataFrame structure with only the requested fields.

print(courses["Python"])       # Select single column --> returns a Pandas Series

print(courses[["Python"]])     # Select single column wrapped in a list --> 
                               # returns a Pandas DataFrame

print(expenses[["Category", "Amount"]])
                               # Select multiple columns --> returns DataFrame

print(courses.loc[:, ["Student", "Pandas"]])
                               # Display Students names and pandas marks 
                               # --> Both loc and normal indexing are valid


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Boolean Indexing (Single Condition)
# --------------------------------------------------------------------------------------------
# Boolean Indexing: Filtering rows based on a condition.
# Pandas evaluates expressions/Series like `courses["Python"] > 80` into a Series of True/False values
# * In Pandas, [] operator changes it's behaviour based on type of data passed:
#           i. Pass a String/label : Pandas look for Column name
#           ii. Pass a Boolean list/Series : Pandas take it as Boolean Indexing & Act as Row Filter

print(courses["Python"] > 80)  # It will give a Series of True, False values

print(courses[courses["Python"] > 80])  
                               # Will give the actual DataFrame rows where the 
                               # condition is True. Works just like passing 
                               # courses[[True, False, False, True, False]]

print(expenses[expenses["Amount"] > 3000])
                               # Expenses greater than 3000

print(expenses[expenses["Essential"] == True])
                               # Filtering on boolean columns: You can compare 
                               # directly with `== True`, or simply use 
                               # `expenses[expenses["Essential"]]`


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Combining Multiple Boolean Conditions
# --------------------------------------------------------------------------------------------
# 1. Use bitwise operators: `&` for AND, `|` for OR, `~` for NOT.
# 2. Always wrap each individual condition in parentheses `(...)` due to
#    Python's operator precedence rules.

pyth_marks_boolean = courses["Python"] > 80 
sql_marks_boolean = courses["SQL"] > 80
                               # Break down conditions into variables for clarity

both_marks_boolean = pyth_marks_boolean & sql_marks_boolean
                               # Will combine both boolean Series using AND '&'

print(courses[both_marks_boolean])
                               # Quest : Students with both Python & SQL marks > 80

print(                         
    expenses[                  # Non-essential expenses costing at least 2000 
        (expenses["Essential"] == False) &
        (expenses["Amount"] >= 2000)
    ]
)                              # Writing complex filters across multiple lines 
                               # improves readability


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Advanced Filtering 
# --------------------------------------------------------------------------------------------
# .isin() : Checks if a value exists within a provided list. Great for filtering 
#           multiple OR conditions cleanly.
# .str    : Gives access to string methods (like startswith, contains, lower) for 
#           text-based column filtering.

print(courses[courses["Student"].isin(["Amit", "Sneha", "Karan"])])
                               # Filter rows where the student name is exactly 
                               # Amit, Sneha, OR Karan.

print(courses[courses["Student"].str.startswith("P")])
                               # Filter rows where the Student's name starts 
                               # with the letter "P" (e.g., Priya)