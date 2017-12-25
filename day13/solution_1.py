import re

def get_caught(index, depth):
    if depth == -1:
        return False
    x = depth * 2 - 2
    if index % x == 0:
        return True
    return False

f = open("input").read().strip().split("\n")
answer = 0
firewall = [-1] * 100
for line in f:
    temp = re.match("(\d+): (\d+)",line)
    index, depth = int(temp[1]), int(temp[2])
    firewall[index] = depth

index = 0
for depth in firewall:
    if get_caught(index, depth):
        answer += index * depth
    index += 1
print (answer)
