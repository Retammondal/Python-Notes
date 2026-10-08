print("-----------------------1---------------------------")
# Question : 
# A shop has five products with prices:
# 100, 250, 400, 550, 800
#
# Create a NumPy array
# and calculate the price after applying a 15% discount to every product.

import numpy as np
productPrices = np.array([100, 250, 400, 550, 800])
print(productPrices)

discount = 15                       # in percent
discount = (100-discount)/100       # 0.85

finalPrice = np.round((productPrices * discount)).astype(int).tolist()

print("Original Prices :",productPrices)
print("Final Prices in List format : ", finalPrice)

# -----------------------------------------------------------------------------------------
# Concept : Numpy Rounding and Convert Datatype
# -----------------------------------------------------------------------------------------
# np.round(Numpy Array)
# (Numpy Array).astype(int/float/bool)
# -----------------------------------------------------------------------------------------

print("-----------------------2---------------------------")
# Question : 
# A student's marks are stored in a tuple:
# (78, 85, 92, 67, 88)
# Convert the tuple into a NumPy array and add 3 marks to every value.

studentMarks = (78, 85, 92, 67, 88)
studentMarks = np.array(studentMarks)

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

year2024 = np.array([125000, 148000, 135000, 172000])
year2025 = (year2024 * 1.15).astype(int)

print("Year 2024 Sales -> ", year2024.tolist())
print("Additional Sales Expected -> ", (year2025-year2024).tolist())
print("Year 2025 Expected Sales -> ", year2025.tolist())


print("-----------------------4---------------------------")
# A college wants to initialize a marks table for 5 students and 4 subjects.
# Initially, every student's marks are set to zero.
# Create this using NumPy.
# Then create another 5 × 4 array containing a default value of 50.

marks_table = np.zeros((5,4))
print(marks_table)

print((marks_table + 50).astype(int))

#OR,
updated = np.full((5,4),50,dtype=int)
print(updated)


print("-----------------------4---------------------------")
# A company wants to set targets from ₹20,000 to ₹1,00,000.
# Generate exactly 9 target values, equally spaced.
# Then create actual sales:
# [18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000]

# Calculate the difference between actual and target.

company_target = np.linspace(20000, 100000, 9)
company_actual = np.array([18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000])

print("Targeted Sale ->", company_target)
print("Actual Sale ->", company_actual)
print("Diffence :", (company_actual-company_target).astype(int).tolist())


print("-----------------------5---------------------------")
# --------------------------------------------------------------------------------
# Question : 
# A college stores marks of 4 students in 3 subjects: Maths, Science, and English.

