import reduce
vec = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x * y, vec, 1)
for x in range(len(vec)):
    vec[x] = total/vec[x]
print(vec)