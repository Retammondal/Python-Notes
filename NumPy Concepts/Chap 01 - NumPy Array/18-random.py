import numpy as np

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Random Integers
# --------------------------------------------------------------------------------------------
# Syntax : np.random.randint(low, high, size)
# low is inclusive, high is exclusive. size can be an int (1D) or tuple (2D/3D).

marks = np.random.randint(0, 101, 10)
print(marks)                   # Generate 10 random integers from 0 to 100

print(np.random.randint(10,20,(3,4))) 
                               # Mentos method: Create a 3x4 integer matrix 
                               # directly using a tuple for the size.


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Random Floats (random, rand, uniform)
# --------------------------------------------------------------------------------------------
# np.random.random()  --> Generates random floats in half-open interval [0.0, 1.0)
# np.random.rand()    --> Same as random(), but takes individual dimensions as arguments 
#                         instead of a tuple.
# np.random.uniform() --> Generates random floats in a specific custom range [low, high)

print(np.random.random(5))     # 1D array of 5 floats between [0, 1)

# Question : Generate a 3x4 random matrix (using reshape)

print(np.random.random(12).reshape(3,4))              
print(np.random.random((3,4))) # Generate a 3x4 matrix directly (requires tuple)
print(np.random.rand(3,4))     # Generate a 3x4 matrix directly (multiple arguments)

print(np.random.uniform(20,30,5))
                               # 1D array of 5 floats between [20, 30)

print(np.random.uniform(10,20,(3,4)))
                               # Mentos method: 3x4 float matrix between 10 and 20

# Note : It utilizes Probability Concept
# Question : Generate 20 random probability values and find their min, max, avg and percentage > 0.5
random_prob = np.random.random(20)
print(np.min(random_prob))
print(np.max(random_prob))
print(np.mean(random_prob))

high_prob = random_prob[random_prob > 0.5]
perc = (len(high_prob)/20)*100 
print(perc)                    


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 5. Random Choice (With vs Without Replacement)
# --------------------------------------------------------------------------------------------
# WITH REPLACEMENT: Drawing a card, writing it down, and PUTTING IT BACK. 
# (Duplicates allowed). np.random.randint inherently works WITH replacement.
#
# WITHOUT REPLACEMENT: Drawing a card and KEEPING it in your hand. 
# (Unique Values Only). You must use np.random.choice() and set replace=False.

with_repl = np.random.randint(1, 11, size=6)
print(with_repl)               # Might contain duplicates (e.g. 4 appears twice)

without_repl = np.random.choice(np.arange(1, 11), size=6, replace=False)
print(without_repl)            # Output will NEVER contain duplicates.

                               # Warning check: np.random.choice(pool, size=15, 
                               # replace=False) -> ERROR! If you pull 15 numbers 
                               # from a pool of 10, the bag empties!

colors = np.array(["Red", "Blue", "Green", "White"])

print(np.random.choice(colors))
                               # Picks 1 random color

print(np.random.choice(colors, 3)) 
                               # Picks 3 random colors (with replacement)

print(np.random.choice(colors, 2, replace=False))
                               # Picks 2 unique random colors

students = np.array(["Amit", "Riya", "Karan", "Neha", "Rahul", "Sneha"])

selected_students = np.random.choice(students, 3, replace=False)
print(selected_students)       # What's the usecase of without Replacement?
                               # To select 3 distinct students to distribute 
                               # sweets (cannot select the same student twice).


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. The Concept of 'Seed'
# --------------------------------------------------------------------------------------------
# Computers generate "pseudo-random" numbers using mathematical formulas.
# By setting a specific seed, you lock the starting point, meaning the sequence of 
# random numbers generated will always be exactly the same.
# This is crucial for reproducibility (sharing code, debugging, testing models).
print("Seeded with Choice 42")

np.random.seed(42)             # '42' is a common arbitrary choice, but any int works.

print(np.random.randint(1, 11, 4))
                               # First pull: Because the seed is locked to 42, this 
                               # will ALWAYS output: [ 7  4 10  8]

print(np.random.randint(1, 11, 4))
                               # Second pull: The internal engine moves forward to the 
                               # next numbers. ALWAYS outputs: [ 5  7 10  3]

np.random.seed(42)             
print(np.random.randint(1, 11, 4))
                               # Reset pull: If we reset the seed back to 42, the 
                               # sequence starts from the beginning! [ 7  4 10  8]

print(np.random.choice(students, 2, False))

# How to stop this Seeding?
np.random.seed(None)

