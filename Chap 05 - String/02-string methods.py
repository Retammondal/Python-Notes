# Methods are Immutable
#       --> All these Methods are Applicable on Strings, 
#       --> so if we try to do in any other datatype it will give Error

# --------------------------------------------------
# Immutable Methods
# --------------------------------------------------

string = "RetAm monDal"

print(len(string))                  # Length Find, including spaces

# Case Conversion
print(string.upper())               # Upper case
print(string.lower())               # Lower case
print(string.capitalize())          # Capital case

print()
# -------------------------------------------------------------------
# Find & Replace
# -------------------------------------------------------------------
#   --> Find first occurance
#   --> Find based on Case Sensitivity
text = "Popularity in Python is a popular programming language. Python is used for web development"

# Find
print(text.find("Pop"))
print(text.find("pop"))
print(text.find("Python"))
print()

# Count Occurance
print(text.count("Pop"))            # Count 1 b/c Popular, popular both has diff case..
print(text.count("pop"))
print(text.count("Python"))
print()


# Replace All
print(text.replace("Python","JavaScript"))
print()

# endswith --> Boolean Result
print(text.endswith("development"))     # True
print(text.endswith("develop"))         # False
print()

# Stripping all Spaces from left and right
text2 = " Popularity   in Python  is a popular  programming language."
text2.strip()
print(text2)
print(text2.strip())