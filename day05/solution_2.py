jump = list(map(int,open("input").read().strip().split("\n")))

steps = 0
index = 0
while index >= 0 and index < len(jump):
    start = index
    index += jump[start]
    jump[start] += 1 if jump[start] < 3 else -1
    steps += 1
print(steps)
