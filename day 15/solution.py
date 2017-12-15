a = 116
b = 299
mask = 2**16 - 1
count = 0
for i in range(5000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while (a & -a) < 4:
        a = (a * 16807) % 2147483647
    while (b & -b) < 8:
        b = (b * 48271) % 2147483647

    if a & mask == b & mask:
        count += 1

print(count)
