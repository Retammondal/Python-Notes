# -------------------------------------------------------------------
#   Immutable Methods
# -------------------------------------------------------------------
# Don't change Main List, Returns a new list
#   1. Length of list
#   2. Max of given list    --> Numbers Input only
#   3. Min of given list    --> Numbers Input only
#   4. Sum of given list    --> Numbers Input only

list1 = ["Retam", True, None, 45,46,46.9]
print(len(list1))
# print(max(list1))     -- Error

num_list = [45,46.9,52,63.49,63.53]
max_num_list = max(num_list)
min_num_list = min(num_list)
sum_num_list = sum(num_list)

print("\n")
print(f"Talking Of Given list\n{num_list}")
print(f"Sum --> {sum_num_list}")
print(f"Max --> {max_num_list}")
print(f"Min --> {min_num_list}")

print("\n")

# -------------------------------------------------------------------
#   Mutable Methods
# -------------------------------------------------------------------
# Change Main List
#   1. Adding New Data at end (Only 1 at a time) --> list.append(data)
num_list.append("Retam")
print(num_list)
num_list.append(52)
print(num_list)

#   2. Removing First Occurance only --> list.remove(data)
num_list.remove("Retam")
print(num_list)

#   3. Sort List --> list.sort()                    
num_list.sort()     
print(num_list)

#   4. Reverse List --> list.reverse()              
num_list.reverse()     
print(num_list)

#   5. Insert at an Index --> list.insert(index, data)            
num_list.insert(4, 50)
print(num_list)

#   6. Remove from an Index --> list.pop(index)          
num_list.pop(3)
print(num_list)    

