import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Setup DataFrame
# --------------------------------------------------------------------------------------------

courses = pd.DataFrame({
    "Student": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Python": [85, 92, 60, 78, 45],
    "SQL": [80, 88, 72, 90, 50],
    "Pandas": [82, 95, 65, 86, 40]
})
print(courses)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Column Selection (Series vs DataFrame)
# --------------------------------------------------------------------------------------------

# Quest : Select Python Marks
print(courses["Python"])       # --> will give series
print(courses[["Python"]])     # --> will give Dataframe


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Boolean Indexing (Single Condition)
# --------------------------------------------------------------------------------------------

# Quest : Students with Python marks above 80
print(courses["Python"] > 80)  # It will give True, False

print(courses[courses["Python"] > 80])  
                               # Will give the value where it's true. Acts just 
                               # like courses[[True,False,False, True,..]]


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Multiple Boolean Conditions
# --------------------------------------------------------------------------------------------

# Quest : Students with both Python and SQL marks > 80
pyth_marks = courses["Python"]                      # Give list of Python Marks

pyth_marks_boolean = courses["Python"] > 80     
                                                    # give in True,False -- Series not Dataframe

sql_marks_boolean = courses["SQL"] > 80         
                                                    # give in True,False -- Series not Dataframe

print(pyth_marks)
print(pyth_marks_boolean)

both_marks_boolean = pyth_marks_boolean & sql_marks_boolean
print(both_marks_boolean)      # will combine both boolean

print(courses[both_marks_boolean])


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Column Projection (Standard vs .loc)
# --------------------------------------------------------------------------------------------

# Quest : Display Students names and pandas marks --> Both loc and normal indexing valid
print(courses[["Student", "Pandas"]])
print(courses.loc[:, ["Student", "Pandas"]])