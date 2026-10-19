numbers1 = [1,2,3]
numbers2 = [10,20]
# give all the possible pairs out of these

pair = []
for i in numbers1:
    for j in numbers2:
        pair.append((i,j))
print(pair)

# HOw to do it with List comprehension?
pair = [(item1,item2) for item2 in numbers2 for item1 in numbers1]
print(pair)