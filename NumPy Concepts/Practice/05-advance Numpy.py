
print("\nNumpy Case Study\n")

# --------------------------------------------------------------------------------------------
# Column -- Description

# Student ID       -- Unique student identifier
# Attendance       -- Attendance percentage
# Study Hours      -- Average daily study hours
# Internet Hours   -- Average daily internet usage

# Python           -- Python marks out of 100
# SQL              -- SQL marks out of 100
# Statistics       -- Statistics marks out of 100
# NumPy            -- NumPy marks out of 100
# Communication    -- Communication marks out of 100

# Mock Interview   -- Mock interview score out of 100
# Placement        -- Whether the student was placed (1 = yes, 0 = no)
# --------------------------------------------------------------------------------------------

import numpy as np

np.set_printoptions(suppress=True, precision=2)

student_ids = np.arange(1001, 1031)

attendance = np.array([
    95, 82, 68, 91, 55, 77, 88, 62, 96, 73,
    84, 49, 90, 79, 66, 93, 71, 86, 58, 98,
    75, 81, 64, 89, 52, 94, 70, 83, 60, 92
], dtype=float)

study_hours = np.array([
    4.5, 3.0, 1.5, 4.0, 1.0, 2.5, 3.5, 2.0, 5.0, 2.5,
    3.0, 1.0, 4.5, 3.0, 2.0, 4.0, 2.5, 3.5, 1.5, 5.5,
    2.0, 3.0, 2.5, 4.0, 1.0, 4.5, 2.0, 3.5, 1.5, 4.0
], dtype=float)

internet_hours = np.array([
    3, 4, 7, 3, 8, 5, 4, 6, 3, 5,
    4, 9, 3, 4, 6, 2, 5, 4, 8, 3,
    6, 4, 7, 3, 9, 2, 6, 4, 7, 3
], dtype=float)

marks = np.array([
    [88, 85, 82, 90, 84],
    [75, 80, 70, 78, 76],
    [55, 60, 50, 58, 62],
    [92, 88, 90, 94, 86],
    [45, 52, 48, 50, 55],
    [70, 72, 68, 74, 80],
    [85, 82, 88, 86, 78],
    [60, 65, 55, 62, 68],
    [96, 92, 94, 98, 90],
    [68, 70, 65, 72, 74],
    [80, 78, 82, 84, 76],
    [40, 45, 42, 38, 50],
    [90, 86, 88, 92, 84],
    [72, 75, 70, 76, 80],
    [58, 62, 60, 55, 65],
    [94, 90, 92, 96, 88],
    [65, 68, 62, 70, 72],
    [82, 85, 80, 88, 86],
    [50, 55, 48, 52, 60],
    [98, 95, 96, 99, 94],
    [70, 68, 72, 75, 78],
    [78, 82, 76, 80, 84],
    [62, 60, 65, 58, 70],
    [88, 90, 85, 92, 86],
    [42, 48, 45, 40, 52],
    [95, 92, 94, 97, 90],
    [66, 70, 64, 68, 74],
    [84, 80, 82, 86, 88],
    [55, 58, 52, 60, 62],
    [91, 88, 90, 93, 86]
], dtype=float)

mock_interview = np.array([
    82, 70, 48, 90, 42, 65, 76, 55, 94, 60,
    72, 35, 85, 68, 50, 92, 58, 80, 40, 96,
    62, 74, 52, 88, 38, 93, 57, 79, 45, 86
], dtype=float)

placement = np.array([
    1, 1, 0, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1
], dtype=int)

subject_names = np.array([
    "Python", "SQL", "Statistics", "NumPy", "Communication"
])

# Introduce missing values for practice
attendance[[4, 11]] = np.nan
marks[2, 2] = np.nan
marks[14, 1] = np.nan
mock_interview[18] = np.nan

# Combine all numeric attributes
numeric_data = np.column_stack((
    student_ids,
    attendance,
    study_hours,
    internet_hours,
    marks,
    mock_interview,
    placement
))

# print("Dataset shape:", numeric_data.shape)
# print("Number of students:", len(student_ids))
# print("Marks shape:", marks.shape)
# print("Subject names:", subject_names)
print(numeric_data)

