def get_caught(second, depth):
    if depth == -1:
        return False
    x = depth * 2 - 2
    if second % x == 0:
        return True
    return False

assert get_caught(6,4) == True

import re
f = open("input").read().strip().split("\n")

answer = 0
arr = [-1] * 100
for line in f:
    temp = re.match("(\d+): (\d+)",line)
    x1 = int(temp[1])
    x2 = int(temp[2])
    arr[x1] = x2

initial = 0

while True:
    caught = False
    answer = 0
    second = initial
    for x in arr:
        if get_caught(second, x):
            caught = True
            break
        second += 1
    if not caught:
        print(initial)
        break
    initial += 1
