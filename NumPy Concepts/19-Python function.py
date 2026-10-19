print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Functional Programming (Functions as Values)
# --------------------------------------------------------------------------------------------
# Functional Programming:
# 1. Functions are treated as values.
# 2. Functions can be passed as parameters to other functions.
# 3. Functions can return other Functions.
# 4. Lambda Functions (One liner Functions)
# 5. Filter() -- filtering elements on basis of some criteria
# 6. reduce() -- combine values into single value

def addTwo(num1=5, num2=5):
    return num1+num2

print(addTwo(2,4))

print(addTwo)                  # Calling vs Reference of a Function: This is not 
                               # calling, it's function reference

print(addTwo())                # This is calling

addFunc = addTwo               # addFunc will = addTwo function reference
print(addFunc(10,10))


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Higher Order Functions (HOF)
# --------------------------------------------------------------------------------------------
# Higher Order Functions (HOF):
# 1. Accepts another function as an Argument
# 2. or, returns another function

def square(x):                 # Write a code where one function is used as a 
    return x**2                # parameter to the other function

def cube(x):
    return x**3

def call_func(func, num):
    return func(num)

ans = call_func(cube, 4)
print(ans)

# --------------------------------------------------
def add(a, b):
    return a+b

def mul(a, b):
    return a*b

def operation(callFunc, a, b): # Operation() --> hof. It accepts another function 
    return callFunc(a, b)      # like add(a,b) or mul(a,b)

ans = operation(mul, 4, 5)
print(ans)

ans = operation(add, 10, 5)
print(ans)


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Infinity in Python
# --------------------------------------------------------------------------------------------
# Basic behavior of infinity
# Using the built-in float constructor (case-insensitive)

pos_inf = float("inf")         # inf --> Greater than any Integer or Float
neg_inf = float("-inf")        # -inf --> Smaller than any Integer or Float

print("--- Infinity Comparisons ---")
print("Is -999999 greater than negative infinity?", -999999 > neg_inf)
print("Is  999999 less than positive infinity?", 999999 < pos_inf)
print()


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Using Infinity for Min/Max Algorithms
# --------------------------------------------------------------------------------------------
# Using float('-inf') to find the LARGEST number.
# It works perfectly even if the list contains only negative numbers.

negative_numbers = [-50, -10, -100, -3]

largest = float('-inf')        # Start infinitely small
for num in negative_numbers:
    if num > largest:
        largest = num

print("--- Finding Maximum ---")
print(f"The largest number in {negative_numbers} is: {largest}")
print()

# Using float('inf') to find the SMALLEST number.

prices = [250, 45, 80, 199]

smallest = float('inf')        # Start infinitely large
for price in prices:
    if price < smallest:
        smallest = price

print("--- Finding Minimum ---")
print(f"The smallest price in {prices} is: {smallest}")