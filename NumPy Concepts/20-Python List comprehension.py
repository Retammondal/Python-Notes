print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Basic List Comprehension
# --------------------------------------------------------------------------------------------
# List comprehension in Python is a concise, elegant way to create a new list 
# from an existing iterable (like a list, tuple, or range). It replaces traditional 
# for loops, making your code shorter, cleaner, and faster.
# Syntax : new_list = [expression for item in iterable]

numbers = [1,2,3,4,5]
print(numbers)

sq = []                        # Question : Find square of all numbers
for i in numbers:              # Normal Zindaagi
    sq.append(i**2)
print(sq)

sq = [elem**2 for elem in numbers] 
                               # Mentos Zindaagi -- List Comprehension
                               # {do this} for {every element} in {array}
print(sq)

mul = [elem*5 for elem in numbers]
print(mul)                     # Question : Given a list of integers, store the 
                               # 5 times multiplied number of it (List comprehe.)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Conditional List Comprehension (if)
# --------------------------------------------------------------------------------------------
# new_list = [expression for item in iterable if condition]

numbers = [1,2,3,4,5,6,7,8]

even_num = [num for num in numbers if num%2==0]
print(even_num)                # Question : Create a list with even numbers

words = ["cat", "elephant", "dog", "giraffe", "ant"]

list_word = [(w, w[0]) for w in words if len(w)>=5]
print(list_word)               # Create a list of only those words which are of 
                               # at least length 5, and extract their 1st letter.


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Conditional Expression (if-else)
# --------------------------------------------------------------------------------------------
# new_list = [(expression_if_true) if (condition) else (expression_if_false) 
#             for item in iterable]

numbers = [1,2,3,4,5,6,7,8]

even_odd = ["Even" if item%2 == 0 else "Odd" for item in numbers]
print(even_odd)                # Create a new List categorizing as "Even" or "Odd"


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Nested Conditional Expressions (Simulating elif)
# --------------------------------------------------------------------------------------------
# We can use nested conditional expressions when there are three categories:
# Marks >= 80 → "Distinction"
# Marks >= 40 → "Pass"
# Otherwise → "Fail"

marks = [95, 72, 38, 81, 45, 29]

# Type 1 -->
categories = ["Distinction" if mark>=80 else ("Pass" if mark>=40 else "Fail") for mark in marks]
print(categories)

# Type 2 -->
categories = [                 # Note : Here 'elif' will not work, but we can write 
    "Distinction" if mark >= 80# it without brackets spanning multiple lines
    else "Pass" if mark >= 40  # -> acts exactly like elif
    else "Fail"
    for mark in marks
]
print(categories)

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Nested List Comprehension
# --------------------------------------------------------------------------------------------
# Multiple for loops inside a single bracket notation; Evaluated Left --> Right.
# Syntax : pairs = [(x, y) for x in [List1] for y in [List2]]

# -----------------------------------------------------
# Question : Give all the possible pairs out of these?
numbers1 = [1,2,3]
numbers2 = [10,20]

pair = []                      
for i in numbers1:             # Aam Zindagii
    for j in numbers2:
        pair.append((i,j))
print(pair)

pair = [(item1,item2) for item2 in numbers2 for item1 in numbers1]
print(pair)                    # Mentos Zindagi : How to do it with List Comprehension?

# -----------------------------------------------------
# Question : Make it flattern with use of list comprehension ?
# Extract only passing marks from every row >= 75
# and increase by 5 if they passed?
marks = [                      
    [75, 80, 90],              
    [60, 85, 70],
    [95, 88, 92]
]

flat_marks = []                # Normal Method
for row in marks:
    for elem in row:
        flat_marks.append(elem)
print(flat_marks)

flat_marks = [                 # Mentos ZIndaagi
    elem 
    for row in marks 
    for elem in row
]
print(flat_marks)              # Always remember list comprehension will go 
                               # from left -> right

pass_marks = [elem for row in marks for elem in row if elem>=75]
pass_increased_marks = [elem+5 for row in marks for elem in row if elem>=75]

print(pass_marks)              
print(pass_increased_marks)    