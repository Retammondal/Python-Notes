# Python lists --> excellent for storing Collection of Items, 
# but they aren't desinged to do mathematical computation on whole collection
# NumPy --> Numerical Python; built in library by Python to do Mathematical Operations
# Syntax : np.array(Array)

import numpy as np          # It is must..

# --------------------------------------------------------------------------------------------
# PROBLEM : Store 5 student's Marks; add 10 bonus Marks to each ??
# --------------------------------------------------------------------------------------------
marks = [55, 90, 40, 70 ,80]
bonus = 10

# Method 1 -> Using for Loop
updated_marks1 = []
for i in marks:
  updated_marks1.append(i+bonus)

# Method 2 -> Using lambda, map
updated_marks2 = list(map(lambda x:x+bonus, marks))

# Method 3 --> NumPy Array (BEST METHOD)
numpy_marks = np.array(marks)                  # What it does ? it creates a Numpy array from Python list
updated_marks3 = numpy_marks + bonus

print(updated_marks1)
print(updated_marks2)
print(updated_marks3)

# --------------------------------------------------------------------------------------------
# Checking type()
# --------------------------------------------------------------------------------------------
print("Type of List", type(marks))
print("Type of Numpy Array", type(updated_marks3))

print("----------------------------------------------------------");
# --------------------------------------------------------------------------------------------
# Python List <--> Numpy Array
# --------------------------------------------------------------------------------------------

name = ["Retam", "Ram", "Shyam"]
NumpyName = np.array(name)                      # Converting Python Array --> NumPY Array
print("Numpy Array -->", NumpyName)
print("Python List -->", NumpyName.tolist())    # Converting NumPY Array --> Python List