# Solve the problem using Big datasets..it will be helpful more..to revise concepts
print("----------------------Q1-----------------------")
# --------------------------------------------------------------------------------------------
# Write a program to determine the number of students,
# the number of attributes, the data types,

print("Number of Students ->",len(numeric_data[:,0])) 
print("Dimensions ->",numeric_data.ndim) 
print("Rows and Columns ->",numeric_data.shape) 
print("Total Elements ->",numeric_data.size) 
print("Data Type ->",numeric_data.dtype) 

print("----------------------Q2-----------------------")
# --------------------------------------------------------------------------------------------
# Display the records of students 1001–1005, their first three subject marks,
# and the marks of student 1004 in every subject.
print(numeric_data[:5,4:7])
print(numeric_data[3,4:9])

print("----------------------Q3-----------------------")
# --------------------------------------------------------------------------------------------
# Question (VVI)
# Calculate the total marks and percentage for each student,
# assuming all five subjects carry equal weight and each is out of 100.
# Missing marks must not be treated as zero.

total_marks = np.nansum(marks, axis=1)
valid_subjects = np.sum(~np.isnan(marks), axis=1)       # It's to consider nan also

print("Total Marks Per Student :", total_marks)
print("Percentage :", (total_marks/valid_subjects))


# -----------------------------------------------------------------------------------------
# Concept : Handling NaN Values in NumPy
# -----------------------------------------------------------------------------------------
# NaN (Not a Number) represents missing or undefined numeric data.
# Standard functions like np.sum() propagate NaN (sum becomes NaN if any value is NaN).
# Functions prefixed with 'nan' (e.g., np.nansum) ignore NaNs and treat them as 0.
# np.isnan() returns a boolean mask, which can be inverted using '~' to count or filter valid entries.

# -----------------------------------------------------------------------------------------
# Concept : Boolean Upcasting in Arithmetic Operations
# -----------------------------------------------------------------------------------------
# In Python/NumPy, booleans are a subclass of integers (True == 1, False == 0).
# When an arithmetic operation (such as +, -, np.sum) is performed on a boolean array,
# the boolean values are automatically upcasted: True becomes 1 and False becomes 0.
# This makes counting condition matches straightforward: np.sum(condition_mask).


print("----------------------Q4-----------------------")
# --------------------------------------------------------------------------------------------
# Question(VVI)
# The college wants to analyze only Python, Sql, numpy marks for the first 10 students

print(marks[:11,[0,1,3]])

# -----------------------------------------------------------------------------------------
# Concept : Fancy Indexing vs. Slicing in 2D NumPy Arrays
# -----------------------------------------------------------------------------------------
# NumPy array indexing follows the syntax: array[row_selector, column_selector]
#
# 1. Row Selector:
#    - Use ':' (colon) to select all rows along axis 0.
#
# 2. Column Selector:
#    - Python uses 0-based indexing:
#        * 1st column -> index 0
#        * 3rd column -> index 2
#    - Non-contiguous selection requires 'Fancy Indexing' (passing a list or array of indices):
#        * Syntax: [0, 2]
#    - Note: Slice syntax `start:stop:step` (e.g., `0:3:2`) also works if the columns
#      follow a regular step pattern, but fancy indexing `[0, 2]` works for any arbitrary columns.
#
# 3. View vs. Copy:
#    - Standard slicing (:) returns a view of the original array.
#    - Fancy indexing (passing a list [0, 2]) creates an independent copy in memory.
# -----------------------------------------------------------------------------------------


print("----------------------Q5-----------------------")
# --------------------------------------------------------------------------------------------
# Question(VVI)
# The college awards 5 bonus marks in Python to students with at least 90% attendance.
# If attendance is missing, do not award a bonus automatically.

if_attendence = (attendance>=90) & (~np.isnan(attendance))
eligible_student = student_ids[if_attendence]
python_marks = marks[:,0]

# Normal Method -- FOr the problem if Number goes beyond 100
python_marks[if_attendence] = python_marks[if_attendence] + 5
    # First selecting the Python marks then selecting eligiblity
marks[marks>=100] = 100

# Mentos Method -- Use of np.min ❌ np.minimum
python_marks[if_attendence] = np.minimum(python_marks[if_attendence] + 5, 100)

print(eligible_student)
print(marks)

