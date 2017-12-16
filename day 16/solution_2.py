import re
dance = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
f = open("input").read().strip().split(",")
unique = {"abcdefghijklmnop":0}
moves = []
for line in f:
    if line[0] == "s":
        offset = int(line[1:])
        moves.append(("s",offset))
    if line[0] == "x":
        temp = re.match("x(\d+)/(\d+)",line)
        pos1 = int(temp[1])
        pos2 = int(temp[2])
        moves.append(("x",pos1,pos2))
    if line[0] == "p":
        moves.append(("p",line[1],line[3]))
i = 0
rrr = 1000000000
print(len(moves),moves)
while i < rrr:
    for x in moves:
        if x[0] == "s":
            dance = dance[-x[1]:]+dance[:-x[1]]
        if x[0] == "x":
            dance[x[1]], dance[x[2]] = dance[x[2]], dance[x[1]]
        if x[0] == "p":
            pos1 = dance.index(x[1])
            pos2 = dance.index(x[2])
            dance[pos1], dance[pos2] = dance[pos2], dance[pos1]
    i += 1
    string = "".join(dance)
    if string in unique:
        rrr = 1000000000 % (i-unique[string])
        i = 0
        dance = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        print("find cycle!",string,)
        unique = {"abcdefghijklmnop":0}
        print(unique)
    else:
        unique[string] = i

print ("".join(dance))
