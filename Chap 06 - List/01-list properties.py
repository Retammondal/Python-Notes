# -------------------------------------------------------------------
#   List Properties
# -------------------------------------------------------------------
#       1. Mutable
#       2. Zero-based Indexing + Negative Indexing
#       3. Can Contain Mixed Datatypes

mixed_list = [
    "Hello",                             # String (str)
    42,                                  # Integer (int)
    3.14,                                # Floating-point number (float)
    True,                                # Boolean (bool)
    None,                                # NoneType (represents absence of value),                           # List (list)
    (4, 5, 6),                           # Tuple (tuple)
    {"name": "Alice", "age": 25},        # Dictionary (dict)
    {7, 8, 9},                           # Set (set)
    [7,8,9]                              # List
]

# -------------------------------------------------------------------
#   Indexing + Mutability
# -------------------------------------------------------------------
print()
print(mixed_list[3])
print(mixed_list[-2])           # List inside List

# Nested Indexingg
print(mixed_list[-1][0])        # Getting 1st item of inside list of mixed list
print()

# Changing Boolean value from True to False
mixed_list[3] = False
print(mixed_list)