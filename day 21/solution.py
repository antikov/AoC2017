def get_text(*arr):
    return "/".join(arr)

def allvars(input):
    output = [input]
    x = input.split("/")
    if len(x[0]) == 2:
        f = get_text(x[1][0]+x[0][0],x[1][1]+x[0][1])
        f = f.split("/")
        output.append(get_text(x[1],x[0]))
        output.append(get_text(x[0][::-1],x[1][::-1]))
        output.append(get_text(x[1][::-1],x[0][::-1]))
        output.append(get_text(f[0],f[1]))
        output.append(get_text(f[1],f[0]))
        output.append(get_text(f[0][::-1],f[1][::-1]))
        output.append(get_text(f[1][::-1],f[0][::-1]))
    if len(x[0]) == 3:
        f = get_text(x[2][0]+x[1][0]+x[0][0],x[2][1]+x[1][1]+x[0][1],x[2][2]+x[1][2]+x[0][2])
        f = f.split("/")
        output.append(get_text(x[2],x[1],x[0]))
        output.append(get_text(x[0][::-1],x[1][::-1],x[2][::-1]))
        output.append(get_text(x[2][::-1],x[1][::-1],x[0][::-1]))
        output.append(get_text(f[0],f[1],f[2]))
        output.append(get_text(f[2],f[1],f[0]))
        output.append(get_text(f[0][::-1],f[1][::-1],f[2][::-1]))
        output.append(get_text(f[2][::-1],f[1][::-1],f[0][::-1]))
    return output

print(allvars("x"))

def is_match(text,pattern):
    x = allvars(text)
    #print(pattern,x)
    if pattern in x:
        return True
    return False

def find_pattern(text,s,d):
    for i in range(len(s)):
        if is_match(text,s[i]):
            #print("MATCH")
            return d[i]
    return ""

import re
f = open("input.test").read().strip().split("\n")

img = ".#./..#/###"

rules = []
s = []
d = []
for line in f:
    temp = line.split(" => ")
    s.append(temp[0])
    d.append(temp[1])

for q in range(2):
    img = img.split("/")
    newimg = ""
    i = 0
    size = len(img[0])
    #print(size,len(img),img)
    while i < len(img):
        if size  == 2:
            newimg += find_pattern(get_text(img[i],img[i+1]),s,d) + "/"
            i += 2
        elif size == 3:
            hec = find_pattern(get_text(img[i],img[i+1],img[i+2]),s,d)
            print("HEC",hec)
            #..#/..../..../#..#
            hec = hec.split("/")
            newimg += get_text(hec[0][:2]+hec[1][:2],hec[0][2:]+hec[1][2:],hec[2][:2]+hec[3][:2],hec[2][2:]+hec[3][2:])+"/"
            #newimg += find_pattern(get_text(img[i],img[i+1],img[i+2]),s,d) + "/"
            i += 3
        elif size == 4:
            newimg += find_pattern(get_text(img[i][:2],img[i][2:]),s,d) + "/"
            i += 1
        else:
            print("ERROR SIZE",size)
    img = newimg[:-1]
    print("Newimg",img)
print(img)
print(img.count("#"))
