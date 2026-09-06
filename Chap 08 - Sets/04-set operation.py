set1 = {2,3,4,5,6,7}
set2 = {5,6,7,8,9,0}

# -----------------------------------------------------------------------
# Union
# -----------------------------------------------------------------------
# Method 01 --> Using set1 | set2
set_addition01 = set1 | set2
print(set_addition01)

# Method 02 --> Using set1.union(set2)
set_addition02 = set1.union(set2)
print(set_addition02)

# -----------------------------------------------------------------------
# Intersection
# -----------------------------------------------------------------------
# Method 01 --> Using set1 & set2
set_intersection_01 = set1 & set2
print(set_intersection_01)

# Method 02 --> Using set1.intersection(set2)
set_intersection_02 = set1.intersection(set2)
print(set_intersection_02)

# -----------------------------------------------------------------------
# Difference
# -----------------------------------------------------------------------
set1_set2 = set1 - set2
set2_set1 = set2 - set1
print(set1_set2)
print(set2_set1)