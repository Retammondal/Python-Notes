
print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# Given a list of integers, find the largest element without using Python's built-in max() function.

# Input: [12, 45, 7, 89, 34]
# Output: 89
# --------------------------------------------------------------------------------------------

intList = [12, 45, 7, 89, 34]
largest = intList[0]
for num in intList:
    if num > largest:
        largest = num

print("Largest Element:", largest)

print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# Given a list of distinct integers, find the second largest element without sorting the list.

# Input: [10, 45, 20, 78, 34]
# Output: 45
# --------------------------------------------------------------------------------------------
intList = [10, 45, 20, 78, 34]
largest = intList[0]
for num in intList:
    if num > largest:
        largest = num

# largest2nd = intList[0]
# largest2nd = intList[-1]
# Wrong ? if intList = [78,10,23,45,6] --> Ans will be 78

# Initialize with None to avoid accidentally picking 'largest'
largest2nd = None 

# Second pass: find the second maximum
for num in intList:
    if num < largest:
        # If largest2nd is None, this is the first valid number we've checked.
        # Otherwise, check if num is bigger than our currently stored largest2nd.
        if (largest2nd is None) or (num > largest2nd):
            largest2nd = num

print("2nd Largest Element:", largest2nd)

# ------------------------------------------------------------------------------

# Method 2 --> Right Method: 
intList = [78,10,23,48,6]
largest = intList[0]
for num in intList:
    if num > largest:
        largest = num

largest2nd = float('-inf')
for num in intList:
    if (num<largest) and (num>=largest2nd):
        largest2nd = num

print("2nd Largest Element:", largest2nd)

# Mentos Zindaaagi
intList = [78,10,23,48,6]
largest = float('-inf')
largest2nd = float('-inf')

for num in intList:
    if num > largest:
        largest2nd = largest    # before giving new big value previous will be 2nd large
        largest = num           # largest assigned to new one
    elif num > largest2nd:
        largest2nd = num


print("Largest:", largest)
print("2nd Largest:", largest2nd)

print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# Given a list of integers, create a new list containing only unique elements.
# Maintain the original order of elements.

# Input: [10, 20, 10, 30, 20, 40]
# --------------------------------------------------------------------------------------------
# Can't do Tuple Conversion --> b/c it will break the Order

elements = [10, 20, 12, 30, 20, 40]
uniqueEle = []

for num in elements:
    if (num not in uniqueEle):
        uniqueEle.append(num)

print("Main List:", elements)
print("Unique Elements :", uniqueEle)

print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# Move All Zeros to the End

# Given a list of integers, move all zeros to the end of the list
# while maintaining the relative order of the non-zero elements.

# Input: [0, 5, 0, 3, 8, 0, 2]
# --------------------------------------------------------------------------------------------
intList = [0, 5, 0, 3, 8, 0, 2]
numList = []
zeroList = []

for num in intList:
    if (num==0):
        zeroList.append(num)
    else:
        numList.append(num)

updateList = numList + zeroList
print(updateList)

print("----------------------5-----------------------")
# --------------------------------------------------------------------------------------------
# Given a list of numbers, calculate the average and print all elements 
# that are greater than the average.
# (without numpy)

# Input: [10, 20, 30, 40, 50]
# --------------------------------------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]
total = 0
length = len(numbers)

for num in numbers:
    total += num

average = total/length

finalNumbers = []
for num in numbers:
    if num > average:
        finalNumbers.append(num)

print("Average:", average)
print("> than Average:", finalNumbers)

print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# Given a list containing positive, negative and zero values, create two lists:
# Positive numbers
# Negative numbers
# Ignore zero.

# Input:
numbers = [10, -5, 0, 20, -15, 8, -3, 0, 25, -12]
# --------------------------------------------------------------------------------------------
pos_num = []
neg_num = []

for num in numbers:
    if (num>0):
        pos_num.append(num)
    elif (num<0):
        neg_num.append(num)
print("+ num List:", pos_num)
print("- num List:", neg_num)


print("----------------------6-----------------------")
# --------------------------------------------------------------------------------------------
# Given two lists, find the elements that appear in both lists.

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
# --------------------------------------------------------------------------------------------
common_list = []
# for i in list1:
#     for j in list2:
#         if (i==j):
#             common_list.append(i)

for num in list1:
    if num in list2:
        common_list.append(num)
print(common_list)

