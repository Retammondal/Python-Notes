import numpy as np
import pandas as pd

print("----------------------1-----------------------")
# --------------------------------------------------------------------------------------------
# 1. Viewing Data (head & tail)
# --------------------------------------------------------------------------------------------
# DataFrame.head(n=5) --> returns n rows from top of the DataFrame (like LIMIT in SQL)
# If pass -ve values it will give all except the last n rows.
# DataFrame.tail(n=5) --> returns n rows from the bottom of the DataFrame.

np.random.seed(42)             # Sample Data Creation: Set a random seed for 
                               # reproducibility

data = np.random.randint(10, 100, size=(10, 5))
                               # Generate a 10x5 grid of random numbers
np.random.seed(None)           # Setting random reset
columns = ["Column_A", "Column_B", "Column_C", "Column_D", "Column_E"]
                               # Define column names
data = pd.DataFrame(data, columns=columns)
                               # Create the DataFrame

print(data)
print(data.head(6))
print(data.tail(2))


print("----------------------2-----------------------")
# --------------------------------------------------------------------------------------------
# 2. Random Sampling (.sample)
# --------------------------------------------------------------------------------------------
# .sample(n=1) --> Returns random rows from the DataFrame.
# In a real environment, getting the same random sample every time is useful 
# for testing and sharing code. We achieve this using random_state (acts like seed).

print(data.sample())           # To get any random sample example (default n=1). 
                               # Without random_state, it changes every run.

print(data.sample(2, random_state=42))
print(data.sample(2, random_state=42))
                               # Now in companies we want the same sample to work 
                               # on everytime. Both will give the exact same ans 
                               # because random_state is locked to 42.

print(data.sample(2, random_state=30))
                               # You can use any state number, but to get the 
                               # exact same data next time, just reuse that state.