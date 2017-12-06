f = list(map(int,open("input").read().split()))

print(f)

dic = {}
count = 0
state = "".join(str(x) for x in f)
dic[state] = 1
while True:
    index = f.index(max(f))
    f[index] = 0
    for i in range(index):
        f[(index+i)%len(f)] += 1
    count += 1
    state = "".join(str(x) for x in f)
    if state in dic:
        break
    else:
        dic[state] = 1

print(count)
