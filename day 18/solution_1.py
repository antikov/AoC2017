import re
f = open("input").read().strip().split("\n")

print(f)
i = 0
t = list("qwertyuioplkjhgfdsazxcvbnm")
for x in t:
    r[x] = 0
lastsound = 0
while True:
    line = f[i]
    print(line)
    com = line[:3]
    reg = line[4:5]
    value = line[6:]
    if (re.match("-?\d+",value) != None):
        value = int(value)
    elif (re.match("[a-z]+",value) != None):
        value = r[value]
    print(com,reg, value)
    if (com == "snd"):
        lastsound = r[reg]
    if (com == "set"):
        r[reg] = value
    if (com == "add"):
        r[reg] += value
    if (com == "mul"):
        r[reg] *= value
    if (com == "mod"):
        r[reg] %= value
    if (com == "rcv" and lastsound != 0):
        print(lastsound)
        break
    if com == "jgz" and ((reg in r and r[reg] != 0) or (int(reg) > 0)):
        i += int(value)
        continue
    i += 1
