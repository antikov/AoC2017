f = open("input").read().strip().split("\n")

jump = list(map(int,f))

print(jump)

start = 0
steps = 0
i = 0
while True:
    start = i
    i += jump[i]

    steps += 1
    if i < 0 or i >= len(jump):
        break
    if jump[start] >= 3:
        jump[start] -= 1
    else:
        jump[start] += 1
print(steps)
