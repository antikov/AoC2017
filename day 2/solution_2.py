f = open("input").read().strip().split("\n")

sum = 0
for line in f:
    x = line.split("\t")
    x = list(map(int,x))
    i = 0
    while i < len(x):
        j = 0
        while j < len(x):
            if x[i]%x[j] == 0 and i != j:
                sum+= x[i]/x[j]
            j += 1
        i += 1

print(sum)
