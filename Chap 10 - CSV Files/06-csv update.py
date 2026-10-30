# ==================================================
# LESSON 10: UPDATING CSV RECORDS
# ==================================================
# IMPORTANT:
# 1. CSV has no direct UPDATE command.
# 2. Read records into memory.
# 3. Modify the matching dictionary.
# 4. Rewrite the file using DictWriter().
# 5. "w" overwrites the previous file content.
# 6. writeheader() restores the column headings.
# 7. For large or critical files, use a temporary
#    file and safely replace the original.

import csv

# students.csv:
# name,marks
# Retam,90
# Rahul,65
# Priya,95

# TASK: Update Rahul's marks from 65 to 85.

rows = []

# STEP 1: Read all records
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for row in reader:
        if row["name"] == "Rahul":
            row["marks"] = "85"

        rows.append(row)

# STEP 2: Rewrite the CSV file
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

# RESULT:
# name,marks
# Retam,90
# Rahul,85
# Priya,95


