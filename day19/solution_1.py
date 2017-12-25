f = open("input").read().split("\n")

arr = []
for line in f:
    arr.append(" "+line+" ")
i = 0
j = arr[0].find("|")
let = "QWERTYUIOPLKJHGFDSAZXCVBNM"
answer = ""
di = {"U":(-1,0), "D":(1,0), "L":(0,-1),"R":(0,1)}
d = "D"
steps = 0
while True:
    while arr[i][j] != "+" and arr[i][j] != " ":
        if arr[i][j] != "|" and arr[i][j] != "+" and arr[i][j] != "-":
            answer += arr[i][j]
            if (arr[i][j] == "T"):
                quit()
        i += di[d][0]
        j += di[d][1]
        steps += 1
    if (d == "D" or d == "U"):
        if arr[i][j - 1] == "-" or let.find(arr[i][j-1]) != -1:
            d = "L"
        elif arr[i][j + 1] == "-" or let.find(arr[i][j+1]) != -1:
            d = "R"
        else:
            break
    else:
        if arr[i - 1][j] == "|" or let.find(arr[i - 1][j]) != -1:
            d = "U"
        elif arr[i + 1][j] == "|" or let.find(arr[i + 1][j]) != -1:
            d = "D"
        else:
            break
    i += di[d][0]
    j += di[d][1]
    steps += 1

print("Part 1:",answer)
print("Part 2",steps)
