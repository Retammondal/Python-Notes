print("-----------------------1---------------------------")
# Question : 
# A shop has five products with prices:
# 100, 250, 400, 550, 800
#
# Create a NumPy array
# and calculate the price after applying a 15% discount to every product.

import numpy as numpy
productPrices = numpy.array([100, 250, 400, 550, 800])
print(productPrices)

discount = 15                       # in percent
discount = (100-discount)/100       # 0.85

finalPrice = numpy.round((productPrices * discount)).astype(int).tolist()

print("Original Prices :",productPrices)
print("Final Prices in List format : ", finalPrice)

# -----------------------------------------------------------------------------------------
# Concept : Numpy Rounding and Convert Datatype
# -----------------------------------------------------------------------------------------
# numpy.round(Numpy Array)
# (Numpy Array).astype(int/float/bool)
# -----------------------------------------------------------------------------------------

print("-----------------------2---------------------------")
# Question : 
# A student's marks are stored in a tuple:
# (78, 85, 92, 67, 88)
# Convert the tuple into a NumPy array and add 3 marks to every value.

studentMarks = (78, 85, 92, 67, 88)
studentMarks = numpy.array(studentMarks)

print("Previous Student Marks -> ", studentMarks.tolist())
print("Updated(+3) Student Marks(List) -> ", (studentMarks + 3).tolist())
print("Updated(+3) Student Marks(Tuple) -> ", tuple((studentMarks + 3).tolist()))

# -----------------------------------------------------------------------------------------
# Concept : Tuple in Numpy array
# -----------------------------------------------------------------------------------------
# Just like List, do with Tuple also..
# Convert Numpy Array to List : Numpyarray.tolist()
# Convert Numpy Array to Tuple : tuple(Numpyarray.tolist())
# -----------------------------------------------------------------------------------------

print("-----------------------3---------------------------")
# A company records sales for four quarters:

# Q1 = 125000
# Q2 = 148000
# Q3 = 135000
# Q4 = 172000

# Create a NumPy array.

# The company expects next year's sales to be 15% higher than this year's sales. 
# Calculate the expected sales for each quarter.

# Then calculate the additional sales expected in each quarter.

year2024 = numpy.array([125000, 148000, 135000, 172000])
year2025 = (year2024 * 1.15).astype(int)

print("Year 2024 Sales -> ", year2024.tolist())
print("Additional Sales Expected -> ", (year2025-year2024).tolist())
print("Year 2025 Expected Sales -> ", year2025.tolist())


print("-----------------------4---------------------------")
# A college wants to initialize a marks table for 5 students and 4 subjects.
# Initially, every student's marks are set to zero.
# Create this using NumPy.
# Then create another 5 × 4 array containing a default value of 50.

marks_table = numpy.zeros((5,4))
print(marks_table)

print((marks_table + 50).astype(int))

#OR,
updated = numpy.full((5,4),50,dtype=int)
print(updated)


print("-----------------------4---------------------------")
# A company wants to set targets from ₹20,000 to ₹1,00,000.
# Generate exactly 9 target values, equally spaced.
# Then create actual sales:
# [18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000]

# Calculate the difference between actual and target.

company_target = numpy.linspace(20000, 100000, 9)
company_actual = numpy.array([18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000])

print("Targeted Sale ->", company_target)
print("Actual Sale ->", company_actual)
print("Diffence :", (company_actual-company_target).astype(int).tolist())


print("-----------------------5---------------------------")
# --------------------------------------------------------------------------------
# Question : 
# A college stores marks of 4 students in 3 subjects: Maths, Science, and English.

# import numpy as np

# marks = np.array([
#     [72, 85, 90],
#     [65, 78, 82],
#     [88, 91, 84],
#     [70, 76, 80]
# ])

# Perform the following:

# Display the Science marks of the second student.
# Add 5 bonus marks to every student's English marks.
# Change the Maths marks of the fourth student to 75.
# Display the final marks array.
# --------------------------------------------------------------------------------
# Science marks of Second Student --> (1,1)
marks = numpy.array([
    [72, 85, 90],
    [65, 78, 82],
    [88, 91, 84],
    [70, 76, 80]
])
print(marks[1,1])
# Slicing: [row_start:row_end, col_start:col_end]
# Add 5 bonus marks to every student's English marks. --> Want all row, only 3rd col
marks[:,2] += 5
# Change the Maths marks of the fourth student to 75.
marks[3,0] = 75
print(marks)


print("-----------------------6---------------------------")
# --------------------------------------------------------------------------------
# Question
# A company records monthly sales for 3 branches. 
# The columns represent January, February, and March.

# sales = np.array([
#     [120, 150, 180],
#     [100, 130, 160],
#     [200, 220, 250]
# ])

# Perform the following:

