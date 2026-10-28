import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Creating DataFrames (3 Methods)
# --------------------------------------------------------------------------------------------
# pd.DataFrame() creates a tabular data structure from various Python data types.

data = {                                    # Method 1 : From a Dictionary of Lists...  
    'Name': ['Alice', 'Bob', 'Charlie'],    # => key will be column head. Column Oriented  
    'Age': [25, 30, 35],                    # => data defined by col
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

# -------------------------------------------------
data = [                                                # Method 2 : From a List of Dictionaries...  
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},   # => key will be column head. 
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},       # Row Oriented --> data defined by row
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}     
]
df = pd.DataFrame(data)
print(df)

# -------------------------------------------------
data = [                                            # Method 3 : From a List of Lists/Tuples...  
    ['Alice', 25, 'New York'],                      # => Only Row values. Explicitly provide Column head using 
    ['Bob', 30, 'London'],                          # columns argument: pd.DataFrame(data,columns)
    ['Charlie', 35, 'Paris']
]
data = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. DataFrame Attributes & Dimensions
# --------------------------------------------------------------------------------------------
print(data.shape)                       # Shape of DataFrame. tuple = (rows, cols)

row, col = data.shape                   # Get the row and column value how to get?  
print("Data Rows :", row)               # - Tuple Destructuring.
print("Data Columns :", col)            # If you notice it doesn't including the Table Head at all..

print("Data Cells :", data.size)        # Find no of cells in dataframe
                               

if data.shape[0] > 0:                   # Check whethere a dataset has records or not?
    print("Dataset Contains records.")  # (if row > 0)
else:
    print("Dataset is empty.")

empty_data = pd.DataFrame()             # Recreate an Empty Dataframee --> we will not pass any dictionary
print(empty_data)              
print(empty_data.shape)


print("----------------------3-----------------------")
# --------------------------------------------------------------------------------------------
# 3. Column Operations
# --------------------------------------------------------------------------------------------
print(data.columns)                     # Write a code to get all the column names --> data.columns.
print(list(data.columns))               # To convert to Python lists --> list(data.columns)

print("Retam" in data.columns)          # Ques : Check if specific column exist in the dataframe.
print("Name" in data.columns)           # Check with 'in' operator even though data.columns 
                                        # is an index object it will still work

data.columns = ["MyName", "Age", "Living"]
print(data)                             # Change the names of columns by reassigning