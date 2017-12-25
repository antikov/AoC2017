import re
f = open("input").read().strip().split("\n")

maxvalue = 0

# yg inc 559 if nwe > 189
registers = {}
for line in f:
    parse = re.match(r'^([a-z]+) ([a-z]+) (-?[0-9]+) if ([a-z]+) ([><!=]+) (-?[0-9]+)', line)
    reg = parse.group(1)
    op = parse.group(2)
    value = int(parse.group(3))
    ifreg = parse.group(4)
    cmp = parse.group(5)
    cmpvalue = int(parse.group(6))

    if reg not in registers:
        registers[reg] = 0

    if ifreg not in registers:
        registers[ifreg] = 0

    if op == "dec":
        value = -value

    if eval(str(registers[ifreg])+cmp+str(cmpvalue)):
        registers[reg] += value
        maxvalue = registers[reg] if registers[reg] > maxvalue else maxvalue

print("Part 1: ",max(registers.values()))
print("Part 2: ", maxvalue)
