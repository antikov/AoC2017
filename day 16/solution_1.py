import re

def get_dance(text, moves):
    dance = list(text)
    for line in moves:
        if line[0] == "s":
            offset = int(line[1:])
            dance = dance[-offset:]+dance[:-offset]
        elif line[0] == "x":
            temp = re.match("x(\d+)/(\d+)",line)
            pos1, pos2 = int(temp[1]), int(temp[2])
            dance[pos1], dance[pos2] = dance[pos2], dance[pos1]
        elif line[0] == "p":
            pos1, pos2  = dance.index(line[1]), dance.index(line[3])
            dance[pos1], dance[pos2] = dance[pos2], dance[pos1]
    return "".join(dance)


move_list = open("input").read().strip().split(",")
print(get_dance("abcdefghijklmnop", move_list))
