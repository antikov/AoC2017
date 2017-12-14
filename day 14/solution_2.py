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

total = []
total.append([0] * 130)
#print(total)
qq = open("input").read().strip()
for q in range(128):
    current = 0
    skip = 0

    a = []
    for x in range(length):
        a.append(x)

    string = qq + "-" + str(q)
    #print(string)
    f = list(map(ord,string))
    end = [17, 31, 73, 47, 23]
    f.extend(end)

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
    #print(dense_hash(a))
    dense = dense_hash(a)
    #dense_bin = "{0:128b}".format(int(dense, 16))
    dense_bin = bin(int(dense,16))[2:].zfill(128)
    #print(len(dense_bin))
    total.append([0] + list(dense_bin) + [0])
#print(total)

total.append([0] * 130)
#print(total)
d = 1
for i in range(1,129):
    for j in range(1,129):
        #print(total[i][j],end = " ")
        if total[i][j] == "1":
            todo = []
            d += 1
            total[i][j] = d
            if total[i][j+1] == "1":
                todo.append((i,j+1))
            if total[i][j-1] == "1":
                todo.append((i,j-1))
            if total[i-1][j] == "1":
                todo.append((i-1,j))
            if total[i+1][j] == "1":
                todo.append((i+1,j))
            while len(todo) > 0:
                #print(todo)

                ii, jj = todo[0]
                #print(ii,jj)
                total[ii][jj] = d
                del todo[0]
                if total[ii][jj+1] == "1":
                    todo.append((ii,jj+1))
                if total[ii][jj-1] == "1":
                    todo.append((ii,jj-1))
                if total[ii-1][jj] == "1":
                    todo.append((ii-1,jj))
                if total[ii+1][jj] == "1":
                    todo.append((ii+1,jj))

    #print("\n")

for i in range(1,9):
    for j in range(1,9):
        print(total[i][j], end = " ")
    print("\n")

print(d-1)
