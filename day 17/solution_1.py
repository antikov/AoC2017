f = int(open("input").read().strip())
s = [0]
current = 0
for i in range(1,2018):
    current = (current + f) % len(s) + 1
    s.insert(current, i)
print(s[s.index(2017)+1])
