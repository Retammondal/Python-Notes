student = {
    "name": "Rahul",
    "age": 22,
    "CGPA": 9.0,
    "marks": [99,98,96,97]      # Can contain list also
}

# print(student["grade"])   --> Error as grade key is not present;

# -----------------------------------------------------------------------
# Mutable Properties
# -----------------------------------------------------------------------
#   1. Safe Get             --> dict.get(key,default) ; default set to None(by default)
#   2. Safe Removal         --> dict.pop(key,default) ; default set to None(by default)
#   3. Update Dictionary    --> dict.update(other_dict)

print(student.get("grade"))                     # Return None
print(student.get("grade", "Not Present"))      # Return "Not Present"
print(student.get("age"))                       # Return value as present

print(student.pop("grade", "Not Present"))
print(student.pop("CGPA"))
print(student)

student.update({"age":16, "grade" : "A+"})
print(student)

# -----------------------------------------------------------------------
# Immutable Properties
# -----------------------------------------------------------------------
#   1. Get All Keys         --> dict.keys()     => Not a list; but iterable
#   2. Get All Items        --> dict.items()    => (key, value) pair as tupple
#   3. Length of Dictionary --> len(dict)       [Give only key-value pair no.]

print()
print(student.keys())
print()
print(student.items())