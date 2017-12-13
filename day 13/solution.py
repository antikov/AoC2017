def get_caught(second, depth):
    x = 1
    pos = 0
    for i in range(second):
        pos += x

        if pos == depth:
            x = -1
        if pos == 0:
            x = 1
    if pos == 0:
        return True
    return False

assert get_position(0,0) == 0

import re
f = open("input.test").read().strip().split("\n")

answer = 0
arr = [1000] * 100
for line in f:
    temp = re.match("(\d+): (\d+)",line)
    x1 = int(temp[1])
    x2 = int(temp[2])
    arr[x1] = x2

second = 0
for x in arr:
    print(second,x)
    if get_caught(second, x):
        answer += second * x
    second += 1
print (answer)
