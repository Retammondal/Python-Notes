import numpy as np
import pandas as pd

students = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Maths": [80, np.nan, 70, 90, np.nan],
    "Science": [np.nan, 75, 85, 90, 80],
    "English": [70, 80, np.nan, 95, 85]
})

# Questions :
# Display the dataset.
# Find the missing-value positions.
# Count missing values in each subject.
# Count all missing cells.
# Calculate missing percentages.
# Display only students whose Maths marks are missing.

print(students)
print(students.isnull())
print(students.isnull().sum())
missing_perc = students.isnull().sum().sum() * 100 / students.size
print(missing_perc)
print(students[students["Maths"].isnull()])

# -----------------------------------------------------------------------
import numpy as np
import pandas as pd


df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Branch": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Marks": [90, 85, 80, 95, 85]
})

# Quest : Sort it on base of Branch then break the tie on basis of lower marks first
df_sort = df.sort_values(by=["Branch","Marks"])
print(df_sort)
# Quest : Same but Branch Alphabetically; Marks High to Low within each branch
# Branch alphabetically - ascending, marks high to low - descending
df_sort = df.sort_values(by=["Branch","Marks"], ascending=[True,False])
print(df_sort)

# ================================================================================
data = pd.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "marks":   [88,      95,    91,        95,      84,    91],
    "bonus":   [2,       1,     5,         4,       3,     2]
})

# Question : Least Scoring 3 Students without using nsmallest
# Method 1 :
data_sort = data.sort_values(by="marks")
print(data_sort)
print(data_sort.head(3))

# Method 2 :
data_small = data.nsmallest(3, columns="marks")
print(data_small)

# ================================================================================
employees = pd.DataFrame({
    "Name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Salary": [50000, 70000, 70000, 60000, 80000],
    "Experience": [2, 3, 5, 4, 2]
})

# Question : Top 3 employees based on salary and experience (First on Salary --> then on Experience)
top_employees = employees.nlargest(3,columns=["Salary","Experience"])
print(top_employees)


# ================================================================================
print("----------------------5---------------------------")
df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Marks": [85, 95, 75, 90, 80]
})

# Ques : Sort them on basis of marks
df_sort = df.sort_values(by="Marks")
print(df_sort)

# Ques : Dont change the order just give the rank based on Marks
df["Rank"] = df["Marks"].rank()                     # Will give rank ascending (lowest -> highest)
df["Rank"] = df["Marks"].rank(ascending=False)      # Now give (Highest -> Lowest)
print(df)

# ================================================================================
print("----------------------6---------------------------")
df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Marks": [90, 95, 90, 85, 80]
})

# Ques : Perform Ranking on this data where Marks are same?
df["Avg Rank"] = df["Marks"].rank()
# Method Average (Default) => if rank is coming 2,3 --> asign both 2.5

df["Min Rank"] = df["Marks"].rank(method='min')
# Method Min => min position will given to all + skip the rest position

df["Max Rank"] = df["Marks"].rank(method='max')
# Method Max => max position will given to all + skip the rest position

df["First Rank"] = df["Marks"].rank(method='first')
# Method First => If tied gives rank based on First Appearance

df["Dense Rank"] = df["Marks"].rank(method="dense")
# Method Dense => Assign both same rank + start next rank from next
print(df)