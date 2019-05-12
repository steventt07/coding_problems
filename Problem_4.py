def lowest(vec):
    max_num = max(vec)
    lowest = 1
    data = {k: 0 for k in range(1,max_num+2)}
    for x in vec:
        if data.get(x) != None:
            data[x] = 1
        if lowest == x:
            while(data[lowest] == 1):
                lowest += 1
    return lowest


vec = [3, 4, -1, 1]
vec1 = [1, 2, 0]
print(lowest(vec1))
