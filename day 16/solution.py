import re
dance = list("abcdefghijklmnop")
f = open("input").read().strip().split(",")

for line in f:
    if line[0] == "s":
        offset = int(line[1:])
        dance = dance[-offset:]+dance[:-offset]
    if line[0] == "x":
        temp = re.match("x(\d+)/(\d+)",line)
        pos1 = int(temp[1])
        pos2 = int(temp[2])
        dance[pos1], dance[pos2] = dance[pos2], dance[pos1]
    if line[0] == "p":
        pos1 = dance.index(line[1])
        pos2 = dance.index(line[3])
        dance[pos1], dance[pos2] = dance[pos2], dance[pos1]

print ("".join(dance))
