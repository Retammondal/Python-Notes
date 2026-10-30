# ==================================================
# CSV DICTWRITER()
# ==================================================
# DictWriter() writes dictionaries as CSV rows.
# fieldnames defines the column names and their order.

import csv

with open("Chap 10 - CSV Files/students02.csv", "w", newline="", encoding="utf-8") as file:
    writing = csv.DictWriter(
        file,
        fieldnames = ["name", "age", "marks"]
    )
    writing.writeheader()               # Giving Fieldnames as Headers
    writing.writerow({"name" : "Retam", "marks" : 85})          # age cell will be empty
    writing.writerows([
        {"name": "Rahul", "age": 22, "marks": 85},
        {"name": "Priya", "age": 20, "marks": 95}
    ])

with open("Chap 10 - CSV Files/students02.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["age"])


# ==================================================
# DICTWRITER OPTIONS
# ==================================================
# 1. extrasaction="raise" (default) causes ValueError.
#    extrasaction="ignore"
#    Ignores dictionary keys not listed in fieldnames.

# 2. restval="" (empty field) (default).
#    restval="N/A"
#    Fills missing dictionary keys with a default value.

with open("Chap 10 - CSV Files/students02.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "marks"],
        extrasaction="ignore",
        restval="0"
    )
    writer.writeheader()
    writer.writerows([
        {"name": "Retam", "marks": 90, "age": 21},          # age will auto cancels
        {"name": "Rahul"},                                  # marks given to 0
        {"name": "Priya", "marks": 95}
    ])
with open("Chap 10 - CSV Files/students02.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)