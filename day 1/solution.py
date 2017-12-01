f = open("input").read().strip()
f = f + f[0]
sum = 0
i = 0
while i + 1 < len(x):
    if x[i] == x[i + 1]:
        sum += int(x[i])
    i += 1
print (sum)
