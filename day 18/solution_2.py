import re
f = open("input").read().strip().split("\n")

t = list("qwertyuioplkjhgfdsazxcvbnm")
r1 = {}
r2 = {}
for x in t:
    r1[x] = 0
    r2[x] = 0
r2["p"] = 1

q1 = []
q2 = []
i = 0
j = 0
r = r1
program = 1
answer = 0
while True:
    #print(program, len(q1),len(q2))
    line = f[i]
    com = line[:3]
    reg = line[4:5]
    value = line[6:]
    if (re.match("-?\d+",value) != None):
        value = int(value)
    elif (re.match("[a-z]+",value) != None):
        value = r[value]
    #print(com,reg, value)
    if (com == "snd"):
        if (program == 1):
            q2.append(r[reg])
        else:
            q1.append(r[reg])
            answer += 1
    if (com == "set"):
        r[reg] = value
    if (com == "add"):
        r[reg] += value
    if (com == "mul"):
        r[reg] *= value
    if (com == "mod"):
        r[reg] %= value
    if (com == "rcv"):
        if (len(q1) == 0 and len(q2) == 0):
            print(answer)
            break
        if (program == 1):
            if len(q1) > 0:
                r[reg] = q1[0]
                del q1[0]
            else:
                i, j = j, i
                program = 2
                r = r2
                continue
        else:
            if len(q2) > 0:
                r[reg] = q2[0]
                del q2[0]
            else:
                i, j = j, i
                program = 1
                r = r1
                continue

    if com == "jgz" and ((reg in r and r[reg] > 0) or not(reg in r)):
        i += int(value)
        continue
    i += 1
