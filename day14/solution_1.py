def dense_hash(text):
    result = ""
    for i in range(len(text)//16):
        curr = text[i*16]
        for j in range(1,16):
            curr = curr ^ text[i*16 + j]
        result = result + format(curr,'02x')
    return result


rounds = 64
length = 256

total = ""
current = 0
skip = 0
qq = open("input.test").read().strip()
for q in range(128):
    a = []
    for x in range(length):
        a.append(x)

    string = qq + "-" + str(q)
    print(string)
    f = list(map(ord,string))
    for round in range(rounds):
        for x in f:
            if (current+x) > length:
                b = a[current:] + a[:x-(length-current)]
                b.reverse()
                a = b[length-current:] + a[x-(length-current):current] + b[:length-current]
            else:
                b = a[current:(current+x)]
                b.reverse()
                a = a[:current] + b + a[(current+x):]
            current += (skip + x)
            current = current % length
            skip += 1
    print(dense_hash(a))
    dense = dense_hash(a)
    #dense_bin = "{0:128b}".format(int(dense, 16))
    print(dense_bin)
    dense_bin = bin(int(dense,16))[2:].zfill(128)
    print(len(dense_bin))
    total += dense_bin
print(len(total),total.count("1"))
