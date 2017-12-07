def getHash(array):
    return "-".join(str(x) for x in array)

f = list(map(int,open("input").read().split()))

dic = {}
count = 0
state = getHash(f)

while state not in dic:
    dic[state] = count
    count += 1
    m = max(f)
    index = f.index(m)
    f[index] = 0
    for i in range(m):
        f[(index+i+1)%len(f)] += 1
    state = getHash(f)

print("First answer",count)
print("Second answer",count - dic[state])
