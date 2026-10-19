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