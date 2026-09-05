# ==========================================
# String Writing
# ==========================================
a = 'harry'         # Single quoted string
b = "harry"         # Double quoted string
c = '''harry'''     # Triple quoted string

# ==========================================
# Empty String vs Spaces
# ==========================================
name1 = ""             # It's an Empty String
name2 = " "            # It's not an empty string , it has space as element
print(len(name1))
print(len(name2))

print()
# ==========================================
# String Repetition
# ==========================================
string = "Retam"
print(string*20)

print()
# ==========================================
# String Slicing & Indexing
# ==========================================
# Strings are Indexed ==> Zero Indexed & Negative Indexed
name = "Retam Mondal"
print()

# Slicing
# string[start : stop : step]       Start Included, Stop Excluded
print(name[2 : 5])
print(name[5 : 10])
print(name[2 : 10 : 2])
print(name[-10 : -2])

# Reverse Print
# print(name[-2 : -10])             # Not Possible 
# print(name[10 : 2])               # Not Possible
print(name[10 : 2 : -1])
print(name[-2 : -10 : -1])

print()

# ==========================================
# String Immutability
# ==========================================
# We can't change change any character just like list..b/c Strings are Immutable
print(name[4])
# name[4] = "s"                     # Not Possible
print(name[6])