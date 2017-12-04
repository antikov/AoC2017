def is_anagram(word1, word2):
    w1 = list(word1)
    w2 = list(word2)
    w1.sort()
    w2.sort()
    if w1 == w2:
        return True
    return False

f = open("input").read().strip().split("\n")
count = 0
for line in f:
    d = line.split(" ")
    has_anagram = False
    for i in range(0,len(d)):
        for j in range(0, len(d)):
            if i != j and is_anagram(d[i],d[j]):
                has_anagram = True
    if not has_anagram:
        count += 1
print (count)
