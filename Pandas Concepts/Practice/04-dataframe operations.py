import pandas as pd
import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Setup DataFrame
# --------------------------------------------------------------------------------------------

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Amit", "Priya", "Rahul", "Sneha", "Karan",
        "Neha", "Rohit", "Pooja", "Anjali", "Vikas"
    ],
    "Branch": [
        "CSE", "ECE", "CSE", "IT", "ME",
        "CSE", "ECE", "IT", "EEE", "CSE"
    ],
    "Marks": [82, 91, 68, 88, 76, 95, 79, 72, 85, 74],
    "Attendance": [85, 92, 78, 90, 88, 96, 83, 95, 86, 75],
    "Backlogs": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Placement_Training": [
        "Yes", "Yes", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "Yes", "No"
    ]
})


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Basic Viewing & Slicing
# --------------------------------------------------------------------------------------------

# Q1 : Display the first five and last three records?
print(students.head(5))
print(students.tail(3))

print(students.iloc[:5])       # Using iloc for the first 5 records
print(students.iloc[-3:])      # Using iloc for the last 3 records


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. DataFrame Properties & Metadata
# --------------------------------------------------------------------------------------------

# Q2 : Inspect the datasets's shape, column names, datatype and summary information?
print(students.shape)
print(students.info())

print(students.columns)        # Gives in Pandas Series
print(list(students.columns))  


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Column Selection & Boolean Filtering
# --------------------------------------------------------------------------------------------

# Q3 : Select only the students name, branch, attendance and marks columns.
print(students.loc[:, ["Name", "Branch", "Attendance", "Marks"]])

# Q4 : Identify students with marks of at least 75 and attendance of at least 80%
condition = (students.loc[:, "Marks"] > 75) & (students.loc[:, "Attendance"] > 80)
filtered_students = students[condition]
print(filtered_students)


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Advanced Filtering (isin) & Specific Column Projection
# --------------------------------------------------------------------------------------------

# Q5 : Restrict the results to students from CSE, IT or, ECE.
# Exclude student with pending backlogs, and only provide name, marks, attendence.

# Will i give multiple Or, Statement -- NO xx We have isin()
condition = (students["Branch"].isin(["CSE", "IT", "ECE"])) & (students["Backlogs"] == 0)
filtered_students = students[condition]

print(filtered_students[["Name", "Marks", "Attendance"]])


print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# 6. Slicing Filtered Data (iloc)
# --------------------------------------------------------------------------------------------

# Q6 : Display the first 3 eligible studetns using position based indexing in previous ques
# and only give name, marks (Index 1 is Name, Index 3 is Marks).
print(filtered_students.iloc[:3, [1, 3]])


print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# 7. Statistics & Aggregation
# --------------------------------------------------------------------------------------------

# Q7 : Calculate the avg marks of eligible students

avg_marks = np.mean(filtered_students["Marks"])
                               # Filtered students --> marks series & now we know 
                               # we can apply numpy on a Pandas Series..

avg_marks = (filtered_students["Marks"]).mean()
                               # Also we can be used Python built in Pandas method
print(avg_marks)

# Q8 : Find the students who are above this avg marks?
print(filtered_students[filtered_students["Marks"] > avg_marks])


print("----------------------8-----------------------")
# --------------------------------------------------------------------------------------------
# 8. Exporting Data
# --------------------------------------------------------------------------------------------

# Q9 : Save this Filtered Student Data in the csv File?
# filtered_students.to_csv("filtered_students.csv", index=False)