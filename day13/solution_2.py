import re

def get_caught(index, depth):
    if depth == -1:
        return False
    x = depth * 2 - 2
    if index % x == 0:
        return True
    return False

def try_to_pass(delay, firewall):
    index = delay
    for depth in firewall:
        if get_caught(index, depth):
            return False
        index += 1
    return True

f = open("input").read().strip().split("\n")
answer = 0
firewall = [-1] * 100
for line in f:
    temp = re.match("(\d+): (\d+)",line)
    index, depth = int(temp[1]), int(temp[2])
    firewall[index] = depth

delay = 0
while not try_to_pass(delay,firewall):
    delay += 1

print (delay)
