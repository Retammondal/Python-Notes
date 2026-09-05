# Slicing
# Syntax --> list_name[start : stop : step]
# - `start` (Inclusive): Where the slice begins (defaults to `0`).
# - `stop` (Exclusive): Where the slice ends. It extracts up to, but **does not include**, this index.
# - `step`: The jump size between items (defaults to `1`).

num_list = [10, 20, 30, 40, 50, 60, 70, 80]
print()
print(num_list[:])          # Start and Stop both not given --> default to start to end
print(num_list[2:])         # End not given --> default to end
print(num_list[:4])         # Start not given --> default to start
print()

# Negative Indexing
print(num_list[-6:-2])
print(num_list[-6:])
print(num_list[:-2])

# Giving Custom Step (Defaults to 1)
print()
print(num_list[::2])
print(num_list[-6::2])

# -----------------------------------------------------------------
# Reversing a List
# -----------------------------------------------------------------
print()

print(num_list[::-1])
print(num_list[2:8:-1])         # will give zero datas in list
print(num_list[8:2:-1])
