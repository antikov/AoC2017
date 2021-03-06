def main(file, iterations):
    start = ".#./..#/###".split('/')

    patterns = {}  # key has no slashes
    for line in file:
        from_, to = line.split(' => ')
        f = from_.split('/')
        to = to.split('/')
        for _ in range(4):
            patterns[''.join(map(''.join, f))] = to
            patterns[''.join(''.join(r[::-1]) for r in f)] = to
            f = list(zip(*f[::-1]))

    for _ in range(iterations):
        if len(start) % 2 == 0:
            jmp = 2
        else:
            jmp = 3

        rows = []
        for y in range(0, len(start), jmp):
            rows.extend([] for _ in range(jmp + 1))
            for x in range(0, len(start), jmp):
                key = ''.join(start[y+dy][x+dx] for dy in range(jmp) for dx in range(jmp))
                for i, row in enumerate(patterns[key], -jmp - 1):
                    rows[i].extend(row)
        start = rows
    # for row in rows:
    #     print(''.join(row))
    return sum(e == '#' for row in rows for e in row)


file = open("input.txt").read().strip().split("\n")
print(main(file, 5))  # part 1
print(main(file, 18))  # part 2. Takes ~7 seconds
