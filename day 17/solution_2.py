f = int(open("input").read().strip())
current = 0
s = 1
answer = 0
for i in range(1,50000001):
    current = (current + f) % s + 1
    if current == 1:
        answer = i
    s += 1
print(answer)
