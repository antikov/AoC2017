
def backtrack(l, w, a, c):
    global lll
    global mmm
    if l > lll:
        lll = l
        mmm = w
    elif l == lll:
        mmm = max(mmm, w)

    for i in range(len(a)):
        if a[i][0] == c:
            backtrack(l + 1, w + sum(a[i]), a[:i]+a[i+1:], a[i][1])
        elif a[i][1] == c:
            backtrack(l + 1, w + sum(a[i]), a[:i]+a[i+1:], a[i][0])
    return mmm

f = open("input").read().strip().split("\n")

lll = 0
mmm = 0
arr = []
for line in f:
    a,b=map(int,line.split("/"))
    print(a,b)
    arr.append((a, b))

print(backtrack(0, 0, arr,0))
