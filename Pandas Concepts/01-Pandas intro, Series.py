import pandas as pd
import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Introduction to Pandas & DataFrames
# --------------------------------------------------------------------------------------------
# Tabular Data/ Structured Data or, Data is form of Rows and Columns
# Limitation of Numpy : All the data should be of same Datatype; 
# but we have no such restriction in Pandas
#
# Pandas can be used to perform the following:
#   - Organizing data into rows and columns.
#   - Reading data from CSV and Excel files.
#   - Selecting specific rows and columns.
#   - Filtering records based on conditions.
#   - Handling missing values.
#   - Cleaning inconsistent data.
#   - Calculating statistics.
#   - Grouping and summarizing information.
#   - Combining datasets.
#   - Preparing data for visualization and machine learning.

dictionary = {                 # col1: names --> [n1,n2 ..]
    "Name" : ["Amit", "Priya", "Rahul", "Sneha"],
    "Marks" : [85,92,67,78]    # col2: marks --> [m1, m2..]
}

students = pd.DataFrame(dictionary)
                               # pd.DataFrame(dict)
print(students)                # DataFrame is kind of Table formed by Rows 
                               # and Columns


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Pandas Series
# --------------------------------------------------------------------------------------------
# Series --> it's just like a single column. Syntax: pd.Series(python list)
# Dataframe is a combination of multiple column=Series
# Dataframe can be of multiple datatypes, but inside a series it has to be of 
# the same datatype. In Series -- by giving multiple datatypes it will not give 
# Error.. it will be Upcasted.

marks = pd.Series([85,92,64,85,96])
print(marks)

temperatures = pd.Series([30, 32, 31, 29, 35, 34, 33])
                               # Find min,max and avg of temperature

print(temperatures.mean())     # Whatever functions we have learnt in Python can be 
print(temperatures.max())      # use here as well
print(temperatures.min())
print(len(temperatures))

mixedSeries = pd.Series(["Retam", 29, 29.5])
print(mixedSeries)             


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Custom Indices in Series
# --------------------------------------------------------------------------------------------

data = pd.Series(              # Q : Month name -- index and Sales -- series values
    [100,200,500,450],         # --> these are actual datas
    index = ["Jan", "Feb", "Mar", "Apr"]
)
print(data)

print(data["Feb"])             # I want to access data 200

print(temperatures[2])         # IF we dont' give manual index it will 
                               # happened by default index

salePer = (data["Jan"]/sum(data))*100
print(salePer)                 # What % of sales came from Jan?

dic = {                        # Method 2 to do that: make this dictionary 
    "Jan" : 100,               # and then pass in series to get index as keys 
    "Feb" : 200,               # of that dictinary values
    "Mar" : 500,
    "Apr" : 450
}

upd_data = pd.Series(dic)
print(upd_data)


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Pandas and NumPy Interoperability
# --------------------------------------------------------------------------------------------
# All the concepts we learnt in numpy applicable in pandas also.

arr = np.array([10,20,30,40,50])

num = pd.Series(arr)           # Creating a Pandas series from a Numpy array.
print(num)

print(num+5)                   # add 5 to each in num pandas series