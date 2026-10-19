import numpy as np

print("-----------------------1---------------------------")
# -----------------------------------------------------------------------------------------
# Concept : Numpy Upcasting also happens in Arithmetic Operations
# -----------------------------------------------------------------------------------------

a = np.array([1,2,3])
b = np.array([1.5,2.6,3.5])

print(a.dtype)
print(b.dtype)

c = a + b              # [2.5 4.6 6.5]
print(c)
print(c.dtype)

print("-----------------------2---------------------------")
# -----------------------------------------------------------------------------------------
# Concept : Boolean Upcasting in Arithmetic Operation
# -----------------------------------------------------------------------------------------
# We can convert any number to Boolean
# similarly during arithmetic operation if any arithmetic operation performed on Boolean
# Upcasting change the Boolean to 0/1

arr = np.array([0,1,2,3,0,5], dtype=bool)       # Numbers converts to Boolean(True/false)
print("First Time Array ->", arr)

result = arr*1

print("Array Multiplied by 1 ->" ,arr*1)        # Boolean upcasted to 0/1 * 1
print("Array Multiplied by 5 ->" ,arr*5)        # Boolean upcasted to 0/1 * 5

result = result + 5
print(result)

print(result.dtype)