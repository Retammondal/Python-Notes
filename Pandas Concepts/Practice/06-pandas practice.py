import pandas as pd

print("#########################################################\n")
products = pd.DataFrame({
"Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
"Category": ["Electronics", "Accessories", "Accessories",
"Electronics", "Accessories"],
"Price": [55000, 700, 1500, 12000, 2500],
"Stock": [10, 100, 50, 15, 25]
})

print(products)

print("==========================================================")
# Q1 : Products costing < 2000 and fewer than 20 units
condition = (products["Price"]<3000) & (products["Stock"]<60)
result = products[condition]
print(result)

# Q2 : Create a new column with the total inventory amount for each product
products["Total Amount"] = products["Price"] * products["Stock"]
print(products)

# Q3 : What is the % contribution of each product to the overall inventory amount?
total_inventory_amount = products["Total Amount"].sum()         
products["% Contr."] = (products["Total Amount"]*100/total_inventory_amount).round(2)
print(products)

# Q4 : Select product and stock columns for low-stock products (<20 stock)
filter_products = products[products["Stock"]<20]
print(filter_products[["Product", "Stock"]])
# OR,
filter_products = products.loc[products["Stock"]<20, ["Product", "Stock"]]
print(filter_products)

print("#########################################################\n")
import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Printer"],
    "Quantity": [5, 20, 4, 10, 3],
    "Unit_Price": [50000, 800, 12000, 1500, 18000],
    "Cost": [220000, 10000, 40000, 10000, 45000]
})

print(sales)

print("==========================================================")
# Q1 : Calculate revenue and profit for each product.
# then classify products as High Profit if profit>=9000; otherwise Standard Profit
sales["Revenue"] = sales["Quantity"] * sales["Unit_Price"]
sales["Profit"] = sales["Revenue"] - sales["Cost"]
condition = sales["Profit"]>=9000
sales["Classify"] = np.where(condition, "High Profit", "Standard Profit")

print(sales)

# Q2 : 