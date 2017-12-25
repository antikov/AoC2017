def coord(i,j):
    return str(i)+":"+str(j)

def step(value, current, i, j):
    l = {"L":"D","R":"U","U":"L","D":"R"}
    r = {"L":"U","R":"D","U":"R","D":"L"}
    offset = {"L":(0, -1),"R":(0,1),"U":(-1,0),"D":(1,0)}
    current = r[current] if value =="#" else l[current]
    i += offset[current][0]
    j += offset[current][1]
    return (current, i, j)

f = open("input").read().strip().split("\n")

a = {}
i, j = 0, 0
for line in f:
    j = 0
    for x in line:
        a[coord(i,j)] = x
        j += 1
    i += 1

i, j = 12, 12
current = "U"
burst = 0
for q in range(10000):
    if coord(i,j) not in a:
        a[coord(i,j)] = "."
    old = a[coord(i,j)]
    if a[coord(i,j)] == ".":
        a[coord(i,j)] = "#"
        burst += 1
    else:
        a[coord(i,j)] = "."
    current,i,j = step(old,current,i,j)

print(burst)
