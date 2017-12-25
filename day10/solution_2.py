def sparse_hash(text):
    f = list(map(ord,text))
    end = [17, 31, 73, 47, 23]
    f.extend(end)
    rounds = 64
    length = 256
    a = [ i for i in range(length)]
    current = 0
    skip = 0
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
    return a

def dense_hash(text):
    result = ""
    for i in range(len(text)//16):
        curr = text[i*16]
        for j in range(1,16):
            curr = curr ^ text[i*16 + j]
        result = result + format(curr,'02x')
    return result

def knot_hash(text):
    return dense_hash(sparse_hash(text))

f = open("input").read().strip()
print(knot_hash(f))
