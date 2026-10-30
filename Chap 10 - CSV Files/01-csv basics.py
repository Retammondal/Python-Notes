import csv
# CSV : Comma-Separated Values.
# It is a plain-text format used to store tabular data (rows and columns).

# Each line represents one record (row).
# Commas separate fields (columns).
# The first row often contains column headings.
# All CSV data is stored as text.

# Python provides a built-in csv module, so no installation is needed.

# ==================================================
# READING CSV FILES
# ==================================================
# 1. csv.reader() reads CSV rows as lists & returns an iterator.
# 2. Each value is returned as a string.
# 3. next(reader) consumes one row.
#    Calling next() again consumes another row.
# 4. A reader is exhausted after all rows are read.
# 5. next(reader, None) avoids StopIteration
#    if there are no rows remaining.

with open("Chap 10 - CSV Files/students.csv", "r", newline="") as file:
    reading = csv.reader(file)

    header = next(reading)                  # Skip the header
    print("Headers:", header)

    for row in reading:
        print("Data:",row)

# ==================================================
# WRITING CSV FILES
# ==================================================
# 1. writer() creates a CSV writer object.
# 2. writerow() writes a single row.
# 3. writerows() writes multiple rows.
# 4. "w" mode creates or overwrites a file.
# 5. "a" mode appends at last
# 6. newline="" prevents unwanted blank lines.

with open("Chap 10 - CSV Files/students.csv", "w", newline="", encoding="utf-8") as file:
    writing = csv.writer(file)

    writing.writerow(["id", "name", "marks"])
    writing.writerow([1, "Retam", 95])
    writing.writerows([
        [2, "Rahul", 85],
        [3, "Priya", 95],
        [4, "Kashinath", 95],
        [5, "Maya", 95],
    ])

# ==================================================
# APPENDING DATA TO CSV
# ==================================================
# FILE MODES:
# "r" -> Read existing data
# "w" -> Write (overwrites existing data)
# "a" -> Append (preserves existing data)
# Note :  If the file doesn't exist, "a" creates it.

with open("Chap 10 - CSV Files/students.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([6, "Suman", 88])
    writer.writerow([6, "Suman"])                       # Only give first 2 column