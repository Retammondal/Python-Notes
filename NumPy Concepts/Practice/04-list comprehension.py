print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Convert Celsius temperatures to Fahrenheit using:(List comprehension)
# F = (9/5) * C + 32
# --------------------------------------------------------------------------------------------
celsius = [0,10,20,30,40]
fahrenheit = [((9/5) * c + 32) for c in celsius]
print(celsius)
print(fahrenheit)

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Convert Names to Uppercase

names = ["amit", "neha", "rahul", "priya"]
# --------------------------------------------------------------------------------------------
upper_names = [text.upper() for text in names]
print(names)
print(upper_names)

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Convert each price to floor value integer.
prices = [100.50, 250.75, 399.99, 120.25]
# --------------------------------------------------------------------------------------------
floor_prices = [int(num) for num in prices]
print(floor_prices)

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Store the squares of the even numbers and ignore the odd numbers.
# 1 - With and without list comprehension.
# --------------------------------------------------------------------------------------------
# Normal Method
sq_num = []
for i in numbers:
    if i%2 == 0:
        sq_num.append(i**2)
print(numbers)
print(sq_num)

# Mentos Zindaagi
sq_num = [i**2 for i in numbers if i%2 == 0]
print(sq_num)

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# Give a 10% discount to products costing at least ₹1,000.
# Keep other prices unchanged.

prices = [500, 1200, 800, 2500, 1500]
# --------------------------------------------------------------------------------------------
update_prices = [price*0.90 if price>=1000 else float(price) for price in prices]
print(update_prices)

print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
salaries = [35000, 50000, 75000, 80000, 95000, 42000, 60000, 120000, 28000, 78000]

# Calculate bonus amounts based on the following rules:
# Salary >= ₹80,000 → 20% bonus
# Salary >= ₹50,000 but below ₹80,000 → 10% bonus
# Salary below ₹50,000 → 5% bonus

# Return a list containing only the bonus amounts.
# --------------------------------------------------------------------------------------------
bonus = [
    salary*0.2 if salary >= 80000
    else salary*0.1 if salary >=50000
    else salary*0.05
    for salary in salaries
]
print(salaries)
print(bonus)

print("----------------------7-----------------------")
# --------------------------------------------------------------------------------------------
# Given two lists, find elements that are present in the first list but not in the second list.

list1 = [10, 20, 30, 40]
list2 = [20, 40, 50]
# --------------------------------------------------------------------------------------------
final = [item for item in list1 if item not in list2]
print(final)


print("----------------------8-----------------------")
# --------------------------------------------------------------------------------------------
# Generate all possible combinations of T-shirt colors and sizes.
# Sample Data:
colors = ["Red", "Blue", "Black", "White"]
sizes = ["S", "M", "L", "XL"]
# --------------------------------------------------------------------------------------------
combinations = [[color,size] for color in colors for size in sizes]
print(combinations)

print("----------------------9-----------------------")
# --------------------------------------------------------------------------------------------
# Generate pairs whose sum is greater than 12.

numbers1 = [1, 2, 3]
numbers2 = [10, 20]
# --------------------------------------------------------------------------------------------
pairs = [[num1,num2] for num1 in numbers1 for num2 in numbers2 if (num1+num2)>12]
print(pairs)

print("----------------------10-----------------------")
# --------------------------------------------------------------------------------------------
# Find pairs of numbers from 1 to 5 where both numbers are different
# and their product is even.
# --------------------------------------------------------------------------------------------
# Without List Comprehension
even_result = []
for num1 in range(1,6):
    for num2 in range(1,6):
        if ((num1*num2)%2==0) and (num1 != num2):
            even_result.append((num1,num2))
print(even_result)

# With List Comprehension
numbers = [1,2,3,4,5]                   # Here also we can use range though
even_result = [(num1,num2) for num1 in numbers for num2 in numbers if ((num1*num2)%2==0) and (num1 != num2)]
odd_result = [(num1,num2) for num1 in numbers for num2 in numbers if (num1*num2)%2!=0]
print(even_result)
print()
print(odd_result)

print("----------------------11-----------------------")
# --------------------------------------------------------------------------------------------
# Extract only vowels from multiple words
words = ["retam","python","analytics"]
# --------------------------------------------------------------------------------------------
vowels = ['a','e','i','o','u']
extracted = [
    letter
    for text in words
    for letter in text
    # if letter in vowels       -- it's also possible
    if letter in "aeiou"
]
# How to remove duplicates
extracted = set(extracted)
print(extracted)


# Normal Method
# In normal method i am able to remove duplicates
extracted = []
for text in words:
    for letter in text:
        if (letter not in extracted) and (letter in vowels):
            extracted.append(letter)
print(extracted)

print("----------------------12-----------------------")
# --------------------------------------------------------------------------------------------
# Each inner list represents the prices of items in one customer's cart.
# Calculate the total for every customer.

carts = [
    [100, 250, 50],
    [500, 200],
    [120, 80, 300, 100]
]
# --------------------------------------------------------------------------------------------
total = [sum(customerCart) for customerCart in carts]
print(total)

print("----------------------13-----------------------")
# --------------------------------------------------------------------------------------------
prices = [500, 1200, 2500, 800, 1500]

# Problem: Apply 18% tax to products priced above ₹1,000
# and 5% tax to other products.
# --------------------------------------------------------------------------------------------
updated_prices = [
    price*1.18
    if price>1000
    else price*1.05
    for price in prices
]
print(updated_prices)

print("----------------------14-----------------------")
# --------------------------------------------------------------------------------------------
# Given employee records, extract the names of employees whose sales are at least ₹50,000.

employees = [
    {"name": "Aman", "sales": 65000},
    {"name": "Riya", "sales": 42000},
    {"name": "Karan", "sales": 80000},
    {"name": "Neha", "sales": 50000}
]
# --------------------------------------------------------------------------------------------
good_employees = [
    employee["name"]
    for employee in employees
    if employee["sales"]>=50000
]
print(good_employees)

print("----------------------15-----------------------")
# --------------------------------------------------------------------------------------------
# Convert full names into lowercase usernames by joining
# the first and last names with a dot.

names = [
    "Aman Sharma",
    "Riya Verma",
    "Karan Patel"
]
# --------------------------------------------------------------------------------------------
updated_name = [".".join(text.lower().split(" ")) for text in names]
print(updated_name)