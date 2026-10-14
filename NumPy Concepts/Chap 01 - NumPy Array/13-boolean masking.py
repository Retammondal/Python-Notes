import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Comparison Operators & Boolean Masking
# --------------------------------------------------------------------------------------------
# We can apply Comparison Operators across all elements in a NumPy Array.
# Conditional formatting and masking in NumPy allows us to select, filter, 
# or modify array elements based on logical conditions.

marks = np.array([70, 80, 65, 90, 75])
marks2 = np.array([60, 70, 85, 95, 75])

print(marks > 75)              
print(marks > marks2)
print(marks == marks2)
# -------------------------------------------------------------------------
filteredMarks = []             # Normal Python Method to filter marks > 75
for i in marks.tolist():       
    if i>75:
        filteredMarks.append(i)
print(filteredMarks)

# -------------------------------------------------------------------------
print(marks > 75)              # NumPY Method Step 1: Create a Boolean Mask 
                               # => Array of True/False. 
                               # Output: [False  True False  True False]

print(marks[[False, True, False, True, False]]) 
print(marks[marks > 75])       # Step 2: Filtering / Extracting Values. Pass the 
                               # boolean mask directly into the array's brackets 
                               # to pull out elements where mask is True.

marks[marks > 75] = marks[marks > 75] + 10
print(marks)                   # Step 3: Modifying Elements with a Mask


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Multiple Conditions
# --------------------------------------------------------------------------------------------
# Common Mistake : Using 'and', 'or' in Numpy Array condition 
# --> Use & (AND), | (OR), ~ (NOT (inverse))
# Multiple Condition () is must for every condition

prices = np.array([499,799,1299,2499,3999,599])

print(prices[(prices>600) & (prices<1000)]) 
                               # Prices b/w 600-1000

print(prices[(prices<600) | (prices>1000)])
                               # Prices less than 600 or greater than 1000

print(prices[~(prices>900)])   # Prices not greater than 900


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Filtering 2-D Arrays
# --------------------------------------------------------------------------------------------
# For 2-D Arrays... filtering out will give the result in a 1-D Array.
# Why? Because filtering will give different numbers of values from different rows,
# and for NumPy arrays every row MUST have the same number of elements. So it 
# defaults to flattening into a 1D array.

marks = np.array([
    [72, 85, 90],
    [55, 60, 65],
    [88, 92, 95],
    [45, 50, 48]
])

print(marks[marks > 70])       # Filter Marks > 70

print(marks[0][marks[0] > 80]) # Find marks > 80 only in the first row

print(marks[:, -1][marks[:, -1] > 80])
                               # Find mark > 80 only in 3rd Column


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. CONCEPT: NumPy Type Wrapping vs Native Python Types
# --------------------------------------------------------------------------------------------
# • Issue: NumPy operations like np.mean() return NumPy scalars (e.g., np.float64) 
#   instead of native types.
# • Behavior: When appended to a Python list, they retain the wrapper and print as 
#   'np.float64(81.25)'.
# • Solution 1: Use .item() on the NumPy value to pull out the native Python 
#   float/int directly.
# • Solution 2: Explicitly cast the value using the built-in float() or int().

# Question --> Student (Row), Subject (Column)
marks = np.array([
    [72, 85, 90],
    [55, 60, 65],
    [88, 92, 95],
    [45, 50, 48]
])

student_avg = []               # Average Marks of Every Student?? 
for student in marks:          # Normal loop implementation
    avg = np.trunc(np.mean(student)).item()
    student_avg.append(avg)
print(student_avg)


print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. The Axis Parameter (Rows vs Columns)
# --------------------------------------------------------------------------------------------
# The axis parameter dictates the direction along which a data operation (such as 
# sum, mean, max, or min) is performed.
# axis=0 refers to the first dimension (running vertically downward across rows).
# axis=1 refers to the second dimension (running horizontally across columns).

print(np.trunc(np.mean(marks, axis=1)))
                               # NUMPY Method --> Average of every student 

print(np.mean(marks, axis=0))  # Average marks of Every Subject


print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# 6. Real World Example / Logical Questions
# --------------------------------------------------------------------------------------------
# The following array contains marks of 5 students in 4 subjects:
# Assume each row represents a student and each column represents a subject.
#
# Find:
# 1. Average marks of every student.
# 2. Average marks of every subject.
# 3. Students whose average is above 75.
# 4. Highest mark obtained in each subject.
# 5. The complete row of the student with the highest average.

marks = np.array([
    [72, 85, 90, 78],
    [65, 70, 96, 80],
    [88, 92, 95, 90],
    [55, 60, 58, 65],
    [78, 82, 85, 88]
])

student_avg = []               # 1. Avg mark of every student --> METHOD 1
for student in marks:
    avg = np.mean(student).item()
    student_avg.append(avg)
print(student_avg)

student_avg = np.mean(marks, axis=1)
print(student_avg)             # Avg mark of every student --> METHOD 2

print(np.mean(marks, axis=0))  # 2. Avg marks of Every Subject

print(marks[student_avg > 75]) # 3. Student avg > 75

print(np.max(marks, axis=0))   # 4. Highest Mark obtained in each subject

index = np.argmax(student_avg) # 5. Show Complete row of student with Highest 
print(marks[index])            # average


print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# 7. Conditional Choice with np.where()
# --------------------------------------------------------------------------------------------
# Conditional Choice with np.where() ~ Works like if-else
# Use: np.where(condition, value_if_true, value_if_false)

marks = np.array([45,72,88,31,65,91])
                               
print(np.where(marks>70, "Good", "Average"))

updated_marks = np.where(marks<50, marks+5, marks)
print(updated_marks)           # Students scoring < 50 get 5 grace marks

result = np.where(marks<50, "Fail", np.where(marks<90, "Pass", "Excellent"))
print(result)                  # >= 90 : Excellent, 50-89 : Pass, <50 : Fail 
                               # ==> Nested Condition