import pandas as pd

# ==================================================
# PANDAS: DATATYPES AND TYPECASTING
# ==================================================
# 1. WHY DTYPES ARE IMPORTANT
# We cannot apply mathematical operations if the dtype is not numeric.

student_name = "Amit"
age = 20
marks = 87.5
is_placed = True

print(type(student_name))
print(type(age))
print(type(marks))
print(type(is_placed))


# --------------------------------------------------
# 2. THE PROBLEM WITH HIDDEN STRING DATA

sales = pd.DataFrame({
    "ProductID": [101, 102, 103],
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": ["50000", "25000", "18000"],
    "Quantity": ["2", "3", "4"],
    "Rating": [4.8, 3.5, 4.2],
    "QualityCheck": [1, 0, 1]
})
print(sales)                   # It's obvious to say by looking at the print 
                               # that all are numbers, but they may not be!

print(sales.dtypes)            # Solution : Always check datatype before proceeding.
                               # We see Price and Quantity are strings (object).

print(sales["Quantity"].sum()) # Because they are strings, sum() concatenates them. 
                               # Ans: 2+3+4 = 234 ❌ (not 9 ✅)


# --------------------------------------------------
# 3. TYPECASTING USING .astype()
# How to convert the Datatype of a particular column.

sales["Price"] = sales["Price"].astype(int)
sales["Quantity"] = sales["Quantity"].astype(int)

print(sales)
print(sales["Quantity"].sum()) # Now they are integers. Ans : 2+3+4 = 9 ✅


# --------------------------------------------------
# 4. OTHER USEFUL CONVERSIONS

sales["Rating"] = sales["Rating"].astype(int)
print(sales)                   # Convert Float to Int? TypeCasting -- just like 
                               # in numpy, it will be rounded/truncated to int.

sales["ProductID"] = sales["ProductID"].astype(str)
print(sales)                   # Want Product ID converted from int to str?

sales["QualityCheck"] = sales["QualityCheck"].astype(bool)
print(sales)                   # Convert Quality Check from int (1, 0) to Boolean?