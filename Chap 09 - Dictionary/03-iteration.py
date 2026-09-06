# -----------------------------------------------------------------------
# Keys only -- Default
# -----------------------------------------------------------------------
# Iterate over Dict ~ iterate over Dict.keys()

student = {
    "name": "Rahul",
    "age": 22,
    "CGPA": 9.0,
    "marks": [99,98,96,97]   
}

for i in student:
    print(i)
for i in student.keys():
    print(i)

# -----------------------------------------------------------------------
# Values only 
# -----------------------------------------------------------------------
# METHOD 01 : iterate over Dict.values()
for i in student.values():
    print(i)

# METHOD 02 : iterate over keys 
for i in student.keys():
    print(student[i])

# -----------------------------------------------------------------------
# Items + Tuple Unpacking
# -----------------------------------------------------------------------
# Thourgh Items and Tuple unpacking we can get both key and value pair
print()
for i in student.items():
    print(i)

print()
for i,j in student.items():
    print(i,"+", j)