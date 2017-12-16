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

def get_cycle_count(text, moves):
    unique = {}
    i = 0
    while not text in unique:
        unique[text] = i
        text = get_dance(text, moves)
        i += 1
    return 1000000000 % (i - unique[text])


move_list = open("input").read().strip().split(",")
text = "abcdefghijklmnop"
count = get_cycle_count(text, move_list)
for i in range(count):
    text = get_dance(text, move_list)
print (text)
