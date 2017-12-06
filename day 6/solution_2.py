f = list(map(int,open("input").read().split()))

print(f)

dic = {}
count = 0
state = "-".join(str(x) for x in f)
dic[state] = 0
while True:
    index = f.index(max(f))
    m = max(f)
    f[index] = 0
    for i in range(m):
        f[(index+i+1)%len(f)] += 1
    print (f)
    count += 1
    state = "-".join(str(x) for x in f)
    if state in dic:
        break
    else:
        dic[state] = count

Loopstate = "-".join(str(x) for x in f)

count = 0
while True:
    index = f.index(max(f))
    m = max(f)
    f[index] = 0
    for i in range(m):
        f[(index+i+1)%len(f)] += 1
    print (f)
    count += 1
    state = "-".join(str(x) for x in f)
    if state == Loopstate:
        break
    else:
        dic[state] = 1


count = 0
print(count)