# -----------------------------------------------------------------------------------------
# Concept : Element-wise Comparison with np.minimum vs. Reduction with np.min
# -----------------------------------------------------------------------------------------
# 1. np.min() / np.amin():
#    - Purpose: Aggregation / Reduction.
#    - Finds the single minimum value across an entire array or along a specified axis.
#    - Signature: np.min(a, axis=None, ...)
#    - Example: np.min([10, 20, 5]) -> 5
#    - WRONG USAGE: np.min(array + 5, 100) -> The second argument is interpreted as 'axis=100',
#      causing an AxisError: axis 100 is out of bounds.
#
# 2. np.minimum():
#    - Purpose: Element-wise minimum (Universal function / ufunc).
#    - Compares two arrays (or an array and a scalar via broadcasting) element by element
#      and takes the smaller of the two at each position.
#    - Signature: np.minimum(x1, x2)
#    - Example: np.minimum([95, 102, 98], 100) -> array([95, 100, 98])
#    - Ideal for clamping/capping values to an upper limit (e.g., max grade of 100).
#
# 3. Related Functions:
#    - np.maximum(x1, x2): Element-wise maximum (ideal for floor/lower limits, e.g., max(x, 0)).
#    - np.clip(a, a_min, a_max): Clamps values between both a lower and upper bound simultaneously.
# -----------------------------------------------------------------------------------------

print("----------------------Q6-----------------------")
# --------------------------------------------------------------------------------------------
# Question (VVI)
# Categorize each student as:
# - High attendance: 85% or above
# - Moderate attendance: 70% to below 85%
# - Low attendance: below 70%
# - Unknown: attendance is missing

attend_category = np.where(
    (np.isnan(attendance))|(attendance<0), "Unknown",
    np.where(attendance>=85,"High", 
    np.where(attendance>=70, "Moderate",
    "Low")))
print(attend_category)

# Mentos Method: np.select()
conditions = [
    np.isnan(attendance) | (attendance<0),
    attendance>=85,
    attendance>=70
]
choices = [
    "Unknown",
    "High",
    "Moderate"
]
attend_category = np.select(
    conditions,
    choices,
    default="Low"
)
print(attend_category)


# -----------------------------------------------------------------------------------------
# Concept : Multi-Condition Logic with np.select() vs. Nested np.where()
# -----------------------------------------------------------------------------------------
# 1. Why avoid nested np.where()?
#    - np.where(condition, x, y) is great for simple binary choices (if/else).
#    - For multiple branches (if/elif/elif/else), nesting np.where() leads to messy,
#      hard-to-read "arrowhead" code that is prone to parenthesization bugs.
#
# 2. What is np.select()?
#    - Purpose: Evaluates an ordered list of conditions and returns values from a corresponding
#      list of choices. It acts like a vectorized `if-elif-else` ladder.
#    - Signature: np.select(condlist, choicelist, default=0)
#
# 3. How np.select() evaluates:
#    - First-match semantics: Conditions are evaluated sequentially from top to bottom.
#      Once a condition is met for an element, later conditions are ignored for that element.
#    - Because of this, always place edge cases / NaN checks or the most specific conditions FIRST.
#    - If no condition evaluates to True, the value specified in `default` is assigned.
# -----------------------------------------------------------------------------------------


print("----------------------Q7-----------------------")
# --------------------------------------------------------------------------------------------
# Categorize students into three study bands:
# Less than 2 hours, 2–4 hours inclusive, and more than 4 hours.

conditions = [
    study_hours<2,
    (study_hours>=2) & (study_hours<=4)
    # study_hours>4
]
choicelist = [
    "Bad",
    "Moderate"
]
study_cat = np.select(conditions,choicelist,default="Good")
print(study_cat)

print("----------------------Q8-----------------------")
# --------------------------------------------------------------------------------------------
# Reshape the first 15 students Python marks into a matrix with (3,5)
stude_pyth_resh = marks[:15,0].reshape(3,5)
print(stude_pyth_resh)
print("Shape :",stude_pyth_resh.shape)

print("----------------------Q9-----------------------")
# --------------------------------------------------------------------------------------------
# Count missing values in attendance, each subject, and mock interview scores
miss_count_attendance = np.sum(np.isnan(attendance))
print(miss_count_attendance)
miss_count_subwise = np.sum(np.isnan(marks),axis=0)
print(miss_count_subwise)