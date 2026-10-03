

# --------------------------------------------------------------------------------------------
# Iterating Over Arrays (Loops)
# --------------------------------------------------------------------------------------------

for i in range(len(marks_1d)):         # Loops in NumPy Array --> Yes we can iterate over numpy array also...
    if i == len(marks_1d)-1:           # Print all the numbers in a Numpy array separated by a space
        print(marks_1d[i])
    else:
        print(marks_1d[i], end=" ")

for i in marks_1d:                     # Direct iteration
    if i == marks_1d[-1]:              # Concept added: Using marks[-1] for the condition fails if the last number appears twice in the array. 
        print(i)                       # Using enumerate() is a safer Pythonic way: `for idx, val in enumerate(marks_1d):`
    else:
        print(i, end=" ")