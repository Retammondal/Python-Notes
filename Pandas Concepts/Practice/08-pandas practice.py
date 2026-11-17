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

