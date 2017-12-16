f = open("input").read().strip().split("\n")
count = 0
for line in f:
    words = line.split()
    dic = dict.fromkeys(words)
    if len(dic) == len(words):
        count += 1
print (count)
