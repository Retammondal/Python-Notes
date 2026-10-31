import numpy as np
import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Reading Data from CSV (pd.read_csv)
# --------------------------------------------------------------------------------------------

csv_data = """Student,Age,Marks,Branch
Amit,18,85,CSE
Priya,19,92,ECE
Rahul,18,76,IT
Sneha,20,88,CSE
Karan,19,67,ME
"""

with open("student.csv", "w") as file:
    file.write(csv_data)       # Creating a new file and writing the csv data to it

df = pd.read_csv("student.csv")
print(df)                      # Have loaded the existing datafile to pandas 
                               # rather than creating


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. DataFrame Properties & Info Summary
# --------------------------------------------------------------------------------------------

print(df.shape)                # Get the properties
print(df.columns)
print(list(df.columns))

print("-----------------------------------")

print(df.info())               # Beautiful Function --> The pandas.info() method 
                               # prints a concise summary of a DataFrame


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Extracting Series from DataFrame
# --------------------------------------------------------------------------------------------
# How to get each column from a Pandas Dataframe --> in form of Series
# Syntax: dataframe["Column Name"]

print(df["Student"])           

print(df["Marks"].mean())      # Find the min, max and avg marks.
print(df["Marks"].max())       # After getting series from Dataframe we can apply 
print(df["Marks"].min())       # Series Methods and properties


print("----------------------4-----------------------")
# --------------------------------------------------------------------------------------------
# 4. Advanced read_csv() Parameters Cheat Sheet
# --------------------------------------------------------------------------------------------
# PANDAS read_csv() 
# ====================================================================
# Quick Reference:
# 1. sep=';' or '\t'            -> Custom delimiter (; or tab)
# 2. header=None                -> File has no header row
# 3. names=['Col1', 'Col2']     -> Assign column names manually
# 4. index_col='id'             -> Set column as row index/labels
# 5. usecols=['Age', 'Salary']  -> Load specific columns only (saves RAM)
# 6. nrows=100                  -> Read first N rows only (fast testing)
# 7. parse_dates=['timestamp']  -> Convert text column to datetime
# 8. na_values=['missing', 'N/A']-> Convert custom text into NaN
# ====================================================================

# STEP 1: Create a dummy CSV file ("sample_data.csv")
# - Uses ';' delimiter
# - Has NO header row
# - Includes 'missing' and 'N/A' strings

raw_csv_data = """101;Alice;29;75000;2026-01-15 08:30:00;HR
102;Bob;missing;82000;2026-02-20 09:15:00;IT
103;Charlie;35;N/A;2026-03-10 14:45:00;Finance
104;Diana;28;68000;2026-04-05 11:00:00;Marketing
105;Evan;42;95000;2026-05-12 16:20:00;IT
106;Fiona;31;missing;2026-06-18 10:05:00;HR
"""
with open("sample_data.csv", "w") as file:
    file.write(raw_csv_data)


# STEP 2: Apply Cheat Sheet Parameters Together

dataframe = pd.read_csv(
    "sample_data.csv",
    sep=";",                                     # 1. Custom Delimiters: semicolon-separated
    header=None,                                 # 2. No Header Row: prevents 1st row becoming headers
    names=["id", "Name", "Age", "Salary", "timestamp", "Dept"],  # 3. Custom Headers: manual column names
    index_col="id",                              # 4. Set Index Column: 'id' becomes row labels
    usecols=["id", "Age", "Salary", "timestamp"],  # 5. Select Columns: skips 'Name' & 'Dept' to save RAM
    nrows=4,                                     # 6. Limit Rows: reads only first 4 rows
    skiprows = 2,                                # skips first two rows..not the header you given just..
    parse_dates=["timestamp"],                   # 7. Parse Dates: converts 'timestamp' to datetime64
    na_values=["missing", "N/A"],                  # 8. Missing Values: converts 'missing' & 'N/A' to NaN
)
dataframe.index.name = None    # Removing id name

print("--- Resulting DataFrame ---")
print(dataframe)

print("\n--- Column Data Types ---")
print(dataframe.dtypes)

salary_series = dataframe["Salary"]
                               # Only load the salary 
print(salary_series)
print(salary_series.mean())    # avg salary