# import np as np

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
marks = np.array([
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
sales = np.array([
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
# Display the sales of the second employee.
# Increase the sales of the third employee by 15%.
# Add 1 year of experience to the first employee.
# Display the final employee array.
# --------------------------------------------------------------------------------
employees = np.array([
    [30000, 2],
    [40000, 4],
    [50000, 6],
    [60000, 8]
])
print(employees[-1])    #last emmployee
print("Salary of 2nd Employee :", employees[1,0])
# Increase the sales
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

revenue = np.array([120000, 135000, 142000, 150000, 165000, 172000])
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

dayNum = np.arange(1,31)
target = np.linspace(500,1500,30, dtype=int)

print("First 5 Target -> ", target[:5])
print("Last 5 Target -> ", target[-5:])
print("Updating Every Target by 10% ...")

target[:] = target[:] * 1.10

print("First 5 Updated -> ", target[:5])


print("-----------------------10---------------------------")

# --------------------------------------------------------------------------------
# A college records marks of 5 students in 4 subjects.

marks = np.array([
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

print("-----------------------11---------------------------")

# --------------------------------------------------------------------------------
# A warehouse has 4 storage sections and 5 products.

# Initially, every product has a stock level of 100 units.

# Tasks
# 1. Create a 4 x 5 array where every value is 100.
# 2. Increase the stock of the first two sections by 20 units.
# 3. Reduce stock of the last two products by 10%.
# 4. Display only the middle two sections.
# 5. Display the bottom-right 2 x 2 portion of the matrix.
# --------------------------------------------------------------------------------

warehouse = np.full((4,5), 100)
warehouse[:2,:] = warehouse[:2,:] + 20
warehouse[:,-2:] = warehouse[:,-2:] * 0.90

print(warehouse)
print(warehouse[1:3,:])
print(warehouse[-2:,-2:])

print("-----------------------12---------------------------")

# --------------------------------------------------------------------------------
# A startup expects its monthly users to grow from 10,000 to 100,000 over 12 months.

# Tasks
# 1. Generate monthly user targets using np.linspace().
# 2. Create month numbers using np.arange().
# 3. Display users expected in Month 1 and Month 12.
# 4. Display users expected from Months 4-8.
# 5. Increase all targets by another 15%.
# 6. Display the updated targets for the last 4 months.
# --------------------------------------------------------------------------------
import numpy as np

month = np.arange(1, 13)
user_expected = np.linspace(10000, 100000, 12, dtype=int)

print("Months:", month)
print("Expected Users:", user_expected)

print("Months 5 to 9 Expected Users:", user_expected[4:9])

user_expected = (user_expected * 1.15).astype(int)

startup = np.array([month.tolist(), user_expected.tolist()])

print("Combined Startup Matrix:\n", startup)

print("Updated Targets for Last 4 Months:", user_expected[-4:])


print("-----------------------13---------------------------")

# --------------------------------------------------------------------------------
# A simple grayscale image can be represented as a 2D NumPy array 
# where each number represents pixel intensity.

image = np.array([
    [10, 20, 30, 40, 50],
    [20, 30, 40, 50, 60],
    [30, 40, 50, 60, 70],
    [40, 50, 60, 70, 80],
    [50, 60, 70, 80, 90]
])

# Tasks:
# 1. Find the dimensions of the image.
# 2. Find its shape.
# 3. Find the total number of pixels.
# 4. Display the center pixel.
# 5. Extract the top-left 3 × 3 region.
# 6. Extract the bottom-right 2 × 2 region.
# 7. Increase the intensity of the center 3 × 3 region by 20.
# 8. Display the modified image.
# --------------------------------------------------------------------------------
print(image.ndim)
print(image.shape)
print(image.size)
print(image[2,2])
print(image[:4,:4])
print(image[-2:,-2:])

image[1:-1,1:-1] = image[1:-1,1:-1] + 20
print(image)

print("-----------------------14---------------------------")

# --------------------------------------------------------------------------------
# A classroom has 6 rows and 5 seats per row.
# Initially, all seats are empty.
#
# 0 = Empty
# 1 = Occupied
#
# Tasks:
# 1. Create a 6 × 5 array filled with zeros.
# 2. Mark the first seat of the first row as occupied.
# 3. Mark all seats in the 3rd row as occupied.
# 4. Mark the last two seats of the last row as occupied.
# 5. Display the first 3 rows.
# 6. Display the last 2 columns.
# 7. Display the complete seating matrix.
# --------------------------------------------------------------------------------

classroom = np.zeros((6,5))
classroom = np.full((6,5), 0)
# Why am I taking full, because I want Integer; but np.zeros give decimal
classroom[0,0] = 1
classroom[2] = 1
classroom[-1,-2:] = 1

print(classroom)
print(classroom[:2])
print(classroom[:,-2:])

print("-----------------------15---------------------------")

# --------------------------------------------------------------------------------
# An electricity board records the monthly electricity consumption of a household for one year:

consumption = np.array([
    180, 220, 195, 250,
    280, 310, 295, 270,
    240, 210, 190, 230
])

# Perform the following:

# 1. Find the total annual consumption.
# 2. Calculate average monthly consumption.
# 3. Find the highest and lowest consumption.
# 4. Find the month index with the highest consumption.
# 5. Extract the first 6 months using slicing.
# 6. Extract alternate months.
# 7. Find all months where consumption was greater than the annual average.
# --------------------------------------------------------------------------------
print("Total Annual Consumption:", np.sum(consumption))
print("Avg Monthly Consumption:", np.mean(consumption))
print("Max Monthly Consumption:", np.max(consumption))
print("Min Monthly Consumption:", np.min(consumption))
print("Max Consumption Month Index:", np.argmax(consumption))
print("First 6 Month Data:", consumption[:7])
print("Alternate Months:", consumption[::2])
print("Months Consum>Avg:", consumption[consumption > np.mean(consumption)])


print("-----------------------16---------------------------")
# --------------------------------------------------------------------------------
# Suppose a loan applicant must satisfy both:
#
# sales >= ₹50,000
# credit score >= 700
#
# Then approve, else reject.

sales = np.array([60000, 40000, 75000, 55000, 30000])
credit_score = np.array([720, 750, 680, 710, 800])
# --------------------------------------------------------------------------------
result = np.where((sales>=50000) & (credit_score>=700), "Approve", "Reject")
print(result)

print("-----------------------17---------------------------")
# --------------------------------------------------------------------------------
# Suppose a customer receives free shipping if:
#
# order value >= ₹1,000
#
# OR
#
# customer is a premium customer.

order_value = np.array([500, 1200, 700, 800, 1500])
premium = np.array([False, False, True, False, True])
# --------------------------------------------------------------------------------
result = np.where((order_value>=1000) | (premium==True), "Yes", "No")
result = np.where((order_value>=1000) | (premium), "Yes", "No")
print(result)

# -----------------------------------------------------------------------------------------
# Concept : Boolean Varibles
# -----------------------------------------------------------------------------------------
# Rule of Thumb: Never use == True or == False when checking boolean variables. 
# Just pass the variable itself (or ~variable for False).
# -----------------------------------------------------------------------------------------

print("-----------------------17---------------------------")
# --------------------------------------------------------------------------------
students = np.array([
    [101, 78, 85, 92],
    [102, 45, 55, 60],
    [103, 91, 88, 95],
    [104, 62, 70, 68],
    [105, 35, 42, 50]
])
# Student_ID | Python | SQL | ML
# Calculate average marks of each student

# Let's classify students as:
# Average >= 85 → Excellent
# Average >= 60 → Good
# Average >= 50 → Pass
# Otherwise → Fail
# --------------------------------------------------------------------------------

students_marks = students[:,1:]
avg_marks = np.mean(students_marks,axis=1)
grade = np.where(avg_marks>=85, "Excellent", np.where(avg_marks>=60, "Good", np.where(avg_marks>=50, "Pass", "Fail")))
print(students_marks)
print(avg_marks)
print(grade)


print("-----------------------18---------------------------")

# --------------------------------------------------------------------------------
# (VVI) Question:
employees = np.array([
    [101, 35000, 2],
    [102, 48000, 4],
    [103, 62000, 6],
    [104, 40000, 3],
    [105, 75000, 8],
    [106, 55000, 5]
])

# Columns represent:
# Employee ID | Salary | Experience

# Find:
# 1. Employees earning more than ₹50,000.
# 2. Employees with more than 4 years of experience.
# 3. Employees earning more than ₹50,000 AND having more than 4 years of experience.
# 4. Average sales of employees satisfying condition 3.
# 5. Employee with the highest sales.
# 6. Employees earning below the median sales.
# --------------------------------------------------------------------------------
# 1. Employees earning more than ₹50,000.
print(employees[:,1]>50000)         # Boolean Mask (True False True)
print(employees[employees[:,1]>50000])  # Working Like 1D Array

# 2. Employees with more than 4 years of experience.
print(employees[:,2]>4)         
print(employees[employees[:,2]>4])  

# 3. Employees earning more than ₹50,000 AND having more than 4 years of experience.
print((employees[:,1]>50000) & (employees[:,2]>4))       
print(employees[(employees[:,1]>50000) & (employees[:,2]>4)])  

# 4. Average sales of employees satisfying condition 3.
condition3 = employees[(employees[:,1]>50000) & (employees[:,2]>4)]
print(np.round(np.mean(condition3[1])))

# 5. Employee with the highest sales.
sales = employees[:,1]      # --> sales array
index = np.argmax(sales)
print(employees[index])

# 6. Employees earning below the median sales.
avg_sales = np.mean(employees[:,1])
print("Average Sales -> ", avg_sales)
print(employees[employees[:,1] > avg_sales])


print("-----------------------19---------------------------")
# --------------------------------------------------------------------------------
# (VVI) Question : 
employees = np.array([
    [101, 45000, 120000],
    [102, 60000, 180000],
    [103, 35000, 90000],
    [104, 75000, 250000],
    [105, 50000, 160000]
])

# Columns:
# Employee_ID | Salary | Sales

# 1. Employees with sales >= ₹150,000 receive 5% commission, otherwise 2% commission.

# 2. Sales > 200000 → Excellent,
#    Sales >= 150000 → Good,
#    Else → Improvement.
# --------------------------------------------------------------------------------

sales = employees[:,-1]
print(sales)
print(sales >= 150000)


category = np.where(sales > 200000, "Excellent", np.where((sales > 150000), "Good", "Needs Improvement"))
print(category)
# print(empl)

commission = np.where(sales>=150000, sales*0.05, sales*0.02)
print(commission)

# How to Change the actual array?
employees[:,-1] = employees[:,-1] + commission
print(employees)

print("-----------------------20---------------------------")
# --------------------------------------------------------------------------------
# An e-commerce company records the quantity sold and selling price of 12 products.

quantity = np.array([2, 5, 3, 8, 4, 6, 10, 1, 7, 5, 9, 3])

price = np.array([
    1200, 800, 1500, 450, 2200, 900,
    700, 1800, 650, 1300, 500, 2500
])
# Find products whose revenue is above the average revenue.
# Apply a 10% discount only to products whose price is greater than ₹1,000.
# Round the discounted prices to two decimal places.
# Identify products whose price is above the median and whose quantity is at least 5.
# --------------------------------------------------------------------------------
revenue = quantity * price
print(revenue)
avg_revenue = np.mean(revenue)
print(avg_revenue)
print(price[revenue>avg_revenue])

# 10% Discount
discounted_price = np.round(np.where(price>1000, 0.9*price, price),2)
print(discounted_price)

avg_product_price = np.mean(price)
print(price[(price>avg_product_price) & (quantity>=5)])

print("-----------------------21---------------------------")
# --------------------------------------------------------------------------------
# A company's monthly sales for one year are:
sales = np.array([
    120000, 135000, 128000, 150000,
    160000, 172000, 165000, 180000,
    195000, 210000, 205000, 225000
])
# Create a forecast for the next 6 months using np.linspace() between:
# the minimum observed sales
# and 20% above the maximum observed sales.

# Round the forecast values to the nearest rupee.
# Combine the original sales and forecast into one 18-element array.
# Reshape the combined array into 3 × 6.
# Calculate the average sales for each row.
# --------------------------------------------------------------------------------
min_sales = np.min(sales)
max_sales = np.max(sales)
forecast = np.round(np.linspace(min_sales, max_sales*1.20, 6))
print(forecast)

# Combine the original sales and forecast into one 18-element array.
combined_sales = np.append(sales, forecast)
print(combined_sales)
reshaped_sales = combined_sales.reshape(3,6)
print(reshaped_sales)
print(np.round(np.mean(reshaped_sales, axis=1)))


print("-----------------------22---------------------------")
# --------------------------------------------------------------------------------
# A factory collects temperatures from 20 sensor readings:

temperature = np.array([
    28.5, 31.2, 29.8, 35.6, 38.1,
    40.2, 27.9, 30.5, 42.3, 39.8,
    36.4, 33.2, 29.1, 41.7, 44.2,
    31.8, 34.5, 37.6, 26.9, 43.1
])

# Calculate mean, median, minimum and maximum.
# Calculate variance and standard deviation.
# Find all temperatures more than standard deviation above the mean.
# Find the five readings having the largest deviation from the mean. (Top 5 Waala Question..)
# Find the number and percentage of critical readings(>=40).
# Reshape the readings into a 4 × 5 array.
# Find the average temperature for each row.
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Concept :
# Relation b/w Variance and Std => Square of std. is Variance
# --------------------------------------------------------------------------------
mean = np.mean(temperature)
median = np.median(temperature)
maximum = np.max(temperature)
minimum = np.min(temperature)
std = np.std(temperature)
var = np.square(std)
print("Mean", mean)
print("Median", median)
print("Maximum", maximum)
print("Minimum",minimum)
print("Standard Deviation", std)
print("Variance", var)

print(temperature[temperature> (std + mean)])

deviation = np.abs(temperature - mean)
largest_deviation = np.sort(deviation)      # By default give descending order
print(largest_deviation)
# To get Top 5 from largest_deviation --> We need to get Last 5 (As Descending Order)
large5 = largest_deviation[-5:]         # will again give in back order [7.18 7.22 7.98 ]
large5 = largest_deviation[-1:-5:-1]         # will again give in back order [7.18 7.22 7.98 ]
print(large5)

critical_readings = temperature[temperature>=40]
print(critical_readings.size)
print(critical_readings.size*100/temperature.size)


print("-----------------------23---------------------------")
# --------------------------------------------------------------------------------
# Consider the following loan portfolio:

loan_amount = np.array([
    100000, 250000, 500000, 750000,
    120000, 350000, 900000, 450000
])
interest_rate = np.array([
    8.5, 9.2, 8.8, 10.1,
    7.9, 9.5, 10.5, 8.7
])
# Categorize loans:
# Rate >= 10 → High
# Rate >= 9 → Medium
# Otherwise → Low

# Round interest to 2 decimal places.
# Find median loan amount.
# Find loans above median amount AND interest above average interest.
# Calculate standard deviation of interest rates.
# --------------------------------------------------------------------------------
category = np.where(interest_rate>=10, "High", np.where(interest_rate>=9, "Medium", "Low"))
print(category)

median_amount = np.median(loan_amount)
median_interest = np.median(interest_rate)
print(median_amount)

print(loan_amount[(loan_amount>median_amount) & (interest_rate>median_interest)])
print(np.round(np.std(interest_rate),2))


print("-----------------------24---------------------------")
# --------------------------------------------------------------------------------
# The coordinates of eight delivery locations are:
points = np.array([
    [3, 4],
    [5, 12],
    [8, 15],
    [7, 24],
    [9, 40],
    [12, 35],
    [15, 20],
    [6, 8]
])

# Each row contains:
# [x, y]
# Calculate distance from the origin using:
# distance = √(x² + y²)

# Extract x and y coordinates.
# Calculate distance for every location.
# Round distances to 2 decimals.
# Find nearest and farthest location.
# Find average distance.
# Find locations above average distance.

# Categorize:
# if >= 30 → Long
# elif >= 15 → Medium
# Otherwise → Short

# Find percentage of Long-distance deliveries.
# Flatten the coordinate array.
# --------------------------------------------------------------------------------
x_points = points[:,0]
y_points = points[:,1]
distance = np.round(np.sqrt(np.square(x_points) + np.square(y_points)),2)

print(distance)
print("Nearest :", np.min(distance))
print("Farthest :", np.max(distance))

print(np.mean(distance))
print(points[distance>np.mean(distance)])

category = np.where(distance>=30, "Long",np.where(distance>=15, "Medium", "Short"))
print(category)

long_dist_no = category[category == "Long"].size
print(long_dist_no*100 / distance.size)

print(points.flatten())


print("-----------------------25---------------------------")
# --------------------------------------------------------------------------------
# (VVI) Question : 
patient = np.array([
    [101, 120, 85, 98],
    [102, 135, 92, 96],
    [103, 110, 78, 99],
    [104, 150, 88, 94],
    [105, 125, 95, 97],
    [106, 160, 82, 93],
    [107, 115, 90, 98],
    [108, 145, 87, 95],
    [109, 130, 91, 96],
    [110, 155, 80, 92]
])
# Patient_ID, Heart_Rate, Oxygen_Level, Recovery_Score

# Calculate average heart rate.
# Calculate median oxygen level.
# Find patients with heart rate above average AND oxygen below 90.

# Categorize recovery:
# >= 97 → Excellent
# >= 95 → Stable
# Otherwise → Monitor

# Count each category.(***)
# Find patient with highest heart rate.
# Find oxygen levels more than 1 standard deviation below the mean.
# --------------------------------------------------------------------------------
patient_id = patient[:,0]
heart_rate = patient[:,1]
oxygen_level = patient[:,2]
recovery = patient[:,3]

print(np.mean(heart_rate))
print(np.median(oxygen_level))
print(patient[(heart_rate>np.mean(heart_rate)) & (oxygen_level<90)])

category = np.where(recovery>=97,"Excellent", np.where(recovery>=95,"Stable", "Monitor"))
print(category)

# Count each category.
print(category == "Excellent")          # Result in [True False  True False]
print(np.sum(category == "Excellent"))  # Total Sum where True is present
print(np.sum(category == "Stable"))
print(np.sum(category == "Monitor"))

print(patient[np.argmax(heart_rate)])
print(oxygen_level[oxygen_level> (np.mean(oxygen_level) - np.std(oxygen_level))])
# --------------------------------------------------------------------------------

