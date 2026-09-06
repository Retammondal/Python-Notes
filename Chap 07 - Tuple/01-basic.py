# -----------------------------------------------------------------
# Why We need Tuple?
# -----------------------------------------------------------------
print()
days_list=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday", "Sunday"]
days_list[0]="Hello"     # IT will change the days which we dont want
print(days_list)
print()

days_tuple=("Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday", "Sunday")
# THis tuple can never be changed or edited
# days_tuple[0] = "Helo"      # Not Possible
print(days_tuple)
print()

# -----------------------------------------------------------------
# Tuple Indexing
# -----------------------------------------------------------------
print(f"Getting Tuple data using Index --> ",days_tuple[5])

# -----------------------------------------------------------------
# Tuple Creating
# -----------------------------------------------------------------
#   1. Using ()
tuple1 = (1,52,23,"Retam")
print()

#   2. Tuple Packing
tuple2 = 34,23,"Retam"

print(tuple1)
print(tuple2)
print()
# -----------------------------------------------------------------
# Tuple --Trailing Comma Rule
# -----------------------------------------------------------------
# Single Item Tuple Creation
dataType1 = (30)       # Integer not Tuple
dataType2 = (30,)      # Tuple with 1 Entry

# Empty Tuple Creation
dataType3 = []          # Empty List
dataType4 = ()          # Empty Tuple

print(dataType1,"-->", type(dataType1))
print(dataType2,"-->", type(dataType2))
print(dataType3,"-->", type(dataType3))
print(dataType4,"-->", type(dataType4))
