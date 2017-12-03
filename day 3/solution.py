import math

number = int(open("input").read())

p = int(math.sqrt(number))

if p * p == number:
    answer = p - 1
else:
    p += 1
    s = p // 2
    answer = s + s - (p * p - number)

print(answer)
