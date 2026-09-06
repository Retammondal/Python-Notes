
# -----------------------------------------------------------------------
# Tuple += Illusion
# -----------------------------------------------------------------------

print()

tuple1 = (25,26,34,"Retam")
print(tuple1)
# tuple1 += ("Mondal")       # It's not Tuple, it's String; Tuple + String ❌
tuple1 += ("Mondal",)

# it's not changing tuple1; it's actually creating a new tuple (tuple1) and replacing with previous one
print(tuple1)