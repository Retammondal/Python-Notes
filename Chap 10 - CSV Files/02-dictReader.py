# ==================================================
# CSV DICTREADER()
# ==================================================

import csv

# csv.reader()     -> Returns each row as a list
# csv.DictReader() -> Returns each row as a dictionary

# 1. DictReader uses the first row as dictionary keys.
# 2. Each subsequent row becomes a dictionary.
# 3. Access values using column names instead of indexes.
# 4. Values are strings by default.
# 5. DictReader automatically consumes the header.
# 6. No need to call next(reader) to skip the header.

with open("Chap 10 - CSV Files/students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    next(reader)        # skip the header ❌ skip the first data row

    for row in reader:
        print(row["name"], row["marks"])

# ==================================================
# IMPORTANT: reader() vs DictReader()
# ==================================================

# csv.reader():
# Header is treated as a normal row.
# next(reader) skips the header.

# csv.DictReader():
# Header is automatically used as dictionary keys.
# next(reader) skips the first DATA row.