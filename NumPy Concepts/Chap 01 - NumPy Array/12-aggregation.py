print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. What is Statistics?? / Aggregation in NumPy
# --------------------------------------------------------------------------------------------
# Aggregation means combining or summarizing multiple values of an array into a single result/value.
#
# Common aggregation functions in NumPy:
# np.sum()    -> Calculates the sum of all elements
# np.mean()   -> Calculates the average (mean)  --> always gives in Float
# np.min()    -> Finds the minimum value
# np.max()    -> Finds the maximum value
# np.median() -> Middle Element/ average of middle elements
# np.std()    -> Calculates the standard deviation

import numpy as np

sales = np.array([100,200,300,250,400,500])

# Basic Python Method
sum = 0                       
for elem in sales:
    sum += elem
print(sum)

# NumPY Method
print(np.sum(sales))           
print(np.mean(sales))           # print(np.avg(sales)) --> No avg in numpy => mean
print(np.max(sales))
print(np.min(sales))
print(np.median(sales))


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Special Case : Finding Max by Normal Python Method (When all are Negative)
# --------------------------------------------------------------------------------------------
sales = np.array([-100,-200,-300,-50,-500])

# Wrong Approach -- ❌
max = 0
for s in sales: 
    if s>max:
        max = s
print(max)                     # 0 : will give Wrong Answer!!

# Right Approach -- ✅
max = sales[0]                 # Solution is Initialize with first Element of array
for s in sales:
    if s>max:
        max = s
print(max)                     # -50

                               # Why initialize with the FIRST element? We use sales[0] 
                               # because it is guaranteed to be an actual value. We could 
                               # technically start with ANY element of the array, but it's 
                               # not necessary may be array will be small.. so it works 
                               # correctly even when ALL values are negative. If we use 0, 
                               # none of the negative values are greater than 0, so max 
                               # incorrectly remains 0.


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Find index of Max sales/ Min Sales
# --------------------------------------------------------------------------------------------
sales = np.array([100,200,300,500, 250,400,500])
max_sales = np.max(sales)

# Normal Method
for i in range(len(sales)):
    if sales[i] == max_sales:
        print("index - ",i)

# Numpy Method
print(np.argmax(sales))        # Drawback --> gives the First index of Max value of Given Array
print(np.argmin(sales))        # Drawback --> gives the First index of Min value of Given Array


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Measure of Central Tendency (Real World Scenario)
# --------------------------------------------------------------------------------------------
# A company's daily sales for 7 days are given below. Calculate the mean and median.
# Then determine which measure better represents a typical sales day when considering
# the unusually large sale. Also calculate the standard deviation. 
#
# Standard deviation is a statistical measure that shows how spread out the numbers 
# in a data set are from their average, or mean

sales = np.array([45000, 47000, 49000, 52000, 50000, 48000, 250000])

mean = np.mean(sales)          # Calculate mean
median = np.median(sales)      # Calculate median
std = np.std(sales)            # Calculate standard deviation

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)

print("Better measure for typical sales:", median) 
                               # The unusually large sale (250000) pulls the mean 
                               # upward. Therefore, the median better represents a 
                               # typical sales day.