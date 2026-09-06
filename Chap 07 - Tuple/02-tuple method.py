# Tuple is Immutable
# List Mutable Methods like append, sort, remove will not work

# --------------------------------------------------
# Immutable Methods
# --------------------------------------------------
#   1. len(tuple)
#   2. max(tuple)               --> max value find
#   3. min(tuple)               --> min value find
#   4. tuple.count(data)        --> Count No. of Occurances of data in tuple
#   5. tuple.index(data)        --> Find first index of data

grades = (88, 92, 45, 79, 95, 45, 61)

print("--- Original Tuple ---")
print(f"Grades Tuple: {grades}\n")

# 1. len(tuple) -> Gets total number of items
total_items = len(grades)
print(f"1. Length of tuple: {total_items}")

# 2. max(tuple) -> Finds highest value
highest_grade = max(grades)
print(f"2. Maximum value  : {highest_grade}")

# 3. min(tuple) -> Finds lowest value
lowest_grade = min(grades)
print(f"3. Minimum value  : {lowest_grade}")

# 4. tuple.count(data) -> Counts occurrences of a specific item
count_45 = grades.count(45)
print(f"4. Occurrences of 45: {count_45} times")

# 5. tuple.index(data) -> Finds the FIRST index location of an item
# Even though 45 appears at index 2 and index 5, it returns 2
first_index_45 = grades.index(45)
print(f"5. First index of 45: Position {first_index_45}")
