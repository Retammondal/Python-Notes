# ==================================================
# FILTERING CSV RECORDS
# ==================================================

import csv

# students.csv:
# name,age,marks
# Retam,21,90
# Rahul,22,65
# Priya,20,95
# Amit,23,70

# TASK: Display students with marks >= 80

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["marks"]) >= 80:
            print(row["name"], row["marks"])

# OUTPUT:
# Retam 90
# Priya 95

# IMPORTANT:
# 1. DictReader returns dictionaries.
# 2. CSV values are strings by default.
# 3. Convert numeric values using int() or float().
# 4. Filtering does not modify the original CSV file.