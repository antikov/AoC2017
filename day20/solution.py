import re
import math
f = open("input").read().strip().split("\n")

i = 0
p = []
v = []
a = []
d = [0] * 1000
for line in f:
    #p=<2290,257,-3040>, v=<41,119,57>, a=<-10,-10,5>
    print(line)
    temp = re.match(r"^p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$",line)
    print(temp)
    p.append((int(temp[1]),int(temp[2]),int(temp[3])))
    v.append((int(temp[4]),int(temp[5]),int(temp[6])))
    a.append((int(temp[7]),int(temp[8]),int(temp[9])))
    print(p[i],v[i],a[i])
    i += 1

repeats = 1000
for step in range(repeats):
    for i in range(len(p)):
        v[i] = (v[i][0] + a[i][0],v[i][1] + a[i][1],v[i][2] + a[i][2])
        p[i] = (p[i][0] + v[i][0],p[i][1] + v[i][1],p[i][2] + v[i][2])
        d[i] += abs(p[i][0])+abs(p[i][1])+abs(p[i][2])

x = min(d)
x = d.index(x)
print(x)
