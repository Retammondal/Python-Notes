import numpy as np

# --------------------------------------------------------------------------------------------
# Conditional Formatting and Masking
# --------------------------------------------------------------------------------------------
# We can apply Comparison Operator accross all element in Numpy Array Also...

marks = np.array([70, 80, 65, 90, 75])
marks2 = np.array([60, 70, 85, 95, 75])

print(marks>75)                
print(marks > marks2)          
print(marks == marks2)

print("----------------------------------------")
marks = np.array([70, 80, 65, 90, 75])
# Write a code to filter in only the marks > 75

# Normal Method
filteredMarks = []             
for i in marks.tolist():       
    if i>75:
        filteredMarks.append(i)
print(filteredMarks)

# NumPY Method: Conditional formatting and masking in NumPy. Select, filter, or modify 
# array elements based on logical conditions. 

print(marks>75)                # 1. Create a Boolean Mask => Array of True/ False.                                
                               # Output: [False  True False  True False]

print(marks[[False, True, False, True, False]]) 
                               # 2. Filtering / Extracting Values: Pass the boolean 
print(marks[marks>75])         # mask directly into the array's brackets to pull out 
                               # elements where the mask is True. Output: [80 90]

marks[marks>75] = marks[marks>75] + 10
print(marks)                   # 3. Modifying Elements with a Mask

print("----------------------------------------")

prices = np.array([499,799,1299,2499,3999,599])

print(prices[(prices>600) & (prices<1000)]) 
                               # Prices b/w 600-1000. Multiple Condition () is must 
                               # for every condition. Common Mistake : Using and, 
                               # or in Numpy Array condition --> Use & (AND), 
                               # | (OR), ~ (NOT (inverse))

print(prices[(prices<600) | (prices>1000)])
                               # Prices less than 600 or greater than 1000

print(prices[~(prices>900)])   # Prices not greater than 900

print("----------------------------------------")
# 2-D Arrays
# --------------------------------------------------------------------------------------------
marks = np.array([             # For 2-D Arrays...filter out will give result in 1-D 
    [72, 85, 90],              # Array. Why? b/c filter out will give different values 
    [55, 60, 65],              # from diff row and for numpy arrays as every row has 
    [88, 92, 95],              # to be same no. of element so by default comes in 
    [45, 50, 48]               # 1D array.
])

print(marks[marks>70])         # Filter Marks > 70

print(marks[0][marks[0]>80])   # Find marks > 80 only in the first row

print(marks[:,-1][marks[:,-1]>80])
                               # Find mark > 80 only in 3rd Column

print("----------------------------------------")

marks = np.array([
    [72, 85, 90],
    [55, 60, 65],
    [88, 92, 95],
    [45, 50, 48]
])

student_avg = []               # Average Marks of Every Student?? Now how will we 
for student in marks:          # do it??
    avg = np.trunc(np.mean(student)).item()
    student_avg.append(avg)
print(student_avg)

# --------------------------------------------------------------------------------------------
# CONCEPT: NumPy Type Wrapping vs Native Python Types
# --------------------------------------------------------------------------------------------
# • Issue: NumPy operations like np.mean() return NumPy scalars (e.g., np.float64) 
#   instead of native types.
# • Behavior: When appended to a Python list, they retain the wrapper and print as 
#   'np.float64(81.25)'.
# • Solution 1: Use .item() on the NumPy value to pull out the native Python float/int 
#   directly.
# • Solution 2: Explicitly cast the value using the built-in float() or int() constructor.
# --------------------------------------------------------------------------------------------

print(np.trunc(np.mean(marks, axis=1)))
                               # NUMPY Method --> axis. The axis parameter dictates 
                               # the direction along which a data operation (such as 
                               # sum, mean, max, or min) is performed. 
                               # axis=0 refers to the first dimension (running 
                               # vertically downward across rows in 2D). 
                               # axis=1 refers to the second dimension (running 
                               # horizontally across columns in 2D).

print(np.mean(marks, axis=0))  # Average marks of Every Subject ??

# --------------------------------------------------------------------------------------------
# The following array contains marks of 5 students in 4 subjects:
# --------------------------------------------------------------------------------------------
marks = np.array([             # Assume each row represents a student and each 
    [72, 85, 90, 78],          # column represents a subject. Find:
    [65, 70, 96, 80],          # 4. Average marks of every student.
    [88, 92, 95, 90],          # 5. Average marks of every subject.
    [55, 60, 58, 65],          # 6. Students whose average is above 75.
    [78, 82, 85, 88]           # 7. Highest mark obtained in each subject.
])                             # 8. The complete row of the student with the 
                               #    highest average.

student_avg = []               # Avg mark of every student  --> METHOD 1
for student in marks:
    avg = np.mean(student).item()
    student_avg.append(avg)
print(student_avg)

student_avg = np.mean(marks, axis=1)
print(student_avg)             # Avg mark of every student  --> METHOD 2

print(np.mean(marks, axis=0))  # Avg marks of Every Subject

print(marks[student_avg > 75]) # Student avg > 75

print(np.max(marks, axis=0))   # Highest Mark obtained in each subject

index = np.argmax(student_avg) # Show Complete row of student with Highest average
print(marks[index])

# --------------------------------------------------------------------------------------------
# Conditional Choice with np.where()
# --------------------------------------------------------------------------------------------
marks = np.array([45,72,88,31,65,91])
                               
print(np.where(marks>70, "Good", "Average"))
                               # Conditional Choice with np.where() ~ Works like 
                               # if-else. Use:
                               # np.where(condition, value_if_true, value_if_false) 

updated_marks = np.where(marks<50, marks+5, marks)
print(updated_marks)           # Students scoring < 50 get 5 grace marks

result = np.where(marks<50,"Fail",np.where(marks<90, "Pass", "Excellent"))
print(result)                  # >= 90 : Excellent, 50-89 : Pass, <50 : Fail 
                               # ==> Nested Condition