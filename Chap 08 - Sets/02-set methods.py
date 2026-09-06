print()

# -----------------------------------------------------------------------
# Set Mutable Methods
# -----------------------------------------------------------------------
#     1. Add Element --> set.add(x)
#     1. Remove Element --> set.remove(x) / set.discard(x) - no error
#     1. Remove Random Element --> set.pop()
#     1. Clear Entire set --> set.clear()


set1 = {2,5,6,8,"Retam"}
# Add "Mondal" to set1
set1.add("Mondal")
print(set1)

# Remove 6 from set1
set1.remove(6)
print(set1)
# set1.remove(9)      # 9 not present, this will give Error
set1.discard(9)

# remove Random Element
set1.pop()
print(set1)

# Clear entire set
set1.clear()
print(set1)

# -----------------------------------------------------------------------
# Set Immutable Methods
# -----------------------------------------------------------------------
# Length of Set
print(len(set1))