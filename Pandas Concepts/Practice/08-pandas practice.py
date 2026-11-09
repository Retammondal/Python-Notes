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



