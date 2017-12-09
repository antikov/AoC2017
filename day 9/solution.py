def delete_garbage(text):
    while text.find("!") > -1:
        x = text.find("!")
        text = text[:x] + text[x+2:]
    count = 0
    while True:
        start = text.find("<")
        end = text.find(">")
        while start > end:
            start = text.find("<",start)
            end = text.find(">",start)
        if start == -1 or end == -1:
            break
        count += end - start - 1
        text = text[:start] + text[end:]
    return text, count

def count_groups(text):
    count = 0
    current = 0
    for i in range(len(text)):
        if text[i] == "{" :
            current += 1
        if text[i] == "}" :
            count += current
            current -= 1
    return count

f = open("input").read().strip()
f,d = delete_garbage(f)
print(count_groups(f),d)
