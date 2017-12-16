f = list(map(int,open("input").read().strip().split(",")))
length = 256
a = [i for i in range(length)]
current = 0
skip = 0
for x in f:
    if (current+x) > length:
        b = a[current:] + a[:x-(length-current)]
        b.reverse()
        a = b[length-current:] + a[x-(length-current):current] + b[:length-current]
    else:
        b = a[current:current+x]
        b.reverse()
        a = a[:current] + b + a[current+x:]
    current += skip + x
    current %= length
    skip += 1

print(a[0]*a[1])
