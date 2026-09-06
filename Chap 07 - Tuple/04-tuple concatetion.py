# -----------------------------------------------------------------------
# Tuple Concatenation
# -----------------------------------------------------------------------
# Add Two Tuple
# We can only add two tuple

tuple1 = (1,2,3,"Retam")
tuple2 = (7,8,"Mondal")

# As we know Tuples are Immutable, we can't change data inside (Add/ Remove)
concated_tuple = tuple1 + tuple2
print(concated_tuple)

# here tuple1, tuple2 are not destroying or changing;
# a new tuple is being created from tuple1 and tuple2

# -----------------------------------------------------------------------
# Tuple Replication
# -----------------------------------------------------------------------
# Will repeat same tuple multiple times and add..
replicated_tuple = tuple1 * 3
print(replicated_tuple)