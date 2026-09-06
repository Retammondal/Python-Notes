# -----------------------------------------------------------------------
# Dictionary Properties
# -----------------------------------------------------------------------
#   1. Unordered
#   2. Unindexed, indexed with Key
#   3. Mutable -- Inserting and Updation allowed
#   4. Duplicates Keys not allowed
#   5. Key : Value -- Pair

student = {
    "name": "Rahul",
    "age": 22,
    "CGPA": 9.0,
    "marks": [99,98,96,97]      # Can contain list also
}

# Inserting a New Key or, Update existing Key 
student["name"] = "Retam Mondal"
student["grade"] = "A+"

print(student)