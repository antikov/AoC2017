f = open("input").read().strip()
sum = 0
i = 0
offset = int(len(f) / 2)
while i < len(f):
    if f[i] == f[int((i + offset) % len(f))]:
        sum += int(f[i])
    i += 1
print (sum)