# Display the complete sales data of Branch 2.
# Display the sales of all branches in February.
# Increase the March sales of every branch by 10%.
# Display the updated sales array.
# --------------------------------------------------------------------------------
# Display the complete sales data of Branch 2.
sales = numpy.array([
    [120, 150, 180],
    [100, 130, 160],
    [200, 220, 250]
])
bra2_Sales = sales[1]       
bra2_Sales = sales[1,:]     # Both can be done
print(bra2_Sales)
# Display the sales of all branches in February.
print(sales[:,1])
# Increase the March sales of every branch by 10%.
mar_sales = sales[:,2] * 1.10

print(mar_sales)

# Update the Original Sales data
sales[:,2] = mar_sales
print(sales)

print("-----------------------7---------------------------")
# --------------------------------------------------------------------------------
# Question : 
# An organization stores employee information as:

# Salary | Experience
# employees = np.array([
#     [30000, 2],
#     [40000, 4],
#     [50000, 6],
#     [60000, 8]
# ])

# Perform the following:

# Display the information of the last employee using negative indexing.
# Display the salary of the second employee.
# Increase the salary of the third employee by 15%.
# Add 1 year of experience to the first employee.
# Display the final employee array.
# --------------------------------------------------------------------------------
employees = numpy.array([
    [30000, 2],
    [40000, 4],
    [50000, 6],
    [60000, 8]
])
print(employees[-1])    #last emmployee
print("Salary of 2nd Employee :", employees[1,0])
# Increase the salary
employees[2,0] = employees[2,0]*1.15
employees[0,1] = employees[0,1]+1

print(employees)

print("-----------------------8---------------------------")

# --------------------------------------------------------------------------------
# A company has recorded its monthly revenue for the first 6 months:

# revenue = np.array([120000, 135000, 142000, 150000, 165000, 172000])

# Write a NumPy program to:

# 1. Display the revenue of the third month.
# 2. Display the revenue of the last month using negative indexing.
# 3. Select the revenue from Month 2 to Month 5 using slicing.
# 4. Increase the revenue of the last 3 months by 10%.
# 5. Add 40000 revenue to 1st month
# 6. Display the final revenue array.
# --------------------------------------------------------------------------------

revenue = numpy.array([120000, 135000, 142000, 150000, 165000, 172000])
print("Revenue of 3rd Month ->", revenue[2])
print("Revenue of last Month ->", revenue[-1])
print("Revenue from Month 2-5 ->", revenue[1:5])

revenue[-3:] = revenue[-3:] * 1.10
revenue[0] = revenue[0] + 40000
print("Last 3 Month increment by 10% ....")
print("First Month increment by 40,000 ....")
print("Final Revenue Array ->", revenue)

print("-----------------------9---------------------------")

# --------------------------------------------------------------------------------
# A factory operates for 30 days and wants to create a production schedule
# starting from 500 units per day and gradually increasing to 1,500 units per day.

# Tasks
# Generate exactly 30 production targets using np.linspace().
# Create day numbers from 1 to 30 using np.arange().
# Display the first 5 production targets.
# Display the last 5 production targets.
# Increase every production target by 10%.
# Display the first 5 updated targets.
# --------------------------------------------------------------------------------

dayNum = numpy.arange(1,31)
target = numpy.linspace(500,1500,30, dtype=int)

print("First 5 Target -> ", target[:5])
print("Last 5 Target -> ", target[-5:])
print("Updating Every Target by 10% ...")

target[:] = target[:] * 1.10

print("First 5 Updated -> ", target[:5])

import numpy as np

print("-----------------------10---------------------------")

# --------------------------------------------------------------------------------
# A college records marks of 5 students in 4 subjects.

marks = numpy.array([
    [72, 85, 90, 78],
    [65, 70, 75, 80],
    [88, 92, 95, 90],
    [55, 65, 60, 70],
    [78, 82, 85, 88]
])

# Each row represents a student and each column represents a subject.

# Tasks:
# 1. Determine the number of dimensions.
# 2. Determine the number of students and subjects using shape.
# 3. Determine the total number of marks using size.
# 4. Display the complete marks of the 3rd student.
# 5. Display marks of all students in the 2nd subject.
# 6. Extract marks of the first 3 students in the first 2 subjects.
# 7. Increase the marks of the last 2 students in the 4th subject by 5.
# --------------------------------------------------------------------------------
print("Dimensions", marks.ndim)

row,column = marks.shape
print("No. of Students ->", row)
print("No. of Subjects ->", column)
print("Total No of Marks ->", marks.size)
print("Displaying the 3rd Student Marks ->", marks[2,:])
print("Displaying 2nd Sub all students marks ->", marks[:,1])
print("Extracting first 3 student, first 2 sub ->", marks[:3,:2])
print("Increasing the marks of last 2 students in 4th sub by 5 ..")

marks[-2: ,3] = marks[-2: ,3] + 5
print("Updated Marks List ::: ", marks)