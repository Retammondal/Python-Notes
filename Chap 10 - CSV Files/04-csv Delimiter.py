# ==================================================
# CSV DELIMITERS AND QUOTING
# ==================================================
# 1. DELIMITER
# Defines which character separates CSV fields.
# Default delimiter is a comma (,).

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(["name", "city"])
    writer.writerow(["Retam", "Kolkata"])

# OUTPUT:
# name;city
# Retam;Kolkata

# --------------------------------------
# 2. READING WITH CUSTOM DELIMITER

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        print(row)

# --------------------------------------
# 3. QUOTING
# Quoting protects fields containing special characters.

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["Retam", "Kolkata, West Bengal"])

# OUTPUT:
# Retam,"Kolkata, West Bengal"


# COMMON QUOTING OPTIONS:
# csv.QUOTE_MINIMAL -> Quotes fields only when necessary.(Default)
# csv.QUOTE_ALL     -> Quotes every field.
# csv.QUOTE_NONE    -> Does not quote fields.
#                       May require escapechar.

# ==================================================
# CSV DELIMITER AND QUOTING - IMPORTANT
# ==================================================

# delimiter=";" separates columns using semicolons.
#
# If a field contains the delimiter itself,
# csv.writer() automatically wraps that field
# in double quotes (default QUOTE_MINIMAL).
#
# Example:
# ["Retam", "Kolkata;West Bengal", 90]
#
# CSV Output:
# Retam;"Kolkata;West Bengal";90
#
# Quotes preserve the semicolon inside the city field.
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["department"] == "IT":
            print(row["name"], row["salary"])