# list.sort()       --> Sort the List in the Place (Mutable); Returns None
# sorted(list)      --> Sort the List but don't change Real; Return sorted list
# ------------------------------------------------------------------------------

num_list = [95,65,48,52.5,65.64,82]
str_list = ["ChatGPT", "chatGPT", "Apple", "banana", "aeroplane"]

sorted_num_list = sorted(num_list)      # sort num list
sorted_str_list = sorted(str_list)      # sort string list

print()
print("Sorting But not in place--")
print(sorted_num_list)
print(sorted_str_list)

# NOTE: String sorting Big Alphabets will come before Small Alphabets
print()
print("Real List didn't change --")
print(num_list)
print(str_list)


print()
print("Sorting List in place --")
print(num_list.sort())
print(str_list.sort())
print(num_list)
print(str_list)
