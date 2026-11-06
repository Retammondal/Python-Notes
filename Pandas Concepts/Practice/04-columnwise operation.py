import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha"],
    "Python": [80, 95, 45, 70, 30, 88],
    "SQL": [75, 90, 50, 65, 40, 92],
    "Statistics": [85, 92, 40, 80, 35, 90],
    "Attendance": [90, 95, 65, 80, 55, 98],
    "Branch": ["CSE", "IT", "CSE", "ECE", "ME", "IT"]
})

print(students)

# Q1 : Create a column academic year and assign value 2026 to each student
students["Academic Year"] = 2026
print(students)

# Q2 : Assign a Mentor to Each Student
students["Mentor"] = ["Aarav", "Zara", "Leo", "Maya", "Felix", "Elena"]
print(students)

# Q3 : Create a column total marks = python + Sql + statistics
students["Total"] = students["Python"] + students["SQL"] + students["Statistics"]
print(students)

# Q4 : New Column = % marks
students["Percentage"] = (students["Total"]*100 / 300).round(2)
print(students)

# Q5 : Average of each subject accross all Students --> Class Avg for each Subject
avg_Python = np.mean(students["Python"]).round(2)                      # Column Wise Average
avg_SQL = np.mean(students["SQL"]).round(2)                            # Method 1 : Numpy
avg_Statistics = np.mean(students["Statistics"]).round(2)
column_wise_avg = pd.Series([avg_Python, avg_SQL, avg_Statistics])
print(column_wise_avg)

                                                                       # Method 2 : Pandas
column_wise_avg = students[["Python", "SQL", "Statistics"]].mean()
print(column_wise_avg)

# Q6 : Average Marks of 3 Subjects for every Students; # Row Wise Average

                                                                        # Basic Method --> add all the subject marks and divide by 3
                                                                        # Mentos Method
row_wise_avg = students[["Python", "SQL", "Statistics"]].mean(axis=1)
print(row_wise_avg)

# Q7 : Which Students scored better in Python than in SQL, and by how much?
pyt_sql_diff = (students["Python"] - students["SQL"])
condition = pyt_sql_diff > 0                        # True,False,... Series
print(students[condition])

# Q7 : Assign 10 grace marks to each student for Python
students["Python"] = np.minimum(students["Python"] +5,100)             # Numpy Way
students["Python"] = (students["Python"] +5).clip(upper = 100)         # Pandas Way

print(students)