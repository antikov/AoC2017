f = open("input").read().strip().split("\n")

sum = 0
for line in f:
    x = line.split("\t")
    x = list(map(int,x))
    sum += max(x) - min(x)

print(sum)
