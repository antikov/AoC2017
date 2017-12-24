def backtrack(a, c):
    mmm = 0
    for i in range(len(a)):
        if a[i][0] == c:
            mmm = max(sum(a[i])+backtrack(a[:i]+a[i+1:], a[i][1]), mmm)
        elif a[i][1] == c:
            mmm = max(sum(a[i])+backtrack(a[:i]+a[i+1:], a[i][0]), mmm)
    return mmm

f = open("input").read().strip().split("\n")

arr = []
for line in f:
    a,b=map(int,line.split("/"))
    print(a,b)
    arr.append((a, b))

print(backtrack(arr,0))
