def get_val(a):
    try:
        return int(a)
    except:
        return reg[a]

f = open("input").read().strip().split("\n")
reg = { r:0 for r in list("abcdefgh")}
i = 0
count = 0
while 0 <= i < len(f):
    r,a,b = f[i].split()
    if (r=="set"):
        reg[a] = get_val(b)
    if (r=="sub"):
        reg[a] -= get_val(b)
    if (r=="mul"):
        reg[a] *= get_val(b)
        count += 1
    if (r=="jnz" and get_val(a) != 0):
        i +=get_val(b) - 1
    i += 1
print(count)
