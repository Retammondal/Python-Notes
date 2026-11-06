# ==================================================
# PYTHON BUILT-IN FUNCTIONS: ZIP()
# ==================================================
# 1. BASICS OF ZIP()
# The zip() function is a built-in utility that pairs elements from multiple 
# iterables (like lists, tuples, or strings) into a single iterator of tuples.
# It pairs the element at index 0 of the first list with index 0 of the 
# second list, and so on.
# Because it returns an Iterator, we must loop through it or convert it 
# to a list to view the values.

a = [1, 2, 3]
b = [7, 8, 9]

zipped = zip(a, b)             # Passing two lists into zip()
print(list(zipped))            # Convert iterator to list to view.
                               # Output: [(1, 7), (2, 8), (3, 9)]


# --------------------------------------------------
# 2. PARALLEL ITERATION (LOOPS)
# In each loop, zip returns a tuple (). We can use the Tuple Unpacking 
# concept to extract those values directly into variables.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
                               # Tuple Unpacking inside the loop
    print(f"{name} scored {score}")


# --------------------------------------------------
# 3. UNZIPPING DATA
# Unzip a zipped object using the * (unpack) operator, which returns the 
# separated elements as tuples.
# Note: An iterator is exhausted after one use. If you try to unzip an 
# already consumed iterator, it throws an error. Re-zip or convert to list first!

zipped = zip(a, b)             # Re-creating the iterator because the first 
                               # one was consumed by list(zipped) above.
c, d = zip(*zipped)            
print(c)                       # Output: (1, 2, 3)


# --------------------------------------------------
# 4. CREATING DICTIONARIES
# Passing a zipped object to dict() instantly maps the first list as keys 
# and the second list as values.

keys = ['name', 'age', 'role']
values = ['Devin', 28, 'Developer']

user_dict = dict(zip(keys, values))
print(user_dict)               # Output: {'name': 'Devin', 'age': 28, 
                               # 'role': 'Developer'}


# --------------------------------------------------
# 5. HANDLING UNEQUAL LISTS
# If you pass iterables of different sizes, zip() defaults to stopping at 
# the shortest sequence, ignoring the remaining elements of the longer sequence.

letters = ['A', 'B', 'C']
numbers = [1, 2]

print(list(zip(letters, numbers)))
                               # Output: [('A', 1), ('B', 2)]  <-- 'C' is dropped

# zip(letters, numbers, strict=True)
                               # PRO TIP: Setting strict=True forces Python 
                               # to raise a ValueError if lengths don't match.