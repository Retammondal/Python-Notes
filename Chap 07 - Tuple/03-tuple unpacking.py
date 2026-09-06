grades = (88, 92, 99)

# -----------------------------------------------------------------------
# Tuple Unpacking --> But it should contain same no. left = right
# -----------------------------------------------------------------------

science_grade, physics_grade, math_grade = grades

print(f"\nAll Grades are {grades}\n")

print(f"Science Marks : {science_grade}")
print(f"Physics Marks : {physics_grade}")
print(f"Mathematice Marks : {math_grade}")

# -----------------------------------------------------------------------
# Tuple Unpacking using Index
# -----------------------------------------------------------------------

print()
nameP = ("Retam", "Ram", "Shyam")
my_name = nameP[0]
print(my_name)
print()

# -----------------------------------------------------------------------
# Tuple Unpacking in Function Return
# -----------------------------------------------------------------------

def marks():
    return 95, "Retam", 52.5, "Mondal"          # As we know, writing with comma give in Tuple

print('Function Returning --> ' ,marks())
chem_marks, name_front, bengali_marks, name_last = marks()

print("Full Name will be --> ", name_front + " " + name_last)
print("My Chemistry Marks --> ", chem_marks)
print("My Bengali Marks --> ", bengali_marks)