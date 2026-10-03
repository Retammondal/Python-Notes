import numpy as np 
# A NumPy array must be homogeneous. 
# What happens if you pass a mixed list like [1, 2.5, "apple", True]?
# It auto converts based on Upcasting

# Hierarchy of Upcasting: Boolean ➔ Integer ➔ Float ➔ String

a = [2,5.6, "Retam", True]      # --> all change to String
b = np.array(a)
print(b)

c = [3,5,6,5.6,2]                # Float> integer --> Upcasting all will convert to float
d = np.array(c)
print(d)