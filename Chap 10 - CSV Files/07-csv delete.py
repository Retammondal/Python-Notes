# ==================================================
# DELETING CSV RECORDS
# ==================================================

import csv

# students.csv:
# name,marks
# Retam,90
# Rahul,65
# Priya,95

# TASK: Delete Rahul's record

rows = []

# STEP 1: Read and filter records
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for row in reader:
        if row["name"] != "Rahul":
            rows.append(row)

# STEP 2: Rewrite the file
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

# RESULT:
# name,marks
# Retam,90
# Priya,95


# IMPORTANT:
# 1. CSV has no direct DELETE command.
# 2. Keep records that do not match the target.
# 3. Rewrite the file with the remaining records.
# 4. != means "not equal to".
# 5. Duplicate names may cause multiple deletions.
#    Prefer a unique ID for identifying records.